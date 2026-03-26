#!/usr/bin/env python3

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError as exc:  # pragma: no cover - user-facing dependency error
    raise SystemExit(
        "Missing dependency: beautifulsoup4. Install it with `pip install -r requirements-dev.txt`."
    ) from exc


SHARED_DOCS = {
    "jsonrpc": "JSON-RPC 2.0 over WebSocket API",
    "query_methods": "Query Methods",
    "jobs": "Jobs",
}

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
            required_roles = [role.strip() for role in roles_text.split(",") if role.strip()]

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

    heading = f"{'#' * level} {name}"
    if required:
        heading += " (required)"

    lines = [heading, ""]
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
        elif child.name == "span" and "default-value" in child_classes:
            lines.append(f"- {clean_inline_text(child)}")
        elif child.name == "span" and "no-additional" in child_classes:
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
            lines.extend(["", f"{'#' * level} {clean_inline_text(child)}", ""])
        elif child.name == "div" and "accordion" in child_classes:
            for nested in child.find_all("div", class_="card", recursive=False):
                lines.extend(render_schema_card(nested, level=level))
                lines.append("")
        elif child.name == "div" and "card" in child_classes:
            lines.extend(render_inline_schema_card(child, level=level))
            lines.append("")
        elif child.name == "div" and "any-of-value" in child_classes:
            lines.extend(render_any_of(child, level=level))
            lines.append("")
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
    lines: list[str] = []
    if title is not None:
        lines.extend([f"{'#' * level} {clean_inline_text(title)}", ""])
    lines.extend(render_schema_body(body, level + 1))
    return trim_blank_lines(lines)


def render_any_of(node: Tag, level: int) -> list[str]:
    lines = [f"{'#' * level} Any of", ""]
    labels = [clean_inline_text(link) for link in node.select(".nav-link")]
    panes = node.select(".tab-content > .tab-pane")
    for index, pane in enumerate(panes, start=1):
        label = labels[index - 1] if index - 1 < len(labels) and labels[index - 1] else f"Option {index}"
        lines.extend([f"{'#' * (level + 1)} {label}", ""])
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
        return "".join(render_inline(child) for child in node.children)
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
            lines.extend(render_html_children(child.children, base_level=base_level))
        elif re.fullmatch(r"h[1-6]", child.name or ""):
            heading_level = min(base_level + int(child.name[1]) - 1, 6)
            lines.extend([f"{'#' * heading_level} {clean_inline_text(child)}", ""])
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


def convert(source_root: Path, output_root: Path, clean: bool) -> None:
    if clean and output_root.exists():
        shutil.rmtree(output_root)

    pages = build_pages(source_root)
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
                "python convert_truenas_api_docs_to_markdown.py --clean",
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


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    default_source = repo_root / "truenas-v25.10.2-docs"
    default_output = repo_root / "docs" / "truenas-api"

    parser = argparse.ArgumentParser(description="Convert offline TrueNAS API docs into AI-friendly Markdown.")
    parser.add_argument("--source", type=Path, default=default_source, help="Path to the offline docs snapshot root.")
    parser.add_argument("--output", type=Path, default=default_output, help="Output directory for generated Markdown.")
    parser.add_argument("--clean", action="store_true", help="Remove the output directory before regenerating Markdown.")
    args = parser.parse_args()

    convert(args.source.resolve(), args.output.resolve(), clean=args.clean)


if __name__ == "__main__":
    main()
