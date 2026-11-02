# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Fixed

- serve HTTP requests in separate threads so `/healthz` stays responsive while `/metrics` waits for the exporter lock during a long API poll; previously orchestrator liveness probes timed out and restarted the exporter
- cap concurrent `/metrics` requests (default 4, `MAX_CONCURRENT_METRICS_REQUESTS`) and answer further ones with `503`, so waiting scrapes cannot pile up threads

### Added

- public release support files: `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, and GitHub Actions CI

### Changed

- refreshed `README.md` for public launch, including runtime, testing, and configuration guidance
- hardened container defaults with a non-root runtime user and `/healthz` Docker health check
- updated ignore rules so the local offline TrueNAS docs snapshot stays out of the published repository
