# T16 — Reduce cadence of server-heavy queries

- **Priority:** P2 (performance — load on the TrueNAS middleware, not the exporter)
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md finding C3

## Problem

Two queries force disproportionate server-side work **every poll cycle** (default 30 s):

1. `disk.temperature_agg(disk_names, 7)` (`src/truenas_exporter/runtime.py` ~3571) — asks
   middleware to aggregate **7 days** of netdata temperature history per disk, per cycle, to
   produce min/max/avg gauges that change slowly by construction.
2. `pool.snapshot.query` with `order_by: ["properties.creation.parsed"]`, `limit: 1`
   (~4456–4469) — forces a server-side sort of the entire snapshot set (can be 100k+ rows on
   busy systems) every cycle, to find the oldest snapshot's timestamp — a value that changes at
   most when the oldest snapshot is deleted.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` ~3542–3596 (disk block), `_collect_snapshot_metrics`
  (~4446–4483), `__init__` (~721–765, for adding cadence state), `_reset_poll_metrics`
  exclusion list `_POLL_RESET_EXCLUDED_NAMES` (~688–700) — **critical interaction, see below**.

## Required behavior

1. Add a simple per-method refresh cadence: run these two calls only every N cycles
   (suggested: temperature_agg every 10 cycles ≈ 5 min; snapshot-oldest every 10 cycles),
   caching the last successful values in instance state and re-emitting the cached values on
   the in-between cycles. Constants in code with a comment; no new env vars unless a reviewer
   asks.
2. **Interaction with the wipe policy:** `_reset_poll_metrics` clears these gauges every cycle,
   so "skip the call" alone would leave the metrics absent 9 of 10 cycles. You must re-emit
   from the cache each cycle (e.g. a small `_emit_cached_disk_temp_agg()` re-setting
   `DISK_TEMP_AGG_C` / `SNAPSHOT_OLDEST_TS` from stored floats). Cache invalidation: drop the
   cache when the disk list changes (temperature agg) and always attempt refresh on the Nth
   cycle; on refresh failure keep serving the cache but count a collector error, and drop the
   cache if it hasn't refreshed for 3×N cycles (bounded staleness, mirroring the T13 guard).
3. `SNAPSHOT_TOTAL_COUNT` (`_query_count(pool.snapshot.query)`) stays every-cycle — a
   server-side count is cheap; only the *sorted* query is throttled.
4. Behavior when the metric was never fetched (startup): absent until the first successful
   fetch, which must happen on the **first** cycle (cadence counts from 0).

## Compatibility rules

- Values may now be up to ~5 minutes old; both metrics are slow-moving by nature. Document the
  cadence in each metric's HELP suffix (e.g. "refreshed every ~5 minutes") — HELP change ⇒
  regenerate contract/parity/dashboard.

## Tests

1. Cycle 1 fetches and emits; cycles 2..N-1 do not call the method (RecordingClient) but the
   samples are still present with cached values; cycle N re-fetches.
2. Refresh failure at cycle N → cached values still served + collector error counted; after
   3×N without success → samples absent.
3. Disk list change → temperature agg refetches immediately.

## Verification

```
python3 -m pytest tests/test_phase1_metrics.py -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

## Definition of done

- Heavy queries run at ~1/10th cadence with values continuously served and bounded staleness;
  tests prove call cadence + cache + expiry; validate.sh green; TASKS.md updated.

## Outcome

Implemented per-instance 10-cycle refresh cadence for
`disk.temperature_agg(disk_names, 7)` and the sorted oldest-snapshot
`pool.snapshot.query`, with cached re-emission after `_reset_poll_metrics`
clears gauges each scrape. Both caches keep serving the last successful values
after refresh failures, increment/log collector errors on failed refreshes, and
drop cached values after 3x cadence cycles without a successful refresh.

`SNAPSHOT_TOTAL_COUNT` remains an every-cycle `_query_count(pool.snapshot.query)`
call. Disk temperature aggregate cache state is invalidated immediately when
the disk list changes. No API methods, metric names, or label sets changed;
only the required HELP text cadence suffixes changed, and generated contract /
parity artifacts were regenerated.

Tests added in `tests/test_phase1_metrics.py` cover first-cycle fetch, skipped
cycles re-emitting cached samples, cycle-10 refetch, refresh failure with
collector error accounting, cache expiry, and disk-list-triggered refetch.
Verification passed locally:
`python3 -m pytest tests/test_phase1_metrics.py -q` (`55 passed`);
`python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py`;
and `./scripts/validate.sh` (ruff, mypy, `226 passed`, 91.55% coverage,
dashboard validation, generated checks, `public_release_audit_ok`, Docker image
build, container version smoke `5.2.0`, and `validation_ok`).
