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

Current branch coverage is 90.44%, enforced by `./scripts/validate.sh` with a
`--cov-fail-under=85` gate. Configuration is at 100%, transport at 95%, metric
declarations at 99%, collection parsing at 96%, and HTTP serving at 100%.

## Completion state

All five modernization phases are complete. The midway findings in
[05-handover.md](05-handover.md) and the convergence queue in
[02-architecture.md](02-architecture.md) are retained as historical design and
review evidence. Future changes remain subject to `./scripts/validate.sh`, the
generated metric-contract check, the read-only API policy, and the prohibition
on hosted CI.

The 2026-07-15 public-release hardening pass restored the local release gate,
added a tracked-file public-release audit, and completed Docker-backed
validation on this host.

## Verification evidence

- 2026-07-15 startup configuration fix: removed the Compose-level
  `EVENT_SUBSCRIPTIONS` injection so sample deployments do not force the newest
  event list into stale or externally supplied images. `.env.example` now leaves
  `EVENT_SUBSCRIPTIONS` unset by default and documents version-specific override
  examples. Regression coverage in `tests/test_tooling.py` verifies Compose no
  longer forces the optional runtime default. Focused checks passed:
  `python3 -m pytest -q tests/test_tooling.py tests/test_api_catalog.py tests/test_phase2_events.py tests/test_removed_source_suppression.py`
  (`40 passed`); `docker compose --env-file .env.example config --no-env-resolution --quiet`
  passed; explicit source config validation accepted
  `reporting.realtime,app.stats,virt.instance.metrics,container.metrics`; and
  `python3 scripts/public_release_audit.py` returned `public_release_audit_ok`.
  Required full validation passed: `./scripts/validate.sh` completed ruff,
  mypy, `186 passed`, 90.44% coverage, dashboard validation
  (`dashboard_ok panels=318 metric_references=287`), generated checks,
  `public_release_audit_ok`, Compose validation, Docker image build, container
  version smoke `5.2.0`, and `validation_ok`. Optional live smoke was not run
  because no read-only live TrueNAS target/key was provided.

- 2026-07-15 public-release hardening: scrubbed realistic `auth_token=` example
  values from the generated 25.10.2 and v26 API Markdown and updated
  `scripts/convert_truenas_api_docs_to_markdown.py` so regenerated examples use
  placeholders. Added `scripts/public_release_audit.py` and wired it into
  `./scripts/validate.sh`; the audit fails on tracked `.env` files, hosted
  workflow files, cache/build artifacts, old scratch files, private keys, common
  cloud/service token formats, and realistic URL token parameters. Profile-aware
  event defaults are now documented and validated as `reporting.realtime`,
  `app.stats`, `virt.instance.metrics` for 25.10 and `reporting.realtime`,
  `app.stats`, `container.metrics` for 26.0/unknown; `container.metrics` uses
  the same interval subscription formatting as the v25 instance event. The
  v25/v26 parity generator now treats the v25 event docs and reviewed v26 event
  additions as separate target surfaces. `nvmet.global.sessions` remains absent
  from the pinned v26 corpus but is documented as a bounded count source kept
  enabled under v26/unknown because live 26.0.0-BETA.2 still serves it.
  Focused compatibility tests passed:
  `python3 -m pytest -q tests/test_api_catalog.py tests/test_phase2_events.py tests/test_removed_source_suppression.py tests/test_runtime_api_parity.py`
  (`67 passed`). Generated and release checks passed:
  `python3 scripts/generate_api_docs_manifest.py --check`;
  `python3 scripts/generate_api_exporter_parity.py --check`;
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`;
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`;
  `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`;
  `python3 scripts/generate_metric_contract.py --check`; and
  `python3 scripts/public_release_audit.py` (`public_release_audit_ok`).
  Required full validation passed: `./scripts/validate.sh` completed ruff,
  mypy, `185 passed`, 90.44% coverage, dashboard validation
  (`dashboard_ok panels=318 metric_references=287`), generated checks,
  `public_release_audit_ok`, Compose validation, Docker image build, container
  version smoke `5.2.0`, and `validation_ok`. Python matrix validation passed:
  `./scripts/test_python_matrix.sh` built and tested Python 3.12, 3.13, and
  3.14 images with `185 passed` in each. Optional live smoke was skipped because
  no read-only live TrueNAS target/key was provided. No GitHub Actions, hosted
  CI/CD automation, credentials, live API response captures, metric names,
  metric types, help text, or label sets were added or changed.

- 2026-07-14 Mission Control dashboard review: added
  `docs/mission-control-dashboard-review.md` after reviewing the 27 rendered
  screenshots in `grafana-dashboard/screenshots/` and the generated
  `dashboard.grafana.app/v2beta1` resource at
  `grafana-dashboard/truenas-mission-control.json`. Structural checks found
  312 v2 panel elements, 312 layout references, no orphan or missing
  references, no duplicate panel IDs, and no 24-column grid overflow.
  `python3 scripts/validate_dashboard.py grafana-dashboard/truenas-mission-control.json`
  passed (`dashboard_ok panels=313 metric_references=282`). The required
  `./scripts/validate.sh` gate was attempted and passed ruff/mypy, the full
  Python test suite (`176 passed`, 90.47% coverage), and dashboard validation,
  then failed in the API parity generator with `ValueError: runtime event
  catalog differs from documented event leaves`. The failure is recorded as a
  host/worktree blocker for this review rather than a dashboard-report failure;
  pre-existing runtime/event-catalog changes were present before the report
  edit and were not reverted.

- 2026-07-14 Mission Control independent second pass: updated the report with
  screenshot-backed findings for inverted update/app/job mappings, misleading
  API success and lifetime-error panels, additional no-data and alias failures,
  and disk/pool/temperature/snapshot values that require exporter data-quality
  investigation. Reconfirmed 312 elements, 312 unique layout references, 12
  tabs, 11 variables, no missing/orphan references, duplicate IDs, or grid
  overflow, and all 406 Prometheus panel queries using
  `instance=~"$instance"`. JSON parsing, dashboard validation
  (`dashboard_ok panels=313 metric_references=282`), and `git diff --check`
  passed. The required `./scripts/validate.sh` currently passes ruff, mypy, 185
  tests, and 90.44% coverage, then fails with `Metric contract is out of date:
  regenerate metrics-contract.json`. This is recorded as a failed full gate;
  unrelated runtime, test, and screenshot changes were not reverted.

- 2026-07-13 live-review VM memory unit fix: a read-only scrape of a live
  TrueNAS SCALE 25.10.3 system (the operator's running exporter) showed
  `truenas_vm_available_memory_bytes` reporting ~1.83e16 (16.2 PiB). Direct
  read-only calls confirmed `vm.get_available_memory` returns raw bytes
  (17,388,047,459 = 16.19 GiB on a 31.3 GiB host), so the pinned 25.10.2 doc's
  "megabytes" claim is wrong and the `25.10` profile's `1024**2` multiplier
  inflated the metric. Fixed the `25.10` profile to treat both VM memory methods
  as bytes (matching `26.0`); with the fix the same live value normalizes to
  16.19 GiB. Metric names/types/help/labels are unchanged
  (`python3 scripts/generate_metric_contract.py --check` passed). Focused tests
  passed:
  `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tests/test_api_catalog.py tests/test_documented_api_shapes.py tests/test_runtime_api_parity.py`
  (54 passed); full suite and `./scripts/validate.sh` re-run recorded below.
  A sanitized pre-upgrade metric baseline was captured to
  `docs/truenas-25-10-2-and-26-0-0-compatibility/baseline-live-25.10.3.{md,json}`
  (no credentials, hostnames, IDs, serials, IPs, or raw responses). No live
  responses were saved; no dashboards, release behavior, hosted automation, or
  credentials changed.

- 2026-07-13 COMPAT-08 full validation and release gate: focused
  compatibility tests passed:
  `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tests/test_api_catalog.py tests/test_documented_api_shapes.py tests/test_runtime_api_parity.py tests/test_phase2_events.py tests/test_transport.py`
  (`68 passed`). Full test suite passed:
  `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q` (`174 passed`,
  `2 skipped`; skipped tests are optional cache/coverage checks). Required
  generated and dashboard checks passed:
  `python3 scripts/generate_metric_contract.py --check`;
  `python3 scripts/generate_truenas_dashboard.py --check`;
  `python3 scripts/validate_dashboard.py` (`dashboard_ok panels=313
  metric_references=282`);
  `python3 scripts/generate_api_docs_manifest.py --check`;
  `python3 scripts/generate_api_exporter_parity.py --check`;
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`;
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`;
  and `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`.
  `git diff --check` passed. `./scripts/validate.sh` passed (`176 passed`,
  90.47% coverage, dashboard validation passed, Docker image build and version
  smoke `5.2.0` passed, `validation_ok`). `./scripts/release.sh` was run
  without `--publish` and printed the dry-run multi-arch `docker buildx build`
  command only. `./scripts/test_python_matrix.sh` initially exposed that the
  validation container omitted `docs/` and `grafana-dashboard/`; after adding
  those test inputs to `Dockerfile.test`, the matrix passed on Python 3.12,
  3.13, and 3.14 (`176 passed` in each image build). Optional live smoke was
  skipped because no read-only live TrueNAS credentials or target were provided.
  No runtime code, metric names/types/help text/labels, dashboards, live API
  calls, credentials, hosted automation, or publish operation changed.

- 2026-07-13 COMPAT-07 operator documentation and handoff: README,
  `.env.example`, changelog, and the compatibility index now document automatic
  profile selection from `system.version_short`, supported `25.10`, `26.0`,
  and fail-closed `unknown` behavior, v26/unknown suppression for
  `virt.instance.query`, `virt.volume.query`, `nvmet.global.sessions`,
  `reporting.graphs`, `reporting.netdata_graphs`, and
  `virt.instance.metrics`, unavailable metric absent/NaN behavior without
  fabricated zeros, profile-aware event defaults, subscription-id validation
  and unsubscribe cleanup, `app.image.query` eligibility, and the continued
  blocks for `pool.is_upgraded` and `pool.ddt_prefetch`. Required checks
  passed: `python3 scripts/generate_metric_contract.py --check`;
  `python3 scripts/generate_api_docs_manifest.py --check`;
  `python3 scripts/generate_api_exporter_parity.py --check`;
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`;
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`;
  `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`;
  `git diff --check`; and `./scripts/validate.sh` (`176 passed`, 90.47%
  coverage, dashboard validation passed, Docker image build and version smoke
  `5.2.0` passed). No runtime code, metric names/types/help text/labels,
  dashboards, release behavior, live API calls, credentials, or hosted
  automation changed.

- 2026-07-13 COMPAT-06 event lifecycle hardening: event subscriptions now
  require a non-empty string subscription id from `core.subscribe`; invalid or
  missing ids are treated as subscription failures and are not tracked.
  Successful subscription ids are tracked by event and `core.unsubscribe` is
  called for each tracked id during clean event-loop shutdown and reconnect
  cleanup. Cleanup marks the event stream down, clears cached dedicated and
  generic event series, removes freshness state, and preserves existing
  reconnect backoff and diagnostics. Focused tests prove v25 keeps and
  unsubscribes `virt.instance.metrics`, v26/unknown still do not subscribe to
  removed `virt.instance.metrics`, invalid subscription ids are rejected
  without unsubscribe, and cached event series are cleared on reconnect
  cleanup. Focused checks passed:
  `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_lifecycle.py tests/test_removed_source_suppression.py -q`
  (35 passed). Metric contract check passed:
  `python3 scripts/generate_metric_contract.py --check`. Generated checks
  passed after regenerating legitimate parity artifacts with
  `python3 scripts/generate_api_exporter_parity.py`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0`, and
  `python3 scripts/generate_api_exporter_parity.py --compat-diff`:
  `python3 scripts/generate_api_docs_manifest.py --check`,
  `python3 scripts/generate_api_exporter_parity.py --check`,
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`,
  and `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`.
  `git diff --check` passed. `./scripts/validate.sh` passed (`176 passed`,
  90.47% coverage, dashboard validation passed, Docker image build and version
  smoke `5.2.0` passed). No metric names, types, help text, labels,
  dashboards, release behavior, live API calls, credentials, or hosted
  automation changed.

- 2026-07-13 COMPAT-05 removed-source suppression: removed v26/common-
  intersection methods are now diagnosed as intentional
  `profile_removed_method_suppressed` skips before transport invocation, and
  the removed `virt.instance.metrics` event is diagnosed as
  `profile_removed_event_suppressed` before subscription. Focused synthetic
  transport tests prove `virt.instance.query`, `virt.volume.query`,
  `nvmet.global.sessions`, `reporting.graphs`, and
  `reporting.netdata_graphs` are not sent by collector call sites, count
  queries, `EXTRA_METHODS`, generic discovery, dynamic discovery, or reporting
  discovery under `26.0` and `unknown`; they also prove
  `virt.instance.metrics` is not subscribed under those profiles. The same
  tests prove v25 still transports the removed-in-v26 methods/events where
  allowed, and `app.image.query` remains callable for reviewed count use.
  Stale metric handling remains the existing reset/NaN/absent behavior; no
  zeros or replacement v26 metrics were fabricated. Focused checks passed:
  `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py tests/test_removed_source_suppression.py -q`
  (51 passed). Metric contract check passed:
  `python3 scripts/generate_metric_contract.py --check`. Generated checks
  passed after regenerating the legitimate parity artifact with
  `python3 scripts/generate_api_exporter_parity.py`: `python3 scripts/generate_api_docs_manifest.py --check`,
  `python3 scripts/generate_api_exporter_parity.py --check`,
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`,
  and `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`.
  `git diff --check` passed. `./scripts/validate.sh` passed (`173 passed`,
  90.50% coverage, dashboard validation passed, Docker image build and version
  smoke `5.2.0` passed). No metric names, types, help text, labels,
  dashboards, release behavior, live API calls, credentials, or hosted
  automation changed.

- 2026-07-13 COMPAT-04 collector normalization and units: wired VM memory
  conversion through profile-owned unit metadata so 25.10 values documented as
  MiB are converted to bytes and 26.0/unknown profile values documented as
  bytes are not inflated. Added bounded response-field normalization for
  dataset, pool, and application collector shapes, including documented
  `value`/`parsed`/`rawvalue` wrappers and `properties` containers, while
  preserving existing labels and omitting malformed/null data. Existing
  realtime additive parsing for `disls`/`disks` and `cpuN` shapes was preserved.
  Added sanitized v26 VM fixtures under `tests/fixtures/api_26_0_0/` and
  focused tests proving v25/v26/unknown VM output magnitudes, malformed VM
  omission, and bounded dataset/app normalizers. Focused checks passed:
  `PYTHONPATH=. pytest tests/test_runtime_api_parity.py -q` (35 passed) and
  `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py tests/test_documented_api_shapes.py -q`
  (54 passed). Metric contract check passed:
  `python3 scripts/generate_metric_contract.py --check`. Required generated
  checks passed: `python3 scripts/generate_api_docs_manifest.py --check`,
  `python3 scripts/generate_api_exporter_parity.py --check`,
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`,
  and `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`.
  `git diff --check` passed. `./scripts/validate.sh` passed (`163 passed`,
  90.52% coverage, dashboard validation passed, Docker image build and version
  smoke `5.2.0` passed). No metric names, types, help text, labels,
  dashboards, release behavior, live API calls, credentials, or hosted
  automation changed.

- 2026-07-13 COMPAT-03 runtime version detection: authenticated bootstrap now
  calls `system.version_short` once per scrape/event WebSocket connection before
  collectors, generic discovery, reporting discovery, count queries, or event
  subscriptions run. Version strings beginning with `25.10.` select the 25.10
  profile, strings beginning with `26.0.` select the 26.0 profile, and unknown,
  malformed, or failed detection falls back to the unknown/common-intersection
  profile. Detection failure remains fail-closed: the unknown profile excludes
  `virt.instance.query`, `virt.volume.query`, `virt.instance.metrics`,
  `nvmet.global.sessions`, `reporting.graphs`, and
  `reporting.netdata_graphs`; focused tests also assert removed methods/events
  cannot reach the fake client and version-detection logs do not include a
  synthetic secret. Focused checks passed:
  `PYTHONPATH=. pytest tests/test_api_catalog.py tests/test_runtime_api_parity.py tests/test_runtime_lifecycle.py -q`
  (55 passed) and
  `PYTHONPATH=. pytest tests/test_phase1_metrics.py tests/test_phase3_collector_mode.py -q`
  (42 passed). Required generated checks passed:
  `python3 scripts/generate_api_docs_manifest.py --check`,
  `python3 scripts/generate_api_exporter_parity.py --check`,
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`,
  and `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`.
  `git diff --check` passed. `./scripts/validate.sh` passed (`161 passed`,
  90.46% coverage, dashboard validation passed, Docker image build and version
  smoke `5.2.0` passed). No metric names, types, help text, labels,
  dashboards, fixtures, release behavior, live API calls, credentials, or
  hosted automation changed.

- 2026-07-13 COMPAT-02 compatibility profiles and pre-call safety gates: added
  profile-owned 25.10, 26.0, and unknown/common-intersection method/event
  allowlists, v26 removed-source declarations, query-limit policy data, and VM
  unit-conversion metadata in `src/truenas_exporter/compat_profiles.py`.
  Runtime calls, count queries, generic discovery, `EXTRA_METHODS`, reporting
  discovery, and configured event subscriptions now fail closed against the
  selected profile while default runtime behavior remains on the 25.10.2
  profile until COMPAT-03 adds version detection. The v26 and unknown profiles
  exclude `virt.instance.query`, `virt.volume.query`, `virt.instance.metrics`,
  `nvmet.global.sessions`, `reporting.graphs`, and
  `reporting.netdata_graphs`; `app.image.query` remains eligible for owned
  count/select use; `pool.is_upgraded` and `pool.ddt_prefetch` remain blocked.
  Focused profile tests passed (`PYTHONPATH=. pytest tests/test_api_catalog.py
  tests/test_runtime_api_parity.py -q`: 33 passed). Required local checks
  passed: `python3 scripts/generate_api_docs_manifest.py --check`,
  `python3 scripts/generate_api_exporter_parity.py --check`,
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`,
  `git diff --check`, and `./scripts/validate.sh` (`155 passed`, 90.36%
  coverage, dashboard validation passed, Docker image build and version smoke
  passed). No metric names, types, help text, labels, dashboards, fixtures,
  release behavior, live API calls, credentials, or hosted automation changed.

- 2026-07-13 COMPAT-01B v26 parity and compatibility diff: added target-aware
  v26 parity generation to `scripts/generate_api_exporter_parity.py` without
  changing the default 25.10.2 parity artifacts. Generated
  `docs/api-exporter-parity-v26.{json,md}` and
  `docs/truenas-25-10-2-and-26-0-0-compatibility/api-compatibility-diff.{json,md}`.
  The v26 parity inventory records 805 methods, 80 events, and the v26 manifest
  aggregate `32acc76d9ec44593ae17a53571a29b5cbc33526741feff3b2062b645b9c88855`.
  The compatibility diff records 87 methods added in v26, 49 methods removed,
  22 events added, 5 events removed, and current exporter surfaces partitioned
  as 8 absent in v26, 97 schema-changed, and 133 unchanged by parsed signature
  (the unchanged count was 132 at COMPAT-01B generation time and became 133
  after the legitimate parity/diff artifact was regenerated during COMPAT-05/06;
  the checked-in `api-compatibility-diff.json` now records 133).
  Required checks for `app.image.query`, `pool.is_upgraded`,
  `pool.ddt_prefetch`, `nvmet.global.sessions`, `reporting.graphs`,
  `reporting.netdata_graphs`, `virt.instance.query`, `virt.volume.query`, and
  `virt.instance.metrics` are captured in the generated diff. The checks
  `python3 scripts/generate_api_exporter_parity.py --check`,
  `python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check`,
  `python3 scripts/generate_api_exporter_parity.py --compat-diff --check`,
  `git diff --check`, and `./scripts/validate.sh` passed. No runtime, metrics,
  dashboards, fixtures, manifests, release behavior, credentials, live API
  calls, or hosted automation were changed.

- 2026-07-13 COMPAT-01A v26 API documentation manifest: added target-aware
  manifest support while preserving the default 25.10.2 manifest behavior.
  Generated `docs/truenas-api-v26/MANIFEST.json` for target `26.0.0` with
  1,092 Markdown files, aggregate SHA-256
  `32acc76d9ec44593ae17a53571a29b5cbc33526741feff3b2062b645b9c88855`,
  per-file hashes, provenance noting that `truenas-v26.0.0-docs/` is not
  checked in, generator metadata, and generation/check commands. The legacy
  25.10.2 checks `python3 scripts/generate_api_docs_manifest.py --check` and
  `python3 scripts/generate_api_exporter_parity.py --check` passed unchanged;
  `python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check`,
  `git diff --check`, and `./scripts/validate.sh` also passed. No runtime,
  metrics, dashboards, fixtures, release behavior, credentials, live API calls,
  or hosted automation were changed.

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
