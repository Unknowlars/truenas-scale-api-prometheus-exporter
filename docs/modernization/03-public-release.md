# Phase 3: Public Release

## Tasks

- [x] Add MIT licensing, security policy, support policy, and version policy.
- [x] Correct every README and changelog path and remove hosted-CI claims.
- [x] Use Python 3.14 in a reproducible non-root container image.
- [x] Make the main Compose quick start build the checked-out source.
- [x] Provide a portable same-network Prometheus example without private IPs.
- [x] Make the dashboard generator deterministic and canonical.
- [x] Validate dashboard queries against the metric contract.
- [x] Add provenance and inventory validation for generated API Markdown.
- [x] Guard documentation cleanup against unsafe output paths.

## Acceptance

- Every documented path exists and every quick-start command is structurally valid.
- Regenerating the dashboard produces the committed canonical JSON.
- Compose uses local code with `docker compose up --build`.
