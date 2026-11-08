# Dashboard review toolkit

Local only. Never commit keys, renders of private data, or `*.eval.json`.

```bash
cd .scratch/dashboard-overhaul/tools
./../../../scripts/validate.sh            # builds the :validate exporter image
export TRUENAS_WS_URL=wss://<nas>/api/current
export TRUENAS_API_KEY_FILE=/abs/path/outside/repo/key   # mode 600
export RENDER_TOKEN=$(openssl rand -hex 16)
docker compose up -d                       # Grafana http://localhost:3000 (anonymous admin)
# wait ~5 min for rate() history, then:
./render_tabs.sh ./shots                   # PNG per MC tab + classic
python3 -I eval_queries.py ../../../grafana-dashboard/*.json   # needs Prometheus :9090
docker compose down
```

No NAS? Omit the exporter (`docker compose up -d prometheus renderer grafana`
with dummy TRUENAS_* vars) and render the **no-data** state: every panel must
read neutral N/A, never green or red.

Notes:
- Mission Control is schema v2 and needs Grafana 13+; it is imported via the
  v2 API by `render_tabs.sh`. The classic dashboard is file-provisioned
  straight from `grafana-dashboard/` (provisioning also picks up MC's JSON
  harmlessly; the v2 import is authoritative).
- Select a tab in URLs with `dtab=<slug>`, e.g. `dtab=-pools-zfs`.
- `eval_queries.py` substitutes every `$var` with `.*` and `$__rate_interval`
  with `2m`; empties are written to `<dashboard>.eval.json` for classification.
- The renderer needs a shared non-default token (Grafana 13 refuses the default).

## Sanitized mock stack (no NAS, no key)

```bash
./mock_stack.sh up 27       # or: up 25.10 — synthetic exporter + 6 h backfilled history
./render_tabs.sh /path/out now-6h          # every MC tab + every classic row (expanded)
THEME=light TABS="0 1 3" CLASSIC=0 ./render_tabs.sh /path/out-light now-6h
./mock_stack.sh empty       # Prometheus with no targets -> no-data render
./mock_stack.sh down
```

- `mock_exporter.py` builds its metrics from `docs/metrics-contract.json`, using fictional names only. It reproduces D1/D2/D3/D10/D12/D13 on purpose. Profile `27` sends aggregate disk I/O and no CPU split or pool realtime I/O; profile `25.10` sends per-disk I/O and the CPU split.
- State lives in `/tmp/truenas-dash-mock` (outside the repo).
- `render_tabs.sh` imports both dashboards through the API on every run, so regenerated JSON is always what gets rendered. Grafana no longer file-provisions dashboards (`prov-api/` holds the datasource only).
- `render_tabs.sh` and `eval_queries.py` take `GRAFANA=` and `PROM=` to point at another stack, such as a live stack on other ports. `eval_queries.py` also substitutes `$__range` with `6h` and writes to `EVAL_DIR`.
