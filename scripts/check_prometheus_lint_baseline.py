#!/usr/bin/env python3
"""Fail when the compatibility metric set gains an unreviewed promtool warning."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "docs" / "metrics-contract.json"

# Captured from promtool 3.5.0 against the 420-metric compatibility contract.
# Changing this digest requires reviewing and documenting every changed warning.
EXPECTED_SHA256 = "1ffab2d3cecca096c6310c32cf0b739943e10af230d7ec3c3ecc540356da15d6"
EXPECTED_COUNTS = {
    "non-histogram and non-summary metrics should not have _count suffix": 87,
    "non-counter metrics should not have _total suffix": 2,
    "use base unit seconds instead of days": 7,
    "use base unit seconds instead of minutes": 2,
}
PROMTOOL_IMAGE = "prom/prometheus:v3.5.0"


def lint_inventory(metrics: list[dict[str, Any]]) -> dict[str, list[str]]:
    return {
        "non-histogram and non-summary metrics should not have _count suffix": sorted(
            metric["name"]
            for metric in metrics
            if metric["type"] not in {"histogram", "summary"}
            and metric["name"].endswith("_count")
        ),
        "non-counter metrics should not have _total suffix": sorted(
            metric["name"]
            for metric in metrics
            if metric["type"] != "counter" and metric["name"].endswith("_total")
        ),
        "use base unit seconds instead of days": sorted(
            metric["name"]
            for metric in metrics
            if re.search(r"_days(?:_|$)", metric["name"])
        ),
        "use base unit seconds instead of minutes": sorted(
            metric["name"]
            for metric in metrics
            if re.search(r"_minutes(?:_|$)", metric["name"])
        ),
    }


def verify_with_promtool(expected: dict[str, list[str]]) -> None:
    sys.path.insert(0, str(ROOT / "src"))
    from prometheus_client import REGISTRY, generate_latest

    from truenas_exporter.metrics import METRIC_SPECS

    for spec in METRIC_SPECS:
        metric = spec.metric.labels(*(["synthetic"] * len(spec.labels))) if spec.labels else spec.metric
        if spec.metric_type == "gauge":
            metric.set(0)
        elif spec.metric_type == "counter":
            metric.inc(0)

    result = subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "-i",
            "--entrypoint",
            "/bin/promtool",
            PROMTOOL_IMAGE,
            "check",
            "metrics",
        ],
        input=generate_latest(REGISTRY),
        capture_output=True,
        check=False,
    )
    output = (result.stdout + result.stderr).decode("utf-8", errors="replace")
    observed: dict[str, list[str]] = {}
    unparsable: list[str] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        name, separator, reason = line.partition(" ")
        normalized_reason = reason.replace('"', "")
        if not separator or normalized_reason not in expected:
            unparsable.append(line)
            continue
        observed.setdefault(normalized_reason, []).append(name)
    observed = {reason: sorted(names) for reason, names in observed.items()}
    if result.returncode not in {0, 3} or unparsable or observed != expected:
        observed_counts = {reason: len(names) for reason, names in observed.items()}
        raise SystemExit(
            "promtool compatibility inventory changed "
            f"(exit={result.returncode}, unparsable={len(unparsable)}, "
            f"observed_counts={observed_counts})"
        )
    print(
        f"promtool_lint_inventory_ok image={PROMTOOL_IMAGE} "
        f"warnings={sum(map(len, observed.values()))}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--promtool",
        action="store_true",
        help="also run promtool 3.5.0 in its pinned local container image",
    )
    args = parser.parse_args()
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    inventory = lint_inventory(contract["metrics"])
    counts = {reason: len(names) for reason, names in inventory.items()}
    encoded = json.dumps(inventory, sort_keys=True, separators=(",", ":")).encode()
    digest = hashlib.sha256(encoded).hexdigest()
    if counts != EXPECTED_COUNTS or digest != EXPECTED_SHA256:
        raise SystemExit(
            "Prometheus lint compatibility baseline changed; review names, aliases, "
            f"and migration policy before updating it (counts={counts}, sha256={digest})"
        )
    print(
        "prometheus_lint_baseline_ok "
        f"warnings={sum(counts.values())} counts={json.dumps(counts, sort_keys=True)}"
    )
    if args.promtool:
        verify_with_promtool(inventory)


if __name__ == "__main__":
    main()
