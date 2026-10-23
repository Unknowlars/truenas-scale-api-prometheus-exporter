# Typed telemetry expansion evidence — 2026-10-22

Implementation: 47 new families, 467 total. All 420 previous metric contracts
compared exactly against the pre-change local contract and remain unchanged.
Existing working-tree changes and the untracked gap analysis are preserved.

## Official/documented

Both pinned 27 API corpora were compared. The server's release tag resolves
to middleware commit `d83c3bf89aa4226c8fd1ef25dd273bdf447eb777`. Release source
establishes UPS units/row layout and upstream zero filling, projected backup
job fields, read-only SED status extension and dataset property selection.
See `docs/telemetry-expansion.md` for exact primary-source references and bounds.

## Synthetic

Regressions cover collection through fake RPC responses into public snapshots:
valid zero/false, unknown and malformed values, source recovery/expiry, bounded
tier detail queries, per-version projections, private-field exclusions, UPS
freshness and transport failures. Testing reproduced and fixed default-zero
label allocation in the new nullable pool, disk and backup booleans.

An initial full gate found a stale pre-existing assertion for the dataset
projection list. It was extended with the new field and a measured-zero
assertion. The earlier full gate passed 352 tests before the final boolean
regressions; that intermediate result is superseded by the final gate.

## Bounded live source runtime

SCALE `27.0.0-RC.1`, profile `27.0`: 9.611-second poll, 162 read-only RPCs,
zero API failures, up=1, readiness true, 2,180 samples including 497 finite
samples from new families. All 556 checked source/metric comparisons matched.
Dataset tuning, logical accounting, scan details and tier configuration were
observed. SED capability/status was unknown and omitted. No cloud-backup tasks
or tier rewrite jobs were available. UPS graph presence is verified, but
electrical measurements are not. No raw responses or private labels retained.

## Packaged/full gate

The 356-test full gate passed at 91.80% coverage, including image build and
version smoke. The packaged cold-start observation then caught readiness 200
before the first snapshot became visible (up=0, initial metrics). Later
observations were healthy, but the first 70-second check correctly failed.
A deterministic concurrency regression reproduced the ordering defect. First
readiness now follows successful snapshot publication; the final gate and
packaged repeat below supersede that intermediate image.

Final `./scripts/validate.sh`: PASS (`validation_ok`), 357 tests, 91.80%
branch-enabled coverage, Ruff/mypy, all generated/API/dashboard/Compose checks,
release audit, exact 98-warning promtool baseline, image build and version smoke.
The 420 existing metric contracts remain identical in every field, with 47
additional families. No optional Python matrix or vulnerability scan was rerun.

Final image `30fb58e7872d46e1301d3068c43c6289309fda1715d9310fa0537d679378d345`
is running as `truenas-local-test-exporter-1`, tag `:local-test`.
Cold-start acceptance passed: 15 observations over 70.68 seconds, up=1 and
ready=200 throughout, 497 additional finite samples at every observation,
two polling snapshots and a final 2,350 samples. The first polling snapshot
preceded the first CPU event. Event acceptance correctly permits that initial
unknown state and requires finite CPU and event age <=15 seconds thereafter;
maximum observed age was 7.889 seconds. A deterministic regression separately
covers publication before readiness. The final Windows-side LAN metrics
request returned HTTP 200; a separate LAN scraper remains unverified.

The prior running image is retained under
`truenas-scale-api-prometheus-exporter:before-telemetry-expansion` for rollback.
No remote publication, NAS configuration change, push or commit is in scope.

No unresolved local validation failure remains. Real backup/tier execution,
electrical UPS accuracy (upstream reporting can zero-fill gaps), all SED states,
real older appliances, least-privilege authentication, TLS verification, external
Prometheus/Grafana acceptance and longer soak remain unverified. Key rotation
is still owner-managed; recreate the container after replacing the mounted key.

## Files changed for this expansion

- Runtime: `src/truenas_exporter/runtime.py`, `metrics.py`, `compat_profiles.py`.
- Tests: `tests/test_telemetry_expansion.py`; additive projection/zero assertions
  in the already modified `tests/test_phase1_metrics.py`.
- Ownership generators: `scripts/generate_api_exporter_parity.py`,
  `scripts/generate_truenas27_review.py`.
- Generated: `docs/metrics-contract.json`, `docs/api-exporter-parity.json`,
  `docs/api-exporter-parity.md`, `docs/reviews/truenas27-inventory.json`,
  `docs/reviews/truenas27-metric-coverage.md`,
  `docs/reviews/truenas27-api-compatibility.md`.
- Documentation: `README.md`, `docs/telemetry-expansion.md`,
  `docs/modernization/README.md`; local records/scripts in this directory.

Existing Dockerfile/Compose/release/config/transport changes, remediation tests,
the original live-validation scratch work and the untracked gap analysis were
present before this expansion and are preserved. Generated dashboard outputs
were checked/regenerated and did not change. No hosted automation was added.
