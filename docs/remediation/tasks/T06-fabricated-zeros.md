# T06 — Eliminate fabricated zeros on partial failure

- **Priority:** P1
- **Size:** S
- **Depends on:** nothing
- **Review reference:** review-report.md finding A6

## Problem

Two places violate the exporter's zero-vs-absent policy by publishing `0` when the API did not
answer:

**(1) Job flags** — `_collect_job_metrics` (`src/truenas_exporter/runtime.py` ~1225–1325):

```python
JOB_ABORTABLE_ACTIVE_COUNT.set(0)      # line ~1251
JOB_TRANSIENT_ACTIVE_COUNT.set(0)      # line ~1252
...
except Exception:
    self._collector_error("jobs", "core.get_jobs detail query failed")
    return                              # line ~1279 — zeros remain published
```

If the per-state count queries succeed (`truenas_job_active_count = 7`) but the detail query
fails, `truenas_job_abortable_active_count` / `truenas_job_transient_active_count` report `0` —
"no abortable jobs" fabricated from "API didn't answer".

**(2) Reporting service** — `_collect_misc_configs` (~4801–4813):

```python
reporting_services = self._query_service_enable_map(client, ("netdata", "reporting"))
if reporting_services:
    ...
else:
    REPORTING_ENABLED.set(0)            # line ~4810
```

An empty match (service under a different name on this TrueNAS version) publishes
`truenas_reporting_enabled 0` — "unknown" reported as "disabled".

## Code to read (only this)

- `src/truenas_exporter/runtime.py` ~1225–1325 (`_collect_job_metrics`), ~4795–4813
  (reporting block in `_collect_misc_configs`), and `_reset_poll_metrics` (~778–791) to
  understand the NaN-until-set baseline.
- `tests/test_phase1_metrics.py` — find existing job-metric tests to extend.

## Required behavior

1. **Jobs:** do not pre-set the abortable/transient gauges to 0. Compute them from the detail
   query results and set them **only after** the detail query succeeds (move the two `.set(0)`
   lines so they participate in the same success path as the loop's final
   `JOB_ABORTABLE_ACTIVE_COUNT.set(abortable_count)`). Special case that must keep working:
   `total_active == 0` → it is *correct* to publish 0 for both (no active jobs means no
   abortable/transient ones) — keep an explicit `set(0)` in that early-return branch.
2. **Reporting:** in the `else` branch (empty service map), publish nothing — the gauge stays
   NaN from `_reset_poll_metrics`. Only `set(0/1)` when the queried service row was actually
   found (`"netdata" in reporting_services or "reporting" in reporting_services`).
3. Grep for other `.set(0)` calls that execute before their data source has succeeded and list
   any you find in TASKS.md "Discovered" (do not fix them here unless they are in the two
   functions above).

## Compatibility rules

- Values change from wrong-0 to absent in failure paths only. Patch-worthy behavior fix; no
  contract/generator changes needed (names/HELP/labels untouched).

## Tests

1. Fake client: state-count queries return 3 and 4; detail query raises → assert
   `truenas_job_active_count == 7` and abortable/transient gauges have NaN value (use
   `math.isnan(GAUGE._value.get())` per existing test style) — must fail on current code.
2. Fake client: counts return 0 → abortable/transient == 0 (the legitimate zero).
3. Fake client: `service.query` returns `[]` for the reporting map → `truenas_reporting_enabled`
   NaN; returns netdata row with `enable: false` → 0; `enable: true` → 1.

## Verification

```
python3 -m pytest tests/test_phase1_metrics.py -q
./scripts/validate.sh
```

## Definition of done

- Failure paths publish absence, legitimate zeros still publish 0, tests prove both, validate.sh
  green, TASKS.md updated.

## Outcome

- Removed the premature `JOB_ABORTABLE_ACTIVE_COUNT` and `JOB_TRANSIENT_ACTIVE_COUNT`
  zero assignments before the active-job detail query succeeds. The legitimate
  `total_active == 0` path still publishes explicit zeroes.
- Removed the `REPORTING_ENABLED.set(0)` fallback for an empty reporting service
  map, so `truenas_reporting_enabled` stays NaN unless `netdata` or `reporting`
  is present.
- Added fixture/synthetic regressions in `tests/test_phase1_metrics.py` for job
  detail failure, no-active-job legitimate zeroes, and reporting service unknown
  / disabled / enabled states.
- Regenerated API/exporter parity artifacts after the runtime evidence line
  numbers changed.
- Grepped `src/truenas_exporter/runtime.py` for `.set(0)` and found no
  additional out-of-scope pre-success fabricated-zero candidates.
- Verification: `python3 -m pytest tests/test_phase1_metrics.py -q` passed
  (`40 passed`); `./scripts/validate.sh` passed and exited `validation_ok`.
