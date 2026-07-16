# T21 — Optional batch: new low-cost metrics (stretch)

- **Priority:** P3 (stretch — only after all other tasks are done or explicitly requested)
- **Size:** M
- **Depends on:** T11 (profile hygiene) — and read T04/T08 Outcomes for established patterns
- **Review reference:** review-report.md section (b) rows 8–13

Each sub-item is independent; implement in order, skip any that turns out unsupported by the
docs, and record skips with reasons in Outcome. All methods below are already in
`READ_ONLY_METHOD_ALLOWLIST` / telemetry candidates unless noted — verify membership in
`api_catalog.py` before calling; if absent, adding to the allowlist requires the doc file to
exist in **both** corpora (or profile-gating like `smb.status`).

## Item 1 — API key inventory & expiry

- Method: `api_key.query` (verify: it is allowlisted read-only but the `api_key.` namespace is
  in `SENSITIVE_NAMESPACE_PREFIXES` — check `api_catalog.py:614`. If sensitive-blocked for
  generic reads, a dedicated collector with a strict
  `select: ["id", "name", "expires_at", "revoked"]` is the pattern; confirm the doc schema
  first: `docs/truenas-api/methods/api_key/query.md`).
- Metrics: `truenas_api_key_count` (gauge), `truenas_api_key_expiry_timestamp_seconds{name}`
  (gauge; absent when `expires_at` null = non-expiring),
  `truenas_api_key_revoked_count` (gauge).
- Never select or log the key material fields.

## Item 2 — HA reboot info

- Method: `failover.reboot.info` (docs in both corpora; telemetry candidate, unreferenced).
- Metrics: `truenas_failover_node_reboot_required{node}` (gauge 0/1) from the documented
  per-node structure (read the doc for exact shape: `docs/truenas-api/methods/failover/reboot/info.md`).
- On non-HA systems the call may error → absent, debug log (standard pattern).

## Item 3 — KMIP sync pending

- Method: `kmip.kmip_sync_pending` (boolean, allowlisted, unreferenced).
- Metric: `truenas_kmip_sync_pending` (gauge 0/1) via `_set_optional_bool_gauge`.

## Item 4 — Interface speed / link state from realtime (v26-documented fields)

- Source: `reporting.realtime` event `interfaces.<name>.speed` (Mbit/s) and `link_state`
  (enum) — documented required on v26 (`docs/truenas-api-v26/events/reporting/realtime.md`),
  present in the 25.10 fixture too.
- Metrics: `truenas_interface_realtime_speed_mbits{interface}` (gauge; keep the documented
  Mbit unit **in the name**), `truenas_interface_realtime_link_up{interface}` (gauge 0/1 via
  `_link_is_up` — reuse `collection.py`).
- Event-owned: register in `events.py` `_EVENT_METRICS["reporting.realtime"]` (T04 checklist:
  publish/expire/reset-exclusion + the three tests).

## Item 5 — v26 `zpool.query` status detail (only if time permits)

- v26-only method (gate exactly like `smb.status`: add to `V26_ADDED_METHODS` +
  `allows_method` check in the collector). Metric:
  `truenas_pool_status_code{pool,status_code}` info-style gauge from the documented
  `status_code` field. Skip if the profile plumbing gets non-trivial — note instead.

## Rules for every item

- Declare via `declare_gauge` in `metrics.py`; bounded labels only; absent-on-failure; dedicated
  collector functions following the existing `_collect_*(client, cache)` pattern; wrap in
  try/except + `LOG.debug`.
- Update the parity generator mapping tables for each new metric (source method + fields).
- Regenerate contract/parity/dashboard; minor-version-worthy — note in TASKS.md.

## Tests

Per item: (1) fake payload → exact samples; (2) failure/null → absent; (3) for item 4, the
event-owned trio (publish, expire, reset-survival); (4) for items with `select`, RecordingClient
assertion that only the safe fields are requested.

## Verification

```
python3 -m pytest tests/ -q
python3 scripts/generate_metric_contract.py && python3 scripts/generate_api_exporter_parity.py && python3 scripts/generate_truenas_dashboard.py
./scripts/validate.sh
```

## Definition of done

- Implemented items emit from fixtures with absent-on-failure semantics and truthful parity
  rows; skipped items documented with doc-based reasons; validate.sh green; TASKS.md updated.

## Outcome

Completed 2026-07-16:

- Implemented item 1 with a dedicated `api_key.query` collector using strict
  `select: ["id", "name", "expires_at", "revoked"]`, plus count-mode revoked
  aggregation. New metrics: `truenas_api_key_count`,
  `truenas_api_key_expiry_timestamp_seconds{name}`, and
  `truenas_api_key_revoked_count`.
- Implemented item 2 from documented `failover.reboot.info` structures. New
  metric: `truenas_failover_node_reboot_required{node}` for `this_node` and
  available `other_node` structures; `other_node: null` remains absent.
- Implemented item 3 from documented `kmip.kmip_sync_pending`. New metric:
  `truenas_kmip_sync_pending`.
- Implemented item 4 from `reporting.realtime` interface `speed` and
  `link_state`. New event-owned metrics:
  `truenas_interface_realtime_speed_mbits{interface}` and
  `truenas_interface_realtime_link_up{interface}`; ownership covers publish,
  expiry, and poll-reset survival.
- Implemented item 5 as a v26-only profile-gated collector by adding
  `zpool.query` to `V26_ADDED_METHODS` and calling it only when the active
  profile allows it. New metric:
  `truenas_pool_status_code{pool,status_code}`.
- Updated parity generator source/field mappings for all new metrics and
  regenerated metric contract and parity artifacts. Dashboard generation
  produced no dashboard file diff.
- Added focused tests for safe API key selects, failure/null absence, KMIP
  null handling, failover `other_node: null`, v26 zpool profile gating, and
  realtime interface publish/expiry/reset behavior.
- Verification passed: focused
  `python3 -m pytest tests/test_t21_low_cost_metrics.py tests/test_phase2_events.py tests/test_api_catalog.py tests/test_runtime_api_parity.py -q`
  (`60 passed`), full `python3 -m pytest tests/ -q` (`241 passed,
  4 skipped`), required generators
  `python3 scripts/generate_metric_contract.py`,
  `python3 scripts/generate_api_exporter_parity.py`, and
  `python3 scripts/generate_truenas_dashboard.py`, and
  `./scripts/validate.sh` (`245 passed`, 91.31% coverage, dashboard
  validation, generated checks, `public_release_audit_ok`, Docker build,
  version smoke `5.2.0`, `validation_ok`).
- Skipped sub-items: none.
- Versioning: minor-version-worthy because new metrics were added; no existing
  metric names, types, HELP text, or label sets changed, and no mutating API
  calls were added.
