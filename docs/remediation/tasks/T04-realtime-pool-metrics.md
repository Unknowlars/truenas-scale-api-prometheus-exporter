# T04 — Realtime `pools` section: retire dead read/write rates, emit used/available/total bytes

- **Priority:** P1
- **Size:** M
- **Depends on:** nothing
- **Review reference:** review-report.md findings A3 + gap table row "reporting.realtime pools"

## Problem

`_cache_realtime_event` (`src/truenas_exporter/runtime.py` ~1914–1930) maps the realtime event's
`pools` section to `truenas_pool_realtime_{read,write}_bytes_per_second` by looking for
`read_bytes` / `read_bytes_per_second` keys.

Reality check:
- The committed live capture `tests/fixtures/realtime/reporting_realtime_25_10_shape.json` shows
  `pools.<name> = {available, used, total}` — **space in bytes, no I/O rates**.
- The v26 doc (`docs/truenas-api-v26/events/reporting/realtime.md`, pools section) types it as
  "mapping of stat name to value" with no rate fields promised.

So the two rate metrics never emit on any supported version, while the per-pool space data that
*is* in every event is dropped. Worse, `docs/api-exporter-parity.json` marks the rate metrics
"active dedicated" — a documented overclaim.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` ~1914–1930 (pools mapping) and `_dispatch_event` payload
  validation (~1943–1945).
- `src/truenas_exporter/metrics.py` ~637–639 (POOL_REALTIME_*), and the declaration helpers at top.
- `src/truenas_exporter/events.py` — `_EVENT_METRICS["reporting.realtime"]` (~137–150): new
  event-owned metrics must be added here or they won't be published/expired correctly.
- Fixture `tests/fixtures/realtime/reporting_realtime_25_10_shape.json`.
- `scripts/generate_api_exporter_parity.py` — `_metric_source_overrides` / `owned_response_fields`
  (search for `POOL_REALTIME`) — you must update these tables.
- `tests/test_phase2_events.py` for test patterns.

## Required behavior

1. **New metrics** (declare in `metrics.py`, wire in `_cache_realtime_event`, register in
   `events.py` `_EVENT_METRICS["reporting.realtime"]`):
   - `truenas_pool_realtime_used_bytes{pool}` (gauge) ← `pools.<name>.used`
   - `truenas_pool_realtime_available_bytes{pool}` (gauge) ← `pools.<name>.available`
   - `truenas_pool_realtime_total_bytes{pool}` (gauge) ← `pools.<name>.total`
   Only set when the key parses via `_as_float`; absent otherwise (never 0).
2. **Keep** the existing `read_bytes`/`write_bytes` probing exactly as is (if some middleware
   build ever sends rates, they'll light up), but fix their status in the parity mapping tables:
   they are opportunistic, not "active dedicated" — the note must say the documented/observed
   payload carries space stats, not rates.
3. Keep label = pool name (bounded), values floats.
4. HELP strings must state the source ("from the reporting.realtime event stream") consistent
   with neighboring realtime metrics.

## Compatibility rules that apply

- Adding metrics = minor-version-worthy; note in TASKS.md. No renames/removals here.
- New event-owned metrics **must** be in `events.py` ownership tables so that
  `_reset_poll_metrics` exclusion, freshness expiry, and collector-mode publishing all work.
  Verify each of those three behaviors in tests — this is the part most likely to be missed.

## Tests

In `tests/test_phase2_events.py` (or alongside existing realtime tests):

1. Dispatch the committed 25.10 fixture → assert
   `truenas_pool_realtime_{used,available,total}_bytes{pool="big_data"}` carry the fixture values
   and the read/write rate metrics have no samples.
2. Staleness: advance a monkeypatched `time.monotonic` past `event_stale_after_seconds` → new
   metrics expire to absent (mirror `test_collector_omits_expired_event_metrics`).
3. Poll-cycle survival: run `_reset_poll_metrics()` → event-owned pool realtime series must NOT
   be cleared (they're event-owned; verify exclusion works via `_EVENT_SOURCE_BY_METRIC_NAME`).
4. Payload with a non-dict pool entry or non-numeric values → no crash, no sample.

## Verification

```
python3 -m pytest tests/test_phase2_events.py tests/test_phase3_collector_mode.py tests/test_reliability.py -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

Read the regenerated parity rows for all five metrics and confirm they now tell the truth.

## Definition of done

- Three new per-pool realtime space gauges emit from the fixture payload; expire correctly;
  survive poll resets. Rate metrics' parity claims corrected. Generators re-run. validate.sh
  green. TASKS.md updated (note: minor-version-worthy).

## Outcome

_(fill in when done)_
