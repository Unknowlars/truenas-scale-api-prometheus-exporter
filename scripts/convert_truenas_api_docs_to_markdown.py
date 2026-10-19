#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shlex
import shutil
import stat
import tempfile
from collections.abc import Iterable
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen
from zipfile import ZipFile

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError as exc:  # pragma: no cover - user-facing dependency error
    raise SystemExit(
        "Missing dependency: beautifulsoup4. Install it with `pip install -r requirements-dev.txt`."
    ) from exc

try:
    from .tooling import TRUENAS_API_VERSION
except ImportError:  # direct script execution
    from tooling import TRUENAS_API_VERSION


SHARED_DOCS = {
    "jsonrpc": "JSON-RPC 2.0 over WebSocket API",
    "query_methods": "Query Methods",
    "jobs": "Jobs",
}

TOKEN_PARAM_RE = re.compile(
    r"\b(auth_token|access_token|refresh_token|api_key|apikey|token)="
    r"[A-Za-z0-9_-]{20,}\b",
    re.IGNORECASE,
)
BEARER_TOKEN_RE = re.compile(r"\bBearer\s+[A-Za-z0-9._-]{20,}\b")

@dataclass
class Page:
    kind: str
    title: str
    source_stem: str
    source_path: Path
    html_path: Path
    is_leaf: bool
    summary: list[str] = field(default_factory=list)
    required_roles: list[str] = field(default_factory=list)
    schema_html: str = ""
    children: list[str] = field(default_factory=list)

    @property
    def output_name(self) -> str:
        return self.title


def split_paragraphs(lines: Iterable[str]) -> list[str]:
    paragraphs: list[list[str]] = []
    current: list[str] = []
    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip():
            if current:
                paragraphs.append(current)
                current = []
            continue
        current.append(line)
    if current:
        paragraphs.append(current)

    rendered: list[str] = []
    for paragraph_lines in paragraphs:
        if all(line.lstrip().startswith(("- ", "* ")) for line in paragraph_lines):
            rendered.extend(normalize_rst_inline(line.strip()) for line in paragraph_lines)
        else:
            rendered.append(normalize_rst_inline(" ".join(line.strip() for line in paragraph_lines)))
    return rendered


def normalize_rst_inline(text: str) -> str:
    text = re.sub(r":doc:`([^`<>]+) <([^`<>]+)>`", r"[\1](\2.html)", text)
    text = re.sub(r":ref:`(uploading-files)`", r"[\1](jobs.html#\1)", text)
    text = text.replace("``", "`")
    text = text.replace("‘", "'").replace("’", "'")
    text = text.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def parse_toctree_entries(text: str) -> list[str]:
    lines = text.splitlines()
    entries: list[str] = []
    in_toctree = False
    for line in lines:
        stripped = line.strip()
        if stripped == ".. toctree::":
            in_toctree = True
            continue
        if not in_toctree:
            continue
        if not stripped:
            continue
        if not line.startswith("   "):
            break
        if stripped.startswith(":"):
            continue
        entries.append(stripped)
    return entries


def parse_leaf_page(kind: str, source_path: Path, html_path: Path) -> Page:
    text = source_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = lines[0].strip()

    raw_index = None
    for idx, line in enumerate(lines):
        if line.strip() == ".. raw:: html":
            raw_index = idx
            break
    if raw_index is None:
        raise ValueError(f"Expected raw HTML schema block in {source_path}")

    body_lines = lines[2:raw_index]
    summary = split_paragraphs(body_lines)

    schema_lines: list[str] = []
    for line in lines[raw_index + 1 :]:
        if line.startswith("    ") or not line.strip():
            schema_lines.append(line[4:] if line.startswith("    ") else "")
            continue
        break
    schema_html = "\n".join(schema_lines).strip()

    required_roles: list[str] = []
    match = re.search(r"^\*Required roles:\*\s*(.*)$", text, flags=re.MULTILINE)
    if match:
        roles_text = match.group(1).strip()
        if roles_text:
            required_roles = [role.strip() for role in re.split(r"[,|]", roles_text) if role.strip()]

    return Page(
        kind=kind,
        title=title,
        source_stem=source_path.name.replace(".rst.txt", ""),
        source_path=source_path,
        html_path=html_path,
        is_leaf=True,
        summary=summary,
        required_roles=required_roles,
        schema_html=schema_html,
    )


def parse_namespace_page(kind: str, source_path: Path, html_path: Path) -> Page:
    text = source_path.read_text(encoding="utf-8")
    return Page(
        kind=kind,
        title=text.splitlines()[0].strip(),
        source_stem=source_path.name.replace(".rst.txt", ""),
        source_path=source_path,
        html_path=html_path,
        is_leaf=False,
        children=parse_toctree_entries(text),
    )


def build_pages(source_root: Path) -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for prefix, kind in (("api_methods_", "method"), ("api_events_", "event")):
        for source_path in sorted((source_root / "_sources").glob(f"{prefix}*.rst.txt")):
            html_path = source_root / source_path.name.replace(".rst.txt", ".html")
            text = source_path.read_text(encoding="utf-8")
            if ".. raw:: html" in text:
                page = parse_leaf_page(kind, source_path, html_path)
            else:
                page = parse_namespace_page(kind, source_path, html_path)
            pages[page.source_stem] = page
    return pages


def make_output_path(output_root: Path, page: Page) -> Path:
    base = output_root / ("methods" if page.kind == "method" else "events")
    if not re.fullmatch(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*", page.output_name):
        raise ValueError(f"Unsafe API page title: {page.output_name!r}")
    parts = page.output_name.split(".")
    if page.is_leaf:
        if len(parts) == 1:
            return base / f"{parts[0]}.md"
        return base.joinpath(*parts[:-1], f"{parts[-1]}.md")
    return base.joinpath(*parts, "index.md")


def render_frontmatter(mapping: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in mapping.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            if value:
                for item in value:
                    lines.append(f"  - {item}")
            else:
                lines.append("  []")
            continue
        lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def render_leaf_markdown(page: Page, source_root: Path, output_root: Path) -> str:
    output_path = make_output_path(output_root, page)
    query_link = None
    jsonrpc_link = relative_link(output_path, output_root / "shared" / "jsonrpc.md")
    if page.output_name.endswith(".query"):
        query_link = relative_link(output_path, output_root / "shared" / "query_methods.md")

    frontmatter = render_frontmatter(
        {
            "title": page.output_name,
            "kind": page.kind,
            "source_rst": page.source_path.relative_to(source_root),
            "source_html": page.html_path.relative_to(source_root),
            "required_roles": page.required_roles,
        }
    )

    lines = [frontmatter, "", f"# {page.output_name}", ""]

    if page.summary:
        lines.extend(["## Summary", ""])
        for paragraph in page.summary:
            lines.append(paragraph)
            lines.append("")

    lines.extend(["## Required Roles", ""])
    if page.required_roles:
        lines.extend(f"- `{role}`" for role in page.required_roles)
    else:
        lines.append("- None documented.")
    lines.append("")

    if page.schema_html:
        lines.extend(["## Schema", ""])
        lines.extend(render_schema_fragment(page.schema_html))
        lines.append("")

    lines.extend(["## Related Docs", "", f"- JSON-RPC transport: [{SHARED_DOCS['jsonrpc']}]({jsonrpc_link})"])
    if query_link:
        lines.append(f"- Query filters and options: [{SHARED_DOCS['query_methods']}]({query_link})")
    lines.append("")

    return "\n".join(trim_blank_lines(lines)).rstrip() + "\n"


def trim_blank_lines(lines: list[str]) -> list[str]:
    trimmed: list[str] = []
    previous_blank = False
    for line in lines:
        is_blank = not line.strip()
        if is_blank and previous_blank:
            continue
        trimmed.append(line.rstrip())
        previous_blank = is_blank
    while trimmed and not trimmed[0].strip():
        trimmed.pop(0)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()
    return trimmed


def schema_anchor(node: Tag | None) -> list[str]:
    if node is not None and node.get("id"):
        return [f'<a id="{html.escape(str(node["id"]), quote=True)}"></a>']
    return []


def render_schema_fragment(fragment: str) -> list[str]:
    soup = BeautifulSoup(fragment, "html.parser")
    root = soup.find(id="json-schema") or soup
    lines: list[str] = []

    root_type = first_badge_value(root, recursive=False)
    if root_type:
        lines.append(f"- Type: {root_type}")
        lines.append("")

    for accordion in root.find_all("div", class_="accordion", recursive=False):
        for card in accordion.find_all("div", class_="card", recursive=False):
            lines.extend(render_schema_card(card, level=3))
            lines.append("")

    return trim_blank_lines(lines)


def render_schema_card(card: Tag, level: int) -> list[str]:
    header = card.find("div", class_="card-header", recursive=False)
    body_wrapper = None
    if header is not None:
        body_wrapper = header.find_next_sibling("div")
    if body_wrapper is None:
        body_wrapper = card.find("div", class_="card-body", recursive=False)

    name = "Section"
    required = False
    if header is not None:
        name_tag = header.find("span", class_="property-name")
        if name_tag is not None:
            name = clean_inline_text(name_tag)
        required = header.find("span", class_="required-property") is not None

    heading = f"{'#' * min(level, 6)} {name}"
    if required:
        heading += " (required)"

    lines = schema_anchor(header) + schema_anchor(body_wrapper) + [heading, ""]
    body = None
    if isinstance(body_wrapper, Tag):
        body = body_wrapper.find("div", class_="card-body", recursive=False) or body_wrapper
    if isinstance(body, Tag):
        lines.extend(render_schema_body(body, level + 1))
    return trim_blank_lines(lines)


def render_schema_body(body: Tag, level: int) -> list[str]:
    lines: list[str] = []
    for child in direct_tag_children(body):
        child_classes = set(child.get("class", []))

        if child.name == "h4":
            lines.append(f"- Schema name: `{clean_inline_text(child)}`")
        elif child.name == "span" and "value-type" in child_classes:
            value = clean_inline_text(child)
            if value.startswith("Type:"):
                lines.append(f"- {value}")
            else:
                lines.append(f"- Type: {value}")
        elif child.name == "span" and child_classes & {"default-value", "no-additional", "const-value", "pattern-value", "restriction"}:
            lines.append(f"- {clean_inline_text(child)}")
        elif child.name == "span" and "description" in child_classes:
            text = clean_inline_text(child)
            if text:
                lines.extend(["", text])
        elif child.name == "div" and "json-default-value" in child_classes:
            label = child.find("div", class_="value")
            lines.append("- Default:")
            if label is not None:
                lines.extend(code_fence(block_text(label), "json"))
        elif child.name == "p":
            restriction_spans = child.find_all("span", class_="restriction")
            if restriction_spans:
                for span in restriction_spans:
                    lines.append(f"- {clean_inline_text(span)}")
            else:
                text = clean_inline_text(child)
                if text:
                    lines.extend(["", text])
        elif child.name == "h5":
            lines.extend(["", f"{'#' * min(level, 6)} {clean_inline_text(child)}", ""])
        elif child.name == "div" and "accordion" in child_classes:
            for nested in child.find_all("div", class_="card", recursive=False):
                lines.extend(render_schema_card(nested, level=level))
                lines.append("")
        elif child.name == "div" and "card" in child_classes:
            lines.extend(render_inline_schema_card(child, level=level))
            lines.append("")
        elif child.name == "div" and child_classes & {"any-of-value", "one-of-value"}:
            lines.extend(render_any_of(child, level=level))
            lines.append("")
        elif child.name == "div" and "enum-value" in child_classes:
            lines.extend(render_schema_body(child, level=level))
        elif child.name == "div" and "examples" in child_classes:
            lines.extend(render_example_block(child))
        elif child.name == "div" and "tab-content" in child_classes:
            for pane in child.find_all("div", class_="tab-pane", recursive=False):
                lines.extend(render_schema_body(pane, level=level))
        elif child.name == "ul":
            lines.extend(render_html_list(child))

    return trim_blank_lines(lines)


def render_inline_schema_card(card: Tag, level: int) -> list[str]:
    if card.find("div", class_="card-header", recursive=False):
        return render_schema_card(card, level=level)

    body = card.find("div", class_="card-body", recursive=False)
    if body is None:
        return []

    title = body.find("h4", recursive=False)
    lines: list[str] = schema_anchor(body)
    if title is not None:
        lines.extend([f"{'#' * min(level, 6)} {clean_inline_text(title)}", ""])
    lines.extend(render_schema_body(body, level + 1))
    return trim_blank_lines(lines)


def render_any_of(node: Tag, level: int) -> list[str]:
    choice = "One of" if "one-of-value" in node.get("class", []) else "Any of"
    lines = schema_anchor(node) + [f"{'#' * min(level, 6)} {choice}", ""]
    navigation = node.find("ul", recursive=False)
    labels = [clean_inline_text(link) for link in navigation.select(".nav-link")] if navigation else []
    tabs = node.find("div", class_="tab-content", recursive=False)
    panes = tabs.find_all("div", class_="tab-pane", recursive=False) if tabs else []
    for index, pane in enumerate(panes, start=1):
        label = labels[index - 1] if index - 1 < len(labels) and labels[index - 1] else f"Option {index}"
        lines.extend(schema_anchor(pane) + [f"{'#' * min(level + 1, 6)} {label}", ""])
        lines.extend(render_schema_body(pane, level + 2))
        lines.append("")
    return trim_blank_lines(lines)


def render_example_block(node: Tag) -> list[str]:
    pre = node.find("pre")
    if pre is None:
        return []
    code = code_text(pre)
    if not code:
        return []
    return ["Examples:", ""] + code_fence(code, "json")


def first_badge_value(node: Tag, recursive: bool) -> str:
    badge = node.find("span", class_="value-type", recursive=recursive)
    if badge is None:
        return ""
    return clean_inline_text(badge).removeprefix("Type:").strip()


def direct_tag_children(node: Tag) -> list[Tag]:
    return [child for child in node.children if isinstance(child, Tag)]


def block_text(node: Tag) -> str:
    text = html.unescape(node.get_text("\n", strip=False))
    text = text.replace("\xa0", " ")
    text = text.replace("¶", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n")


def code_text(node: Tag) -> str:
    text = html.unescape(node.get_text("", strip=False))
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\xa0", " ")
    text = TOKEN_PARAM_RE.sub(lambda match: f"{match.group(1)}={{token}}", text)
    text = BEARER_TOKEN_RE.sub("Bearer {token}", text)
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines)


def clean_inline_text(node: Tag | NavigableString | str) -> str:
    if isinstance(node, str):
        text = node
    elif isinstance(node, NavigableString):
        text = str(node)
    else:
        text = render_inline(node)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")
    text = text.replace("¶", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def render_inline(node: Tag | NavigableString) -> str:
    if isinstance(node, NavigableString):
        return str(node)

    classes = set(node.get("class", []))
    if "headerlink" in classes:
        return ""
    if node.name == "code":
        inner = clean_inline_text(node.get_text("", strip=False))
        return f"`{inner}`" if inner else ""
    if node.name in {"em", "i"}:
        return f"*{''.join(render_inline(child) for child in node.children).strip()}*"
    if node.name in {"strong", "b"}:
        return f"**{''.join(render_inline(child) for child in node.children).strip()}**"
    if node.name == "a":
        label = "".join(render_inline(child) for child in node.children)
        href = node.get("href", "")
        return f"[{label}]({href})" if href and label else label
    if node.name == "br":
        return "\n"
    if node.name == "span" and "pre" in classes:
        return node.get_text("", strip=False)
    return "".join(render_inline(child) for child in node.children)


def code_fence(code: str, language: str) -> list[str]:
    return [f"```{language}", code.rstrip(), "```"]


def relative_link(from_path: Path, to_path: Path) -> str:
    return str(Path(os.path.relpath(to_path, from_path.parent))).replace("\\", "/")


def render_shared_doc(title: str, html_path: Path, output_path: Path, source_root: Path) -> str:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")
    body = soup.select_one("div.bodywrapper > div.body")
    if body is None:
        raise ValueError(f"Could not locate main article body in {html_path}")

    frontmatter = render_frontmatter(
        {
            "title": title,
            "kind": "shared",
            "source_html": html_path.relative_to(source_root),
        }
    )

    lines = [frontmatter, ""]
    lines.extend(render_html_children(body.children, base_level=1))
    return "\n".join(trim_blank_lines(lines)).rstrip() + "\n"


def render_html_children(children: Iterable[object], base_level: int) -> list[str]:
    lines: list[str] = []
    for child in children:
        if not isinstance(child, Tag):
            continue
        child_classes = set(child.get("class", []))
        if child.name == "section":
            lines.extend(schema_anchor(child))
            lines.extend(render_html_children(child.children, base_level=base_level))
        elif re.fullmatch(r"h[1-6]", child.name or ""):
            heading_level = min(base_level + int(child.name[1]) - 1, 6)
            lines.extend([f"{'#' * heading_level} {clean_inline_text(child)}", ""])
        elif child.name == "span" and child.get("id"):
            lines.extend(schema_anchor(child))
        elif child.name == "p":
            text = clean_inline_text(child)
            if text:
                lines.extend([text, ""])
        elif child.name in {"ul", "ol"}:
            lines.extend(render_html_list(child))
            lines.append("")
        elif child.name == "table":
            lines.extend(render_html_table(child))
            lines.append("")
        elif child.name == "div" and any(name.startswith("highlight") for name in child_classes):
            lines.extend(render_html_codeblock(child))
            lines.append("")
        elif child.name == "div" and "literal-block-wrapper" in child_classes:
            lines.extend(schema_anchor(child))
            caption = child.select_one(".caption-text")
            if caption is not None:
                lines.extend([clean_inline_text(caption), ""])
            lines.extend(render_html_children(child.children, base_level=base_level))
        elif child.name == "div" and "admonition" in child_classes:
            lines.extend(render_admonition(child))
            lines.append("")
        elif child.name == "div" and "line-block" in child_classes:
            for line in child.select(".line"):
                text = clean_inline_text(line)
                if text:
                    lines.append(text)
            lines.append("")
    return trim_blank_lines(lines)


def render_html_list(node: Tag) -> list[str]:
    lines: list[str] = []
    ordered = node.name == "ol"
    for index, item in enumerate(node.find_all("li", recursive=False), start=1):
        prefix = f"{index}." if ordered else "-"
        text = clean_inline_text(item)
        if text:
            lines.append(f"{prefix} {text}")
    return lines


def render_html_table(table: Tag) -> list[str]:
    lines: list[str] = []
    caption = table.find("caption")
    if caption is not None:
        lines.append(clean_inline_text(caption))
        lines.append("")

    headers = [escape_pipe(clean_inline_text(cell)) for cell in table.select("thead th")]
    if not headers:
        first_row = table.find("tr")
        if first_row is not None:
            headers = [escape_pipe(clean_inline_text(cell)) for cell in first_row.find_all(["th", "td"], recursive=False)]

    if headers:
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join("---" for _ in headers) + " |")

    body_rows = table.select("tbody tr") or table.find_all("tr")
    for row in body_rows:
        cells = [escape_pipe(clean_inline_text(cell)) for cell in row.find_all(["th", "td"], recursive=False)]
        if cells == headers:
            continue
        if cells:
            lines.append("| " + " | ".join(cells) + " |")
    return lines


def render_html_codeblock(node: Tag) -> list[str]:
    classes = node.get("class", [])
    language = "text"
    for class_name in classes:
        if class_name.startswith("highlight-"):
            language = class_name.split("-", 1)[1]
            break
    pre = node.find("pre")
    if pre is None:
        return []
    return code_fence(code_text(pre), language)


def render_admonition(node: Tag) -> list[str]:
    title = node.find(class_="admonition-title")
    title_text = clean_inline_text(title) if title is not None else "Note"
    body_parts: list[str] = []
    for child in node.children:
        if not isinstance(child, Tag):
            continue
        if title is not None and child == title:
            continue
        if child.name == "p":
            text = clean_inline_text(child)
            if text:
                body_parts.append(text)
    if body_parts:
        return [f"> **{title_text}** {body_parts[0]}"] + [f"> {part}" for part in body_parts[1:]]
    return [f"> **{title_text}**"]


def escape_pipe(text: str) -> str:
    return text.replace("|", "\\|")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_index_page(title: str, intro: str, entries: list[tuple[str, str]]) -> str:
    lines = [f"# {title}", "", intro, ""]
    for label, href in entries:
        lines.append(f"- [{label}]({href})")
    return "\n".join(lines).rstrip() + "\n"


def convert(
    source_root: Path, output_root: Path, clean: bool, *,
    api_version: str | None = None, source_url: str = "", retrieved_at: str = "",
    archive_sha256: str = "", archive_path: Path | None = None, check: bool = False,
) -> None:
    if output_root.exists():
        resolved = output_root.resolve()
        protected = {
            Path("/").resolve(),
            Path.home().resolve(),
            Path.cwd().resolve(),
            source_root.resolve(),
            source_root.resolve().parent,
        }
        if resolved in protected or len(resolved.parts) < 3 or source_root.resolve().is_relative_to(resolved):
            raise ValueError(f"Refusing unsafe --clean output path: {resolved}")
    if api_version:
        date.fromisoformat(retrieved_at)
        parsed_url = urlsplit(source_url)
        if parsed_url.scheme not in {"http", "https"} or parsed_url.username or parsed_url.password:
            raise ValueError("Source URL must be a public HTTP(S) URL without credentials")
        index = source_root / "index.html"
        if index.is_file():
            match = re.search(r"TrueNAS API v([0-9.]+)", index.read_text(encoding="utf-8"))
            if match and match.group(1) != api_version:
                raise ValueError(f"Served API version {match.group(1)} differs from requested version {api_version}")
    output_root.parent.mkdir(parents=True, exist_ok=True)
    temporary_parent = None if check else output_root.parent
    with tempfile.TemporaryDirectory(prefix="api-docs-", dir=temporary_parent) as temporary:
        staged = Path(temporary) / "snapshot"
        if not clean and not check and output_root.exists():
            for existing in output_root.rglob("*"):
                if existing.is_file():
                    destination = staged / existing.relative_to(output_root)
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(existing, destination)
        render_snapshot(source_root, staged)
        if api_version:
            augment_snapshot(source_root, staged, api_version, source_url, retrieved_at, archive_sha256, output_root, archive_path)
        if check:
            expected = {p.relative_to(staged): p.read_bytes() for p in staged.rglob("*") if p.is_file()}
            actual = {p.relative_to(output_root): p.read_bytes() for p in output_root.rglob("*") if p.is_file()}
            if expected != actual:
                raise ValueError("Generated API documentation is out of date")
            return
        previous = Path(temporary) / "previous"
        if output_root.exists():
            output_root.rename(previous)
        try:
            staged.rename(output_root)
        except OSError:
            if previous.exists():
                previous.rename(output_root)
            raise


def render_snapshot(source_root: Path, output_root: Path) -> None:
    pages = build_pages(source_root)
    if not pages:
        raise ValueError(f"No API source pages found in {source_root}")
    destinations: set[str] = {"methods/index.md", "events/index.md"}
    for page in pages.values():
        destination = make_output_path(output_root, page)
        normalized_destination = destination.relative_to(output_root).as_posix().casefold()
        if normalized_destination in destinations:
            raise ValueError(f"Duplicate output path: {destination}")
        destinations.add(normalized_destination)
        if not page.html_path.is_file():
            raise ValueError(f"Missing source HTML page: {page.html_path}")
        missing = set(page.children) - pages.keys()
        if missing:
            raise ValueError(f"Missing toctree pages in {page.source_stem}: {sorted(missing)}")
    leaf_pages = [page for page in pages.values() if page.is_leaf]
    namespace_pages = [page for page in pages.values() if not page.is_leaf]

    for page in leaf_pages:
        output_path = make_output_path(output_root, page)
        write_text(output_path, render_leaf_markdown(page, source_root, output_root))

    for page in namespace_pages:
        entries: list[tuple[str, str]] = []
        namespace_output = make_output_path(output_root, page)
        for child_stem in page.children:
            child = pages.get(child_stem)
            if child is None:
                continue
            child_output = make_output_path(output_root, child)
            entries.append((child.output_name, relative_link(namespace_output, child_output)))
        intro = f"AI-friendly Markdown index for the `{page.output_name}` {page.kind} namespace."
        write_text(namespace_output, build_index_page(page.output_name, intro, entries))

    for stem, title in SHARED_DOCS.items():
        html_path = source_root / f"{stem}.html"
        output_path = output_root / "shared" / f"{stem}.md"
        write_text(output_path, render_shared_doc(title, html_path, output_path, source_root))

    method_root = output_root / "methods" / "index.md"
    event_root = output_root / "events" / "index.md"
    method_entries: list[tuple[str, str]] = []
    event_entries: list[tuple[str, str]] = []
    for page in sorted(namespace_pages, key=lambda item: item.output_name):
        if "." in page.output_name:
            continue
        page_output = make_output_path(output_root, page)
        target_entries = method_entries if page.kind == "method" else event_entries
        root_path = method_root if page.kind == "method" else event_root
        target_entries.append((page.output_name, relative_link(root_path, page_output)))

    write_text(
        method_root,
        build_index_page(
            "Methods",
            "Namespace index for converted TrueNAS API method docs.",
            method_entries,
        ),
    )
    write_text(
        event_root,
        build_index_page(
            "Events",
            "Namespace index for converted TrueNAS API event docs.",
            event_entries,
        ),
    )

    shared_root = output_root / "shared" / "index.md"
    shared_entries = []
    for stem, title in SHARED_DOCS.items():
        shared_entries.append((title, relative_link(shared_root, output_root / "shared" / f"{stem}.md")))
    write_text(
        shared_root,
        build_index_page(
            "Shared Guides",
            "General API behavior references that apply across multiple methods and events.",
            shared_entries,
        ),
    )

    readme = output_root / "README.md"
    write_text(
        readme,
        "\n".join(
            [
                "# TrueNAS API Markdown Export",
                "",
                "This directory contains an AI-friendly Markdown conversion of the offline TrueNAS API docs.",
                "",
                "## Layout",
                "",
                "- `methods/`: converted API method namespaces and leaf pages",
                "- `events/`: converted API event namespaces and leaf pages",
                "- `shared/`: JSON-RPC, query behavior, and job guides",
                "",
                "## Regenerate",
                "",
                "```bash",
                "python scripts/convert_truenas_api_docs_to_markdown.py --clean",
                "```",
                "",
                "The converter reads from `_sources/*.rst.txt` for page metadata and parses each embedded `#json-schema` block into Markdown headings, bullets, and examples.",
                "",
                "## Entry Points",
                "",
                "- [Methods](methods/index.md)",
                "- [Events](events/index.md)",
                "- [Shared Guides](shared/index.md)",
                "",
            ]
        ),
    )



def augment_snapshot(
    source_root: Path, output_root: Path, api_version: str, source_url: str,
    retrieved_at: str, archive_sha256: str, destination_root: Path, archive_path: Path | None,
) -> None:
    """Add complete versioned provenance while preserving the legacy converter layout."""
    pages = build_pages(source_root)
    links = {f"{page.source_stem}.html": make_output_path(output_root, page) for page in pages.values()}
    links.update({"api_methods.html": output_root / "methods/index.md",
                  "api_events.html": output_root / "events/index.md",
                  "index.html": output_root / "README.md"})
    guide_names = ["jsonrpc", "query_methods", "jobs", "rbac", "changelog"]
    for stem in guide_names:
        path = source_root / f"{stem}.html"
        if path.exists():
            destination = output_root / "shared" / f"{stem}.md"
            write_text(destination, render_shared_doc(stem, path, destination, source_root))
            links[f"{stem}.html"] = destination
    inventory = []
    for page in sorted(pages.values(), key=lambda p: (p.kind, p.title)):
        if not page.is_leaf:
            continue
        fields = []
        soup = BeautifulSoup(page.schema_html, "html.parser")
        for card in soup.select(".card"):
            header = card.find("div", class_="card-header", recursive=False)
            if header is None:
                continue
            name = header.select_one(".property-name")
            if name is None:
                continue
            body_wrapper = header.find_next_sibling("div")
            badge = body_wrapper.find("span", class_="value-type") if body_wrapper else None
            fields.append({"name": clean_inline_text(name),
                           "type": clean_inline_text(badge).removeprefix("Type:").strip() if badge else "",
                           "required": header.select_one(".required-property") is not None,
                           "schema_id": str(header.find("button").get("aria-controls", "")) if header.find("button") else ""})
        rendered_page = make_output_path(output_root, page).read_text(encoding="utf-8")
        missing_fields = [field["schema_id"] for field in fields
                          if field["schema_id"] and f'id="{field["schema_id"]}"' not in rendered_page]
        if missing_fields:
            raise ValueError(f"Truncated schema fields in {page.title}: {missing_fields}")
        inventory.append({"name": page.title, "kind": page.kind,
                          "path": make_output_path(output_root, page).relative_to(output_root).as_posix(),
                          "source_rst": page.source_path.relative_to(source_root).as_posix(),
                          "source_sha256": hashlib.sha256(page.source_path.read_bytes()).hexdigest(),
                          "required_roles": page.required_roles,
                          "schema_sha256": hashlib.sha256(page.schema_html.encode()).hexdigest(),
                          "fields": fields,
                          "parameters": [{"position": int(match.group(1)), "name": match.group(2).strip()}
                                         for node in soup.find_all("h5")
                                         if (match := re.match(r"Parameter (\d+):\s*(.+)", clean_inline_text(node)))]})
    auth_entries = [(p.title, relative_link(output_root / "authentication.md", make_output_path(output_root, p)))
                    for p in sorted(pages.values(), key=lambda p: p.title) if p.is_leaf and p.title.startswith("auth.")]
    write_text(output_root / "authentication.md", build_index_page(
        "Authentication", "Authentication methods and response schemas from this exact snapshot. "
        "See [JSON-RPC transport](shared/jsonrpc.md) and [roles](shared/rbac.md).", auth_entries))
    write_text(output_root / "schemas/index.md", build_index_page(
        "Schemas", "The archive embeds schemas in each owning method/event page; it does not expose canonical JSON Schema files. "
        "The inventory records documented fields, types, required markers and schema digests. Nested context remains in owning pages.",
        [(p.title, relative_link(output_root / "schemas/index.md", make_output_path(output_root, p)))
         for p in sorted(pages.values(), key=lambda p: (p.kind, p.title)) if p.is_leaf]))
    readme = output_root / "README.md"
    source_arguments = ["--archive", str(archive_path)] if archive_path else ["--source", str(source_root)]
    output_argument = os.path.relpath(destination_root, Path.cwd())
    command = shlex.join(["python3", "scripts/convert_truenas_api_docs_to_markdown.py", *source_arguments,
                          "--output", output_argument, "--api-version", api_version,
                          "--source-url", source_url, "--retrieved-at", retrieved_at, "--clean"])
    acquisition = ""
    if archive_path:
        archive_url = urljoin(source_url, f"truenas-v{api_version}-docs.zip")
        acquisition = ("Acquire a fresh archive deliberately (this changes the pinned source checksum):\n\n```bash\n" +
                       command.replace(" --clean", "") + " --download-url " + shlex.quote(archive_url) + "\n```\n\n")
    text = (f"# TrueNAS API {api_version} Markdown snapshot\n\n"
            f"Source: [{source_url}]({source_url}). Retrieved: {retrieved_at}. "
            "This snapshot describes the API documentation; it does not establish the appliance release or live compatibility.\n\n"
            "`MANIFEST.json` records the source archive SHA256, individual source/content checksums, "
            "required roles, parameter positions, schema field identifiers/types/required markers and method/event inventories.\n\n"
            "- [Methods](methods/index.md)\n- [Events](events/index.md)\n- [Authentication](authentication.md)\n"
            "- [Schemas](schemas/index.md)\n- [Shared guides](shared/index.md)\n"
            "- [RBAC](shared/rbac.md)\n- [Changelog](shared/changelog.md)\n- [Compatibility](compatibility.md)\n\n"
            "## Regeneration\n\nRun from the repository root using the retained archive or extracted source tree:\n\n"
            f"```bash\n{command}\n```\n\n"
            "Append `--check` to compare byte-identical output without changing files. "
            "The retrieval date is a fixed input. Raw source archives are deliberately outside Git.\n\n" + acquisition +
            "The existing converter reads `_sources/*.rst.txt` and embedded schema HTML. "
            "Original fields, alternatives, constants, constraints, examples and roles are retained in owning pages; "
            "the inventory is an index, not a substitute for those schemas.\n")
    write_text(readme, text)
    write_text(output_root / "shared/index.md", build_index_page(
        "Shared guides", "Shared transport, querying, jobs, permission and changelog documentation.",
        [(stem, f"{stem}.md") for stem in guide_names if (output_root / "shared" / f"{stem}.md").exists()]))
    write_text(output_root / "compatibility.md", "# Compatibility evidence\n\n"
               f"API documentation version: **{api_version}**. The source URL and checksums are pinned in [README](README.md) and `MANIFEST.json`.\n\n"
               "A documentation match is not authenticated live verification. Compare this snapshot with the separately retained local/official "
               "27 snapshot before accepting schema or permission differences. Read-only roles in the docs do not prove the supplied account permissions.\n\n"
               "Historical references remain available: [25.10.2](../../truenas-api/README.md), "
               "[26.0.0](../../truenas-api-v26/README.md). Exporter compatibility and live results are recorded separately in the repository reviews.\n")
    # Resolve original HTML cross-references to generated Markdown or the owning source URL.
    for path in output_root.rglob("*.md"):
        content = path.read_text()
        def rewrite(match: re.Match[str], from_path: Path = path) -> str:
            label, href = match.groups()
            parsed = urlsplit(href)
            if parsed.scheme or not parsed.path.endswith(".html"):
                return match.group(0)
            target = links.get(Path(parsed.path).name)
            if target is None:
                return f"[{label}]({urljoin(source_url, href)})"
            fragment = f"#{parsed.fragment}" if parsed.fragment else ""
            if fragment and f'id="{parsed.fragment}"' not in target.read_text():
                return f"[{label}]({urljoin(source_url, href)})"
            return f"[{label}]({relative_link(from_path, target)}{fragment})"
        write_text(path, re.sub(r"\[([^\]]+)\]\(([^\s)]+)\)", rewrite, content))
    resolved_output = output_root.absolute()
    for path in output_root.rglob("*.md"):
        for href in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
            parsed = urlsplit(href)
            target = Path(os.path.abspath(path.parent / parsed.path))
            if (not parsed.scheme and parsed.path.endswith(".md")
                    and target.is_relative_to(resolved_output) and not target.is_file()):
                raise ValueError(f"Broken generated Markdown link in {path}: {href}")
    source_files = []
    for path in sorted(source_root.rglob("*")):
        if path.is_file() and (path.suffix == ".html" or path.name.endswith(".rst.txt")):
            data = path.read_bytes()
            source_files.append({"path": path.relative_to(source_root).as_posix(), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    files = []
    for path in sorted(output_root.rglob("*.md")):
        data = path.read_bytes()
        files.append({"path": path.relative_to(output_root).as_posix(), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)})
    aggregate = hashlib.sha256()
    for entry in files:
        aggregate.update(f"{entry['path']}\0{entry['sha256']}\n".encode())
    manifest = {"schema_version": 3, "aggregate_sha256": aggregate.hexdigest(), "truenas_version": api_version, "source_url": source_url,
                "retrieved_at": retrieved_at, "archive_sha256": archive_sha256,
                "generator": "scripts/convert_truenas_api_docs_to_markdown.py",
                "method_count": sum(p["kind"] == "method" for p in inventory),
                "event_count": sum(p["kind"] == "event" for p in inventory),
                "file_count": len(files), "files": files, "source_files": source_files, "inventory": inventory}
    write_text(output_root / "MANIFEST.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def validate_archive(bundle: ZipFile) -> None:
    """Reject unsafe, duplicate, or unreasonably expanded ZIP members before extraction."""
    seen = set()
    expanded_size = 0
    for item in bundle.infolist():
        path = Path(item.filename)
        if path.is_absolute() or ".." in path.parts or "\\" in item.filename or stat.S_ISLNK(item.external_attr >> 16):
            raise ValueError(f"Unsafe archive path: {item.filename}")
        normalized = path.as_posix().casefold()
        if normalized in seen:
            raise ValueError(f"Duplicate archive path: {item.filename}")
        seen.add(normalized)
        expanded_size += item.file_size
        if expanded_size > 500 * 1024 * 1024:
            raise ValueError("Expanded documentation archive exceeds 500 MiB limit")


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    default_source = repo_root / f"truenas-v{TRUENAS_API_VERSION}-docs"
    default_output = repo_root / "docs" / "truenas-api"

    parser = argparse.ArgumentParser(description="Convert offline TrueNAS API docs into AI-friendly Markdown.")
    parser.add_argument("--source", type=Path, default=default_source, help="Path to the offline docs snapshot root.")
    parser.add_argument("--output", type=Path, default=default_output, help="Output directory for generated Markdown.")
    parser.add_argument("--archive", type=Path, help="Documentation ZIP instead of an extracted --source directory.")
    parser.add_argument("--download-url", help="Download a public documentation ZIP into --archive before conversion.")
    parser.add_argument("--api-version", help="Explicit snapshot version; enables provenance and complete guide inventory.")
    parser.add_argument("--source-url", default="", help="Original documentation base URL.")
    parser.add_argument("--retrieved-at", default="", help="Fixed retrieval date (YYYY-MM-DD); retained for deterministic regeneration.")
    parser.add_argument("--check", action="store_true", help="Compare generated files without changing output.")
    parser.add_argument("--clean", action="store_true", help="Replace existing output only after successful conversion.")
    args = parser.parse_args()

    if args.api_version and (not args.source_url or not args.retrieved_at):
        parser.error("--api-version requires --source-url and --retrieved-at")
    if args.download_url:
        if not args.archive or args.check:
            parser.error("--download-url requires --archive and cannot be combined with --check")
        parsed = urlsplit(args.download_url)
        if parsed.scheme not in {"https", "http"} or parsed.username or parsed.password:
            parser.error("Documentation download must be a public HTTP(S) URL without credentials")
        args.archive.parent.mkdir(parents=True, exist_ok=True)
        with urlopen(args.download_url, timeout=60) as response:
            data = response.read(100 * 1024 * 1024 + 1)
        if len(data) > 100 * 1024 * 1024:
            raise ValueError("Documentation archive exceeds 100 MiB limit")
        with tempfile.NamedTemporaryFile(dir=args.archive.parent, delete=False) as downloaded:
            downloaded.write(data)
            temporary_path = Path(downloaded.name)
        try:
            with ZipFile(temporary_path) as bundle:
                validate_archive(bundle)
            temporary_path.replace(args.archive)
        finally:
            temporary_path.unlink(missing_ok=True)
    kwargs = dict(api_version=args.api_version, source_url=args.source_url,
                  retrieved_at=args.retrieved_at, check=args.check)
    if args.archive:
        digest = hashlib.sha256(args.archive.read_bytes()).hexdigest()
        with tempfile.TemporaryDirectory(prefix="truenas-api-source-") as temporary:
            source = Path(temporary)
            with ZipFile(args.archive) as bundle:
                validate_archive(bundle)
                bundle.extractall(source)
            convert(source, args.output.resolve(), clean=args.clean,
                    archive_sha256=digest, archive_path=args.archive.resolve(), **kwargs)
    else:
        convert(args.source.resolve(), args.output.resolve(), clean=args.clean, **kwargs)


if __name__ == "__main__":
    main()
