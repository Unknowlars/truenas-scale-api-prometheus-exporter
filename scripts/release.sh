#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

publish=false
if [[ "${1:-}" == "--publish" ]]; then
  publish=true
elif [[ -n "${1:-}" ]]; then
  echo "usage: $0 [--publish]" >&2
  exit 2
fi

version="$(sed -n 's/^__version__ = "\([^"]*\)"/\1/p' src/truenas_exporter/version.py)"
image="ghcr.io/unknowlars/truenas-scale-api-prometheus-exporter"
current_tag="$(git describe --tags --exact-match 2>/dev/null || true)"

if [[ -z "$version" ]]; then
  echo "unable to read exporter version" >&2
  exit 1
fi

cmd=(docker buildx build
  --platform linux/amd64,linux/arm64
  --build-arg PYTHON_VERSION=3.14.8
  --tag "${image}:${version}"
  --sbom=true
  --provenance=mode=max)

# Prereleases never replace the stable channel.
if [[ "$version" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  cmd+=(--tag "${image}:latest")
fi

if [[ "$publish" == false ]]; then
  printf 'DRY RUN: '
  printf '%q ' "${cmd[@]}"
  printf '%q\n' .
  echo "Run ./scripts/validate.sh and tag v${version} before publishing."
  exit 0
fi

if [[ -n "$(git status --short)" ]]; then
  echo "refusing to publish from a dirty worktree" >&2
  exit 1
fi
if [[ "$current_tag" != "v${version}" ]]; then
  echo "refusing to publish: HEAD must have exact tag v${version}" >&2
  exit 1
fi

./scripts/validate.sh
"${cmd[@]}" --push .

