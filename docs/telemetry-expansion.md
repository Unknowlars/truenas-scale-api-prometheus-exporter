# Typed telemetry expansion — 2026-10-22

This change adds **47 metric families** to the 420-family contract, for **467**.
All 420 existing names, types, HELP strings and label sets remain unchanged.
It also activates the existing referenced-bytes metric and cloud-backup state
metric on the 27.0 profile. New telemetry is collected in background polls;
HTTP `/metrics` continues to read atomic snapshots without contacting the NAS.

## Added coverage

| Domain | New families | Source and behavior |
| --- | ---: | --- |
| Pool scans/features | 7 | `pool.query`: scan state/function, bytes issued, start/pause timestamps, paused flag, and 27-only feature-upgrade flag. Reuses the selected pool response; never invokes `pool.is_upgraded`. |
| Dataset accounting/tuning | 9 | `pool.dataset.query`: logical used/referenced bytes, space used by refreservation, record/volume block sizes, volume size, copies, sync mode and dedup enablement. Reuses the bounded selected query. |
| Disk encryption | 2 | `disk.query`: nullable SED capability and a fixed allowlist of SED states. On 27, requests `extra.sed_status=true` within `QUERY_LIMIT`; no password fields. |
| UPS measurements | 8 | `reporting.get_data`: charge, runtime, voltage, current, frequency, load, temperature, and sample timestamp. Only queried on 27 when the existing service inventory reports UPS running. |
| Cloud backup | 5 | `cloud_backup.query`: locked flag, progress, start/completion timestamps and completed-job duration, plus the existing state metric. Selects individual job fields; excludes credentials, paths, arguments, logs and error text. |
| ZFS tiering | 16 | `zfs.tier.config`, `rewrite_job_query`, `rewrite_job_status`: configuration and bounded latest-observed job state, byte/file statistics and timestamps per dataset. 27-only, explicitly added to its read-only profile. |

The authoritative names, HELP/type/labels and field mappings are generated in
[metrics-contract.json](metrics-contract.json),
[API parity](api-exporter-parity.md), and the
[27 inventory](reviews/truenas27-metric-coverage.md).

## Bounds and missing data

- Refreservation accounting and scan details tolerate absent fields on older
  profiles. New hardware options, dataset tuning/logical properties, backup
  outcomes, UPS and tiering are gated to 27. Existing 25.10/26 behavior remains.
- UPS reads at most nine graph/identifier combinations in one call covering
  90 seconds. A measurement must be finite, have a matching two-column
  time/value legend, and have a timestamp within that window. Null trailing
  rows do not erase a newer valid value. Voltage labels are limited to
  `battery`, `input`, and `output`; units are volts, amperes, hertz, Celsius,
  seconds and percentages. Exported sample timestamps expose data age.
  These are middleware reporting graph values: the release-pinned graph layer
  requests Netdata's `null2zero` option, so upstream gaps can become zeros.
  A zero graph value alone does not prove a physical UPS measurement. The
  exporter preserves returned zeros; electrical accuracy requires a real UPS
  acceptance check, and graph timestamps identify buckets rather than hardware
  observation times.
- Tier jobs are limited to `min(QUERY_LIMIT, MAX_ENTITY_CALLS, 10)` rows, sorted
  newest first. At most one detail call per observed dataset is made. These are
  latest jobs within the bounded inventory, not every historical job. The
  inventory-limit flag exposes possible incomplete coverage. UUIDs, job IDs,
  filenames and error text never become labels. Progress values are gauges
  because the API resets current-run statistics on resume/recovery.
- Unknown/malformed values remain absent or NaN; legitimate zero and false
  remain measurements. Poll resets remove old labelled series. Optional source
  absence is isolated, while transport/deadline failures still make the cycle
  unhealthy. Existing total polling deadlines are unchanged.
  First readiness now follows publication of the successful snapshot, avoiding
  a ready response while HTTP still serves the initial empty metrics snapshot.
- SED status reads may perform hardware queries and are bounded by the disk
  query limit and cycle deadline. They do not initialize/unlock disks or run
  SMART tests. Generic response extraction remains disabled by default.

## Primary-source evidence

The appliance and official API 27 snapshots are both pinned in [docs/api](api/README.md).
Their tiering roles differ (`DATASET_READ` versus `ZFS_RESOURCE_READ`), so
documentation alone does not establish least-privilege permissions.

Release tag `TS-27.0.0-RC.1` resolves to official middleware commit
`d83c3bf89aa4226c8fd1ef25dd273bdf447eb777`. Relevant source:

- [UPS graph definitions and units](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/plugins/reporting/netdata/graphs.py).
  [Graph row normalization and upstream zero filling](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/plugins/reporting/netdata/graph_base.py)
  establish the time/value matrix and its limitations.
- [Backup job attachment](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/plugins/cloud_backup/crud.py)
  and [task-state lookup](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/utils/service/task_state.py).
  Nested job fields follow the documented `core.get_jobs` schema.
- [Disk query and read-only SED extension](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/plugins/disk.py)
  and [recognized SED states](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/plugins/disk_/sed.py).
- [Dataset query property selection](https://github.com/truenas/middleware/blob/d83c3bf89aa4226c8fd1ef25dd273bdf447eb777/src/middlewared/middlewared/plugins/pool_/dataset.py).
  Logical/reference properties are also individually described by the pinned
  `zfs.resource.query` schema. `sync`/`deduplication` use native raw enum strings;
  numeric properties use `parsed` values.

## Verification evidence

- **Mocked:** RPC-to-snapshot regressions in
  `tests/test_telemetry_expansion.py` cover zero/false, malformed values,
  freshness, state expiry/recovery, projections, privacy, request bounds,
  version gating and transport health. No mocked test contacts a NAS.
- **Live source runtime:** SCALE `27.0.0-RC.1` selects profile `27.0`. A bounded
  updated poll completed in 9.611 seconds with 162 read-only RPCs, zero API
  failures, readiness true and `truenas_up=1`. It exposed 497 finite samples
  from new families. All 556 source-to-metric comparisons of dataset values,
  enum policies and tier configuration matched. Nullable SED/pool-feature
  flags remain absent when unknown; they are not inferred as false. No raw
  responses/private labels retained.
- The NAS has no observed cloud-backup tasks or tier rewrite jobs. Their
  execution statistics remain mocked-only; tier configuration is live-verified.
  UPS graph presence is live-verified, but usable UPS electrical measurements
  and all SED states are not. Real 25.10/26 appliances, least-privilege roles,
  verified TLS, live PromQL, browser acceptance and a long soak remain separate
  acceptance work. Existing owner-directed key rotation remains pending.
- Full validation and local packaged-runtime results are recorded in the
  [modernization ledger](modernization/README.md).
- **Final local gate:** `./scripts/validate.sh` passed, 357 tests, 91.80%
  branch-enabled coverage, exact 98-warning promtool baseline, all generated
  artifact/API/dashboard/Compose checks, release audit, image build and version
  smoke. All previous 420 contracts compared exactly, with 47 additions.
- **Final packaged cold start:** 15 observations over 70.68 seconds, readiness
  HTTP 200 and up=1 throughout, 497 additional finite samples at every check,
  two poll snapshots observed. CPU/event data arrived after the first complete
  polling snapshot, as independent producers. After a 15-second startup period,
  CPU stayed finite and event age stayed within the TTL; observed maximum age
  was 7.889 seconds. Final exposition contained 2,350 samples. This is a bounded
  smoke observation, not a long soak or appliance-restart test.
