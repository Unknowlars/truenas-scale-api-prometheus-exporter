# Transforms — Complete Reference

Transforms run **in sequence** — each step receives the output of the previous.
Use "Table view" toggle in Grafana UI to debug intermediate state.
Apply `_tf = lambda id, opts=None: {"id": id, "options": opts or {}}` for brevity.

---

## organize — Rename / Hide / Reorder Columns

The most-used transform. Apply to nearly every table.

```python
{"id": "organize", "options": {
    "excludeByName": {
        "Time": True, "Value": True, "__name__": True,
        "instance": True, "job": True,
        "projectID": True, "buildDefinitionID": True
    },
    "renameByName": {
        "pullrequestID":   "PR ID",
        "creator":         "Author",
        "isDraft":         "Draft?",
        "voteStatus":      "Votes",
        "sourceBranch":    "Source Branch",
        "targetBranch":    "Target Branch",
        "agentPoolName":   "Pool",
        "buildDefinitionName": "Pipeline"
    },
    "indexByName": {          # optional: set column order (0-based)
        "PR ID": 0, "Title": 1, "Author": 2, "Votes": 3
    }
}}
```

---

## labelsToFields — Pivot Label Values Into Columns

Turns each Prometheus series (differentiated by a label value) into a column.
**Required as first step for any barchart from Prometheus data.**

```python
{"id": "labelsToFields", "options": {
    "mode": "columns",   # "columns" = each label value becomes a column
                         # "rows"    = keeps label key-value pairs as rows
    "source": "labels"   # always "labels" for Prometheus
}}
```

**Before:** 3 time series with label `creator=Alice`, `creator=Bob`, `creator=Carol`
**After:** one wide table — columns `Time | Alice | Bob | Carol` with values

---

## reduce — Collapse Time Series to Single Value

Collapses the time dimension. Use **after** `labelsToFields` for bar charts.

```python
{"id": "reduce", "options": {
    "reducers": ["lastNotNull"],  # see below for all options
    "mode": "reduceFields"        # default — "seriesToRows" = different shape
}}
```

**Reducer options:**
`lastNotNull`, `last`, `first`, `firstNotNull`, `mean`, `sum`, `max`, `min`,
`count`, `range`, `delta`, `step`, `allIsNull`, `allIsZero`,
`changeCount`, `distinctCount`, `diffperc`, `variance`, `stdDev`

---

## sortBy — Sort Rows by Column

```python
{"id": "sortBy", "options": {
    "fields": [
        {"displayName": "Open PRs", "desc": True},   # primary (descending)
        {"displayName": "Author",   "desc": False},  # secondary (ascending)
    ]
}}
```

---

## filterByValue — Filter Rows by Condition

```python
{"id": "filterByValue", "options": {
    "filters": [
        {
            "fieldName": "age_days",
            "config": {
                "id": "greater",      # operators below
                "value": {"value": 7}
            }
        },
        {
            "fieldName": "Status",
            "config": {
                "id": "equal",
                "value": {"value": "failed"}
            }
        }
    ],
    "type": "include",   # "include" keeps matching rows; "exclude" removes them
    "match": "all"       # "all" = AND all conditions; "any" = OR
}}
```

**Operators:** `equal`, `notEqual`, `greater`, `greaterOrEqual`, `less`,
`lessOrEqual`, `regex`, `between`, `isEmpty`, `isNotEmpty`

---

## groupBy — Aggregate Like SQL GROUP BY

```python
{"id": "groupBy", "options": {
    "fields": {
        "status": {
            "operation": "groupby",      # field to group on
            "aggregations": []
        },
        "request_count": {
            "operation": "aggregate",
            "aggregations": ["sum"]      # reducers: sum, mean, min, max, count, last
        },
        "response_time": {
            "operation": "aggregate",
            "aggregations": ["mean", "max"]   # multiple calcs per field
        }
    }
}}
```

---

## calculateField — Derive New Columns

**Binary math between two fields:**
```python
{"id": "calculateField", "options": {
    "mode": "binary",
    "alias": "Success Rate",
    "binary": {
        "left": "succeeded",
        "right": "total",
        "operator": "/"    # "+", "-", "*", "/", "**", "%"
    },
    "replace": False   # True = replace input fields with result
}}
```

**Reduce across fields in a row:**
```python
{"id": "calculateField", "options": {
    "mode": "reduceRow",
    "alias": "Total",
    "reduce": {"reducer": "sum"},   # same reducers as reduce transform
    "replace": False
}}
```

**Window / cumulative (Grafana 11+):**
```python
{"id": "calculateField", "options": {
    "mode": "window",
    "alias": "Running Total",
    "window": {"windowAlignment": "trailing", "reducer": "sum"},
    "replace": False
}}
```

**Chain: derive ratio then convert to %:**
```python
transforms=[
    {"id":"calculateField","options":{"mode":"binary","alias":"Success Rate",
        "binary":{"left":"succeeded","right":"total","operator":"/"}}},
    {"id":"calculateField","options":{"mode":"binary","alias":"Success %",
        "binary":{"left":"Success Rate","right":"100","operator":"*"}}},
    {"id":"organize","options":{"excludeByName":{"Success Rate":True}}}
]
```

---

## merge — Combine Multiple Queries Into One Table

Takes results from multiple refIds and merges matching rows (on shared field values).

```python
{"id": "merge", "options": {}}
```

**Setup:** each target gets a different refId + `"format":"table"` + `"instant":True`:
```python
targets=[
    {"expr":"query_a","refId":"A","format":"table","instant":True},
    {"expr":"query_b","refId":"B","format":"table","instant":True},
],
transforms=[
    {"id":"merge","options":{}},
    {"id":"organize","options":{...}}
]
```

---

## joinByField — SQL-style JOIN on a Shared Field

More precise than merge — join only where a specific field matches.

```python
{"id": "joinByField", "options": {
    "byField": "service_name",
    "mode": "outer"    # "outer" | "inner"
}}
```

---

## convertFieldType — Change Column Data Type

```python
{"id": "convertFieldType", "options": {
    "conversions": [
        {"fieldName": "Build ID",    "destinationType": "number"},
        {"fieldName": "Created",     "destinationType": "time",
         "dateFormat": "YYYY-MM-DD HH:mm:ss"},
        {"fieldName": "Is Active",   "destinationType": "boolean"},
        {"fieldName": "Status Code", "destinationType": "enum"}
    ]
}}
```

---

## formatString — Transform String Presentation

```python
{"id": "formatString", "options": {
    "outputFormat": "upperCase",   # "upperCase" | "lowerCase" | "titleCase"
                                   # "trim" | "substring"
    "fieldName": "Status"
}}
```

**substring options:**
```python
{"id": "formatString", "options": {
    "outputFormat": "substring",
    "fieldName": "Branch",
    "substringStart": 11,    # skip "refs/heads/"
    "substringEnd": 0        # 0 = to end
}}
```

---

## renameByRegex — Bulk Rename All Fields Matching Pattern

```python
{"id": "renameByRegex", "options": {
    "regex": "refs/heads/(.*)",
    "renamePattern": "$1"    # capture group → output; strips prefix
}}
# "refs/heads/feature/my-branch" → "feature/my-branch"
```

---

## limit — Restrict Number of Rows

```python
{"id": "limit", "options": {"limitField": 10}}    # keep first 10
{"id": "limit", "options": {"limitField": -5}}    # keep last 5
```

---

## partitionByValues — Split Table Into N Sub-Tables

Splits one table into N frames based on distinct values of a field.
Useful when building per-category bar charts.

```python
{"id": "partitionByValues", "options": {
    "fields": ["priority"],     # field(s) to split on
    "keepFields": True          # keep the partition field in output
}}
```

---

## labelsToFields (rows mode) — Key-Value Pair Rows

```python
{"id": "labelsToFields", "options": {
    "mode": "rows",
    "source": "labels"
}}
```
Produces rows like: `{Field: "creator", Value: "alice"}` — useful for label inspection panels.

---

## series to rows — One Row Per Series

Adds a `Metric` column identifying the source series.
Useful for comparing multiple series in a single table.

```python
{"id": "seriesToRows", "options": {}}
```

---

## concatenateFields — Combine All Frames Horizontally

Takes all frames and combines them into one wide frame. Unlike merge (which
aligns on shared values), this just puts all columns side by side.

```python
{"id": "concatenateFields", "options": {}}
```

---

## filterFieldsByName — Keep/Remove Columns by Name Pattern

```python
{"id": "filterFieldsByName", "options": {
    "include": {"names": ["Time", "Value", "projectName"]},
    # OR:
    "exclude": {"pattern": "^_.*"}   # regex to exclude matching field names
}}
```

---

## filterByRefId — Keep Only Results From Specific Query

```python
{"id": "filterByRefId", "options": {"include": "A"}}
```
Useful when you have queries A+B but only want A's data in this panel.

---

## prepareTimeSeries — Convert Between Wide and Long Formats

Multi-frame time series data format conversion. Use when a viz panel
expects a different shape than what the datasource returns.

```python
{"id": "prepareTimeSeries", "options": {
    "format": "wideToLong"   # "wideToLong" | "longToWide" | "multi"
}}
```

---

## groupToNestedTable — Hierarchical Grouped Table (GA in Grafana 11)

```python
{"id": "groupToNestedTable", "options": {
    "fields": {
        "region": {
            "operation": "groupby",
            "aggregations": []
        },
        "server_type": {
            "operation": "groupby",
            "aggregations": []
        },
        "error_count": {
            "operation": "aggregate",
            "aggregations": ["sum"]
        }
    }
}}
```

---

## histogram (transform) — Build Histogram From Values

Different from the histogram panel type — this transform computes bucket
distribution from a field and returns histogram data.

```python
{"id": "histogram", "options": {
    "bucketSize": {"type": "auto"},   # or {"type": "count", "value": 10}
    "bucketOffset": 0,
    "combine": False,
    "fillValues": False
}}
```

---

## Debugging Transform Chains

1. **Click "Table view"** icon (top right of panel editor) to see raw data
   after all transforms run. Toggle on/off to compare before/after.
2. **Check intermediate state** by temporarily removing transforms from the
   bottom up — find which step is breaking the data.
3. **Empty output after reduce** — check that `labelsToFields` ran first and
   produced columns, not that you still have raw time series rows.
4. **sortBy not working** — field display name must exactly match the column
   header as shown in table view (after renames from organize).
5. **filterByValue not filtering** — check `convertFieldType` ran first if
   filtering a numeric field that arrived as a string.

---

## Complete Chain Examples

### Bar chart: ranked list from Prometheus labels
```python
transforms=[
    {"id":"labelsToFields","options":{"mode":"columns","source":"labels"}},
    {"id":"reduce",         "options":{"reducers":["lastNotNull"]}},
    {"id":"organize",       "options":{
        "excludeByName":{"Time":True},
        "renameByName":{"lastNotNull":"Open PRs","creator":"Author"}
    }},
    {"id":"sortBy","options":{"fields":[{"desc":True,"displayName":"Open PRs"}]}}
]
```

### Table: stale items with age filter and sort
```python
transforms=[
    {"id":"organize","options":{
        "excludeByName":{"__name__":True,"instance":True,"job":True},
        "renameByName":{"Value":"Age (seconds)","pullrequestID":"PR ID"}
    }},
    {"id":"convertFieldType","options":{"conversions":[
        {"fieldName":"Age (seconds)","destinationType":"number"}
    ]}},
    {"id":"filterByValue","options":{
        "filters":[{"fieldName":"Age (seconds)",
                    "config":{"id":"greater","value":{"value":604800}}}],
        "type":"include","match":"all"
    }},
    {"id":"sortBy","options":{"fields":[{"desc":False,"displayName":"Age (seconds)"}]}}
]
```

### Table: merge two queries + derive ratio column
```python
transforms=[
    {"id":"merge","options":{}},
    {"id":"calculateField","options":{
        "mode":"binary","alias":"Success Rate",
        "binary":{"left":"succeeded","right":"total","operator":"/"}
    }},
    {"id":"calculateField","options":{
        "mode":"binary","alias":"Success %",
        "binary":{"left":"Success Rate","right":"100","operator":"*"}
    }},
    {"id":"organize","options":{
        "excludeByName":{"Success Rate":True,"Time":True},
        "renameByName":{"succeeded":"Passed","total":"Total","Success %":"Pass Rate %"}
    }},
    {"id":"sortBy","options":{"fields":[{"desc":True,"displayName":"Pass Rate %"}]}}
]
```

### Multi-query table with join
```python
transforms=[
    {"id":"joinByField","options":{"byField":"service_name","mode":"outer"}},
    {"id":"organize","options":{
        "excludeByName":{"Time":True},
        "renameByName":{
            "Value #A":"Request Count",
            "Value #B":"Error Count",
            "Value #C":"Avg Latency (ms)"
        }
    }},
    {"id":"calculateField","options":{
        "mode":"binary","alias":"Error Rate %",
        "binary":{"left":"Error Count","right":"Request Count","operator":"/"}
    }}
]
```
