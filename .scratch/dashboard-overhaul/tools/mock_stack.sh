#!/usr/bin/env bash
# Usage: mock_stack.sh up [27|25.10]   -> 6h backfilled mock history + live mock scrape
#        mock_stack.sh empty           -> Prometheus with no data at all
#        mock_stack.sh down
# State lives under $MOCK_STATE (default: /tmp/truenas-dash-mock), never in the repo.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"; cd "$here"
state="${MOCK_STATE:-/tmp/truenas-dash-mock}"; mkdir -p "$state"
export RENDER_TOKEN="${RENDER_TOKEN:-$(cat "$state/token" 2>/dev/null || openssl rand -hex 16 | tee "$state/token")}"
export MOCK_TSDB="$state/tsdb"
dc() { docker compose -f compose.mock.yml "$@"; }
case "${1:-}" in
  down) dc down --remove-orphans; exit 0;;
  up)
    export MOCK_PROFILE="${2:-27}" MOCK_SCRAPE=mock
    dc down --remove-orphans >/dev/null 2>&1 || true
    rm -rf "$state/tsdb" "$state/om"; mkdir -p "$state/tsdb" "$state/om"; chmod 777 "$state/tsdb"
    python3 -I mock_exporter.py dump --profile "$MOCK_PROFILE" --hours "${HOURS:-6}" --step 30 --out "$state/om/backfill.om"
    docker run --rm --user 0 --entrypoint promtool -v "$state:/w" prom/prometheus:v3.5.0 \
      tsdb create-blocks-from openmetrics /w/om/backfill.om /w/tsdb >/dev/null
    dc up -d mock prometheus renderer grafana;;
  empty)
    export MOCK_PROFILE=27 MOCK_SCRAPE=none
    dc down --remove-orphans >/dev/null 2>&1 || true
    rm -rf "$state/tsdb"; mkdir -p "$state/tsdb"; chmod 777 "$state/tsdb"
    dc up -d prometheus renderer grafana;;
  *) echo "usage: $0 up [27|25.10] | empty | down" >&2; exit 2;;
esac
for i in $(seq 60); do curl -sf localhost:3000/api/health >/dev/null && curl -sf localhost:9090/-/ready >/dev/null && break; sleep 2; done
echo "stack ready ($1 ${MOCK_PROFILE:-})"
