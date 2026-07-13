#!/usr/bin/env python3
"""Inventory the pinned generated TrueNAS API Markdown snapshot."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

try:
    from .tooling import TRUENAS_API_VERSION, ApiDocsTarget, check_or_write, resolve_api_docs_target
except ImportError:  # direct script execution
    from tooling import TRUENAS_API_VERSION, ApiDocsTarget, check_or_write, resolve_api_docs_target

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TARGET = TRUENAS_API_VERSION


def docs_root_for(target: ApiDocsTarget) -> Path:
    return REPO_ROOT / "docs" / target.docs_dir


def output_path_for(target: ApiDocsTarget) -> Path:
    docs_root = docs_root_for(target)
    output = docs_root / "MANIFEST.json"
    legacy_output = REPO_ROOT / "docs" / "truenas-api" / "MANIFEST.json"
    if target.version != TRUENAS_API_VERSION and output.resolve() == legacy_output.resolve():
        raise SystemExit(
            f"Refusing to write target {target.version} manifest to the "
            f"{TRUENAS_API_VERSION} manifest path: {legacy_output}"
        )
    return output


def collect_files(docs_root: Path) -> tuple[list[dict[str, object]], str]:
    files = []
    aggregate = hashlib.sha256()
    for path in sorted(docs_root.rglob("*.md")):
        relative = path.relative_to(docs_root).as_posix()
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(digest.encode("ascii"))
        aggregate.update(b"\n")
        files.append({"path": relative, "sha256": digest, "bytes": len(data)})
    return files, aggregate.hexdigest()


def build_manifest(target: ApiDocsTarget) -> dict[str, object]:
    docs_root = docs_root_for(target)
    files, aggregate_sha256 = collect_files(docs_root)
    if target.version == TRUENAS_API_VERSION:
        return {
            "schema_version": 1,
            "truenas_version": target.version,
            "source": target.source,
            "generator": "scripts/convert_truenas_api_docs_to_markdown.py",
            "file_count": len(files),
            "aggregate_sha256": aggregate_sha256,
            "files": files,
        }

    target_arg = target.version
    return {
        "schema_version": 2,
        "target_version": target.version,
        "truenas_version": target.version,
        "target": {
            "docs_path": docs_root.relative_to(REPO_ROOT).as_posix() + "/",
            "manifest_path": output_path_for(target).relative_to(REPO_ROOT).as_posix(),
        },
        "source": target.source,
        "provenance": target.provenance or {},
        "generator": {
            "manifest_script": "scripts/generate_api_docs_manifest.py",
            "converter_script": "scripts/convert_truenas_api_docs_to_markdown.py",
            "algorithm": "sha256 per Markdown file plus path/digest aggregate",
        },
        "commands": {
            "generate": f"python3 scripts/generate_api_docs_manifest.py --target {target_arg}",
            "check": f"python3 scripts/generate_api_docs_manifest.py --target {target_arg} --check",
        },
        "file_count": len(files),
        "aggregate_sha256": aggregate_sha256,
        "files": files,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--target",
        default=DEFAULT_TARGET,
        help="TrueNAS API documentation target to manifest: 25.10.2 (default) or 26.0.0.",
    )
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        target = resolve_api_docs_target(args.target)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    output = output_path_for(target)
    rendered = json.dumps(build_manifest(target), indent=2, sort_keys=True) + "\n"
    check_or_write(output, rendered, check=args.check, description=f"API docs manifest for {target.version}")


if __name__ == "__main__":
    main()
