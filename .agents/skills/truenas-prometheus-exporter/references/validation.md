# Tests, dashboards and release

Use TDD through converter CLI, JSON-RPC client, collection/snapshot, HTTP and
builders/validators. Fake external sockets and clocks; use representative
sanitized fixtures. Assert exposed behavior and forbidden/repeated calls where
those calls are the defect, not private implementation order.

The checkout launcher aliases the runtime. In tests obtain the actual runtime
through sys.modules[TrueNASExporter.__module__] and transport through
sys.modules[JsonRpcWsClient.__module__]. Importing transport relative to the
runtime alias can create a second module and exception class.

Cover zero/false/null/missing/malformed data, known units, source isolation,
connection loss, deadlines before connect/send, auth failures, subscription
recovery and TTL via TrueNASCollector.collect without privately republishing.
Repeat expiry while polling blocks; HTTP must stay independent of NAS RPCs.

Regenerate owned artifacts from sources:

```sh
python3 scripts/generate_metric_contract.py
python3 scripts/generate_truenas_dashboard.py
python3 grafana-dashboard/build_mission_control.py
python3 scripts/generate_api_exporter_parity.py
python3 scripts/generate_api_exporter_parity.py --target 26.0.0
python3 scripts/generate_api_exporter_parity.py --compat-diff
python3 scripts/generate_truenas27_review.py
./scripts/validate.sh
```

The classic generator owns queries; Mission Control reads its JSON. Preserve
both identities, datasource variables, units and missing-data semantics. Mission
Control is offline by default; optional --metric-names takes local names-only
JSON. Never personalize committed dashboards from production observations.
JSON/reference validation is separate from PromQL evaluation and browser
acceptance. Use local Prometheus/promtool for expression/exposition checks.

Record exact checks, tool versions, counts and limitations in the modernization
ledger; update27 reviews and migration notes. Live tests still need a verified
read-only key. Never commit raw responses, private labels or credentials.

Recheck actual history/tags/version.py before choosing a release. The27 candidate
is5.2.0rc1, not exporter version27. Keep dry-run release behavior and prereleases
off latest. Publication needs explicit authorization, clean worktree and exact
tag. Never introduce hosted workflows.
