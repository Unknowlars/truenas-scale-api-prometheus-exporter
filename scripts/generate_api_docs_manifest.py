#!/usr/bin/env python3
"""Inventory the pinned generated TrueNAS API Markdown snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

try:
    from .tooling import TRUENAS_API_VERSION, check_or_write
except ImportError:  # direct script execution
    from tooling import TRUENAS_API_VERSION, check_or_write

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "docs" / "truenas-api"
OUTPUT = DOCS_ROOT / "MANIFEST.json"


def build_manifest() -> dict[str, object]:
    files = []
    aggregate = hashlib.sha256()
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        relative = path.relative_to(DOCS_ROOT).as_posix()
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")
        files.append({"path": relative, "sha256": digest, "bytes": len(data)})
    return {
        "schema_version": 1,
        "truenas_version": TRUENAS_API_VERSION,
        "source": "offline TrueNAS API documentation snapshot (not redistributed)",
        "generator": "scripts/convert_truenas_api_docs_to_markdown.py",
        "file_count": len(files),
        "aggregate_sha256": aggregate.hexdigest(),
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_manifest(), indent=2, sort_keys=True) + "\n"
    check_or_write(OUTPUT, rendered, check=args.check, description="API docs manifest")


if __name__ == "__main__":
    main()
