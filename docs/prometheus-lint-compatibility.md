# Prometheus lint compatibility baseline

The 2026-10-21 live exposition produced 97 warnings from
`promtool 3.5.0 check metrics`. A synthetic exposition containing every family
in the existing 420-metric contract produces 98 because
`truenas_certificate_days_to_expiry` was absent from that live scrape:

- 87 gauges ending in `_count`;
- 2 gauges ending in `_total`;
- 7 gauges using `_days` rather than base-unit seconds;
- 2 gauges using `_minutes` rather than base-unit seconds.

All 98 names predate the TrueNAS 27 release work and are public compatibility
contracts. They remain unchanged because silently renaming, retyping, or
rescaling them would break existing PromQL, alerts, recordings, and dashboards.
These warnings are not suppressed: `scripts/check_prometheus_lint_baseline.py`
derives the full warning-name inventory from `docs/metrics-contract.json`,
checks its exact count and SHA-256 fingerprint, and has promtool 3.5.0 lint a
synthetic exposition containing every metric family. Any added, removed,
renamed, or newly classified warning fails local validation and requires an
explicit compatibility review.

Future canonical replacements must be added alongside these aliases, use the
correct type and base unit, update generated dashboards, and include a dated
deprecation/migration note. Compatibility aliases stay available until a
separately approved breaking release.
