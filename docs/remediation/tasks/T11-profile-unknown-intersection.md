# T11 — Make `PROFILE_UNKNOWN` a true 25.10 ∩ 26.0 intersection

- **Priority:** P2
- **Size:** S
- **Depends on:** nothing (T12 and T14 build on this)
- **Review reference:** review-report.md finding D2

## Problem

`PROFILE_UNKNOWN` (`src/truenas_exporter/compat_profiles.py` ~153–164) declares
`target_version="common-intersection"` and a docstring promise of "common intersection", but is
actually built from `_V26_METHODS` / `_V26_EVENTS`, which **include** `V26_ADDED_METHODS`
(`container.query`, `smb.status`, `sharing.webshare.query`, `webshare.config`) and
`container.metrics` — none of which exist on 25.10.

**Failure scenarios:**
- A transient `system.version_short` failure on a healthy 25.10 box selects "unknown"
  (`runtime.py::_bootstrap_connection` ~946–955) → that cycle calls v26-only methods (fail →
  collector errors, and via `_should_runtime_skip_method` "method does not exist" matching, may
  permanently poison `_auto_skipped_methods` — see T14) **and** blocks `virt.instance.query` /
  `reporting.*graphs` as "removed" → metrics absent.
- A genuinely unknown version (24.x, 27.x) runs the v26 surface instead of the safest common set.

## Code to read (only this)

- `src/truenas_exporter/compat_profiles.py` — whole file (182 lines).
- `src/truenas_exporter/runtime.py` — `_bootstrap_connection` (~939–967),
  `_require_profile_method` (~1089–1109), `_collect_virt_metrics` head (~4017–4045: the
  `allows_method("container.query")` switch — this is how unknown-profile behavior manifests).
- `tests/test_removed_source_suppression.py` — parametrizes `PROFILE_UNKNOWN`; its expectations
  will change.

## Required behavior

1. Define the unknown profile as the intersection:
   - `reviewed_methods = _V25_METHODS & _V26_METHODS` (equivalently `_V25_METHODS -
     V26_REMOVED_METHODS`; note this *excludes* `V26_ADDED_METHODS`).
   - `telemetry_methods` analogous.
   - `reviewed_events = _V25_EVENTS & _V26_EVENTS` (i.e. `reporting.realtime`, `app.stats` —
     both instance-metrics event names drop out; that's correct: neither name is safe to assume).
   - `removed_methods`: keep `V26_REMOVED_METHODS` listed so the suppression logging still
     explains *why* a v25-only method is blocked under unknown.
   - `default_event_subscriptions`, `query_limit_methods` recomputed from the above.
2. Fix `target_version` / docstring to match reality (they already say intersection — the sets
   are what change).
3. Consequences to verify (not change): on unknown profile `_collect_virt_metrics` must now take
   the `virt.instance.query` branch? **No** — with the intersection, `container.query` is not
   allowed AND `virt.instance.query` is removed-on-v26 → also not allowed; instance metrics stay
   absent under unknown. That is the intended safe behavior; assert it in a test.
4. Keep `PROFILES` mapping and `get_profile` fallback semantics unchanged.
5. The module-ending asserts (`_V25_EVENTS <= DOCUMENTED_EVENT_NAMES` etc.) must still hold; add
   an equivalent assert for the unknown profile's events.

## Compatibility rules

- No metric contract changes. Behavioral: systems that fail version detection now collect a
  slightly smaller, guaranteed-safe method set. Patch-worthy. The parity generator imports
  `PROFILE_26_0`/`V26_ADDED_EVENTS` — confirm it does not bake unknown-profile assumptions
  (grep `PROFILE_UNKNOWN` in `scripts/`); regenerate parity anyway.

## Tests

1. Assert set identities directly: `PROFILE_UNKNOWN.reviewed_methods ==
   PROFILE_25_10.reviewed_methods & PROFILE_26_0.reviewed_methods`, and that no
   `V26_ADDED_METHODS` member is allowed by unknown.
2. `tests/test_removed_source_suppression.py` — re-run; update expectations where they assumed
   unknown==v26 (e.g. `smb.status`/`container.query` reaching the transport under
   `PROFILE_UNKNOWN` must now be blocked).
3. Behavior test: exporter with `PROFILE_UNKNOWN` + RecordingClient → neither `container.query`
   nor `virt.instance.query` is called.

## Verification

```
python3 -m pytest tests/test_removed_source_suppression.py tests/test_api_catalog.py tests/test_phase1_metrics.py -q
python3 scripts/generate_api_exporter_parity.py
./scripts/validate.sh
```

## Definition of done

- Unknown profile provably equals the intersection; v26-only methods never called under it;
  suppression logging preserved; tests updated; validate.sh green; TASKS.md updated.

## Outcome

Implemented. `PROFILE_UNKNOWN` now uses explicit 25.10/26.0 intersection sets for
reviewed methods, telemetry methods, reviewed events, default event
subscriptions, and query-limit methods while preserving `V26_REMOVED_METHODS` for
suppression logging and leaving `PROFILES` / `get_profile` fallback semantics
unchanged.

Tests now assert that unknown reviewed methods/events equal the profile
intersection, that v26-added methods are disjoint from unknown, and that
`PROFILE_UNKNOWN` does not transport either `container.query` or
`virt.instance.query` during virt collection. Stale unknown==v26 expectations for
container, webshare, SMB status, and `container.metrics` were updated.

Verification:
- `rg -n "PROFILE_UNKNOWN" scripts` returned no matches; parity generation does
  not bake old unknown==v26 assumptions.
- `python3 -m pytest tests/test_removed_source_suppression.py tests/test_api_catalog.py tests/test_phase1_metrics.py -q`
  passed: 74 tests.
- `python3 scripts/generate_api_exporter_parity.py` completed; generated parity
  artifacts were already current.
- `./scripts/validate.sh` exited 0: ruff, mypy, 209 tests at 91.42% coverage,
  dashboard validation, parity checks, public-release audit, Docker image build,
  and version smoke all passed with `validation_ok`.
