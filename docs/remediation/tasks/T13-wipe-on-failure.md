# T13 — Don't wipe all metrics on pre-auth connection failure

- **Priority:** P2
- **Size:** M — this is a *policy* change; implement exactly the spec below, no more
- **Depends on:** nothing
- **Review reference:** review-report.md finding D4

## Problem

`scrape_once` (`src/truenas_exporter/runtime.py` ~3113–3774) resets every polled metric at the
**start** of the cycle (`_reset_poll_metrics()` at ~3124 plus the explicit `.clear()` block),
*before* attempting to connect. If the connection or authentication fails at second 0, the cycle
ends with everything absent, and in collector mode the emptied registry is still published as the
new snapshot (~3763–3774).

**Failure scenario:** a 1-second network blip at cycle start → ~400 series vanish for a full
`SCRAPE_INTERVAL_SECONDS` (30 s+) window; every dashboard shows holes; `absent()`-style alerts
fire, even though the exporter knew nothing new about the target.

The absent-on-failure *policy* stays (never serve stale data as if fresh). The fix is only about
**when** the wipe happens: a cycle that never got authenticated has learned nothing and should
leave the previous cycle's snapshot in place, with `truenas_up 0` marking it.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `scrape_once` top through the connection block
  (~3113–3260), the failure tail (~3763–3774), `_reset_poll_metrics` (~778–791),
  `_publish_metric_snapshot` (~903–906), `is_ready` (~884).
- `tests/test_runtime_lifecycle.py`, `tests/test_phase3_collector_mode.py` — snapshot/lifecycle
  test patterns.

## Required behavior

1. Restructure `scrape_once` so the connection is established and `_bootstrap_connection`
   (auth + version detection) succeeds **before** `_reset_poll_metrics()` and the `.clear()`
   block run. Concretely: move the reset+clear block to just after a successful
   `_bootstrap_connection(client)` inside the `with JsonRpcWsClient(...)` body.
   - The reset must still happen inside `self._lock` (it already will be — the lock wraps the
     whole cycle).
   - `SCRAPE_DURATION` semantics: keep `started` where it is (whole-cycle timing including the
     connect attempt is fine; do not overthink).
2. On pre-auth failure (connect/auth/version raise): set `SCRAPE_SUCCESS`/`truenas_up` to 0, set
   `SCRAPE_DURATION`, do **not** touch the polled metrics, and:
   - collector mode: **do not** republish the snapshot (the previous complete snapshot keeps
     serving; `truenas_up` is part of the registry — make sure the served snapshot reflects
     up=0! In collector mode the snapshot is the only thing served, so you MUST republish at
     least the health metrics. Simplest correct approach: always republish the snapshot as
     today — the registry still holds last cycle's values because you didn't wipe them — the
     snapshot will therefore contain previous values + `truenas_up 0`.)
   Re-read that: because the wipe moved *inside* the success path, the "keep previous data"
   behavior falls out naturally and the existing unconditional republish becomes correct. The
   actual diff is small.
3. On post-auth failure (some collector raised after the wipe): current behavior is unchanged —
   the cycle was wiped and partially refilled, `truenas_up 0`, snapshot published. Each
   collector already isolates its own failures, so this only happens for mid-cycle transport
   death, where partial-with-up=0 is the honest representation.
4. Freshness guard: previous values must not survive forever across repeated failures.
   `is_ready()` already flips `/readyz` after ~2 intervals. Add one guard: if the last
   *successful* cycle is older than `max(3 * interval_seconds, 300)`, run the full reset+publish
   anyway so ancient data isn't served indefinitely (tunable constant, documented in a comment).
5. `LAST_SCRAPE_TS` keeps meaning "last attempt" (unchanged).

## Compatibility rules

- No contract changes. This alters failure-mode visibility: document in Outcome that dashboards
  should key on `truenas_up == 0` (they always should have). Patch-worthy.

## Tests

1. Fake client whose construction/auth raises → previously-populated gauge (set it directly in
   the test before calling `scrape_once`) still has its value after the failed cycle;
   `truenas_up == 0`; collector-mode snapshot contains both.
2. Auth succeeds, later collector raises mid-cycle → wipe happened (pre-set gauge gone),
   `truenas_up == 0` (existing behavior; pin it).
3. Staleness guard: monkeypatch monotonic so the last success is > the guard window → failed
   cycle now wipes and publishes absence.
4. Existing lifecycle tests must still pass (they may assert the old wipe-first order — update
   them only where the assertion is specifically about pre-connect wiping).

## Verification

```
python3 -m pytest tests/test_runtime_lifecycle.py tests/test_phase3_collector_mode.py tests/test_http_integration.py -q
./scripts/validate.sh
```

## Definition of done

- A pre-auth failure no longer blanks the exporter's output; `truenas_up 0` visible; stale-guard
  bounded; post-auth semantics unchanged; tests prove all paths; validate.sh green; TASKS.md
  updated.

## Outcome

_(fill in when done)_
