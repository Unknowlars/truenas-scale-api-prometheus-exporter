# TrueNAS SCALE 25.10.2 and 26.0.0 Compatibility Plan

Status: discovery complete; implementation not started

The companion implementation documents are now the authoritative handoff for
coding agents:

- [Compatibility index](00-compatibility-index.md)
- [API baseline and diff](01-api-baseline-and-diff.md)
- [Runtime profiles and safety](02-runtime-profile-and-safety.md)
- [Collectors and events](03-runtime-collectors-and-events.md)
- [Tests and release](04-tests-fixtures-and-release.md)
- [Agent task board](05-agent-task-board.md)

Important corrections to this discovery draft are recorded in those documents.
In particular, `app.image.query` is present in the checked-in v26 corpus and
must not be treated as removed; v26 retains singular `reporting.graph` and
`reporting.netdata_graph` while the current optional collector calls the plural
discovery methods; and v26 authentication introduces `auth.login_ex` while
retaining `auth.login_with_api_key` as deprecated rather than immediately
removing it.

This document records the repository discovery performed for supporting both the current TrueNAS SCALE 25.10.x API family and the upcoming TrueNAS SCALE 26.0.0 API family. It is intended to be the working breakdown for implementation tasks.

The current repository compatibility baseline remains TrueNAS SCALE 25.10.2. Observations from a live 25.10.3 system are recorded separately and must not replace the authoritative 25.10.2 documentation baseline.

## 1. Executive summary

A dedicated compatibility implementation is required.

The exporter is currently designed around the TrueNAS SCALE 25.10.2 API contract. The repository also contains a substantially changed v26 documentation tree. The v26 tree is structurally useful, but it is not yet an authoritative compatibility baseline because it lacks a v26 manifest, parity artifacts, target-aware generator support, and complete provenance validation.

The recommended design is a hybrid:

1. Detect the API version through the existing read-only `system.version_short` call.
2. Select a declarative compatibility profile for the detected API family.
3. Keep additive, shape-tolerant parsing where fields are merely renamed, moved, or omitted.
4. Apply explicit profile-specific unit conversion where semantics changed.
5. Fail closed for removed, ambiguous, opaque, or permission-dependent sources.
6. Do not add a normal user-managed `.env` version toggle.
7. Keep one container image capable of supporting both API families.

Unsupported metrics must remain absent or NaN according to current exporter behavior. The exporter must never turn a removed method, denied permission, or missing field into a fabricated zero.

## 2. Repository state and evidence

The worktree was checked with `git status --short` before discovery and was clean. No pre-existing user changes were present.

The repository guidance establishes these constraints:

- TrueNAS SCALE 25.10.2 is the authoritative current API target.
- Only demonstrably read-only API calls may be proposed or used by collectors, tests, discovery, or smoke checks.
- Existing Prometheus metric names, types, help text, and label sets are locked.
- Semantic replacements require a compatibility alias and documented deprecation.
- Credentials, API keys, hostnames, and unredacted live responses must not be committed.
- GitHub Actions and other hosted CI/CD automation must not be added.
- Release tooling must remain dry-run by default.
- Verification evidence must be recorded in `docs/modernization/README.md`.

The current implementation and documentation establish:

- TrueNAS SCALE 25.10.2 as the documented compatibility target.
- 767 documented method leaves.
- 63 documented event leaves.
- 398 explicitly approved read-only method calls.
- 112 telemetry candidates.
- 405 locked metric contract entries.
- Three default event subscriptions:
  - `reporting.realtime`
  - `app.stats`
  - `virt.instance.metrics`
- Collector mode as the default mode, with a legacy compatibility mode.
- Static API safety and event allowlists centered on the 25.10.2 documentation.

Discovery-only checks completed successfully without changing committed files:

- `python3 scripts/generate_metric_contract.py --check`
- `python3 scripts/generate_truenas_dashboard.py --check`
- `python3 scripts/validate_dashboard.py`
- `python3 scripts/generate_api_docs_manifest.py --check`
- `python3 scripts/generate_api_exporter_parity.py --check`
- Focused API, runtime, event, and transport tests: 56 passed.

The complete `./scripts/validate.sh` gate was not run during discovery because it may generate bytecode, build containers, or otherwise alter local state. It remains a required implementation-stage check.

## 3. Documentation comparison

### 3.1 Inventory

| API surface | 25.10 documentation | v26 documentation |
| --- | ---: | ---: |
| Method leaf documents | 767 | 805 |
| Event leaf documents | 63 | 80 |
| Method/event namespace files | 114 | 128 |
| Added methods | — | 87 |
| Removed methods | — | 49 |
| Added events | — | 22 |
| Removed events | — | 5 |

The 25.10 tree has a checked-in `MANIFEST.json` identifying target version 25.10.2, source type, generator, file count, and aggregate hash. It also has generated parity JSON and Markdown artifacts.

The converted v26 tree has 805 method leaves and 80 event leaves under
`docs/truenas-api-v26/`. The raw `truenas-v26.0.0-docs/` source tree is not
checked in, and the converted tree currently has no equivalent v26 manifest,
parity artifact, target constant, or integrated generator check. The v26 README
is descriptive but does not establish exact release provenance.

Therefore, the v26 documentation should be treated as a generated candidate corpus until the following are completed:

- Confirm source and release provenance.
- Generate a v26 manifest.
- Record source and converted-tree hashes.
- Generate v26 parity artifacts.
- Add check-mode validation for both documentation targets.
- Ensure the converter and generators do not overwrite the 25.10.2 artifacts.

### 3.2 Added methods

Important v26 additions include:

- `container.query`
- `container.device.query`
- `container.metrics`
- `enclosure2.query`
- `failover.status`
- `sharing.webshare.query`
- `smb.status`
- `zpool.query`
- `zfs.resource.snapshot.query`
- `zfs.resource.snapshot.count`
- `zfs.tier.rewrite_job_query`
- `zfs.tier.rewrite_job_status`
- `zfs.tier.status`
- `directoryservices.status`

Other additions include container lifecycle methods, failover actions, SED operations, webshare configuration methods, license operations, and ZFS resource mutation methods. Mutation-capable additions must remain excluded from the exporter.

Potential read-only additions require individual review for permissions, response stability, cardinality, and metric semantics. They must not be added merely because they appear in the v26 inventory.

### 3.3 Removed methods

Methods relevant to current exporter behavior that are removed from v26 include:

- `nvmet.global.sessions`
- `virt.instance.query`
- `virt.volume.query`
- `virt.instance.metrics`
- `reporting.graphs`
- `reporting.netdata_graphs`

The v26 corpus also removes the wider `virt.instance.*`, `virt.volume.*`, and `virt.global.*` families and several service or snapshot mutation methods.

The v25 documentation already marked service lifecycle methods and `pool.dataset.destroy_snapshots` for removal. Those methods are not safe exporter surfaces and must remain excluded.

`app.image.query` is not removed. It exists in the checked-in v26 corpus and
remains eligible only after profile safety, permission, count-mode, and schema
review.

### 3.4 Added and removed events

Added v26 events include:

- `auth.sessions`
- `container.device.query`
- `container.metrics`
- `container.query`
- `directoryservices.status`
- `disk.query`
- `docker.events`
- `docker.state`
- `failover.disabled.reasons`
- `failover.reboot.info`
- `failover.status`
- `pool.scan`
- `sharing.webshare.query`
- `system.ready`
- `system.reboot.info`
- `system.shutdown`
- `tn_connect.config`
- `truecommand.config`
- `user.web_ui_login_disabled`
- `zfs.tier.rewrite_job_query`
- `zfs.tier.rewrite_job_status`
- `zpool.query`

Removed v26 events include:

- `app.image.query`
- `app.registry.query`
- `virt.instance.metrics`
- `virt.instance.query`
- `virt.volume.query`

The v26 documentation clarifies that `core.subscribe` returns a subscription identifier and that `core.unsubscribe` can remove a subscription. Existing code ignores the returned identifier. This is not an immediate compatibility break, but reconnect and shutdown handling should be hardened.

## 4. API behavior differences

### 4.1 Methods and parameters

v26 adds upper bounds and non-negative constraints to many query `limit` and `offset` parameters. The current exporter default query limit of 200 is safe, but profile-aware validation should be added rather than relying on current defaults.

Several v26 query methods use more structured parameter and response forms. The implementation must validate the exact parameter shapes used by the exporter against both documentation targets.

### 4.2 Return shapes

The following shape changes require normalization:

- `pool.dataset.query` may return arrays, objects, or nested hierarchy structures.
- `pool.query` adds structured scan information and `all_sed`.
- `zpool.query` introduces a separate pool/status-oriented query surface.
- `reporting.realtime` changes from partly opaque fields to structured CPU, disk, interface, memory, and pool fields.

The exporter should normalize these responses before metric extraction. It must not assume every query returns a flat list.

### 4.3 Confirmed unit changes

The following are definite compatibility risks:

| Method | 25.10 documentation | v26 documentation | Required treatment |
| --- | --- | --- | --- |
| `vm.get_available_memory` | MB | bytes | Profile-specific conversion |
| `vm.get_vmemory_in_use` | MB | bytes | Profile-specific conversion |

The current code multiplies these results by `1024**2`. That is correct for the documented 25.10 behavior but would inflate v26 values if left unchanged.

The v26 `vm.query` documentation also describes memory fields in MiB. Those fields require separate field-level verification before being mapped to existing metrics.

### 4.4 Realtime event shape

The existing parser already supports several cross-version forms:

- Legacy `disls` and v26 `disks`.
- Aggregate and per-CPU fields.
- Interface rate fields and cumulative fallback fields.
- Optional pool and ZFS fields.

The v26 shape is more structured:

- CPU entries are keyed by `cpu`, `cpu0`, and similar names with `usage` and nullable `temp`.
- Disk data uses `disks` and aggregate read/write counters.
- Interfaces expose link state, speed, and byte rates.
- Memory omits several legacy free/cache/buffer/swap fields.
- Pools expose numeric values under pool names.

Live 25.10.3 observations show behavior similar to the v26 structured realtime shape. These observations are useful compatibility evidence but do not supersede the 25.10.2 documentation.

### 4.5 Authentication and transport

No material change was found in the documented WebSocket, JSON-RPC, TLS, or error-code behavior.

`auth.login_with_api_key` remains available in v26 with the same basic API-key flow, but is documented as deprecated for removal in v27. Authentication migration should be planned before v27 without introducing password authentication or mutation-capable behavior.

### 4.6 Permissions and roles

No role changes were found for common methods and events. New v26 methods introduce new permission requirements, including container, SMB, pool, failover, and resource-specific roles.

Collectors must treat authorization failures as unavailable data. They must not infer zero from a denied or omitted response.

## 5. Existing exporter surfaces at risk

| Implementation surface | Existing behavior | v26 risk | Plan |
| --- | --- | --- | --- |
| `runtime.py` VM memory collection | Multiplies values by `1024**2` | v26 values are bytes | Add profile-specific normalization |
| `runtime.py` virtual metrics | Calls `virt.instance.query` and `virt.volume.query` | Methods removed | Suppress calls; preserve metrics as unavailable |
| `runtime.py` NVMe metrics | Calls `nvmet.global.sessions` | Method removed | Suppress calls; preserve metric as unavailable |
| `runtime.py` miscellaneous configs | Calls `app.image.query` | Method exists in v26; schema/permission still requires review | Keep eligible under a reviewed profile; do not substitute registry query |
| `runtime.py` generic reporting | Calls graph methods when enabled | Methods removed | Skip under v26 profile |
| `events.py` | Subscribes to v25 event set | `virt.instance.metrics` removed | Profile-specific subscriptions |
| `collection.py` | Parses mostly flat responses | v26 nested/union responses | Add bounded normalizers |
| `api_catalog.py` | Static 25.10.2 catalog | Cannot represent v26 safety | Make catalog target/profile aware |
| `method_safety.py` | Static v25 allowlist and blocks | New/removed methods | Add v26 reviewed safety data |
| API generators | Target hard-coded to 25.10.2 | Cannot validate v26 | Add target-aware check mode |
| Tests and fixtures | 25.10.2 fixture namespace | No v26 regression coverage | Add synthetic v26 fixtures |

## 6. Compatibility strategy

### Recommended: hybrid compatibility profiles with additive parsers

The exporter should maintain profiles for:

- `25.10`, anchored to the 25.10.2 documentation.
- `26.0`, anchored to the validated v26 documentation.
- `unknown`, using only the verified common intersection.

Profiles should own:

- Read-only method allowlists.
- Safe event subscriptions.
- Removed-method decisions.
- Query limits and parameter constraints.
- Unit conversions.
- Field aliases.
- Response-shape normalizers.
- Version-specific metric source mappings.

Additive parsing should be used for compatible shape variations. It must not be used to conceal unit changes or map an unrelated v26 feature onto an old metric name.

### Alternative A: one parser with additive fallback only

Advantages:

- Minimal configuration change.
- Low initial test complexity.
- Good for field aliases and optional fields.

Problems:

- Cannot safely handle removed methods.
- Cannot reliably handle changed units.
- Encourages silent semantic inference.
- Does not model different event inventories or permissions.

This is insufficient as the complete design.

### Alternative B: automatic version detection only

Advantages:

- No operator configuration.
- Good upgrade ergonomics.

Problems:

- Version detection does not encode schema or safety policy.
- Unknown or vendor-patched versions require fallback behavior.
- Runtime branching becomes scattered and difficult to audit.

Detection should select profiles, not replace them.

### Alternative C: explicit `.env` version selection

Advantages:

- Deterministic selection.
- Simple fixture testing.

Problems:

- Stale configuration after a server upgrade can cause wrong units or wrong methods.
- Creates an avoidable operational migration step.
- Can silently publish incorrect metrics.

This should not be the normal configuration model.

### Alternative D: separate compatibility profiles without automatic detection

Advantages:

- Strong separation of method safety and schema rules.
- Clear unit and event ownership.

Problems:

- Still needs a reliable way to select the profile.
- Manual selection recreates the `.env` toggle risk.

Profiles are required, but they should normally be selected automatically.

### Alternative E: hybrid approach

This is the recommendation. Automatic read-only version detection selects declarative profiles, while additive parsers handle compatible field and shape changes. Unknown versions use the conservative common profile.

## 7. Version and configuration behavior

Normal runtime behavior should be:

1. Authenticate using the existing read-only API-key flow.
2. Call `system.version_short`.
3. Normalize the returned version into a compatibility family.
4. Select the profile.
5. Record the selected profile and detected version in diagnostics.
6. Use the profile for methods, events, parameters, and units.

No normal `.env` version toggle is necessary or recommended.

If a forced profile is eventually added for diagnostics, it must:

- Default to `auto`.
- Emit a prominent mismatch warning.
- Never expand the safe method allowlist.
- Never bypass read-only safety checks.
- Never be required for normal operation.

One container image should support both API families.

## 8. Metric compatibility policy

### Metrics expected to continue unchanged

Common system, host, pool, dataset, disk, interface, service, alert, job, update, certificate, application, `app.stats`, and common realtime metrics should retain their current names, types, help text, labels, and semantics.

### Metrics requiring version-specific parsing

- VM available memory.
- VM memory in use.
- Nested dataset and pool responses.
- Structured pool scan data.
- Realtime disk aliases.
- Realtime memory omissions.
- Application nullable version fields.

### Metrics that may become unavailable on v26

The following should remain absent or NaN on v26 unless an exact equivalent is proven:

- Virtual instance count and running-state metrics.
- Virtual volume count metrics.
- Virtual instance realtime CPU and memory metrics.
- NVMe-over-TCP session count.
- Docker image count.
- Generic reporting graph metrics from removed methods.

### Metrics that may become available on v26

Potential candidates include:

- SMB session, open-file, and connection counts from bounded `smb.status` responses.
- WebDAV share count from `sharing.webshare.query`.
- Container count and state from `container.query`.
- Pool scan/status metrics from `pool.query` or `zpool.query`.
- Failover status.
- ZFS tier rewrite-job status.

Each candidate requires a safety review, read-only permission fixture, schema fixture, cardinality review, metric contract update, and dashboard review.

Do not map `container.metrics` directly to legacy virtual-machine metrics. Its documented payload is opaque and its semantics are not established as an equivalent.

## 9. Event and parser plan

For 25.10, retain the current default subscriptions:

- `reporting.realtime`
- `app.stats`
- `virt.instance.metrics`

For v26:

- Retain `reporting.realtime`.
- Retain `app.stats`.
- Remove `virt.instance.metrics`.
- Do not subscribe to `container.metrics` until stable fields and semantics are established.
- Evaluate pool, failover, and tier events only after bounded-payload and permission review.

The realtime parser should continue supporting `disls` and `disks`, aggregate and per-CPU forms, interface rate/cumulative fallbacks, and optional fields.

Event handling should be hardened to:

- Track subscription identifiers.
- Unsubscribe during clean shutdown where supported.
- Avoid subscribing to events absent from the selected profile.
- Distinguish unsupported events from transient transport failures.
- Avoid turning missing events into zero-valued metrics.

## 10. New, changed, deprecated, and unavailable behavior

### New metrics

Add v26-only metrics only after read-only safety, schema, permissions, cardinality, and contract review.

### Changed metrics

Correct VM unit handling and normalize dataset, pool, application, and realtime response differences without changing existing metric contracts.

### Deprecated behavior

Plan migration away from `auth.login_with_api_key` before its documented v27 removal. Do not introduce password authentication.

Mutation-related deprecated methods remain excluded.

### Unavailable metrics

Keep metrics absent or NaN when their v25 source is removed, permission is denied, or no semantically equivalent v26 source exists. Never emit zero as a substitute.

## 11. Dashboard and generated-artifact work

The existing dashboard workflow must remain intact:

1. Treat `grafana-dashboard/operations-center-dashboard.json` and its generator as the source surface.
2. Validate metric references against `docs/metrics-contract.json`.
3. Rebuild or validate mission control with `build_mission_control.py`.
4. Do not hand-edit generated dashboard JSON.

Common dashboard queries should remain unchanged.

V26-only panels should not be added to the default dashboards until their metrics are stable and contract-approved. Panels must tolerate NaN and unavailable metrics and must not imply that missing data means zero.

The v26 API manifest and parity artifacts should be generated through local checkable tooling. Existing 25.10.2 artifacts must remain reproducible and must not be overwritten by v26 generation.

No hosted CI/CD or automatic container publication should be introduced.

## 12. Test and fixture tasks

Add sanitized synthetic fixtures in a separate namespace, for example:

- `tests/fixtures/api_26_0_0/`
- `tests/fixtures/realtime/reporting_realtime_26_shape.json`

Do not commit credentials, hostnames, API keys, or unredacted live response captures.

Add parametrized tests covering:

- Version detection.
- Profile selection.
- Unknown-version fallback.
- VM MB versus byte conversion.
- Removed-method suppression.
- Dataset array/object/nested responses.
- Pool scan fields.
- Realtime `disls` and `disks` forms.
- Missing realtime fields.
- V26 event subscriptions.
- Subscription identifiers and clean unsubscribe.
- Authentication compatibility.
- Permission failures.
- No fabricated zero values.
- New candidate metrics only when their semantics are proven.
- Existing metric names, types, help text, and labels.

Update API catalog and parity tests so both documentation targets can be checked independently.

## 13. Validation and release tasks

The implementation-stage validation set is:

```text
./scripts/validate.sh
```

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q
```

```text
python3 scripts/generate_metric_contract.py --check
python3 scripts/generate_truenas_dashboard.py --check
python3 scripts/validate_dashboard.py
python3 scripts/generate_api_docs_manifest.py --check
python3 scripts/generate_api_exporter_parity.py --check
```

The v26 implementation must add equivalent target-aware checks.

Focused compatibility checks should run before the full suite:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q \
  tests/test_api_catalog.py \
  tests/test_documented_api_shapes.py \
  tests/test_runtime_api_parity.py \
  tests/test_phase2_events.py \
  tests/test_transport.py
```

Optional live validation must use only a read-only API key, must not persist responses, and must not commit identifying data. It should separately verify 25.10.x and v26 profile behavior.

Release tooling remains local and dry-run by default. Publication requires an explicit publish flag.

Verification evidence must be added to `docs/modernization/README.md` after implementation validation.

## 14. Rollout and fallback plan

1. Establish and validate v26 documentation provenance.
2. Add profile and generator support without enabling new v26 metrics.
3. Add automatic detection and unknown-version fallback.
4. Implement unit and response-shape normalization.
5. Suppress removed v26 methods and events.
6. Verify with sanitized v26 fixtures.
7. Verify with a read-only v26 live smoke test.
8. Add individually approved v26 metrics.
9. Update dashboards only for approved metrics.
10. Run the complete local validation gate before release.

If v26 validation fails, the exporter should continue serving common metrics and mark v26-specific sources unavailable. It must not fall back to unsafe calls or guessed semantics.

Operational monitoring should include:

- Unknown or unsupported API versions.
- Profile selection failures.
- Authorization failures.
- Removed-source suppression.
- Parser shape errors.
- Event reconnects.
- Metric disappearance.
- Unexpected value-magnitude changes.

## 15. Dependency-ordered implementation tasks

### Task group 1: Establish the v26 documentation baseline

- Identify and record the exact v26 documentation source and release provenance.
- Add a v26 manifest with file counts and hashes.
- Add target-aware converter and manifest checks.
- Generate v26 parity inventory without overwriting 25.10.2 artifacts.
- Add tests proving both targets are independently reproducible.

### Task group 2: Define compatibility-profile data

- Define `25.10`, `26.0`, and `unknown` profiles.
- Move method safety and event safety decisions into profile-owned data.
- Keep global mutation exclusions.
- Record per-method parameter limits.
- Record removed methods and events explicitly.
- Record unit conversions and field aliases.

### Task group 3: Add read-only version detection

- Call `system.version_short` after authentication.
- Select a profile automatically.
- Add unknown-version conservative fallback.
- Add diagnostic logging or metrics without exposing secrets.
- Ensure detection failure does not expand API access.

### Task group 4: Normalize common response shapes

- Normalize dataset list/object/nested responses.
- Normalize pool and scan response forms.
- Preserve realtime `disls`/`disks` handling.
- Preserve missing-field and NaN behavior.
- Handle application nullable version fields.

### Task group 5: Correct version-specific units

- Add profile-specific conversion for `vm.get_available_memory`.
- Add profile-specific conversion for `vm.get_vmemory_in_use`.
- Review `vm.query` memory fields separately.
- Add magnitude and unit regression tests.

### Task group 6: Handle removed methods and events

- Suppress v26 calls to removed methods.
- Suppress v26 virtual-machine event subscriptions.
- Preserve unavailable metrics as NaN/absent.
- Skip removed optional generic reporting methods.
- Ensure collector logs distinguish intentional unavailability from failures.

### Task group 7: Harden event lifecycle behavior

- Track subscription identifiers.
- Implement clean unsubscribe where supported.
- Make reconnect behavior profile-aware.
- Test unsupported, denied, malformed, and transient event conditions.

### Task group 8: Evaluate new v26 read-only sources

Evaluate one source at a time:

- `smb.status`
- `sharing.webshare.query`
- `container.query`
- `zpool.query`
- `failover.status`
- ZFS tier rewrite-job methods/events

For each source, document read-only status, required role, response shape, cardinality, metric mapping, unavailable behavior, fixtures, and dashboard impact.

### Task group 9: Update metric contract and dashboards

- Add only approved new metrics.
- Preserve existing names, types, help, and labels.
- Add compatibility aliases and deprecations only where semantics require them.
- Update dashboard generator inputs, not generated JSON directly.
- Validate classic and mission-control dashboards.

### Task group 10: Complete verification and release readiness

- Run focused compatibility tests.
- Run full `./scripts/validate.sh`.
- Run target-aware documentation and parity checks.
- Run sanitized read-only smoke tests for both API families.
- Record evidence in `docs/modernization/README.md`.
- Run release tooling in dry-run mode.

## 16. Expected files and subsystems to change

Expected implementation areas:

- `src/truenas_exporter/config.py`
- `src/truenas_exporter/api_catalog.py`
- `src/truenas_exporter/method_safety.py`
- `src/truenas_exporter/events.py`
- `src/truenas_exporter/collection.py`
- `src/truenas_exporter/runtime.py`
- `src/truenas_exporter/metrics.py`, only for approved new contract metrics
- API documentation, manifest, parity, and conversion scripts
- `docs/truenas-api-v26/` metadata and validation support
- `docs/api-exporter-parity.*`
- `docs/metrics-contract.json`, only when approved metrics are added
- `docs/modernization/README.md`
- V26 tests and sanitized fixtures
- Dashboard generator inputs and dashboard tests
- `.env.example` only if a non-version compatibility setting is later proven necessary

No GitHub Actions, hosted CI/CD, credentials, live response captures, mutation-capable smoke calls, or automatic publication workflows should be added.

## 17. Product decisions and conservative defaults

The repository cannot determine the desired release timing for v26 support. The plan therefore uses these defaults:

- V26 support may be staged behind documentation, fixture, and read-only live verification gates.
- Unsupported metrics remain absent or NaN.
- Version selection is automatic, not operator-managed through `.env`.
- V26-only metrics are disabled until individually verified.
- One container image supports both versions.
- The current 25.10.2 compatibility contract remains the release safety baseline.

If product requirements later mandate v26 support before the next release, or require v26-only dashboard metrics to be enabled by default, those are release-scope decisions rather than repository-discovery findings and should be recorded before Task Group 8.

## 18. Assumptions and remaining risks

Assumptions:

- TrueNAS SCALE 25.10.2 remains authoritative for the current implementation.
- The checked-in v26 documentation represents the intended 26.0.0 API surface once provenance is established.
- One exporter image should support both API families.
- Prometheus metric contracts remain locked.
- Missing, removed, or denied sources must not become zero values.

Risks:

- The final v26 release may differ from the checked-in documentation.
- Read-only API keys may lack newly required roles.
- Opaque event payloads may not provide stable metric semantics.
- Similar-looking VM fields may have different units.
- Container metrics may not be a semantic replacement for virtual-machine metrics.
- `zpool.query` may not replace every existing pool source.
- Live 25.10.3 observations may diverge from documented 25.10.2 behavior.
- Existing realtime ZFS hit-ratio values may remain semantically unreliable.

The implementation should proceed conservatively: validate the documentation and profiles first, preserve the existing contract, add explicit unit handling, and only expose new v26 data when its semantics are proven.
