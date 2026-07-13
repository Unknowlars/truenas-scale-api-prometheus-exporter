# Dashboard Design Patterns

Layout philosophy, audience-focused rows, information hierarchy,
creative panel choices, and lessons from building real production dashboards.

> For visual polish — hero KPI bands, gradients, color identity, value
> mappings, panel style presets (Grafana 13.1), demo mode, and the wow-factor
> pre-flight checklist — read `visual-design-wow.md` alongside this file.

---

## Information Hierarchy

Every dashboard should have three tiers, top to bottom:

```
┌─────────────────────────────────────────────────────────┐
│  TIER 1 — Always Visible (top of dashboard)             │
│                                                         │
│  KPI stat panels · Health scores · Live counts          │
│  DORA metrics · Threshold-coloured big numbers          │
│  h=3-4, arranged across full 24 cols                    │
├─────────────────────────────────────────────────────────┤
│  TIER 2 — Key Trends (middle, main content)             │
│                                                         │
│  Time series trends · Bar gauge rankings                │
│  Pie/donut distributions · State timelines              │
│  Histograms · Bar charts                                │
│  h=7-10                                                 │
├─────────────────────────────────────────────────────────┤
│  TIER 3 — Detail / On Demand (bottom, collapsible)      │
│                                                         │
│  Full data tables · Drill-down views                    │
│  Collapsed rows with stage/job detail                   │
│  h=8-14                                                 │
└─────────────────────────────────────────────────────────┘
```

---

## Audience-Specific Row Design

Design each row FOR a specific person. Label it in the row title.

### For Managers / Stakeholders
- DORA KPIs: Deployment Frequency, Change Failure Rate
- CI/CD Health Score (% success)
- PR review velocity (avg age, stale count)
- Release success rates
- Single-number stats with background colour + sparkline

### For DevOps Engineers
- Agent pool utilisation + capacity
- Queue depth vs throughput overlay
- Build duration per definition (find slow pipelines)
- Running jobs table (live)
- Failing definitions ranked
- Deploy failed environments

### For Developers / Squads
- Open PRs by author (who's blocked)
- PR vote status (what needs attention)
- Build results per definition (is their pipeline green)
- Latest build per definition table
- PR age buckets (is the team reviewing fast enough)

### For SRE / Reliability
- Error rates and service health
- Agent availability state timeline
- Exporter health / scrape errors
- Release environment status

---

## Row Structure Template

```python
# Pattern for a well-structured section:
panels.append(row(N, "🔀 Section Name", y)); y += 1

# 1. Text header with context (optional but good for complex dashboards):
panels.append(text_panel(N+1, "",
    "## Section Name\n\nWhat this shows. Who it is for.\n\n> **Tip:** filter with `$project`",
    0, y, 24, 3))
y += 3

# 2. KPI stats row:
for i, (id, title, expr, thresholds) in enumerate(kpis):
    panels.append(stat(id, title, expr, x=i*3, y=y, w=3, h=4, thresholds=thresholds))
y += 4

# 3. Visual panels (trends, distributions, rankings):
panels.append(ts(N+10, "Trend", ..., x=0, y=y, w=12, h=8))
panels.append(bargauge(N+11, "Top N", ..., x=12, y=y, w=12, h=8))
y += 8

# 4. Detail table (full data):
panels.append(table(N+20, "All Items", ..., x=0, y=y, w=24, h=10))
y += 10
```

---

## Creative Panel Choices

### When to use each panel type

| Use case | Best panel | Why |
|----------|-----------|-----|
| "Is this good or bad?" | `stat` with threshold colours | Instant visual |
| "How has this changed?" | `timeseries` | Time = x-axis |
| "Who has the most?" | `barchart` horizontal | Easy to read rankings |
| "What's the breakdown?" | `piechart` donut | Proportions |
| "Which are the worst?" | `bargauge` gradient | Top-N with threshold |
| "What shape is the data?" | `histogram` | Distribution insight |
| "How did status change over time?" | `state-timeline` | Colour bands per entity |
| "What's everything now?" | `table` with cell overrides | Filterable, sortable |
| "What % of gauge range?" | `gauge` radial | Context vs min/max |

### Histogram instead of average

An average hides the distribution. A histogram showing PR age reveals:
- Most PRs close in < 1 day (healthy)
- A fat tail to 7+ days (bottleneck)
- Bimodal distribution (two workflows)

Use histogram for: PR ages, build durations, queue waits, latency values.

### State timeline for "health over time"

Instead of a sparkline, show an agent pool's online fraction as a
state timeline band (red/yellow/green). You instantly see:
- Overnight maintenance windows (daily dips)
- Agents going offline during business hours (incident)
- Consistently red pool (capacity problem)

### Stacked area for composition

Show build results as stacked area (succeeded/failed/canceled):
- Width of each colour = volume
- Rising red band = more failures
- Flat stack = steady pipeline

Use `stacking="normal"` on timeseries.

### Dual-axis overlay for correlation

Put build duration (line) and queue wait (line) on the same panel.
When wait rises while duration is flat = agent capacity issue.
When both rise = pipeline and capacity problem.

---

## Colour Strategy

### Traffic light (standard):
```python
thresholds=[
    {"color":"red",    "value":0},
    {"color":"yellow", "value":70},
    {"color":"green",  "value":90}
]
```

### Inverse (lower is better):
```python
thresholds=[
    {"color":"green",  "value":0},
    {"color":"yellow", "value":15},
    {"color":"red",    "value":30}
]
```

### Agent/capacity pressure:
```python
thresholds=[
    {"color":"green",  "value":0},
    {"color":"yellow", "value":0.6},
    {"color":"red",    "value":0.85}
]
```

### Consistent series colours across panels

Pin every `succeeded` series to `#1a9e3a` green and every `failed` series to
`#F2495C` red in every panel. Use overrides:

```python
RESULT_OVERRIDES = [
    {"matcher":{"id":"byName","options":"succeeded"},
     "properties":[{"id":"color","value":{"fixedColor":"#1a9e3a","mode":"fixed"}}]},
    {"matcher":{"id":"byName","options":"failed"},
     "properties":[{"id":"color","value":{"fixedColor":"#F2495C","mode":"fixed"}}]},
    {"matcher":{"id":"byName","options":"canceled"},
     "properties":[{"id":"color","value":{"fixedColor":"#FF9830","mode":"fixed"}}]},
    {"matcher":{"id":"byName","options":"partiallySucceeded"},
     "properties":[{"id":"color","value":{"fixedColor":"#E0B400","mode":"fixed"}}]},
]
# Reuse this list across all build result panels
```

---

## PR Intelligence Center Pattern

A dedicated multi-panel section specifically for pull request health.
This pattern was developed and validated in the Azure DevOps v5 dashboard.

### Required stats row (8 stats × w=3):
1. Total Open PRs
2. Approved PRs (green)
3. Waiting for Author (orange warning threshold)
4. Rejected PRs (red warning threshold)
5. Draft PRs (gray)
6. Stale PRs > 7 days (red warning threshold)
7. Average PR Age (unit: `dtdurations`)
8. Oldest PR (unit: `dtdurations`)

### Required visual panels:
- **Histogram** of PR ages → reveals distribution shape
- **Pie/donut** of vote status mix → Approved/Waiting/Rejected/NoVote
- **Timeseries** Draft vs Ready count over time
- **Stacked timeseries** vote status evolution over time
- **Stacked timeseries** age bucket trend (< 1 day / 1-3 days / 3-7 days / > 7 days)
- **State timeline** PR vote status per repository
- **Barchart** PRs by author (horizontal, sorted desc)
- **Barchart** PRs by target branch (horizontal)
- **Barchart** PRs by source branch type (feature/bugfix/hotfix/users/other)

### Required tables:
- All Open Pull Requests (full detail, filterable, sortable)
- Stale PRs > 7 days (action-required view)
- Author Leaderboard (count per developer, threshold colour on count)

---

## DORA Metrics Implementation

DORA = DevOps Research and Assessment. Four key metrics:

| Metric | PromQL proxy | Target |
|--------|-------------|--------|
| Deployment Frequency | `sum(rate(builds{result="succeeded"}[1h])) * 86400` | Daily |
| Change Failure Rate | `failed_builds / total_builds * 100` | < 15% |
| Lead Time | Not available from ADO exporter directly | — |
| MTTR | Not available from ADO exporter directly | — |

**CI/CD Health Score** (derived KPI, not official DORA):
```promql
avg(success_sum / success_count) * 100
```
Display as stat with: `< 70% = red`, `70-90% = yellow`, `≥ 90% = green`.

---

## Layout Patterns for Common Widths

### 8 stats across full width (w=3 each):
```
[3][3][3][3][3][3][3][3]  = 24 ✓
```

### 6 stats (w=4 each):
```
[4][4][4][4][4][4]  = 24 ✓
```

### Two equal panels:
```
[timeseries w=12][bargauge w=12]  = 24 ✓
```

### Three equal panels:
```
[piechart w=8][piechart w=8][timeseries w=8]  = 24 ✓
```

### Wide + narrow:
```
[state-timeline w=14][table w=10]  = 24 ✓
[table w=16][bargauge w=8]         = 24 ✓
```

### Full-width:
```
[table w=24]  = 24 ✓
[timeseries w=24]  = 24 ✓
```

---

## Dashboard Metadata Best Practices

```python
dashboard = {
    "title":       "Service Name — Dashboard Type",  # format: "Service — Type"
    "uid":         "service-type-v3",                # slug, unique in instance
    "description": "One sentence: what it shows, who it's for, what data source.",
    "tags":        ["team", "service", "environment", "dora"],
    "refresh":     "30s",       # "5s" for live ops; "5m" for historical
    "time":        {"from": "now-6h", "to": "now"},  # default range
    "graphTooltip": 1,          # 1=shared crosshair, 2=shared tooltip
    "links": [
        {"title": "Source Code", "url": "https://github.com/...",
         "icon": "external link", "type": "link", "targetBlank": True}
    ]
}
```

---

## Self-Documenting Dashboards

Add `description` to every panel. Good descriptions answer:
- What does this panel show?
- Why does it matter?
- What should trigger action?
- What's the relationship to other panels?

Example:
```python
desc="Rising queue wait while build duration is flat = agent capacity problem. "
     "Add agents to the pool or investigate if agents are going offline."
```

Add a text panel at the start of complex sections:
```
## 🔀 Pull Request Intelligence Center

This section gives a **360° view of your PR pipeline** — from team-level
health to individual PR staleness, review velocity, author patterns,
branch strategies, and voting dynamics.

> **Tip:** Use `$project` and `$repository` variables to drill into
> specific teams or repositories.
```

---

## Variable Design

```
DS_PROMETHEUS  →  project  →  buildDefinition   (cascades)
                          →  repository         (cascades)
                          →  agentPool
                          →  releaseDefinition
                          →  buildResult         (from metric, not info)
                          →  buildReason         (from metric, not info)
```

Put all variables at the top. Order: datasource → scope (project) →
sub-scope (definition, pool, repo) → filter (result, reason).

Multi-select with All on most variables — users want to filter by project
but usually see all pools/definitions within that project.

---

## Performance Guidelines

- **Instant queries** (`instant: True`) are faster than range queries
  for tables and current-state panels.
- **Prefer typed Prometheus variable query types for new dashboards.** Classic
  `label_values(metric, label)` remains common in older dashboards, but Grafana
  documents it as deprecated classic query syntax. Use `query_result(expr)` only
  when you need dashboard time-range variables or query logic.
- **Collapsed rows** don't execute their queries until expanded — use
  for heavy queries that aren't needed in the default view.
- **Rate windows:** prefer Grafana `$__rate_interval` for Prometheus `rate()`/`increase()` panels, or choose an explicit range that is at least 4× the scrape interval. Use longer fixed windows such as `[10m]` or `[1h]` only when smoothing or slow-moving metrics justify it.
- **Avoid `.*` in metric selectors** — always filter by at least one label
  when the metric set is large.
