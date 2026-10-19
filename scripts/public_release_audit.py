#!/usr/bin/env python3
"""Check tracked files for public-release blockers.

The audit is intentionally local and read-only. It scans only Git-tracked
content because ignored files such as `.env` can exist in an operator checkout
without being published.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

BINARY_SUFFIXES = {
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".pdf",
    ".png",
    ".pyc",
    ".webp",
}

FORBIDDEN_EXACT_PATHS = {
    "api",
    ".coverage",
    "CLAUDE.md",
    "TrueNAS - newest dashboard.json",
    "prometheus_metrics.txt",
    "promthues_metrics.txt",
    "truenas_exporter_old.py",
}

FORBIDDEN_PREFIXES = (
    ".agent/",
    ".claude/",
    ".cursor/",
    ".github/workflows/",
    ".mypy_cache/",
    ".opencode/",
    ".pytest_cache/",
    ".ruff_cache/",
    ".venv/",
    "__pycache__/",
    "build/",
    "dist/",
    "htmlcov/",
    "scripts/__pycache__/",
    "src/truenas_exporter/__pycache__/",
    "tests/__pycache__/",
    "venv/",
)

SECRET_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("private key", re.compile(r"BEGIN (?:RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}\b|\bgithub_pat_[A-Za-z0-9_]+\b")),
    ("GitLab token", re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    (
        "URL token parameter",
        re.compile(
            r"\b(?:auth_token|access_token|refresh_token|api_key|apikey|token)="
            r"(?!\{token\}|<redacted>|redacted|example|replace_with_api_key)"
            r"[A-Za-z0-9_-]{20,}\b",
            re.IGNORECASE,
        ),
    ),
)


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        [
            "git",
            "-c",
            f"safe.directory={REPO_ROOT}",
            "ls-files",
            "-z",
        ],
        cwd=REPO_ROOT,
    )
    return [Path(raw.decode("utf-8")) for raw in output.split(b"\0") if raw]


def is_forbidden_path(path: Path) -> str | None:
    name = path.as_posix()
    # The reusable skill's Claude discovery bridge is public project guidance,
    # not local Claude configuration. Its contents still undergo secret scans.
    if name == ".claude/skills/truenas-prometheus-exporter/SKILL.md":
        return None
    if name in FORBIDDEN_EXACT_PATHS:
        return "local/scratch artifact"
    if name == ".env" or (name.startswith(".env.") and name != ".env.example"):
        return "environment file"
    if name.endswith(".prompt.md"):
        return "agent prompt artifact"
    if any(name.startswith(prefix) for prefix in FORBIDDEN_PREFIXES):
        return "local/cache/hosted-automation artifact"
    if "__pycache__/" in name or name.endswith((".pyc", ".pyo", ".pyd")):
        return "Python bytecode artifact"
    return None


def scan_text(path: Path) -> list[str]:
    absolute = REPO_ROOT / path
    if absolute.suffix.lower() in BINARY_SUFFIXES:
        return []
    data = absolute.read_bytes()
    if b"\0" in data:
        return []
    text = data.decode("utf-8", errors="ignore")
    findings: list[str] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for label, pattern in SECRET_PATTERNS:
            if pattern.search(line):
                findings.append(f"{path}:{line_number}: {label}")
    return findings


def main() -> int:
    findings: list[str] = []
    for path in tracked_files():
        reason = is_forbidden_path(path)
        if reason:
            findings.append(f"{path}: forbidden tracked {reason}")
        findings.extend(scan_text(path))

    if findings:
        print("public_release_audit_failed", file=sys.stderr)
        for finding in findings:
            print(finding, file=sys.stderr)
        return 1

    print("public_release_audit_ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
