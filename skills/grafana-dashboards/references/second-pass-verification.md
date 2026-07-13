# Second-pass Verification Notes

Date: 2026-04-24

This file records the main documentation corrections made in the second pass.

## Verified against official Grafana docs

- Grafana 13 dynamic dashboards are generally available and on by default.
- Grafana 13 Git Sync for dashboards/folders is generally available.
- Grafana 13 renamed Ad hoc filters to Filters in the UI, while the dashboard schema still uses `AdhocVariable`.
- Grafana 13 deprecates the legacy `/api` path in favor of `/apis` and disables deprecated numeric datasource-ID APIs by default.
- Classic dashboard `gridPos.w` is still based on a 24-column grid.
- `schemaVersion` is a Grafana dashboard schema version and should not be hardcoded blindly.
- Prometheus variable classic query syntax such as `label_values(metric, label)` is documented as deprecated classic variable syntax.
- Grafana recommends `$__rate_interval` for Prometheus `rate()` and `increase()`.
- Multi-value variable interpolation is datasource-specific. A custom All value is not universally required.
- Elasticsearch standard queries in Grafana use Lucene syntax and uppercase boolean operators.
- Transformations run as a pipeline and the output of one transformation is the input to the next.
- Provisioned dashboard UI edits are not automatically written back to provisioning sources and can be overwritten by source-file updates.
- Alert labels identify/rout alerts; annotations provide responder context.
- Grafana supports No Data and Error state handling for Grafana-managed alert rules.
- Tempo trace-to-logs and trace-to-metrics require configured datasources and matching identifiers/attributes.

## Main corrections made

1. Removed hard requirement to use `schemaVersion: 42` and `pluginVersion: "12.4.0"`.
2. Reworded Grafana 13/v2 guidance to preserve the actual input/export shape rather than forcing a single `dashboard.grafana.app/v2` form.
3. Changed the “each panel must be in exactly one tab” rule into schema-aware layout validation.
4. Replaced blanket `allValue: ".*"` guidance with datasource/matcher-context-aware guidance.
5. Marked classic Prometheus `label_values(...)` syntax as compatibility/deprecated rather than preferred for all new dashboards.
6. Added Elasticsearch Lucene/KQL/ES|QL caveats.
7. Added Loki, Tempo, alerting, provisioning, Git Sync, Foundation SDK, and Observability-as-Code guidance.
8. Added stronger validation and output-reporting checklists.
