# Panel Types — Full Builder Reference

> Second-pass version note: these builders are classic dashboard JSON examples. Do not hardcode Grafana `pluginVersion` from these examples into every dashboard. Preserve the value exported by the target Grafana instance, set `TARGET_GRAFANA_PLUGIN_VERSION` deliberately, or remove the key if it is not required by your workflow.

```python
TARGET_GRAFANA_PLUGIN_VERSION = "13.0.0"  # replace with target export/version, or remove pluginVersion keys
```

All builders assume `DS` and `copy` are already imported (see SKILL.md boilerplate).
Every builder returns a complete panel dict ready to append to `panels`.

---

## stat

```python
def stat(id, title, expr, x, y, w, h,
         unit="short", legend="Value", desc="",
         thresholds=None, mappings=None,
         graph=False,         # True = area sparkline behind number
         percent_change=False # Grafana 10.3+ percent delta badge
         ):
    steps = thresholds or [{"color": "blue", "value": 0}]
    opts = {
        "colorMode": "background",   # "background" | "value" | "none"
        "graphMode": "area" if graph else "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
        "textMode": "auto",
        "wideLayout": True,
    }
    if percent_change:
        opts["showPercentChange"] = True
        opts["percentChangeColorMode"] = "inverted"  # green=up | "standard"=red=up
    return {
        "type": "stat", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": [tgt(expr, legend)],
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": mappings or [],
                "thresholds": {"mode": "absolute", "steps": steps},
                "unit": unit
            },
            "overrides": []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": opts,
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**Threshold recipes:**
```python
# Traffic light (higher=better):
[{"color":"red","value":0}, {"color":"yellow","value":70}, {"color":"green","value":90}]
# Inverse (lower=better):
[{"color":"green","value":0}, {"color":"yellow","value":15}, {"color":"red","value":30}]
# Capacity warning:
[{"color":"green","value":0}, {"color":"yellow","value":0.6}, {"color":"red","value":0.85}]
# Single accent colour:
[{"color":"blue","value":0}]
```

**Status badge mappings:**
```python
mappings=[
    {"type":"value","options":{"0":{"color":"green","text":"✅ OK",   "index":0}}},
    {"type":"value","options":{"1":{"color":"red",  "text":"❌ Error","index":1}}},
    # Range:
    {"type":"range","options":{"from":0,"to":50,"result":{"color":"red","text":"Low","index":0}}},
    # Null:
    {"type":"special","options":{"match":"null","result":{"color":"gray","text":"No data"}}},
]
```

---

## timeseries

```python
def ts(id, title, targets, x, y, w, h,
       unit="short", calcs=None, stacked=False, bars=False,
       fill=15, desc="", overrides=None, transforms=None):
    custom = {
        "drawStyle": "bars" if bars else "line",
        "lineInterpolation": "smooth",   # "linear" | "smooth" | "stepAfter"
        "lineWidth": 2,
        "fillOpacity": fill,
        "gradientMode": "opacity",       # "none" | "opacity" | "hue" | "scheme"
        "showPoints": "never" if bars else "auto",
        "spanNulls": False,
        "stacking": {"group": "A", "mode": "normal" if stacked else "none"},
        "barAlignment": 0, "barWidthFactor": 0.6,
        "thresholdsStyle": {"mode": "off"},
        "scaleDistribution": {"type": "linear"},
        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
    }
    return {
        "type": "timeseries", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": custom, "mappings": [], "unit": unit,
                "thresholds": {"mode":"absolute","steps":[{"color":"green","value":0}]}
            },
            "overrides": overrides or []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "legend": {
                "calcs": calcs or ["lastNotNull"],
                "displayMode": "table",   # "list" | "table" | "hidden"
                "placement": "bottom",    # "bottom" | "right"
                "showLegend": True
            },
            "tooltip": {"hideZeros": False, "mode": "multi", "sort": "desc"}
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**Useful legend calcs:** `lastNotNull`, `mean`, `max`, `min`, `sum`, `count`,
`range`, `delta`, `first`, `last`

**Series colour override (pin a series to a fixed colour):**
```python
overrides=[
    {"matcher":{"id":"byName","options":"✅ Succeeded"},
     "properties":[{"id":"color","value":{"fixedColor":"#1a9e3a","mode":"fixed"}}]},
    {"matcher":{"id":"byName","options":"❌ Failed"},
     "properties":[{"id":"color","value":{"fixedColor":"#F2495C","mode":"fixed"}}]},
]
```

---

## bargauge

```python
def bargauge(id, title, targets, x, y, w, h,
             unit="short", min=0, max=None,
             thresholds=None, desc="",
             orientation="horizontal",   # "horizontal" | "vertical" | "auto"
             transforms=None):
    steps = thresholds or [
        {"color":"green","value":0},
        {"color":"yellow","value":0.6},
        {"color":"red","value":0.85}
    ]
    fd = {"color":{"mode":"thresholds"},"mappings":[],"min":min,
          "thresholds":{"mode":"absolute","steps":steps},"unit":unit}
    if max is not None: fd["max"] = max
    return {
        "type": "bargauge", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {"defaults": fd, "overrides": []},
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "displayMode": "gradient",   # "basic" | "lcd" | "gradient"
            "orientation": orientation,
            "namePlacement": "auto",
            "valueMode": "color",
            "showUnfilled": True,
            "sizing": "auto",
            "minVizHeight": 16, "maxVizHeight": 300, "minVizWidth": 8,
            "reduceOptions": {"calcs":["lastNotNull"],"fields":"","values":False},
            "legend": {"calcs":[],"displayMode":"list","placement":"bottom","showLegend":False}
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**topk pattern for bargauge rankings:**
```promql
topk(10,
  avg by(projectID, buildDefinitionID)(duration_sum / duration_count)
  * on(buildDefinitionID, projectID) group_left(buildDefinitionName) build_def_info
  * on(projectID) group_left(projectName) project_info{projectName=~"$project"}
)
```
legendFormat: `"{{projectName}} / {{buildDefinitionName}}"`

---

## table

```python
def table(id, title, targets, x, y, w, h,
          desc="", overrides=None, sort_col=None, sort_desc=True,
          transforms=None, footer=None):
    return {
        "type": "table", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "align": "auto",
                    "cellOptions": {"type": "auto"},
                    "filterable": True,       # per-column filter UI
                    "footer": {"reducers": []},
                    "inspect": False
                },
                "mappings": [],
                "thresholds": {"mode":"absolute","steps":[{"color":"green","value":0}]}
            },
            "overrides": overrides or []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "cellHeight": "sm",   # "sm" | "md" | "lg"
            "showHeader": True,
            "footer": footer or {"show": False, "reducer": ["sum"], "fields": ""},
            "sortBy": [{"desc": sort_desc, "displayName": sort_col}] if sort_col else []
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**Common target format for current-state Prometheus tables:**
```python
{"datasource": DS, "expr": "my_metric", "refId": "A",
 "format": "table", "instant": True}
```

`format: "table"` is usually needed when the Prometheus datasource should return tabular data. `instant: True` is often appropriate for inventory/current-state tables, but do not force it for tables that intentionally show time-range rows or trend data.

**Cell override recipes:**
```python
# Coloured background:
{"matcher":{"id":"byName","options":"Status"},"properties":[
    {"id":"custom.cellOptions","value":{"type":"color-background"}},
    {"id":"mappings","value":[
        {"type":"value","options":{"succeeded":{"color":"#1a9e3a","text":"✅ Succeeded"}}},
        {"type":"value","options":{"failed":   {"color":"#F2495C","text":"❌ Failed"}}},
    ]}
]},
# Coloured text only:
{"matcher":{"id":"byName","options":"Vote"},"properties":[
    {"id":"custom.cellOptions","value":{"type":"color-text"}},
    {"id":"mappings","value":[...]}
]},
# Clickable URL:
{"matcher":{"id":"byName","options":"URL"},"properties":[
    {"id":"links","value":[{"title":"Open","url":"${__value.text}","targetBlank":True}]}
]},
# Sparkline in cell:
{"matcher":{"id":"byName","options":"Trend"},"properties":[
    {"id":"custom.cellOptions","value":{"type":"sparkline"}}
]},
# Threshold-coloured number:
{"matcher":{"id":"byName","options":"Open PRs"},"properties":[
    {"id":"custom.displayMode","value":"color-background"},
    {"id":"thresholds","value":{"mode":"absolute","steps":[
        {"color":"green","value":0},{"color":"yellow","value":5},{"color":"red","value":10}
    ]}}
]},
```

---

## piechart

```python
def piechart(id, title, targets, x, y, w, h,
             desc="", overrides=None, transforms=None):
    return {
        "type": "piechart", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {"hideFrom": {"legend":False,"tooltip":False,"viz":False}},
                "mappings": []
            },
            "overrides": overrides or []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "pieType": "donut",   # "donut" | "pie"
            "sort": "desc",
            "legend": {"displayMode":"table","placement":"right",
                       "showLegend":True,"values":["value","percent"]},
            "reduceOptions": {"calcs":["lastNotNull"],"fields":"","values":False},
            "tooltip": {"hideZeros":False,"mode":"multi","sort":"none"}
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**Multiple instant-query targets (one slice each):**
```python
targets=[
    tgt('count(metric{status="ok"})',     "OK",     "A"),
    tgt('count(metric{status="failed"})', "Failed", "B"),
    tgt('count(metric{status="warn"})',   "Warn",   "C"),
]
# Pin colours via overrides on series names:
overrides=[
    {"matcher":{"id":"byName","options":"OK"},    "properties":[{"id":"color","value":{"fixedColor":"#1a9e3a","mode":"fixed"}}]},
    {"matcher":{"id":"byName","options":"Failed"},"properties":[{"id":"color","value":{"fixedColor":"#F2495C","mode":"fixed"}}]},
]
```

---

## barchart

```python
def barchart(id, title, targets, x, y, w, h,
             unit="short", desc="", xField=None,
             orientation="auto",     # "auto" | "horizontal" | "vertical"
             stacking="none",        # "none" | "normal" | "percent"
             overrides=None, transforms=None, legend_placement="bottom"):
    return {
        "type": "barchart", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "fillOpacity": 80, "gradientMode": "none", "lineWidth": 1,
                    "axisBorderShow": False, "axisColorMode": "text",
                    "axisPlacement": "auto",
                    "scaleDistribution": {"type": "linear"},
                    "thresholdsStyle": {"mode": "off"},
                    "hideFrom": {"legend":False,"tooltip":False,"viz":False}
                },
                "mappings": [], "unit": unit,
                "thresholds": {"mode":"absolute","steps":[{"color":"green","value":0}]}
            },
            "overrides": overrides or []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "barRadius": 0.05, "barWidth": 0.7, "fullHighlight": False,
            "groupWidth": 0.7,
            "legend": {"displayMode":"list","placement":legend_placement,"showLegend":True},
            "orientation": orientation, "stacking": stacking,
            "tooltip": {"hideZeros":False,"mode":"multi","sort":"desc"},
            "xField": xField,
            "xTickLabelRotation": -45, "xTickLabelSpacing": 100
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**Required transform chain for Prometheus → barchart:**
```python
transforms=[
    {"id":"labelsToFields","options":{"mode":"columns","source":"labels"}},
    {"id":"reduce",         "options":{"reducers":["lastNotNull"]}},
    {"id":"organize",       "options":{
        "excludeByName":{"Time":True},
        "renameByName":{"lastNotNull":"Count","creator":"Author"}
    }},
    {"id":"sortBy","options":{"fields":[{"desc":True,"displayName":"Count"}]}}
]
```

---

## histogram

```python
def histogram_panel(id, title, targets, x, y, w, h,
                    unit="s", desc="", fill_opacity=80, transforms=None):
    return {
        "type": "histogram", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {"fillOpacity":fill_opacity,"gradientMode":"none","lineWidth":1,
                           "hideFrom":{"legend":False,"tooltip":False,"viz":False}},
                "unit": unit
            },
            "overrides": []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "bucketSize": "auto",   # or integer
            "combine": False,       # True = merge all series into one histogram
            "fillOpacity": fill_opacity, "gradientMode": "none",
            "legend": {"displayMode":"list","placement":"bottom","showLegend":True},
            "tooltip": {"hideZeros":False,"mode":"single","sort":"none"}
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**PR age distribution query (value = age in seconds, histogram buckets it):**
```promql
time() - pullrequest_status{type="created"}
  * on(projectID) group_left(projectName) project_info{projectName=~"$project"}
```
unit = `"s"` — Grafana auto-formats buckets as seconds.

---

## state_timeline

```python
def state_timeline(id, title, targets, x, y, w, h,
                   desc="", mappings=None, overrides=None,
                   transforms=None, row_height=0.8, fill_opacity=70):
    return {
        "type": "state-timeline", "id": id, "title": title, "description": desc,
        "datasource": copy.deepcopy(DS), "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {
                    "fillOpacity": fill_opacity, "lineWidth": 0,
                    "hideFrom": {"legend":False,"tooltip":False,"viz":False}
                },
                "mappings": mappings or [],
                "thresholds": {"mode":"absolute","steps":[{"color":"green","value":0}]}
            },
            "overrides": overrides or []
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "alignValue": "left",
            "mergeValues": True,      # merge consecutive identical states
            "rowHeight": row_height,  # 0–1
            "showValue": "auto",      # "always" | "never" | "auto"
            "legend": {"displayMode":"list","placement":"bottom","showLegend":True},
            "tooltip": {"hideZeros":False,"mode":"single","sort":"none"}
        },
        "transformations": transforms or [],
        "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
    }
```

**Numeric fraction → colour states:**
```python
overrides=[{"matcher":{"id":"byType","options":"number"},"properties":[
    {"id":"thresholds","value":{"mode":"absolute","steps":[
        {"color":"red","value":0},{"color":"yellow","value":0.5},{"color":"green","value":0.9}
    ]}},
    {"id":"unit","value":"percentunit"},
    {"id":"min","value":0}, {"id":"max","value":1}
]}]
```

**Difference from status-history:**
- `state-timeline` merges consecutive identical values → shows duration of states
- `status-history` shows each sample independently → no merging

---

## gauge (radial)

```python
{
    "type": "gauge", "id": id, "title": title,
    "datasource": copy.deepcopy(DS), "targets": targets,
    "fieldConfig": {
        "defaults": {
            "color": {"mode": "thresholds"}, "mappings": [],
            "min": 0, "max": 1,
            "thresholds": {"mode":"absolute","steps":[
                {"color":"green","value":0},
                {"color":"yellow","value":0.6},
                {"color":"red","value":0.85}
            ]},
            "unit": "percentunit"
        }, "overrides": []
    },
    "gridPos": {"x":x,"y":y,"w":w,"h":h},
    "options": {
        "minVizHeight": 75, "minVizWidth": 75, "orientation": "auto",
        "reduceOptions": {"calcs":["lastNotNull"],"fields":"","values":False},
        "showThresholdLabels": False, "showThresholdMarkers": True, "sizing": "auto"
    },
    "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
}
```

---

## text (markdown)

```python
{
    "type": "text", "id": id, "title": "",
    "gridPos": {"x":x,"y":y,"w":w,"h":h},
    "options": {
        "mode": "markdown",   # "markdown" | "html" | "code"
        "content": """## Section Title\n\nDescribe what this row shows and who it is for.\n\n> **Tip:** Use `$project` to filter.""",
        "code": {"language":"plaintext","showLineNumbers":False,"showMiniMap":False}
    },
    "pluginVersion": TARGET_GRAFANA_PLUGIN_VERSION
}
```

---

## row

```python
def row(id, title, y, collapsed=False, panels=None):
    return {
        "type": "row", "id": id, "title": title,
        "collapsed": collapsed,
        "panels": panels or [],   # only populated when collapsed=True
        "gridPos": {"x": 0, "y": y, "w": 24, "h": 1}
    }
```

**Collapsed row — child panels go INSIDE the row, not the top-level list:**
```python
child1 = table(401, "Detail Table", ..., x=0, y=y+1, w=24, h=10)
child2 = ts(402, "Detail Trend",   ..., x=0, y=y+11, w=12, h=8)
panels.append(row(400, "Detail Section", y, collapsed=True, panels=[child1, child2]))
y += 1   # row only adds 1 to y; child panels are hidden
```

---

## Common Units

```
short        → auto-scales (k, M, G)
percent      → appends %
percentunit  → 0.0–1.0 input displayed as 0–100%
s            → seconds
ms           → milliseconds
µs           → microseconds
dtdurations  → "3 days 4 hours" human duration
reqps        → requests/sec
bytes        → IEC auto-suffix (KiB, MiB)
decbytes     → SI auto-suffix (KB, MB)
bps          → bits/sec
```

Full list: https://grafana.com/docs/grafana/latest/panels-visualizations/configure-standard-options/#unit
