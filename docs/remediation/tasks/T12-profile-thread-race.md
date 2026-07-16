# T12 — Fix cross-thread `compatibility_profile` race

- **Priority:** P2
- **Size:** M
- **Depends on:** T11 (do T11 first; it shrinks the blast radius of a wrong profile)
- **Review reference:** review-report.md finding D3

## Problem

`self.compatibility_profile` is a single mutable attribute on `TrueNASExporter`, written by
`_bootstrap_connection` from **two threads** — the scrape thread (`scrape_once`,
`runtime.py` ~3261) and the event thread (`_event_stream_loop`, ~2003) — and read on every
`_require_profile_method` / `allows_method` check in both threads.

**Failure scenario:** the event thread reconnects mid-scrape and its `system.version_short`
call fails transiently → it assigns `get_profile("unknown")` → the scrape thread, halfway
through its collector list on a healthy 25.10 box, suddenly has v25 methods blocked
("outside the unknown compatibility profile"), producing a partial cycle and misleading
`profile_method_blocked` collector errors. The reverse flip can also occur mid-cycle.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `__init__` (~721–764), `_bootstrap_connection`
  (~939–967), `_require_profile_method` (~1089), `_is_safe_read_method` (~1363),
  `_profile_normalized_bytes` (~970), the event-loop profile checks (~2006–2022, 2077),
  `scrape_once` bootstrap (~3261).
- `tests/test_runtime_lifecycle.py` (thread/lifecycle test patterns).

## Required behavior

Make profile selection race-free with **per-connection resolution + monotonic shared update**:

1. `_bootstrap_connection` returns the resolved profile (and version string) instead of blindly
   assigning; each loop (scrape cycle, event connection) captures it in a **local** variable and
   passes it down to the code paths it drives. Practical approach given the code shape:
   - Add an optional `profile` parameter (defaulting to `self.compatibility_profile`) to the few
     chokepoints: `_require_profile_method`, `_is_safe_read_method`,
     `_profile_normalized_bytes`, or
   - Simpler and acceptable: keep the attribute but make the **update rule** monotonic — only
     replace the current profile when the new detection produced a *concrete* profile
     ("25.10"/"26.0"); a detection *failure* must not downgrade an already-detected concrete
     profile to "unknown" (log it instead). First-ever detection failure (startup) may still
     select "unknown".
   Choose ONE approach and state the choice + rationale in Outcome. The monotonic rule is the
   minimum bar; per-connection locals are the cleaner fix if the diff stays reviewable.
2. Whichever approach: a concrete→different-concrete change (TrueNAS upgraded live, e.g.
   25.10→26.0 detected by the next scrape) must still take effect and must clear
   `_auto_skipped_methods` (coordinates with T14 — if T14 is already done, just call its reset
   hook; if not, add the clear here and note it).
3. Attribute writes happen from two threads → guard the assignment + the auto-skip clear with an
   existing lock (`self._lock` is an RLock; a dedicated small lock is also fine). Reads of an
   attribute reference are atomic in CPython — document that assumption in a comment.

## Compatibility rules

- Pure behavior/robustness fix; no metric or config changes. Patch-worthy.

## Tests

1. Monotonic rule: bootstrap succeeds with "25.10", then a second bootstrap's version call
   raises → profile stays 25.10 (assert), a `version_detection` collector error is recorded.
2. Legit upgrade: "25.10" then "26.0" → profile becomes 26.0 and `_auto_skipped_methods` is
   cleared.
3. Startup failure: first bootstrap raises → profile is unknown (existing behavior preserved).
4. If you chose per-connection locals: a scrape driven with an injected stale profile must not
   be affected by mutating `self.compatibility_profile` mid-run (simulate by swapping the
   attribute between collector calls with a fake client).

## Verification

```
python3 -m pytest tests/test_runtime_lifecycle.py tests/test_removed_source_suppression.py tests/test_phase1_metrics.py -q
./scripts/validate.sh
```

## Definition of done

- A transient version-detection failure can no longer flip a healthy system's profile mid-run;
  genuine version changes still apply; choice documented; tests prove all three transitions;
  validate.sh green; TASKS.md updated.

## Outcome

Implemented the monotonic shared update rule rather than per-connection local
profile plumbing. This keeps the diff small for the current runtime shape while
still preventing a transient reconnect/version-detection failure in either
thread from downgrading an already detected concrete profile to `unknown`.

`_bootstrap_connection` now routes all profile changes through a locked helper.
Unknown results are applied only before any concrete profile has been detected;
after a successful `25.10` or `26.0` detection, later transient failures still
record the `version_detection` collector error but leave the active concrete
profile intact. Legitimate concrete profile changes still replace the active
profile, and concrete-to-different-concrete changes clear `_auto_skipped_methods`
under the same lock. Profile reads remain simple and lock-free, with a code
comment documenting the CPython atomic attribute-reference read assumption at
the guarded write site.

Added lifecycle regression coverage for: `25.10` followed by a detection
exception staying on `25.10` while recording `version_detection`; `25.10` then
`26.0` updating the profile and clearing `_auto_skipped_methods`; and a
first-ever detection failure selecting `unknown`.

Verification passed:

- `python3 -m pytest tests/test_runtime_lifecycle.py tests/test_removed_source_suppression.py tests/test_phase1_metrics.py -q`
  (`90 passed`)
- `./scripts/validate.sh` (`212 passed`, 91.45% coverage,
  `dashboard_ok panels=318 metric_references=287`, generated checks,
  `public_release_audit_ok`, Docker image build, version smoke `5.2.0`,
  `validation_ok`)

No live smoke was run because no read-only TrueNAS API target/key was available.
This is patch-worthy: behavior/robustness only, with no metric or config
contract changes.
