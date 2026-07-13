# 05 — Coding Agent Task Board

Each task must remain within its file ownership and must run its listed checks.
Agents must not add mutating API calls, credentials, live captures, hosted CI,
or unrelated refactors.

Hard gate: no runtime, transport, collector, event, metric-contract, dashboard,
or fixture implementation may start until COMPAT-01A and COMPAT-01B are
complete and validated.

## Agent execution status

Update this table before and after each task. Agents must update only their own
task row, except to add a blocking note that directly affects their assigned
task.

Allowed statuses: `not started`, `in progress`, `blocked`, `needs review`,
`complete`.

| Task | Status | Owner/session | Started | Finished | Evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| COMPAT-01A | complete | Codex GPT-5 / session 2026-07-13T13:52+02:00 | 2026-07-13T13:52:00+02:00 | 2026-07-13T13:56:31+02:00 | `python3 scripts/generate_api_docs_manifest.py --check`; `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`; `git diff -- docs/truenas-api/MANIFEST.json` empty; `git diff --check`; `./scripts/validate.sh` | v26 manifest: `docs/truenas-api-v26/MANIFEST.json`; dependent runtime/profile tasks remain blocked until COMPAT-01B |
| COMPAT-01B | complete | Codex GPT-5 / session 2026-07-13T14:02+02:00 | 2026-07-13T14:02:29+02:00 | 2026-07-13T14:09:14+02:00 | `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`; `git diff -- docs/api-exporter-parity.json docs/api-exporter-parity.md docs/truenas-api/MANIFEST.json docs/truenas-api-v26/MANIFEST.json src grafana-dashboard tests fixtures scripts/validate.sh scripts/release.sh .github` empty; `git diff --check`; `./scripts/validate.sh` | v26 parity: `docs/api-exporter-parity-v26.{json,md}`; compatibility diff: `docs/truenas-25-10-2-and-26-0-0-compatibility/api-compatibility-diff.{json,md}`; runtime/profile work remains blocked until COMPAT-02 starts |
| COMPAT-02 | complete | Codex GPT-5 / session 2026-07-13T14:14+02:00 | 2026-07-13T14:14:56+02:00 | 2026-07-13T14:25:14+02:00 | `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py -q` (33 passed); `python3 scripts/generate_api_docs_manifest.py --check`; `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`; `git diff --check`; `./scripts/validate.sh` (155 passed, 90.36% coverage, Docker image build/version smoke passed) | 25.10, 26.0, and unknown/common-intersection profiles added; COMPAT-03 remains blocked until version detection starts |
| COMPAT-03 | complete | Codex GPT-5 / session 2026-07-13T14:28+02:00 | 2026-07-13T14:28:21+02:00 | 2026-07-13T14:34:54+02:00 | `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py tests/test_runtime_lifecycle.py -q` (55 passed); `PYTHONPATH=. pytest tests/test_phase1_metrics.py tests/test_phase3_collector_mode.py -q` (42 passed); `python3 scripts/generate_api_docs_manifest.py --check`; `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`; `git diff --check`; `./scripts/validate.sh` (161 passed, 90.46% coverage, Docker image build/version smoke passed) | Runtime bootstrap selects 25.10, 26.0, or unknown/common-intersection profile after authentication and before telemetry; detection failure remains fail-closed |
| COMPAT-04 | complete | Codex GPT-5 / session 2026-07-13T16:16+02:00 | 2026-07-13T16:16:02+02:00 | 2026-07-13T16:23:07+02:00 | `PYTHONPATH=. pytest tests/test_runtime_api_parity.py -q` (35 passed); `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py tests/test_documented_api_shapes.py -q` (54 passed); `python3 scripts/generate_metric_contract.py --check`; `python3 scripts/generate_api_docs_manifest.py --check`; `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`; `git diff --check`; `./scripts/validate.sh` (163 passed, 90.52% coverage, Docker image build/version smoke passed) | VM memory conversion uses profile-owned units; bounded dataset/pool/app normalizers added; metric contract unchanged |
| COMPAT-05 | complete | Codex GPT-5 / session 2026-07-13T16:48+02:00 | 2026-07-13T16:48:09+02:00 | 2026-07-13T16:53:12+02:00 | `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py tests/test_removed_source_suppression.py -q` (51 passed); `python3 scripts/generate_metric_contract.py --check`; `python3 scripts/generate_api_docs_manifest.py --check`; `python3 scripts/generate_api_exporter_parity.py`; `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`; `git diff --check`; `./scripts/validate.sh` (173 passed, 90.50% coverage, Docker image build/version smoke passed) | Removed methods/events are intentionally suppressed before transport under 26.0 and unknown; v25 remains allowed; `app.image.query` remains eligible for reviewed count use |
| COMPAT-06 | complete | Codex GPT-5 / session 2026-07-13T16:57+02:00 | 2026-07-13T16:57:02+02:00 | 2026-07-13T17:02:50+02:00 | `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_lifecycle.py tests/test_removed_source_suppression.py -q` (35 passed); `python3 scripts/generate_metric_contract.py --check`; `python3 scripts/generate_api_docs_manifest.py --check`; `python3 scripts/generate_api_exporter_parity.py`; `python3 scripts/generate_api_exporter_parity.py --check`; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0`; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`; `python3 scripts/generate_api_exporter_parity.py --compat-diff`; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`; `git diff --check`; `./scripts/validate.sh` (176 passed, 90.47% coverage, Docker image build/version smoke passed) | Tracks valid subscription ids, rejects invalid ids, unsubscribes on clean shutdown/reconnect cleanup, clears stale event caches; v25 virt event remains supported and v26/unknown suppress removed virt event |
| COMPAT-07 | complete | Codex GPT-5 / session 2026-07-13T17:07+02:00 | 2026-07-13T17:07:35+02:00 | 2026-07-13T17:11:05+02:00 | `python3 scripts/generate_metric_contract.py --check` passed; `python3 scripts/generate_api_docs_manifest.py --check` passed; `python3 scripts/generate_api_exporter_parity.py --check` passed; `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check` passed; `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check` passed; `python3 scripts/generate_api_exporter_parity.py --compat-diff --check` passed; `git diff --check` passed; `./scripts/validate.sh` passed (176 passed, 90.47% coverage, dashboard validation passed, Docker image build/version smoke `5.2.0` passed) | Operator docs now describe automatic profile selection, fail-closed unknown behavior, v26/unknown removed-source suppression, absent/NaN unavailable metrics, profile-aware event defaults, subscription ID/unsubscribe lifecycle hardening, `app.image.query` eligibility, and continued blocks for `pool.is_upgraded`/`pool.ddt_prefetch` |
| COMPAT-08 | blocked | — | — | — | — | Requires all prior tasks |

### Status update rules

Before starting a task:

- set `Status` to `in progress`;
- set `Owner/session` to the agent name or session id;
- set `Started` to the current date/time;
- leave `Finished` as `—`.

When finishing a task:

- set `Status` to `needs review` if implementation is complete but acceptance
  checks or independent review are not complete;
- set `Status` to `complete` only after all acceptance checks pass;
- set `Finished` to the current date/time;
- set `Evidence` to exact commands/artifacts, for example
  `v26 manifest check passed; ./scripts/validate.sh passed`;
- put any blocker, follow-up, or dependency note in `Notes`.

When blocked:

- set `Status` to `blocked`;
- put the exact blocker and required evidence/action in `Notes`;
- do not continue into dependent tasks.

## COMPAT-01A — Pin v26 documentation provenance

**Prerequisite:** none.

**Own:** `scripts/convert_truenas_api_docs_to_markdown.py`,
`scripts/generate_api_docs_manifest.py`, `scripts/tooling.py`, v26 metadata,
and target-aware manifest generation.

**Implement:** target selection, v26 manifest, source provenance, converted-tree
hashes, and checks proving one documentation target cannot overwrite another.

**Accept when:** the 25.10.2 manifest/hash is unchanged, the v26 manifest passes
independently, and the v26 source/provenance fields are recorded.

## COMPAT-01B — Generate v26 parity and compatibility diff

**Prerequisite:** COMPAT-01A.

**Own:** target-aware parity generation, separate v26 parity artifacts, and
compatibility diff artifacts.

**Implement:** separate v26 parity JSON/Markdown outputs, a machine-readable and
human-readable diff, and exact current-call method/event comparison.

**Accept when:** v25 and v26 parity checks pass independently, v25 artifacts are
unchanged, and the diff identifies every current exporter method/event absent or
schema-changed in v26.

## COMPAT-02 — Add compatibility profiles

**Prerequisite:** COMPAT-01A and COMPAT-01B.

**Own:** new profile module plus `api_catalog.py`, `method_safety.py`, and
profile selection tests.

**Implement:** `25.10`, `26.0`, and `unknown` profiles; pre-call method/event
gating; query-limit policy; removed-source declarations; redacted diagnostics.

**Accept when:** no profile can call a method outside its reviewed allowlist and
unknown versions use only the common intersection.

## COMPAT-03 — Bootstrap version detection

**Prerequisite:** COMPAT-02.

**Own:** `runtime.py`, connection setup, and bootstrap tests.

**Implement:** authenticate, call `system.version_short`, select the profile,
and only then schedule collectors/discovery. Avoid duplicate version calls per
connection.

**Accept when:** v25, v26, failed, malformed, and unknown detection cases are
covered, detection failure does not expand API access, and no secrets appear in
logs.

## COMPAT-04 — Normalize collectors and units

**Prerequisite:** COMPAT-02 and COMPAT-03.

**Own:** `runtime.py`, `collection.py`, v26 fixtures, and collector tests.

**Implement:** VM byte/MB handling, bounded dataset/pool/application normalizers,
and additive realtime shape handling.

**Accept when:** existing metric contracts are unchanged and VM output values
are correct for both documented units.

## COMPAT-05 — Suppress removed sources

**Prerequisite:** COMPAT-03.

**Own:** collector call sites, method safety, profile fixtures, and parity tests.

**Implement:** suppress v26 `virt.*`, `nvmet.global.sessions`, and plural
reporting discovery; keep `pool.is_upgraded` blocked because it requires a pool
id; keep `pool.ddt_prefetch` prohibited because it is action-like; clear stale
metrics and preserve NaN/absent behavior.

**Accept when:** transport traces prove removed methods are never called under
the v26 profile.

## COMPAT-06 — Harden event lifecycle

**Prerequisite:** COMPAT-02 and COMPAT-03.

**Own:** event loop, transport test doubles, event fixtures, and event tests.

**Implement:** profile-aware subscriptions, v26 default event set, subscription
ID tracking, clean unsubscribe, reconnect cleanup, and stale-cache clearing.

**Accept when:** v25 keeps its virt event, v26 does not subscribe to it, and all
successful subscriptions are unsubscribed during clean teardown.

## COMPAT-07 — Documentation and operator handoff

**Prerequisite:** COMPAT-01 through COMPAT-06.

**Own:** README, `.env.example` documentation, changelog, compatibility docs,
and `docs/modernization/README.md`.

**Implement:** describe automatic profile selection, unavailable v26 metrics,
authentication deprecation, supported event defaults, and verification evidence.

**Accept when:** operator docs do not recommend a stale version toggle and all
claims link to the pinned local artifacts or official TrueNAS documentation.

## COMPAT-08 — Full validation and release gate

**Prerequisite:** all prior tasks.

**Own:** no production code; verification evidence only.

**Implement:** run focused tests, full `./scripts/validate.sh`, target-aware
checks, optional read-only smoke tests, and evidence recording.

**Accept when:** every required local check passes, skipped checks are recorded,
and release tooling remains dry-run unless explicitly asked to publish.

## Copy-paste coding-agent prompts

Use these prompts as the starting handoff. Assign only one task per agent unless
the previous task is complete and validated.

### Prompt for COMPAT-01A

```text
You are implementing COMPAT-01A only.

Read AGENTS.md, docs/modernization/README.md, and
docs/truenas-25-10-2-and-26-0-0-compatibility/06-final-review.md.

Goal: pin the checked-in v26 API documentation corpus without changing runtime
behavior.

Do:
- add target-aware manifest support for docs/truenas-api-v26/
- generate/check a v26 manifest with file counts, hashes, target version,
  source/provenance metadata, generator metadata, and generation command
- prove v26 generation cannot overwrite docs/truenas-api/MANIFEST.json
- keep the 25.10.2 manifest and docs unchanged

Do not:
- modify runtime, transport, collectors, events, metrics, dashboards, fixtures,
  release behavior, or hosted automation
- call a live TrueNAS system
- commit credentials or raw live API responses

Acceptance:
- v25 manifest check passes unchanged
- v26 manifest check passes independently
- git diff is limited to COMPAT-01A tooling/docs/generated v26 manifest work
- ./scripts/validate.sh passes or any environment limitation is classified
```

### Prompt for COMPAT-01B

```text
You are implementing COMPAT-01B only.

Prerequisite: COMPAT-01A is complete and validated.

Goal: generate separate v26 parity and compatibility-diff artifacts without
overwriting 25.10.2 artifacts.

Do:
- add target-aware v26 parity generation to separate output paths
- add a compatibility diff covering method/event existence, params, roles,
  response shapes, units, deprecations, removals, and current exporter usage
- explicitly verify app.image.query exists in v26
- explicitly verify pool.is_upgraded and pool.ddt_prefetch exist in v26 but
  remain blocked/suppressed for safety/parameter reasons
- explicitly verify nvmet.global.sessions, virt.instance.*, virt.volume.*,
  reporting.graphs, and reporting.netdata_graphs are absent in v26

Do not modify runtime, collectors, events, metrics, dashboards, or fixtures.

Acceptance:
- v25 parity check passes unchanged
- v26 parity/diff checks pass independently
- current exporter method/event diff is generated from tooling, not hand-entered
- ./scripts/validate.sh passes or any environment limitation is classified
```

### Prompt for COMPAT-02

```text
You are implementing COMPAT-02 only.

Prerequisite: COMPAT-01A and COMPAT-01B are complete and validated.

Goal: add compatibility profile data and pre-call safety gates without changing
metric semantics.

Do:
- define 25.10, 26.0, and unknown/common-intersection profiles
- move method/event allowlists, removed-source decisions, query limits, and unit
  conversion metadata into profile-owned data
- ensure EXTRA_METHODS, generic discovery, configured EVENT_SUBSCRIPTIONS,
  reporting discovery, and count queries cannot bypass the selected profile
- keep global mutation and sensitive-response exclusions

Acceptance:
- tests prove no profile can call outside its reviewed allowlist
- unknown/malformed/failed detection can only use the common intersection
- v26 profile excludes removed v25-only methods/events
```

### Prompt for COMPAT-03

```text
You are implementing COMPAT-03 only.

Prerequisite: COMPAT-02 is complete and validated.

Goal: authenticate, detect TrueNAS API version, and select a profile before any
discovery, collector, count query, reporting query, or event subscription.

Do:
- call system.version_short once after authentication per connection
- select 25.10, 26.0, or unknown/common profile
- prove failed, denied, malformed, and unknown detection cannot expand API access
- keep secrets out of logs

Acceptance:
- call-order tests show no profile-gated API call happens before profile
  selection
- no duplicate version calls per connection
- no raw API key or response body is logged
```

### Prompt for COMPAT-04 through COMPAT-08

```text
Continue in dependency order from docs/truenas-25-10-2-and-26-0-0-compatibility/05-agent-task-board.md.

Do not start a task until all prerequisites are complete and validated.
Do not add v26-only metrics or dashboard panels unless the task explicitly
approves the metric contract, aliases/deprecations, fixtures, and dashboard
behavior.
```
