# T05 — Remove cumulative-bytes fallback in network rx/tx rate gauges

- **Priority:** P1
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md finding A4

## Problem

`_cache_realtime_event` (`src/truenas_exporter/runtime.py` ~1897–1912) fills
`truenas_network_{rx,tx}_bytes_per_second{interface}` with:

```python
rx = _as_float(_first_not_none(iface_data.get("received_bytes_rate"), iface_data.get("received_bytes")))
```

Per the v26 schema (`docs/truenas-api-v26/events/reporting/realtime.md`, interfaces section),
`received_bytes_rate` (bytes/s) and `received_bytes` (cumulative total) are **both optional**.
If a payload carries only the cumulative fields, a metric named `_per_second` silently serves an
ever-growing byte total — wrong by orders of magnitude with no error anywhere.

The committed 25.10 fixture carries `received_bytes_rate`/`sent_bytes_rate`, so the primary path
is the observed one; the fallback is the hazard.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` ~1897–1912.
- `docs/truenas-api-v26/events/reporting/realtime.md` — interfaces section.
- Fixture `tests/fixtures/realtime/reporting_realtime_25_10_shape.json`.
- `tests/test_phase2_events.py` (patterns).

## Required behavior

1. The `_per_second` gauges must read **only** `received_bytes_rate` / `sent_bytes_rate`. Delete
   the `received_bytes` / `sent_bytes` fallbacks. Absent rate field ⇒ absent metric.
2. **Optional (recommended, small):** expose the cumulative fields honestly as counters:
   `truenas_network_rx_bytes_total{interface}` / `truenas_network_tx_bytes_total{interface}`
   (Counter is awkward for externally-sourced totals — prometheus_client counters can't be
   `.set()`. Use a Gauge declared with an explicit `_total`-free name and cumulative HELP, e.g.
   `truenas_network_rx_bytes_cumulative` — OR skip this entirely. If skipping, note it in
   TASKS.md "Discovered" so it can be a T21 item. Do NOT emit a counter-typed metric you cannot
   set monotonically.)
3. If you add metrics, register them as event-owned in `events.py` (same checklist as T04 step 1)
   and regenerate contract/parity/dashboard.

## Compatibility rules

- Removing the fallback changes values only in the (never-observed-in-fixtures) case where the
  fallback fired — i.e., it changes wrong values to absent. Patch-worthy behavior fix.

## Tests

1. Payload with only `received_bytes`/`sent_bytes` (no `_rate` keys) → rx/tx `_per_second`
   metrics have **no** samples (this test must fail on current code).
2. Payload with `_rate` keys (use the committed fixture) → values emitted, unchanged behavior.

## Verification

```
python3 -m pytest tests/test_phase2_events.py tests/test_reliability.py -q
./scripts/validate.sh
```

(Plus generators if you added metrics — README rule 6.)

## Definition of done

- No code path can put a cumulative byte count into a `_per_second` series. Tests prove both
  directions. validate.sh green. TASKS.md updated.

## Outcome

Completed 2026-07-16.

- Removed the `received_bytes` / `sent_bytes` fallbacks from
  `truenas_network_rx_bytes_per_second{interface}` and
  `truenas_network_tx_bytes_per_second{interface}`. The rate gauges now read
  only `received_bytes_rate` / `sent_bytes_rate`; cumulative-only payloads
  leave the samples absent.
- Skipped optional cumulative network byte metrics for this patch-worthy fix and
  recorded the possible honest non-rate metrics as a T21 follow-up in
  `TASKS.md`.
- Added regression coverage for cumulative-only interface payloads and kept
  fixture coverage for rate-key payloads.
- Verification passed:
  `python3 -m pytest tests/test_phase2_events.py tests/test_reliability.py -q`
  (`37 passed`). Regenerated metric contract, API parity, and dashboard
  artifacts; they produced no file changes. `./scripts/validate.sh` exited 0
  with `195 passed`, 90.67% coverage, `dashboard_ok panels=318
  metric_references=287`, `public_release_audit_ok`, Docker build/version smoke
  `5.2.0`, and `validation_ok`.
