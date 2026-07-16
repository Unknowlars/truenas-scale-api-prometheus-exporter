#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

for version in 3.12 3.13 3.14; do
  echo "==> Testing Python ${version}"
  docker build \
    --file Dockerfile.test \
    --build-arg "PYTHON_VERSION=${version}" \
    --tag "truenas-exporter-test:py${version}" \
    .
done

