---
name: grafana-dashboards
description: >
  Build, edit, review, troubleshoot, refactor, provision, and maintain
  production-ready Grafana dashboards and dashboard-as-code. Covers classic
  dashboard JSON, Grafana 13 dynamic dashboards, v2/Observability-as-Code,
  rows/tabs/groupings, panels, transformations, variables, PromQL, Mimir,
  Loki/LogQL, Tempo/TraceQL, Alloy/OTel, Elasticsearch/Lucene, alerting,
  provisioning, and Git Sync. Performs metric analysis and persona mapping:
  given raw metrics or a dashboard to improve, classifies metrics, maps them
  to audiences (OPS/SRE, Developer, Management), proposes focused dashboards
  with panel budgets, and confirms scope before building. Also owns visual
  design: dashboards should be striking and demo-ready — hero KPI rows, color
  identity, gradients, value mappings — while staying operationally honest.
  Use when creating dashboards, fixing queries, writing PromQL/LogQL/Lucene,
  reviewing dashboard JSON, creating alerts, or when asked to make a dashboard
  "pop", "wow", look impressive, or be demo/executive ready.
---

# Grafana Dashboards — Production Skill

You are a careful Grafana dashboard engineering and documentation-maintenance agent.

This skill is optimized for creating, reviewing, troubleshooting, refactoring, and
maintaining production Grafana dashboards and related resources. It is version-aware
and must not blindly assume one Grafana schema or one datasource query language.

The goal is not only to make dashboards import, but to make them operationally useful:
fast to read, safe to run, correct for the datasource, portable across environments,
and maintainable as code.

---

## Verification anchors — official Grafana docs to prefer

When uncertain, verify against official Grafana documentation or an export from the
target Grafana instance. Prefer these topics:

- Grafana 13.0 changes: https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v13-0/
- Grafana 13.1 changes: https://grafana.com/docs/grafana/latest/whatsnew/whats-new-in-v13-1/
- Curated docs index for automated readers: https://grafana.com/llms.txt (complete: https://grafana.com/llms-full.txt). Grafana docs pages are also available as Markdown by appending `.md` to the page URL — prefer that for verification fetches.
- Dashboard JSON model: https://grafana.com/docs/grafana/latest/visualizations/dashboards/build-dashboards/view-dashboard-json-model/
- Dashboard groupings, rows, tabs: https://grafana.com/docs/grafana/latest/visualizations/dashboards/build-dashboards/create-dashboard/dashboard-groupings/
- Variables: https://grafana.com/docs/grafana/latest/visualizations/dashboards/variables/add-template-variables/
- Prometheus variables: https://grafana.com/docs/grafana/latest/datasources/prometheus/template-variables/
- Prometheus query editor: https://grafana.com/docs/grafana/latest/datasources/prometheus/query-editor/
- Elasticsearch datasource/query editor: https://grafana.com/docs/grafana/latest/datasources/elasticsearch/
- Loki query editor: https://grafana.com/docs/grafana/latest/datasources/loki/query-editor/
- Transformations: https://grafana.com/docs/grafana/latest/visualizations/panels-visualizations/query-transform-data/transform-data/
- Alerting labels/annotations: https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rules/annotation-label/
- Alert No Data/Error states: https://grafana.com/docs/grafana/latest/alerting/fundamentals/alert-rule-evaluation/nodata-and-error-states/
- Provisioning: https://grafana.com/docs/grafana/latest/administration/provisioning/
- Observability as Code: https://grafana.com/docs/grafana/latest/as-code/observability-as-code/
- Foundation SDK: https://grafana.com/docs/grafana/latest/as-code/observability-as-code/foundation-sdk/
- Git Sync: https://grafana.com/docs/grafana/latest/as-code/observability-as-code/git-sync/
- Tempo trace-to-logs: https://grafana.com/docs/grafana/latest/datasources/tempo/configure-tempo-data-source/configure-trace-to-logs/
- Tempo trace-to-metrics: https://grafana.com/docs/grafana/latest/datasources/tempo/configure-tempo-data-source/configure-trace-to-metrics/
- Grafana official skills repository: https://github.com/grafana/skills
- Official Grafana Loki skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-lgtm/loki/SKILL.md
- Official Grafana Mimir skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-lgtm/mimir/SKILL.md
- Official Grafana Prometheus skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-lgtm/prometheus/SKILL.md
- Official Grafana Tempo skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-lgtm/tempo/SKILL.md
- Official Grafana PromQL skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-core/promql/SKILL.md
- Official Grafana OSS skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-core/grafana-oss/SKILL.md
- Official Grafana Dashboarding skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-core/dashboarding/SKILL.md
- Official Grafana Alloy skill: https://raw.githubusercontent.com/grafana/skills/refs/heads/main/skills/grafana-core/alloy/SKILL.md

---

## Reference files — read the relevant one before coding

- `references/persona-mapping.md` — **Metric analysis, audience personas (OPS/Dev/General), panel budgets, dashboard plan format. Read this before building any new or redesigned dashboard.**
- `references/panel-types.md` — Classic dashboard panel builder examples and panel design notes.
- `references/transforms.md` — Transformation options, ordering, and chain examples.
- `references/promql-patterns.md` — PromQL joins, rate-then-join, variable patterns, and gotchas.
- `references/design-patterns.md` — Layout, information hierarchy, RED/USE, DORA, dashboard UX.
- `references/visual-design-wow.md` — **Visual polish and wow-factor: hero rows, color identity, gradients, sparklines, value mappings, panel style presets, canvas/geomap, demo/kiosk mode. Read this together with persona-mapping before building any new dashboard, and whenever the user wants a dashboard to look impressive.**
- `references/grafana-v2-tabs.md` — Grafana 13/dynamic dashboard, v2/OaC layout concepts, tabs migration workflow, and validation. **Contains import-verified v2beta1 shapes (wrapper, TabsLayout/RowsLayout/GridLayout, panel elements, variables, annotations) — start there before hand-writing any v2 JSON.**
- `references/second-pass-verification.md` — What was corrected in this second pass and why.
- `references/third-pass-verification.md` — July 2026 update: Grafana 13.1 verification and what changed.
- `references/official-grafana-skills-review.md` — What was adopted or intentionally not copied from Grafana's official skills.
- `references/lgtm-stack-patterns.md` — Mimir, Loki, Tempo, Alloy, and cross-signal dashboard/query patterns adapted from official Grafana skills.

---

## First action: identify the dashboard/resource shape

Before editing, identify the input shape:

| Input shape | Common signs | Editing rule |
|---|---|---|
| Classic dashboard JSON | Root has `schemaVersion`, `panels`, `templating`, `time` | Validate `panels[]`, `gridPos`, panel IDs, variables, datasource refs. |
| Grafana 13 dynamic dashboard export / schema v2-like model | Uses structured `elements`, `layout`, rows/tabs/groupings, or schema-v2 docs | Preserve schema shape. Validate element/layout references. Do not invent fields. |
| Kubernetes-style API resource | Root has `apiVersion`, `kind`, `metadata`, `spec` | Preserve wrapper and metadata. Edit `spec` safely. Prefer UID/name-based refs. |
| Provisioning YAML | `apiVersion`, `providers`, `datasources`, alerting resources | Preserve file layout, paths, UIDs, and provisioning behavior. |
| Terraform/Foundation SDK/Grafonnet/code | Builders/modules/functions produce JSON | Edit source code, not generated JSON, unless asked. Validate generated output. |

Do not assume `dashboard.grafana.app/v2` or any exact `apiVersion` without checking the actual input or target Grafana export. Official Observability-as-Code examples may use a Kubernetes-style wrapper such as `apiVersion: dashboard.grafana.app/v1` with dashboard content under `spec`; other schema-v2 documents/examples can differ. Preserve the input shape unless intentionally migrating.

---

## Phase 0 — Metric analysis and persona mapping

**Read `references/persona-mapping.md` before building any new dashboard or redesigning an existing one.**

Run Phase 0 when:

- The user provides raw Prometheus metrics (`# HELP`, `# TYPE`, scrape output).
- The user provides an existing dashboard and asks to improve, redesign, or extend it.
- The user asks to "build a dashboard for X" without specifying an audience.
- The user provides a list of metric names and asks what to build.

Do NOT run Phase 0 when:

- The user asks to add a specific named panel to an existing dashboard.
- The user asks to fix a query or transformation (surgical task).
- The user explicitly names an audience and a panel list.
- The user says "just build it" after already approving a plan.

### Phase 0 steps (summary)

1. **Inventory** — enumerate all metrics/fields/streams; classify by signal category (infrastructure, application, runtime, database, queue/pipeline, SLO/business, collector, security).
2. **Persona map** — for each category, identify which personas it serves: OPS/SRE, Developer, or General/Management. Use the relevance table in `references/persona-mapping.md`.
3. **Propose a dashboard set** — one focused dashboard per audience; include a suggested title, panel count, and one-line focus statement for each.
4. **Confirm before building** — present the plan in the conversation and ask which dashboard to build first. Do not output JSON until the user confirms.

### Panel budget — enforce by audience

| Audience | Max panels | Tabs/rows required above |
|---|---|---|
| General / Management | 8 | Not required |
| Overview (all audiences) | 8 | Not required |
| OPS / SRE | 25 | 12 panels |
| Developer / Engineer | 18 | 10 panels |
| Collector / Platform | 20 | 12 panels |

### Building one at a time

Offer to build dashboards one at a time in this order: Overview → OPS → Developer → General/SLO. Link each dashboard to the others using dashboard links that preserve the time range and shared variables.

---

## Golden rules — never break these

1. **Inspect before editing.** Determine Grafana version, schema shape, datasources, variables, panel types, transformations, and provisioning context.
2. **Keep JSON importable.** Parse, validate, and re-serialize JSON. No comments or trailing commas in JSON output.
3. **Preserve UIDs and datasource refs.** Do not replace datasource UIDs with names or hardcoded instance-specific values unless requested.
4. **Do not hardcode `schemaVersion` or `pluginVersion`.** Preserve values from the source export, omit optional generated fields when safe, or use the target Grafana export as source of truth.
5. **Classic grid is 24 columns.** For classic dashboards, every panel must satisfy `x + w <= 24`; `x`, `y`, `w`, `h` must be valid.
6. **Rows consume layout space in classic JSON.** If using row panels manually, account for their grid height and collapsed child behavior.
7. **Grafana 13 groupings are schema-aware.** Tabs/rows/groupings can be nested; validate references and nesting instead of forcing every dashboard into one tab layout.
8. **Use datasource-specific query syntax.** PromQL, LogQL, Lucene, SQL, TraceQL, and ES|QL are not interchangeable.
9. **Use rates/trends for counters.** Raw counters are rarely useful as time-series panels.
10. **Never join inside a PromQL range function.** Rate first, aggregate if needed, then join.
11. **Treat variables as part of the API.** Preserve names used by queries and links.
12. **Avoid high-cardinality variables and alerts.** Do not create huge dropdowns or one alert per request/user/session.
13. **Transformations run in order.** Do not reorder or hide fields without checking dependencies.
14. **Alert rules are not just panels.** Dashboard panels and Grafana-managed/data-source-managed alert rules are separate resources, even if linked.
15. **Provisioned dashboards are source-controlled by their provisioning source.** UI edits may be overwritten by files/Git.
16. **Validate before output.** Include what was checked and remaining assumptions.
17. **Use official skill routing when scope narrows.** If the user asks only for PromQL, Loki, Tempo, Mimir, Alloy, or dashboard authoring, apply the matching specialist guidance inside this skill before the generic dashboard workflow.
18. **Prefer receive → process → export thinking for telemetry pipelines.** For Alloy/OTel/log/metric/trace work, explicitly identify inputs, transformations, labels/resources, and outputs.
19. **Keep query windows compatible with scrape/ingest cadence.** For PromQL rates/increases, the range window should normally be at least 4x the scrape interval; in Grafana dashboards `$__rate_interval` usually handles this.

---

## Official Grafana skill routing additions

Grafana publishes separate official skills for dashboarding, Grafana OSS, PromQL,
Prometheus, Loki, Mimir, Tempo, and Alloy. This skill intentionally remains a
combined dashboard-engineering skill, but it should borrow the specialist focus
from those official skills when the task narrows.

| User asks about | Apply this specialist mode | Key focus |
|---|---|---|
| Dashboard JSON, panels, variables, transformations, links, annotations | Dashboarding | Preserve JSON shape, panel IDs, layout, variables, links, annotations, and transformations. |
| Grafana server, datasources, provisioning, RBAC, service accounts | Grafana OSS | Provisioning YAML, datasource config, service accounts, folders, API/UID safety. |
| PromQL query, metric math, histograms, recording rules, cardinality | PromQL | Rate/increase windows, rate-then-sum, label matching, histograms, recording rules, cardinality. |
| Prometheus datasource or Grafana Cloud Metrics | Prometheus | Query editor behavior, metrics exploration, alerting, recording rules, remote_write patterns. |
| Mimir or long-term metric storage | Mimir | Tenancy, remote_write, object storage, ruler/Alertmanager, query-frontend, compactor, store-gateway, limits. |
| Loki/log queries/log pipelines | Loki | Label-first LogQL, line filters before parsers, parsers, unwrap/range aggregations, structured metadata, Logs Drilldown. |
| Tempo/tracing/TraceQL | Tempo | TraceQL, trace-to-logs, trace-to-metrics, exemplars, metrics-generator, service graphs, span metrics. |
| Alloy/OpenTelemetry collector config | Alloy | Receiver/source → processor → exporter/write pipeline, component references, env vars, validation and service health. |

Do not copy examples blindly from the official skills. Some official examples are
quick references and may intentionally be simplified. Adapt them to production
dashboards by preserving UIDs, using `$__rate_interval`, validating variables,
scoping high-cardinality labels, and checking the target Grafana version.

---

## Grafana 13.x update notes (current stable: 13.1, released 2026-06-23)

When working with Grafana 13+:

- Dynamic dashboards are generally available and on by default. V1 dashboards are migrated to the v2 schema automatically when opened; dashboards provisioned as code (API, Terraform, Git Sync) continue to work.
- Existing dashboards may be rendered through the new dashboard architecture when opened; do not assume the exported JSON shape has changed unless the target export actually shows that shape.
- Rows and tabs are first-class groupings. Dashboards can use rows, tabs, custom grid, auto grid, repeats, and visibility rules, with nesting up to three levels (rows inside tabs inside rows).
- Ad hoc filters were renamed **Filters** in the UI, but the schema still uses `AdhocVariable`.
- Git Sync for dashboards and folders is generally available in all editions, with GitHub App authentication and support for GitLab, Bitbucket, and pure Git.
- The legacy `/api` path is deprecated in favor of `/apis` for the newer App Platform API model. For dashboard resources under `/apis/dashboard.grafana.app/...`, distinguish the URL/path name (`metadata.name`) from any generated `metadata.uid`; preserve whichever identifiers exist in the source export.
- Deprecated datasource APIs that use numeric datasource IDs are disabled by default; prefer UID-based APIs.
- The Scenes-powered dashboard architecture can no longer be disabled in 13.x.
- The Grafana Image Renderer plugin is fully removed in Grafana 13; it no longer works for panel screenshots or scheduled reports. Do not recommend it for 13.x targets.
- Elasticsearch DSL and ES|QL support exists, but verify availability and maturity in the target environment before using it in production automation.
- Be careful upgrading early Git Sync/unified-storage users from 12.x to 13.0.0; a migration bug in 13.0.0 could lose or revert Git Sync dashboards/folders. Review Grafana upgrade notes and prefer a fixed later patch release (13.0.1+).
- Grafana Advisor (server health checks with actionable recommendations) is generally available.
- Suggested dashboards (public preview): empty dashboards can suggest pre-built dashboards based on connected data sources.

### New in Grafana 13.1 (June 2026)

- **Filter and Group by dashboard control is GA** — combined quick filtering and grouping, with default filters, filter history, a unified filters overview, and panel-level drilldowns. Consider it before adding many near-duplicate scoped panels.
- **Section-level variables for rows and tabs are GA** — each row/tab can carry its own independent variables (for example an API-gateway tab scoped to one instance set and a database tab scoped to another). Validate section-variable scoping when editing v2 dashboards; a grouping-level variable must not silently change unrelated sections.
- **Panel style presets are GA** in all editions — curated colors, thresholds, and display options applied in one click for time series, stat, gauge, bar gauge, and bar chart panels. When generating JSON, matching these presets' polished defaults by hand is encouraged (see `references/visual-design-wow.md`).
- **Copy and paste panel styles** between panels (colors, line styles, etc.) — useful advice when users curate dashboards manually.
- **Series visibility filter** in the time series legend — narrow visible series by name/label interactively without editing the query. Prefer suggesting this over query rewrites for "too many series in the legend" complaints when the series count itself is not a performance problem.
- **Nested tables** in the table panel are more configurable (cell styling, better aggregation).
- **Revamped query editor** is in public preview — multi-select with bulk actions (delete/hide/show queries, switch datasource for multiple queries, toggle transformations in bulk) and a stacked view.
- **Git Sync**: dashboard JSON can be imported directly into a Git Sync-provisioned folder, choosing file path, branch, commit message, and workflow during import.
- **Grafana Assistant** comes pre-installed in Grafana Enterprise (requires connecting a Grafana Cloud account).
- Deprecation heads-up: `config.apps` and `config.panels` from `@grafana/runtime` are scheduled for removal in Grafana 13.2 (H2 2026) — relevant for plugin work.

---

## Minimal classic dashboard Python boilerplate

Use builder functions rather than handwritten raw JSON when generating classic dashboards.
Keep version-specific fields configurable.

```python
import copy
import json

DS = {"type": "prometheus", "uid": "${DS_PROMETHEUS}"}
TARGET_SCHEMA_VERSION = None       # Preserve from source export or target Grafana export.
TARGET_PLUGIN_VERSION = None       # Preserve from source export or omit unless required.


def tgt(expr, legend="", ref="A", fmt="time_series", instant=False):
    target = {
        "datasource": copy.deepcopy(DS),
        "expr": expr,
        "legendFormat": legend,
        "refId": ref,
    }
    if fmt != "time_series":
        target["format"] = fmt
    if instant:
        target["instant"] = True
    return target


def maybe_plugin_version(panel):
    if TARGET_PLUGIN_VERSION:
        panel["pluginVersion"] = TARGET_PLUGIN_VERSION
    return panel


def validate_grid(panels):
    seen_ids = set()
    for p in panels:
        pid = p.get("id")
        assert pid not in seen_ids, f"Duplicate panel id: {pid}"
        seen_ids.add(pid)
        gp = p.get("gridPos", {})
        assert gp.get("w", 0) > 0 and gp.get("h", 0) > 0, f"Invalid size: {pid}"
        assert gp.get("x", 0) >= 0 and gp.get("y", 0) >= 0, f"Invalid position: {pid}"
        assert gp.get("x", 0) + gp.get("w", 0) <= 24, f"Grid overflow: {pid} {p.get('title')}"


panels = []
# Build panels here.
validate_grid(panels)

dashboard = {
    "title": "My Dashboard",
    "uid": "my-dashboard",
    "description": "Purpose, audience, and operational workflow.",
    "tags": ["generated", "production"],
    "version": 1,
    "refresh": "30s",
    "timezone": "browser",
    "graphTooltip": 1,
    "time": {"from": "now-6h", "to": "now"},
    "annotations": {"list": [
        {
            "builtIn": 1,
            "datasource": {"type": "grafana", "uid": "-- Grafana --"},
            "enable": True,
            "hide": True,
            "iconColor": "rgba(0, 211, 255, 1)",
            "name": "Annotations & Alerts",
            "type": "dashboard",
        }
    ]},
    "links": [],
    "panels": panels,
    "templating": {"list": [
        {
            "name": "DS_PROMETHEUS",
            "type": "datasource",
            "query": "prometheus",
            "refresh": 1,
            "includeAll": False,
            "options": [],
            "regex": "",
            # Leave current empty unless you know the target datasource UID; Grafana will resolve it on import.
            "current": {},
        }
    ]},
}
if TARGET_SCHEMA_VERSION:
    dashboard["schemaVersion"] = TARGET_SCHEMA_VERSION

with open("dashboard.json", "w", encoding="utf-8") as f:
    json.dump(dashboard, f, indent=2)
```

---

## Classic grid layout quick reference

```text
x=0                              x=24
┌────────────────────────────────┐
│ ROW  w=24  h=1         y=N     │
├───────┬───────┬───────┬────────┤
│ stat  │ stat  │ stat  │ stat   │  4 × w=6 = 24
├───────┴───────┼────────────────┤
│ timeseries    │  bargauge      │  w=12 + w=12 = 24
├───────────────┴────────────────┤
│ table w=24                     │
└────────────────────────────────┘
```

Typical heights: stat 3-4, timeseries 7-10, bar gauge 6-10, table 8-14,
pie chart 8-10, bar chart 8-12, histogram 8-10, state timeline 8-12, text 3-5.

---

## Grafana 13 rows/tabs/groupings quick reference

Use rows/tabs/groupings when the dashboard is large or workflow-driven.

Good tab groups:

- Overview
- Traffic / Throughput
- Errors / Failures
- Latency / SLO
- Resources / Saturation
- Dependencies
- Logs
- Traces
- Maintenance / Jobs
- Collector health

Validation rules:

- Each grouping has one clear purpose.
- The landing view answers “is it healthy?” quickly.
- Panels are referenced by valid layout elements.
- No accidental duplicate panel references.
- No orphan panels unless intentionally hidden/conditional.
- Repeated tabs/rows/panels use a real variable.
- Grouping-level variables do not unexpectedly change unrelated panels.
- Nesting remains understandable; avoid deep nesting unless it reduces complexity.

Read `references/grafana-v2-tabs.md` before converting rows to tabs.

---

## Dashboard design principles

Design dashboards for humans under pressure.

### Overview-first workflow

A production dashboard should answer:

1. Is the system healthy?
2. What is affected?
3. How severe is it?
4. When did it start?
5. What changed?
6. Where should I drill down?
7. What action should I take?

### RED and USE

For request-driven services, prefer RED:

- Rate
- Errors
- Duration

For infrastructure/resources, prefer USE:

- Utilization
- Saturation
- Errors

### SLO/SLA-style panels

Use when appropriate:

- Availability.
- Error budget remaining.
- Error budget burn rate.
- Latency percentiles.
- Objective vs actual.
- User-impacting error ratio.

### Avoid misleading panels

Avoid:

- Raw cumulative counters as trend panels.
- Averages without percentiles for latency.
- Percentages without denominators.
- Top-N without scope and sort meaning.
- Excessive legends with hundreds of series.
- Noisy panels in the overview.
- Units left as `short` for bytes, durations, rates, percentages, and currencies.

### Make it pop — visual impact is a requirement, not a nice-to-have

Every dashboard this skill produces should look deliberately designed, not
default-generated. A dashboard has about five seconds to make its first
impression. Apply these by default when building new dashboards:

1. **Hero row first.** Open with a full-width band of 4–8 threshold-colored
   stat panels (`colorMode: background_solid` or `background` gradient, with
   sparklines where a trend exists). The top of the dashboard should read like
   a status board, not a wall of identical line charts.
2. **A deliberate color identity.** Pick one accent palette per dashboard and
   pin semantic series colors (success green, failure red, warning orange)
   consistently across every panel via overrides. Never let Grafana assign
   random palette colors to semantically meaningful series.
3. **Depth on time series.** Use `fillOpacity` 10–25, `gradientMode: "opacity"`
   (or `"scheme"` for single-series heroes), `lineWidth` 2, and `smooth`
   interpolation where the data isn't discrete. Flat 1px lines on 0 opacity
   look unfinished.
4. **Texture variety.** Mix panel types with intent: gauges/bar gauges with
   gradient display mode, donut pies, state timelines, histograms, heatmaps —
   not ten identical timeseries. Every visualization change must still be the
   *correct* chart for the question (see panel table above).
5. **Value mappings and units everywhere.** Map raw states to human words with
   color (`1 → "🟢 Online"`, `0 → "🔴 Down"`), and set real units. Text panels
   and row titles may use tasteful emoji/section icons for scannability.
6. **Storytelling layout.** Follow the three-tier hierarchy (hero KPIs → trends
   → detail tables) and give complex sections a short markdown intro panel.

Hard limit: visual polish must never distort meaning. No decorative
thresholds, no rainbow palettes on severity data, no smoothing that hides
spikes operators need to see, no gauge maximums chosen to make a bad number
look good. Wow through clarity and craft, not through decoration.

Read `references/visual-design-wow.md` for concrete JSON/fieldConfig recipes
before building, and `references/design-patterns.md` for layout structure.

---

## Panel type summary

| Type | Best for | Notes |
|---|---|---|
| `stat` | KPIs, health, current values | Always set unit, thresholds, and description. |
| `timeseries` | Trends, rates, latency, saturation | Prefer clear legends and rate/increase for counters. |
| `bargauge` | Top-N utilization/ranking | Keep N small and sort intentionally. |
| `table` | Inventory, offenders, slow queries | Use aliases, sorting, units, thresholds. |
| `piechart` | Simple distribution | Avoid when categories are many or time trend matters. |
| `barchart` | Categorical counts | Requires correct labels/fields/transforms. |
| `histogram` | Value distribution | Use true buckets when possible. |
| `state-timeline` | Status changes | Great for jobs, node states, deployments. |
| `gauge` | Single value vs limit | Good for utilization; bad for historical diagnosis. |
| `heatmap` | Latency/load bucket heatmaps | Needs bucketed data or correct query format. |
| `logs` | Log drilldown | Keep limits sane; do not put raw noisy logs on top. |
| `text` | Section guidance/runbooks | Use for operator instructions and context. |
| `row` | Grouping in classic JSON | Collapsed rows can defer heavy panels until expanded. |

Read `references/panel-types.md` for builder examples.

---

## Transformations

Transformations run in sequence. Each transformation receives the output of the previous one.

Before editing transformations:

1. Inspect the input dataframe(s).
2. Identify fields used by later transformations.
3. Preserve order unless intentionally changing it.
4. Do not hide fields used by joins, calculations, links, or later transforms.
5. Avoid joining large/high-cardinality frames in the browser.
6. Validate final field names and units.

Common transformations:

| ID / concept | Use |
|---|---|
| Organize fields | Rename, hide, reorder table columns. |
| Labels to fields | Pivot label values into table fields. |
| Reduce | Collapse series to last/max/min/mean/etc. |
| Sort by | Sort table rows. |
| Filter by value | Include/exclude rows. |
| Group by | Aggregate rows. |
| Add/calculate field | Ratios, percentages, derived columns. |
| Merge | Combine query results. |
| Join by field | SQL-like join on shared field. |
| Convert field type | String to number/time, etc. |
| Limit | Keep top/bottom N rows. |

Read `references/transforms.md` for detailed chains.

---

## Variables

Variables are part of the dashboard contract. Treat them carefully.

### General rules

- Use datasource variables for portability.
- Use scoped variables such as cluster, namespace, service, job, instance, tenant.
- Avoid high-cardinality variables such as request ID, trace ID, user ID, session ID, pod UID, container ID, raw URL.
- Use cascading variables when environments are large.
- Preserve variable names used in queries, links, repeats, and alert annotations.
- Use `refresh: On dashboard load` or `On time range change` based on the variable query.
- Use `All` only when the query language and panel intent support it.

### Multi-value and All handling

Grafana formats multi-value variables differently per datasource.

- Prometheus/InfluxDB variables are interpolated as regex-like alternations.
- Elasticsearch variables are formatted for Lucene.
- A custom All value changes how Grafana sends the All selection.

For Prometheus and Loki label matchers:

```promql
# Single-value variable
{job="$job"}

# Multi-value or All variable
{job=~"$job"}
```

A custom `allValue: ".*"` is useful when the variable is always used in regex matcher context (`=~`). Do not apply it blindly to every datasource or every variable. If you leave the custom All value blank, Grafana can format all selected values according to the datasource.

### Prometheus variables

For new dashboards, prefer typed Prometheus variable query types where possible:

- Label names
- Label values
- Metrics
- Query result
- Series query

Classic `label_values(metric, label)` still appears in many dashboards, but Grafana documents it as the deprecated classic query editor syntax. Use it only for compatibility or when generating older-style dashboards deliberately.

Use `query_result(...)` when the variable must depend on `$__range`, `$__range_s`, or query logic; otherwise label values/series queries are usually cheaper.

---

## PromQL quick reference

### Use `$__rate_interval`

For counters:

```promql
rate(http_requests_total[$__rate_interval])
increase(http_requests_total[$__rate_interval])
```

### Rate then join

```promql
sum by (projectID) (rate(builds_total[$__rate_interval]))
* on(projectID) group_left(projectName)
project_info{projectName=~"$project"}
```

### Histogram quantiles

```promql
histogram_quantile(
  0.95,
  sum by (le, job) (
    rate(http_request_duration_seconds_bucket[$__rate_interval])
  )
)
```

### Common mistakes

- `rate(metric * on(id) info[$__rate_interval])` is invalid. Join after `rate()`.
- Do not use exact matchers with multi-value variables.
- Do not join two high-cardinality vectors unless you know the cardinality.
- Do not use `histogram_quantile()` on summaries without bucket labels.
- Do not alert on highly volatile `irate()` unless there is a clear reason.

### PromQL patterns adopted from Grafana's official PromQL skill

- `rate()` and `increase()` require range vectors. In dashboards, prefer `$__rate_interval`; in hand-written fixed windows, the window should normally be at least 4x the scrape interval.
- Rate first, then aggregate. Do not aggregate raw counters and then try to rate the aggregate.
- Use `rate()` for dashboards and alerting. Use `irate()` only for volatile visual debugging where spike sensitivity matters.
- Classic histograms must preserve `le` inside the inner aggregation for `histogram_quantile()`.
- Native histograms use different syntax; verify Prometheus/Mimir support before generating native histogram panels.
- Use recording rules for expensive dashboard PromQL, repeated histogram quantiles, and SLO/error-budget calculations.
- For SLO panels, show numerator, denominator, success/error ratio, and burn-rate windows where possible.
- Use cardinality checks when a query is slow or a dashboard fan-outs too many series.

Read `references/promql-patterns.md` and `references/lgtm-stack-patterns.md` for more patterns.

---

## Mimir / Grafana Cloud Metrics guidance

Use this section when dashboards or alerts target Grafana Mimir, Grafana Cloud
Metrics, or another Prometheus-compatible long-term metrics backend.

Mimir behaves as a horizontally scalable, highly available, multi-tenant,
Prometheus-compatible metrics backend. Design dashboards and rules with tenant,
cardinality, query fan-out, and long-term storage cost in mind.

Rules:

- Treat `X-Scope-OrgID` / tenant identity as operationally important when present.
- Preserve tenant scoping in datasource provisioning, reverse proxies, and Alloy/Prometheus `remote_write`.
- Use recording rules for expensive or repeated dashboard queries.
- Prefer pre-aggregated rules for high-traffic overview dashboards.
- Watch active series, ingestion rate, query latency, compactor, ruler, Alertmanager, query-frontend, ingester, store-gateway, and object-store health.
- For Mimir dashboards, include tenant-level panels when multi-tenancy matters.
- Do not create unbounded global label discovery variables across all tenants.
- Prefer object-storage-backed production deployments; local filesystem examples are demo/development patterns.
- When troubleshooting slow queries, check query range, step, cardinality, query-frontend splitting/cache, store-gateway, and ingester pressure.

Prometheus remote_write / Alloy write examples are collector configuration, not
dashboard JSON. Keep them in provisioning/runbook files rather than embedding
secrets or endpoint credentials in dashboards.

---

## Loki / LogQL guidance

Start narrow, then parse.

```logql
{cluster=~"$cluster", namespace=~"$namespace", app=~"$app"}
|= "error"
| json
```

Rules:

- Filter by indexed labels first.
- Use line filters before expensive parsing.
- Use regex matchers for multi-value variables.
- Avoid extracting high-cardinality values as labels.
- Keep log line limits sane.
- Narrow time ranges for raw log panels.
- Prefer metric queries for trends.
- Use `| json`, `| logfmt`, `| pattern`, `| regexp`, or `| unpack` only after stream and line filtering where possible.
- Use `line_format` for readability in log panels, but avoid hiding fields needed for troubleshooting.
- Use `unwrap` only for numeric values extracted from logs, and validate duration/bytes conversions.
- Use `absent_over_time()` for absence alerts when missing logs indicate failure.
- Prefer Logs Drilldown/Explore for ad-hoc investigation; dashboards should contain curated log panels and log-derived metrics, not unlimited raw log search.

Metric query example:

```logql
sum by (app) (
  rate({namespace=~"$namespace", app=~"$app"} |= "error" [$__rate_interval])
)
```

Unwrapped numeric example:

```logql
quantile_over_time(
  0.95,
  {app=~"$app"} | logfmt | unwrap duration | duration_seconds [$__interval]
) by (app)
```

---

## Elasticsearch datasource guidance

Grafana’s standard Elasticsearch query editor uses Lucene query syntax.

Example Lucene query:

```lucene
tags:"ad" AND monitor.duration.us:>=1007601
```

Rules:

- Use uppercase `AND`, `OR`, `NOT` in Lucene queries.
- Do not assume Kibana KQL syntax works in Grafana’s Lucene editor.
- Use `.keyword` fields for terms aggregations when the source field is text.
- Avoid enabling fielddata on text fields unless deliberately accepting the memory cost.
- Set reasonable terms sizes and date histogram intervals.
- Use the OpenSearch datasource for OpenSearch/Amazon OpenSearch, not Elasticsearch.
- Verify ES|QL/DSL mode availability and maturity in the target Grafana version before using it in production dashboards.

---

## SQL datasource guidance

Rules:

- Bound time-series queries with Grafana time macros.
- Alias the time column as `time` where required.
- Return numeric values for time series.
- Use readable SQL aliases for table columns.
- Limit table queries.
- Avoid unindexed `SELECT DISTINCT` variable queries on huge tables.
- Never interpolate untrusted raw values into SQL.

Example:

```sql
SELECT
  date_trunc('minute', created_at) AS time,
  count(*) AS value
FROM events
WHERE $__timeFilter(created_at)
GROUP BY 1
ORDER BY 1;
```

---

## Tempo, tracing, and correlation

Use tracing guidance only when Tempo/tracing exists.

Good practices:

- Use trace-to-logs when logs contain trace IDs and Loki/another log datasource is configured.
- Use trace-to-metrics when service labels map from spans to Prometheus-compatible metrics.
- Use exemplars to navigate from metrics to traces where supported.
- Use TraceQL for trace searches only when Tempo supports it.
- Use Traces Drilldown/Explore for open-ended trace investigation.
- Use service graphs and span metrics when Tempo metrics-generator is enabled.
- Treat TraceQL metrics as version/feature-sensitive; verify support before relying on them for production dashboards or alerts.
- Do not invent span attributes; inspect actual trace/resource attributes.
- Keep span/trace high-cardinality labels out of dashboard-wide variables.

Useful TraceQL examples:

```traceql
{ status = error }
{ resource.service.name = "frontend" && duration > 1s }
{ span.http.status_code >= 500 }
{ kind = server } >> { status = error }
```

Correlation checklist:

- Metrics panel has exemplar support or data link to Tempo.
- Loki logs include trace ID and a derived/data link to Tempo.
- Tempo datasource links back to logs, metrics, and profiles where available.
- Span/resource attribute names match OpenTelemetry semantic conventions or actual observed data.

---

## Alloy / OpenTelemetry pipeline guidance

Use this section when the user asks for Grafana Alloy, OpenTelemetry Collector,
Prometheus scraping, Loki log shipping, Tempo trace ingestion, Pyroscope profiles,
or telemetry pipeline troubleshooting.

Think in pipelines:

```text
receive/source/discover -> process/relabel/transform/batch -> export/write
```

Rules:

- Identify every signal: metrics, logs, traces, profiles.
- Identify every input component, processor, and output component.
- Use component exports/references correctly, for example `forward_to = [component.receiver]`.
- Keep secrets in environment variables or secret stores, not in dashboards or committed examples.
- Use `sys.env()` for environment-sourced values in Alloy config examples.
- Preserve labels/resource attributes needed for dashboard variables and correlations.
- Drop or hash high-cardinality labels before ingestion when they are not needed.
- For Prometheus scraping, ensure scrape interval aligns with dashboard rate windows.
- For Loki pipelines, parse and label only stable low-cardinality fields.
- For Tempo pipelines, preserve `service.name`, trace IDs, and semantic attributes.
- Validate with Alloy's own logs, `/metrics`, target backend ingestion, and Grafana Explore before declaring dashboards correct.

Minimal Alloy pattern examples should be treated as starting points and adjusted to
the target deployment, security model, tenant headers, TLS, and backend URLs.

---

## Alerting guidance

Dashboard panels and alert rules are related but separate.

Grafana supports:

- Grafana-managed alert rules.
- Data source-managed rules for supported datasources/backends, for example Prometheus-compatible rule stores where configured.

### Alert design rules

Good alerts are:

- Actionable.
- Tied to user impact or clear operational risk.
- Scoped to the correct environment/service/team.
- Stable enough to avoid flapping.
- Routed by stable labels.
- Documented with annotations and runbooks.

### Labels vs annotations

Use labels for identity and routing:

```yaml
labels:
  severity: warning
  team: platform
  service: api
```

Use annotations for human context:

```yaml
annotations:
  summary: High API error rate
  description: Error rate is above threshold for the selected window.
  runbook_url: https://example/runbooks/api-errors
```

Do not put changing query values into labels. Query labels can create multiple alert instances; this is useful when intentional, but dangerous if uncontrolled.

### No Data / Error states

Always decide:

- No Data behavior.
- Error behavior.
- Pending period / `for` duration.
- Keep-firing/recovery behavior.
- Whether a missing series should resolve or alert.

### Linking alerts to panels

If linking a Grafana alert rule to a dashboard panel, preserve both `__dashboardUid__` and `__panelId__` annotations together.

---

## Provisioning, GitOps, and dashboard-as-code

### Provisioned dashboards

Rules:

- UI edits to provisioned dashboards are not automatically written back to the provisioning source.
- If provisioning files change later, Grafana can overwrite the database copy.
- Preserve `uid` to keep stable dashboard URLs.
- Avoid duplicate UIDs.
- Understand `allowUiUpdates`, `disableDeletion`, and provider paths.
- Do not store secrets in dashboards.
- Export JSON back to Git/source if UI edits are allowed.

### Git Sync

Rules:

- Decide and document the source of truth. For production automation, prefer reviewed Git changes as the source of truth; avoid mixing unmanaged UI edits with generated changes.
- Keep commits small and reviewable.
- Avoid mixing unmanaged UI edits with generated changes.
- Preserve folder structure and UIDs.
- Validate before committing generated JSON.
- Review Grafana 13 upgrade notes for early Git Sync/unified-storage migrations.

### Foundation SDK / Observability as Code

Rules:

- Edit the source builder code when the dashboard is generated from code.
- Use the SDK `build()`/equivalent output as validation.
- Wrap dashboards in Kubernetes-style API resources only when the target deployment workflow expects it.
- Prefer UID/name-based APIs over numeric IDs.
- Avoid generated JSON churn.

---

## Annotations, events, and deployment context

Use annotations to make timelines explainable. Good dashboards should show
important events such as deployments, incidents, maintenance, failovers, scaling
actions, or configuration changes when that context helps operators.

Rules:

- Preserve existing annotation queries and built-in annotations.
- Keep annotation queries bounded and cheap.
- Use datasource-specific annotation syntax: Loki annotations use LogQL, Prometheus annotations use PromQL, SQL annotations need time fields.
- Include deployment/version labels in annotation text when available.
- Do not overload every panel with noisy annotations; use them where timeline context is useful.

---

## Dashboard links and drilldowns

Use links to make dashboards actionable.

Good links pass:

- Time range.
- Relevant variables.
- Cluster/namespace/service/job/instance/tenant.
- Trace ID or log context when relevant.

Useful link types:

- Dashboard links.
- Panel links.
- Data links.
- Trace links.
- Log links.
- Runbook links.
- Incident/CMDB links.

Do not link operators into an unfiltered dashboard when a scoped link is possible.

---

## Debugging checklist

| Symptom | Likely cause | Fix |
|---|---|---|
| Empty panel | Wrong time range, variable, datasource, label, or transformation | Use Query Inspector, test without variables, inspect labels. |
| Prometheus “bad_data” | Invalid PromQL/vector matching/range function | Rate first, aggregate, then join. |
| Multi-value variable returns nothing | Exact matcher used with multi value | Use `=~` and check All formatting. |
| Table has no columns | Wrong query format or transformation order | Use table format/instant where needed, inspect dataframe. |
| Elasticsearch terms error | Aggregating on text field | Use `.keyword` or correct mapping. |
| Elasticsearch query fails | KQL used in Lucene editor | Rewrite as Lucene or enable correct query mode intentionally. |
| Loki query too large | Broad selector/time range/line limit | Add label filters, line filters, reduce range/limit. |
| Grafana 13 grouping looks wrong | Broken layout references, repeats, or visibility rules | Validate elements/layout/groupings. |
| Provisioned dashboard changes disappear | UI edits overwritten by provisioning source | Sync edits back to files/Git or change workflow. |
| Alert spam | High-cardinality labels or too-sensitive condition | Reduce dimensions, add pending window, route/group properly. |

---

## Validation checklist before returning work

### Dashboard JSON

- JSON parses.
- Root shape is preserved.
- UID/folder metadata preserved unless intentionally changed.
- Datasource refs preserved.
- Variables used by queries still exist.
- Panel IDs are unique.
- Classic `gridPos` is valid if classic JSON.
- v2/dynamic layout references are valid if schema-v2/dynamic dashboard.
- Transformations are ordered correctly.
- FieldConfig overrides target real fields/matchers.
- Units and thresholds are intentional.
- No unsupported or invented fields added.

### Queries

- PromQL uses `$__rate_interval` for rate/increase unless justified.
- Multi-value Prometheus/Loki variables use regex matchers.
- Elasticsearch uses Lucene syntax unless another mode is explicitly enabled.
- SQL queries are time-bounded and aliased.
- Loki queries filter labels before parsing.
- Mimir/Grafana Cloud Metrics queries are tenant-aware when relevant.
- Tempo/TraceQL panels use actual trace attributes and bounded time ranges.
- Alloy-related guidance separates collector config from dashboard JSON.
- Expensive joins/aggregations are justified.

### Alerting

- Labels are stable and route-friendly.
- Dynamic values are in annotations, not labels.
- No Data/Error behavior is intentional.
- Runbook links included where possible.
- Dashboard/panel links preserve `dashboardUid` and `panelId` together.

### Provisioning/GitOps

- UID stability preserved.
- File layout preserved.
- No secrets embedded.
- Generated JSON is deterministic.
- Source-of-truth workflow documented.

---

## Output format when modifying dashboards

Return:

1. Short summary of what changed.
2. Files changed.
3. Dashboard/schema type detected.
4. Datasources affected.
5. Variables affected.
6. Panels added/removed/changed.
7. Query changes.
8. Alerting changes.
9. Provisioning/GitOps impact.
10. Validation performed.
11. Assumptions and remaining risks.

---

## Common colour hex values

```text
Green   #1A9E3A
Yellow  #E0B400
Red     #F2495C
Orange  #FF9830
Blue    #5794F2
Gray    #808080
Purple  #B877D9
```

Use colour to communicate meaning, not decoration. Red/yellow/green should match operational severity.
