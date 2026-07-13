# LGTM Stack Patterns for Grafana Dashboard Agents

This reference adapts useful guidance from Grafana's official Loki, Mimir,
Prometheus, Tempo, PromQL, Dashboarding, Grafana OSS, and Alloy skills.

Use it when a dashboard or troubleshooting request crosses logs, metrics,
traces, or telemetry pipelines.

---

## Cross-signal dashboard model

A production observability dashboard should connect:

- **Metrics** for health, rate, errors, duration, saturation, capacity, SLOs, and trends.
- **Logs** for recent examples and failure context.
- **Traces** for request-level causality and latency breakdown.
- **Profiles** when CPU/memory flame graphs are available.
- **Events/annotations** for deploys, incidents, and operational changes.

Prefer an overview that shows health first, then drilldowns that pivot across
metrics, logs, traces, and runbooks.

---

## Prometheus / PromQL

Rules:

- Use `$__rate_interval` in Grafana dashboards for `rate()` and `increase()`.
- Fixed range vectors should normally be at least 4x the scrape interval.
- Rate first, then aggregate.
- Use `rate()` for dashboards and alerts; use `irate()` only for spike-sensitive visual debugging.
- Preserve `le` for classic histogram `histogram_quantile()`.
- Verify native histogram support before using native histogram syntax.
- Use recording rules for expensive dashboard queries and repeated SLO calculations.
- Avoid high-cardinality grouping labels such as request ID, user ID, raw URL, trace ID, or pod UID.

Examples:

```promql
sum by (service) (
  rate(http_requests_total{service=~"$service"}[$__rate_interval])
)
```

```promql
histogram_quantile(
  0.95,
  sum by (le, service) (
    rate(http_request_duration_seconds_bucket{service=~"$service"}[$__rate_interval])
  )
)
```

---

## Mimir / Grafana Cloud Metrics

Use Mimir guidance when the backend is Grafana Mimir, Grafana Cloud Metrics, or a
multi-tenant Prometheus-compatible long-term storage backend.

Dashboard concerns:

- Tenant scoping.
- Active series and cardinality.
- Ingestion rate.
- Query latency and query fan-out.
- Query-frontend behavior.
- Ingester pressure.
- Store-gateway/object-store health.
- Compactor health.
- Ruler and Alertmanager health.
- Remote write status.

Rules:

- Preserve tenant headers and tenant identity in datasource/proxy/collector config.
- Do not create global variable queries that enumerate labels across all tenants.
- Prefer recording rules for expensive or frequently repeated dashboard queries.
- Use tenant-level dashboards when multi-tenancy is operationally important.
- Treat local filesystem Mimir examples as development/demo only.
- Keep secrets and endpoint credentials out of dashboards.

---

## Loki / LogQL

Good LogQL pipeline order:

```logql
{cluster=~"$cluster", namespace=~"$namespace", app=~"$app"}
|= "error"
| json
| status >= 500
```

Rules:

- Start with indexed labels.
- Then apply line filters.
- Then parse.
- Then filter extracted labels/fields.
- Use `line_format` only for display readability.
- Use `unwrap` only for numeric values.
- Use regex matchers for multi-value variables.
- Avoid turning request IDs, trace IDs, user IDs, raw URLs, or exception messages into labels.
- Keep raw log panels narrow and limited.
- Prefer log-derived metrics for overview trends.

Examples:

```logql
sum by (app) (
  rate({namespace=~"$namespace", app=~"$app"} |= "error" [$__rate_interval])
)
```

```logql
quantile_over_time(
  0.95,
  {app=~"$app"} | logfmt | unwrap duration | duration_seconds [$__interval]
) by (app)
```

Absence alert pattern:

```logql
absent_over_time({job="expected-batch-job"}[30m])
```

---

## Tempo / TraceQL

Use Tempo/TraceQL when the task involves traces, service graphs, metrics from
traces, exemplars, trace-to-logs, or trace-to-metrics.

Rules:

- Inspect actual span/resource attributes before generating TraceQL.
- Keep trace queries time-bounded.
- Use Traces Drilldown/Explore for open-ended investigations.
- Use service graphs and span metrics only when metrics-generator is configured.
- Treat TraceQL metrics as version/feature-sensitive and verify availability.
- Connect metrics → traces via exemplars or data links.
- Connect logs → traces when log lines contain trace IDs.
- Connect traces → logs/metrics/profiles through Tempo datasource settings.

Examples:

```traceql
{ status = error }
```

```traceql
{ resource.service.name = "frontend" && duration > 1s }
```

```traceql
{ kind = server } >> { status = error }
```

---

## Alloy / OpenTelemetry pipelines

Think in pipelines:

```text
receive/source/discover -> process/relabel/transform/batch -> export/write
```

Rules:

- Identify signal type: metrics, logs, traces, profiles.
- Identify each input component.
- Identify processing/relabeling/parsing.
- Identify each output.
- Preserve labels/resource attributes required for dashboard variables and correlation.
- Drop high-cardinality labels before ingestion when they are not useful.
- Keep secrets in environment variables or secret stores.
- Validate Alloy syntax and runtime health before assuming dashboards are wrong.
- Validate backend ingestion in Grafana Explore.

Minimal conceptual examples:

```alloy
prometheus.scrape "node" {
  targets    = [{"__address__" = "localhost:9100"}]
  forward_to = [prometheus.remote_write.metrics.receiver]
}
```

```alloy
loki.source.file "app" {
  targets    = [{"__path__" = "/var/log/app/*.log", "job" = "app"}]
  forward_to = [loki.process.app.receiver]
}
```

---

## Dashboarding additions from official Grafana skills

Use annotations for timeline context:

- Deploys.
- Incidents.
- Maintenance windows.
- Scaling events.
- Failovers.
- Configuration changes.

Use links intentionally:

- Dashboard links for workflow navigation.
- Panel/data links for scoped drilldowns.
- Runbook links for operational action.
- Trace/log links for cross-signal correlation.

Do not drop time range or variables when linking to drilldown dashboards.

---

## Validation additions

Before returning dashboard or pipeline work:

- Confirm which specialist mode was used.
- Confirm all variables used in queries exist.
- Confirm label matchers are compatible with multi-value variables.
- Confirm PromQL windows are compatible with scrape interval.
- Confirm Loki selectors are not broad/unbounded.
- Confirm Mimir tenant scope is respected where relevant.
- Confirm Tempo attributes are real, not guessed.
- Confirm Alloy examples separate config from dashboards and do not include secrets.
