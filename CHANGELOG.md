# Changelog

All notable changes to this project are documented here.

## 5.2.0rc1 — TrueNAS 27 candidate

- Add an explicit 27.0 compatibility profile, suppressing historical methods
  absent from the pinned local or official API 27.0.0 documentation.
- Support `auth.login_ex(API_KEY_PLAIN)` with optional `TRUENAS_USERNAME`;
  require explicit success and never downgrade after rejection. Keep legacy
  key-only authentication for existing configurations.
- Enforce scrape deadlines before connect/send/receive, isolate required source
  failures, and limit query fallbacks to invalid-parameter responses.
- Enforce event freshness during snapshot exposition even while polling blocks;
  retain both realtime disk-map input spellings.
- Bound optional generic extraction with `MAX_GENERIC_SERIES` and add
  `truenas_generic_series` and `truenas_generic_series_limit_hits_total` diagnostics.
- Preserve all pre-existing metric names, types, HELP and labels. Unknown or
  unsupported sources remain absent/NaN rather than fabricated values.
- Preserve both dashboards, make Mission Control generation offline/repeatable,
  validate both formats and show generic-budget diagnostics.
- Add pinned local/official API Markdown, exhaustive compatibility/metric
  inventories, architecture and baseline reviews, and a reusable Codex/Claude skill.
- Keep publication local and explicit; prereleases never update `latest`.

Authenticated live checks against 27.0.0-RC.1 were performed with an
administrator key. A least-privilege key and the 27.0 GA release remain
unverified.
See `docs/reviews/` and `docs/modernization/README.md` for evidence and limitations.

## Unreleased - 5.2.0

### Fixed

- stop inflating `truenas_vm_available_memory_bytes` (and `truenas_vm_vmemory_in_use_bytes`) by 1024² on TrueNAS 25.10: live 25.10.3 returns these VM memory methods in bytes despite the pinned docs saying megabytes, so the `25.10` profile now passes bytes through unchanged, matching the `26.0` profile (metric name, type, help, and labels unchanged)
- preserve valid numeric zero and boolean false values when parsing alternative API fields
- expire stale event-derived telemetry instead of retaining disconnected values indefinitely
- reset polling gauges to a fresh snapshot so optional-method failures cannot retain stale values or look like zero
- align system readiness/product identity, reboot reasons, update status/downloads, VM memory units, pool fragmentation/dedup/expansion, dataset identity/compression, interface MTU, disk temperature parameters, GPU nesting, IPMI fields, DockerHub limits, directory-service health, NFS protocols, NTP poll intervals, security configuration, boot environments, and audit units with the 25.10.2 schemas
- restore all 22 documented `reporting.realtime.zfs` demand/L2ARC fields, converting percentage values to Prometheus ratios
- remove the undocumented `smb.status` and `smart.test.results` calls and invalid query fields/parameters
- use exact server-side count queries where a configured list limit previously under-reported totals
- reject boolean/non-finite numeric values, out-of-range percentages, invalid count responses, and malformed reboot reasons instead of emitting plausible zeroes
- fail closed on selected `disk.query` errors, mask configured filesystem/app/VM identities in generic path labels, and block generic extraction for raw, opaque, identity-bearing, and configuration-heavy responses
- stop reading opaque task-job state/time objects and secret-bearing advanced-system configuration; affected compatibility metrics now remain absent/NaN
- stop relabelling opaque or configuration values as CPU-user utilization, gateway reachability, UPS live status, virtual utilization, FC detail, or vdev error telemetry
- expose API, collector, exporter, and event diagnostics from collector mode
- make `docker compose up --build` build the checked-out source
- replace private Prometheus example targets with a portable service-network configuration
- reconcile the dashboard generator and committed dashboard path

### Added

- strict configuration validation, total scrape budgets, custom CA files, and API-key files
- `/readyz` readiness endpoint and graceful signal-driven shutdown
- installable `src/` package, console command, and Python 3.14 container image
- MIT license, security and support policies, metric contract, API-doc manifest, and modernization roadmap
- automatic TrueNAS 25.10, 26.0, and fail-closed unknown compatibility profiles selected from `system.version_short`
- exhaustive machine/human-readable API parity artifacts covering all 1,011 API Markdown files, 767 methods, 63 event sources, 114 namespaces, and every dedicated metric
- documentation-derived catalogs for 398 read-only methods, 112 telemetry candidates, 60 sensitive reads, 43 non-secret generic-response exclusions, and 63 documented events
- fixture-based 25.10.2 regressions for full, sparse, null, false, zero, malformed, timestamp, count, fallback, optional-failure, stale-event, and recovery shapes
- compatibility-safe replacement metrics for dedup-table bytes, expansion fields, configured default gateway, certificate expiry timestamps, boot-environment activation/used bytes, AMD-ASID support, directory faults, audit retention/capacity/remote logging, DockerHub remaining window, GPU host/critical status, NFS RDMA, SMB1/NTLMv1/encryption, and update download progress
- local lint, type, coverage, generated-asset, Compose, image, Python-matrix, security-audit, live-smoke, and manual-release tooling

### Changed

- collector mode is now the default; set `EXPORTER_MODE=legacy` to retain the previous coordinator for this compatibility release
- container startup now uses the `truenas-exporter` entrypoint; Compose `command:` overrides that repeated `python /app/truenas_exporter.py` must be removed
- configuration parsing is strict: values such as `TRUENAS_VERIFY_TLS=maybe`, HTTP URLs, invalid ports, and relative filesystem paths now abort startup instead of being tolerated
- generic method selection now requires membership in both the 25.10.2 read catalog and the reviewed telemetry/base set; mutators, unsafe/entity-specific operations, and sensitive full responses cannot be enabled through discovery or `EXTRA_METHODS`
- default event subscriptions are profile-aware: 25.10 keeps `reporting.realtime`, `app.stats`, and `virt.instance.metrics`; 26.0 and unknown use `reporting.realtime`, `app.stats`, and `container.metrics`
- v26 and unknown profiles suppress removed sources before transport: `virt.instance.query`, `virt.volume.query`, `reporting.graphs`, `reporting.netdata_graphs`, and `virt.instance.metrics`; `nvmet.global.sessions` remains allowed as a bounded count source because live 26.0.0-BETA.2 still serves it
- event streams now require valid string `core.subscribe` IDs and unsubscribe tracked IDs with `core.unsubscribe` during clean shutdown and reconnect cleanup
- the generated dashboard now uses verified producers only, removes fabricated `or vector(0)` fallbacks, and migrates panels to the compatibility replacements

### Deprecated

- `truenas_pool_dedup_ratio` (byte-valued API field), `truenas_pool_expand_size_bytes`, `truenas_network_gateway_reachable`, `truenas_boot_env_size_bytes`, `truenas_vm_flag_amd_asids`, `truenas_certificate_days_to_expiry`, and `truenas_directoryservices_fault_reason` are retained for compatibility; see the README migration table for replacements
- legacy metrics with no safe documented 25.10.2 source now remain absent/NaN instead of emitting fabricated values: dataset referenced bytes; memory free/cache/buffer and swap detail; disk temperature-alert and SMART detail; pool scrub and generic task state/last-run; cloud-backup state; vdev errors; SMB sessions/files/connections; NFS operation rate; FC port detail; virtual volume/global state; console/serial flags; UPS/TrueNAS Connect/TrueCommand detail; and unsupported ARC aggregate metrics
- secret- or PII-bearing configuration responses are no longer fetched for SSH password-auth, KMIP, mail, proxy, support-contact, or directory-service configuration-detail metrics

### Policy

- hosted CI is intentionally prohibited; validation and releases are local and explicit
- TrueNAS SCALE 25.10.2 remains the authoritative API compatibility target
