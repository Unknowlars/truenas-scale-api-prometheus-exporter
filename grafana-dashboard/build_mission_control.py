#!/usr/bin/env python3
"""Build the TrueNAS Mission Control dashboard (Grafana v2beta1, native tabs).

Reads the classic operations-center-dashboard.json (source of truth for
queries), converts every panel to the Grafana dashboard schema v2beta1
element shape, reorganizes the 19 classic rows into 12 tabs, applies a
consistent visual-design pass, and prepends a hand-built hero Overview tab.

Schema shapes follow grafana/grafana
packages/grafana-schema/src/schema/dashboard/v2beta1/types.spec.gen.ts.

Usage: python3 build_mission_control.py
Output: truenas-mission-control.json (Kubernetes-style resource wrapper).
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "operations-center-dashboard.json"
OUT = HERE / "truenas-mission-control.json"
sys.path.insert(0, str(HERE.parent / "scripts"))

# One semantic palette and one set of shared query fragments for both
# dashboards: the classic generator owns them, Mission Control reuses them.
import generate_truenas_dashboard as classic_gen  # noqa: E402

DS_VAR = "${DS_PROMETHEUS}"

GREEN = classic_gen.OK
RED = classic_gen.CRIT
ORANGE = classic_gen.WARN
YELLOW = classic_gen.WARN
BLUE = classic_gen.INFO
PURPLE = classic_gen.ACCENT
GREY = classic_gen.NEUTRAL
NA = classic_gen.NO_VALUE

# New hero/overview panels get IDs above every classic panel ID.
NEW_ID_START = 400
_next_id = NEW_ID_START


def next_id() -> int:
    global _next_id
    _next_id += 1
    return _next_id


# ---------------------------------------------------------------------------
# v2beta1 building blocks
# ---------------------------------------------------------------------------

def data_query(spec: dict) -> dict:
    return {
        "kind": "DataQuery",
        "group": "prometheus",
        "version": "v0",
        "datasource": {"name": DS_VAR},
        "spec": spec,
    }


def panel_query(expr: str, ref: str = "A", legend: str = "",
                instant: bool = False, fmt: str | None = None,
                hidden: bool = False) -> dict:
    spec: dict = {"expr": expr, "legendFormat": legend}
    if fmt:
        spec["format"] = fmt
    if instant:
        spec["instant"] = True
    return {
        "kind": "PanelQuery",
        "spec": {"refId": ref, "hidden": hidden, "query": data_query(spec)},
    }


def panel_element(pid: int, ptype: str, title: str, description: str,
                  queries: list, options: dict, field_defaults: dict,
                  overrides: list | None = None,
                  transformations: list | None = None) -> dict:
    return {
        "kind": "Panel",
        "spec": {
            "id": pid,
            "title": title,
            "description": description,
            "links": [],
            "data": {
                "kind": "QueryGroup",
                "spec": {
                    "queries": queries,
                    "transformations": transformations or [],
                    "queryOptions": {},
                },
            },
            "vizConfig": {
                "kind": "VizConfig",
                "group": ptype,
                "version": "",
                "spec": {
                    "options": options,
                    "fieldConfig": {
                        "defaults": field_defaults,
                        "overrides": overrides or [],
                    },
                },
            },
        },
    }


def grid_item(x: int, y: int, w: int, h: int, name: str) -> dict:
    assert 1 <= w <= 24 and x >= 0 and x + w <= 24 and y >= 0 and h >= 1, (
        f"invalid grid slot for {name}: x={x} y={y} w={w} h={h}")
    return {
        "kind": "GridLayoutItem",
        "spec": {"x": x, "y": y, "width": w, "height": h,
                 "element": {"kind": "ElementReference", "name": name}},
    }


def grid_layout(items: list) -> dict:
    return {"kind": "GridLayout", "spec": {"items": items}}


def rows_layout(rows: list) -> dict:
    return {"kind": "RowsLayout", "spec": {"rows": rows}}


def layout_row(layout: dict, title: str = "", collapse: bool = False,
               hide_header: bool = False) -> dict:
    spec: dict = {"layout": layout}
    if title:
        spec["title"] = title
    if collapse:
        spec["collapse"] = True
    if hide_header:
        spec["hideHeader"] = True
    return {"kind": "RowsLayoutRow", "spec": spec}


def tab(title: str, layout: dict) -> dict:
    return {"kind": "TabsLayoutTab", "spec": {"title": title, "layout": layout}}


# ---------------------------------------------------------------------------
# Field-config helpers (visual identity)
# ---------------------------------------------------------------------------

def thresholds(*steps) -> dict:
    """steps: (color, value) pairs; first value should be None (base)."""
    return {"mode": "absolute",
            "steps": [{"color": c, "value": v} for c, v in steps]}


def value_map(mapping: dict) -> dict:
    options = {}
    for i, (raw, (text, color)) in enumerate(mapping.items()):
        options[str(raw)] = {"text": text, "color": color, "index": i}
    return {"type": "value", "options": options}


def stat_options(color_mode: str = "background_solid", graph: str = "none",
                 text_mode: str = "auto") -> dict:
    return {
        "colorMode": color_mode,
        "graphMode": graph,
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
        "textMode": text_mode,
        "wideLayout": True,
    }


TS_CUSTOM_BASE = {
    "drawStyle": "line",
    "lineInterpolation": "smooth",
    "lineWidth": 2,
    "fillOpacity": 18,
    "gradientMode": "opacity",
    "showPoints": "never",
    "pointSize": 5,
    "spanNulls": 900000,
    "axisSoftMin": 0,
    "stacking": {"mode": "none", "group": "A"},
    "thresholdsStyle": {"mode": "off"},
    "scaleDistribution": {"type": "linear"},
    "hideFrom": {"legend": False, "tooltip": False, "viz": False},
}

TS_OPTIONS = {
    "legend": {"displayMode": "list", "placement": "bottom",
               "showLegend": True, "calcs": []},
    "tooltip": {"mode": "multi", "sort": "desc"},
}


def ts_custom(**over) -> dict:
    c = copy.deepcopy(TS_CUSTOM_BASE)
    c.update(over)
    return c


def color_override(name: str, color: str, by_regex: bool = False) -> dict:
    return {
        "matcher": {"id": "byRegexp" if by_regex else "byName", "options": name},
        "properties": [{"id": "color",
                        "value": {"mode": "fixed", "fixedColor": color}}],
    }


# ---------------------------------------------------------------------------
# Classic -> v2 conversion
# ---------------------------------------------------------------------------

def convert_target(t: dict, idx: int) -> dict:
    spec = {k: v for k, v in t.items()
            if k not in ("datasource", "refId", "hide")}
    return {
        "kind": "PanelQuery",
        "spec": {
            "refId": t.get("refId") or chr(ord("A") + idx),
            "hidden": bool(t.get("hide", False)),
            "query": data_query(spec),
        },
    }


NAN_STAT_MAPPING = copy.deepcopy(classic_gen.NA_MAPPINGS[1])


def restyle_classic(p: dict) -> dict:
    """Light-touch consistency pass. Never changes query semantics."""
    p = copy.deepcopy(p)
    fc = p.setdefault("fieldConfig", {}).setdefault("defaults", {})
    if p["type"] == "timeseries":
        custom = fc.setdefault("custom", {})
        if 0 < custom.get("fillOpacity", 0) < 10:
            custom["fillOpacity"] = 15
        if custom.get("gradientMode", "none") == "none":
            custom["gradientMode"] = "opacity"
        if custom.get("lineWidth", 1) < 2:
            custom["lineWidth"] = 2
        custom.setdefault("axisSoftMin", 0)
        # The exporter's realtime metrics flap to NaN between samples and the
        # scrape itself is slow; bridge gaps up to 15 minutes so trends read
        # as lines instead of dots. Real outages (scrape down) still show.
        custom["spanNulls"] = 900000
        opts = p.setdefault("options", {})
        tooltip = opts.setdefault("tooltip", {})
        if tooltip.get("mode") in (None, "single"):
            tooltip["mode"] = "multi"
            tooltip["sort"] = "desc"
    if p["type"] == "stat":
        opts = p.setdefault("options", {})
        # Field names fall back to the raw PromQL expression; never print it.
        if opts.get("textMode") == "value_and_name":
            opts["textMode"] = "auto"
        mappings = fc.setdefault("mappings", [])
        # ~50 config metrics are emitted as NaN on some systems; show a quiet
        # n/a instead of a giant "NaN".
        if not any(m.get("type") == "special" for m in mappings):
            mappings.append(copy.deepcopy(NAN_STAT_MAPPING))
        # Plain inventory counts (single-step threshold, no value mappings)
        # become quiet colored numbers; solid backgrounds stay reserved for
        # panels that actually signal health.
        steps = [st for st in fc.get("thresholds", {}).get("steps", [])
                 if st.get("color") not in (GREY, "#808080")]
        value_maps = [m for m in mappings if m.get("type") != "special"]
        if len(steps) <= 1 and not value_maps and \
                opts.get("colorMode") in ("background", "background_solid"):
            opts["colorMode"] = "value"
    if p["type"] == "bargauge":
        opts = p.setdefault("options", {})
        if opts.get("displayMode") in ("basic", "lcd"):
            opts["displayMode"] = "gradient"
    return p


# ---------------------------------------------------------------------------
# Targeted panel patches (screenshot-driven corrections)
# ---------------------------------------------------------------------------

# Wrap gauge selectors as (selector >= 0) in timeseries queries so NaN samples
# (which the exporter emits between realtime updates) are dropped instead of
# breaking lines. The lookahead must reject `[` (selector already inside a
# range vector), `{` and name characters (both mean backtracking shortened
# the match and would split a selector or metric name in half).
NAN_GUARD_RE = re.compile(
    r"(truenas_[a-z0-9_]+(?:\{[^}]*\})?)(?![a-z0-9_]|\s*[\[{])")


def guard_nan(expr: str) -> str:
    return NAN_GUARD_RE.sub(r"(\1 >= 0)", expr)


def _set_color(p, mode):
    p["fieldConfig"]["defaults"]["color"] = {"mode": mode}


def _patch_policy_bool_column(overrides, column, one, zero):
    """Replace a 0/1 color-background column with quiet colored text that
    highlights only the exceptional state."""
    for o in overrides:
        if o.get("matcher", {}).get("options") != column:
            continue
        for prop in o["properties"]:
            if prop["id"] == "custom.cellOptions":
                prop["value"] = {"type": "auto"}
            elif prop["id"] == "mappings":
                prop["value"] = [value_map({1: one, 0: zero})]


def _patch_policy_table(p):
    ov = p["fieldConfig"]["overrides"]
    _patch_policy_bool_column(ov, "Readonly", ("Yes", ORANGE), ("No", "text"))
    _patch_policy_bool_column(ov, "Atime", ("On", BLUE), ("Off", "text"))
    _patch_policy_bool_column(ov, "Exec", ("Yes", "text"), ("No", ORANGE))
    _patch_policy_bool_column(ov, "Key Loaded", ("Yes", GREEN), ("No", "text"))
    _patch_policy_bool_column(ov, "Locked", ("Locked", RED), ("No", "text"))


APP_STATE_OVERRIDES = [
    color_override("RUNNING", GREEN),
    color_override("STOPPED", ORANGE),
    color_override("EXITED", "#808080"),
    color_override("DEPLOYING", BLUE),
    color_override("CRASHED", RED),
]


def _patch_app_states(p):
    p["fieldConfig"]["overrides"].extend(copy.deepcopy(APP_STATE_OVERRIDES))


def _patch_load_avg(p):
    p["targets"] = [t for t in p["targets"]
                    if "host_cpu_cores" not in t["expr"]]


def _patch_oldest_snap(p):
    p["targets"][0]["expr"] = (
        'time() - (truenas_snapshot_oldest_timestamp_seconds'
        '{instance=~"$instance"} > 0)')
    p["fieldConfig"]["defaults"]["noValue"] = "n/a"


PANEL_PATCHES = {
    ("Apps & Docker", "App State Distribution"): _patch_app_states,
    ("Apps & Docker", "App Container State Distribution"): _patch_app_states,
    ("Apps & Docker", "Top Apps by CPU"): lambda p: (
        p["fieldConfig"]["defaults"].update(decimals=2)),
    ("Apps & Docker", "Top Apps by Memory"): lambda p: _set_color(
        p, "continuous-blues"),
    ("CPU & Load", "Load Average"): _patch_load_avg,
    ("Storage & Pools", "Oldest Snap"): _patch_oldest_snap,
    ("Dataset Deep-Dive", "Dataset Policy Detail"): _patch_policy_table,
    ("Dataset Deep-Dive", "Dataset Compression Ratio"): lambda p: (
        p["fieldConfig"]["defaults"].update(min=1)),
    ("Dataset Deep-Dive", "Top Datasets by Used Bytes"): lambda p: _set_color(
        p, "continuous-blues"),
    ("Dataset Deep-Dive", "Dataset Snapshot Counts"): lambda p: _set_color(
        p, "continuous-blues"),
    ("Dataset Deep-Dive", "Datasets Using Snapshot Space"): lambda p: _set_color(
        p, "continuous-blues"),
    ("Dataset Deep-Dive", "Datasets with Reservations"): lambda p: _set_color(
        p, "continuous-blues"),
    ("Dataset Deep-Dive", "Datasets by Available Space (Bottom 15)"):
        lambda p: _set_color(p, "continuous-RdYlGr"),
}


def convert_panel(p: dict, row_title: str = "") -> tuple[str, dict]:
    p = restyle_classic(p)
    patch = PANEL_PATCHES.get((row_title, p.get("title", "")))
    if patch:
        patch(p)
    question = QUESTION_TITLES.get((row_title, p.get("title", "")))
    if question:
        p["title"] = question
    name = f"panel-{p['id']}"
    queries = [convert_target(t, i) for i, t in enumerate(p.get("targets", []))]
    transformations = [{"kind": tr["id"], "spec": tr}
                       for tr in p.get("transformations", [])]
    element = {
        "kind": "Panel",
        "spec": {
            "id": p["id"],
            "title": p.get("title", ""),
            "description": p.get("description", ""),
            "links": [],
            "data": {
                "kind": "QueryGroup",
                "spec": {
                    "queries": queries,
                    "transformations": transformations,
                    "queryOptions": {},
                },
            },
            "vizConfig": {
                "kind": "VizConfig",
                "group": p["type"],
                "version": "",
                "spec": {
                    "options": p.get("options", {}),
                    "fieldConfig": p.get(
                        "fieldConfig", {"defaults": {}, "overrides": []}),
                },
            },
        },
    }
    return name, element


# ---------------------------------------------------------------------------
# Live-metric detection (panels for never-emitted metrics get tucked away)
# ---------------------------------------------------------------------------

METRIC_NAME_RE = re.compile(r"truenas_[a-z0-9_]+")

# Metrics that are only emitted while something is happening (running jobs,
# API errors, expiring certificates). Their panels are empty most of the time
# by design and must stay visible — an operator needs them exactly when they
# start returning data.
CONDITIONAL_METRIC_PREFIXES = (
    "truenas_job_",
    "truenas_api_call_errors_total",
    "truenas_collector_errors_total",
    "truenas_certificate_",
)


def panel_is_dead(p: dict, live: set | None) -> bool:
    """True when every truenas_* metric the panel queries has zero samples."""
    if live is None:
        return False
    names = set()
    for t in p.get("targets", []):
        names.update(METRIC_NAME_RE.findall(t.get("expr", "")))
    if any(n.startswith(CONDITIONAL_METRIC_PREFIXES) for n in names):
        return False
    return bool(names) and not (names & live)


def pack_grid(panels: list, elements: dict) -> dict:
    """Flow-pack panels (used for the relocated dead panels): keep sizes,
    place left-to-right, wrap at 24 columns."""
    items, x, y, row_h = [], 0, 0, 0
    for p in sorted(panels, key=lambda q: (q["gridPos"]["y"], q["gridPos"]["x"])):
        name, element = convert_panel(p)
        assert name not in elements, f"duplicate element name {name}"
        elements[name] = element
        gp = p["gridPos"]
        if x + gp["w"] > 24:
            x, y, row_h = 0, y + row_h, 0
        items.append(grid_item(x, y, gp["w"], gp["h"], name))
        x += gp["w"]
        row_h = max(row_h, gp["h"])
    return grid_layout(items)


def classic_row_to_grid(panels: list, elements: dict, row_title: str = "",
                        dead_bucket: list | None = None,
                        live: set | None = None) -> dict:
    """Convert one classic row's inner panels to a v2 GridLayout,
    rebasing y so the grid starts at 0. Panels whose metrics are never
    emitted on this system are diverted into dead_bucket."""
    kept = []
    for p in panels:
        if dead_bucket is not None and panel_is_dead(p, live):
            dead_bucket.append(p)
        else:
            kept.append(p)
    if not kept:
        return grid_layout([])
    y0 = min(p["gridPos"]["y"] for p in kept)
    items = []
    for p in sorted(kept, key=lambda q: (q["gridPos"]["y"], q["gridPos"]["x"])):
        name, element = convert_panel(p, row_title)
        assert name not in elements, f"duplicate element name {name}"
        elements[name] = element
        gp = p["gridPos"]
        items.append(grid_item(gp["x"], gp["y"] - y0, gp["w"], gp["h"], name))
    return grid_layout(items)


# ---------------------------------------------------------------------------
# Hero Overview tab (hand built)
# ---------------------------------------------------------------------------

def apply_nan_guard(elements: dict) -> None:
    """Guard every timeseries query once, after all panels are assembled."""
    for element in elements.values():
        if element["spec"]["vizConfig"]["group"] != "timeseries":
            continue
        for q in element["spec"]["data"]["spec"]["queries"]:
            spec = q["spec"]["query"]["spec"]
            if "expr" in spec:
                spec["expr"] = guard_nan(spec["expr"])


# ---------------------------------------------------------------------------
# Mission Control hand-built content: hero Overview, Incident tab, helpers
# ---------------------------------------------------------------------------

DASH_UID = "truenas-mission-control"
INST = 'instance=~"$instance"'


def tab_slug(title: str) -> str:
    """Grafana slugifyForUrl(title): lowercase, drop non-word chars, spaces -> '-'."""
    return re.sub(r" +", "-", re.sub(r"[^\w ]+", "", title.lower()))


def tab_url(title: str, keep_vars: bool = True) -> str:
    vars_part = "&${__all_variables}" if keep_vars else "&${instance:queryparam}"
    return f"/d/{DASH_UID}?${{__url_time_range}}{vars_part}&dtab={tab_slug(title)}"


def steps(*pairs) -> dict:
    """(color, value) pairs -> thresholds with the shared neutral base, so a
    panel without data reads grey N/A instead of the first real colour."""
    return {"mode": "absolute", "steps": classic_gen.neutral_base(
        [{"color": c, "value": v} for c, v in pairs])}


def na_maps(mapping: dict | None = None) -> list:
    base = [value_map(mapping)] if mapping else []
    return classic_gen.with_na(base)


def mc_stat(title, expr, desc, *, unit="short", th=((BLUE, None),), mapping=None,
            graph="none", color_mode="background", decimals=None, link=None,
            text_mode="auto", no_value=NA, legend="", value_size=None):
    fd = {"unit": unit, "noValue": no_value, "mappings": na_maps(mapping),
          "thresholds": steps(*th), "color": {"mode": "thresholds"}}
    if decimals is not None:
        fd["decimals"] = decimals
    opts = stat_options(color_mode=color_mode, graph=graph, text_mode=text_mode)
    if value_size:
        opts["text"] = {"valueSize": value_size}
    el = panel_element(next_id(), "stat", title, desc,
                       [panel_query(expr, legend=legend)], opts, fd)
    if link:
        el["spec"]["links"] = [{"title": link[0], "url": link[1], "targetBlank": False}]
    return el


def check(label: str, expr: str) -> str:
    return f'label_replace({expr}, "check", "{label}", "", "")'


# Each component scores 0 (OK), 1 (attention) or 2 (action). The verdict is
# the worst score; the Health checks table lists every component so the
# verdict is never a black box. Absent components simply drop out; with no
# data at all the verdict is N/A (grey).
FULLEST_POOL = (f'max(100 * truenas_pool_allocated_bytes{{{INST}}} '
                f'/ (truenas_pool_size_bytes{{{INST}}} > 0))')
HOTTEST_DISK = f'max({classic_gen.DISK_TEMP.replace(chr(36) + "disk", ".*")})'
SCRAPE_AGE = f'(time() - max(truenas_last_scrape_timestamp_seconds{{{INST}}}))'
HEALTH_CHECKS = [
    ("Exporter reachable", f"2 * (1 - min(truenas_up{{{INST}}}))"),
    ("Middleware ready", f"2 * (1 - min(truenas_system_ready{{{INST}}}))"),
    ("All pools healthy", f"2 * (1 - min(truenas_pool_healthy{{{INST}}}))"),
    ("Boot pool healthy", f"2 * (1 - min(truenas_boot_pool_healthy{{{INST}}}))"),
    ("No outstanding alerts", f"clamp_max({classic_gen.OUTSTANDING_ALERTS}, 1)"),
    ("Pools below 80 % / 90 %", f"({FULLEST_POOL} > bool 80) + ({FULLEST_POOL} > bool 90)"),
    ("Disks below 45 / 55 °C", f"({HOTTEST_DISK} > bool 45) + ({HOTTEST_DISK} > bool 55)"),
    ("Data fresh (< 5 / 15 min)", f"({SCRAPE_AGE} > bool 300) + ({SCRAPE_AGE} > bool 900)"),
]
HEALTH_UNION = " or ".join(check(label, expr) for label, expr in HEALTH_CHECKS)
VERDICT = f"max({HEALTH_UNION})"
VERDICT_MAP = {0: ("✓  HEALTHY", GREEN), 1: ("⚠  ATTENTION", ORANGE), 2: ("✕  ACTION NEEDED", RED)}
CHECK_MAP = {0: ("✓ OK", GREEN), 1: ("⚠ Attention", ORANGE), 2: ("✕ Action", RED)}


def bars(title, desc, expr, legend, *, unit, th, mx=None, decimals=None, instant=True,
         no_value=NA, link=None, mode="gradient"):
    fd = {"unit": unit, "min": 0, "thresholds": steps(*th), "noValue": no_value,
          "mappings": na_maps(), "color": {"mode": "thresholds"}}
    if mx is not None:
        fd["max"] = mx
    if decimals is not None:
        fd["decimals"] = decimals
    el = panel_element(next_id(), "bargauge", title, desc,
                       [panel_query(expr, legend=legend, instant=instant)],
                       {"displayMode": mode, "orientation": "horizontal",
                        "valueMode": "text", "namePlacement": "top", "showUnfilled": True,
                        "minVizHeight": 30, "maxVizHeight": 36, "sizing": "manual",
                        "text": {"titleSize": 12, "valueSize": 14},
                        "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
                        "legend": {"showLegend": False}}, fd)
    if link:
        el["spec"]["links"] = [{"title": link[0], "url": link[1], "targetBlank": False}]
    return el


def ts(title, desc, queries, *, unit, overrides=None, mn=None, mx=None, stack=False,
       fill=18, no_value=NA):
    fd = {"unit": unit, "noValue": no_value,
          "custom": ts_custom(fillOpacity=fill,
                              stacking={"mode": "normal" if stack else "none", "group": "A"}),
          "color": {"mode": "palette-classic-by-name"},
          "thresholds": steps((GREEN, None))}
    if mn is not None:
        fd["min"] = mn
    if mx is not None:
        fd["max"] = mx
    return panel_element(next_id(), "timeseries", title, desc, queries,
                         copy.deepcopy(TS_OPTIONS), fd, overrides=overrides)


def state_table(title, desc, expr, columns, value_col, mapping, *, sort_desc=True,
                no_value=NA, unit="short"):
    """Instant table keeping only the named label columns plus Value."""
    keep = [label for label, _ in columns] + ["Value"]
    rename = dict(columns)
    rename["Value"] = value_col
    fd = {"noValue": no_value, "unit": unit, "mappings": [], "thresholds": steps((BLUE, None)),
          "custom": {"align": "auto", "cellOptions": {"type": "auto"}, "inspect": False}}
    overrides = [{"matcher": {"id": "byName", "options": value_col}, "properties": [
        {"id": "custom.cellOptions", "value": {"type": "color-text"}},
        {"id": "mappings", "value": [value_map(mapping)] if mapping else []},
        {"id": "custom.width", "value": 150}]}]
    transformations = [
        {"kind": "filterFieldsByName", "spec": {"id": "filterFieldsByName", "options": {
            "include": {"names": keep}}}},
        {"kind": "organize", "spec": {"id": "organize", "options": {
            "renameByName": rename,
            "indexByName": {name: i for i, name in enumerate(keep)}}}},
        {"kind": "sortBy", "spec": {"id": "sortBy", "options": {
            "fields": [{"displayName": value_col, "desc": sort_desc}]}}},
    ]
    return panel_element(next_id(), "table", title, desc,
                         [panel_query(expr, instant=True, fmt="table")],
                         {"showHeader": True, "cellHeight": "sm",
                          "footer": {"show": False, "reducer": ["sum"], "fields": ""}},
                         fd, overrides=overrides, transformations=transformations)


def add_to(elements: dict, items: list, x, y, w, h, element, repeat=None) -> None:
    name = f"panel-{element['spec']['id']}"
    assert name not in elements, f"duplicate element name {name}"
    elements[name] = element
    item = grid_item(x, y, w, h, name)
    if repeat:
        item["spec"]["repeat"] = repeat
    items.append(item)


def build_overview(elements: dict, snapshot_panels: list,
                   live: set | None, tabs_by_key: dict) -> dict:
    items: list = []
    add = lambda *a, **k: add_to(elements, items, *a, **k)  # noqa: E731
    inc = classic_gen

    # --- Hero: one verdict, eight linked sparkline tiles -----------------
    add(0, 0, 8, 8, mc_stat(
        "Is my NAS OK?",
        VERDICT,
        "Worst of: exporter reachability, middleware ready, pool and boot-pool health, outstanding "
        "(non-dismissed) alerts, fullest pool (80/90 %), hottest disk (45/55 °C) and data freshness "
        "(5/15 min). See 'Health checks' for which one fired. N/A means no data at all.",
        mapping=VERDICT_MAP, th=((GREEN, 0), (ORANGE, 1), (RED, 2)),
        link=("Open Incident view", tab_url(tabs_by_key["incident"])), value_size=44))

    tiles = [
        ("CPU", f"avg(truenas_cpu_usage_percent{{{INST}}})", "percent", 1,
         ((GREEN, 0), (ORANGE, 70), (RED, 90)), "compute", "Average CPU utilisation."),
        ("RAM excl. ARC", inc.RAM_EXCL_ARC, "percent", 1, inc.RAM_THRESHOLDS, "compute",
         inc.RAM_EXCL_ARC_DESC),
        ("Fullest pool", FULLEST_POOL, "percent", 1, ((GREEN, 0), (ORANGE, 80), (RED, 90)), "pools",
         "Used share of the fullest pool."),
        ("Hottest disk", HOTTEST_DISK, "celsius", 0, ((GREEN, 0), (ORANGE, 45), (RED, 55)), "disks",
         "Highest disk temperature; 0 °C readings (no sensor) are ignored."),
        ("Network", f"sum(truenas_network_rx_bytes_per_second{{{INST}}}) + "
                    f"sum(truenas_network_tx_bytes_per_second{{{INST}}})",
         "Bps", 1, ((BLUE, None),), "network", "Total receive + transmit across all interfaces."),
        ("Alerts", inc.OUTSTANDING_ALERTS, "short", 0, ((GREEN, 0), (ORANGE, 1), (RED, 5)), "alerts",
         "Outstanding alerts: alert_count minus dismissed (alert_count includes dismissed alerts)."),
        ("ARC hit", inc.rate_pct("demand_data_hits_per_second", "demand_data_accesses_per_second"),
         "percent", 1, ((RED, 0), (ORANGE, 70), (GREEN, 90)), "pools",
         "ZFS ARC demand-data hit rate from hits/s ÷ accesses/s."),
        ("Uptime", f"max(truenas_host_uptime_seconds{{{INST}}})", "s", 1, ((BLUE, None),), "exporter",
         "Host uptime."),
    ]
    for i, (title, expr, unit, dec, th, key, desc) in enumerate(tiles):
        th_pairs = [(t["color"], t["value"]) for t in th] if th and isinstance(th[0], dict) else th
        add(8 + (i % 4) * 4, (i // 4) * 4, 4, 4, mc_stat(
            title, expr, desc + f" Click to open {tabs_by_key[key].split(' ', 1)[1]}.", unit=unit,
            decimals=dec, th=th_pairs, graph="area", color_mode="value",
            link=(f"Open {tabs_by_key[key].split(' ', 1)[1]}", tab_url(tabs_by_key[key]))))

    # --- Why: checks, capacity, temperatures ------------------------------
    add(0, 8, 7, 11, state_table(
        "Health checks", "Each component of the verdict above. ✓ OK, ⚠ attention, ✕ action needed.",
        HEALTH_UNION, [("check", "Check")], "Status", CHECK_MAP))
    add(7, 8, 6, 11, bars(
        "Which pool fills first?", "Used share of each pool (allocated ÷ size).",
        f'sort_desc(100 * truenas_pool_allocated_bytes{{{INST}, pool=~"$pool"}} '
        f'/ (truenas_pool_size_bytes{{{INST}, pool=~"$pool"}} > 0))', "{{pool}}",
        unit="percent", th=((GREEN, 0), (ORANGE, 80), (RED, 90)), mx=100, decimals=1,
        link=("Open Pools & ZFS", tab_url(tabs_by_key["pools"]))))
    add(13, 8, 5, 11, bars(
        "Days until full", "Projection of the last 7 days' growth per pool. 'Not growing' when "
        "allocation is flat or shrinking; short history gives rough estimates.",
        f"sort({inc.DAYS_UNTIL_FULL})", "{{pool}}", unit="d", decimals=0, mx=365,
        th=((RED, 0), (ORANGE, 30), (GREEN, 90)), no_value="Not growing", mode="basic"))
    add(18, 8, 6, 11, bars(
        "Hottest disks", "Current temperature per disk, hottest first (0 °C = no sensor, hidden).",
        f"sort_desc(topk(8, {inc.DISK_TEMP}))", "{{disk}}", unit="celsius", decimals=0, mx=70,
        th=((GREEN, 0), (ORANGE, 45), (RED, 55)), mode="basic",
        link=("Open Disks & Hardware", tab_url(tabs_by_key["disks"]))))

    # --- Trends --------------------------------------------------------
    add(0, 19, 12, 8, ts(
        "Network throughput", "Receive (up) and transmit (down) per interface.",
        [panel_query(f'sum by (interface) (truenas_network_rx_bytes_per_second{{{INST}, interface=~"$interface"}})',
                     "A", "{{interface}} rx"),
         panel_query(f'-1 * sum by (interface) (truenas_network_tx_bytes_per_second{{{INST}, interface=~"$interface"}})',
                     "B", "{{interface}} tx")],
        unit="Bps"))
    add(12, 19, 12, 8, ts(
        "CPU and memory pressure",
        "CPU %, RAM used excluding the ZFS ARC, and RAM including ARC (dashed, informational).",
        [panel_query(f"avg(truenas_cpu_usage_percent{{{INST}}})", "A", "CPU"),
         panel_query(inc.RAM_EXCL_ARC, "B", "RAM excl. ARC"),
         panel_query(inc.RAM_INCL_ARC, "C", "RAM incl. ARC")],
        unit="percent", mn=0, mx=100, fill=10,
        overrides=[color_override("CPU", BLUE), color_override("RAM excl. ARC", GREEN),
                   {"matcher": {"id": "byName", "options": "RAM incl. ARC"}, "properties": [
                       {"id": "color", "value": {"mode": "fixed", "fixedColor": PURPLE}},
                       {"id": "custom.lineStyle", "value": {"fill": "dash", "dash": [8, 6]}},
                       {"id": "custom.fillOpacity", "value": 0}]}]))
    add(0, 27, 12, 8, ts(
        "Storage throughput", "Read (up) and write (down) across all disks. Uses per-disk series where the NAS "
        "reports them (25.10/26.0) and the aggregate disk=\"total\" series on TrueNAS 27.",
        [panel_query(f'sum({inc.disk_sel("truenas_disk_read_bytes_per_second").replace(chr(36) + "disk", ".*")})', "A", "read"),
         panel_query(f'-1 * sum({inc.disk_sel("truenas_disk_write_bytes_per_second").replace(chr(36) + "disk", ".*")})', "B", "write")],
        unit="Bps", overrides=[color_override("read", BLUE), color_override("write", PURPLE)]))
    add(12, 27, 6, 8, bars(
        "Which apps use the most memory?", "Top 8 apps by memory.",
        f'sort_desc(topk(8, truenas_app_memory_bytes{{{INST}, app=~"$app"}}))', "{{app}}",
        unit="bytes", th=((BLUE, None),), decimals=1, no_value="No apps",
        link=("Open Apps & Docker", tab_url(tabs_by_key["apps"]))))
    add(18, 27, 6, 8, bars(
        "What are the alerts about?", "Current alert classes (includes dismissed alerts).",
        f'sort_desc(sum by (klass) (truenas_alert_count_by_class{{{INST}}}))', "{{klass}}",
        unit="short", th=((BLUE, None),), decimals=0, no_value="No alerts",
        link=("Open Alerts & Jobs", tab_url(tabs_by_key["alerts"]))))

    hero_grid = grid_layout(items)
    dead: list = []
    snapshot_grid = classic_row_to_grid(snapshot_panels, elements,
                                        "System Overview", dead, live)
    rows = [
        layout_row(hero_grid, hide_header=True),
        layout_row(snapshot_grid, title="📋 System snapshot (all headline numbers)", collapse=True),
    ]
    if dead:
        rows.append(layout_row(pack_grid(dead, elements),
                               title="🚫 Not collected on this system",
                               collapse=True))
    return rows_layout(rows)


def attention(expr: str, kind: str, item_label: str, severity: int) -> str:
    """One 'needs attention' source: value = severity, labels kind + item."""
    inner = f'label_replace(0 * ({expr}) + {severity}, "kind", "{kind}", "", "")'
    if item_label:
        return f'label_replace({inner}, "item", "$1", "{item_label}", "(.*)")'
    return f'label_replace({inner}, "item", "—", "", "")'


def changed(expr: str, kind: str, item_label: str) -> str:
    inner = f'label_replace({expr}, "kind", "{kind}", "", "")'
    if item_label:
        return f'label_replace({inner}, "item", "$1", "{item_label}", "(.*)")'
    return f'label_replace({inner}, "item", "—", "", "")'


def build_incident(elements: dict, tabs_by_key: dict) -> dict:
    items: list = []
    add = lambda *a, **k: add_to(elements, items, *a, **k)  # noqa: E731
    inc = classic_gen
    z = inc.ZERO_IF_UP
    tiles = [
        ("Alerts", inc.OUTSTANDING_ALERTS, ((GREEN, 0), (ORANGE, 1), (RED, 5)),
         "Alerts not dismissed (alert_count − dismissed)."),
        ("Critical", f'sum(truenas_alert_count_by_level{{{INST}, level=~"CRITICAL|ALERT|EMERGENCY"}})' + z,
         ((GREEN, 0), (RED, 1)), "Critical-or-worse alerts (may include dismissed)."),
        ("Bad pools", f"count(truenas_pool_healthy{{{INST}}} == 0)" + z,
         ((GREEN, 0), (RED, 1)), "Pools whose healthy flag is false."),
        ("Svc stopped", f"count((truenas_service_enabled{{{INST}}} == 1) and on (instance, service) "
                             f"(truenas_service_running{{{INST}}} == 0))" + z,
         ((GREEN, 0), (ORANGE, 1)), "Services enabled at boot but not running."),
        ("API failing", f"count(truenas_api_call_success{{{INST}}} == 0)" + z,
         ((GREEN, 0), (ORANGE, 1), (RED, 5)), "API methods whose latest call failed."),
        ("Errors 1h", f"sum(increase(truenas_collector_errors_total{{{INST}}}[1h]))" + z,
         ((GREEN, 0), (ORANGE, 1), (RED, 5)), "Collector errors in the last hour."),
        ("Data age", SCRAPE_AGE, ((GREEN, 0), (ORANGE, 300), (RED, 900)),
         "Seconds since the exporter last completed a poll."),
        ("Realtime", f'min(truenas_event_stream_up{{{INST}, event="reporting.realtime"}})', ((RED, 0), (GREEN, 1)),
         "reporting.realtime subscription (feeds CPU, memory, network and ZFS ARC). Optional subscriptions such as "
         "virt.instance.metrics may be inactive on systems without that feature; see the Exporter tab."),
    ]
    for i, (title, expr, th, desc) in enumerate(tiles):
        unit = "s" if title == "Data age" else "short"
        mapping = {1: ("Up", GREEN), 0: ("Down", RED)} if title == "Realtime" else None
        add(i * 3, 0, 3, 4, mc_stat(title, expr, desc, unit=unit, th=th, decimals=0,
                                    mapping=mapping, graph="area" if not mapping else "none"))

    sources = " or ".join([
        attention(f"truenas_up{{{INST}}} == 0", "Exporter cannot reach TrueNAS", "instance", 2),
        attention(f"truenas_pool_healthy{{{INST}}} == 0", "Pool unhealthy", "pool", 2),
        attention(f"truenas_boot_pool_healthy{{{INST}}} == 0", "Boot pool unhealthy", "", 2),
        attention(f"truenas_directoryservices_fault_present{{{INST}}} == 1", "Directory service faulted", "service", 2),
        attention(f'truenas_app_state{{{INST}, state=~"CRASHED|ERROR"}}', "App crashed", "app", 2),
        attention(f"(truenas_service_enabled{{{INST}}} == 1) and on (instance, service) "
                  f"(truenas_service_running{{{INST}}} == 0)", "Service enabled but stopped", "service", 2),
        attention(f"truenas_pool_warning{{{INST}}} == 1", "Pool warning", "pool", 1),
        attention(f"100 * truenas_pool_allocated_bytes{{{INST}}} / (truenas_pool_size_bytes{{{INST}}} > 0) > 85",
                  "Pool over 85 % full", "pool", 1),
        attention(f'{inc.DISK_TEMP.replace(chr(36) + "disk", ".*")} > 50', "Disk above 50 °C", "disk", 1),
        attention(f"(truenas_certificate_expiry_timestamp_seconds{{{INST}}} - time()) < 30 * 86400",
                  "Certificate expires within 30 days", "name", 1),
        attention(f"truenas_api_call_success{{{INST}}} == 0", "API method failing", "method", 1),
        attention(f"{inc.OUTSTANDING_ALERTS} > 0", "Outstanding alerts in TrueNAS", "", 1),
        attention(f"truenas_system_reboot_required{{{INST}}} == 1", "Reboot required", "", 1),
    ])
    add(0, 4, 14, 11, state_table(
        "What needs attention right now?",
        "Everything currently failing or close to a limit, worst first. Empty means nothing needs attention.",
        sources, [("kind", "Problem"), ("item", "Where")], "Severity",
        {2: ("✕ Action", RED), 1: ("⚠ Attention", ORANGE)},
        no_value="✓ Nothing needs attention"))
    changes = " or ".join([
        changed(f"resets(truenas_host_uptime_seconds{{{INST}}}[$__range]) > 0", "Host rebooted", ""),
        changed(f"changes(truenas_pool_healthy{{{INST}}}[$__range]) > 0", "Pool health changed", "pool"),
        changed(f"changes(truenas_service_running{{{INST}}}[$__range]) > 0", "Service started/stopped", "service"),
        changed(f"changes(truenas_interface_link_up{{{INST}}}[$__range]) > 0", "Link went up/down", "interface"),
        changed(f"changes(truenas_app_container_count{{{INST}}}[$__range]) > 0", "App containers changed", "app"),
        changed(f"changes(truenas_alert_count{{{INST}}}[$__range]) > 0", "Alert count changed", ""),
        changed(f"changes(truenas_update_available{{{INST}}}[$__range]) > 0", "Update availability changed", ""),
        changed(f"changes(truenas_up{{{INST}}}[$__range]) > 0", "Exporter connectivity flapped", "instance"),
    ])
    add(14, 4, 10, 11, state_table(
        "What changed in this time range?",
        "State flips inside the selected time range (count of changes). Widen the time range to look further back.",
        changes, [("kind", "Change"), ("item", "Where")], "Changes", None,
        no_value="No changes in this time range"))
    add(0, 15, 8, 8, ts(
        "Alerts over time", "Outstanding vs dismissed alerts.",
        [panel_query(inc.OUTSTANDING_ALERTS, "A", "Outstanding"),
         panel_query(f"sum(truenas_alert_dismissed_count{{{INST}}})", "B", "Dismissed")],
        unit="short", mn=0,
        overrides=[color_override("Outstanding", ORANGE), color_override("Dismissed", GREY)]))
    add(8, 15, 8, 8, ts(
        "Error rates", "API-call and collector error rates (errors per second).",
        [panel_query(f"sum by (method) (rate(truenas_api_call_errors_total{{{INST}}}[$__rate_interval])) > 0", "A", "{{method}}"),
         panel_query(f"sum(rate(truenas_collector_errors_total{{{INST}}}[$__rate_interval])) > 0", "B", "collector")],
        unit="ops", mn=0, no_value="No errors recorded"))
    add(16, 15, 8, 8, ts(
        "Exporter poll time", "How long each poll of the TrueNAS API takes; spikes precede stale data.",
        [panel_query(f"max(truenas_scrape_duration_seconds{{{INST}}})", "A", "poll duration")],
        unit="s", mn=0))
    return rows_layout([layout_row(grid_layout(items), hide_header=True)])


# MC-only question-led titles (the classic dashboard keeps its noun titles).
QUESTION_TITLES = {
    ("CPU & Load", "CPU Usage"): "How busy is the CPU?",
    ("Storage & Pools", "Pool Utilization"): "Which pool fills first?",
    ("Storage & Pools", "Days Until Full"): "When will each pool be full?",
    ("Storage & Pools", "Pool Capacity Trends"): "How fast are pools growing?",
    ("Disks & Temperatures", "Disk Temperatures"): "Hottest disks",
    ("Disks & Temperatures", "Disk Busy %"): "Which disks are saturated?",
    ("Network & Interfaces", "Network RX by Interface"): "Inbound traffic per interface",
    ("Network & Interfaces", "Network TX by Interface"): "Outbound traffic per interface",
    ("Apps & Docker", "Top Apps by CPU"): "Which apps use the most CPU?",
    ("Apps & Docker", "Top Apps by Memory"): "Which apps use the most memory?",
    ("Dataset Deep-Dive", "Top Datasets by Used Bytes"): "Top space consumers",
    ("Dataset Deep-Dive", "Datasets Using Snapshot Space"): "Where is snapshot space going?",
    ("Dataset Deep-Dive", "Datasets by Available Space (Bottom 15)"): "Datasets closest to their limit",
    ("Alerts, Tasks & Updates", "Alert Classes"): "What are the alerts about?",
}

# Table columns that link to the matching tab filtered by that variable.
DRILLDOWN = {"Pool": ("pool", "pools"), "Disk": ("disk", "disks"),
             "App": ("app", "apps"), "Dataset": ("dataset", "datasets")}


def add_drilldown_links(elements: dict, tabs_by_key: dict) -> None:
    for el in elements.values():
        spec = el["spec"]
        if spec["vizConfig"]["group"] != "table":
            continue
        overrides = spec["vizConfig"]["spec"]["fieldConfig"].setdefault("overrides", [])
        names = json.dumps(spec["data"]["spec"]["transformations"])
        for column, (var, key) in DRILLDOWN.items():
            if f'"{column}"' not in names:
                continue
            url = (f"/d/{DASH_UID}?${{__url_time_range}}&${{instance:queryparam}}"
                   f"&var-{var}=${{__value.raw}}&dtab={tab_slug(tabs_by_key[key])}")
            overrides.append({"matcher": {"id": "byName", "options": column}, "properties": [
                {"id": "links", "value": [{"title": f"Show {column.lower()} ${{__value.raw}}",
                                            "url": url, "targetBlank": False}]}]})


def pool_cards(elements: dict) -> dict:
    """Per-pool capacity cards, repeated by $pool (1 pool or 20)."""
    items: list = []
    card = mc_stat(
        "Pool $pool",
        f'100 * truenas_pool_allocated_bytes{{{INST}, pool=~"$pool"}} '
        f'/ (truenas_pool_size_bytes{{{INST}, pool=~"$pool"}} > 0)',
        "Used share of this pool with its trend. Repeated for every pool selected in the Pool variable.",
        unit="percent", decimals=1, th=((GREEN, 0), (ORANGE, 80), (RED, 90)), graph="area",
        color_mode="background")
    add_to(elements, items, 0, 0, 6, 4, card,
           repeat={"mode": "variable", "value": "pool", "direction": "h", "maxPerRow": 4})
    return grid_layout(items)


# ---------------------------------------------------------------------------
# Variables
# ---------------------------------------------------------------------------

def convert_variables(classic_vars: list) -> list:
    out = []
    for v in classic_vars:
        if v["type"] == "datasource":
            out.append({
                "kind": "DatasourceVariable",
                "spec": {
                    "name": v["name"],
                    "label": v.get("label", "Datasource"),
                    "pluginId": v.get("query", "prometheus"),
                    "refresh": "onDashboardLoad",
                    "regex": v.get("regex", ""),
                    "current": {"text": "", "value": ""},
                    "options": [],
                    "multi": False,
                    "includeAll": False,
                    "hide": "dontHide",
                    "skipUrlSync": False,
                    "allowCustomValue": True,
                },
            })
        elif v["type"] == "query":
            query_text = v["query"]["query"] if isinstance(v["query"], dict) \
                else v["query"]
            spec = {
                "name": v["name"],
                "label": v.get("label", v["name"]),
                "current": {"text": ["All"], "value": ["$__all"]},
                "hide": "dontHide",
                "refresh": "onTimeRangeChanged",
                "skipUrlSync": False,
                "query": data_query({"query": query_text, "refId": "Q"}),
                "regex": v.get("regex", ""),
                "sort": "naturalAsc",
                "definition": v.get("definition", query_text),
                "options": [],
                "multi": bool(v.get("multi", False)),
                "includeAll": bool(v.get("includeAll", False)),
                "allowCustomValue": True,
            }
            if v.get("allValue"):
                spec["allValue"] = v["allValue"]
            out.append({"kind": "QueryVariable", "spec": spec})
        else:
            raise ValueError(f"unhandled variable type: {v['type']}")
    return out


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------

# New tab title -> (key, classic rows). A row is "show" (expanded), "split"
# (first band of tiles visible, the rest collapsed as details) or "collapse"
# (optional feature: collapsed, its tiles read N/A when the feature is absent).
TAB_SOURCES: list[tuple[str, str, list[tuple[str, str]]]] = [
    ("💻 Compute", "compute", [("CPU & Load", "show"), ("Memory & Swap", "show")]),
    ("🗄️ Pools & ZFS", "pools", [("Storage & Pools", "show"), ("ZFS ARC & Cache", "show")]),
    ("📁 Datasets", "datasets", [("Dataset Deep-Dive", "show")]),
    ("💿 Disks & Hardware", "disks",
     [("Disks & Temperatures", "show"), ("Hardware & IPMI", "collapse")]),
    ("🌐 Network", "network", [("Network & Interfaces", "show")]),
    ("🔗 Shares & Protocols", "shares",
     [("Services & Shares", "show"), ("Advanced Protocols (NVMe-oF / FC / HA)", "collapse")]),
    ("📦 Apps & Docker", "apps", [("Apps & Docker", "show")]),
    ("🖥️ VMs & Virt", "vms", [("Virtualization (VMs & Incus)", "split")]),
    ("🚨 Alerts & Jobs", "alerts", [("Alerts, Tasks & Updates", "show")]),
    ("🔐 Security & Audit", "security",
     [("Security & Platform", "show"), ("Boot Environment", "show"),
      ("Audit & Directory Services", "collapse")]),
    ("⚙️ Exporter & Config", "exporter",
     [("Exporter + Advanced ZFS", "show"), ("System Configuration", "collapse")]),
]
OVERVIEW_TITLE = "🏠 Overview"
INCIDENT_TITLE = "🚑 Incident"
FEATURE_NOTE = {
    "Hardware & IPMI": "Hardware & IPMI — tiles read N/A on systems without IPMI/GPUs",
    "Advanced Protocols (NVMe-oF / FC / HA)": "NVMe-oF, Fibre Channel & HA — N/A unless configured",
    "Audit & Directory Services": "Audit & directory services",
    "System Configuration": "System configuration",
}


def build(live: set | None = None) -> tuple[dict, set | None]:
    global _next_id
    _next_id = NEW_ID_START
    classic = json.loads(SRC.read_text(encoding="utf-8"))
    classic_rows = {p["title"]: p.get("panels", [])
                    for p in classic["panels"] if p["type"] == "row"}

    elements: dict = {}
    tabs = []
    relocated: list[str] = []
    tabs_by_key = {key: title for title, key, _ in TAB_SOURCES}
    tabs_by_key["incident"] = INCIDENT_TITLE
    tabs_by_key["overview"] = OVERVIEW_TITLE

    overview_layout = build_overview(elements,
                                     classic_rows.pop("System Overview"), live,
                                     tabs_by_key)
    tabs.append(tab(OVERVIEW_TITLE, overview_layout))
    tabs.append(tab(INCIDENT_TITLE, build_incident(elements, tabs_by_key)))

    consumed = set()
    for tab_title, key, row_specs in TAB_SOURCES:
        rows = []
        dead: list = []
        if key == "pools":
            rows.append(layout_row(pool_cards(elements), title="Pools at a glance"))
        for rt, mode in row_specs:
            panels = classic_rows[rt]
            consumed.add(rt)
            if mode == "split":
                y_first = min(p["gridPos"]["y"] for p in panels)
                head = [p for p in panels if p["gridPos"]["y"] == y_first]
                tail = [p for p in panels if p["gridPos"]["y"] != y_first]
                rows.append(layout_row(classic_row_to_grid(head, elements, rt, dead, live),
                                       title=f"{rt} — what is configured?"))
                rows.append(layout_row(classic_row_to_grid(tail, elements, rt, dead, live),
                                       title="Details (expand when VMs or Incus instances exist)",
                                       collapse=True))
                continue
            grid = classic_row_to_grid(panels, elements, rt, dead, live)
            if mode == "collapse":
                rows.append(layout_row(grid, title=FEATURE_NOTE.get(rt, rt), collapse=True))
            elif len(row_specs) == 1 and key != "pools":
                rows.append(layout_row(grid, hide_header=True))
            else:
                rows.append(layout_row(grid, title=rt))
        if dead:
            relocated.extend(f"{tab_title} / {p['title']}" for p in dead)
            rows.append(layout_row(pack_grid(dead, elements),
                                   title="🚫 Not collected on this system",
                                   collapse=True))
        tabs.append(tab(tab_title, rows_layout(rows)))

    if live is not None:
        print(f"relocated {len(relocated)} dead panels:")
        for entry in relocated:
            print(f"  - {entry}")

    apply_nan_guard(elements)
    add_drilldown_links(elements, tabs_by_key)

    leftover = set(classic_rows) - consumed
    assert not leftover, f"classic rows not mapped to any tab: {leftover}"

    spec = {
        "title": "TrueNAS · Mission Control",
        "description": (
            "Flagship TrueNAS SCALE dashboard fed by the "
            "truenas-scale-api-prometheus-exporter. Overview answers 'is my NAS "
            "OK?' in seconds, Incident puts everything failing on one screen, "
            "and the remaining tabs group the full metric surface by concern. "
            "Grey N/A always means 'no data / not present', never healthy. "
            "Generated by build_mission_control.py."),
        "tags": ["truenas", "mission-control", "generated"],
        "cursorSync": "Crosshair",
        "editable": True,
        "preload": False,
        "liveNow": False,
        "annotations": [{
            "kind": "AnnotationQuery",
            "spec": {
                "builtIn": True,
                "enable": True,
                "hide": True,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "query": {"kind": "DataQuery", "group": "grafana",
                          "version": "v0", "spec": {}},
            },
        }],
        "links": [{
            "title": "← Operations Center (classic)",
            "type": "link",
            "icon": "dashboard",
            "tooltip": "Open the original TrueNAS Operations Center dashboard",
            "url": f"/d/{classic['uid']}",
            "tags": [],
            "asDropdown": False,
            "targetBlank": False,
            "includeVars": True,
            "keepTime": True,
        }],
        "timeSettings": {
            "timezone": "browser",
            "from": "now-6h",
            "to": "now",
            "autoRefresh": "30s",
            "autoRefreshIntervals": ["10s", "30s", "1m", "5m", "15m",
                                     "30m", "1h", "2h", "1d"],
            "hideTimepicker": False,
            "fiscalYearStartMonth": 0,
        },
        "variables": convert_variables(classic["templating"]["list"]),
        "elements": elements,
        "layout": {"kind": "TabsLayout", "spec": {"tabs": tabs}},
    }

    return classic_gen.finalize({
        "apiVersion": "dashboard.grafana.app/v2beta1",
        "kind": "Dashboard",
        "metadata": {"name": "truenas-mission-control"},
        "spec": spec,
    }), live


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def collect_element_refs(node, refs: list) -> list:
    if isinstance(node, dict):
        if node.get("kind") == "ElementReference":
            refs.append(node["name"])
        for v in node.values():
            collect_element_refs(v, refs)
    elif isinstance(node, list):
        for item in node:
            collect_element_refs(item, refs)
    return refs


def collect_visible_refs(node, refs: list) -> list:
    """Element refs excluding those under '🚫 Not collected' rows."""
    if isinstance(node, dict):
        if node.get("kind") == "RowsLayoutRow" and \
                node["spec"].get("title", "").startswith("🚫"):
            return refs
        if node.get("kind") == "ElementReference":
            refs.append(node["name"])
        for v in node.values():
            collect_visible_refs(v, refs)
    elif isinstance(node, list):
        for item in node:
            collect_visible_refs(item, refs)
    return refs


def validate(doc: dict, live: set | None) -> None:
    spec = doc["spec"]
    elements = spec["elements"]

    if live is not None:
        for name in collect_visible_refs(spec["layout"], []):
            el = elements[name]
            names = set()
            for q in el["spec"]["data"]["spec"]["queries"]:
                names.update(METRIC_NAME_RE.findall(
                    q["spec"]["query"]["spec"].get("expr", "")))
            conditional = any(n.startswith(CONDITIONAL_METRIC_PREFIXES)
                              for n in names)
            assert not names or conditional or names & live, (
                f"visible panel {el['spec']['title']!r} queries only "
                f"never-emitted metrics: {sorted(names)}")

    refs = collect_element_refs(spec["layout"], [])
    assert len(refs) == len(set(refs)), "element referenced more than once"
    assert set(refs) == set(elements), (
        f"layout/elements mismatch: only-in-layout="
        f"{set(refs) - set(elements)} only-in-elements="
        f"{set(elements) - set(refs)}")

    ids = [e["spec"]["id"] for e in elements.values()]
    assert len(ids) == len(set(ids)), "duplicate panel ids"

    var_names = {v["spec"]["name"] for v in spec["variables"]}
    expected = {"DS_PROMETHEUS", "instance", "pool", "dataset", "disk",
                "interface", "service", "app", "task_type", "level", "method"}
    assert expected <= var_names, f"missing variables: {expected - var_names}"

    # Metric coverage: everything the classic dashboard referenced must
    # still be present.
    old_metrics = set(re.findall(r"truenas_[a-z0-9_]+",
                                 SRC.read_text(encoding="utf-8")))
    new_metrics = set(re.findall(r"truenas_[a-z0-9_]+", json.dumps(doc)))
    missing = old_metrics - new_metrics
    assert not missing, f"metric coverage regression: {sorted(missing)}"
    # Bidirectional: every metric name in the output must be a real name from
    # the source dashboard or the live exporter — catches any transformation
    # that mangles a selector (e.g. a regex splitting a metric name).
    known = old_metrics | (live or set())
    invented = new_metrics - known
    assert not invented, f"mangled/unknown metric names: {sorted(invented)}"

    print(f"validated: {len(elements)} panels, "
          f"{len(spec['layout']['spec']['tabs'])} tabs, "
          f"{len(new_metrics)} distinct truenas_* metric names "
          f"(classic had {len(old_metrics)})")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--metric-names", type=Path, help="Optional local JSON list of metric names for system-specific layout")
    args = parser.parse_args()
    live = None
    if args.metric_names:
        names = json.loads(args.metric_names.read_text(encoding="utf-8"))
        if not isinstance(names, list) or not all(isinstance(n, str) and re.fullmatch(r"truenas_[A-Za-z0-9_:]+", n) for n in names):
            parser.error("--metric-names must contain a JSON list of truenas_ metric names")
        live = set(names)
    doc, live = build(live)
    validate(doc, live)
    rendered = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not args.output.is_file() or args.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit("Mission Control dashboard is out of date: regenerate without --check")
    else:
        args.output.write_text(rendered, encoding="utf-8")
    print("mission_control_ok")


if __name__ == "__main__":
    main()
