# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Added

- public release support files: `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, and GitHub Actions CI

### Changed

- refreshed `README.md` for public launch, including runtime, testing, and configuration guidance
- hardened container defaults with a non-root runtime user and `/healthz` Docker health check
- updated ignore rules so the local offline TrueNAS docs snapshot stays out of the published repository
