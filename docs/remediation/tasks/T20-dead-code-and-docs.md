# T20 — Remove dead code and the misleading version-history docstring

- **Priority:** P3 (cleanup — do late; low conflict risk but touches shared files)
- **Size:** S
- **Depends on:** best done after T01–T16 to avoid churn (check TASKS.md first)
- **Review reference:** review-report.md item (e)8

## Problem

1. **The 230-line module docstring** at the top of `src/truenas_exporter/runtime.py`
   (lines 1–234) is a v1→v5.1 changelog describing many behaviors that **no longer exist** —
   e.g. "12 default event subscriptions" incl. `pool.scan`, `alert.list`, `disk.query` events
   (the real default is 4: `api_catalog.py` ~749–754), vdev error extraction being active, etc.
   It actively misleads maintainers and agents.
2. **Dead code:** `_merge_event_snapshot` (`runtime.py` ~793–812) is called only from tests
   (`tests/test_reliability.py`, `tests/test_runtime_lifecycle.py`).
3. **No-op stub collectors** kept only as documentation:
   `_collect_smart_test_results` (~2983), `_collect_ups_metrics` (~4260),
   `_collect_tn_connect` (~4353), `_collect_truecommand_status` (~4360),
   `_collect_disk_used_metrics` (~4566) — each has a docstring explaining *why* it does nothing.
4. Stray artifacts: the orphaned "Maximum number of out-of-order…" comment (~708–710) refers to
   a constant that lives in `transport.py`; duplicated section-divider comments (~2813–2814,
   5024–5030).

## Required behavior

1. Replace the giant docstring with ≤ 25 lines: what the module is, the two threads, the two
   modes, a pointer to `docs/api-exporter-parity.md` for the field contract and to git history
   for changelogs. **Preserve any sentence that is load-bearing documentation of current
   behavior** (e.g. the "disls" key note is still true — move it next to the code that handles
   it if not already commented there; it is — `_cache_realtime_event` reads clearly, verify).
2. `_merge_event_snapshot`: keep it **only if** a task (T17 option A) started using it;
   otherwise delete it and rewrite the two tests to exercise the equivalent public behavior
   (`_publish_cached_events_to_default_registry` + snapshot render) — the tests' *intent*
   (freshness filtering) must survive, pointed at real code.
3. No-op stubs: keep the *knowledge*, drop the ceremony — replace each stub method + its
   call-site with a comment block at the call-site (or a short module-level note) stating why
   the source is not collected (secrets / no documented method). Removing the methods must not
   change any metric (they set nothing).
4. Delete the stray comment artifacts.
5. This task must produce **zero metric/behavior changes**: the metric contract JSON diff after
   regeneration must be empty.

## Code to read

- `runtime.py` lines 1–234, 700–812, 2810–2986, 4255–4370, 4560–4570, 5020–5035.
- The two test files that call `_merge_event_snapshot`.

## Tests

- Existing suite is the guard. If you delete `_merge_event_snapshot`, its two tests must be
  rewritten (not deleted) to cover the same freshness behavior through public paths.

## Verification

```
python3 -m pytest tests/ -q
python3 scripts/generate_metric_contract.py --check   # must pass with NO diff
python3 scripts/generate_api_exporter_parity.py       # diff should be line-number-only churn
./scripts/validate.sh
```

Note: the parity generator embeds `runtime.py` line numbers as evidence
(`runtime_evidence` fields) — big deletions shift them, so a large parity diff of line numbers
is expected and fine; field/status changes are not.

## Definition of done

- Docstring truthful and short; no dead/no-op code; zero contract diff; coverage still ≥ 85%;
  validate.sh green; TASKS.md updated.

## Outcome

Completed 2026-07-16:

- Replaced the misleading historical runtime changelog with a short current
  module summary covering the scrape/event threads, collector/legacy modes,
  generated parity contract, and git-history changelogs.
- Removed `_merge_event_snapshot`; the two freshness tests now exercise
  `_publish_cached_events_to_default_registry()` plus `TrueNASCollector`
  snapshots.
- Removed no-op collector stubs for SMART test results, UPS, TrueNAS Connect,
  TrueCommand, and disk-used metrics. Their safety/source notes now live at the
  scrape call sites, and existing guard tests assert the absent collector/metric
  behavior.
- Deleted stray comment/divider artifacts and moved the current `disls`
  realtime disk-map note next to the parser.
- Regenerated API/exporter parity artifacts for runtime line-number evidence
  churn only. `python3 scripts/generate_metric_contract.py --check` passed with
  no metric contract diff.
- Verification passed: `python3 -m pytest tests/ -q` (`233 passed, 4 skipped`),
  `python3 scripts/generate_metric_contract.py --check`,
  `python3 scripts/generate_api_exporter_parity.py`, and
  `./scripts/validate.sh` (`237 passed`, 91.40% coverage, dashboard validation,
  generated checks, `public_release_audit_ok`, Docker build, version smoke
  `5.2.0`, `validation_ok`).
- Versioning: patch-worthy cleanup only; no metric names, types, HELP text,
  label sets, or API calls changed.
