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

import copy
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "operations-center-dashboard.json"
OUT = HERE / "truenas-mission-control.json"

# Live exporter endpoint used to detect metrics that exist in code but are
# never emitted on this system (their panels get moved to a collapsed row).
EXPORTER_URL = os.environ.get("TRUENAS_EXPORTER_URL",
                              "http://192.168.0.247:9108/metrics")

DS_VAR = "${DS_PROMETHEUS}"

GREEN = "#1A9E3A"
RED = "#F2495C"
ORANGE = "#FF9830"
YELLOW = "#E0B400"
BLUE = "#5794F2"
PURPLE = "#B877D9"

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


NAN_STAT_MAPPING = {
    "type": "special",
    "options": {"match": "nan",
                "result": {"text": "n/a", "color": "#808080", "index": 99}},
}


def restyle_classic(p: dict) -> dict:
    """Light-touch consistency pass. Never changes query semantics."""
    p = copy.deepcopy(p)
    fc = p.setdefault("fieldConfig", {}).setdefault("defaults", {})
    if p["type"] == "timeseries":
        custom = fc.setdefault("custom", {})
        if custom.get("fillOpacity", 0) < 10:
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
        steps = fc.get("thresholds", {}).get("steps", [])
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


def _set_mappings(p, mapping, color_mode=None):
    p["fieldConfig"]["defaults"]["mappings"] = [value_map(mapping)]
    if color_mode:
        p.setdefault("options", {})["colorMode"] = color_mode


def _set_color(p, mode):
    p["fieldConfig"]["defaults"]["color"] = {"mode": mode}


def _hit_pct_expr(kind: str) -> str:
    hits = f'sum(truenas_zfs_{kind}_hits_per_second{{instance=~"$instance"}})'
    misses = f'sum(truenas_zfs_{kind}_misses_per_second{{instance=~"$instance"}})'
    return f"100 * {hits} / clamp_min({hits} + {misses}, 1)"


def _patch_hit_pct(kind, neutral=False):
    def fn(p):
        p["targets"][0]["expr"] = _hit_pct_expr(kind)
        fc = p["fieldConfig"]["defaults"]
        if neutral:
            fc["thresholds"] = thresholds((BLUE, None))
            p["description"] = (p.get("description", "") +
                                " Shows 0% when no L2ARC device exists.").strip()
        else:
            fc["thresholds"] = thresholds(("red", None), (YELLOW, 80),
                                          ("green", 95))
        fc["noValue"] = "n/a"
    return fn


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


def _patch_blkio(p):
    p["title"] = "App Block I/O Rate"
    p["description"] = "Read/write throughput per app (rate of cumulative counters)."
    for t in p["targets"]:
        t["expr"] = re.sub(r"(truenas_app_blkio_\w+\{[^}]*\})",
                           r"rate(\1[$__rate_interval])", t["expr"])
    p["fieldConfig"]["defaults"]["unit"] = "Bps"


def _patch_load_avg(p):
    p["targets"] = [t for t in p["targets"]
                    if "host_cpu_cores" not in t["expr"]]


def _patch_oldest_snap(p):
    p["targets"][0]["expr"] = (
        'time() - (truenas_snapshot_oldest_timestamp_seconds'
        '{instance=~"$instance"} > 0)')
    p["fieldConfig"]["defaults"]["noValue"] = "n/a"


PANEL_PATCHES = {
    ("Apps & Docker", "DH RL Error"): lambda p: _set_mappings(
        p, {0: ("✅ None", "green"), 1: ("Rate limited", "red")}),
    ("Apps & Docker", "NVIDIA GPU"): lambda p: _set_mappings(
        p, {0: ("Not present", "#808080"), 1: ("Yes", "green")},
        color_mode="value"),
    ("Memory & Swap", "ECC"): lambda p: _set_mappings(
        p, {0: ("No", ORANGE), 1: ("Yes", "green")}, color_mode="value"),
    ("Apps & Docker", "App Block I/O"): _patch_blkio,
    ("Apps & Docker", "App State Distribution"): _patch_app_states,
    ("Apps & Docker", "App Container State Distribution"): _patch_app_states,
    ("Apps & Docker", "Top Apps by CPU"): lambda p: (
        p["fieldConfig"]["defaults"].update(decimals=2)),
    ("Apps & Docker", "Top Apps by Memory"): lambda p: _set_color(
        p, "continuous-blues"),
    ("CPU & Load", "Load Average"): _patch_load_avg,
    ("Storage & Pools", "Oldest Snap"): _patch_oldest_snap,
    ("System Overview", "Data Hit %"): _patch_hit_pct("demand_data"),
    ("ZFS ARC & Cache", "Data Hit %"): _patch_hit_pct("demand_data"),
    ("ZFS ARC & Cache", "Meta Hit %"): _patch_hit_pct("demand_meta"),
    ("ZFS ARC & Cache", "L2ARC Hit %"): _patch_hit_pct("l2arc", neutral=True),
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


NAMES_CACHE = HERE / ".metric-names-cache.json"


def fetch_live_metrics() -> set | None:
    """Names of truenas_* metrics with at least one sample line (NaN counts).

    A single scrape is flaky (some collectors report intermittently), so the
    result is unioned with every name observed in previous runs, cached in a
    names-only file next to this script. Returns None when the exporter is
    unreachable and no cache exists (pass is then skipped).
    """
    cached: set = set()
    if NAMES_CACHE.exists():
        cached = set(json.loads(NAMES_CACHE.read_text(encoding="utf-8")))
    try:
        with urllib.request.urlopen(EXPORTER_URL, timeout=60) as resp:
            text = resp.read().decode("utf-8", errors="replace")
    except (urllib.error.URLError, OSError) as exc:
        print(f"warning: exporter not reachable ({exc}); "
              f"using {len(cached)} cached metric names" if cached else
              f"warning: exporter not reachable ({exc}); "
              "dead-panel relocation skipped", file=sys.stderr)
        return cached or None
    live = set(cached)
    for line in text.splitlines():
        if line.startswith("truenas_"):
            live.add(line.split("{", 1)[0].split(" ", 1)[0])
    NAMES_CACHE.write_text(json.dumps(sorted(live), indent=0) + "\n",
                           encoding="utf-8")
    return live


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


def build_overview(elements: dict, snapshot_panels: list,
                   live: set | None) -> dict:
    items = []

    def add(x, y, w, h, element):
        name = f"panel-{element['spec']['id']}"
        assert name not in elements, f"duplicate element name {name}"
        elements[name] = element
        items.append(grid_item(x, y, w, h, name))

    inst = 'instance=~"$instance"'

    # --- Hero band: 8 tiles, w=3 h=4, solid backgrounds -------------------
    add(0, 0, 3, 4, panel_element(
        next_id(), "stat", "System", "TrueNAS middleware state (system.ready).",
        [panel_query(f"min(truenas_system_ready{{{inst}}})")],
        stat_options(),
        {"unit": "short",
         "mappings": [value_map({1: ("🟢 READY", "green"),
                                 0: ("🔴 NOT READY", "red")})],
         "thresholds": thresholds(("red", None), ("green", 1))}))

    add(3, 0, 3, 4, panel_element(
        next_id(), "stat", "Active Alerts", "Alerts currently raised by TrueNAS.",
        [panel_query(f"sum(truenas_alert_count{{{inst}}}) OR on() vector(0)")],
        stat_options(),
        {"unit": "short", "decimals": 0,
         "mappings": [value_map({0: ("✅ 0", "green")})],
         "thresholds": thresholds(("green", None), (YELLOW, 1), ("red", 3))}))

    add(6, 0, 3, 4, panel_element(
        next_id(), "stat", "Pools", "Worst pool health across all ZFS pools.",
        [panel_query(f"min(truenas_pool_healthy{{{inst}}})")],
        stat_options(),
        {"unit": "short",
         "mappings": [value_map({1: ("🟢 HEALTHY", "green"),
                                 0: ("🔴 DEGRADED", "red")})],
         "thresholds": thresholds(("red", None), ("green", 1))}))

    add(9, 0, 3, 4, panel_element(
        next_id(), "stat", "Pool Capacity", "Allocated share of total pool space.",
        [panel_query(
            f"100 * (sum(truenas_pool_allocated_bytes{{{inst}}}) "
            f"/ clamp_min(sum(truenas_pool_size_bytes{{{inst}}}), 1))")],
        stat_options(graph="area"),
        {"unit": "percent", "decimals": 1, "min": 0, "max": 100,
         "thresholds": thresholds(("green", None), (YELLOW, 70), ("red", 85))}))

    add(12, 0, 3, 4, panel_element(
        next_id(), "stat", "CPU", "Average CPU utilization.",
        [panel_query(f"avg(truenas_cpu_usage_percent{{{inst}}})")],
        stat_options(graph="area"),
        {"unit": "percent", "decimals": 1, "min": 0, "max": 100,
         "thresholds": thresholds(("green", None), (YELLOW, 70), ("red", 90))}))

    add(15, 0, 3, 4, panel_element(
        next_id(), "stat", "RAM", "Physical memory in use.",
        [panel_query(
            f"100 * (sum(truenas_memory_physical_used_bytes{{{inst}}}) "
            f"/ clamp_min(sum(truenas_memory_physical_total_bytes{{{inst}}}), 1))")],
        stat_options(graph="area"),
        {"unit": "percent", "decimals": 1, "min": 0, "max": 100,
         "thresholds": thresholds(("green", None), (YELLOW, 80), ("red", 92))}))

    add(18, 0, 3, 4, panel_element(
        next_id(), "stat", "Hottest Disk", "Highest current disk temperature.",
        [panel_query(f"max(truenas_disk_temperature_celsius{{{inst}}})")],
        stat_options(graph="area"),
        {"unit": "celsius", "decimals": 0,
         "thresholds": thresholds(("green", None), (YELLOW, 45), ("red", 55))}))

    add(21, 0, 3, 4, panel_element(
        next_id(), "stat", "Uptime", "Host uptime.",
        [panel_query(f"max(truenas_host_uptime_seconds{{{inst}}})")],
        stat_options(color_mode="value"),
        {"unit": "s", "decimals": 1, "color": {"mode": "fixed", "fixedColor": BLUE},
         "thresholds": thresholds((BLUE, None))}))

    # --- Second band: 6 tiles, w=4 h=3, quieter ---------------------------
    quiet = stat_options(color_mode="value")
    add(0, 4, 4, 3, panel_element(
        next_id(), "stat", "Services Running", "TrueNAS services currently running.",
        [panel_query(f"sum(truenas_service_running{{{inst}}})")],
        quiet, {"unit": "short", "decimals": 0,
                "thresholds": thresholds((BLUE, None))}))
    add(4, 4, 4, 3, panel_element(
        next_id(), "stat", "Apps", "Installed apps (Docker).",
        [panel_query(f"max(truenas_app_count{{{inst}}})")],
        quiet, {"unit": "short", "decimals": 0,
                "thresholds": thresholds((PURPLE, None))}))
    add(8, 4, 4, 3, panel_element(
        next_id(), "stat", "ARC Data Hit",
        "ZFS ARC demand-data hit ratio (computed from hit/miss counters).",
        [panel_query(_hit_pct_expr("demand_data"))],
        quiet, {"unit": "percent", "decimals": 1, "noValue": "n/a",
                "thresholds": thresholds(("red", None), (YELLOW, 80),
                                         ("green", 95))}))
    add(12, 4, 4, 3, panel_element(
        next_id(), "stat", "Load (1m)", "1-minute load average.",
        [panel_query(f'avg(truenas_host_load_average{{{inst}, window="1m"}})')],
        quiet, {"unit": "short", "decimals": 2,
                "thresholds": thresholds(("green", None), (YELLOW, 4),
                                         ("red", 8))}))
    add(16, 4, 4, 3, panel_element(
        next_id(), "stat", "Update", "Whether a TrueNAS update is available.",
        [panel_query(f"max(truenas_update_available{{{inst}}})")],
        quiet, {"unit": "short",
                "mappings": [value_map({0: ("✅ Up to date", "green"),
                                        1: ("⬆️ Available", YELLOW)})],
                "thresholds": thresholds(("green", None), (YELLOW, 1))}))
    add(20, 4, 4, 3, panel_element(
        next_id(), "stat", "Scrape Time", "Exporter scrape duration (last run).",
        [panel_query(f"max(truenas_scrape_duration_seconds{{{inst}}})")],
        quiet, {"unit": "s", "decimals": 2,
                "thresholds": thresholds(("green", None), (YELLOW, 15),
                                         ("red", 30))}))

    # --- Visual band ------------------------------------------------------
    add(0, 7, 8, 8, panel_element(
        next_id(), "bargauge", "Pool Utilization",
        "Allocated percentage per ZFS pool against real capacity.",
        [panel_query(
            f'100 * max by (pool) (truenas_pool_allocated_bytes{{{inst}, pool=~"$pool"}}) '
            f'/ clamp_min(max by (pool) (truenas_pool_size_bytes{{{inst}, pool=~"$pool"}}), 1)',
            legend="{{pool}}", instant=True)],
        {"displayMode": "gradient", "orientation": "horizontal",
         "valueMode": "color", "showUnfilled": True, "minVizHeight": 16,
         "maxVizHeight": 300, "sizing": "auto",
         "reduceOptions": {"calcs": ["lastNotNull"], "fields": "",
                           "values": False},
         "legend": {"showLegend": False}},
        {"unit": "percent", "decimals": 1, "min": 0, "max": 100,
         "thresholds": thresholds(("green", None), (YELLOW, 70), ("red", 85))}))

    add(8, 7, 6, 8, panel_element(
        next_id(), "piechart", "Alerts by Level",
        "Current alert distribution by severity level.",
        [panel_query(
            f"sum by (level) (truenas_alert_count_by_level{{{inst}}})",
            legend="{{level}}", instant=True)],
        {"pieType": "donut",
         "displayLabels": ["name", "value"],
         "legend": {"displayMode": "list", "placement": "right",
                    "showLegend": True, "values": []},
         "reduceOptions": {"calcs": ["lastNotNull"], "fields": "",
                           "values": False},
         "tooltip": {"mode": "single", "sort": "none"}},
        {"unit": "short", "decimals": 0,
         "color": {"mode": "palette-classic-by-name"}},
        overrides=[
            color_override("CRITICAL", RED),
            color_override("ERROR", ORANGE),
            color_override("WARNING", YELLOW),
            color_override("NOTICE", BLUE),
            color_override("INFO", GREEN),
        ]))

    add(14, 7, 10, 8, panel_element(
        next_id(), "timeseries", "Load per Core",
        "Load average normalized by CPU core count. 100% means the run queue "
        "equals the core count; the dashed line marks that saturation point.",
        [panel_query(
            f'100 * avg by (window) (truenas_host_load_average{{{inst}}})'
            f' / on () group_left () max(truenas_host_cpu_cores{{{inst}}})',
            legend="load {{window}}")],
        TS_OPTIONS,
        {"unit": "percent", "decimals": 1,
         "custom": ts_custom(thresholdsStyle={"mode": "dashed+area"}),
         "color": {"mode": "palette-classic-by-name"},
         "thresholds": thresholds(("transparent", None), (YELLOW, 70),
                                  ("red", 100))}))

    # --- Trend band -------------------------------------------------------
    add(0, 15, 12, 8, panel_element(
        next_id(), "timeseries", "CPU Usage",
        "Total and per-core CPU usage. TrueNAS 25.10 no longer reports CPU mode splits.",
        [panel_query(f"truenas_cpu_core_usage_percent{{{inst}}}", "A", "Core {{core}}"),
         panel_query(f"avg(truenas_cpu_usage_percent{{{inst}}})", "B", "Total")],
        TS_OPTIONS,
        {"unit": "percent", "min": 0,
         "custom": ts_custom(fillOpacity=35, gradientMode="none", lineWidth=1),
         "color": {"mode": "palette-classic-by-name"},
         "thresholds": thresholds(("green", None))}))

    add(12, 15, 12, 8, panel_element(
        next_id(), "timeseries", "Memory & ZFS ARC",
        "Physical memory used vs total, with the ZFS ARC share.",
        [panel_query(f"sum(truenas_memory_physical_used_bytes{{{inst}}})",
                     "A", "Used"),
         panel_query(f"sum(truenas_zfs_arc_size_bytes{{{inst}}})",
                     "B", "ZFS ARC"),
         panel_query(f"sum(truenas_memory_physical_total_bytes{{{inst}}})",
                     "C", "Total")],
        TS_OPTIONS,
        {"unit": "bytes", "min": 0,
         "custom": ts_custom(),
         "color": {"mode": "palette-classic-by-name"},
         "thresholds": thresholds(("green", None))},
        overrides=[
            color_override("ZFS ARC", PURPLE),
            {"matcher": {"id": "byName", "options": "Total"},
             "properties": [
                 {"id": "color", "value": {"mode": "fixed", "fixedColor": RED}},
                 {"id": "custom.lineStyle",
                  "value": {"fill": "dash", "dash": [10, 10]}},
                 {"id": "custom.fillOpacity", "value": 0},
             ]},
        ]))

    hero_grid = grid_layout(items)
    dead: list = []
    snapshot_grid = classic_row_to_grid(snapshot_panels, elements,
                                        "System Overview", dead, live)
    rows = [
        layout_row(hero_grid, hide_header=True),
        layout_row(snapshot_grid, title="📋 System Snapshot", collapse=True),
    ]
    if dead:
        rows.append(layout_row(pack_grid(dead, elements),
                               title="🚫 Not collected on this system",
                               collapse=True))
    return rows_layout(rows)


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

# New tab title -> classic row titles feeding it (order preserved).
TAB_SOURCES: list[tuple[str, list[str]]] = [
    ("💻 Compute", ["CPU & Load", "Memory & Swap"]),
    ("🗄️ Pools & ZFS", ["Storage & Pools", "ZFS ARC & Cache"]),
    ("📁 Datasets", ["Dataset Deep-Dive"]),
    ("💿 Disks & Hardware", ["Disks & Temperatures", "Hardware & IPMI"]),
    ("🌐 Network", ["Network & Interfaces"]),
    ("🔗 Shares & Protocols",
     ["Services & Shares", "Advanced Protocols (NVMe-oF / FC / HA)"]),
    ("📦 Apps & Docker", ["Apps & Docker"]),
    ("🖥️ VMs & Virt", ["Virtualization (VMs & Incus)"]),
    ("🚨 Alerts & Jobs", ["Alerts, Tasks & Updates"]),
    ("🔐 Security & Audit",
     ["Security & Platform", "Audit & Directory Services", "Boot Environment"]),
    ("⚙️ Exporter & Config",
     ["Exporter + Advanced ZFS", "System Configuration"]),
]


def build() -> dict:
    classic = json.loads(SRC.read_text(encoding="utf-8"))
    classic_rows = {p["title"]: p.get("panels", [])
                    for p in classic["panels"] if p["type"] == "row"}

    live = fetch_live_metrics()
    elements: dict = {}
    tabs = []
    relocated: list[str] = []

    overview_layout = build_overview(elements,
                                     classic_rows.pop("System Overview"), live)
    tabs.append(tab("🏠 Overview", overview_layout))

    consumed = set()
    for tab_title, row_titles in TAB_SOURCES:
        rows = []
        dead: list = []
        for rt in row_titles:
            panels = classic_rows[rt]
            consumed.add(rt)
            grid = classic_row_to_grid(panels, elements, rt, dead, live)
            if len(row_titles) == 1:
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

    leftover = set(classic_rows) - consumed
    assert not leftover, f"classic rows not mapped to any tab: {leftover}"

    spec = {
        "title": "TrueNAS · Mission Control",
        "description": (
            "Flagship TrueNAS SCALE dashboard fed by the "
            "truenas-scale-api-prometheus-exporter. Tabs group the full "
            "metric surface by operational concern; the Overview tab is the "
            "30-second health check. Generated by build_mission_control.py."),
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
            "title": "Operations Center (classic)",
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

    return {
        "apiVersion": "dashboard.grafana.app/v2beta1",
        "kind": "Dashboard",
        "metadata": {"name": "truenas-mission-control"},
        "spec": spec,
    }, live


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
    doc, live = build()
    validate(doc, live)
    OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KiB)")


if __name__ == "__main__":
    main()
