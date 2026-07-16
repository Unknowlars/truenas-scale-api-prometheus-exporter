# T14 — Re-try auto-skipped methods on profile change / periodically

- **Priority:** P2
- **Size:** S
- **Depends on:** T11 (and coordinates with T12 — check TASKS.md; T12 may already clear the set
  on profile change)
- **Review reference:** review-report.md finding D5

## Problem

`_auto_skipped_methods` (`src/truenas_exporter/runtime.py` ~764, populated in `_safe_call_auto`
~1431–1445) permanently skips any method that once failed with an
`_AUTO_SKIP_ERROR_PATTERNS` match ("method not found", "missing required argument", …) — for the
lifetime of the process. Legit triggers for un-skipping:

- The compatibility profile flips (wrong profile during a D2/D3 episode caused spurious
  "not found" errors).
- TrueNAS is upgraded live (25.10 → 26.0): methods appear.
- A feature is configured server-side making its method start existing.

Long-running daemons (weeks) accumulate permanently-dark methods.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `__init__` (~764), `_safe_call_auto` (~1431–1445),
  `_bootstrap_connection` (~939–967), `scrape_once` bootstrap region (~3261).
- `src/truenas_exporter/method_safety.py` — `_AUTO_SKIP_ERROR_PATTERNS` (~29–34).

## Required behavior

1. **Clear on profile change:** whenever the resolved profile object changes identity/name
   (25.10 → 26.0, unknown → concrete, …), clear `_auto_skipped_methods` (and log at INFO with
   the count cleared). Implement as a small helper (e.g. `_note_profile(profile)`) called from
   `_bootstrap_connection`, so T12's monotonic-update logic and this share one place.
2. **Periodic amnesty:** additionally, clear the set on a slow cadence so non-profile-related
   causes heal — e.g. record `_auto_skipped_at: dict[str, float]` and retry a method when its
   entry is older than 24 h, or simpler: clear the whole set every N cycles
   (N = `max(1, 86400 // interval_seconds)`), whichever keeps the diff smaller. A retried method
   that still fails just re-enters the set at the cost of one call per day — acceptable.
3. Keep the skip behavior itself unchanged (patterns, counters,
   `auto_discovery_skipped` collector error).

## Compatibility rules

- No contract changes. Patch-worthy.

## Tests

1. Method fails with "method does not exist" → skipped on next call (existing behavior — pin it
   if untested).
2. Profile change (call the helper with a different profile) → set cleared → method attempted
   again.
3. Amnesty: simulate time/cycle passage → method attempted again; still-failing method
   re-enters the skip set without error spam (COLLECTOR_ERRORS counted once per re-attempt).

## Verification

```
python3 -m pytest tests/test_removed_source_suppression.py tests/test_phase1_metrics.py -q
./scripts/validate.sh
```

## Definition of done

- Auto-skips heal on profile change and within ≤ 24 h otherwise; no per-cycle retry storms;
  tests prove skip/clear/retry; validate.sh green; TASKS.md updated.

## Outcome

_(fill in when done)_
