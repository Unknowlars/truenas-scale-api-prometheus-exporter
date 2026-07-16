# 1. Executive verdict

APPROVED WITH REQUIRED PLAN CHANGES

The repository is not yet ready for production implementation exactly as planned. The current 25.10.2 exporter baseline is well-evidenced and validates cleanly, but the v26 side is not sufficiently pinned for coding-agent work: the checked-in v26 tree has no manifest, no raw source tree, no source hashes, no target-aware parity artifacts, and several planning statements disagree with the actual checked-in v26 method pages.

Finding counts:

- P0: 0
- P1: 3
- P2: 5
- P3: 3

No P0 issue was found. The unresolved P1 issues are plan/data-corpus blockers for safe v26 implementation, not evidence of unsafe behavior in the existing 25.10.2 runtime.

# 2. Review scope and repository state

- Starting commit: `967b83ec098fdcdc55d4bfbc3b2f2ab64d6b48e1`
- Starting git status: clean; `git status --short` returned no entries.
- Ending commit: `967b83ec098fdcdc55d4bfbc3b2f2ab64d6b48e1`
- Ending git status: `?? docs/truenas-25-10-2-and-26-0-0-compatibility/06-final-review.md`
- Files created: `docs/truenas-25-10-2-and-26-0-0-compatibility/06-final-review.md`
- Confirmation: no production source, tests, generated artifacts, dashboards, credentials, `.env` files, hosted automation, or existing planning documents were intentionally changed.

Scope included:

- Governance: `AGENTS.md`, `docs/modernization/README.md`.
- Compatibility docs: all documents under `docs/truenas-25-10-2-and-26-0-0-compatibility/`.
- 25.10.2 docs and artifacts: `docs/truenas-api/`, `docs/truenas-api/MANIFEST.json`, `docs/api-exporter-parity.{md,json}`.
- v26 docs corpus: actual checked-in path `docs/truenas-api-v26/`.
- Runtime surfaces: `src/truenas_exporter/runtime.py`, `transport.py`, `collection.py`, `metrics.py`, `events.py`, `api_catalog.py`, `method_safety.py`, `config.py`.
- Validation and generated assets: scripts, metric contract, dashboards, dashboard validator, parity generator, tests, fixtures.
- Official external spot checks, verified on 2026-07-13:
  - `https://www.truenas.com/docs/scale/26/gettingstarted/versionnotes/`
  - `https://api.truenas.com/v26.0/`
  - `https://api.truenas.com/v26.0/api_methods_auth.login_ex.html`
  - `https://api.truenas.com/v26.0/api_methods_auth.login_with_api_key.html`
  - `https://api.truenas.com/v26.0/api_methods_vm.get_available_memory.html`
  - `https://api.truenas.com/v26.0/api_methods_core.subscribe.html`
  - `https://github.com/truenas/api_client`

# 3. Verified facts

- VERIFIED: 25.10.2 is the locked local baseline. `docs/truenas-api/MANIFEST.json` records `truenas_version: 25.10.2`, `file_count: 1011`, generator `scripts/convert_truenas_api_docs_to_markdown.py`, and aggregate SHA-256 `377d24c74fa0836d43505f6c4db1f9ca12c105219abfeda34b6ac7d63c3f2cda`.
- VERIFIED: the existing 25.10.2 parity artifact is current. `python3 scripts/generate_api_exporter_parity.py --check` passed and reported 767 methods, 63 events, 398 documented reads, 325 mutations, 44 unsafe/session workflows, and 405 metric mappings.
- VERIFIED: the prompt path `docs/truenas-api-v26.0.0/` does not exist. The checked-in v26 corpus is `docs/truenas-api-v26/`.
- VERIFIED: `docs/truenas-api-v26/` contains 1,092 Markdown files, 805 method leaves, and 80 event leaves, but no `MANIFEST.json`, no checked-in `_sources/` tree, and no checked-in `truenas-v26.0.0-docs/` tree.
- VERIFIED: generator tooling is still target-hard-coded to 25.10.2 through `scripts/tooling.py::TRUENAS_API_VERSION = "25.10.2"` and current manifest/parity outputs target only `docs/truenas-api/`.
- VERIFIED: current runtime authentication uses `auth.login_with_api_key` in `src/truenas_exporter/transport.py::JsonRpcWsClient.authenticate`.
- VERIFIED: v26 documentation keeps `auth.login_with_api_key` but marks it deprecated and removed in v27, recommending `auth.login_ex` with API-key mechanisms; see `docs/truenas-api-v26/methods/auth/login_with_api_key.md`.
- VERIFIED: `auth.login_ex` exists in both 25.10.2 and v26 docs, but the current exporter does not implement it.
- VERIFIED: v26 `vm.get_available_memory` returns bytes, while 25.10.2 says megabytes. Current runtime multiplies by `1024**2` in `runtime.py::scrape_once`, so profile-specific conversion is required before v26 collection.
- VERIFIED: v26 `vm.get_vmemory_in_use` returns RNP/PRD/RPRD in bytes, while 25.10.2 documents MB. Current runtime multiplies by `1024**2`, so profile-specific conversion is required.
- VERIFIED: `app.image.query` exists in both `docs/truenas-api/methods/app/image/query.md` and `docs/truenas-api-v26/methods/app/image/query.md`. Planning text that treats it as removed is wrong.
- VERIFIED: `pool.is_upgraded` and `pool.ddt_prefetch` exist in `docs/truenas-api-v26/methods/pool/`. Planning text that says they are officially removed is wrong, but they remain unsuitable for generic exporter calls because they require entity/name parameters and `pool.ddt_prefetch` is an action-like method returning null after prefetch.
- VERIFIED: `nvmet.global.sessions`, `reporting.graphs`, `reporting.netdata_graphs`, `virt.instance.query`, `virt.volume.query`, and `virt.instance.metrics` are absent from `docs/truenas-api-v26/`. Later live 26.0.0-BETA.2 validation showed `nvmet.global.sessions` still serves an empty-list response, so runtime keeps only the bounded count source enabled under v26/unknown.
- VERIFIED: v26 keeps singular `reporting.graph` and `reporting.netdata_graph`, but the current exporter’s optional graph discovery calls the plural 25.10 methods.
- VERIFIED: `core.subscribe` returns a string subscription id and `core.unsubscribe` accepts that id in both doc families. Current `runtime.py::_event_stream_loop` calls `core.subscribe` but ignores the returned id and never calls `core.unsubscribe`.
- VERIFIED: configured events are validated in `config.py::load_config` against `SAFE_EVENT_SUBSCRIPTIONS`; configured extra methods are filtered in `runtime.py::_is_safe_read_method`.
- VERIFIED: current safe method discovery is 25.10-derived: `api_catalog.py` states the catalog is generated from `docs/truenas-api`, and `method_safety.py` derives exact membership from that catalog.
- VERIFIED: release tooling is dry-run by default. `scripts/release.sh` requires an explicit publish path and `AGENTS.md` prohibits hosted CI/CD automation.
- CORROBORATED: official TrueNAS v26 docs at `https://api.truenas.com/v26.0/` expose the same key methods spot-checked locally, and the TrueNAS 26 version notes page states the 26 content is early-release documentation.

# 4. API evidence matrix

Matrix conventions:

- Required role/permission: the converted Markdown front matter has `required_roles:` but no populated role list for the reviewed common surfaces. Treat this as insufficient role detail until v26 provenance/parity generation preserves role metadata.
- Runtime call site: direct runtime calls include dedicated collectors, generic discovery, count queries, transport auth, and event subscription handling.
- Planned runtime treatment: all rows require profile-aware gating before v26 production implementation.

| Current exporter method/event | runtime call site | owning source file/function | affected metric or dashboard consumer | 25.10.2 documentation evidence | 26.0.0 documentation evidence | read-only status | required role/permission | parameter/query-limit difference | response/schema/unit difference | planned runtime treatment | required fixture/test | evidence classification | source file/page reference | reviewer notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| system.version_short | direct collection/version signal | `runtime.py::_collect_system_extras`; planned bootstrap | `truenas_system_version_info`, profile selection | `docs/truenas-api/methods/system/version_short.md` | `docs/truenas-api-v26/methods/system/version_short.md` | documented read-only | not populated in converted role metadata | no query params | version string | use after auth, before discovery/events; unknown/malformed must fail closed to common profile | v25, v26, unknown, malformed, denied, timeout | VERIFIED | both method pages; `runtime.py` | Current code collects it during scrape, not as a pre-discovery profile gate. |
| auth.login_with_api_key | transport authentication | `transport.py::JsonRpcWsClient.authenticate` | session only | `docs/truenas-api/methods/auth/login_with_api_key.md` | `docs/truenas-api-v26/methods/auth/login_with_api_key.md` | session workflow; allowed only for auth | no role before login | `[api_key]`; masked in docs | v26 returns boolean and marks deprecated/removed in v27 | keep for first compatibility release; log deprecation without leaking key; plan `auth.login_ex` separately | success, false, malformed, denied, no raw key logging | VERIFIED | v26 page says deprecated and removed in v27 | Not a collector call; must not be available to generic discovery. |
| auth.login_ex | planned auth alternative only | none currently | session only | `docs/truenas-api/methods/auth/login_ex.md` | `docs/truenas-api-v26/methods/auth/login_ex.md`; official API page spot-checked | session workflow | no role before login | complex `login_data` mechanism flow | response has `response_type` outcomes and may require continuation | defer from first compatibility release unless task explicitly implements API-key mechanism without password auth | mechanism fixture only if implemented | DEFERRED | local and official v26 page | Do not silently switch to password/SCRAM behavior. |
| core.subscribe | event subscription | `runtime.py::_event_stream_loop` | event metrics | `docs/truenas-api/methods/core/subscribe.md` | `docs/truenas-api-v26/methods/core/subscribe.md`; official API page spot-checked | event transport | not populated | `[event]`; dynamic event names may include interval payload | returns subscription id string | track returned id; only subscribe profile-safe events | subscribe id success, denied event, malformed id | VERIFIED | both method pages | Current code ignores id. |
| core.unsubscribe | event teardown | not currently called | event recovery/teardown | `docs/truenas-api/methods/core/unsubscribe.md` | `docs/truenas-api-v26/methods/core/unsubscribe.md` | event transport | not populated | `[id_]` string from `core.subscribe` | returns null | call during reconnect/stop for tracked ids | unsubscribe success/failure/reconnect teardown | VERIFIED | both method pages | Required for lifecycle hardening. |
| reporting.realtime | default event subscription | `events.py`; `runtime.py::_event_stream_loop`; realtime handlers | CPU, memory, disk, network, pool, ZFS ARC dashboard panels | `docs/truenas-api/events/reporting/realtime.md` | `docs/truenas-api-v26/events/reporting/realtime.md` | read-only event | not populated | dynamic interval subscription supported | v26 structured `cpu`, `disks`, `interfaces`, `memory`, `zfs`; v25 includes legacy/opaque fields | keep for v25/v26 with profile-aware parser and no fabricated zeroes | v25 shape, v26 shape, null/malformed/non-finite, stale clearing | VERIFIED | both event pages; `events.py` | v25 `disls` compatibility must remain. |
| app.stats | default event subscription | `events.py`; `runtime.py::_event_stream_loop` | app CPU/memory/network/blkio panels | `docs/truenas-api/events/app/stats.md` | `docs/truenas-api-v26/events/app/stats.md` | read-only event | not populated | dynamic interval subscription supported | app stat field names and nullable behavior need fixture coverage | keep for v25/v26; parser must tolerate nulls without zeros | v25/v26 app stats, null/malformed | VERIFIED | both event pages | Existing current event is profile-common. |
| virt.instance.metrics | default v25 event subscription | `events.py`; `runtime.py::_event_stream_loop` | `truenas_virt_instance_*` metrics | `docs/truenas-api/events/virt/instance/metrics.md` | ABSENT | read-only event in v25 only | not populated | dynamic interval subscription in v25 | v26 removed | v25 only; never subscribe under v26/unknown | v25 subscribes, v26 does not, stale metrics cleared | VERIFIED | v25 event page; v26 absence by path search | Must be removed from v26 default events. |
| virt.instance.query | direct/generic VM extras | `runtime.py::_collect_virt_metrics`; generic candidates | virtual instance count/status metrics | `docs/truenas-api/methods/virt/instance/query.md` | ABSENT | documented read-only in v25 | not populated | query `limit/select` | v26 removed | v25 only; suppress under v26/unknown and clear stale labels | v26 call trace absence; v25 success | VERIFIED | v25 method page; v26 absence | P1 if not gated before v26 collection. |
| virt.volume.query | direct/generic VM extras | `runtime.py::_collect_virt_metrics`; generic candidates | virtual volume metrics/unavailable compatibility | `docs/truenas-api/methods/virt/volume/query.md` | ABSENT | documented read-only in v25 | not populated | query `limit/select` | v26 removed | v25 only; suppress under v26/unknown | v26 call trace absence | VERIFIED | v25 method page; v26 absence | P1 if not gated before v26 collection. |
| vm.get_available_memory | direct scrape memory | `runtime.py::scrape_once`; generic auto params | `truenas_vm_available_memory_bytes` | `docs/truenas-api/methods/vm/get_available_memory.md` | `docs/truenas-api-v26/methods/vm/get_available_memory.md`; official API page spot-checked | documented read-only | not populated | `[False]` overcommit flag | 25.10 returns megabytes; v26 returns bytes | profile-specific conversion; do not multiply v26 by MiB | v25 MB, v26 bytes, null/malformed/non-finite | VERIFIED | both method pages | Existing code would inflate v26 if unchanged. |
| vm.get_vmemory_in_use | direct/generic VM memory | `runtime.py::scrape_once`; `_safe_call_auto` | `truenas_vm_vmemory_in_use_bytes{state}` | `docs/truenas-api/methods/vm/get_vmemory_in_use.md` | `docs/truenas-api-v26/methods/vm/get_vmemory_in_use.md` | documented read-only | not populated | no params | 25.10 MB; v26 bytes for RNP/PRD/RPRD | profile-specific conversion; skip missing states | v25 MB, v26 bytes, null/malformed/negative | VERIFIED | both method pages | Existing code multiplies all states by MiB. |
| vm.query | generic/dedicated VM inventory | `runtime.py::_auto_params`; `_collect_vm_extras` | VM counts/generic metrics | `docs/truenas-api/methods/vm/query.md` | `docs/truenas-api-v26/methods/vm/query.md` | documented read-only | not populated | query `limit`, selected fields | v26 memory fields described separately; not equivalent to byte metrics without review | keep with selected fields only; do not map memory fields until reviewed | v25/v26 selected query fixtures | VERIFIED | both method pages | Memory fields remain deferred. |
| app.image.query | count query/generic | `runtime.py::_collect_misc_configs`; generic candidate | `truenas_docker_image_count` | `docs/truenas-api/methods/app/image/query.md` | `docs/truenas-api-v26/methods/app/image/query.md` | documented read-only | not populated | query/count mode; limit/offset docs common | image entry schema present in both; v26 item name differs | keep eligible after profile review; do not suppress as removed | count success, denied, malformed | VERIFIED | both method pages | Corrects old plan contradiction. |
| nvmet.global.sessions | direct/generic NVMe-oF | `runtime.py::_collect_nvmet_metrics`; BASE | NVMe-oF session count/details | `docs/truenas-api/methods/nvmet/global/sessions.md` | ABSENT in pinned corpus; live 26.0.0-BETA.2 serves empty list | documented read-only in v25; live v26 bounded count only | not populated | query filters/options | absent from pinned corpus but live-compatible as count source | keep bounded count source under v26/unknown; never recursively export full response | v26 count call trace, sensitive full response blocked | VERIFIED | v25 method page; live v26 note | No full-response v26 generic extraction approved. |
| reporting.graphs | optional generic reporting discovery | `runtime.py::_collect_reporting_timeseries`; BASE | generic reporting discovery only | `docs/truenas-api/methods/reporting/graphs.md` | ABSENT | documented read-only in v25 | not populated | query filters/options | v26 removed plural method | suppress under v26; do not auto-substitute singular method | v26 graph-discovery disabled trace | VERIFIED | v25 method page; v26 absence | Current optional path can bypass if not profiled. |
| reporting.netdata_graphs | optional generic reporting discovery | `runtime.py::_collect_reporting_timeseries`; BASE | generic reporting discovery only | `docs/truenas-api/methods/reporting/netdata_graphs.md` | ABSENT | documented read-only in v25 | not populated | query filters/options | v26 removed plural method | suppress under v26; do not auto-substitute singular method | v26 graph-discovery disabled trace | VERIFIED | v25 method page; v26 absence | Current optional path can bypass if not profiled. |
| reporting.graph | auto params candidate | `runtime.py::_auto_params`; telemetry candidate | generic reporting sample if enabled | `docs/truenas-api/methods/reporting/graph.md` | `docs/truenas-api-v26/methods/reporting/graph.md` | documented read-only but unsuitable unless explicit graph chosen | not populated | current auto param uses `["cpu", {"unit": "HOURLY"}]` | singular method exists in v26; semantics must be reviewed before replacement | do not use as replacement for plural discovery in first compatibility release | explicit graph fixture if ever enabled | DEFERRED | both method pages | v26-only replacement not approved. |
| reporting.netdata_graph | auto params candidate | `runtime.py::_auto_params`; telemetry candidate | generic reporting sample if enabled | `docs/truenas-api/methods/reporting/netdata_graph.md` | `docs/truenas-api-v26/methods/reporting/netdata_graph.md` | documented read-only but unsuitable unless explicit graph chosen | not populated | current auto param uses `["cpu", {"unit": "HOURLY"}]` | singular method exists in v26; semantics must be reviewed before replacement | do not use as replacement for plural discovery in first compatibility release | explicit graph fixture if ever enabled | DEFERRED | both method pages | v26-only replacement not approved. |
| pool.is_upgraded | entity-param method | `method_safety.py::REQUIRES_ENTITY_PARAM`; not generic | none unless entity-specific pool metric added | `docs/truenas-api/methods/pool/is_upgraded.md` | `docs/truenas-api-v26/methods/pool/is_upgraded.md` | read-only but requires pool id | not populated | mandatory integer pool id | boolean | keep blocked from generic discovery; only call with reviewed pool id if future metric approved | blocked-generic test; future per-pool fixture if used | VERIFIED | both method pages | Corrects plan claim that it was removed. |
| pool.ddt_prefetch | action-like method | not safely called; plan mentions suppression | none | `docs/truenas-api/methods/pool/ddt_prefetch.md` | `docs/truenas-api-v26/methods/pool/ddt_prefetch.md` | unsafe/action-like despite doc presence | not populated | mandatory pool name | returns null after prefetch | never call from exporter collectors/discovery/tests | denylist test | VERIFIED | both method pages | Corrects plan claim that it was removed; still must be prohibited. |
| remaining current runtime/read candidates | generic discovery, dedicated collectors, count queries, helper calls | `runtime.py`, `method_safety.py`, `api_catalog.py`, `collection.py` | 326 active dedicated metrics, 8 generic extraction metrics, 52 unavailable compatibility declarations, 313 dashboard panels | 25.10.2 parity artifact covers all 767 method rows and 63 event rows | v26 docs existence must be target-checked before implementation; current review spot-checked changed/high-risk rows above | 25.10.2 read-only partition: 398 documented reads, 325 mutations, 44 unsafe/session workflows | not populated in converted role metadata | current query limit default 200; v26 limit/offset bounds require target-aware validation | no global shape equivalence can be inferred | all must pass selected profile allowlist before call; EXTRA_METHODS, auto discovery, configured events, and count queries must share same profile gate | generated v25 parity check plus new target-aware v26 parity and fixtures | CORROBORATED | `docs/api-exporter-parity.json`; `src/truenas_exporter/api_catalog.py`; `src/truenas_exporter/method_safety.py` | Complete inventory source: `BASE_METHODS`, `TELEMETRY_CANDIDATE_METHOD_ALLOWLIST`, direct string calls, and safe event constants. |

The complete reviewed current method inventory from runtime/catalog sources is:

`alert.list`, `alertclasses.config`, `alertservice.query`, `api_key.query`, `app.available_space`, `app.image.dockerhub_rate_limit`, `app.image.query`, `app.outdated_docker_images`, `app.query`, `app.upgrade_summary`, `audit.config`, `audit.query`, `auth.login_ex`, `auth.login_with_api_key`, `auth.me`, `auth.sessions`, `auth.twofactor.config`, `boot.environment.query`, `boot.get_disks`, `boot.get_state`, `catalog.config`, `catalog.trains`, `certificate.query`, `cloud_backup.query`, `cloudsync.query`, `core.get_jobs`, `core.get_methods`, `core.subscribe`, `core.unsubscribe`, `cronjob.query`, `device.get_info`, `directoryservices.config`, `directoryservices.status`, `disk.details`, `disk.get_used`, `disk.query`, `disk.temperature_agg`, `disk.temperature_alerts`, `disk.temperatures`, `dns.query`, `docker.config`, `docker.list_backups`, `docker.network.query`, `docker.nvidia_present`, `docker.status`, `failover.disabled.reasons`, `failover.reboot.info`, `fc.fc_host.query`, `fcport.query`, `fcport.status`, `filesystem.get_zfs_attributes`, `filesystem.getacl`, `filesystem.listdir`, `filesystem.stat`, `filesystem.statfs`, `ftp.config`, `group.has_password_enabled_user`, `group.query`, `hardware.virtualization.variant`, `initshutdownscript.query`, `interface.checkin_waiting`, `interface.has_pending_changes`, `interface.query`, `ipmi.chassis.info`, `ipmi.is_loaded`, `ipmi.lan.channels`, `ipmi.lan.query`, `ipmi.sel.elist`, `ipmi.sel.info`, `iscsi.extent.query`, `iscsi.global.alua_enabled`, `iscsi.global.client_count`, `iscsi.global.iser_enabled`, `iscsi.global.sessions`, `iscsi.initiator.query`, `iscsi.portal.query`, `iscsi.target.query`, `jbof.query`, `kerberos.config`, `keychaincredential.query`, `kmip.config`, `kmip.kmip_sync_pending`, `mail.config`, `network.configuration.config`, `network.general.summary`, `nfs.client_count`, `nfs.config`, `nfs.get_nfs3_clients`, `nfs.get_nfs4_clients`, `nvmet.global.config`, `nvmet.global.sessions`, `nvmet.host.query`, `nvmet.namespace.query`, `nvmet.port.query`, `nvmet.subsys.query`, `pool.dataset.details`, `pool.dataset.query`, `pool.dataset.snapshot_count`, `pool.get_disks`, `pool.is_upgraded`, `pool.query`, `pool.resilver.config`, `pool.scrub.query`, `pool.snapshot.query`, `pool.snapshottask.max_count`, `pool.snapshottask.max_total_count`, `pool.snapshottask.query`, `privilege.query`, `replication.config.config`, `replication.query`, `reporting.config`, `reporting.exporters.query`, `reporting.get_data`, `reporting.graph`, `reporting.graphs`, `reporting.netdata_graph`, `reporting.netdata_graphs`, `route.ipv4gw_reachable`, `route.system_routes`, `rsynctask.query`, `service.query`, `service.started`, `service.started_or_enabled`, `sharing.nfs.query`, `sharing.smb.query`, `smb.config`, `snmp.config`, `ssh.config`, `staticroute.query`, `support.config`, `support.is_available`, `support.is_available_and_enabled`, `system.advanced.config`, `system.advanced.sed_global_password_is_set`, `system.boot_id`, `system.feature_enabled`, `system.general.config`, `system.global.id`, `system.host_id`, `system.info`, `system.ntpserver.query`, `system.product_type`, `system.ready`, `system.reboot.info`, `system.security.config`, `system.security.info.fips_available`, `system.security.info.fips_enabled`, `system.state`, `system.version`, `system.version_short`, `systemdataset.config`, `tn_connect.config`, `truecommand.config`, `truenas.get_chassis_hardware`, `truenas.is_ix_hardware`, `truenas.is_production`, `truenas.managed_by_truecommand`, `tunable.query`, `update.available_versions`, `update.config`, `update.status`, `ups.config`, `user.has_local_administrator_set_up`, `user.query`, `virt.global.config`, `virt.instance.query`, `virt.volume.query`, `vm.device.iommu_enabled`, `vm.flags`, `vm.get_available_memory`, `vm.get_memory_usage`, `vm.get_vm_memory_info`, `vm.get_vmemory_in_use`, `vm.maximum_supported_vcpus`, `vm.query`, `vm.status`, `vm.supports_virtualization`, `vm.virtualization_details`, `zfs.resource.query`.

The complete reviewed current event inventory is: `app.stats`, `reporting.realtime`, `virt.instance.metrics`.

# 5. Blocking findings

## P1-1 — v26 corpus is not production-pinned

- Severity: P1
- Evidence: `docs/truenas-api-v26/` has no `MANIFEST.json`, no `_sources/`, no raw HTML/RST tree, and no generated parity artifact. `scripts/tooling.py` still targets only `25.10.2`.
- Impact: coding agents cannot safely distinguish documented v26 removals, schema changes, role changes, or stale generated files. This affects safety and metric correctness.
- Required resolution: first implementation task must generate v26 manifest/parity artifacts without overwriting 25.10.2 artifacts and record source provenance/hashes.

## P1-2 — v26 profile gate does not exist yet, but current runtime has v25-only calls/events

- Severity: P1
- Evidence: current catalog is 25.10-derived. Current/default surfaces include `virt.instance.query`, `virt.volume.query`, `virt.instance.metrics`, `nvmet.global.sessions`, `reporting.graphs`, and `reporting.netdata_graphs`; these are absent from `docs/truenas-api-v26/`.
- Impact: if v26 support is implemented without an early profile gate, removed v25 surfaces can be called or subscribed to under v26.
- Required resolution: profile selection must occur immediately after authentication and before generic discovery, dedicated collection, reporting discovery, and event subscription.

## P1-3 — VM memory unit conversion would be wrong on v26 if runtime is reused unchanged

- Severity: P1
- Evidence: v25 pages document `vm.get_available_memory` and `vm.get_vmemory_in_use` in megabytes/MB; v26 pages document bytes. Current runtime multiplies both by `1024**2`.
- Impact: v26 VM memory metrics would be inflated by 1,048,576x.
- Required resolution: add profile-specific conversion before enabling v26 collection.

## P2-1 — planning docs contain incorrect v26 removal statements

- Severity: P2
- Evidence: `app.image.query`, `pool.is_upgraded`, and `pool.ddt_prefetch` exist under `docs/truenas-api-v26/methods/`, but some planning text says they are removed.
- Impact: coding agents may suppress valid read-only count sources or misclassify action-like methods for the wrong reason.
- Required resolution: correct plan wording. `app.image.query` remains eligible; `pool.is_upgraded` exists but requires entity id; `pool.ddt_prefetch` exists but must remain prohibited because it triggers prefetch/action behavior.

## P2-2 — event lifecycle plan is necessary but not yet test-complete

- Severity: P2
- Evidence: docs show `core.subscribe` returns an id and `core.unsubscribe` removes it. Current runtime ignores the id and never unsubscribes.
- Impact: reconnect/teardown behavior can leave ambiguous subscription state and cannot prove clean shutdown.
- Required resolution: COMPAT-06 must include id tracking, unsubscribe, reconnect, stop, and failure-path tests.

## P2-3 — role/permission evidence is incomplete in converted Markdown

- Severity: P2
- Evidence: reviewed Markdown front matter contains `required_roles:` with no populated role data for common pages.
- Impact: least-privilege API-key guidance and denied-response fixture coverage cannot be finalized from current converted docs alone.
- Required resolution: v26/v25 target-aware generator should preserve role metadata or explicitly record that upstream docs omit it.

## P2-4 — v26 fixture namespace is absent

- Severity: P2
- Evidence: tests have `tests/fixtures/api_25_10_2/` and realtime 25.10 fixture, but no `tests/fixtures/api_26_0_0/`.
- Impact: removed calls, byte units, structured realtime, app stats, denied/null/malformed handling, and unknown-version behavior cannot be regression-tested yet.
- Required resolution: add sanitized v26 fixtures before runtime profile implementation is considered complete.

## P2-5 — unknown-version/common-intersection behavior is only planned

- Severity: P2
- Evidence: planning docs require common-intersection behavior, but current code has no profile abstraction or unknown-version profile.
- Impact: malformed/failed version detection could accidentally retain 25.10 behavior if implementation is naive.
- Required resolution: add tests proving detection failure cannot expand permissions and cannot call v25-only/v26-only surfaces.

# 6. Required plan changes

## Change 1

- Document path: `docs/truenas-25-10-2-and-26-0-0-compatibility/01-api-baseline-and-diff.md`
- Section: Current evidence / Required implementation
- Problem: references `docs/truenas-api-v26.0.0/truenas-v26.0.0-docs/`, which is not checked in.
- Exact replacement decision or wording: use `docs/truenas-api-v26/` as the current corpus path, and state that the raw source tree is missing until provenance is restored.
- Proposed patch:

```diff
- The v26 corpus is under `docs/truenas-api-v26.0.0/truenas-v26.0.0-docs/` and
- must receive the same manifest/parity treatment.
+ The checked-in v26 corpus is under `docs/truenas-api-v26/`. The raw
+ `truenas-v26.0.0-docs/` source tree is not checked in, so COMPAT-01 must
+ either restore/source it or record equivalent provenance before generating
+ the v26 manifest and parity artifacts.
```

- Validation required afterward: v26 manifest check, v26 parity check, and `git status --short` showing only intended generated v26 artifacts.

## Change 2

- Document path: `docs/truenas-25-10-2-and-26-0-0-compatibility/truenas-25-10-2-and-26-0-0-compatibility-plan.md`
- Section: 3.3 Removed methods / 5 Existing exporter surfaces at risk
- Problem: still says `app.image.query` is removed in some sections.
- Exact replacement decision or wording: `app.image.query` exists in v26 and remains eligible after schema/permission review.
- Proposed patch:

```diff
- - `app.image.query`
+ - `app.image.query` is not removed; keep it eligible only after profile
+   safety, permission, count-mode, and schema review.

- | `runtime.py` miscellaneous configs | Calls `app.image.query` | Method removed | Suppress call; do not substitute registry query |
+ | `runtime.py` miscellaneous configs | Calls `app.image.query` | Method exists in v26; schema/permission still requires review | Keep eligible under a reviewed profile; do not substitute registry query |
```

- Validation required afterward: direct existence check for both `docs/truenas-api*/methods/app/image/query.md` and fixture-backed count-mode test.

## Change 3

- Document path: `docs/truenas-25-10-2-and-26-0-0-compatibility/01-api-baseline-and-diff.md`
- Section: Diff rules table
- Problem: says `pool.is_upgraded` and `pool.ddt_prefetch` are officially removed in v26.
- Exact replacement decision or wording: both exist in checked-in v26 docs; keep them blocked for safety/parameter reasons.
- Proposed patch:

```diff
- | `pool.is_upgraded`, `pool.ddt_prefetch` | Keep blocked/suppressed; officially removed in v26 |
+ | `pool.is_upgraded`, `pool.ddt_prefetch` | Both exist in checked-in v26 docs; keep blocked/suppressed because `pool.is_upgraded` requires a pool id and `pool.ddt_prefetch` is action-like and unsuitable for Prometheus collection |
```

- Validation required afterward: denylist tests proving neither can be reached through generic discovery or `EXTRA_METHODS`.

## Change 4

- Document path: `docs/truenas-25-10-2-and-26-0-0-compatibility/05-agent-task-board.md`
- Section: COMPAT-01 / COMPAT-02 / COMPAT-03
- Problem: profile work can start before v26 provenance is fully locked.
- Exact replacement decision or wording: COMPAT-01 is a hard gate; no runtime profile code may be written until v26 manifest/parity/provenance is validated.
- Proposed patch:

```diff
+ **Hard gate:** No runtime, transport, collector, event, or metric-contract
+ implementation may start until the v26 manifest, v26 parity artifact, source
+ provenance, and non-overwrite guarantees pass locally.
```

- Validation required afterward: COMPAT-01 completion evidence includes commands and hashes.

## Change 5

- Document path: `docs/truenas-25-10-2-and-26-0-0-compatibility/04-tests-fixtures-and-release.md`
- Section: Focused tests
- Problem: role/permission and detection-failure tests need stricter stop conditions.
- Exact replacement decision or wording: denied/malformed detection must not expand profile permissions; configured `EXTRA_METHODS` and events must share selected profile.
- Proposed patch:

```diff
+ Add regression tests proving failed, denied, malformed, empty, and unknown
+ version detection selects only the reviewed common intersection and cannot
+ enable v25-only or v26-only methods/events through `EXTRA_METHODS`,
+ generic discovery, reporting discovery, count queries, or configured
+ `EVENT_SUBSCRIPTIONS`.
```

- Validation required afterward: focused profile tests plus `./scripts/validate.sh`.

# 7. Non-blocking risks and deferred decisions

- P3: `auth.login_ex` is deferred. This is acceptable for the first 25.10/v26 compatibility release only because v26 still documents `auth.login_with_api_key`; migration before v27 must be tracked.
- P3: singular v26 `reporting.graph` and `reporting.netdata_graph` are deferred. Do not expose replacements until graph semantics, params, cardinality, and dashboards are reviewed.
- P3: v26-only container/zpool/zfs-tier additions are deferred. Do not add metrics merely because v26 exposes new read-like APIs.
- DEFERRED: live v26 smoke testing. It must remain optional, read-only, non-persistent, and credential-redacted.
- DEFERRED: new v26 dashboard panels. Existing dashboards should tolerate unavailable/NaN metrics first.

# 8. Final implementation order

| task ID | objective | owner | files/functions | prerequisites | acceptance tests | completion evidence | rollback or containment behavior |
| --- | --- | --- | --- | --- | --- | --- | --- |
| COMPAT-01A | Pin v26 docs provenance and non-overwrite behavior | docs/tooling agent | `scripts/tooling.py`, manifest/parity generators, `docs/truenas-api-v26/` metadata | none | v25 manifest/parity unchanged; v26 manifest/parity generated separately | hashes, file counts, command output | remove v26 generated artifacts only; v25 baseline remains locked |
| COMPAT-01B | Correct planning contradictions before code | planning/docs agent | compatibility docs only | COMPAT-01A evidence | doc grep for corrected `app.image.query`, `pool.is_upgraded`, `pool.ddt_prefetch`, actual v26 path | proposed patches applied in docs | revert docs only |
| COMPAT-02 | Add profile data and safety gates | runtime safety agent | `api_catalog.py`, `method_safety.py`, config/profile module | COMPAT-01A/B | unit tests for v25, v26, unknown, malformed; `EXTRA_METHODS` blocked | call-trace tests | fail closed to common profile |
| COMPAT-03 | Bootstrap version detection | transport/runtime agent | `transport.py`, `runtime.py` startup path | COMPAT-02 | auth then `system.version_short`; no discovery/events before profile | call order tests | detection failure uses common intersection |
| COMPAT-04 | Normalize shared collectors and VM units | collector agent | `runtime.py`, `collection.py` | COMPAT-03 | v25 MB and v26 byte fixtures; null/malformed/non-finite tests | metric value assertions | do not emit values for unsupported/invalid payloads |
| COMPAT-05 | Suppress removed v26 sources | collector/profile agent | `runtime.py`, `events.py`, profile data | COMPAT-03 | v26 call traces omit `virt.*`, plural reporting graph methods, `nvmet.global.sessions`; stale metrics clear | trace and metric absence evidence | unavailable/NaN, never zero substitution |
| COMPAT-06 | Harden event lifecycle | event agent | `runtime.py::_event_stream_loop`, `events.py` | COMPAT-02/03 | subscribe id tracked, unsubscribe called, reconnect and stop tested | event lifecycle tests | on failure mark stream down and reconnect without expanding subscriptions |
| COMPAT-07 | Operator docs and compatibility notes | docs agent | README, modernization evidence, compatibility docs | COMPAT-01 through 06 | docs mention profiles, unavailable v26 metrics, auth deprecation, no live data | doc review plus validation | docs-only revert |
| COMPAT-08 | Full local validation/release gate | release agent | scripts, generated assets, tests | COMPAT-01 through 07 | `./scripts/validate.sh`, target-aware v26 checks, dry-run release | command output | release remains dry-run unless explicit publish flag |

# 9. Pre-code checklist

- v26 docs path decision is corrected to `docs/truenas-api-v26/` or a restored raw source path is added.
- v26 manifest exists with file count, source provenance, generator version, and aggregate hash.
- v26 parity artifacts exist and cannot overwrite 25.10.2 artifacts.
- Planning contradictions for `app.image.query`, `pool.is_upgraded`, and `pool.ddt_prefetch` are corrected.
- Profile design includes v25, v26, and unknown/common-intersection profiles.
- Profile selection is specified before discovery, count queries, reporting discovery, collectors, and event subscriptions.
- Fixture plan includes v26 success, missing, denied, malformed, null, unknown, negative, and non-finite cases.
- `EXTRA_METHODS`, generic discovery, configured events, and count queries cannot bypass the selected profile.
- VM memory unit conversion is profile-specific.
- Event subscribe id tracking and unsubscribe behavior are testable.
- Metric contract preservation policy remains unchanged.
- Hosted automation remains prohibited.

# 10. Reviewer confidence

- Directly verified: repository governance, git state, 25.10 manifest, parity generator, v26 corpus inventory, key method/event page existence, runtime auth/event/generic-discovery paths, VM unit docs, and local validation.
- Corroborated: official v26 API/docs pages for auth, VM memory, and subscribe behavior; official TrueNAS 26 version notes identify the v26 docs as early-release content.
- Inferred: current role/permission detail is insufficient because converted pages have empty `required_roles:` fields for common reviewed surfaces; this should be fixed by generator/provenance work rather than guessed.
- Uncertain: exact upstream v26 source commit/hash for the checked-in converted corpus. Evidence required: raw source tree or official archive hash plus generated manifest.
- Uncertain: complete v26 role/permission matrix. Evidence required: preserved role metadata or upstream docs confirming omitted roles.
- Uncertain: final v26 release drift. Evidence required: regenerate/compare against final official v26.0.0 documentation at implementation time.

# 11. Validation results

| command | result | classification | relevant output |
| --- | --- | --- | --- |
| `git status --short` | passed | repository state | no entries at start |
| `git rev-parse HEAD` | passed | repository state | `967b83ec098fdcdc55d4bfbc3b2f2ab64d6b48e1` |
| `python3 scripts/generate_api_docs_manifest.py --check` | passed | 25.10 manifest check | no output |
| `python3 scripts/generate_api_exporter_parity.py --check` | passed | 25.10 parity check | 767 methods, 63 events, 405 field mappings |
| `python3 scripts/generate_metric_contract.py --check` | passed | metric contract | no output |
| `python3 scripts/generate_truenas_dashboard.py --check` | passed | dashboard generation | no output |
| `python3 scripts/validate_dashboard.py` | passed | dashboard validation | `dashboard_ok panels=313 metric_references=282` |
| `python3 -m pytest -q tests/test_runtime_api_parity.py tests/test_documented_api_shapes.py tests/test_phase2_events.py tests/test_transport.py -p no:cacheprovider` | passed | focused compatibility-related tests | `51 passed in 2.32s` |
| `git diff --check` | passed | whitespace/diff check | no output |
| `./scripts/validate.sh` | passed | full local gate | Ruff/mypy passed; `151 passed`; coverage 90.14%; dashboard ok; parity ok; Docker image built; container `--version` returned `5.2.0`; `validation_ok` |
| live smoke | not run | prohibited by review scope | no live TrueNAS calls were made |

Final state proof after writing this artifact:

- `git status --short` showed only `?? docs/truenas-25-10-2-and-26-0-0-compatibility/06-final-review.md`.
- `git rev-parse HEAD` remained `967b83ec098fdcdc55d4bfbc3b2f2ab64d6b48e1`.
