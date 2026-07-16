# T08 — Emit task outcome metrics (replication / cloudsync / rsync / snapshot tasks)

- **Priority:** P1 (biggest operational blind spot)
- **Size:** L — budget a full session; do not combine with anything else
- **Depends on:** nothing
- **Review reference:** review-report.md section (b) rows 1–4; finding table "TASK_STATE dead"

## Problem

`truenas_task_state{task_type,name,state}` and
`truenas_task_last_run_timestamp_seconds{task_type,name}` are declared
(`src/truenas_exporter/metrics.py` ~302–311), cleared every cycle, and **never populated**. The
collectors (`_collect_task_metrics`, `runtime.py` ~2631–2701) select only `["id", "enabled"]`
from `replication.query`, `cloudsync.query`, `rsynctask.query`, `pool.snapshottask.query`.

Consequence: a replication task that has failed every night for a month is invisible in
Prometheus. This was the review's #1 recommended coverage fix.

API reality (verified against `docs/truenas-api/methods/`):
- `replication.query` → `state` field: *object*, "Current state information for the replication
  task" (typed opaquely in the docs; at runtime it is middleware's EphemeralState:
  `{"state": "FINISHED"|"ERROR"|"RUNNING"|..., "datetime": {...}, "error": ...}`), plus `job`
  (object|null).
- `cloudsync.query` → `job` object|null with `state`, `progress.percent`, `time_finished`.
- `rsynctask.query` → `job` object|null (same job shape).
- `pool.snapshottask.query` → `state` object; note the nested schema at
  `docs/truenas-api/methods/replication/query.md` line ~926 shows snapshot-task `state.state` as
  a documented **string**.

## Code to read (only this)

- `src/truenas_exporter/runtime.py` — `_export_task_list` + `_collect_task_metrics`
  (~2609–2701); `_parse_ts` usage examples elsewhere (e.g. alert collector ~1198).
- `src/truenas_exporter/metrics.py` ~301–312 (TASK_* declarations).
- `src/truenas_exporter/collection.py` — `_parse_ts`, `_str_label`.
- Doc files: `docs/truenas-api/methods/replication/query.md` (state/job sections),
  `docs/truenas-api/methods/cloudsync/query.md` (job section),
  `docs/truenas-api/methods/rsynctask/query.md`, `docs/truenas-api/methods/pool/snapshottask/query.md`
  — and their v26 twins (diff the relevant field sections; expect no change, but confirm).
- `scripts/generate_api_exporter_parity.py` — rows for `TASK_STATE`, `TASK_LAST_RUN_TS`
  (currently "unavailable: no reachable 25.10.2 producer") — must be rewritten.
- `tests/test_phase1_metrics.py` for collector-test patterns.

## Required behavior

1. Extend each task query's `select` to additionally fetch the state/job fields **and nothing
   else** (no credentials/paths/scripts — cloudsync rows contain secrets outside the selected
   fields; the select is the safety mechanism):
   - replication: `["id", "name", "enabled", "state"]` (name label should prefer the task's
     `name` when present, falling back to `id` — keep whatever `_export_task_list` does today
     consistent across TASK_COUNT/TASK_ENABLED/TASK_STATE).
   - cloudsync: `["id", "description", "enabled", "job"]`
   - rsynctask: `["id", "enabled", "job"]`
   - snapshottask: `["id", "enabled", "state"]`
2. From those, emit per task (bounded label sets only):
   - `truenas_task_state{task_type, name, state}` = 1 for the current state, with `state`
     normalized `.upper()` and restricted to a **known allowlist**
     (`{"PENDING","RUNNING","SUCCESS","FINISHED","ERROR","FAILED","WAITING","ABORTED","HOLD","UNKNOWN"}`
     — map anything else to `UNKNOWN` to protect cardinality; reuse/extend the `_status_like`
     philosophy, `runtime.py` ~908–921).
   - `truenas_task_last_run_timestamp_seconds{task_type,name}` from the first parseable of
     `state.datetime`, `job.time_finished` via `_parse_ts` (which already handles `{"$date": ms}`).
3. Null/missing handling: `state`/`job` null or unparseable ⇒ no sample for that task (absent,
   not 0). Malformed rows skipped exactly like `_export_task_list` does.
4. Keep the existing count/enabled behavior untouched; respect `max_entity_calls` truncation.
5. Update the parity generator's hand-maintained tables: `TASK_STATE` and `TASK_LAST_RUN_TS`
   move from "unavailable" to produced, with accurate `response_field` entries per task type and
   a note that the `state` object is opaquely typed in the doc corpus but stable in middleware.
6. Consider (and note in Outcome) whether the bundled dashboard should gain a task-failures
   panel — do NOT build it in this task; add a "Discovered" line instead.

## Compatibility rules

- The metrics already exist in the contract with these exact names/labels — you are filling
  declared contracts, not changing them. Minor-version worthy (new producers). Regenerate
  contract (HELP unchanged → no diff expected), parity (big diff expected), dashboard (no diff
  unless you touched it).

## Tests

Add a dedicated test (e.g. extend `tests/test_phase1_metrics.py`):

1. Fake client returning one task per type with realistic payloads:
   replication `state={"state": "ERROR", "datetime": {"$date": 1750000000000}}`,
   cloudsync `job={"state": "SUCCESS", "time_finished": {"$date": ...}, "progress": {"percent": 100}}`,
   rsynctask `job=None`, snapshottask `state={"state": "FINISHED"}`.
   Assert: exact `truenas_task_state` samples (including rsynctask having **no** state sample),
   and correct last-run timestamps (epoch seconds, i.e. `$date/1000`).
2. Unknown state string (e.g. `"WEIRD_NEW_STATE"`) → labeled `UNKNOWN` (cardinality guard).
3. Absent on failure: task query raises → none of the TASK_* series for that type; other types
   unaffected.
4. Assert the wire `select` lists match the spec exactly (RecordingClient inspection) — this is
   the security assertion that no credential fields are fetched.

## Verification

```
python3 -m pytest tests/test_phase1_metrics.py tests/test_runtime_api_parity.py -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

## Definition of done

- All four task types emit state + last-run when the API provides them; absent otherwise; state
  label cardinality bounded by allowlist; selects verified credential-free by test; parity tables
  truthful; validate.sh green; TASKS.md updated (minor-worthy).

## Outcome

_(fill in when done)_
