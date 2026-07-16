# T17 — Legacy mode: `/metrics` must not block for the whole poll cycle

- **Priority:** P3 (default mode is unaffected)
- **Size:** M
- **Depends on:** nothing
- **Review reference:** review-report.md finding C4

## Problem

In `legacy` mode, `/metrics` acquires `exporter._lock` (`src/truenas_exporter/http.py` ~59–61,
wired in `runtime.py::main` ~5071–5075 with `lock_metrics=True` default), and `scrape_once`
holds that same lock for the **entire** serial API cycle (`runtime.py` ~3119). A Prometheus
scrape landing mid-cycle blocks up to `SCRAPE_BUDGET_SECONDS` (25 s) — past the default 10 s
Prometheus scrape timeout ⇒ failed scrapes whenever timing collides.

Collector mode (default) already solves this with the immutable-snapshot pattern
(`TrueNASCollector` + `metric_snapshot()`, `runtime.py` ~898–906, 5011–5021).

## Decision required (make it, document it)

Per `docs/VERSIONING.md`, legacy mode "remains available for one compatibility release" after
collector became the default. Two acceptable resolutions — pick based on effort:

- **Option A (preferred if diff is small):** give legacy mode the same snapshot behavior:
  serve `/metrics` from the last complete registry snapshot (reuse `TrueNASCollector` against
  the default REGISTRY families) instead of locking; keep event updates flowing into the
  snapshot by republishing after each event dispatch (legacy mode already calls
  `_publish_cached_events_to_default_registry` per event — add `_publish_metric_snapshot()`
  there, throttled to ≥ 1/s to bound overhead).
- **Option B (if A gets invasive):** keep the lock but *bound the wait*: serve the previous
  response bytes if the lock isn't acquired within ~2 s (lock.acquire(timeout=2)), plus
  document the limitation in the README env-var table. Less clean; only if A is genuinely
  risky.

## Code to read (only this)

- `src/truenas_exporter/http.py` (73 lines).
- `src/truenas_exporter/runtime.py` — `main()` (~5039–5095), `TrueNASCollector` (~5011),
  snapshot helpers (~898–906), `_dispatch_event` tail (~1978–1983), `scrape_once` tail
  (~3763–3774).
- `tests/test_http_integration.py`, `tests/test_phase3_collector_mode.py`.

## Required behavior (for Option A)

1. Legacy `main()` path registers the snapshot-serving app (no per-request `exporter._lock`).
2. `scrape_once` already publishes the snapshot at cycle end; add snapshot republish on event
   dispatch in legacy mode (throttled).
3. `/metrics` during a long scrape returns the previous complete cycle immediately —
   consistency preserved (that's the point of the snapshot), latency bounded.
4. `/healthz`, `/readyz`, landing page unchanged.

## Compatibility rules

- Legacy mode's observable metric *content* must remain equivalent (same families/values as the
  live registry at last publish). Freshness of event metrics in legacy mode must not regress
  below ~1 s (hence the throttled republish, not per-cycle only).

## Tests

1. Simulate a scrape-in-progress: hold `exporter._lock` in the test thread, request `/metrics`
   (existing HTTP-integration harness) with a short client timeout → response arrives (fails on
   current code in legacy mode).
2. Event dispatch in legacy mode → new value visible in `/metrics` within the throttle window
   without a poll cycle.
3. Existing legacy-mode tests keep passing (update only those asserting lock behavior).

## Verification

```
python3 -m pytest tests/test_http_integration.py tests/test_phase3_collector_mode.py tests/test_runtime_lifecycle.py -q
./scripts/validate.sh
```

## Definition of done

- `/metrics` p99 latency in legacy mode no longer coupled to the poll cycle; event freshness
  preserved; consistency preserved; option choice + rationale in Outcome; validate.sh green;
  TASKS.md updated.

## Outcome

Completed 2026-07-16 with Option A. The diff was small and reused the existing
`TrueNASCollector` immutable snapshot path, so legacy mode now registers a
snapshot-serving registry with `lock_metrics=False` instead of acquiring
`exporter._lock` per `/metrics` request.

`scrape_once` continues publishing the complete snapshot at cycle end. Legacy
event dispatch now republishes the snapshot after updating event-owned metrics;
publishes are throttled to at most once per second by scheduling one delayed
publish for event bursts, so a single event still becomes visible within the
throttle window without waiting for another poll cycle.

Tests added/updated:

- `tests/test_http_integration.py`: legacy `/metrics` returns while
  `exporter._lock` is held.
- `tests/test_phase3_collector_mode.py`: legacy `main()` wires the snapshot
  registry without metrics locking, and legacy event dispatch updates `/metrics`
  through the throttled snapshot path.

Verification:

- `python3 -m pytest tests/test_http_integration.py tests/test_phase3_collector_mode.py tests/test_runtime_lifecycle.py -q`
  passed: 34 passed, 3 skipped.
- `./scripts/validate.sh` passed, including Ruff, mypy, full pytest/coverage
  (229 passed, 91.50% coverage), generated artifact checks, public release
  audit, Docker image build, and container version smoke.

No metric names, types, HELP text, or label sets changed. No live TrueNAS calls
or mutating API calls were added.
