---
name: promql
license: Apache-2.0
description: >
  Write, validate, troubleshoot, and optimise PromQL queries for Prometheus,
  Grafana, Grafana Cloud Metrics, Mimir, and Prometheus-compatible datasources.
  Use when the user asks to query metrics, write PromQL expressions, calculate
  rates, aggregate across labels, build histogram quantiles, create recording
  rules, debug query performance, understand metric cardinality, build Grafana
  dashboard panels, or fix Prometheus/Grafana query errors. Triggers on phrases
  like "PromQL", "Prometheus query", "metric query", "calculate rate",
  "histogram_quantile", "recording rule", "metric cardinality", "sum by",
  "rate vs irate", "absent()", "query is slow", "Grafana Prometheus panel",
  "Prometheus variable", or "join metrics".
---

# PromQL Skill

This skill helps write correct, production-ready PromQL for Prometheus, Grafana,
Grafana Cloud Metrics, Mimir, and other Prometheus-compatible metric stores.

PromQL is a functional query language for time-series data. A query usually
returns one of:

- **Instant vector**: one value per label set at a point in time
- **Range vector**: a window of samples per label set, for example `metric[5m]`
- **Scalar**: a single number

---

## Core Rules

### 1. Rate before aggregation

Always calculate `rate()`, `irate()`, or `increase()` before aggregating counters.

```promql
# Correct
sum by (job) (
  rate(http_requests_total[5m])
)

# Wrong
rate(
  sum by (job) (http_requests_total)[5m]
)
```

Why: summing counters before `rate()` can hide counter resets and break monotonicity.

---

### 2. Use a safe range window

`rate()` and `increase()` require a range vector.

Use a range at least **4x the scrape interval**.

Examples:

| Scrape interval | Minimum practical range |
|---|---|
| 15s | `[1m]` |
| 30s | `[2m]` |
| 60s | `[5m]` |

For Grafana dashboards, prefer:

```promql
rate(http_requests_total[$__rate_interval])
```

---

### 3. Never join inside a range-vector function

Binary operations and vector matching work on instant vectors, not range vectors.

```promql
# Invalid
rate(builds_total * on(projectID) group_left(projectName) project_info[5m])

# Valid
rate(builds_total[5m])
* on(projectID) group_left(projectName)
  project_info
```

This rule also applies to:

- `increase()`
- `delta()`
- `irate()`
- `avg_over_time()`
- `max_over_time()`
- `min_over_time()`
- `quantile_over_time()`

---

### 4. Inspect metrics before building dashboards

Do not assume labels exist. Exporters often expose IDs on metric series and
human-readable names only on separate `*_info` metadata series.

Useful discovery commands:

```bash
# List all metric names, optionally filtered by prefix
curl -s "http://prometheus:9090/api/v1/label/__name__/values" | \
  python3 -c "import json,sys; [print(m) for m in json.load(sys.stdin)['data'] if 'myexporter' in m]"
```

```bash
# Show labels and example series for a metric
curl -s "http://prometheus:9090/api/v1/query?query=my_metric" | \
  python3 -c "
import json,sys
r = json.load(sys.stdin)['data']['result']
if r:
    print('Labels:', list(r[0]['metric'].keys()))
    print('Example:', json.dumps(r[0]['metric'], indent=2))
    print('Series count:', len(r))
else:
    print('NO DATA — metric does not exist or is empty')
"
```

```bash
# List all values for one label
curl -s "http://prometheus:9090/api/v1/label/job/values" | \
  python3 -c "import json,sys; [print(v) for v in json.load(sys.stdin)['data']]"
```

```bash
# Check whether a summary metric has quantile labels
curl -s "http://prometheus:9090/api/v1/query?query=my_summary" | \
  python3 -c "
import json,sys
r = json.load(sys.stdin)['data']['result']
print('quantile values:', sorted({x['metric'].get('quantile','none') for x in r}))
print('total series:', len(r))
"
```

If the output only contains `none`, the summary has no quantile label. Use
`_sum / _count` instead of `histogram_quantile()`.

---

## Aggregation Operators

Aggregation operators combine series across label dimensions.

| Operator | Description |
|---|---|
| `sum` | Sum values |
| `min` | Minimum value |
| `max` | Maximum value |
| `avg` | Average value |
| `group` | Return 1 for each group |
| `stddev` | Standard deviation |
| `stdvar` | Variance |
| `count` | Count series |
| `count_values` | Count series by value |
| `bottomk` | Smallest k elements |
| `topk` | Largest k elements |
| `quantile` | Calculate quantile across series |

Syntax:

```promql
<aggr_op>([parameter,] <vector>) [without|by (<label_list>)]
```

Examples:

```promql
# Sum by job
sum by (job) (
  http_requests_total
)

# Average while dropping instance
avg without (instance) (
  node_cpu_seconds_total
)

# Top 5 containers by memory
topk(5, container_memory_usage_bytes)

# Count series per job
count by (job) (
  up
)

# 95th percentile across series
quantile(0.95, http_request_duration_seconds)
```

### `by` vs `without`

```promql
# Keep only these labels
sum by (service, status_code) (
  rate(http_requests_total[5m])
)

# Drop only these labels and keep the rest
sum without (instance, pod) (
  rate(http_requests_total[5m])
)
```

---

## Rate and Counter Functions

Use these for counters, which are monotonically increasing metrics.

| Function | Description |
|---|---|
| `rate(v[d])` | Per-second average rate over a duration |
| `irate(v[d])` | Instantaneous rate using the last two samples |
| `increase(v[d])` | Total increase over a duration |
| `resets(v[d])` | Number of counter resets in a duration |

Examples:

```promql
# Requests per second
rate(http_requests_total[5m])

# Requests per second, summed by service
sum by (service) (
  rate(http_requests_total[5m])
)

# Total requests over 1 hour
increase(http_requests_total[1h])

# Counter resets in the last day
resets(process_cpu_seconds_total[1d])
```

### `rate()` vs `irate()`

Use `rate()` for:

- Dashboards
- Alerts
- Smooth trends
- SLO and burn-rate calculations

Use `irate()` only for:

- Highly volatile graphs
- Seeing short spikes that `rate()` smooths away

Do not use `irate()` for alerting.

---

## Gauge and Difference Functions

Use these for gauges, which can go up or down.

| Function | Description |
|---|---|
| `delta(v[d])` | Difference over duration |
| `idelta(v[d])` | Instantaneous difference between last two samples |
| `deriv(v[d])` | Per-second derivative using linear regression |
| `predict_linear(v[d], seconds)` | Predict future value using linear regression |

Examples:

```promql
# Gauge difference over 5 minutes
delta(queue_depth[5m])

# Predict disk full in 4 hours
predict_linear(node_filesystem_avail_bytes[1h], 4 * 3600) < 0

# Trend of memory usage
deriv(container_memory_usage_bytes[30m])
```

---

## Aggregation Over Time

These functions aggregate one series across time.

| Function | Description |
|---|---|
| `avg_over_time(v[d])` | Average over time |
| `min_over_time(v[d])` | Minimum over time |
| `max_over_time(v[d])` | Maximum over time |
| `sum_over_time(v[d])` | Sum over time |
| `count_over_time(v[d])` | Count samples |
| `quantile_over_time(q, v[d])` | Quantile over time |
| `stddev_over_time(v[d])` | Standard deviation |
| `stdvar_over_time(v[d])` | Variance |
| `last_over_time(v[d])` | Most recent value |
| `present_over_time(v[d])` | 1 if any value exists |

Examples:

```promql
# Average CPU metric value over 1 hour
avg_over_time(node_cpu_seconds_total[1h])

# Max memory in the last day
max_over_time(container_memory_usage_bytes[1d])

# 95th percentile over 10 minutes
quantile_over_time(0.95, http_request_duration_seconds[10m])

# Count samples in a window
count_over_time(up[1h])

# Check if metric exists in the last 5 minutes
present_over_time(up{job="api"}[5m])
```

### Subquery example

Use subqueries when applying over-time functions to calculated values.

```promql
# Current rate is greater than 3x the 1-hour average rate
rate(http_requests_total[5m])
>
3 * avg_over_time(rate(http_requests_total[5m])[1h:5m])
```

---

## Filtering With Label Matchers

```promql
# Exact match
http_requests_total{job="api", status_code="200"}

# Negative exact match
http_requests_total{job!="api"}

# Regex match
http_requests_total{status_code=~"5.."}

# Negative regex
http_requests_total{status_code!~"2.."}

# Multiple values
http_requests_total{env=~"staging|production"}
```

Prometheus regex matchers are anchored. `status=~"5.."` behaves like `^5..$`.

---

## Binary Operators

### Arithmetic operators

| Operator | Meaning |
|---|---|
| `+` | Add |
| `-` | Subtract |
| `*` | Multiply |
| `/` | Divide |
| `%` | Modulo |
| `^` | Power |

### Comparison operators

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

Use `bool` when you want a 0/1 result instead of filtering.

```promql
http_requests_total > bool 100
```

### Logical and set operators

| Operator | Meaning |
|---|---|
| `and` | Series present in both sides |
| `or` | Series from either side |
| `unless` | Series in left side but not right side |

Examples:

```promql
# Series in both
http_requests_total and http_errors_total

# Series in first but not second
up unless on(instance) alerts

# Either metric
metric_a or metric_b
```

---

## Vector Matching and Joins

PromQL joins are binary operations between instant vectors.

### Add one name label to a metric

Use an `*_info` metric to enrich IDs with names.

```promql
metric
* on(projectID) group_left(projectName)
  project_info{projectName=~"$project"}
```

### Add two name labels

```promql
metric
* on(buildDefinitionID, projectID) group_left(buildDefinitionName)
  build_definition_info{buildDefinitionName=~"$buildDefinition"}
* on(projectID) group_left(projectName)
  project_info{projectName=~"$project"}
```

### Join via an intermediate metric

```promql
agent_job{planType!="PoolMaintenance"}
* on(agentPoolAgentID) group_left(agentPoolID, agentPoolName)
  agent_info{agentPoolName=~"$agentPool"}
```

### Join for legend only

Omit filters on the info metric when you only want labels for legends.

```promql
metric
* on(projectID) group_left(projectName)
  project_info
```

### Rename a label before joining

```promql
label_replace(
  agent_job{planType!="PoolMaintenance"},
  "projectID", "$1", "scopeID", "^(.+)$"
)
* on(projectID) group_left(projectName)
  project_info{projectName=~"$project"}
```

### Divide by matching labels

```promql
http_requests_total
/
on(instance, job) group_left
http_requests_limit
```

### Ignore one label during matching

```promql
node_memory_MemFree_bytes
/
ignoring(device)
node_memory_MemTotal_bytes
```

---

## Histogram Queries

Prometheus has classic histograms and native histograms.

### Classic histograms

Classic histograms expose metrics like:

- `http_request_duration_seconds_bucket`
- `http_request_duration_seconds_sum`
- `http_request_duration_seconds_count`

Use `histogram_quantile()` with bucket metrics.

```promql
# p99 latency
histogram_quantile(0.99,
  sum by (le) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)
```

For grouped quantiles, keep `le` and the grouping labels.

```promql
# p95 latency by service
histogram_quantile(0.95,
  sum by (le, service) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)
```

Common mistake:

```promql
# Wrong: drops le
histogram_quantile(0.95,
  sum by (service) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)
```

Without `le`, Prometheus cannot reconstruct the buckets.

### Native histograms

Native histogram syntax is simpler.

```promql
histogram_quantile(0.95,
  sum(rate(http_request_duration_seconds[5m]))
)
```

### Histogram helper functions

| Function | Description |
|---|---|
| `histogram_quantile(φ, v)` | Calculate φ-quantile |
| `histogram_count(v)` | Extract count from native histogram |
| `histogram_sum(v)` | Extract sum from native histogram |
| `histogram_avg(v)` | Calculate average from histogram |
| `histogram_fraction(l, u, v)` | Fraction between bounds |
| `histogram_stddev(v)` | Standard deviation from histogram |
| `histogram_stdvar(v)` | Variance from histogram |

Examples:

```promql
# Median latency by job
histogram_quantile(0.5,
  sum by (job, le) (
    rate(http_request_duration_seconds_bucket[5m])
  )
)

# Average request size for native histograms
histogram_avg(http_request_size_bytes)
```

---

## Summary Metrics

Prometheus summaries often expose:

- `metric_sum`
- `metric_count`
- `metric{quantile="0.95"}` if quantiles were configured

If no `quantile` label exists, do not use `histogram_quantile()`.

Use `_sum / _count`.

```promql
# Simple average
sum(duration_sum)
/
sum(duration_count)
```

```promql
# Moving average over 10 minutes
sum(increase(duration_sum[10m]))
/
sum(increase(duration_count[10m]))
```

```promql
# Average by build definition, enriched with names
(
  sum by (buildDefinitionID, projectID) (duration_sum)
  /
  sum by (buildDefinitionID, projectID) (duration_count)
)
* on(buildDefinitionID, projectID) group_left(buildDefinitionName)
  build_definition_info
* on(projectID) group_left(projectName)
  project_info{projectName=~"$project"}
```

---

## Math Functions

| Function | Description |
|---|---|
| `abs(v)` | Absolute value |
| `ceil(v)` | Round up |
| `floor(v)` | Round down |
| `round(v, to)` | Round to nearest |
| `clamp(v, min, max)` | Clamp between bounds |
| `clamp_min(v, min)` | Lower bound |
| `clamp_max(v, max)` | Upper bound |
| `exp(v)` | Exponential |
| `ln(v)` | Natural logarithm |
| `log2(v)` | Base-2 logarithm |
| `log10(v)` | Base-10 logarithm |
| `sqrt(v)` | Square root |
| `sgn(v)` | Sign: -1, 0, or 1 |

Examples:

```promql
# Round memory to nearest 0.1 GiB
round(container_memory_usage_bytes / 1024 / 1024 / 1024, 0.1)

# Clamp CPU usage between 0 and 100
clamp(cpu_usage, 0, 100)

# Absolute difference
abs(predicted_value - actual_value)
```

---

## Date and Time Functions

| Function | Description |
|---|---|
| `time()` | Current Unix timestamp |
| `timestamp(v)` | Timestamp of samples |
| `day_of_month()` | Day of month, 1-31 |
| `day_of_week()` | Day of week, 0=Sunday to 6=Saturday |
| `day_of_year()` | Day of year, 1-366 |
| `days_in_month()` | Days in month |
| `hour()` | Hour, 0-23 |
| `minute()` | Minute, 0-59 |
| `month()` | Month, 1-12 |
| `year()` | Year |

Examples:

```promql
# Seconds since last scrape
time() - timestamp(up)

# Business hours only, 09:00-17:00
http_requests_total
and on()
hour() >= 9
and on()
hour() < 17

# Weekdays only
up
and on()
day_of_week() >= 1
and on()
day_of_week() <= 5
```

---

## Label Functions

| Function | Description |
|---|---|
| `label_join(v, dst, sep, src...)` | Join label values into a new label |
| `label_replace(v, dst, repl, src, regex)` | Create or replace a label using regex |

Examples:

```promql
# Create full address label
label_join(up, "address", ":", "instance", "port")

# Extract host from instance
label_replace(up, "host", "$1", "instance", "([^:]+):.*")

# Rename label
label_replace(metric, "new_name", "$1", "old_name", "(.*)")
```

---

## Common Production Patterns

### Request rate

```promql
sum by (service) (
  rate(http_requests_total[5m])
)
```

### Error rate percentage

```promql
sum(rate(http_requests_total{status=~"5.."}[5m]))
/
sum(rate(http_requests_total[5m]))
* 100
```

### Success rate percentage

```promql
(
  1 -
  sum(rate(http_requests_total{status=~"5.."}[5m]))
  /
  sum(rate(http_requests_total[5m]))
)
* 100
```

### Availability SLI

```promql
sum(rate(http_requests_total{status=~"2.."}[5m]))
/
sum(rate(http_requests_total[5m]))
* 100
```

### Service up availability

```promql
avg_over_time(up{job="api"}[5m]) < 0.9
```

### CPU usage percentage

```promql
100 -
(
  avg by (instance) (
    rate(node_cpu_seconds_total{mode="idle"}[5m])
  )
  * 100
)
```

### Memory usage percentage

```promql
100 *
(
  1 -
  node_memory_MemAvailable_bytes
  /
  node_memory_MemTotal_bytes
)
```

### Disk usage percentage

```promql
100 *
(
  1 -
  node_filesystem_avail_bytes{fstype!~"tmpfs|overlay"}
  /
  node_filesystem_size_bytes{fstype!~"tmpfs|overlay"}
)
```

### Disk filling prediction

```promql
predict_linear(node_filesystem_avail_bytes{mountpoint="/"}[1h], 4 * 3600) < 0
```

### Apdex score

Target: 0.5s. Tolerated: 2s.

```promql
(
  sum(rate(http_request_duration_seconds_bucket{le="0.5"}[5m]))
  +
  sum(rate(http_request_duration_seconds_bucket{le="2"}[5m]))
)
/
2
/
sum(rate(http_request_duration_seconds_count[5m]))
```

### Config reloads

```promql
changes(prometheus_config_last_reload_successful[1h])
```

### Restarts

For counters:

```promql
resets(process_start_time_seconds[1d])
```

For process start timestamp age:

```promql
time() - process_start_time_seconds
```

### Missing metric alert

```promql
absent(up{job="myservice"})
```

### No data for duration

```promql
absent_over_time(up{job="myservice"}[5m])
```

---

## Count and Presence Patterns

### Count matching series

```promql
count(
  pullrequest_info
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
```

### Count with label filter

```promql
count(
  pullrequest_info{voteStatus="Approved"}
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
```

### Count grouped by label

```promql
count by (voteStatus) (
  pullrequest_info
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
```

### Metric present in window

```promql
count_over_time(up{job="api"}[5m]) > 0
```

### Metric unchanged

```promql
changes(up{job="api"}[5m]) == 0
```

---

## Time-Based Age Patterns

### Age in seconds

```promql
time() - pullrequest_status{type="created"}
```

### Count items older than 7 days

```promql
count(
  (
    time()
    -
    pullrequest_status{type="created"}
    * on(projectID) group_left(projectName)
      project_info{projectName=~"$project"}
  ) >= 604800
)
```

### Average age

```promql
avg(
  time()
  -
  pullrequest_status{type="created"}
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
```

---

## Top-K Patterns

### Top 10 slowest pipelines

```promql
topk(10,
  avg by (buildDefinitionID, projectID) (
    builds_duration_sum / builds_duration_count
  )
  * on(buildDefinitionID, projectID) group_left(buildDefinitionName)
    build_definition_info
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
```

### Top 10 by count with info join

```promql
topk(10,
  sum by (agentPoolID) (
    increase(agentpool_builds[24h])
  )
  * on(agentPoolID) group_left(agentPoolName)
    agentpool_info{agentPoolName=~"$agentPool"}
)
```

---

## DORA Metric Patterns

### Deployment frequency

Successful builds per day:

```promql
round(
  sum(
    rate(builds{result="succeeded"}[1h])
    * on(projectID) group_left(projectName)
      project_info{projectName=~"$project"}
  )
  * 86400,
  1
)
```

### Change failure rate percentage

```promql
sum(
  rate(builds{result="failed"}[1h])
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
/
sum(
  rate(builds[1h])
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
* 100
```

### CI/CD health score

```promql
avg(
  success_sum
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
/
avg(
  success_count
  * on(projectID) group_left(projectName)
    project_info{projectName=~"$project"}
)
* 100
```

---

## SLO Queries

### Availability SLO over 30 days

```promql
1 -
(
  sum(increase(http_requests_total{status_code=~"5.."}[30d]))
  /
  sum(increase(http_requests_total[30d]))
)
```

### Error budget burn rate

For a 99.9% SLO:

```promql
(
  sum(rate(http_requests_total{status_code=~"5.."}[1h]))
  /
  sum(rate(http_requests_total[1h]))
)
/
(1 - 0.999)
```

Replace `0.999` with the SLO target.

### Multi-window burn-rate alert pattern

Example for a 99.9% SLO:

```promql
(
  (
    sum(rate(http_requests_total{status_code=~"5.."}[5m]))
    /
    sum(rate(http_requests_total[5m]))
  )
  /
  (1 - 0.999)
) > 14.4
and
(
  (
    sum(rate(http_requests_total{status_code=~"5.."}[1h]))
    /
    sum(rate(http_requests_total[1h]))
  )
  /
  (1 - 0.999)
) > 14.4
```

---

## Grafana Variable Queries

For newer Grafana dashboards, prefer the Prometheus variable editor typed query
modes where possible:

- Label names
- Label values
- Metrics
- Query result
- Series query

Classic `label_values(metric, label)` syntax is still widely used for compatibility.

### Classic variable examples

```promql
# All project names
label_values(project_info, projectName)

# Dependent variable filtered by parent variable
label_values(build_definition_info{projectName=~"$project"}, buildDefinitionName)

# Filtered by another variable
label_values(agent_info{agentPoolName=~"$agentPool"}, agentName)
```

### Use variables in queries

```promql
# Single-select variable
{job="$job"}

# Multi-select variable
{job=~"$job"}

# Multi-select with All
{job=~"$job"}
```

For multi-select variables, use regex matchers: `=~"$var"`.

A custom `allValue` of `.*` works well when the variable is always used in a
regex matcher context.

Do not blindly use `.*` for every datasource or every variable. If custom All is
blank, Grafana can format selected values using datasource-specific interpolation.

### Query result variables

Use `query_result(...)` when the variable must depend on:

- `$__range`
- `$__range_s`
- query logic
- calculated values

Otherwise, label and series variables are usually cheaper.

---

## Grafana Dashboard JSON Gotcha

When generating dashboard JSON, make sure the variable `definition` matches the
actual query.

```python
# Wrong
{
  "query": {"query": "label_values(project_info, projectName)"},
  "definition": ""
}

# Correct
q = "label_values(project_info, projectName)"
{
  "query": {"query": q},
  "definition": q
}
```

---

## Recording Rules

Recording rules pre-compute expensive queries, improving dashboard load time and
reducing Prometheus/Mimir query load.

Use them for:

- High-traffic request rates
- Expensive histogram quantiles
- SLO burn rates
- High-cardinality aggregations
- Dashboard panels loaded frequently

Example:

```yaml
groups:
  - name: http_request_rates
    interval: 1m
    rules:
      - record: job:http_requests_total:rate5m
        expr: |
          sum by (job) (
            rate(http_requests_total[5m])
          )

      - record: job:http_errors:ratio5m
        expr: |
          sum by (job) (
            rate(http_requests_total{status_code=~"5.."}[5m])
          )
          /
          sum by (job) (
            rate(http_requests_total[5m])
          )

      - record: job:http_request_duration:p95_rate5m
        expr: |
          histogram_quantile(0.95,
            sum by (le, job) (
              rate(http_request_duration_seconds_bucket[5m])
            )
          )
```

Naming convention:

```text
<aggregation_level>:<metric_name>:<operation_and_window>
```

Examples:

```text
job:http_requests_total:rate5m
job:http_errors:ratio5m
job:http_request_duration:p95_rate5m
```

---

## Cardinality and Performance

High-cardinality labels make queries slow and storage expensive.

Avoid labels like:

- request ID
- user ID
- email address
- session ID
- full URL with IDs
- trace ID
- order ID
- customer-specific free text

Prefer route templates:

```text
/api/users/123      -> /api/users/{id}
/orders/987/items   -> /orders/{order_id}/items
```

### Find metrics with most series

```promql
topk(10,
  count by (__name__) (
    {__name__=~".+"}
  )
)
```

### Count series for a metric

```promql
count(http_requests_total)
```

### Count label value cardinality

```promql
count(
  count by (user_id) (
    http_requests_total
  )
)
```

### Drop high-cardinality labels before ingestion

Example Alloy-style relabeling:

```hcl
prometheus.scrape "api" {
  targets = [...]

  rule {
    source_labels = ["user_id"]
    action        = "labeldrop"
  }
}
```

---

## Performance Rules

1. Use label filters as early as possible.
2. Aggregate before expensive visualisation when possible.
3. Use recording rules for repeated heavy queries.
4. Avoid regex matchers on high-cardinality labels.
5. Avoid broad selectors like `{__name__=~".+"}` in dashboards.
6. Prefer `$__rate_interval` for Grafana rate panels.
7. Avoid `query_result(...)` variables unless needed.
8. Do not put unbounded labels in legends.
9. Precompute SLO and histogram-heavy panels.
10. Inspect actual labels before assuming joins.

---

## Common Gotchas

### Gotcha 1: Stats metrics have only IDs, not names

Counters often only carry IDs.

```promql
# No data if projectName is not on this metric
builds_total{projectName=~"$project"}

# Correct: join metadata metric
builds_total
* on(projectID) group_left(projectName)
  project_info{projectName=~"$project"}
```

---

### Gotcha 2: Wrong label names

Different exporters use different labels for the same concept.

Examples:

```text
pullrequestCreatedBy vs creator
pullrequestID        vs pullrequest_id
buildDefinitionName  vs definitionName vs buildName
```

Prometheus label names are case-sensitive.

Always inspect labels before writing queries.

---

### Gotcha 3: Summary metrics without quantiles

If only these exist:

```text
my_summary_sum
my_summary_count
```

and the base metric has no `quantile` label, you cannot build p50/p90/p99 panels.
Use `_sum / _count`.

---

### Gotcha 4: Release/deployment metrics have no name labels

Some exporters expose release metrics with IDs only.

```text
release_info{projectID="...", releaseDefinitionID="..."}
```

Join to metadata metrics for names:

```promql
release_info
* on(releaseDefinitionID, projectID) group_left(releaseDefinitionName)
  release_definition_info
* on(projectID) group_left(projectName)
  project_info
```

---

### Gotcha 5: Agent job metrics have no pool labels

If `agent_job` has `agentPoolAgentID` and `scopeID` but no `agentPoolName`,
join through `agent_info`.

```promql
label_replace(
  agent_job,
  "projectID", "$1", "scopeID", "^(.+)$"
)
* on(agentPoolAgentID) group_left(agentPoolID, agentPoolName)
  agent_info
* on(projectID) group_left(projectName)
  project_info
```

---

### Gotcha 6: Multi-value variables need regex matchers

```promql
# Wrong for multi-select
{job="$job"}

# Correct
{job=~"$job"}
```

---

### Gotcha 7: `increase()` can return decimals

`increase()` extrapolates to the full window and may return non-integer values.

For display-only panels:

```promql
round(
  increase(builds_total[24h])
  * on(projectID) group_left(projectName)
    project_info,
  1
)
```

---

### Gotcha 8: Binary expression must contain only scalar and instant vector types

This usually means you tried to do a binary operation inside a range-vector
function.

```promql
# Wrong
rate(metric * on(id) group_left(name) info[5m])

# Correct
rate(metric[5m])
* on(id) group_left(name)
  info
```

---

### Gotcha 9: Vector matching on inconsistent metric names

Error:

```text
parse error: vector matching must be on consistent metric name
```

This can happen when both sides of a binary operation carry different
`__name__` labels in a context where Prometheus cannot match them cleanly.

Usually it means:

- You chained two non-info metrics together.
- You should join one data metric to one metadata/info metric.
- You may need `ignoring(__name__)`, but verify the query shape first.

---

### Gotcha 10: Division by zero

PromQL does not have a direct `if denominator == 0 then 0` syntax.

Common dashboard-safe pattern:

```promql
(
  sum(rate(errors_total[5m]))
  /
  sum(rate(requests_total[5m]))
)
or vector(0)
```

For stricter filtering:

```promql
sum(rate(errors_total[5m]))
/
(
  sum(rate(requests_total[5m]))
  > 0
)
```

Use carefully, because comparison without `bool` filters series.

---

### Gotcha 11: Python f-strings and Prometheus braces

When generating PromQL in Python, escape Prometheus label braces.

```python
# Correct
expr = f'rate(http_requests_total{{job=~"{job}"}}[5m])'
```

Keep emojis and display strings outside query f-strings when possible.

```python
tgt(
    f'count(metric{{voteStatus="Approved"}} * on(id) info{{name=~"{project}"}})',
    "Approved",
    "A"
)
```

---

### Gotcha 12: NaN-emitting gauges break Grafana lines

Some exporters emit `NaN` sample values for gauges between real updates (for
example the TrueNAS exporter's realtime CPU/memory/ARC metrics whenever the
underlying API returns nothing). Prometheus stores NaN samples, and Grafana
renders each NaN as a break — dense NaN flapping turns lines into dots.
`spanNulls` does NOT bridge NaN samples, only missing ones.

Fix at query time by filtering NaN with a comparison (NaN fails every
comparison):

```promql
# Before: dotted line whenever the exporter emits NaN
avg(truenas_cpu_user_percent{instance=~"$instance"})

# After: NaN samples dropped, line connects (pair with spanNulls for the
# resulting missing points)
avg((truenas_cpu_user_percent{instance=~"$instance"} >= 0))
```

Use `>= 0` only when negative values are impossible; otherwise use
`== metric` self-comparison or `> -Inf`-style bounds that keep the valid range.

When adding such guards mechanically with a regex over generated dashboards,
the naive pattern `(metric_prefix_[a-z0-9_]+(?:\{[^}]*\})?)(?!\s*\[)` is
dangerous: regex backtracking can shrink `[a-z0-9_]+` so the negative
lookahead passes, splitting a metric name in half (`…_total` becomes
`…_tota` + `l`) or splitting a selector before its `{`. The lookahead must
also reject name characters and `{`:

```python
GUARD = re.compile(r"(truenas_[a-z0-9_]+(?:\{[^}]*\})?)(?![a-z0-9_]|\s*[\[{])")
```

Always validate afterwards that the set of metric names in the generated
output is a subset of known-real metric names — that catches any
transformation that mangles a selector.

---

## Quick Reference Table

| Task | Pattern |
|---|---|
| Add name label | `metric * on(id) group_left(name) info` |
| Add two name labels | Chain two `* on(...) group_left(...)` joins |
| Rate then join | `rate(metric[5m]) * on(id) group_left(name) info` |
| Increase then join | `increase(metric[24h]) * on(id) group_left(name) info` |
| Average from summary | `sum(duration_sum) / sum(duration_count)` |
| Count with filter | `count(metric{label="value"} * on(id) group_left(name) info)` |
| Age in seconds | `time() - timestamp_metric` |
| Top N | `topk(N, avg by(labels)(metric) * on(...) group_left(...) info)` |
| Rename label for join | `label_replace(metric, "new", "$1", "old", "^(.+)$")` |
| Per-project breakdown | `sum by(projectName)(rate(metric[5m]) * on(projectID) group_left(projectName) info)` |
| Missing metric | `absent(metric{label="value"})` |
| Missing over time | `absent_over_time(metric{label="value"}[5m])` |
| Disk full prediction | `predict_linear(node_filesystem_avail_bytes[1h], 4 * 3600) < 0` |
| p95 classic histogram | `histogram_quantile(0.95, sum by (le)(rate(metric_bucket[5m])))` |
| p95 by service | `histogram_quantile(0.95, sum by (le, service)(rate(metric_bucket[5m])))` |

---

## Troubleshooting Checklist

When a PromQL query returns no data:

1. Confirm the metric exists.
2. Query the raw metric without filters.
3. Inspect the actual labels.
4. Confirm variable interpolation in Grafana.
5. Replace `=~"$var"` temporarily with a literal label value.
6. Remove joins and add them back one at a time.
7. Check whether the metric is a counter, gauge, histogram, summary, or info metric.
8. For histograms, verify `_bucket` and `le` labels exist.
9. For summaries, verify whether quantile labels exist.
10. Check the selected dashboard time range.
11. Check the scrape interval and use a wide enough rate window.
12. Use Explore before adding the query to a panel.

When a query is slow:

1. Add label filters.
2. Reduce regex use.
3. Avoid global selectors.
4. Aggregate earlier.
5. Use recording rules.
6. Check cardinality.
7. Limit variable queries.
8. Avoid high-cardinality legend labels.
9. Test with shorter time ranges.
10. Inspect Prometheus/Mimir query logs if available.

---

## References

- Prometheus querying basics: https://prometheus.io/docs/prometheus/latest/querying/basics/
- Prometheus operators: https://prometheus.io/docs/prometheus/latest/querying/operators/
- Prometheus functions: https://prometheus.io/docs/prometheus/latest/querying/functions/
- Prometheus naming best practices: https://prometheus.io/docs/practices/naming/
- Grafana Explore: https://grafana.com/docs/grafana/latest/explore/
- Grafana Prometheus datasource: https://grafana.com/docs/grafana/latest/datasources/prometheus/
- Grafana Mimir: https://grafana.com/docs/mimir/latest/
