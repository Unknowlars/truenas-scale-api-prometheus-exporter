# Modernization Roadmap

This roadmap tracks the production-reliability, architecture, public-release,
and validation work for the TrueNAS Prometheus exporter. TrueNAS SCALE 25.10.2
is the compatibility baseline. Hosted CI is intentionally prohibited; all
evidence is produced locally.

## Status

| Phase | Document | Status | Evidence |
| --- | --- | --- | --- |
| 1 | [Reliability](01-reliability.md) | Complete | 150 tests pass in the unrestricted local gate; zero, expiry, deadline, config, readiness, transport, and API-parity regressions covered |
| 2 | [Architecture](02-architecture.md) | Complete | Collector convergence, owned specs, package boundaries, and the 85% branch-coverage gate are complete |
| 3 | [Public release](03-public-release.md) | Complete | README, policies, MIT license, Compose, dashboard, and generated API docs validated |
| 4 | [Validation and release](04-validation-release.md) | Complete | Local gate, Python 3.12-3.14 matrix, image build, dependency audit, and dry-run release verified |
| 5 | [Review findings and handover](05-handover.md) | Complete | Eight findings fixed with fixture regressions; request-time API scraping removed |

## Locked decisions

- Preserve current Prometheus metric names and label contracts.
- Converge on the custom-collector architecture; deprecate legacy mode only
  after parity, and retain it for one compatibility release.
- Deploy on Python 3.14 and locally test Python 3.12, 3.13, and 3.14.
- Keep and validate the generated TrueNAS 25.10.2 API Markdown snapshot.
- Publish under the MIT license.
- Never add GitHub Actions or paid hosted automation without explicit approval.
- Fixture and integration validation is mandatory; live read-only validation is
  optional.

## Completion rule

A phase is complete only when every checkbox in its document is checked and the
listed local verification commands pass. Partial work remains marked in
progress; roadmap documentation must not claim completion early.

Current branch coverage is 90.09%, enforced by `./scripts/validate.sh` with a
`--cov-fail-under=85` gate. Configuration is at 100%, transport at 95%, metric
declarations at 99%, collection parsing at 96%, and HTTP serving at 100%.

## Completion state

All five modernization phases are complete. The midway findings in
[05-handover.md](05-handover.md) and the convergence queue in
[02-architecture.md](02-architecture.md) are retained as historical design and
review evidence. Future changes remain subject to `./scripts/validate.sh`, the
generated metric-contract check, the read-only API policy, and the prohibition
on hosted CI.

The 2026-07-12 API/exporter parity implementation is complete in the working
tree, but its current Docker image and Python 3.13/3.14 matrix verification is
not complete in this host session because user `aeva` cannot access the
root-owned `docker` socket. This host-level verification blocker is recorded
below; it is not treated as a code or test pass.

## Verification evidence

- 2026-07-13 TrueNAS 25.10.2/26.0.0 compatibility planning: added the
  repository-specific implementation package under
  `docs/truenas-25-10-2-and-26-0-0-compatibility/`, including the corrected
  API diff, profile/safety design, collector and event plan, fixture/release
  plan, and dependency-ordered coding-agent task board. No production code,
  metric contracts, credentials, live responses, or hosted automation were
  changed. Focused API/runtime/event/transport tests passed (56 tests), and
  the existing generated metric, dashboard, API-manifest, exporter-parity,
  and dashboard-validation checks passed. Full `./scripts/validate.sh` and
  target-aware v26 checks remain implementation-stage gates.

- 2026-07-13 realtime metrics fix: implemented sibling `cpuN` usage and
  temperature parsing, documented user/idle CPU fallbacks, and preserved the
  existing `disls`/`disks`, aggregate-disk, interface, and legacy pool-I/O
  compatibility paths. Added a synthetic 25.10-shaped fixture and regenerated
  both dashboards so CPU usage is shown by total and core. The focused event,
  parity, and documented-shape suite passed 44 tests. Realtime pool capacity
  remains intentionally unexported because no compatible metric owner exists;
  ZFS hit-ratio semantics remain deferred with the dashboard counter-derived
  workaround. The required local validation passed, including the Docker image
  build and version smoke; no live smoke was run because no read-only API key
  was provided.

- 2026-07-12 exhaustive API parity: 1,012 files checked against manifest
  aggregate `377d24c74fa0836d43505f6c4db1f9ca12c105219abfeda34b6ac7d63c3f2cda`;
  767 method rows, 63 event rows, 114 method namespaces, and 405 field/metric
  mappings generated. The partitions are 398 documented reads, 325 mutations,
  44 unsafe/session workflows, 60 sensitive full responses, 43 additional
  generic-response exclusions, 3 allowed/60 prohibited events, 326 active
  dedicated metrics, 7 deprecated compatibility metrics, and 52 unavailable
  compatibility declarations.
- Current unrestricted deterministic gate: 150 tests passed on Python 3.12.3
  with 90.09% branch coverage; Ruff and mypy passed. Metric contract, API-doc
  manifest, exhaustive parity, dashboard generation, and dashboard validation
  checks passed. The dashboard has 313 panels and 287 unique contract metric
  references, with zero unavailable or deprecated references.
- `./scripts/validate.sh` passed compile, lint, type, tests/coverage, all
  generated-asset checks, dashboard validation, and both Compose configuration
  checks, then stopped before image build with `permission denied while trying
  to connect to the docker API at unix:///var/run/docker.sock`.
- `./scripts/test_python_matrix.sh` stopped on its first Python 3.12 Docker build
  with the same socket permission error; the current changes have therefore not
  been verified on Python 3.13 or 3.14 in this session. Socket permissions are
  `srw-rw---- root docker`, while user `aeva` is not in group `docker` and
  non-interactive sudo is unavailable.
- Live smoke was not run because no read-only TrueNAS API key was provided.
- 2026-07-13 live observation (TrueNAS SCALE 25.10.3, read-only `/metrics`
  scrapes only): realtime-sourced gauges (`truenas_cpu_*_percent`, several
  `truenas_memory_*_bytes`, SMB/NFS activity, ZFS ARC rate gauges)
  intermittently report `NaN` between event updates, which fragments Grafana
  time series; `truenas_zfs_*_hit_ratio` gauges read 0.0/NaN even while the
  matching `*_hits_per_second` gauges show load; and
  `truenas_snapshot_oldest_timestamp_seconds` was NaN with 150 snapshots
  present. Dashboards work around all three (see README metric behavior
  notes). A future reliability candidate is suppressing or last-known-value
  holding NaN samples at the exporter, subject to the locked metric-contract
  rules.

- 2026-07-12 review fixes: 78 passed, 1 skipped; branch coverage 49.26%; Ruff,
  mypy, metric-contract, dashboard, and fixture checks passed through the local
  validation gate.
- `python3 scripts/generate_metric_contract.py --check` passed after the
  collector-default flip with no metric or label contract change.
- 2026-07-12 Phase 2 convergence: 83 tests pass in the unrestricted gate;
  branch coverage is 77.87% and the enforced floor is 77%. Ruff, mypy,
  generated assets, Compose validation, the Python 3.14 production image, and
  the container version smoke test pass.
- The Docker test matrix passes on Python 3.12, 3.13, and 3.14 with 100 tests on
  each interpreter. Live smoke remains optional and was not run without a key.
- 2026-07-12 Phase 2 completion: 100 tests pass in the unrestricted deterministic
  local suite; branch coverage is 85.07% and the enforced floor is 85%. Lifecycle,
  event-stream recovery, discovery safety, generic extraction, HTTP readiness,
  and collector/legacy startup branches have fixture-based regressions. Live
  smoke remains optional and was not run without a read-only key.
