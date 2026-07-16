# Official Grafana Skills Review

This file records the third-pass review against Grafana's official `grafana/skills`
repository.

Reviewed official skills:

- `grafana-lgtm/loki`
- `grafana-lgtm/mimir`
- `grafana-lgtm/prometheus`
- `grafana-lgtm/tempo`
- `grafana-core/promql`
- `grafana-core/grafana-oss`
- `grafana-core/dashboarding`
- `grafana-core/alloy`

## What was adopted

| Official skill | Adopted into this skill |
|---|---|
| Loki | Label-first LogQL guidance, line filters before parsers, parsers (`json`, `logfmt`, `pattern`, `regexp`, `unpack`), `unwrap`, absence queries, and Logs Drilldown positioning. |
| Mimir | Added a new Mimir / Grafana Cloud Metrics section. Focus: multi-tenancy, remote_write, object storage, ruler/Alertmanager, query-frontend, store-gateway, compactor, limits, query fan-out, and active-series/cardinality awareness. |
| Prometheus | Strengthened Prometheus datasource guidance around metrics exploration, recording rules, alerting, remote_write, and Grafana Cloud Metrics/Mimir backend thinking. |
| Tempo | Expanded TraceQL, TraceQL metrics caution, metrics-generator, span metrics, service graphs, exemplars, trace-to-logs, and trace-to-metrics guidance. |
| PromQL | Added fixed-window guidance: `rate()`/`increase()` need range vectors, range normally >=4x scrape interval; rate before aggregation; classic vs native histogram cautions; recording rules; SLO/error-budget patterns; cardinality checks. |
| Grafana OSS | Reinforced provisioning, datasource config, service accounts/RBAC awareness, annotations, API/UID safety, and plugin/datasource portability. |
| Dashboarding | Added stronger annotation/link guidance, panel type selection, transformation pipeline order, variable routing, and Grafana Scenes note for plugin/app dashboards. |
| Alloy | Added explicit telemetry pipeline mental model: receive/source/discover -> process/relabel/transform/batch -> export/write; added component-reference, secret-handling, validation, and high-cardinality label handling rules. |

## What was intentionally not copied blindly

Some official skill examples are good quick references, but not always production-safe as direct dashboard-generation defaults.

Examples intentionally adjusted:

- Fixed `schemaVersion` examples are not treated as universal. This skill preserves the source dashboard version or uses the target Grafana export.
- Classic `label_values(...)` examples are marked as compatibility/legacy style when Grafana's typed Prometheus variable query model is available.
- Minimal demo configurations for Mimir, Tempo, Loki, and Alloy are treated as examples only, not production defaults.
- Raw endpoint, credential, and object-storage examples are not embedded into dashboard JSON.
- Query examples are adapted to dashboard-safe `$__rate_interval`, scoped variables, tenant boundaries, and high-cardinality checks.

## New capability added because our skill did not cover it enough

The biggest missing official-skill topic was **Mimir / Grafana Cloud Metrics** as its own operational domain. The main `SKILL.md` now includes a dedicated Mimir section and the `lgtm-stack-patterns.md` reference includes Mimir-specific dashboard and troubleshooting guidance.

## Final design decision

This skill remains a combined production dashboard skill, not a full replacement for every specialist skill. The main behavior should be:

1. Detect the task shape.
2. Route to the relevant specialist mode inside this skill.
3. Apply dashboard safety, production UX, datasource correctness, and validation.
4. Avoid copying simplified examples without adapting them to the user's Grafana version and environment.
