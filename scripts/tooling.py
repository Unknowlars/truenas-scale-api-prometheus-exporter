"""Shared deterministic-generator helpers."""

from dataclasses import dataclass
from pathlib import Path

TRUENAS_API_VERSION = "25.10.2"


@dataclass(frozen=True)
class ApiDocsTarget:
    version: str
    docs_dir: str
    source: str
    provenance: dict[str, object] | None = None


API_DOCS_TARGETS = {
    "25.10.2": ApiDocsTarget(
        version="25.10.2",
        docs_dir="truenas-api",
        source="offline TrueNAS API documentation snapshot (not redistributed)",
    ),
    "26.0.0": ApiDocsTarget(
        version="26.0.0",
        docs_dir="truenas-api-v26",
        source="checked-in converted Markdown corpus",
        provenance={
            "corpus_path": "docs/truenas-api-v26/",
            "prompt_path": "docs/truenas-api-v26.0.0/",
            "prompt_path_exists": False,
            "raw_source_tree_path": "truenas-v26.0.0-docs/",
            "raw_source_tree_checked_in": False,
            "note": (
                "The raw truenas-v26.0.0-docs/ source tree is not checked in; "
                "this manifest pins the converted Markdown corpus currently "
                "present in docs/truenas-api-v26/."
            ),
        },
    ),
}

API_DOCS_TARGET_ALIASES = {
    "25": "25.10.2",
    "25.10": "25.10.2",
    "25.10.2": "25.10.2",
    "v25": "25.10.2",
    "v25.10.2": "25.10.2",
    "26": "26.0.0",
    "26.0": "26.0.0",
    "26.0.0": "26.0.0",
    "v26": "26.0.0",
    "v26.0.0": "26.0.0",
}


def resolve_api_docs_target(target: str) -> ApiDocsTarget:
    version = API_DOCS_TARGET_ALIASES.get(target)
    if version is None:
        allowed = ", ".join(sorted(API_DOCS_TARGET_ALIASES))
        raise ValueError(f"Unknown TrueNAS API docs target {target!r}; expected one of: {allowed}")
    return API_DOCS_TARGETS[version]


def check_or_write(path: Path, rendered: str, *, check: bool, description: str) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"{description} is out of date: regenerate {path.name}")
        return
    path.write_text(rendered, encoding="utf-8")
