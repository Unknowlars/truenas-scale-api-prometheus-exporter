#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ -d .github/workflows ]] && find .github/workflows -type f -print -quit | grep -q .; then
  echo "hosted CI is prohibited: remove .github/workflows files" >&2
  exit 1
fi

python3 -m compileall -q truenas_exporter.py src tests scripts
python3 -m ruff check src scripts tests
python3 -m mypy src/truenas_exporter
python3 -m pytest -q -p no:cacheprovider \
  --cov=src/truenas_exporter \
  --cov-branch \
  --cov-report=term \
  --cov-fail-under=85
python3 scripts/generate_metric_contract.py --check
python3 scripts/generate_truenas_dashboard.py --check
python3 grafana-dashboard/build_mission_control.py --check
python3 scripts/validate_dashboard.py
python3 scripts/generate_api_docs_manifest.py --check
python3 scripts/generate_api_docs_manifest.py --target 26.0.0 --check
python3 scripts/generate_api_docs_manifest.py --target 27 --check
python3 scripts/generate_api_docs_manifest.py --target 27-official --check
python3 scripts/generate_api_exporter_parity.py --check
python3 scripts/generate_api_exporter_parity.py --target 26.0.0 --check
python3 scripts/generate_api_exporter_parity.py --compat-diff --check
python3 scripts/generate_truenas27_review.py --check
python3 scripts/public_release_audit.py
docker compose --env-file .env.example config --no-env-resolution --quiet
docker compose --file deploy/prometheus/docker-compose.prometheus.yml --env-file .env.example config --no-env-resolution --quiet
docker build --tag truenas-scale-api-prometheus-exporter:validate .
docker run --rm truenas-scale-api-prometheus-exporter:validate --version

if [[ "${RUN_PYTHON_MATRIX:-0}" == "1" ]]; then
  ./scripts/test_python_matrix.sh
fi
if [[ "${RUN_SECURITY_AUDIT:-0}" == "1" ]]; then
  python3 -m pip_audit \
    --cache-dir /tmp/truenas-exporter-pip-audit \
    --no-deps \
    --disable-pip \
    -r requirements.txt
fi

echo "validation_ok"
