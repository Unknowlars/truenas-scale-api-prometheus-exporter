# Grafana V2 Resources, Dynamic Dashboards, Rows, and Tabs

Use this reference when editing dashboards that may use Grafana 13+ dynamic dashboard layouts, rows/tabs groupings, or the newer Kubernetes-style dashboard resource wrapper.

The safest rule is: **inspect the input/export shape first and preserve that shape unless the task explicitly asks for a migration.** Grafana has classic dashboard JSON, Kubernetes-style resource wrappers, and newer schema-aware dashboard models. They are related, but they are not interchangeable string templates.

---

## First identify the dashboard shape

| Shape | Common signs | Safe editing rule |
|---|---|---|
| Classic dashboard JSON | Top-level `panels`, `templating`, `annotations`, `schemaVersion`, `uid`, `title` | Preserve classic JSON. Use 24-column `gridPos`. Do not convert to v2 just because Grafana 13 exists. |
| Kubernetes-style dashboard resource | Top-level `apiVersion`, `kind: Dashboard`, `metadata`, `spec` | Preserve `apiVersion`, `kind`, `metadata.name`, labels/annotations, and `spec`. Edit the dashboard content under `spec` according to its actual shape. |
| Schema-aware/v2-style dashboard content | Structured `spec` with layout/grouping objects such as tabs/rows/custom grid, elements, variables, or schema-specific `kind`/`spec` blocks | Preserve unknown fields. Copy patterns from a target export from the same Grafana version. Validate against the target Grafana/API when possible. |

Do **not** assume `dashboard.grafana.app/v2` as the API version. Current Grafana examples for dashboard resources commonly use `dashboard.grafana.app/v1` or `v1alpha1` wrappers. The dashboard content inside `spec` can still use newer schema concepts, so the wrapper API version and the dashboard content schema are separate concerns.

---

## Dynamic dashboard and grouping concepts

Grafana 13+ dynamic dashboards support first-class groupings such as rows and tabs, plus layout features such as nested containers, repeats, conditional visibility, and grouping-level variables in supported versions/configurations.

Practical implications for an AI dashboard agent:

1. **Rows and tabs are not just visual separators.** They can affect layout, visibility, repeated sections, and variable scope.
2. **Do not flatten groupings accidentally.** Moving a panel out of a tab/row can change the operator workflow.
3. **Do not assume every dashboard should be converted to tabs.** Tabs are best when the dashboard has distinct workflows such as Overview, Capacity, Queries, Replication, Locks, Logs, Traces, and Admin.
4. **Preserve visibility/repeat rules.** If the input contains `repeat`, conditional visibility, group variables, or nested layouts, carry them forward unless the user asks for simplification.
5. **Use target exports as templates.** When possible, create or inspect one small tabbed dashboard from the target Grafana version and mirror its exact JSON/YAML shape.

---

## Classic grid rules still matter

For classic dashboards and classic panels embedded under a resource wrapper:

- Grafana classic grid layout is 24 columns wide.
- `gridPos.w` should be between `1` and `24`.
- `gridPos.x + gridPos.w` should not exceed `24`.
- Keep panel IDs unique and stable when editing existing dashboards.
- Preserve `uid`, datasource UIDs, variable names, links, annotations, transformations, field config, thresholds, mappings, and drilldowns.
- Avoid hardcoding `schemaVersion` or `pluginVersion`; preserve from the source export or omit optional generated fields when safe.

For schema-aware custom grids, only apply the classic 24-column checks when the actual target schema uses the classic/custom 24-column coordinate model.

---

## Kubernetes-style dashboard resource wrapper

A safe resource wrapper pattern looks like this conceptually:

```json
{
  "apiVersion": "dashboard.grafana.app/v1",
  "kind": "Dashboard",
  "metadata": {
    "name": "stable-dashboard-name"
  },
  "spec": {
    "title": "Example dashboard",
    "uid": "optional-classic-dashboard-uid-if-present-in-source",
    "panels": []
  }
}
```

Rules:

- Preserve the wrapper API version from the source or target export.
- Preserve `metadata.name`; in the newer `/apis/dashboard.grafana.app/...` API path this is the resource name used in URLs.
- Do not invent `metadata.uid`. If present, preserve it; otherwise let Grafana manage it.
- Preserve labels/annotations under `metadata`.
- Preserve the entire `spec` shape. Do not assume `spec.panels` or `spec.elements`; inspect the target export.
- Do not mix classic top-level fields with resource-wrapper fields at the same level.

---

## Tabs/rows migration workflow

Use this only when the user explicitly wants a dashboard reorganized into tabs or the input already uses tabs/rows.

1. **Inventory the source dashboard**
   - Dashboard title, uid, tags, timezone, time range, refresh.
   - Variables and datasource variables.
   - Panel IDs, titles, datasource references, targets, transformations, overrides.
   - Links, annotations, drilldowns, alert-panel links.
   - Existing rows/tabs or collapsed sections.

2. **Design the operator workflow**
   - Default/Overview tab first.
   - Troubleshooting tabs after overview.
   - Heavy or specialist tabs later.
   - Keep high-risk admin panels away from landing pages.

3. **Move panels without changing internals**
   - Preserve queries and datasource UIDs.
   - Preserve transformations and field config.
   - Preserve alert annotations linking dashboard/panel IDs.
   - Preserve panel IDs unless intentionally replacing panels.

4. **Validate references**
   - Every visible panel intended for the tabbed layout appears in exactly one visible place unless deliberate duplication is documented.
   - No unknown panel IDs are referenced by layouts.
   - No orphan panels are left behind unless intentionally hidden/library/external.
   - Rows/tabs preserve repeat/visibility/group variable semantics.

5. **Validate importability**
   - JSON/YAML parses.
   - UIDs are stable.
   - Datasource references are portable.
   - Query syntax matches datasource type.
   - Unknown schema fields were preserved.

---

## Recommended tab patterns

### Generic production service dashboard

1. **Overview** — health, SLOs, request rate, errors, latency, saturation.
2. **Golden Signals / RED** — rate, errors, duration by route/service/status.
3. **Resources / USE** — CPU, memory, disk, network, saturation.
4. **Dependencies** — upstream/downstream calls, database, cache, queue, external APIs.
5. **Logs** — Loki/Elasticsearch log panels and links to Explore/Logs Drilldown.
6. **Traces** — Tempo trace links, exemplars, service graphs/span metrics where available.
7. **Alerts / Runbooks** — alert status, alert links, runbook links, ownership.
8. **Collector / Data Quality** — scrape health, agent health, missing data, cardinality warnings.

### PostgreSQL dashboard

1. **Overview** — availability, connections, transactions, cache hit, replication summary, slow queries.
2. **Sessions & Locks** — active sessions, waiting/blocking, lock age, top blockers.
3. **Queries** — `pg_stat_statements`, latency, calls, rows, temp usage, shared block reads.
4. **Replication & WAL** — replication lag, slots, WAL generation, checkpoint behavior.
5. **Vacuum & Bloat** — vacuum/analyze age, dead tuples, table/index bloat if collected.
6. **Storage & IO** — database/table/index size, IO time, temp files, disk saturation.
7. **Config & Collector Health** — exporter up, scrape duration, enabled extensions, reset timestamps.

### Kubernetes / infrastructure dashboard

1. **Overview** — cluster/node health, workload status, error budget, top issues.
2. **Nodes** — CPU, memory, disk, pressure, network.
3. **Workloads** — deployments, pods, restarts, OOM kills, saturation.
4. **Networking** — ingress, DNS, service latency, errors.
5. **Storage** — PVC usage, IO, filesystem pressure.
6. **Logs / Events** — Loki logs, Kubernetes events.
7. **Traces** — Tempo links or service maps where instrumentation exists.
8. **Collector Health** — Prometheus/Alloy/agent health and scrape quality.

---

## Safe builders and templates

Prefer one of these approaches:

### Best option: clone an existing target export

1. Create a tiny dashboard in the target Grafana version with the desired layout.
2. Export it using the same API/file path you will later import with.
3. Use the exported panel/layout objects as templates.
4. Replace only titles, IDs, positions, targets, and datasource references.
5. Preserve unknown fields.

### Acceptable option: classic dashboard builders

For classic dashboards, use deterministic helper functions for panels and `gridPos`. Keep `schemaVersion` and `pluginVersion` configurable or omitted.

### Risky option: hand-written schema-v2 objects

Only hand-write schema-v2 layout objects when you have a target schema example. Do not invent `kind`, `group`, `version`, `spec`, or layout field names from memory.

---

## Verified v2beta1 shapes (import-tested July 2026)

The shapes below were taken from the generated types in the Grafana repo
(`packages/grafana-schema/src/schema/dashboard/v2beta1/types.spec.gen.ts`)
and verified end-to-end: a ~300-panel dashboard generated with them imported
cleanly into a Grafana 13 instance via **Dashboards → New → Import** and
rendered a native tab bar. Treat them as a reliable starting template, but
still diff against the target Grafana's own export when the version differs.

### Resource wrapper

```json
{
  "apiVersion": "dashboard.grafana.app/v2beta1",
  "kind": "Dashboard",
  "metadata": {"name": "stable-url-slug"},
  "spec": { ... }
}
```

`metadata.name` is the URL slug; re-importing the same name updates the same
dashboard (delete + import, or `PUT
/apis/dashboard.grafana.app/v2beta1/namespaces/default/dashboards/<name>`).

### spec — required top-level fields

```json
{
  "title": "...", "description": "...", "tags": [],
  "cursorSync": "Crosshair",            // "Off" | "Crosshair" | "Tooltip"
  "editable": true, "preload": false, "liveNow": false,
  "annotations": [ /* AnnotationQueryKind */ ],
  "links": [ /* DashboardLink */ ],
  "timeSettings": {
    "timezone": "browser", "from": "now-6h", "to": "now",
    "autoRefresh": "30s", "autoRefreshIntervals": ["10s", "30s", "1m"],
    "hideTimepicker": false, "fiscalYearStartMonth": 0
  },
  "variables": [ /* VariableKind — see below */ ],
  "elements": { "panel-1": { /* PanelKind */ } },
  "layout": { /* GridLayout | RowsLayout | AutoGridLayout | TabsLayout */ }
}
```

Panels live in the `elements` map (key convention `panel-<id>`); layouts
reference them by key via `ElementReference`. Every element must be
referenced exactly once.

### Tabs / rows / grid layout kinds

```json
{"kind": "TabsLayout", "spec": {"tabs": [
  {"kind": "TabsLayoutTab", "spec": {
     "title": "🏠 Overview",
     "layout": {"kind": "RowsLayout", "spec": {"rows": [
        {"kind": "RowsLayoutRow", "spec": {
           "title": "Section", "collapse": false, "hideHeader": false,
           "layout": {"kind": "GridLayout", "spec": {"items": [
              {"kind": "GridLayoutItem", "spec": {
                 "x": 0, "y": 0, "width": 12, "height": 8,
                 "element": {"kind": "ElementReference", "name": "panel-1"}}}
           ]}}}}
     ]}}}}
]}}
```

- Grid coordinates use `width`/`height` (NOT classic `w`/`h`), 24 columns.
- Each row/tab grid restarts `y` at 0 — rebase when moving classic panels.
- Rows nest inside tabs (and vice versa) up to 3 levels; rows support
  `collapse`, `hideHeader`, `fillScreen`, `repeat`, `conditionalRendering`.
- Per-item `conditionalRendering` exists only on AutoGridLayout items, not
  GridLayout items.

### Panel element

```json
{"kind": "Panel", "spec": {
  "id": 1, "title": "...", "description": "", "links": [],
  "data": {"kind": "QueryGroup", "spec": {
    "queries": [
      {"kind": "PanelQuery", "spec": {
        "refId": "A", "hidden": false,
        "query": {"kind": "DataQuery", "group": "prometheus", "version": "v0",
                  "datasource": {"name": "${DS_PROMETHEUS}"},
                  "spec": {"expr": "up", "legendFormat": "",
                            "format": "table", "instant": true}}}}
    ],
    "transformations": [
      {"kind": "organize", "spec": {"id": "organize", "options": { ... }}}
    ],
    "queryOptions": {}
  }},
  "vizConfig": {"kind": "VizConfig", "group": "timeseries", "version": "",
    "spec": {"options": { ... }, "fieldConfig": {"defaults": { ... },
                                                   "overrides": []}}}
}}
```

- `vizConfig.group` = plugin id (`stat`, `timeseries`, `bargauge`, `table`,
  `piechart`, `state-timeline`, …); `version` may be empty.
- `options`/`fieldConfig` bodies are identical to classic panel JSON — a
  classic→v2 converter can copy them through unchanged.
- Classic `targets[i]` fields (minus `datasource`, `refId`, `hide`) map into
  `query.spec`; `refId`/`hidden` move to the `PanelQuery` spec.
- `TransformationKind.kind` duplicates the transformation id.

### Variables

```json
{"kind": "DatasourceVariable", "spec": {
  "name": "DS_PROMETHEUS", "label": "Datasource", "pluginId": "prometheus",
  "refresh": "onDashboardLoad", "regex": "", "current": {"text": "", "value": ""},
  "options": [], "multi": false, "includeAll": false, "hide": "dontHide",
  "skipUrlSync": false, "allowCustomValue": true}}

{"kind": "QueryVariable", "spec": {
  "name": "pool", "label": "Pool",
  "current": {"text": ["All"], "value": ["$__all"]},
  "hide": "dontHide", "refresh": "onTimeRangeChanged", "skipUrlSync": false,
  "query": {"kind": "DataQuery", "group": "prometheus", "version": "v0",
            "datasource": {"name": "${DS_PROMETHEUS}"},
            "spec": {"query": "label_values(metric, pool)", "refId": "Q"}},
  "regex": "", "sort": "naturalAsc", "definition": "label_values(metric, pool)",
  "options": [], "multi": true, "includeAll": true, "allValue": ".*",
  "allowCustomValue": true}}
```

Enums are strings, not classic integers: `refresh` is
`never|onDashboardLoad|onTimeRangeChanged`, `hide` is
`dontHide|hideLabel|hideVariable|inControlsMenu`, `sort` is
`disabled|alphabeticalAsc|naturalAsc|…`.

### Built-in annotations layer

```json
{"kind": "AnnotationQuery", "spec": {
  "builtIn": true, "enable": true, "hide": true,
  "iconColor": "rgba(0, 211, 255, 1)", "name": "Annotations & Alerts",
  "query": {"kind": "DataQuery", "group": "grafana", "version": "v0", "spec": {}}}}
```

---

## Validation helpers

These helpers are intentionally conservative. Extend them based on the actual schema shape in the target export.

```python
def collect_classic_panels(dashboard):
    """Return classic panels from either a classic dashboard or resource wrapper."""
    root = dashboard.get("spec", dashboard)
    return root.get("panels", []) or []


def validate_classic_grid(dashboard):
    panels = collect_classic_panels(dashboard)
    ids = []
    for panel in panels:
        pid = panel.get("id")
        if pid is not None:
            ids.append(pid)
        grid = panel.get("gridPos")
        if not grid:
            continue
        x = grid.get("x", 0)
        w = grid.get("w", 0)
        assert 1 <= w <= 24, f"Panel {pid} width outside 1..24: {w}"
        assert 0 <= x <= 23, f"Panel {pid} x outside 0..23: {x}"
        assert x + w <= 24, f"Panel {pid} exceeds 24-column grid: x={x}, w={w}"
    assert len(ids) == len(set(ids)), "Duplicate classic panel IDs"


def walk_unknown_safe_layout(layout, found_refs=None):
    """Collect element/panel references from a schema-aware layout without assuming a full schema."""
    if found_refs is None:
        found_refs = []
    if isinstance(layout, dict):
        for key in ("element", "elementRef", "panel", "panelRef", "panelId"):
            if key in layout:
                found_refs.append(layout[key])
        for value in layout.values():
            walk_unknown_safe_layout(value, found_refs)
    elif isinstance(layout, list):
        for item in layout:
            walk_unknown_safe_layout(item, found_refs)
    return found_refs
```

Do not make validation delete unknown fields. Validation should report risks and preserve the source unless the user explicitly asks for cleanup.

---

## Anti-patterns

Avoid:

- Converting classic JSON to v2/resource format without a user request.
- Assuming `apiVersion: dashboard.grafana.app/v2`.
- Assuming `spec.elements` exists in every resource-wrapped dashboard.
- Hardcoding Grafana `schemaVersion`, panel `pluginVersion`, or visualization schema `version` values.
- Rebuilding panels from scratch when a safe move/reorder would work.
- Dropping transformations, field overrides, mappings, thresholds, links, annotations, or alert links.
- Changing datasource UIDs to local names.
- Replacing UID-stable dashboards with new UIDs.
- Flattening tabs/rows and losing visibility/repeat semantics.
- Treating Git Sync as magic conflict resolution. Keep review, source-of-truth, and rollback practices explicit.

---

## Migration checklist

Before returning an edited dashboard package, verify:

- [ ] JSON/YAML parses.
- [ ] The original shape is preserved unless migration was requested.
- [ ] `uid`/`metadata.name`/folder identifiers are preserved as appropriate.
- [ ] Datasource UIDs and datasource variables are preserved.
- [ ] No duplicate panel IDs in classic panels.
- [ ] Classic grid positions remain within 24 columns.
- [ ] Rows/tabs preserve intended grouping, ordering, repeat, and visibility behavior.
- [ ] Panel queries still use datasource-correct syntax.
- [ ] Transformations, field config, overrides, thresholds, mappings, links, and annotations were preserved.
- [ ] Alert rule links, if present, preserve both dashboard UID and panel ID annotations.
- [ ] Git/provisioning behavior is documented when the dashboard is provisioned or synced.
- [ ] Version-sensitive assumptions are called out instead of hidden in generated JSON.
