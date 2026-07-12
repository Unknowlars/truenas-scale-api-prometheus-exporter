#!/usr/bin/env python3
"""Validate dashboard structure and exporter metric references."""

from __future__ import annotations

import json
import re
from collections.abc import Iterable
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = REPO_ROOT / "grafana-dashboard" / "operations-center-dashboard.json"
CONTRACT = REPO_ROOT / "docs" / "metrics-contract.json"
METRIC_RE = re.compile(r"\btruenas_[a-zA-Z_:][a-zA-Z0-9_:]*\b")


def walk_panels(panels: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
    for panel in panels:
        yield panel
        nested = panel.get("panels")
        if isinstance(nested, list):
            yield from walk_panels(item for item in nested if isinstance(item, dict))


def main() -> None:
    dashboard = json.loads(DASHBOARD.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    metric_names = {metric["name"] for metric in contract["metrics"]}
    panels = list(walk_panels(dashboard.get("panels", [])))

    ids = [panel.get("id") for panel in panels if isinstance(panel.get("id"), int)]
    duplicates = sorted({panel_id for panel_id in ids if ids.count(panel_id) > 1})
    if duplicates:
        raise SystemExit(f"duplicate dashboard panel IDs: {duplicates}")

    errors: list[str] = []
    expressions: list[str] = []
    for panel in panels:
        grid = panel.get("gridPos", {})
        if isinstance(grid, dict) and grid.get("x", 0) + grid.get("w", 0) > 24:
            errors.append(f"panel exceeds 24 columns: {panel.get('title', panel.get('id'))}")
        for target in panel.get("targets", []):
            if isinstance(target, dict) and isinstance(target.get("expr"), str):
                expressions.append(target["expr"])

    templating = dashboard.get("templating", {}).get("list", [])
    for variable in templating:
        query = variable.get("definition") or variable.get("query")
        if isinstance(query, dict):
            query = query.get("query")
        if isinstance(query, str):
            expressions.append(query)

    referenced = {name for expression in expressions for name in METRIC_RE.findall(expression)}
    missing = sorted(referenced - metric_names)
    if missing:
        errors.append("dashboard references undefined exporter metrics: " + ", ".join(missing))
    if errors:
        raise SystemExit("\n".join(errors))

    print(f"dashboard_ok panels={len(panels)} metric_references={len(referenced)}")


if __name__ == "__main__":
    main()

