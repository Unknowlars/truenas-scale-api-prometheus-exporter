# Modernization Roadmap

This roadmap tracks the production-reliability, architecture, public-release,
and validation work for the TrueNAS Prometheus exporter. TrueNAS SCALE 25.10.2
is the compatibility baseline. Hosted CI is intentionally prohibited; all
evidence is produced locally.

## Status

| Phase | Document | Status | Evidence |
| --- | --- | --- | --- |
| 1 | [Reliability](01-reliability.md) | Complete | 72 tests pass in the unrestricted local gate; zero, expiry, deadline, config, readiness, and transport regressions covered |
| 2 | [Architecture](02-architecture.md) | In progress | Package boundaries and full metric parity are implemented; global metric mutation removal remains |
| 3 | [Public release](03-public-release.md) | Complete | README, policies, MIT license, Compose, dashboard, and generated API docs validated |
| 4 | [Validation and release](04-validation-release.md) | Complete | Local gate, Python 3.12-3.14 matrix, image build, dependency audit, and dry-run release verified |
| 5 | [Review findings and handover](05-handover.md) | In progress | Midway review (2026-07-12): 6 confirmed + 2 plausible findings open; fix before finishing phase 2 |

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

Current branch coverage is 48%. Configuration is at 100%, transport at 97%,
and metric declarations at 100%. Raising total branch coverage to 85% remains
part of the architecture migration because the legacy coordinator still holds
most untested domain branches.

## Handover

Next agent: start at [05-handover.md](05-handover.md) — fix the checked-off
review findings first, then follow the "Remaining work queue" in
[02-architecture.md](02-architecture.md). All work is verified through
`./scripts/validate.sh` and the metric-contract check; the working tree is
uncommitted at handover, so create a checkpoint commit before changing code.
