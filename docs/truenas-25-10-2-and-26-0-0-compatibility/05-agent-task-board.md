# 05 — Coding Agent Task Board

Each task must remain within its file ownership and must run its listed checks.
Agents must not add mutating API calls, credentials, live captures, hosted CI,
or unrelated refactors.

## COMPAT-01 — Pin and compare API documentation

**Prerequisite:** none.

**Own:** `scripts/convert_truenas_api_docs_to_markdown.py`,
`scripts/generate_api_docs_manifest.py`, `scripts/tooling.py`, v26 metadata,
target-aware parity generation, and compatibility diff artifacts.

**Implement:** target selection, v26 manifest, separate parity artifacts,
provenance checks, and exact current-call method/event diff.

**Accept when:** both targets pass independent `--check` commands and the
25.10.2 manifest/hash is unchanged.

## COMPAT-02 — Add compatibility profiles

**Prerequisite:** COMPAT-01 diff and target metadata.

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
covered and no secrets appear in logs.

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

**Implement:** suppress v26 `virt.*`, `nvmet.global.sessions`, removed pool
methods, and plural reporting discovery; clear stale metrics and preserve
NaN/absent behavior.

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
