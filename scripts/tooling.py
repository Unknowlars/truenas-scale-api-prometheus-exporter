"""Shared deterministic-generator helpers."""

from pathlib import Path

TRUENAS_API_VERSION = "25.10.2"


def check_or_write(path: Path, rendered: str, *, check: bool, description: str) -> None:
    if check:
        if not path.exists() or path.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"{description} is out of date: regenerate {path.name}")
        return
    path.write_text(rendered, encoding="utf-8")
