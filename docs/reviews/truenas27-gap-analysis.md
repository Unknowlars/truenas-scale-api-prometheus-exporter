# TrueNAS 27 code-fit, code review and metric gap analysis

Date: 2026-10-19. Branch: `feat/truenas-27-support` (after commit `a1a5526`).
Target: TrueNAS SCALE 27 (primary), keeping 25.10 and 26.0 compatibility.

## Evidence boundary

Evidence tiers used below:

| Tier | Meaning in this report |
| --- | --- |
| LOCAL-DOCS | `docs/api/truenas-27/` (rendered from a local server's `/api/docs`, `truenas_version` 27.0.0), `docs/truenas-api-v26/`, `docs/truenas-api/` (25.10.2) |
| OFFICIAL-DOCS | `docs/api/truenas-27-official/` |
| SOURCE | Static reading of `src/truenas_exporter/` |
| MOCKED-TEST | A throwaway mock run against the real runtime code (not added to `tests/`) |
| LIVE | Not used. **No API call was made for this analysis.** |

UNCONFIRMED marks a schema that is untyped, opaque or that disagrees between archives.

Before analysis, every generator was run with `--check`, and all were up to date: `generate_api_docs_manifest.py` (25.10, 26.0.0, 27, 27-official), `generate_api_exporter_parity.py` (default, 26.0.0, `--compat-diff`), `generate_truenas27_review.py` and `generate_metric_contract.py`.

This report replaces an earlier uncommitted draft of the same file. These draft claims were corrected:
- "`reporting.graphs`/`reporting.netdata_graphs` removed in 27" is wrong. Both 27 archives document them (section 1.2).
- "`zfs.tier.*` role `DATASET_READ`" is true only in LOCAL-DOCS. OFFICIAL-DOCS says `ZFS_RESOURCE_READ`.
- The draft missed the `truenas_smb1_enabled` regression (section 1.3).

## 1. Does the code hold up?

### 1.1 Profile membership (LOCAL-DOCS, OFFICIAL-DOCS, SOURCE)

| Profile | Reviewed methods | Telemetry methods | Events | Default subscriptions | Missing from target docs |
| --- | --- | --- | --- | --- | --- |
| 27.0 | 381 | 106 | 3 | `reporting.realtime`, `app.stats`, `container.metrics` | **None** (checked against both 27 archives) |
| 26.0 | 396 | 106 | 3 | same | 17 reviewed methods are absent from the 26 docs (see below) |
| 25.10 | 397 | 111 | 3 | `reporting.realtime`, `app.stats`, `virt.instance.metrics` | None |
| unknown | intersection of 25.10 and 26.0 | | | | All telemetry methods exist in both 27 archives. 15 reviewed-only methods do not |

The 26.0 profile allows 17 methods that the 26 doc snapshot lacks: `app.available`, `app.latest`, `disk.get_instance`, `nvmet.global.sessions`, `tn_connect.ip_choices`, `vm.device.pptdev_choices`, and 11 `virt.*` choice/get_instance methods. Only `nvmet.global.sessions` is a telemetry method, and it is intentionally kept based on a recorded live 26.0.0-BETA.2 observation (`compat_profiles.py:28`). No collector calls the others (SOURCE, by grep), so there is no runtime effect. This is profile hygiene only.

### 1.2 Removed or renamed surfaces, 26.0 → 27

| Surface | 27-local | 27-official | 27 profile | Fallback |
| --- | --- | --- | --- | --- |
| `pool.dataset.encryption_algorithm_choices` | absent | absent | excluded | not used by collectors |
| `disk.get_instance`, `tn_connect.ip_choices` | present | absent | excluded (conservative) | not used by collectors |
| `core.debug`, `zfs.resource.create` | present | absent | not allowed | mutating/diagnostic; correctly never allowed |
| `boot.environment.get_instance` | absent | present | not added | not needed |
| events `app.image.query`, `app.registry.query` | present | absent | not subscribed | n/a |
| events `boot.environment.query`, `zfs.resource.list` | absent | present | not subscribed | n/a |
| `virt.*`, event `virt.instance.metrics` | absent | absent | excluded since 26.0 | `container.query`/`container.metrics` path (`runtime.py:4419`, `events.py:137`) |
| `smart.test.results` | absent | absent | not used | gauges intentionally unavailable (`runtime.py:3616`) |
| **`reporting.graphs`, `reporting.netdata_graphs`** | **present** | **present** | **excluded** | Feeds only opt-in generic metrics (`runtime.py:2411`) |

Disagreement: `V26_REMOVED_METHODS` (`compat_profiles.py:18`) removes `reporting.graphs` and `reporting.netdata_graphs` because the 26 doc snapshot lacks them, but both 27 archives document them (role `REPORTING_READ`). `app.available`, `app.latest` and `nvmet.global.sessions` follow the same pattern: absent from 26 docs, present in both 27 archives. This suggests the 26 snapshot is incomplete rather than that these methods were removed. Impact is low: with `ENABLE_GENERIC_METHOD_METRICS=true`, the generic `truenas_method_*` series for reporting graphs are absent on 26/27. Whether the methods are actually served needs a live check.

### 1.3 Consumed-field changes for methods the exporter uses

Parameters, required roles and return types of all 106 telemetry methods are identical between 26.0 docs and 27-local, and between 27-local and 27-official, as compared by `generate_truenas27_review.snapshot()`. Field-level checks used the per-metric `field_verification_27_*` rows in `docs/reviews/truenas27-inventory.json`. After removing placeholder entries ("bounded dynamic JSON path", scalar `result` returns, and multi-source cross-mappings), one real regression remains:

| Field | 25.10 | 26.0 | 27-local | 27-official | Code | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `smb.config.enable_smb1` | documented | **absent** | **absent** | **absent** | `runtime.py:5056` reads `smb.get("enable_smb1")` | `truenas_smb1_enabled` is silently absent on 26/27. The SMB1 panel in both dashboards is empty. |

The replacement is `smb.config.minimum_protocol`, enum `SMB1`/`SMB2`/`SMB3`, documented as "`SMB1` enables legacy client support" (LOCAL-DOCS and OFFICIAL-DOCS). The fixture at `tests/test_runtime_api_parity.py:312` still uses the 25.10 field, so tests do not catch this. The other fields read from `smb.config` (`multichannel`, `ntlmv1_auth`, `encryption`) are present in all three versions.

Untyped schemas in 27, all UNCONFIRMED: `reporting.realtime` `fields.cpu` and `fields.interfaces` are documented only as `object` with no sub-fields. The per-core, temperature and NIC keys the code reads (`runtime.py:1900-1933`, `usage`, `temp`, `cpuN`) cannot be checked against the 27 docs. In 25.10 and 26 the realtime disk map key was `disls`; 26 and 27 document `disks`. The code accepts both (`runtime.py:1997`).

### 1.4 Local vs official 27 snapshots

| Difference | Detail |
| --- | --- |
| Presence | Methods only in local: `core.debug`, `disk.get_instance`, `tn_connect.ip_choices`, `zfs.resource.create`. Only in official: `boot.environment.get_instance`, `sharing.s3.recover`, `sharing.s3.recoverable_buckets`. Events: see 1.2 |
| Roles | `zfs.tier.config` and `zfs.tier.rewrite_job_query`: local `DATASET_READ`, official `ZFS_RESOURCE_READ`. Matters for gap G1 |
| Signatures | `truenas27-inventory.json` records 60 used-method signature disagreements at the field-hierarchy level. None changes roles, parameters or return types of a telemetry method (1.3) |

### 1.5 HELP text units and semantics (SOURCE vs LOCAL-DOCS)

| Check | Result |
| --- | --- |
| `*_percent` HELP says 0 to 100 | Consistent |
| ZFS `*_ratio` metrics say 0.0 to 1.0 | Consistent. The docs' `*_percentage` fields are divided by 100 (`runtime.py:1990-1993`) |
| `*_bytes` metrics vs MiB | No HELP text claims MiB or KiB. VM memory is treated as bytes based on a recorded live 25.10.3 observation (`compat_profiles.py:119`) |
| Gauges named like counters | `truenas_pool_scan_bytes_total` and `truenas_app_dockerhub_pull_limit_total` are gauges with a `_total` suffix. `truenas_app_blkio_{read,write}_bytes` are cumulative but typed gauge (HELP says "use rate()"). These metric names are already published, so they can only gain aliases. Low priority |
| `*_per_second` | Instantaneous snapshots from the realtime stream, correctly typed gauge |

### 1.6 Auth, subscription and error handling vs documented JSON-RPC behaviour

| Path | Finding |
| --- | --- |
| `auth.login_ex` `API_KEY_PLAIN` | Matches LOCAL-DOCS (mechanism, `login_options`, `response_type` `SUCCESS`). `user_info` and `reconnect_token` are both disabled |
| Non-SUCCESS login | Raises `"auth.login_ex did not return SUCCESS"` (`transport.py:147-148`). The documented `response_type` values (`AUTH_ERR`, `EXPIRED`, `OTP_REQUIRED`, `REDIRECT`) are a closed, non-secret enum, but they are dropped from the error, so an expired key looks the same as a wrong one (finding R4) |
| JSON-RPC errors | Code is kept, server message is never echoed (`transport.py:112-115`). Good |
| Stray messages | Discarded up to 100 by id, deadline enforced per recv (`transport.py:93-97`) |
| Subscriptions | Profile-gated before `core.subscribe`. Empty or non-string ids are rejected. Idle deadline handles dead sockets. Unsubscribe is skipped on dead connections (`runtime.py:2153-2306`) |
| Version → profile | `27.0.*` maps to 27.0, including `-RC.1` and the `TrueNAS-SCALE-` prefix (tested in `tests/test_truenas27.py`). Any other 27.x string falls back to `unknown`, whose telemetry set is still inside the 27 docs |

## 2. Code review

Findings with a concrete failing scenario only, ordered by severity.

| # | Severity | Location | Finding | Failing scenario | Tier |
| --- | --- | --- | --- | --- | --- |
| R1 | High | `runtime.py:4141` (`success = not self._required_source_failed`), with collectors from `runtime.py:4072` to `4139` | Budget exhaustion after the last `_source_scope` block is reported as a successful scrape | The scrape budget expires just after `update.status`. Each later `_call` raises `TimeoutError` immediately, and the ~30 `_collect_*` helpers catch `Exception` (73 handlers, none of them `_source_scope`), so `success` stays true. Mock result: 45 calls succeeded, **74 failed with `TimeoutError`, `truenas_up=1`, `is_ready()=True`**. Dashboards show gaps with no `up=0` and no alert | MOCKED-TEST |
| R2 | Medium | `runtime.py:5056` | `truenas_smb1_enabled` reads a field removed in 26/27 | On any 26.0 or 27 system the gauge is NaN or absent, even when `minimum_protocol` is `SMB1`, which is exactly the insecure case the panel is meant to flag | LOCAL-DOCS, OFFICIAL-DOCS, SOURCE |
| R3 | Low | `runtime.py:4560-4613`, `4893-4951` | Heavy-query cache TTL counts collector cycles, not wall time | The NAS is unreachable for 6 h, so the cycle counters do not advance. On reconnect, `truenas_snapshot_oldest_timestamp_seconds` and `truenas_disk_temperature_agg_celsius` re-emit values that are 6 h old for up to 9 more cycles (~4.5 min at 30 s) before the next refresh | SOURCE |
| R4 | Low | `transport.py:147-148` | Login failure reason is discarded | An expired API key logs the same message as a wrong one, so the operator cannot tell from logs that the key needs rotation | SOURCE |

Checked with no finding: collector error isolation (`_source_scope` re-raises transport errors and contains data errors), null vs zero (`_set_optional_bool_gauge` and `_as_float` omit rather than zero), poll-metric reset under the lock and timer publish under the lock (`runtime.py:905-915`), stale event expiry and the snapshot freshness projection, generic series and status-label cardinality bounds, mutating calls (every call passes `_require_profile_method`, and generic discovery also passes `is_documented_read_only_method`, sensitive-method and deny-regex filters), and traceback host redaction.

Hardening note, no current failure: `Config` (`config.py:16`) is a plain dataclass with `api_key: str`, so its default `repr` contains the key. Nothing logs a `Config` today. `field(repr=False)` would prevent a future leak.

## 3. Events (LOCAL-DOCS)

84 events in 27. 61 are `*.query` or ADDED/CHANGED/REMOVED notifications for configuration objects. The rest:

| Event | Classification |
| --- | --- |
| `reporting.realtime`, `app.stats`, `container.metrics` | Metric streams, all subscribed by default |
| `zfs.tier.rewrite_job_status` (new since 26) | Metric-like, but a dynamic subscription per `tier_job_id` (`dataset@uuid`). Unbounded subscriptions and per-entity identity, so rejected. Poll `zfs.tier.rewrite_job_query` instead (G1) |
| `zfs.tier.rewrite_job_query` | Query-change notification |
| `pool.scan` | Repeats scan progress already polled into `truenas_pool_scan_*` |
| `app.container_log_follow`, `filesystem.file_tail_follow`, `docker.events` | Log/text streams, not metrics |
| `auth.sessions`, `user.web_ui_login_disabled` | `FULL_ADMIN`, security-sensitive |
| `system.ready`, `system.shutdown`, `system.reboot.info`, `update.status`, `docker.state`, `directoryservices.status`, `failover.*`, `tn_connect.config`, `truecommand.config`, `core.get_jobs` | State changes already polled, or config. No added value from subscribing |

No new event subscriptions are recommended.

## 4. Metric gaps

Screening: 188 documented read-only 27 methods have numeric, boolean or enum return fields that no metric consumes (1,283 fields in total; the full listing is a scratchpad artefact and was not committed). After removing configuration flags, secrets, untyped objects, mutating/download methods, HA- and hardware-only data and per-entity identifiers, these remain.

### 4.1 Recommended (ranked)

| Rank | Candidate | Method / role | Fields | Proposed metric | Labels, cardinality | Extra calls per cycle | Profiles | Dashboard | Needs live |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| G0 (fix) | SMB1 via new field | `smb.config` / existing | `minimum_protocol` enum | Keep `truenas_smb1_enabled`, set to 1 when `minimum_protocol == "SMB1"` and fall back to `enable_smb1` on 25.10. Optional new `truenas_smb_minimum_protocol_info{protocol}` | `protocol` ∈ 3 values | 0 | 25.10 (fallback), 26.0, 27 | Existing SMB1 panel starts working again | Confirm field on a live 27 |
| G1 | Pool vdev health counters | `zpool.query` (`POOL_READ`), already called once per cycle with `[{}]` | `topology.*.stats.slow_ios` (int or null), `self_healed_bytes`, `dio_verify_errors`, `initialize_errors` | `truenas_pool_vdev_slow_ios`, `truenas_pool_vdev_self_healed_bytes`, `truenas_pool_vdev_dio_verify_errors` (gauges, matching the existing `truenas_pool_vdev_*_errors`) | `pool`, `vdev`, same bound as the existing vdev error metrics | 0. Add `topology: true` to the existing call (larger response) | 26.0, 27 (`zpool.query` does not exist in 25.10) | Add to the pool health row | Response size on large pools. `slow_ios` null semantics |
| G2 | ZFS tiering | `zfs.tier.config`, `zfs.tier.rewrite_job_query`. Role UNCONFIRMED: `DATASET_READ` (local) or `ZFS_RESOURCE_READ` (official) | `enabled` (bool), `max_concurrent_jobs` (int), per-job `status` enum (6 values) | `truenas_zfs_tier_enabled`, `truenas_zfs_tier_rewrite_jobs{status}` | `status` ≤ 6. Never use job UUID or dataset as labels | 2 (one bounded `select:["status"]`/`limit` query) | 26.0, 27 | New small panel | Role, and whether a read-only key may call it |
| G3 | Cheaper snapshot count | `zfs.resource.snapshot.count` (`SNAPSHOT_READ`, both archives) | per-dataset counts | No new metric. Could back `truenas_snapshot_count` and `truenas_dataset_snapshot_count` | n/a | Replaces 1 or more | 26.0, 27 | none | Only worth doing if snapshot scrape cost is measured as a problem |

All candidates add metrics only. Existing names, types, HELP text and labels stay unchanged. Each needs the profile allowlist updated (`zfs.tier.*` and `zfs.resource.snapshot.count` are not in the 27 profile today), fixtures under `tests/`, metric-contract entries and both dashboard formats.

### 4.2 Reviewed and rejected

| Source | Reason |
| --- | --- |
| `zfs.tier.rewrite_job_status` event | Per-job dynamic subscription (see section 3) |
| `pool.query` `bytes_issued`, `function`, `state`; `boot.get_state` scan fields | Already covered by `truenas_pool_scan_*` and `truenas_boot_pool_scan_*` |
| `zpool.query` `healthy`, `warning`, `fragmentation`, space fields | Duplicates `pool.query` metrics already exported |
| `pool.dataset.query` `tier_type`; nested tier job `status` | Per-dataset or per-share identity. G2 aggregates job status without identity |
| `disk.query` `rotationrate`, `slot`, `sed`, `hddstandby`, `advpowermgmt`, `number` | Hardware inventory or configuration |
| `interface.query` `vlan_*`, `ipv4_dhcp`, `rx_queues` and similar | Configuration |
| `container.query` `autostart`, `capabilities_policy`, `gpu_type` and similar | Configuration or inventory |
| `boot.environment.query` `can_activate`; `update.status` `matches_profile` | Static flags |
| `disk.temperature_alerts` `dismissed`, `one_shot` | Covered by alert metrics |
| `filesystem.*`, `sharing.smb.*`, `privilege`, `user`, `group`, `ftp`, `iscsi.*`, `nvmet.*` config fields | Configuration, ACLs or identities |
| `enclosure2.query` | Untyped object, and only populated on iXsystems hardware. UNCONFIRMED |
| `s3.*`, `sharing.s3.*` (new in 27) | Configuration. `s3.accesskey.*` touches credentials |
| `truenas.entitlements.*`, `core.debug`, `service.start/stop/restart/reload` | Licensing, diagnostics or mutating, excluded by policy |
| `reporting.graphs`, `reporting.netdata_graphs` | Graph-name discovery only. Could be restored to the 26/27 profiles for generic metrics after a live check (section 1.2) |

## 5. Recommended follow-up (prioritised)

1. **R1**: make budget exhaustion fail the scrape. For example, check `time.monotonic() >= deadline`, or count `TimeoutError`s, before `success = ...`, and add a regression test that exhausts the budget late in the cycle.
2. **R2/G0**: derive `truenas_smb1_enabled` from `minimum_protocol` on 26/27, keeping `enable_smb1` for 25.10. Add 26/27 fixtures.
3. **Live read-only check** on a 27 system: `smb.config.minimum_protocol`, `zpool.query` with `topology: true` (size and `slow_ios`), the `zfs.tier.*` role and access with the read-only key, `reporting.graphs` and `app.available` presence, the `reporting.realtime` `cpu` and `interfaces` payload keys, and the actual `system.version_short` string.
4. **G1** pool vdev health counters (26.0 and 27).
5. **G2** ZFS tiering, after the role is confirmed.
6. R3 (wall-clock TTL for the heavy-query caches) and R4 (log the `response_type` enum on login failure).
7. Profile hygiene: reconcile the 26.0 profile with its doc gaps (section 1.1), and add `repr=False` to `Config.api_key`.

## 6. Limits of this analysis

- No live API evidence. Method presence in the docs does not prove permissions, response contents or support on a particular build.
- Field gaps come from the parity field mappings, which are coarse for nested fields. Some fields read through nested paths may show up as gaps, and the screen in section 4 is a filter, not an exhaustive audit.
- The 26 doc snapshot appears incomplete (section 1.2). Differences inferred from it should be treated as UNCONFIRMED.
- Not verified: the Python version matrix (`RUN_PYTHON_MATRIX`), the dependency audit (`RUN_SECURITY_AUDIT`), image scanning, and dashboard rendering in a browser.
