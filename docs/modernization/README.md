# Modernization verification

## 2026-11-09: Build without a LICENSE file

- `docker build -t truenas-exporter-license-check:local .`: passed locally.
- `./scripts/validate.sh`: Ruff and mypy passed; pytest reported 398 passed and 2 failed because the local `docs/truenas-api/` documentation and manifest are absent. Validation stopped at pytest; later checks did not run.
