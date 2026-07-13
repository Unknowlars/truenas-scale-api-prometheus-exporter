# 05 — Coding Agent Task Board

Each task must remain within its file ownership and must run its listed checks.
Agents must not add mutating API calls, credentials, live captures, hosted CI,
or unrelated refactors.

Hard gate: no runtime, transport, collector, event, metric-contract, dashboard,
or fixture implementation may start until COMPAT-01A and COMPAT-01B are
complete and validated.

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
