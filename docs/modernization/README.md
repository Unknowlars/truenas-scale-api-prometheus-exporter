# Modernization Roadmap

This roadmap tracks the production-reliability, architecture, public-release,
and validation work for the TrueNAS Prometheus exporter. TrueNAS SCALE 25.10.2
is the compatibility baseline. Hosted CI is intentionally prohibited; all
evidence is produced locally.

## Status

| Phase | Document | Status | Evidence |
| --- | --- | --- | --- |
| 1 | [Reliability](01-reliability.md) | Complete | 100 tests pass in the unrestricted local gate; zero, expiry, deadline, config, readiness, and transport regressions covered |
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

Current branch coverage is 85.07%, enforced by `./scripts/validate.sh` with a
`--cov-fail-under=85` gate. Configuration is at 100%, transport at 95%, metric
declarations at 99%, collection parsing at 99%, and HTTP serving at 100%.

## Completion state

All five modernization phases are complete. The midway findings in
[05-handover.md](05-handover.md) and the convergence queue in
[02-architecture.md](02-architecture.md) are retained as historical design and
review evidence. Future changes remain subject to `./scripts/validate.sh`, the
generated metric-contract check, the read-only API policy, and the prohibition
on hosted CI.

## Verification evidence

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
