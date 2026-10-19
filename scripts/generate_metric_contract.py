#!/usr/bin/env python3
"""Generate a stable manifest of the exporter's public Prometheus metrics."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "src" / "truenas_exporter" / "metrics.py"
OUTPUT = REPO_ROOT / "docs" / "metrics-contract.json"
sys.path.insert(0, str(REPO_ROOT / "src"))

from truenas_exporter.metrics import METRIC_SPECS  # noqa: E402

try:
    from .tooling import TRUENAS_API_VERSION, check_or_write
except ImportError:  # direct script execution
    from tooling import TRUENAS_API_VERSION, check_or_write


def build_contract() -> dict[str, object]:
    metrics: list[dict[str, object]] = [
        {
            "variable": spec.variable,
            "name": spec.name,
            "type": spec.metric_type,
            "help": spec.help,
            "labels": list(spec.labels),
        }
        for spec in METRIC_SPECS
    ]

    metrics.sort(key=lambda metric: str(metric["name"]))
    names = [str(metric["name"]) for metric in metrics]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise ValueError(f"duplicate metric definitions: {', '.join(duplicates)}")
    return {
        "schema_version": 1,
        "primary_truenas_version": "27.0.0",
        "supported_truenas_profiles": ["25.10", "26.0", "27.0"],
        "truenas_version": TRUENAS_API_VERSION,
        "source": "src/truenas_exporter/metrics.py",
        "metrics": metrics,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(build_contract(), indent=2, sort_keys=True) + "\n"
    check_or_write(OUTPUT, rendered, check=args.check, description="Metric contract")


if __name__ == "__main__":
    main()
