# T02 — Stop fabricating `truenas_cpu_user_percent` / `truenas_cpu_idle_percent`

- **Priority:** P1
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md finding A2

## Problem

On every supported TrueNAS version, the `reporting.realtime` CPU payload has **no** user/system/
iowait/idle split — the aggregate object carries only `usage` (+ `temp`). Evidence:

- Fixture `tests/fixtures/realtime/reporting_realtime_25_10_shape.json`: `cpu.cpu = {usage, temp}`.
- v26 doc `docs/truenas-api-v26/events/reporting/realtime.md`: per-core objects expose only
  `usage` and `temp`.

The handler `_cache_realtime_event` (`src/truenas_exporter/runtime.py` ~lines 1713–1735)
therefore *always* takes its fallback branches:

- `truenas_cpu_user_percent` ← total CPU usage (a mislabeled duplicate of
  `truenas_cpu_usage_percent`),
- `truenas_cpu_idle_percent` ← `max(0, 100 − total)` (a derived approximation).

This violates the exporter's own never-fabricate policy. A box at 80 % CPU that is mostly iowait
reports `user_percent = 80`.

`tests/test_reliability.py::test_collector_realtime_zero_replaces_previous_value` (lines ~15–24)
**cements the buggy fallback** — it asserts `CPU_USER_PERCENT == 0.0` and `CPU_IDLE_PERCENT ==
100.0` from a payload containing only `usage`. This test must be updated as part of this task.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `_cache_realtime_event` CPU section (~1699–1799).
- `src/truenas_exporter/metrics.py` — CPU metric declarations (~564–571).
- `tests/test_reliability.py` (~1–35), `tests/test_phase2_events.py` (patterns).
- Fixture: `tests/fixtures/realtime/reporting_realtime_25_10_shape.json`.

## Required behavior

1. Remove the fallback `elif total_cpu_percent is not None:` branches for **user** and **idle**
   (`runtime.py` ~1718–1719 and ~1732–1735). If the payload does not carry a real `user` / `idle`
   field, the metric must not be cached for that event cycle (it will read NaN/absent, matching
   `system`/`iowait`/`interrupt`, which already behave this way).
2. Keep the *real* extraction paths intact: if some payload variant does deliver
   `cpu.user`/`cpu.idle` (older/newer middleware), it must still be honored.
3. Fix the HELP strings in `metrics.py` (they currently document the fallback):
   - `CPU_USER_PERCENT` → e.g. "Host CPU user-space usage percent (0 to 100); absent when the
     API does not report a user/system split"
   - `CPU_IDLE_PERCENT` → analogous.
   HELP text changes require regenerating the metric contract and parity docs (README rule 6).
4. Update the hand-maintained parity mapping if needed: the parity row for
   `truenas_cpu_user_percent` currently claims parser key `cpu.user` while emitting total —
   after this fix the claim becomes accurate; verify by regenerating and reading the row.

## Compatibility rules that apply

- Metric names/labels/types unchanged — only values-when-absent and HELP change. Per
  `docs/VERSIONING.md` this is a behavior fix (patch-worthy). Going from "always present, wrong"
  to "absent when unavailable" is the documented zero-vs-absent policy; note it in the Outcome
  section so it lands in release notes.

## Tests

1. **Update** `tests/test_reliability.py::test_collector_realtime_zero_replaces_previous_value`:
   with a `{usage: 50}`-only payload, assert `CPU_USAGE_PERCENT` cached as 50.0 and
   `CPU_USER_PERCENT` / `CPU_IDLE_PERCENT` **not present** in `_collector_event_scalars`.
2. **Add**: payload *with* explicit `user`/`idle` keys → both cached with the real values
   (protects the non-fallback path).
3. **Add**: full-pipeline check — dispatch the committed 25.10 fixture through
   `_dispatch_event("reporting.realtime", fixture)` and assert `truenas_cpu_user_percent` renders
   as NaN/absent in the published output while `truenas_cpu_usage_percent` carries the fixture
   value.

## Verification

```
python3 -m pytest tests/test_reliability.py tests/test_phase2_events.py tests/test_phase3_collector_mode.py -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

Also check: does the bundled Grafana dashboard reference `truenas_cpu_user_percent` or
`truenas_cpu_idle_percent`? (`grep` the dashboard JSON.) If yes, the panels should be switched to
`truenas_cpu_usage_percent` (or 100−usage) via the dashboard *generator*, not hand-edits.

## Definition of done

- No fabricated user/idle values on fixture-shaped payloads (tests prove it).
- Real split still honored when present.
- HELP accurate; contract/parity/dashboard regenerated; validate.sh green; TASKS.md updated.

## Outcome

_(fill in when done)_
