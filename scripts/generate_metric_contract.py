#!/usr/bin/env python3
"""Generate a stable manifest of the exporter's public Prometheus metrics."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "src" / "truenas_exporter" / "metrics.py"
OUTPUT = REPO_ROOT / "docs" / "metrics-contract.json"


def build_contract() -> dict[str, object]:
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    metrics: list[dict[str, object]] = []
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        call = node.value
        if not isinstance(target, ast.Name) or not isinstance(call, ast.Call):
            continue
        if not isinstance(call.func, ast.Name) or call.func.id not in {"Gauge", "Counter"}:
            continue
        if len(call.args) < 2:
            continue
        name = ast.literal_eval(call.args[0])
        help_text = ast.literal_eval(call.args[1])
        labels: list[str] = []
        if len(call.args) >= 3:
            labels = list(ast.literal_eval(call.args[2]))
        metrics.append({
            "variable": target.id,
            "name": name,
            "type": call.func.id.lower(),
            "help": help_text,
            "labels": labels,
        })

    metrics.sort(key=lambda metric: str(metric["name"]))
    names = [str(metric["name"]) for metric in metrics]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise ValueError(f"duplicate metric definitions: {', '.join(duplicates)}")
    return {
        "schema_version": 1,
        "truenas_version": "25.10.2",
        "source": "src/truenas_exporter/metrics.py",
        "metrics": metrics,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_contract(), indent=2, sort_keys=True) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"Metric contract is out of date: run {Path(__file__).name}")
        return
    OUTPUT.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
