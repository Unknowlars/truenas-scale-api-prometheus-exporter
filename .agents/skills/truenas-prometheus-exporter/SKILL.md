---
name: truenas-prometheus-exporter
description: Maintain this repository's read-only TrueNAS collectors, version profiles, WebSocket events, Prometheus metrics, Grafana generators, compatibility evidence, and local releases. Use when adding telemetry or diagnosing this exporter.
---

# TrueNAS Prometheus exporter

Read AGENTS.md first. TrueNAS27 is primary; preserve tested25.10/26.0 behavior.
The owner permits bounded read-only real-server verification. Keep credentials
private and retain only sanitized fixtures or non-sensitive summaries. Permission
to inspect does not establish successful live compatibility.

Start from the four reviews under docs/reviews and check their provenance.

- New collector, API removal or subscription: [collectors](references/collectors.md).
- Missing values, failures or high cardinality: [diagnostics](references/diagnostics.md).
- Tests, Grafana, compatibility or releases: [validation](references/validation.md).
- Dashboard queries, layout, no-data styling or renders: [dashboards](references/dashboards.md).

Preserve metric names, types, HELP and labels; corrections need compatibility
aliases and migration notes. Unsupported data stays absent/NaN; valid zero/false
is preserved. Read-only semantics require exact documented membership, not a
method-name heuristic. Never expose opaque full responses generically.

Preserve background polling, the separate event connection, and atomic HTTP
snapshots. Do not issue NAS RPCs during /metrics or build a competing collector
framework. Extend existing metric ownership, parsers and profiles.

Complete ./scripts/validate.sh and record evidence in docs/modernization/README.md.
Separate documented, mocked and live verification. No hosted CI, publication,
push or deployment is authorized by this skill.
