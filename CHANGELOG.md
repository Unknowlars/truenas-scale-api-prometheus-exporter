# Changelog

All notable changes to this project are documented here.

## Unreleased - 5.2.0

### Fixed

- preserve valid numeric zero and boolean false values when parsing alternative API fields
- expire stale event-derived telemetry instead of retaining disconnected values indefinitely
- expose API, collector, exporter, and event diagnostics from collector mode
- make `docker compose up --build` build the checked-out source
- replace private Prometheus example targets with a portable service-network configuration
- reconcile the dashboard generator and committed dashboard path

### Added

- strict configuration validation, total scrape budgets, custom CA files, and API-key files
- `/readyz` readiness endpoint and graceful signal-driven shutdown
- installable `src/` package, console command, and Python 3.14 container image
- MIT license, security and support policies, metric contract, API-doc manifest, and modernization roadmap
- local lint, type, coverage, generated-asset, Compose, image, Python-matrix, security-audit, live-smoke, and manual-release tooling

### Policy

- hosted CI is intentionally prohibited; validation and releases are local and explicit
- TrueNAS SCALE 25.10.2 remains the authoritative API compatibility target

