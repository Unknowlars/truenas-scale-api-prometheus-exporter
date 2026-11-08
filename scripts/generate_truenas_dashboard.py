import argparse
import copy
import json
from pathlib import Path

try:
    from .tooling import check_or_write
except ImportError:  # direct script execution
    from tooling import check_or_write


DS = {"type": "prometheus", "uid": "${DS_PROMETHEUS}"}
PLUGIN_VERSION = "12.4.0"
REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / "grafana-dashboard" / "operations-center-dashboard.json"


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


def tf(name, options=None):
    return {"id": name, "options": options or {}}


# ── Semantic palette ────────────────────────────────────────────────────
# The single colour system for both dashboards (build_mission_control.py
# imports it). Panel code may keep using Grafana's names; finalize()
# rewrites them to these values so every panel speaks the same language.
OK = "#37A85B"         # healthy / within limits
WARN = "#E8A33D"       # amber: needs attention soon
CRIT = "#E0464E"       # red: broken / act now
INFO = "#3D8BEA"       # blue: informational counts and capabilities
NEUTRAL = "#7B828C"    # grey: N/A, disabled, not present, no data
ACCENT = "#9E6CDB"     # purple: ZFS ARC and other "cache" series
SEMANTIC = {
    "green": OK, "dark-green": OK, "semi-dark-green": OK,
    "yellow": WARN, "orange": WARN, "dark-yellow": WARN,
    "red": CRIT, "dark-red": CRIT, "semi-dark-red": CRIT,
    "blue": INFO, "purple": ACCENT, "#808080": NEUTRAL,
}
NO_VALUE = "N/A"
# Stat/bar-gauge "No data" takes the base threshold colour, so every
# threshold set starts with a neutral base: missing data reads grey, never
# green or red. Real steps start at a value no real sample goes below.
FLOOR = -1e12
NA_MAPPINGS = [
    {"type": "special", "options": {"match": "null", "result": {"text": NO_VALUE, "color": NEUTRAL, "index": 90}}},
    {"type": "special", "options": {"match": "nan", "result": {"text": NO_VALUE, "color": NEUTRAL, "index": 91}}},
]


def neutral_base(steps):
    """Prepend a neutral base step; the first real step keeps its value
    (or FLOOR when it was the base) so real values keep their colour."""
    steps = copy.deepcopy(steps)
    if steps and steps[0].get("value") is None:
        steps[0]["value"] = FLOOR
    return [{"color": NEUTRAL, "value": None}] + steps


def with_na(mappings):
    return copy.deepcopy(mappings or []) + copy.deepcopy(NA_MAPPINGS)


# D8: tile titles must fit their tile. Grafana truncates around 11
# characters on a w=3 tile at 1600 px; TITLE_LIMITS is enforced by
# scripts/validate_dashboard.py and SHORT_TITLES applies the short forms.
TITLE_LIMITS = {2: 7, 3: 11, 4: 16, 5: 20, 6: 24}
SHORT_TITLES = {
    "RAM excl. ARC": "RAM no ARC", "Boot Pool OK": "Boot Pool", "Snap Task Max Total": "Snap Max Total",
    "Gateway Config": "Gateway", "Default Routes": "Def. Routes", "DNS Resolvers": "Resolvers",
    "Pending Changes": "Pending", "Checkin Wait": "Rollback In", "iSCSI Targets": "iSCSI Tgts",
    "SMB Sessions": "SMB Sess.", "iSCSI Clients": "iSCSI Cli.", "WebShare Auth": "WS Auth",
    "SMB Encryption": "SMB Crypt", "Catalog Trains": "Trains", "Virt Support": "HW Virt",
    "Virt Details": "Virt Info", "VM Avail RAM": "VM RAM Free", "Cloud Backups": "Cloud Bkp",
    "Last Alert Activity": "Last Alert", "Dir Svc Configured": "Dir Svc Set",
    "KMIP Sync Pending": "KMIP Pending", "Boot Healthy": "Boot Health", "Activated BEs": "Next BEs",
    "Power Overld": "Overload", "NVMe-oF Sess": "NVMe Sess", "NVMe-oF Subs": "NVMe Subs",
    "NVMe-oF Ports": "NVMe Ports", "NVMe-oF Hosts": "NVMe Hosts", "Event Stream": "Events",
    "Methods OK %": "Methods OK", "API Errors (1h)": "API Err 1h", "Coll Errors (1h)": "Coll Err 1h",
    "Oldest Alert Age": "Alert Age", "Repl Parallel": "Repl Max", "Boot Env Active": "BE Active",
    "Boot Env Next": "BE Next", "Demand Access/s": "ARC Reqs/s", "Data IO Hit %": "Data IO Hit",
    "Meta IO Hit %": "Meta IO Hit", "L2ARC Miss %": "L2ARC Miss",
}


def shorten_titles(panels):
    for p in panels:
        if p.get("type") in ("stat", "gauge") and len(p.get("title", "")) > TITLE_LIMITS.get(p["gridPos"]["w"], 99):
            p["title"] = SHORT_TITLES.get(p["title"], p["title"])


def finalize(node):
    """Rewrite Grafana colour names to the semantic palette, in place."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in ("color", "fixedColor") and isinstance(value, str) and value in SEMANTIC:
                node[key] = SEMANTIC[value]
            else:
                finalize(value)
    elif isinstance(node, list):
        for item in node:
            finalize(item)
    return node


def qvar(name, label, query):
    return {
        "name": name,
        "label": label,
        "type": "query",
        "datasource": copy.deepcopy(DS),
        "query": {"query": query, "refId": "Q"},
        "definition": query,
        "refresh": 2,
        "multi": True,
        "includeAll": True,
        "allValue": ".*",
        "current": {},
        "sort": 1,
        "options": [],
    }


class Ids:
    def __init__(self):
        self.value = 1

    def next(self):
        current = self.value
        self.value += 1
        return current


IDS = Ids()


def stat(title, expr, x, y, w=3, h=4, unit="short", desc="", thresholds=None,
         mappings=None, graph=False, color_mode="background", graph_mode=None,
         legend="", text_mode="auto", decimals=None, no_value=None):
    panel = {
        "type": "stat",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": [tgt(expr, legend)],
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": with_na(mappings),
                "noValue": NO_VALUE,
                "thresholds": {"mode": "absolute", "steps": neutral_base(thresholds or [{"color": "blue", "value": None}])},
                "unit": unit,
            },
            "overrides": [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "colorMode": color_mode,
            "graphMode": graph_mode or ("area" if graph else "none"),
            "justifyMode": "auto",
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "textMode": text_mode,
            "wideLayout": True,
        },
        "pluginVersion": PLUGIN_VERSION,
    }
    if decimals is not None:
        panel["fieldConfig"]["defaults"]["decimals"] = decimals
    if no_value:
        panel["fieldConfig"]["defaults"]["noValue"] = no_value
    return panel


def timeseries(title, targets, x, y, w=12, h=8, unit="short", desc="", stacked=False,
               bars=False, fill=15, overrides=None, transforms=None, legend_table=False,
               min_value=None, max_value=None, no_value=None):
    panel = {
        "type": "timeseries",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "drawStyle": "bars" if bars else "line",
                    "lineInterpolation": "smooth",
                    "lineWidth": 2,
                    "fillOpacity": fill,
                    "gradientMode": "opacity",
                    "showPoints": "never" if bars else "auto",
                    "spanNulls": False,
                    "stacking": {"group": "A", "mode": "normal" if stacked else "none"},
                    "barAlignment": 0,
                    "barWidthFactor": 0.6,
                    "thresholdsStyle": {"mode": "off"},
                    "scaleDistribution": {"type": "linear"},
                    "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                },
                "mappings": [],
                "unit": unit,
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": 0}]},
            },
            "overrides": overrides or [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            # Table legends only where few series fit; lists elsewhere so the
            # plot area is never squeezed or clipped (D15).
            "legend": {
                "calcs": ["lastNotNull", "max"] if legend_table else [],
                "displayMode": "table" if legend_table else "list",
                "placement": "bottom",
                "showLegend": True,
            },
            "tooltip": {"hideZeros": False, "mode": "multi", "sort": "desc"},
        },
        "transformations": transforms or [],
        "pluginVersion": PLUGIN_VERSION,
    }
    if unit == "celsius":
        panel["fieldConfig"]["defaults"]["custom"]["axisSoftMin"] = 20
    _apply_limits(panel, min_value, max_value, no_value)
    return panel


def _apply_limits(panel, min_value=None, max_value=None, no_value=None):
    defaults = panel["fieldConfig"]["defaults"]
    if min_value is not None:
        defaults["min"] = min_value
    if max_value is not None:
        defaults["max"] = max_value
    if no_value:
        defaults["noValue"] = no_value
    return panel


def bargauge(title, targets, x, y, w=12, h=8, unit="short", desc="", min_value=0,
             max_value=None, thresholds=None, transforms=None, mappings=None, decimals=None):
    defaults = {
        "color": {"mode": "thresholds"},
        "mappings": with_na(mappings),
        "noValue": NO_VALUE,
        "min": min_value,
        "thresholds": {
            "mode": "absolute",
            "steps": neutral_base(thresholds or [
                {"color": "green", "value": 0},
                {"color": "yellow", "value": 70},
                {"color": "red", "value": 90},
            ]),
        },
        "unit": unit,
    }
    if max_value is not None:
        defaults["max"] = max_value
    if decimals is not None:
        defaults["decimals"] = decimals
    # Bars render in frame order: topk/bottomk do not sort, so rank them
    # explicitly from an instant query (largest first / smallest first).
    targets = copy.deepcopy(targets)
    for t in targets:
        expr = t["expr"]
        if expr.startswith("topk("):
            t["expr"], t["instant"] = f"sort_desc({expr})", True
        elif expr.startswith("bottomk("):
            t["expr"], t["instant"] = f"sort({expr})", True
    return {
        "type": "bargauge",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {"defaults": defaults, "overrides": []},
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "displayMode": "gradient",
            "orientation": "horizontal",
            "namePlacement": "top",
            "valueMode": "text",
            "showUnfilled": True,
            # Fixed bar height keeps names visible and text legible whether
            # there are 2 items or 20 (the panel scrolls instead of shrinking).
            "sizing": "manual",
            "minVizHeight": 30,
            "maxVizHeight": 36,
            "text": {"titleSize": 12, "valueSize": 14},
            "minVizWidth": 8,
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "legend": {"calcs": [], "displayMode": "list", "placement": "bottom", "showLegend": False},
        },
        "transformations": transforms or [],
        "pluginVersion": PLUGIN_VERSION,
    }


def gauge(title, expr, x, y, w=6, h=8, unit="percentunit", desc="", min_value=0, max_value=1,
          thresholds=None):
    return {
        "type": "gauge",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": [tgt(expr)],
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": with_na([]),
                "noValue": NO_VALUE,
                "min": min_value,
                "max": max_value,
                "thresholds": {
                    "mode": "absolute",
                    "steps": neutral_base(thresholds or [
                        {"color": "green", "value": 0},
                        {"color": "yellow", "value": 0.6},
                        {"color": "red", "value": 0.85},
                    ]),
                },
                "unit": unit,
            },
            "overrides": [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "showThresholdLabels": False,
            "showThresholdMarkers": True,
            "sizing": "auto",
        },
        "pluginVersion": PLUGIN_VERSION,
    }


def piechart(title, targets, x, y, w=8, h=8, desc="", overrides=None, transforms=None):
    return {
        "type": "piechart",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {"hideFrom": {"legend": False, "tooltip": False, "viz": False}},
                "mappings": [],
            },
            "overrides": overrides or [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "pieType": "donut",
            "sort": "desc",
            "legend": {"displayMode": "table", "placement": "right", "showLegend": True, "values": ["value", "percent"]},
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "tooltip": {"hideZeros": False, "mode": "multi", "sort": "none"},
        },
        "transformations": transforms or [],
        "pluginVersion": PLUGIN_VERSION,
    }


def barchart(title, targets, x, y, w=12, h=8, unit="short", desc="", transforms=None, overrides=None):
    return {
        "type": "barchart",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "fillOpacity": 80,
                    "gradientMode": "none",
                    "lineWidth": 1,
                    "axisBorderShow": False,
                    "axisColorMode": "text",
                    "axisPlacement": "auto",
                    "scaleDistribution": {"type": "linear"},
                    "thresholdsStyle": {"mode": "off"},
                    "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                },
                "mappings": [],
                "unit": unit,
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": 0}]},
            },
            "overrides": overrides or [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "barRadius": 0.05,
            "barWidth": 0.7,
            "fullHighlight": False,
            "groupWidth": 0.7,
            "legend": {"displayMode": "list", "placement": "bottom", "showLegend": False},
            "orientation": "horizontal",
            "stacking": "none",
            "tooltip": {"hideZeros": False, "mode": "multi", "sort": "desc"},
            "xTickLabelRotation": -30,
            "xTickLabelSpacing": 100,
        },
        "transformations": transforms or [],
        "pluginVersion": PLUGIN_VERSION,
    }


def histogram(title, targets, x, y, w=12, h=8, unit="short", desc=""):
    return {
        "type": "histogram",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "palette-classic"},
                "custom": {
                    "fillOpacity": 80,
                    "gradientMode": "none",
                    "lineWidth": 1,
                    "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                },
                "unit": unit,
            },
            "overrides": [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "bucketSize": "auto",
            "combine": False,
            "fillOpacity": 80,
            "gradientMode": "none",
            "legend": {"displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"hideZeros": False, "mode": "single", "sort": "none"},
        },
        "pluginVersion": PLUGIN_VERSION,
    }


def state_timeline(title, targets, x, y, w=24, h=8, desc="", mappings=None, overrides=None):
    """0/1 state history. Grafana 13.0 state timelines ignore value mappings
    and label bars with threshold ranges ("-∞+", "1+"), so the colours come
    from thresholds built from the 0/1 mapping, value labels and legend are
    hidden, and the description names the colours (D4)."""
    mappings = mappings or UP_MAP
    opts = mappings[0]["options"]
    zero, one = opts["0"], opts["1"]
    desc = (desc + f" Colour key: {one['text']} = {_colour_name(one['color'])}, "
            f"{zero['text']} = {_colour_name(zero['color'])}.").strip()
    panel = {
        "type": "state-timeline",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "custom": {
                    "fillOpacity": 70,
                    "lineWidth": 0,
                    "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                },
                "mappings": with_na(mappings),
                "noValue": NO_VALUE,
                "thresholds": {"mode": "absolute", "steps": [
                    {"color": zero["color"], "value": None}, {"color": one["color"], "value": 1}]},
            },
            "overrides": overrides or [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "alignValue": "left",
            "mergeValues": True,
            "rowHeight": 0.8,
            "showValue": "never",
            "legend": {"displayMode": "list", "placement": "bottom", "showLegend": False},
            "tooltip": {"hideZeros": False, "mode": "single", "sort": "none"},
        },
        "pluginVersion": PLUGIN_VERSION,
    }
    return panel


def _colour_name(colour):
    return {"green": "green", "red": "red", "#808080": "grey", "yellow": "amber",
            "blue": "blue"}.get(colour, colour)


def table(title, targets, x, y, w=24, h=10, desc="", overrides=None, transforms=None, sort_col=None, sort_desc=True):
    options = {
        "cellHeight": "sm",
        "showHeader": True,
        "footer": {"show": False, "reducer": ["sum"], "fields": ""},
        "sortBy": [{"desc": sort_desc, "displayName": sort_col}] if sort_col else [],
    }
    return {
        "type": "table",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": targets,
        "fieldConfig": {
            "defaults": {
                "custom": {
                    "align": "auto",
                    "cellOptions": {"type": "auto"},
                    "filterable": True,
                    "footer": {"reducers": []},
                    "inspect": False,
                },
                "mappings": [],
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": 0}]},
            },
            "overrides": overrides or [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": options,
        "transformations": transforms or [],
        "pluginVersion": PLUGIN_VERSION,
    }


def text_panel(content, x, y, w=24, h=4):
    return {
        "type": "text",
        "id": IDS.next(),
        "title": "",
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "mode": "markdown",
            "content": content,
            "code": {"language": "plaintext", "showLineNumbers": False, "showMiniMap": False},
        },
        "pluginVersion": PLUGIN_VERSION,
    }


def row(title, y, collapsed=False, panels=None):
    return {
        "type": "row",
        "id": IDS.next(),
        "title": title,
        "collapsed": collapsed,
        "panels": panels or [],
        "gridPos": {"x": 0, "y": y, "w": 24, "h": 1},
    }


def table_target(expr, ref):
    return tgt(expr, ref=ref, fmt="table", instant=True)


def outer_join(field):
    return tf('joinByField', {'byField': field, 'mode': 'outer'})


# Plain yes/no attribute (autotrim, encryption, enablement): neither state
# is a fault, so "No" is neutral grey rather than red.
BOOL_MAP = [
    {
        "type": "value",
        "options": {
            "0": {"color": "#808080", "index": 0, "text": "No"},
            "1": {"color": "blue", "index": 1, "text": "Yes"},
        },
    }
]

UP_MAP = [
    {
        "type": "value",
        "options": {
            "0": {"color": "red", "index": 0, "text": "Down"},
            "1": {"color": "green", "index": 1, "text": "Up"},
        },
    }
]

GRAY = "#808080"


def bmap(one_text, one_color, zero_text, zero_color):
    """Explicit 0/1 value map.

    Replaces overloading a single BOOL_MAP (0=red "No" / 1=green "Yes") for
    three semantically different boolean kinds: security risks (bad when on),
    neutral capability/mode flags (off is not a fault), and required-action
    states (attention when set). Returns a fresh list per call.
    """
    return [{
        "type": "value",
        "options": {
            "0": {"color": zero_color, "index": 0, "text": zero_text},
            "1": {"color": one_color, "index": 1, "text": one_text},
        },
    }]


# Optional capability or mode: present = informational blue, absent = neutral
# gray. Off is expected/benign, never rendered as a red fault.
NEUTRAL_MAP = bmap("Yes", "blue", "No", GRAY)

# Mappings now live in the state-timeline defaults (D4); no overrides needed.
STATE_OVERRIDES: list = []
RUN_MAP = bmap("Running", "green", "Stopped", "#808080")

I = '$instance'
SEL = f'instance=~"{I}"'
# "Absence means zero" only while the exporter itself is up: an empty
# Prometheus or a dead exporter still reads N/A, never a green 0 (D7).
ZERO_IF_UP = f' or on() (0 * max(truenas_up{{{SEL}}} == 1))'
# D1: truenas_alert_count includes dismissed alerts.
OUTSTANDING_ALERTS = (
    f'clamp_min(sum(truenas_alert_count{{{SEL}}}) - '
    f'(sum(truenas_alert_dismissed_count{{{SEL}}}) or on() vector(0)), 0)'
)


# D14 (owner decision): show RAM both excluding and including the ZFS ARC.
# The ARC is reclaimable cache, so only the excl.-ARC figure carries
# warning thresholds; the incl.-ARC figure is informational.
RAM_EXCL_ARC = (
    f'100 * clamp_min(sum(truenas_memory_physical_used_bytes{{{SEL}}}) - '
    f'(sum(truenas_zfs_arc_size_bytes{{{SEL}}}) or on() vector(0)), 0) / '
    f'(sum(truenas_memory_physical_total_bytes{{{SEL}}}) > 0)'
)
RAM_INCL_ARC = (
    f'100 * sum(truenas_memory_physical_used_bytes{{{SEL}}}) / '
    f'(sum(truenas_memory_physical_total_bytes{{{SEL}}}) > 0)'
)
RAM_EXCL_ARC_DESC = ("Memory used by the OS, services, apps and VMs: used minus the ZFS ARC, as a share of "
                     "physical RAM. The ARC is cache that ZFS releases under pressure, so it is excluded here.")
DAYS_UNTIL_FULL = (
    f'truenas_pool_free_bytes{{{SEL}, pool=~"$pool"}} / '
    f'(deriv(truenas_pool_allocated_bytes{{{SEL}, pool=~"$pool"}}[7d]) > 0) / 86400'
)
# D3: directory service as one state; DISABLED is a choice, not a failure.
DIRSVC_STATE = (
    f'(0 * max(truenas_directoryservices_status{{{SEL}, status="DISABLED"}})) or '
    f'(1 * max(truenas_directoryservices_status{{{SEL}, status="HEALTHY"}})) or '
    f'(2 * max(truenas_directoryservices_status{{{SEL}, status=~"JOINING|LEAVING"}})) or '
    f'(3 * max(truenas_directoryservices_status{{{SEL}, status="FAULTED"}}))'
)
DIRSVC_MAP = [{"type": "value", "options": {
    "0": {"text": "Disabled", "color": "#808080", "index": 0},
    "1": {"text": "Healthy", "color": "green", "index": 1},
    "2": {"text": "Joining/leaving", "color": "yellow", "index": 2},
    "3": {"text": "Faulted", "color": "red", "index": 3},
}}]
DIRSVC_DESC = ("Directory service (AD/LDAP/IPA) state from directoryservices.status. Disabled is a deliberate "
               "choice and reads grey; only FAULTED is red.")
RAM_THRESHOLDS = [{"color": "green", "value": 0}, {"color": "yellow", "value": 80}, {"color": "red", "value": 92}]


def rate_pct(num, den, by=""):
    """D2: hit/miss percentages from realtime rates, never the upstream
    *_hit_ratio / *_hit_percentage fields (27.0 RC.1 sends 0). A zero
    denominator yields no sample (N/A) instead of a fake 0 %."""
    agg = f"sum{f' by ({by})' if by else ''}"
    return (f'100 * {agg} (truenas_zfs_{num}{{{SEL}}}) / '
            f'({agg} (truenas_zfs_{den}{{{SEL}}}) > 0)')


def disk_sel(metric, extra=""):
    """D6: per-disk series when the NAS reports them (25.10/26.0); otherwise
    the aggregate disk="total" series that 27.0 sends."""
    return (f'({metric}{{{SEL}, disk=~"$disk", disk!="total"{extra}}} or '
            f'({metric}{{{SEL}, disk="total"{extra}}} unless on (instance) '
            f'{metric}{{{SEL}, disk!="total"{extra}}}))')


# D13: a reported 0 degC means "no sensor" (e.g. USB bridges).
DISK_TEMP = f'(truenas_disk_temperature_celsius{{{SEL}, disk=~"$disk", disk!="total"}} > 0)'
DISK_27_NOTE = (" TrueNAS 27 reports aggregate disk I/O only; this then shows one"
                " \"total\" series, and per-disk filters do not apply.")


def reflow(panels, y, w=3, h=4, per_row=None):
    """Lay tiles left-to-right at a fixed width; returns the next free y."""
    per_row = per_row or 24 // w
    for i, p in enumerate(panels):
        p["gridPos"] = {"x": (i % per_row) * w, "y": y + (i // per_row) * h, "w": w, "h": h}
    return y + ((len(panels) + per_row - 1) // per_row) * h


def build_dashboard():
    IDS.value = 1
    panels = []
    y = 0

    panels.append(text_panel(
        "# TrueNAS Operations Center\n\n"
        "Comprehensive monitoring covering **system health, CPU, memory, ZFS pools & ARC, disks, network, "
        "services, shares, apps, VMs, boot environments, hardware, alerts, tasks, security posture, and exporter diagnostics**.\n\n"
        "> **Tip:** start with the *Instance* picker, then narrow by Pool, Dataset, Disk, Service, App or API Method. "
        "Collapsed detail rows keep the default view fast.",
        0, y, h=4,
    ))
    y += 4

    # ── ROW: Overview ───────────────────────────────────────────────────
    panels.append(row("System Overview", y))
    y += 1
    overview = [
        stat("Exporter", f'min(truenas_up{{instance=~"{I}"}})', 0, y, desc="Exporter can reach the TrueNAS API.", mappings=UP_MAP),
        stat("Ready", f'min(truenas_system_ready{{instance=~"{I}"}})', 0, y, desc="Middleware reports system ready.", mappings=bmap("Ready", "green", "Not ready", "red")),
        stat("Uptime", f'max(truenas_host_uptime_seconds{{instance=~"{I}"}})', 0, y, unit="s", decimals=1, color_mode="value", desc="Host uptime."),
        stat("Alerts", OUTSTANDING_ALERTS, 0, y,
             desc="Outstanding (not dismissed) alerts: alert_count minus alert_dismissed_count. truenas_alert_count includes dismissed alerts.",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Update", f'max(truenas_update_available{{instance=~"{I}"}})', 0, y, desc="TrueNAS update available.", mappings=bmap("⬆ Available", "yellow", "Current", "green")),
        stat("CPU Cores", f'max(truenas_host_cpu_cores{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Total CPU cores (incl. HT)."),
        stat("RAM", f'max(truenas_host_physical_memory_bytes{{instance=~"{I}"}})', 0, y, unit="bytes", color_mode="value", desc="Total physical RAM."),
        stat("Datasets", f'truenas_dataset_count{{instance=~"{I}"}}', 0, y, color_mode="value", desc="Number of datasets."),
        stat("CPU", f'avg(truenas_cpu_usage_percent{{instance=~"{I}"}})', 0, y, unit="percent", decimals=1,
             desc="Average CPU utilization.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 70}, {"color": "red", "value": 90}], graph=True),
        stat("RAM excl. ARC", RAM_EXCL_ARC, 0, y, unit="percent", decimals=1,
             desc=RAM_EXCL_ARC_DESC, thresholds=RAM_THRESHOLDS, graph=True),
        stat("Pool Used", f'100 * (sum(truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}}) / (sum(truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}}) > 0))', 0, y, unit="percent", decimals=1,
             desc="Aggregate pool utilization.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}], graph=True),
        stat("ARC Hit", rate_pct("demand_data_hits_per_second", "demand_data_accesses_per_second"), 0, y, unit="percent", decimals=1,
             desc="ZFS ARC demand-data hit rate, computed from hits/s ÷ accesses/s (the upstream hit-ratio field is unreliable on 27.0 RC.1).",
             thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
        stat("Load 1m", f'avg(truenas_host_load_average{{instance=~"{I}", window="1m"}})', 0, y, decimals=2, color_mode="value",
             desc="1-minute load average.", graph=True),
        stat("NFS Clients", f'sum(truenas_nfs_client_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Active NFS clients.", graph=True),
        stat("Update DL", f'max(truenas_update_download_progress_percent{{instance=~"{I}"}})', 0, y, unit="percent", color_mode="value",
             desc="Update download progress; N/A when no download is running."),
        stat("Scrape Time", f'max(truenas_scrape_duration_seconds{{instance=~"{I}"}})', 0, y, unit="s", decimals=1,
             desc="Exporter scrape duration.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 10}, {"color": "red", "value": 30}], graph=True),
    ]
    panels.extend(overview)
    y = reflow(overview, y)

    # ── ROW: CPU & Load ─────────────────────────────────────────────────
    panels.append(row("CPU & Load", y))
    y += 1
    panels.append(timeseries(
        "CPU Usage",
        [
            tgt(f'truenas_cpu_core_usage_percent{{instance=~"{I}"}}', 'Core {{core}}', 'A'),
            tgt(f'avg(truenas_cpu_usage_percent{{instance=~"{I}"}})', 'Total', 'B'),
        ],
        0, y, unit="percent", min_value=0, max_value=100,
        desc="Total and per-core CPU usage. Look for a single core pinned near 100 % (single-threaded bottleneck).",
        overrides=[{"matcher": {"id": "byName", "options": "Total"}, "properties": [
            {"id": "color", "value": {"mode": "fixed", "fixedColor": "blue"}},
            {"id": "custom.lineWidth", "value": 3}, {"id": "custom.fillOpacity", "value": 0}]}],
    ))
    panels.append(timeseries(
        "Load Average",
        [
            tgt(f'avg(truenas_host_load_average{{instance=~"{I}", window="1m"}})', 'Load 1m', 'A'),
            tgt(f'avg(truenas_host_load_average{{instance=~"{I}", window="5m"}})', 'Load 5m', 'B'),
            tgt(f'avg(truenas_host_load_average{{instance=~"{I}", window="15m"}})', 'Load 15m', 'C'),
            tgt(f'max(truenas_host_cpu_cores{{instance=~"{I}"}})', 'CPU cores', 'D'),
        ],
        12, y, unit="short",
        desc="Load average vs CPU core count. Load above core count means queueing.",
    ))
    y += 8
    panels.append(timeseries(
        "CPU Temperature per Core",
        [tgt(f'truenas_cpu_temperature_celsius{{instance=~"{I}"}}', 'Core {{core}}', 'A')],
        0, y, unit="celsius", fill=0,
        desc="Per-core CPU temperatures. Sustained high temps indicate cooling issues.",
        overrides=[{"matcher": {"id": "byType", "options": "number"}, "properties": [
            {"id": "thresholds", "value": {"mode": "absolute", "steps": [
                {"color": "green", "value": 0}, {"color": "yellow", "value": 70}, {"color": "red", "value": 85}
            ]}},
            {"id": "custom.thresholdsStyle", "value": {"mode": "line+area"}},
        ]}],
    ))
    panels.append(timeseries(
        "CPU Time Breakdown",
        [
            tgt(f'truenas_cpu_user_percent{{instance=~"{I}"}} >= 0', 'User', 'A'),
            tgt(f'truenas_cpu_system_percent{{instance=~"{I}"}} >= 0', 'System', 'B'),
            tgt(f'truenas_cpu_iowait_percent{{instance=~"{I}"}} >= 0', 'IOWait', 'C'),
            tgt(f'truenas_cpu_interrupt_percent{{instance=~"{I}"}} >= 0', 'IRQ', 'D'),
            tgt(f'truenas_cpu_idle_percent{{instance=~"{I}"}} >= 0', 'Idle', 'E'),
        ],
        12, y, w=12, unit="percent", stacked=True, min_value=0, max_value=100,
        no_value="Not reported by TrueNAS 27 (usage only)",
        desc="User/system/iowait/IRQ/idle split. TrueNAS 25.10 and 26.0 report it; 27.0 sends total usage only (NaN here), so the panel stays empty there by design (D11).",
    ))
    y += 8

    # ── ROW: Memory & Swap ──────────────────────────────────────────────
    panels.append(row("Memory & Swap", y))
    y += 1
    panels.extend([
        stat("Total RAM", f'truenas_memory_physical_total_bytes{{instance=~"{I}"}}', 0, y, w=4, unit="bytes", color_mode="value", desc="Total physical RAM."),
        stat("RAM excl. ARC", RAM_EXCL_ARC, 4, y, w=4, unit="percent", decimals=1, desc=RAM_EXCL_ARC_DESC, thresholds=RAM_THRESHOLDS, graph=True),
        stat("RAM incl. ARC", RAM_INCL_ARC, 8, y, w=4, unit="percent", decimals=1, color_mode="value",
             desc="Raw 'used' share as TrueNAS reports it, including the reclaimable ZFS ARC. Informational: high values are normal on a NAS.", graph=True),
        stat("Available", f'truenas_memory_physical_available_bytes{{instance=~"{I}"}}', 12, y, w=4, unit="bytes", color_mode="value", desc="Available RAM (free + reclaimable)."),
        stat("ARC Size", f'truenas_zfs_arc_size_bytes{{instance=~"{I}"}}', 16, y, w=4, unit="bytes", color_mode="value", desc="Current ZFS ARC size."),
        stat("ECC", f'max(truenas_host_ecc_memory{{instance=~"{I}"}})', 20, y, w=4, desc="ECC memory present.", mappings=bmap("Yes", "green", "No / not reported", GRAY)),
    ])
    y += 4
    panels.append(timeseries(
        "Memory Capacity Over Time",
        [
            tgt(f'truenas_memory_physical_total_bytes{{instance=~"{I}"}}', 'Total', 'A'),
            tgt(f'truenas_memory_physical_used_bytes{{instance=~"{I}"}}', 'Used (incl. ARC)', 'B'),
            tgt(f'truenas_memory_physical_available_bytes{{instance=~"{I}"}}', 'Available', 'C'),
            tgt(f'clamp_min(truenas_memory_physical_used_bytes{{instance=~"{I}"}} - on (instance) truenas_zfs_arc_size_bytes{{instance=~"{I}"}}, 0)', 'Used excl. ARC', 'D'),
        ],
        0, y, unit="bytes", stacked=False,
        desc="Physical memory from reporting.realtime. 'Used' includes the ZFS ARC; 'Used excl. ARC' is what services, apps and VMs hold.",
    ))
    panels.append(timeseries(
        "Documented ARC Memory Over Time",
        [
            tgt(f'truenas_zfs_arc_size_bytes{{instance=~"{I}"}}', 'ARC Size', 'A'),
            tgt(f'truenas_zfs_arc_available_bytes{{instance=~"{I}"}}', 'ARC Available', 'B'),
            tgt(f'truenas_zfs_arc_free_memory_bytes{{instance=~"{I}"}}', 'ARC Free', 'C'),
        ],
        12, y, unit="bytes",
        desc="ARC memory fields explicitly documented by reporting.realtime.",
    ))
    y += 8

    # ── ROW: Storage & Pools ────────────────────────────────────────────
    panels.append(row("Storage & Pools", y))
    y += 1
    panels.extend([
        stat("Pool Count", f'truenas_pool_count{{instance=~"{I}"}}', 0, y, w=3, color_mode="value", desc="Number of pools."),
        stat("All Healthy", f'min(truenas_pool_healthy{{instance=~"{I}", pool=~"$pool"}})', 3, y, w=3, desc="Lowest pool health.", mappings=UP_MAP),
        stat("Total Size", f'sum(truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}})', 6, y, w=3, unit="bytes", desc="Aggregate pool capacity."),
        stat("Total Free", f'sum(truenas_pool_free_bytes{{instance=~"{I}", pool=~"$pool"}})', 9, y, w=3, unit="bytes", desc="Aggregate free space."),
        stat("Snapshots", f'sum(truenas_snapshot_count{{instance=~"{I}"}})', 12, y, w=3, desc="Total ZFS snapshots."),
        stat("Oldest Snap", f'time() - truenas_snapshot_oldest_timestamp_seconds{{instance=~"{I}"}}', 15, y, w=3, unit="s",
             desc="Age of the oldest snapshot. Very old snapshots may waste space."),
        stat("Scrub Tasks", f'truenas_pool_scrub_task_count{{instance=~"{I}"}}', 18, y, w=3, desc="Configured scrub tasks."),
        stat("Boot Pool OK", f'min(truenas_boot_pool_healthy{{instance=~"{I}"}})', 21, y, w=3, desc="Boot pool health.", mappings=UP_MAP),
    ])
    y += 4
    panels.append(bargauge(
        "Days Until Full",
        [tgt(DAYS_UNTIL_FULL, '{{pool}}', 'A', instant=True)],
        0, y, w=12, h=6, unit="d", decimals=0, min_value=0, max_value=365,
        desc="Linear projection of each pool's allocation trend over the last 7 days (predict_linear-style: free ÷ growth rate). "
             "Pools that are flat or shrinking show N/A. Needs a few hours of history; treat short-range estimates as rough.",
        thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 30}, {"color": "green", "value": 90}],
    ))
    panels[-1]["fieldConfig"]["defaults"]["noValue"] = "Not growing"
    panels[-1]["options"]["displayMode"] = "basic"
    panels.append(timeseries("Pool Space Being Freed", [tgt(f'truenas_pool_freeing_bytes{{instance=~"{I}", pool=~"$pool"}}', '{{pool}}')], 12, y, w=12, h=6, unit="bytes", desc="Bytes being freed by ongoing operations on TrueNAS26/27. Missing on unsupported or unavailable sources."))
    y += 6
    panels.append(bargauge(
        "Pool Utilization",
        [tgt(f'100 * truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}} / (truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}} > 0)', '{{pool}}', 'A')],
        0, y, unit="percent", max_value=100, decimals=1,
        desc="Per-pool fill ratio. Pools above 80% suffer performance degradation.",
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}],
    ))
    panels.append(bargauge(
        "Top Dataset Utilization",
        [tgt(f'topk(10, 100 * truenas_dataset_used_bytes{{instance=~"{I}", dataset=~"$dataset"}} / clamp_min(truenas_dataset_used_bytes{{instance=~"{I}", dataset=~"$dataset"}} + truenas_dataset_available_bytes{{instance=~"{I}", dataset=~"$dataset"}}, 1))', '{{dataset}}', 'A')],
        12, y, unit="percent", max_value=100,
        desc="Datasets closest to filling their available space.",
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}],
    ))
    y += 8
    panels.append(timeseries(
        "Pool Capacity Trends",
        [
            tgt(f'truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} allocated', 'A'),
            tgt(f'truenas_pool_free_bytes{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} free', 'B'),
        ],
        0, y, unit="bytes",
        desc="Pool allocated and free space over time for capacity planning.",
    ))
    panels.append(timeseries(
        "Pool Fragmentation",
        [tgt(f'truenas_pool_fragmentation_percent{{instance=~"{I}", pool=~"$pool"}}', '{{pool}}', 'A')],
        12, y, w=6, unit="percent",
        desc="Pool fragmentation over time. High fragmentation degrades performance.",
    ))
    panels.append(timeseries(
        "Pool Scan Progress",
        [
            tgt(f'clamp_max(truenas_pool_scan_percent{{instance=~"{I}", pool=~"$pool"}}, 100)', '{{pool}}', 'A'),
        ],
        18, y, w=6, unit="percent", min_value=0, max_value=100,
        desc="Scrub/resilver progress per pool, clamped to 100 %: TrueNAS can report slightly over 100 % (e.g. 101.4) for a finished scan.",
    ))
    y += 8
    # Pool table with dedup/autotrim
    pool_table_targets = [
        table_target(f'max by (pool) (truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}})', 'A'),
        table_target(f'max by (pool) (truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}})', 'B'),
        table_target(f'max by (pool) (truenas_pool_free_bytes{{instance=~"{I}", pool=~"$pool"}})', 'C'),
        table_target(f'max by (pool) (truenas_pool_fragmentation_percent{{instance=~"{I}", pool=~"$pool"}})', 'D'),
        table_target(f'max by (pool) (truenas_pool_healthy{{instance=~"{I}", pool=~"$pool"}})', 'E'),
        table_target(f'100 * max by (pool) (truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}}) / clamp_min(max by (pool) (truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}}), 1)', 'F'),
        table_target(f'max by (pool) (truenas_pool_autotrim_enabled{{instance=~"{I}", pool=~"$pool"}})', 'H'),
        table_target(f'max by (pool) (truenas_pool_dedup_table_size_bytes{{instance=~"{I}", pool=~"$pool"}})', 'I'),
        table_target(f'max by (pool) (truenas_pool_expand_reflowed_bytes{{instance=~"{I}", pool=~"$pool"}})', 'K'),
        table_target(f'max by (pool) (truenas_pool_expand_to_reflow_bytes{{instance=~"{I}", pool=~"$pool"}})', 'L'),
    ]
    pool_table_transforms = [
        outer_join('pool'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {
                'pool': 'Pool', 'Value #A': 'Size', 'Value #B': 'Allocated', 'Value #C': 'Free',
                'Value #D': 'Frag %', 'Value #E': 'Healthy', 'Value #F': 'Used %',
                'Value #H': 'Autotrim', 'Value #I': 'DDT Size',
                'Value #K': 'Reflowed', 'Value #L': 'To Reflow',
            },
            'indexByName': {'Pool': 0, 'Used %': 1, 'Allocated': 2, 'Free': 3, 'Size': 4, 'Frag %': 5, 'DDT Size': 6, 'Reflowed': 7, 'To Reflow': 8, 'Autotrim': 9, 'Healthy': 10},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Used %', 'desc': True}]}),
    ]
    pool_overrides = [
        {"matcher": {"id": "byName", "options": "Used %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
        {"matcher": {"id": "byName", "options": "Healthy"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Healthy", "green", "Unhealthy", "red")}]},
        {"matcher": {"id": "byName", "options": "Autotrim"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        {"matcher": {"id": "byName", "options": "Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Allocated"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Free"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "DDT Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Reflowed"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "To Reflow"}, "properties": [{"id": "unit", "value": "bytes"}]},
    ]
    panels.append(table(
        "Pool Inventory", pool_table_targets, 0, y, h=7,
        desc="Pool capacity, health, dedup-table footprint, and active expansion progress.",
        overrides=pool_overrides, transforms=pool_table_transforms, sort_col='Used %',
    ))
    y += 7
    panels.append(timeseries(
        "Pool Expansion Progress",
        [tgt(f'truenas_pool_expand_percent{{instance=~"{I}", pool=~"$pool"}}', '{{pool}}', 'A')],
        0, y, unit="percent", desc="Completion percentage for active pool expansion reflow.",
        min_value=0, max_value=100, no_value="No expansion running",
    ))
    panels.append(timeseries(
        "Pool Realtime I/O",
        [
            tgt(f'truenas_pool_realtime_read_bytes_per_second{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} read', 'A'),
            tgt(f'truenas_pool_realtime_write_bytes_per_second{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} write', 'B'),
        ],
        12, y, unit="Bps", no_value="Not reported by TrueNAS 27",
        desc="Per-pool read/write throughput from reporting.realtime. TrueNAS 27.0 sends pool capacity only; see Disk Throughput for I/O on 27.",
    ))
    y += 8
    panels.extend([
        stat("Snap Task Max", f'max(truenas_snapshot_task_max_count{{instance=~"{I}"}})', 0, y, w=4, desc="Maximum number of snapshot tasks allowed."),
        stat("Snap Task Max Total", f'max(truenas_snapshot_task_max_total_count{{instance=~"{I}"}})', 4, y, w=4, desc="Maximum total snapshot tasks allowed."),
        stat("Scrub Enabled", f'count(truenas_pool_scrub_task_enabled{{instance=~"{I}", pool=~"$pool"}} == 1)', 8, y, w=4, desc="Pools with an enabled scrub task."),
        stat("Pools Warning", f'sum(truenas_pool_warning{{instance=~"{I}", pool=~"$pool"}})', 12, y, w=4,
             desc="Pools currently flagging a warning.", thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("Scanning Now", f'count(truenas_pool_scan_seconds_remaining{{instance=~"{I}", pool=~"$pool"}} > 0)' + ZERO_IF_UP, 16, y, w=4, color_mode="value", desc="Pools with an active scrub/resilver scan (0 when none is running)."),
        stat("Oldest Scan", f'time() - min(truenas_pool_last_scan_timestamp_seconds{{instance=~"{I}", pool=~"$pool"}})', 20, y, w=4, unit="s", desc="Age of the least-recently-scanned pool."),
    ])
    y += 4
    pool_status_table_targets = [
        table_target(f'max by (pool, status) (truenas_pool_status{{instance=~"{I}", pool=~"$pool"}})', 'A'),
        table_target(f'max by (pool, status_code) (truenas_pool_status_code{{instance=~"{I}", pool=~"$pool"}})', 'B'),
        table_target(f'max by (pool) (truenas_pool_warning{{instance=~"{I}", pool=~"$pool"}})', 'C'),
        table_target(f'max by (pool) (truenas_pool_scrub_task_enabled{{instance=~"{I}", pool=~"$pool"}})', 'D'),
        table_target(f'time() - max by (pool) (truenas_pool_last_scan_timestamp_seconds{{instance=~"{I}", pool=~"$pool"}})', 'E'),
    ]
    panels.append(table(
        "Pool Status & Scrub Detail", pool_status_table_targets, 0, y, h=6,
        desc="Pool status enum, v26 detailed status_code, warning flag, scrub-task enablement, and time since last scan.",
        transforms=[
            outer_join('pool'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value #A': True, 'Value #B': True},
                'renameByName': {
                    'pool': 'Pool', 'status': 'Status', 'status_code': 'Status Code',
                    'Value #C': 'Warning', 'Value #D': 'Scrub Enabled', 'Value #E': 'Since Last Scan',
                },
                'indexByName': {'Pool': 0, 'Status': 1, 'Status Code': 2, 'Warning': 3, 'Scrub Enabled': 4, 'Since Last Scan': 5},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Pool', 'desc': False}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Warning"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("⚠ Warning", "yellow", "OK", "green")}]},
            {"matcher": {"id": "byName", "options": "Scrub Enabled"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Yes", "green", "No", "yellow")}]},
            {"matcher": {"id": "byName", "options": "Since Last Scan"}, "properties": [{"id": "unit", "value": "s"}]},
        ],
        sort_col='Pool', sort_desc=False,
    ))
    y += 6
    panels.append(timeseries(
        "Pool Scan Bytes Progress",
        [
            tgt(f'truenas_pool_scan_bytes_processed{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} processed', 'A'),
            tgt(f'truenas_pool_scan_bytes_total{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} total', 'B'),
        ],
        0, y, unit="bytes", desc="Bytes processed vs. total for the last/active pool scrub or resilver scan.",
    ))
    panels.append(timeseries(
        "Pool Realtime Capacity",
        [
            tgt(f'truenas_pool_realtime_available_bytes{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} available', 'A'),
            tgt(f'truenas_pool_realtime_total_bytes{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} total', 'B'),
            tgt(f'truenas_pool_realtime_used_bytes{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} used', 'C'),
        ],
        12, y, unit="bytes", desc="Per-pool capacity from the reporting.realtime event stream.",
    ))
    y += 8
    panels.append(timeseries(
        "Pool Scan ETA",
        [tgt(f'truenas_pool_scan_seconds_remaining{{instance=~"{I}", pool=~"$pool"}}', '{{pool}}', 'A')],
        0, y, unit="s", desc="Estimated seconds remaining in the active pool scan.",
    ))
    panels.append(timeseries(
        "Pool Scan Errors",
        [tgt(f'truenas_pool_scan_errors{{instance=~"{I}", pool=~"$pool"}}', '{{pool}}', 'A')],
        12, y, unit="short", bars=True,
        desc="Errors found during the last/active pool scan.",
    ))
    y += 8

    # ── ROW: ZFS ARC & Cache ────────────────────────────────────────────
    panels.append(row("ZFS ARC & Cache", y))
    y += 1
    panels.extend([
        stat("ARC Size", f'truenas_zfs_arc_size_bytes{{instance=~"{I}"}}', 0, y, w=4, unit="bytes",
             desc="Current documented ZFS ARC cache size.", graph=True),
        stat("ARC Free", f'truenas_zfs_arc_free_memory_bytes{{instance=~"{I}"}}', 4, y, w=4, unit="bytes", desc="ARC-reported free memory."),
        stat("ARC Avail", f'truenas_zfs_arc_available_bytes{{instance=~"{I}"}}', 8, y, w=4, unit="bytes", desc="ARC-reported available memory."),
        stat("L2ARC Hit %", rate_pct("l2arc_hits_per_second", "l2arc_accesses_per_second"), 12, y, w=4, unit="percent", decimals=1, color_mode="value",
             desc="L2ARC hits/s ÷ accesses/s. N/A when there is no L2ARC device or no L2ARC traffic.", graph=True),
        stat("Data Hit %", rate_pct("demand_data_hits_per_second", "demand_data_accesses_per_second"), 16, y, w=4, unit="percent", decimals=1,
             desc="Demand-data hits/s ÷ accesses/s (computed from rates; the upstream ratio field reads 0 on 27.0 RC.1).", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
        stat("Meta Hit %", rate_pct("demand_meta_hits_per_second", "demand_metadata_accesses_per_second"), 20, y, w=4, unit="percent", decimals=1,
             desc="Demand-metadata hits/s ÷ accesses/s (computed from rates).", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
    ])
    y += 4
    panels.append(timeseries(
        "Demand Hit & Miss Rates",
        [
            tgt(f'truenas_zfs_demand_data_hits_per_second{{instance=~"{I}"}}', 'Data hits/s', 'A'),
            tgt(f'truenas_zfs_demand_data_misses_per_second{{instance=~"{I}"}}', 'Data misses/s', 'B'),
            tgt(f'truenas_zfs_demand_meta_hits_per_second{{instance=~"{I}"}}', 'Metadata hits/s', 'C'),
            tgt(f'truenas_zfs_demand_meta_misses_per_second{{instance=~"{I}"}}', 'Metadata misses/s', 'D'),
        ],
        0, y, unit="ops",
        desc="Documented ARC demand-data and demand-metadata hit and miss rates.",
    ))
    panels.append(timeseries(
        "ARC Memory Headroom",
        [
            tgt(f'truenas_zfs_arc_free_memory_bytes{{instance=~"{I}"}}', 'Free', 'A'),
            tgt(f'truenas_zfs_arc_available_bytes{{instance=~"{I}"}}', 'Available', 'B'),
        ],
        12, y, unit="bytes",
        desc="Documented ARC free and available memory fields.",
    ))
    y += 8
    panels.append(timeseries(
        "Demand & L2ARC Hit Ratios",
        [
            tgt(rate_pct("l2arc_hits_per_second", "l2arc_accesses_per_second"), 'L2ARC hit %', 'A'),
            tgt(rate_pct("demand_data_hits_per_second", "demand_data_accesses_per_second"), 'Data hit %', 'B'),
            tgt(rate_pct("demand_meta_hits_per_second", "demand_metadata_accesses_per_second"), 'Meta hit %', 'C'),
        ],
        0, y, w=8, unit="percent", min_value=0, max_value=100,
        desc="Cache hit percentages computed from hits/s ÷ accesses/s. Higher is better; gaps mean no accesses in that interval.",
    ))
    panels.append(timeseries(
        "Demand Data & Metadata Rates",
        [
            tgt(f'truenas_zfs_demand_data_accesses_per_second{{instance=~"{I}"}}', 'Data accesses/s', 'A'),
            tgt(f'truenas_zfs_demand_data_hits_per_second{{instance=~"{I}"}}', 'Data hits/s', 'B'),
            tgt(f'truenas_zfs_demand_metadata_accesses_per_second{{instance=~"{I}"}}', 'Meta accesses/s', 'C'),
            tgt(f'truenas_zfs_demand_meta_hits_per_second{{instance=~"{I}"}}', 'Meta hits/s', 'D'),
            tgt(f'truenas_zfs_demand_data_io_hits_per_second{{instance=~"{I}"}}', 'Data I/O hits/s', 'E'),
            tgt(f'truenas_zfs_demand_metadata_io_hits_per_second{{instance=~"{I}"}}', 'Metadata I/O hits/s', 'F'),
        ],
        8, y, w=8, unit="ops",
        desc="Demand access rates for data and metadata, including I/O-level hit rates.",
    ))
    panels.append(timeseries(
        "L2ARC Throughput",
        [
            tgt(f'truenas_zfs_l2arc_read_bytes_per_second{{instance=~"{I}"}}', 'L2ARC read', 'A'),
            tgt(f'truenas_zfs_l2arc_write_bytes_per_second{{instance=~"{I}"}}', 'L2ARC write', 'B'),
        ],
        16, y, w=8, unit="Bps",
        desc="L2ARC I/O. High write with low hit ratio signals cache churn.",
    ))
    y += 8

    # ── ROW: Disks & Temperatures ───────────────────────────────────────
    panels.append(row("Disks & Temperatures", y))
    y += 1
    panels.extend([
        stat("Disk Count", f'truenas_disk_count{{instance=~"{I}"}}', 0, y, w=8, color_mode="value", desc="Number of disks."),
        stat("Hottest Disk", f'max({DISK_TEMP})', 8, y, w=8, unit="celsius", decimals=0,
             desc="Highest disk temperature. Disks reporting 0 °C (no sensor, e.g. USB bridges) are ignored.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 45}, {"color": "red", "value": 55}], graph=True),
        stat("Avg Busy", f'avg({disk_sel("truenas_disk_busy_percent")})', 16, y, w=8, unit="percent", decimals=1,
             desc="Average disk busy %." + DISK_27_NOTE, thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 60}, {"color": "red", "value": 85}], graph=True),
    ])
    y += 4
    panels.append(timeseries(
        "Disk Throughput by Device",
        [
            tgt(f'topk(8, {disk_sel("truenas_disk_read_bytes_per_second")})', 'read {{disk}}', 'A'),
            tgt(f'-1 * topk(8, {disk_sel("truenas_disk_write_bytes_per_second")})', 'write {{disk}}', 'B'),
        ],
        0, y, unit="Bps", desc="Read (up) and write (down) throughput for the busiest devices." + DISK_27_NOTE,
    ))
    panels.append(timeseries(
        "Disk IOPS by Device",
        [
            tgt(f'topk(8, {disk_sel("truenas_disk_read_ops_per_second")})', 'read {{disk}}', 'A'),
            tgt(f'-1 * topk(8, {disk_sel("truenas_disk_write_ops_per_second")})', 'write {{disk}}', 'B'),
        ],
        12, y, unit="iops", desc="Read (up) and write (down) IOPS per device." + DISK_27_NOTE,
    ))
    y += 8
    panels.append(timeseries(
        "Disk Busy %",
        [tgt(f'topk(8, {disk_sel("truenas_disk_busy_percent")})', '{{disk}}', 'A')],
        0, y, unit="percent", min_value=0, max_value=100, desc="Disk utilization saturation." + DISK_27_NOTE,
    ))
    panels.append(timeseries(
        "Disk Temperature Over Time",
        [tgt(DISK_TEMP, '{{disk}}', 'A')],
        12, y, unit="celsius", fill=0, desc="Per-disk temperatures over time (0 °C readings = no sensor, hidden).",
    ))
    y += 8
    panels.append(bargauge(
        "Disk Temperatures",
        [tgt(f'sort_desc({DISK_TEMP})', '{{disk}}', 'A', instant=True)],
        0, y, unit="celsius", decimals=0, max_value=70,
        desc="Current temperature per disk, hottest first. Disks reporting 0 °C (no sensor) are omitted.",
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 45}, {"color": "red", "value": 55}],
    ))
    panels.append(bargauge(
        "Disk Sizes",
        [tgt(f'sort_desc(truenas_disk_size_bytes{{instance=~"{I}", disk=~"$disk", disk!="total"}})', '{{disk}}', 'A', instant=True)],
        12, y, unit="bytes", desc="Raw capacity per disk, largest first.",
        thresholds=[{"color": "blue", "value": None}],
    ))
    y += 8
    # Disk inventory table with documented performance and rotational fields.
    disk_table_targets = [
        table_target(f'max by (disk) (truenas_disk_size_bytes{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'A'),
        table_target(f'max by (disk) (truenas_disk_busy_percent{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'B'),
        table_target(f'max by (disk) ({DISK_TEMP})', 'C'),
        table_target(f'max by (disk) (truenas_disk_read_bytes_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'D'),
        table_target(f'max by (disk) (truenas_disk_write_bytes_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'E'),
        table_target(f'max by (disk) (truenas_disk_read_ops_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'F'),
        table_target(f'max by (disk) (truenas_disk_write_ops_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'G'),
        table_target(f'max by (disk) (truenas_disk_rotational{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'H'),
    ]
    disk_table_transforms = [
        outer_join('disk'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {
                'disk': 'Disk', 'Value #A': 'Size', 'Value #B': 'Busy %', 'Value #C': 'Temp C',
                'Value #D': 'Read B/s', 'Value #E': 'Write B/s', 'Value #F': 'Read IOPS', 'Value #G': 'Write IOPS',
                'Value #H': 'HDD',
            },
            'indexByName': {'Disk': 0, 'Busy %': 1, 'Temp C': 2, 'Read B/s': 3, 'Write B/s': 4, 'Read IOPS': 5, 'Write IOPS': 6, 'Size': 7, 'HDD': 8},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Busy %', 'desc': True}]}),
    ]
    disk_overrides = [
        {"matcher": {"id": "byName", "options": "Busy %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 60}, {"color": "red", "value": 85}]}}]},
        {"matcher": {"id": "byName", "options": "Temp C"}, "properties": [{"id": "unit", "value": "celsius"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 45}, {"color": "red", "value": 55}]}}]},
        {"matcher": {"id": "byName", "options": "Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Read B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
        {"matcher": {"id": "byName", "options": "Write B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
        {"matcher": {"id": "byName", "options": "Read IOPS"}, "properties": [{"id": "unit", "value": "iops"}]},
        {"matcher": {"id": "byName", "options": "Write IOPS"}, "properties": [{"id": "unit", "value": "iops"}]},
        {"matcher": {"id": "byName", "options": "HDD"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": [{"type": "value", "options": {"0": {"color": "blue", "text": "SSD/NVMe"}, "1": {"color": "purple", "text": "HDD"}}}]}]},
    ]
    panels.append(table(
        "Disk Inventory", disk_table_targets, 0, y,
        desc="Per-disk capacity, performance, temperature and media type. On TrueNAS 27 the busy/throughput/IOPS columns are absent because 27 reports aggregate disk I/O only; temperature 0 °C (no sensor) is left blank.",
        overrides=disk_overrides, transforms=disk_table_transforms, sort_col='Busy %',
    ))
    y += 10
    panels.append(table(
        "Disk Identity",
        [table_target(f'truenas_disk_info{{instance=~"{I}", disk=~"$disk"}}', 'A')],
        0, y, w=12, h=8,
        desc="Disk model, serial number, and bus for each device.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {'disk': 'Disk', 'model': 'Model', 'serial': 'Serial', 'bus': 'Bus'},
                'indexByName': {'Disk': 0, 'Model': 1, 'Serial': 2, 'Bus': 3},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Disk', 'desc': False}]}),
        ],
        sort_col='Disk', sort_desc=False,
    ))
    panels.append(timeseries(
        "Peak Disk Temperature (~5 min max)",
        [tgt(f'truenas_disk_temperature_agg_celsius{{instance=~"{I}", disk=~"$disk", kind="max"}} > 0', '{{disk}}', 'A')],
        12, y, w=12, unit="celsius", fill=0,
        desc="Per-disk maximum from the aggregated (min/avg/max) temperature query, refreshed on the heavy-query cadence. Catches short spikes the instant reading misses.",
    ))
    y += 8

    # ── ROW: Network & Interfaces ───────────────────────────────────────
    panels.append(row("Network & Interfaces", y))
    y += 1
    panels.extend([
        stat("Interfaces", f'truenas_interface_count{{instance=~"{I}"}}', 0, y, w=3, desc="Network interface count."),
        stat("Gateway Config", f'max(truenas_network_default_gateway_configured{{instance=~"{I}"}})', 3, y, w=3, desc="Applied default route is configured.", mappings=bmap("Yes", "green", "No", "yellow")),
        stat("Nameservers", f'truenas_network_nameservers{{instance=~"{I}"}}', 6, y, w=3, desc="Configured nameservers."),
        stat("Default Routes", f'truenas_network_default_routes{{instance=~"{I}"}}', 9, y, w=3, desc="Number of default routes."),
        stat("DNS Resolvers", f'truenas_dns_resolver_count{{instance=~"{I}"}}', 12, y, w=3, desc="Configured DNS resolvers."),
        stat("Pending Changes", f'max(truenas_interface_has_pending_changes{{instance=~"{I}"}})', 15, y, w=3, desc="Unapplied network interface changes.", mappings=bmap("Pending", "orange", "None", "green")),
        stat("Checkin Wait", f'max(truenas_interface_checkin_waiting_seconds{{instance=~"{I}"}})', 18, y, w=3, unit="s", color_mode="value", desc="Seconds until pending network changes auto-rollback; N/A when nothing is pending."),
    ])
    y += 4
    panels.append(timeseries(
        "Network RX by Interface",
        [tgt(f'truenas_network_rx_bytes_per_second{{instance=~"{I}", interface=~"$interface"}}', '{{interface}} RX', 'A')],
        0, y, unit="Bps", desc="Per-interface receive throughput.",
    ))
    panels.append(timeseries(
        "Network TX by Interface",
        [tgt(f'truenas_network_tx_bytes_per_second{{instance=~"{I}", interface=~"$interface"}}', '{{interface}} TX', 'A')],
        12, y, unit="Bps", desc="Per-interface transmit throughput.",
    ))
    y += 8
    panels.append(state_timeline(
        "Interface Link State",
        [tgt(f'truenas_interface_link_up{{instance=~"{I}", interface=~"$interface"}}', '{{interface}}', 'A')],
        0, y, w=12, desc="Link up/down history. Down on an unused port is normal.", mappings=bmap("Up", "green", "Down", "#808080"),
    ))
    panels.append(bargauge(
        "Interface MTU",
        [tgt(f'truenas_interface_mtu{{instance=~"{I}", interface=~"$interface"}}', '{{interface}}', 'A')],
        12, y, unit="none", decimals=0, desc="MTU per interface (bytes; 1500 standard, 9000 jumbo).",
        thresholds=[{"color": "blue", "value": None}],
    ))
    y += 8
    panels.append(state_timeline(
        "Interface Realtime Link State",
        [tgt(f'truenas_interface_realtime_link_up{{instance=~"{I}", interface=~"$interface"}}', '{{interface}}', 'A')],
        0, y, w=12, desc="Link up/down from the reporting.realtime event stream.", mappings=bmap("Up", "green", "Down", "#808080"),
    ))
    panels.append(timeseries(
        "Interface Realtime Speed",
        [tgt(f'truenas_interface_realtime_speed_mbits{{instance=~"{I}", interface=~"$interface"}}', '{{interface}}', 'A')],
        12, y, w=12, unit="Mbits", desc="Negotiated link speed from reporting.realtime.",
    ))
    y += 8
    panels.append(table(
        "Interface Types",
        [table_target(f'truenas_interface_type{{instance=~"{I}", interface=~"$interface"}}', 'A')],
        0, y, w=24, h=6,
        desc="Interface type (PHYSICAL/BRIDGE/etc) per interface.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {'interface': 'Interface', 'type': 'Type'},
                'indexByName': {'Interface': 0, 'Type': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Interface', 'desc': False}]}),
        ],
        sort_col='Interface', sort_desc=False,
    ))
    y += 6

    # ── ROW: Services & Shares ──────────────────────────────────────────
    panels.append(row("Services & Shares", y))
    y += 1
    share_tiles = [
        stat("Services", f'truenas_service_count{{instance=~"{I}"}}', 0, y, color_mode="value", desc="Total services."),
        stat("Running", f'count(truenas_service_running{{instance=~"{I}", service=~"$service"}} == 1)' + ZERO_IF_UP, 0, y, color_mode="value", desc="Running services."),
        stat("SMB Shares", f'sum(truenas_smb_share_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Configured SMB shares."),
        stat("NFS Shares", f'sum(truenas_nfs_share_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Configured NFS shares."),
        stat("iSCSI Targets", f'sum(truenas_iscsi_target_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="iSCSI targets."),
        stat("SMB Sessions", f'sum(truenas_smb_session_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Active SMB sessions (live, from smb.status).", graph=True),
        stat("NFS Clients", f'sum(truenas_nfs_client_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Active NFS clients.", graph=True),
        stat("iSCSI Clients", f'sum(truenas_iscsi_client_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="iSCSI clients.", graph=True),
        stat("NFS v3", f'sum(truenas_nfs_v3_client_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="NFSv3 clients.", graph=True),
        stat("NFS v4", f'sum(truenas_nfs_v4_client_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="NFSv4 clients.", graph=True),
        stat("NVMe-oF", f'sum(truenas_nvmet_session_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="NVMe-oF sessions; N/A when NVMe-oF is not configured.", graph=True),
        stat("SMB Conns", f'sum(truenas_smb_connection_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Active SMB tree connections (live, from smb.status).", graph=True),
        stat("Open Files", f'sum(truenas_smb_open_file_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Open SMB file locks (live, from smb.status).", graph=True),
        stat("SMB1", f'max(truenas_smb1_enabled{{instance=~"{I}"}})', 0, y, desc="Legacy SMB1 protocol enabled (insecure when on).", mappings=bmap("⚠ Enabled", "red", "Disabled", "green")),
        stat("NTLMv1", f'max(truenas_smb_ntlmv1_auth_enabled{{instance=~"{I}"}})', 0, y, desc="Insecure NTLMv1 authentication enabled.", mappings=bmap("⚠ Enabled", "red", "Disabled", "green")),
        stat("NFS RDMA", f'max(truenas_nfs_rdma_enabled{{instance=~"{I}"}})', 0, y, desc="NFS over RDMA enabled.", mappings=NEUTRAL_MAP),
        stat("WebShares", f'sum(truenas_webdav_share_count{{instance=~"{I}"}})', 0, y, color_mode="value", desc="Configured WebShare (WebDAV) shares (v26+)."),
        stat("WebShare Auth", f'max(truenas_webshare_enabled{{instance=~"{I}"}})', 0, y,
             desc="WebShare passkey authentication enabled (v26+).", mappings=bmap("Enabled", "green", "Disabled", GRAY)),
        stat("SMB Encryption", f'max by (mode) (truenas_smb_encryption_mode{{instance=~"{I}"}})', 0, y, legend="{{mode}}", text_mode="name", color_mode="value",
             desc="Configured SMB transport-encryption mode."),
    ]
    panels.extend(share_tiles)
    y = reflow(share_tiles, y, w=3, per_row=8)
    panels.append(state_timeline(
        "Service Runtime State",
        [tgt(f'truenas_service_running{{instance=~"{I}", service=~"$service"}}', '{{service}}', 'A')],
        0, y, w=12, desc="Service running/stopped history. Stopped is normal for services you do not use.", mappings=RUN_MAP,
    ))
    panels.append(piechart(
        "Protocol Activity Mix",
        [
            tgt(f'sum(truenas_nfs_client_count{{instance=~"{I}"}})', 'NFS', 'A'),
            tgt(f'sum(truenas_iscsi_client_count{{instance=~"{I}"}})', 'iSCSI', 'B'),
            tgt(f'sum(truenas_nvmet_session_count{{instance=~"{I}"}})', 'NVMe-oF', 'C'),
        ],
        12, y, w=12, desc="Relative protocol activity.",
    ))
    y += 8
    # iSCSI detail stats
    panels.extend([
        stat("Portals", f'sum(truenas_iscsi_portal_count{{instance=~"{I}"}})', 0, y, w=3, desc="iSCSI portals."),
        stat("Extents", f'sum(truenas_iscsi_extent_count{{instance=~"{I}"}})', 3, y, w=3, desc="iSCSI extents."),
        stat("Initiators", f'sum(truenas_iscsi_initiator_count{{instance=~"{I}"}})', 6, y, w=3, desc="iSCSI initiator groups."),
        stat("iSCSI Sess", f'sum(truenas_iscsi_session_count{{instance=~"{I}"}})', 9, y, w=3, desc="Active iSCSI sessions."),
        stat("ALUA", f'max(truenas_iscsi_alua_enabled{{instance=~"{I}"}})', 12, y, w=3, desc="iSCSI ALUA protocol (optional).", mappings=NEUTRAL_MAP),
        stat("iSER", f'max(truenas_iscsi_iser_enabled{{instance=~"{I}"}})', 15, y, w=3, desc="iSCSI iSER (RDMA) protocol (optional).", mappings=NEUTRAL_MAP),
        stat("SMB Multi", f'max(truenas_smb_multichannel_enabled{{instance=~"{I}"}})', 18, y, w=3, desc="SMB multichannel (optional).", mappings=NEUTRAL_MAP),
        stat("NFSv4 On", f'max(truenas_nfs_v4_enabled{{instance=~"{I}"}})', 21, y, w=3, desc="NFSv4 enabled (optional).", mappings=NEUTRAL_MAP),
    ])
    y += 4
    panels.extend([
        stat("iSER Sess", f'sum(truenas_iscsi_session_iser_count{{instance=~"{I}"}})', 0, y, w=4, desc="Active iSCSI sessions using iSER."),
        stat("Offload Sess", f'sum(truenas_iscsi_session_offload_count{{instance=~"{I}"}})', 4, y, w=5, desc="Active iSCSI sessions using offload."),
        stat("ImmediateData", f'sum(truenas_iscsi_session_immediate_data_count{{instance=~"{I}"}})', 9, y, w=5, desc="Active iSCSI sessions with immediate-data enabled."),
        stat("NFS Threads", f'max(truenas_nfs_servers{{instance=~"{I}"}})', 14, y, w=5, desc="NFS server threads."),
        stat("Used Disks", f'count(truenas_disk_in_use{{instance=~"{I}", disk=~"$disk"}} == 1)', 19, y, w=5, desc="Disks currently in use by pools."),
    ])
    y += 4
    # Service inventory table
    service_table_targets = [
        table_target(f'max by (service) (truenas_service_running{{instance=~"{I}", service=~"$service"}})', 'A'),
        table_target(f'max by (service) (truenas_service_enabled{{instance=~"{I}", service=~"$service"}})', 'B'),
    ]
    service_table_transforms = [
        outer_join('service'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {'service': 'Service', 'Value #A': 'Running', 'Value #B': 'Enabled'},
            'indexByName': {'Service': 0, 'Running': 1, 'Enabled': 2},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Service', 'desc': False}]}),
    ]
    service_overrides = [
        {"matcher": {"id": "byName", "options": "Running"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": RUN_MAP}]},
        {"matcher": {"id": "byName", "options": "Enabled"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
    ]
    panels.append(table(
        "Service Inventory", service_table_targets, 0, y,
        desc="Service runtime state and boot enablement.",
        overrides=service_overrides, transforms=service_table_transforms, sort_col='Service', sort_desc=False,
    ))
    y += 10

    # ── ROW: Apps & Docker ──────────────────────────────────────────────
    panels.append(row("Apps & Docker", y))
    y += 1
    panels.extend([
        stat("Apps", f'sum(truenas_app_count{{instance=~"{I}"}})', 0, y, w=3, desc="Installed apps."),
        stat("Avail Space", f'truenas_app_available_space_bytes{{instance=~"{I}"}}', 3, y, w=3, unit="bytes", desc="Space available for new apps."),
        stat("Docker Imgs", f'sum(truenas_docker_image_count{{instance=~"{I}"}})', 6, y, w=3, desc="Docker images."),
        stat("Docker Nets", f'sum(truenas_docker_network_count{{instance=~"{I}"}})', 9, y, w=3, desc="Docker networks."),
        stat("Docker Up", f'max(truenas_docker_status{{instance=~"{I}", status="RUNNING"}})', 12, y, w=3, desc="Docker service running.", mappings=UP_MAP),
        stat("NVIDIA GPU", f'max(truenas_docker_nvidia_present{{instance=~"{I}"}})', 15, y, w=3, desc="NVIDIA GPU available.", mappings=bmap("Yes", "green", "Not present", GRAY)),
        stat("Catalog Trains", f'truenas_catalog_train_count{{instance=~"{I}"}}', 18, y, w=3, desc="App catalog trains."),
        stat("Pref Trains", f'max(truenas_catalog_preferred_train_count{{instance=~"{I}"}})', 21, y, w=3, desc="Preferred catalog trains configured."),
    ])
    y += 4
    panels.extend([
        stat(
            "DH RL Error",
            f'max(truenas_app_dockerhub_rate_limit_error_present{{instance=~"{I}"}})',
            0,
            y,
            w=4,
            mappings=bmap("Error", "yellow", "None", "green"),
            desc="DockerHub rate-limit endpoint currently reports an error.",
        ),
        stat(
            "DH Rem %",
            f'100 * max(truenas_app_dockerhub_pull_limit_remaining{{instance=~"{I}"}}) / '
            f'clamp_min(max(truenas_app_dockerhub_pull_limit_total{{instance=~"{I}"}}), 1)',
            4,
            y,
            w=5,
            unit="percent",
            thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 20}, {"color": "green", "value": 50}],
            desc="DockerHub pull-limit budget remaining percentage.",
        ),
        stat("DockerHub Rem", f'max(truenas_app_dockerhub_pull_limit_remaining{{instance=~"{I}"}})', 9, y, w=5, desc="DockerHub pull requests remaining in current window."),
        stat("DockerHub Limit", f'max(truenas_app_dockerhub_pull_limit_total{{instance=~"{I}"}})', 14, y, w=5, desc="DockerHub pull limit window total requests."),
        stat("DH Window Left", f'max(truenas_app_dockerhub_pull_limit_remaining_window_seconds{{instance=~"{I}"}})', 19, y, w=5, unit="s", desc="Seconds remaining in the current DockerHub pull-limit window."),
    ])
    y += 4
    panels.extend([
        stat("App Upgrades", f'sum(truenas_app_upgrade_available{{instance=~"{I}", app=~"$app"}})', 0, y, w=6,
             desc="Apps with a newer chart or package version available."),
        stat("Custom Apps", f'sum(truenas_app_custom{{instance=~"{I}", app=~"$app"}})', 6, y, w=6,
             desc="Apps deployed as custom apps."),
        stat("Migrated Apps", f'sum(truenas_app_migrated{{instance=~"{I}", app=~"$app"}})', 12, y, w=6,
             desc="Apps migrated from the older Kubernetes stack."),
        stat("Img Updates", f'sum(truenas_app_image_updates_available{{instance=~"{I}", app=~"$app"}})', 18, y, w=6,
             desc="Apps with container image updates available."),
    ])
    y += 4
    panels.append(bargauge(
        "Top Apps by CPU",
        [tgt(f'topk(10, truenas_app_cpu_percent{{instance=~"{I}", app=~"$app"}})', '{{app}}', 'A')],
        0, y, unit="percent", max_value=100,
        desc="Top CPU consumers.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 50}, {"color": "red", "value": 80}],
    ))
    panels.append(bargauge(
        "Top Apps by Memory",
        [tgt(f'topk(10, truenas_app_memory_bytes{{instance=~"{I}", app=~"$app"}})', '{{app}}', 'A')],
        12, y, unit="bytes", desc="Top memory consumers.",
    ))
    y += 8
    panels.append(timeseries(
        "App CPU Over Time",
        [tgt(f'topk(8, truenas_app_cpu_percent{{instance=~"{I}", app=~"$app"}})', '{{app}}', 'A')],
        0, y, unit="percent", desc="App CPU usage trends.",
    ))
    panels.append(timeseries(
        "App Memory Over Time",
        [tgt(f'topk(8, truenas_app_memory_bytes{{instance=~"{I}", app=~"$app"}})', '{{app}}', 'A')],
        12, y, unit="bytes", desc="App memory usage trends.",
    ))
    y += 8
    panels.append(timeseries(
        "App Block I/O Rate",
        [
            tgt(f'topk(8, rate(truenas_app_blkio_read_bytes{{instance=~"{I}", app=~"$app"}}[$__rate_interval]))', 'read {{app}}', 'A'),
            tgt(f'-1 * topk(8, rate(truenas_app_blkio_write_bytes{{instance=~"{I}", app=~"$app"}}[$__rate_interval]))', 'write {{app}}', 'B'),
        ],
        0, y, unit="Bps", desc="Read (up) / write (down) throughput per app, from the cumulative block-I/O byte counters.",
    ))
    panels.append(timeseries(
        "App Network",
        [
            tgt(f'topk(8, truenas_app_net_rx_bytes_per_second{{instance=~"{I}", app=~"$app"}})', 'rx {{app}}', 'A'),
            tgt(f'-1 * topk(8, truenas_app_net_tx_bytes_per_second{{instance=~"{I}", app=~"$app"}})', 'tx {{app}}', 'B'),
        ],
        12, y, unit="Bps", desc="App network receive (up) and transmit (down).",
    ))
    y += 8
    panels.append(bargauge(
        "Apps by Container Count",
        [tgt(f'topk(12, truenas_app_container_count{{instance=~"{I}", app=~"$app"}})', '{{app}}', 'A')],
        0, y, w=8, unit="short", desc="Apps with the largest active workload footprint.",
    ))
    panels.append(piechart(
        "App State Distribution",
        [tgt(f'sum by (state) (truenas_app_state{{instance=~"{I}", app=~"$app"}})', '{{state}}', 'A')],
        8, y, w=8, desc="Current state mix across installed apps.",
    ))
    panels.append(piechart(
        "App Container State Distribution",
        [tgt(f'sum by (state) (truenas_app_container_state_count{{instance=~"{I}", app=~"$app"}})', '{{state}}', 'A')],
        16, y, w=8, desc="Current runtime state mix across app containers.",
    ))
    y += 8
    app_table_targets = [
        table_target(f'max by (app) (truenas_app_cpu_percent{{instance=~"{I}", app=~"$app"}})', 'A'),
        table_target(f'max by (app) (truenas_app_memory_bytes{{instance=~"{I}", app=~"$app"}})', 'B'),
        table_target(f'max by (app) (truenas_app_container_count{{instance=~"{I}", app=~"$app"}})', 'C'),
        table_target(f'max by (app) (truenas_app_upgrade_available{{instance=~"{I}", app=~"$app"}})', 'D'),
        table_target(f'max by (app) (truenas_app_image_updates_available{{instance=~"{I}", app=~"$app"}})', 'E'),
        table_target(f'max by (app) (truenas_app_used_port_count{{instance=~"{I}", app=~"$app"}})', 'F'),
        table_target(f'max by (app) (truenas_app_used_host_ip_count{{instance=~"{I}", app=~"$app"}})', 'G'),
    ]
    app_table_transforms = [
        outer_join('app'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {'app': 'App', 'Value #A': 'CPU %', 'Value #B': 'Memory', 'Value #C': 'Containers', 'Value #D': 'Upgrade', 'Value #E': 'Img Updates', 'Value #F': 'Ports', 'Value #G': 'Host IPs'},
            'indexByName': {'App': 0, 'CPU %': 1, 'Memory': 2, 'Containers': 3, 'Ports': 4, 'Host IPs': 5, 'Upgrade': 6, 'Img Updates': 7},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Memory', 'desc': True}]}),
    ]
    app_overrides = [
        {"matcher": {"id": "byName", "options": "CPU %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 50}, {"color": "red", "value": 80}]}}]},
        {"matcher": {"id": "byName", "options": "Memory"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Upgrade"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Available", "yellow", "—", GRAY)}]},
        {"matcher": {"id": "byName", "options": "Img Updates"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Available", "yellow", "—", GRAY)}]},
    ]
    panels.append(table(
        "App Inventory", app_table_targets, 0, y,
        desc="App resource footprint, update posture, and exposure summary.", overrides=app_overrides, transforms=app_table_transforms, sort_col='Memory',
    ))
    y += 10
    panels.append(stat(
        "DH Window", f'max(truenas_app_dockerhub_pull_limit_window_seconds{{instance=~"{I}"}})', 0, y, w=6, unit="s",
        desc="DockerHub rate-limit window duration.",
    ))
    y += 4

    # ── ROW: Virtualization ─────────────────────────────────────────────
    panels.append(row("Virtualization (VMs & Incus)", y))
    y += 1
    panels.extend([
        stat("VMs", f'sum(truenas_vm_count{{instance=~"{I}"}})', 0, y, w=3, desc="Virtual machines configured.", mappings=[{"type": "value", "options": {"0": {"text": "None", "color": "#808080", "index": 0}}}]),
        stat("Virt Support", f'max(truenas_vm_supports_virtualization{{instance=~"{I}"}})', 3, y, w=3, desc="KVM/HW virt available.", mappings=NEUTRAL_MAP),
        stat("Virt Details", f'max(truenas_vm_virtualization_details_supported{{instance=~"{I}"}})', 6, y, w=3,
             desc="Virtualization support from vm.virtualization_details.", mappings=NEUTRAL_MAP),
        stat("Virt Error", f'max(truenas_vm_virtualization_details_error_present{{instance=~"{I}"}})', 9, y, w=3,
             desc="vm.virtualization_details currently reports an error.", mappings=bmap("Error", "yellow", "OK", "green")),
        stat("Max vCPUs", f'max(truenas_vm_maximum_supported_vcpus{{instance=~"{I}"}})', 12, y, w=3, desc="Maximum supported vCPUs."),
        stat("VM Avail RAM", f'sum(truenas_vm_available_memory_bytes{{instance=~"{I}"}})', 15, y, w=3, unit="bytes", desc="Available memory for VMs."),
        stat("Incus Inst", f'sum(truenas_virt_instance_count{{instance=~"{I}"}})', 18, y, w=3, desc="Incus/LXD instances.", mappings=[{"type": "value", "options": {"0": {"text": "None", "color": "#808080", "index": 0}}}]),
        stat("IOMMU", f'max(truenas_iommu_enabled{{instance=~"{I}"}})', 21, y, w=3, desc="IOMMU/PCI passthrough.", mappings=NEUTRAL_MAP),
    ])
    y += 4
    panels.extend([
        stat("Intel VMX", f'max(truenas_vm_flag_intel_vmx{{instance=~"{I}"}})', 0, y, w=4, desc="Intel VT-x capability flag.", mappings=NEUTRAL_MAP),
        stat("AMD RVI", f'max(truenas_vm_flag_amd_rvi{{instance=~"{I}"}})', 4, y, w=4, desc="AMD RVI/NPT capability flag.", mappings=NEUTRAL_MAP),
        stat("Unrestricted", f'max(truenas_vm_flag_unrestricted_guest{{instance=~"{I}"}})', 8, y, w=4, desc="Unrestricted guest capability flag.", mappings=NEUTRAL_MAP),
        stat("AMD ASIDs", f'max(truenas_vm_flag_amd_asids_supported{{instance=~"{I}"}})', 12, y, w=4,
             desc="AMD Address Space Identifiers are supported.", mappings=NEUTRAL_MAP),
        stat("Incus Vols", f'sum(truenas_virt_volume_count{{instance=~"{I}"}})', 16, y, w=4, desc="Incus storage volumes."),
        stat("VM Mem Used", f'sum(truenas_vm_vmemory_in_use_bytes{{instance=~"{I}"}})', 20, y, w=4, unit="bytes", desc="VM memory in use."),
    ])
    y += 4
    panels.append(timeseries(
        "VM Memory Allocation",
        [
            tgt(f'sum(truenas_vm_available_memory_bytes{{instance=~"{I}"}})', 'Available', 'A'),
            tgt(f'sum(truenas_vm_vmemory_in_use_bytes{{instance=~"{I}"}})', 'In Use', 'B'),
        ],
        0, y, unit="bytes", desc="VM memory available vs in use.",
    ))
    panels.append(timeseries(
        "Incus Instance CPU",
        [tgt(f'truenas_virt_instance_cpu_usage_percent{{instance=~"{I}"}}', '{{name}}', 'A')],
        12, y, unit="percent", desc="Per-instance CPU usage.",
    ))
    y += 8
    panels.append(timeseries(
        "Incus Instance Memory",
        [tgt(f'truenas_virt_instance_mem_bytes{{instance=~"{I}"}}', '{{name}}', 'A')],
        0, y, w=24, unit="bytes", desc="Per-instance memory usage.",
    ))
    y += 8
    panels.append(table(
        "Incus Instance Running State",
        [table_target(f'max by (name, type) (truenas_virt_instance_running{{instance=~"{I}"}})', 'A')],
        0, y, w=24, h=8, desc="Current running state per Incus instance (container or VM).",
        transforms=[tf('organize', {
            'excludeByName': {'Time': True},
            'renameByName': {'name': 'Instance', 'type': 'Type', 'Value': 'State'},
            'indexByName': {'Instance': 0, 'Type': 1, 'State': 2}})],
        overrides=[{"matcher": {"id": "byName", "options": "State"}, "properties": [
            {"id": "custom.cellOptions", "value": {"type": "color-text"}}, {"id": "mappings", "value": RUN_MAP}]}],
        sort_col='Instance', sort_desc=False,
    ))
    y += 8

    # ── ROW: Alerts, Tasks & Updates ────────────────────────────────────
    panels.append(row("Alerts, Tasks & Updates", y))
    y += 1
    panels.extend([
        stat("Outstanding", OUTSTANDING_ALERTS, 0, y, w=3,
             desc="Alerts not dismissed: truenas_alert_count minus truenas_alert_dismissed_count (alert_count includes dismissed alerts).", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Critical", f'sum(truenas_alert_count_by_level{{instance=~"{I}", level=~"CRITICAL|ALERT|EMERGENCY"}})' + ZERO_IF_UP, 3, y, w=3,
             desc="Critical-or-worse alerts (may include dismissed ones). 0 when none; N/A when the exporter is down.", thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}], graph=True),
        stat("Warning", f'sum(truenas_alert_count_by_level{{instance=~"{I}", level=~"WARNING|ERROR"}})' + ZERO_IF_UP, 6, y, w=3,
             desc="Warning/error alerts (may include dismissed ones).", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Tasks", f'sum(truenas_task_count{{instance=~"{I}"}})', 9, y, w=3, color_mode="value", desc="Scheduled tasks."),
        stat("Tasks On", f'sum(truenas_task_enabled{{instance=~"{I}"}})' + ZERO_IF_UP, 12, y, w=3, color_mode="value", desc="Enabled tasks."),
        stat("Cloud Backups", f'sum(truenas_cloud_backup_task_count{{instance=~"{I}"}})', 15, y, w=3, color_mode="value", desc="Cloud backup tasks."),
        stat("Cron Jobs", f'truenas_cronjob_count{{instance=~"{I}"}}', 18, y, w=3, color_mode="value", desc="Configured cron jobs."),
        stat("Reboot", f'max(truenas_system_reboot_required{{instance=~"{I}"}})', 21, y, w=3, desc="Reboot required to finish pending changes.", mappings=bmap("Required", "yellow", "Not needed", "green")),
    ])
    y += 4
    panels.extend([
        stat("Dismissed", f'max(truenas_alert_dismissed_count{{instance=~"{I}"}})', 0, y, w=4, color_mode="value", desc="Alerts dismissed in the UI but still present."),
        stat("One-Shot", f'max(truenas_alert_one_shot_count{{instance=~"{I}"}})', 4, y, w=4, color_mode="value", desc="One-shot alerts requiring explicit handling."),
        stat("Active Jobs", f'max(truenas_job_active_count{{instance=~"{I}"}})', 8, y, w=4, color_mode="value", desc="Jobs currently waiting or running."),
        stat("Abortable", f'max(truenas_job_abortable_active_count{{instance=~"{I}"}})', 12, y, w=4, color_mode="value", desc="Active jobs that can be cancelled."),
        stat("Transient", f'max(truenas_job_transient_active_count{{instance=~"{I}"}})', 16, y, w=4, color_mode="value", desc="Active transient jobs."),
        stat("Last Alert Activity", f'time() - (max(truenas_alert_last_occurrence_timestamp_seconds{{instance=~"{I}"}}) > 0)', 20, y, w=4, unit="s", decimals=1, color_mode="value", desc="Age since the most recent alert occurrence."),
    ])
    y += 4
    panels.append(piechart(
        "Alert Level Distribution",
        [tgt(f'truenas_alert_count_by_level{{instance=~"{I}", level=~"$level"}}', '{{level}}', 'A')],
        0, y, w=8, desc="Current alert severity mix.",
    ))
    panels.append(bargauge(
        "Tasks by Type",
        [tgt(f'sort_desc(truenas_task_count{{instance=~"{I}", task_type=~"$task_type"}})', '{{task_type}}', 'A', instant=True)],
        8, y, w=8, desc="Configured scheduled tasks per type.", decimals=0,
        thresholds=[{"color": "blue", "value": None}],
    ))
    panels.append(timeseries(
        "Alert Count Over Time",
        [tgt(OUTSTANDING_ALERTS, 'Outstanding', 'A'),
         tgt(f'sum(truenas_alert_dismissed_count{{instance=~"{I}"}})', 'Dismissed', 'B'),
         tgt(f'sum(truenas_alert_count{{instance=~"{I}"}})', 'All (incl. dismissed)', 'C')],
        16, y, w=8, desc="Outstanding vs dismissed alerts over time.", min_value=0,
    ))
    y += 8
    panels.append(bargauge(
        "Alert Classes",
        [tgt(f'sort_desc(sum by (klass) (truenas_alert_count_by_class{{instance=~"{I}", level=~"$level"}}))', '{{klass}}', 'A', instant=True)],
        0, y, w=8, desc="Most common current alert classes (includes dismissed alerts).", decimals=0,
        thresholds=[{"color": "blue", "value": None}],
    ))
    panels.append(piechart(
        "Alert Sources",
        [tgt(f'truenas_alert_count_by_source{{instance=~"{I}"}}', '{{source}}', 'A')],
        8, y, w=8, desc="Which subsystems are generating alerts.",
    ))
    panels.append(bargauge(
        "Running Job Progress",
        [tgt(f'topk(10, truenas_job_progress_percent{{instance=~"{I}"}})', '{{method}}', 'A')],
        16, y, w=8, unit="percent", max_value=100, desc="Progress of currently running jobs by method.",
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 50}, {"color": "red", "value": 90}],
    ))
    y += 8
    panels.append(timeseries(
        "Active Jobs by State",
        [tgt(f'truenas_job_active_count_by_state{{instance=~"{I}"}}', '{{state}}', 'A')],
        0, y, w=12, unit="short", desc="Current active job counts split by WAITING and RUNNING state.",
    ))
    panels.append(timeseries(
        "Oldest Active Job Age",
        [tgt(f'time() - truenas_job_oldest_active_timestamp_seconds{{instance=~"{I}"}}', '{{state}}', 'A')],
        12, y, w=12, unit="s", desc="Age of the oldest active job in each state.",
    ))
    y += 8
    panels.append(table(
        "Job Method Detail",
        [
            table_target(f'sum by (method) (truenas_job_active_count_by_method{{instance=~"{I}"}})', 'A'),
            table_target(f'sum by (method) (truenas_job_active_count_by_method{{instance=~"{I}", state="RUNNING"}})', 'B'),
            table_target(f'sum by (method) (truenas_job_active_count_by_method{{instance=~"{I}", state="WAITING"}})', 'C'),
            table_target(f'max by (method) (truenas_job_progress_percent{{instance=~"{I}"}})', 'D'),
        ],
        0, y, w=12,
        desc="Active job counts and progress by middleware method.",
        transforms=[
            outer_join('method'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'method': 'Method', 'Value #A': 'Active', 'Value #B': 'Running', 'Value #C': 'Waiting', 'Value #D': 'Progress %'},
                'indexByName': {'Method': 0, 'Active': 1, 'Running': 2, 'Waiting': 3, 'Progress %': 4},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Active', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Progress %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 50}, {"color": "red", "value": 90}]}}]},
        ],
        sort_col='Active',
    ))
    panels.append(table(
        "Alert Source and Node Detail",
        [
            table_target(f'truenas_alert_count_by_source{{instance=~"{I}"}}', 'A'),
            table_target(f'truenas_alert_count_by_node{{instance=~"{I}"}}', 'B'),
        ],
        12, y, w=12,
        desc="Current alert counts grouped by source and by node.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'source': 'Source', 'node': 'Node', 'Value #A': 'Source Alerts', 'Value #B': 'Node Alerts'},
                'indexByName': {'Source': 0, 'Source Alerts': 1, 'Node': 2, 'Node Alerts': 3},
            }),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Source Alerts"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}]},
            {"matcher": {"id": "byName", "options": "Node Alerts"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}]},
        ],
    ))
    y += 10
    # Task enablement detail table
    panels.append(table(
        "Task Enablement Detail",
        [
            table_target(f'max by (name, task_type) (truenas_task_enabled{{instance=~"{I}", task_type=~"$task_type"}})', 'B'),
        ],
        0, y, desc="Task enablement. Tasks without a description (e.g. snapshot tasks) are labelled by their numeric TrueNAS ID.",
        transforms=[
            outer_join('name'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'Task (name or ID)', 'task_type': 'Type', 'Value #B': 'Enabled'},
                'indexByName': {'Type': 0, 'Task (name or ID)': 1, 'Enabled': 2},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Type', 'desc': False}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Enabled"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        ],
        sort_col='Type', sort_desc=False,
    ))
    y += 10
    panels.extend([
        stat("Alert Svcs", f'max(truenas_alertservice_count{{instance=~"{I}"}})', 0, y, w=4, desc="Configured alert notification services."),
        stat("Cron On", f'sum(truenas_cronjob_enabled{{instance=~"{I}"}})', 4, y, w=4, desc="Enabled cron jobs."),
        stat("Cloud Bkp On", f'sum(truenas_cloud_backup_task_enabled{{instance=~"{I}"}})' + ZERO_IF_UP, 8, y, w=4, color_mode="value", desc="Enabled cloud backup tasks (0 when none are configured)."),
        stat("Boot Changes", f'max(truenas_system_boot_changes_total{{instance=~"{I}"}})', 12, y, w=4, desc="Boot ID changes seen since exporter start (proxy for reboot count).", graph=True),
        stat("Update Avail", f'clamp_max(count(truenas_update_version_available{{instance=~"{I}"}} == 1), 1)' + ZERO_IF_UP, 16, y, w=4,
             desc="A newer version is available.", mappings=bmap("⬆ Available", "yellow", "Current", "green")),
        stat("Reboot Reason", f'clamp_max(count(truenas_system_reboot_reason{{instance=~"{I}"}}), 1)' + ZERO_IF_UP, 20, y, w=4,
             desc="A pending-reboot reason is currently reported.", mappings=bmap("Set", "yellow", "None", GRAY)),
    ])
    y += 4
    panels.append(table(
        "Alert Services",
        [table_target(f'truenas_alertservice_enabled{{instance=~"{I}"}}', 'A')],
        0, y, w=12, h=8,
        desc="Configured alert notification services. The exporter labels services by their numeric TrueNAS ID (no display name is exported), so the service type leads.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'ID', 'type': 'Service', 'Value': 'Enabled'},
                'indexByName': {'Service': 0, 'ID': 1, 'Enabled': 2},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Service', 'desc': False}]}),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Enabled"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]}],
        sort_col='Name', sort_desc=False,
    ))
    panels.append(table(
        "Update & Reboot Status",
        [
            table_target(
                f'label_replace(truenas_update_status{{instance=~"{I}"}}, "field", "Update Status", "__name__", ".*") '
                f'or label_replace(truenas_update_version_available{{instance=~"{I}"}} == 1, "field", "Version Available", "__name__", ".*") '
                f'or label_replace(truenas_system_reboot_reason{{instance=~"{I}"}}, "field", "Reboot Reason", "__name__", ".*")',
                'A',
            ),
        ],
        12, y, w=12, h=8,
        desc="Current update status/available version and any pending reboot reason.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {'field': 'Field', 'status': 'Status', 'version': 'Version', 'reason': 'Reason'},
                'indexByName': {'Field': 0, 'Status': 1, 'Version': 2, 'Reason': 3},
            }),
        ],
    ))
    y += 8

    # ── ROW: Security & Platform ────────────────────────────────────────
    panels.append(row("Security & Platform", y))
    y += 1
    panels.extend([
        stat("2FA", f'max(truenas_2fa_enabled{{instance=~"{I}"}})', 0, y, w=4, desc="Two-factor auth (disabled is a hardening finding, not an outage).", mappings=bmap("Enabled", "green", "Disabled", "yellow")),
        stat("SSH", f'max(truenas_ssh_enabled{{instance=~"{I}"}})', 4, y, w=4, desc="SSH service enabled at boot.", mappings=NEUTRAL_MAP),
        stat("FTP", f'max(truenas_ftp_enabled{{instance=~"{I}"}})', 8, y, w=4, desc="FTP service enabled at boot.", mappings=NEUTRAL_MAP),
        stat("SNMP", f'max(truenas_snmp_enabled{{instance=~"{I}"}})', 12, y, w=4, desc="SNMP service enabled at boot.", mappings=NEUTRAL_MAP),
        stat("FIPS", f'max(truenas_fips_enabled{{instance=~"{I}"}})', 16, y, w=4, desc="FIPS mode (policy-dependent).", mappings=NEUTRAL_MAP),
        stat("Sessions", f'max(truenas_auth_sessions_active{{instance=~"{I}"}})', 20, y, w=4, color_mode="value", desc="Active API sessions."),
    ])
    y += 4
    panels.extend([
        stat("Production", f'max(truenas_is_production{{instance=~"{I}"}})', 0, y, w=4, desc="Marked as production.", mappings=NEUTRAL_MAP),
        stat("iX Hardware", f'max(truenas_is_ix_hardware{{instance=~"{I}"}})', 4, y, w=4, desc="iXsystems hardware.", mappings=NEUTRAL_MAP),
        stat("Support A+E", f'max(truenas_support_available_and_enabled{{instance=~"{I}"}})', 8, y, w=4,
             desc="Support available and enabled.", mappings=NEUTRAL_MAP),
        stat("Directory Svc", DIRSVC_STATE, 12, y, w=4, desc=DIRSVC_DESC, mappings=DIRSVC_MAP),
        stat("Dir Svc Configured", f'max(truenas_directoryservices_config_enabled{{instance=~"{I}"}})', 16, y, w=4, desc="A directory service (AD/LDAP/IPA) is configured.", mappings=bmap("Yes", "blue", "No", GRAY)),
        stat("Dir Faults", f'sum(truenas_directoryservices_fault_present{{instance=~"{I}"}})', 20, y, w=4,
             desc="Enabled directory services reporting a fault (0 when disabled).", mappings=[{"type": "value", "options": {"0": {"text": "None", "color": "green", "index": 0}}}], thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
    ])
    y += 4
    panels.extend([
        stat("Security FIPS", f'max(truenas_system_security_fips_configured{{instance=~"{I}"}})', 0, y, w=4, desc="System security FIPS configured (policy-dependent).", mappings=NEUTRAL_MAP),
        stat("GPOS STIG", f'max(truenas_system_security_gpos_stig{{instance=~"{I}"}})', 4, y, w=4, desc="GPOS STIG policy enabled (policy-dependent).", mappings=NEUTRAL_MAP),
        stat(
            "Pwd Min Len",
            f'max(truenas_system_security_password_min_length{{instance=~"{I}"}})',
            8,
            y,
            w=4,
            thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 10}, {"color": "green", "value": 14}],
            desc="Minimum password length policy. N/A = no policy set (TrueNAS default).", no_value="Not set",
        ),
        stat(
            "Pwd Max Age",
            f'max(truenas_system_security_password_max_age_days{{instance=~"{I}"}})',
            12,
            y,
            w=4,
            unit="d",
            thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 90}, {"color": "red", "value": 180}],
            desc="Maximum password age in days. N/A = no policy set.", no_value="Not set",
        ),
        stat(
            "Pwd History",
            f'max(truenas_system_security_password_history_count{{instance=~"{I}"}})',
            16,
            y,
            w=4,
            thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 3}, {"color": "green", "value": 5}],
            desc="Password history retention count. N/A = no policy set.", no_value="Not set",
        ),
        stat("FIPS Avail", f'max(truenas_fips_available{{instance=~"{I}"}})', 20, y, w=4,
             desc="FIPS capability is available on this system.", mappings=NEUTRAL_MAP),
    ])
    y += 4
    panels.append(table(
        "Security and Identity Counts",
        [
            table_target(
                f'label_replace(max(truenas_local_user_count{{instance=~"{I}"}}), "category", "Local Users", "__name__", ".*") '
                f'or label_replace(max(truenas_local_group_count{{instance=~"{I}"}}), "category", "Local Groups", "__name__", ".*") '
                f'or label_replace(max(truenas_certificate_count{{instance=~"{I}"}}), "category", "Certificates", "__name__", ".*") '
                f'or label_replace(max(truenas_privilege_count{{instance=~"{I}"}}), "category", "Privileges", "__name__", ".*") '
                f'or label_replace(max(truenas_keychain_credential_count{{instance=~"{I}"}}), "category", "Keychain Creds", "__name__", ".*")',
                'A'
            ),
        ],
        0, y, w=12,
        desc="Identity and trust object counts.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'category': 'Category', 'Value': 'Count'},
                'indexByName': {'Category': 0, 'Count': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Count', 'desc': True}]}),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Count"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-text"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "blue", "value": None}]}}]}],
        sort_col='Count',
    ))
    panels.append(table(
        "Certificate Expiry",
        [
            table_target(f'floor((truenas_certificate_expiry_timestamp_seconds{{instance=~"{I}"}} - time()) / 86400)', 'A'),
            table_target(f'1000 * truenas_certificate_expiry_timestamp_seconds{{instance=~"{I}"}}', 'B'),
        ],
        12, y, w=12, h=10,
        desc="Certificate expiry in operator-friendly relative and absolute forms.",
        transforms=[
            outer_join('name'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'Certificate', 'Value #A': 'Days to Expiry', 'Value #B': 'Expires At'},
                'indexByName': {'Certificate': 0, 'Days to Expiry': 1, 'Expires At': 2},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Days to Expiry', 'desc': False}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Days to Expiry"}, "properties": [{"id": "unit", "value": "short"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "red", "value": None}, {"color": "yellow", "value": 14}, {"color": "green", "value": 30}]}}]},
            {"matcher": {"id": "byName", "options": "Expires At"}, "properties": [{"id": "unit", "value": "dateTimeAsIso"}]},
        ],
        sort_col='Days to Expiry', sort_desc=False,
    ))
    y += 10
    panels.extend([
        stat("API Keys", f'max(truenas_api_key_count{{instance=~"{I}"}})', 0, y, w=4, color_mode="value", desc="Configured API keys."),
        stat("API Keys Revoked", f'max(truenas_api_key_revoked_count{{instance=~"{I}"}})', 4, y, w=4,
             desc="Revoked API keys.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}]),
        stat("KMIP Sync Pending", f'max(truenas_kmip_sync_pending{{instance=~"{I}"}})', 8, y, w=4,
             desc="KMIP key synchronization pending.", mappings=bmap("Pending", "yellow", "No", "green")),
        stat("Managed by TC", f'max(truenas_managed_by_truecommand{{instance=~"{I}"}})', 12, y, w=4, desc="Managed by TrueCommand.", mappings=NEUTRAL_MAP),
        stat("Support Avail", f'max(truenas_support_available{{instance=~"{I}"}})', 16, y, w=4, desc="Proactive support available.", mappings=NEUTRAL_MAP),
        stat("Pwd Min Age", f'max(truenas_system_security_password_min_age_days{{instance=~"{I}"}})', 20, y, w=4, unit="d", color_mode="value", no_value="Not set", desc="Configured minimum password age. N/A = no policy set."),
    ])
    y += 4
    panels.append(table(
        "API Key Expiry",
        [table_target(f'floor((truenas_api_key_expiry_timestamp_seconds{{instance=~"{I}"}} - time()) / 86400)', 'A')],
        0, y, w=24, h=8,
        desc="Days until each API key expires (negative = already expired).",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'Name', 'Value': 'Days to Expiry'},
                'indexByName': {'Name': 0, 'Days to Expiry': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Days to Expiry', 'desc': False}]}),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Days to Expiry"}, "properties": [{"id": "unit", "value": "short"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "red", "value": None}, {"color": "yellow", "value": 14}, {"color": "green", "value": 30}]}}]}],
        sort_col='Days to Expiry', sort_desc=False,
    ))
    y += 8

    # ── COLLAPSED ROW: Boot Environment ─────────────────────────────────
    boot_panels = []
    by = y + 1
    boot_panels.extend([
        stat("Boot Healthy", f'truenas_boot_pool_healthy{{instance=~"{I}"}}', 0, by, w=3, desc="Boot pool health.", mappings=UP_MAP),
        stat("Boot Size", f'truenas_boot_pool_size_bytes{{instance=~"{I}"}}', 3, by, w=3, unit="bytes"),
        stat("Boot Free", f'truenas_boot_pool_free_bytes{{instance=~"{I}"}}', 6, by, w=3, unit="bytes"),
        stat("Boot Disks", f'truenas_boot_pool_disk_count{{instance=~"{I}"}}', 9, by, w=3),
        stat("Boot Envs", f'truenas_boot_env_count{{instance=~"{I}"}}', 12, by, w=3),
        stat("Active BEs", f'truenas_boot_env_active_count{{instance=~"{I}"}}', 15, by, w=3),
        stat("Activated BEs", f'truenas_boot_env_activated_count{{instance=~"{I}"}}', 18, by, w=3,
             desc="Boot environments selected for the next boot."),
        stat("Keep BEs", f'truenas_boot_env_keep_count{{instance=~"{I}"}}', 21, by, w=3),
    ])
    by += 4
    boot_panels.append(gauge(
        "Boot Pool Usage",
        f'truenas_boot_pool_allocated_bytes{{instance=~"{I}"}} / clamp_min(truenas_boot_pool_size_bytes{{instance=~"{I}"}}, 1)',
        0, by, w=6, desc="Boot pool fill ratio.",
    ))
    boot_panels.append(bargauge(
        "Boot Environment Used Space",
        [tgt(f'truenas_boot_environment_used_bytes{{instance=~"{I}"}}', '{{name}}', 'A')],
        6, by, w=18, unit="bytes", desc="Bytes used by each boot environment.",
        thresholds=[{"color": "blue", "value": None}],
    ))
    by += 8
    boot_panels.append(stat("Boot Scan %", f'clamp_max(max(truenas_boot_pool_scan_percent{{instance=~"{I}"}}), 100)', 0, by, w=6, unit="percent", color_mode="value", desc="Boot pool scan progress (clamped to 100 %)."))
    boot_panels.append(stat("Boot Pool Scan State", f'max by (state) (truenas_boot_pool_scan_state{{instance=~"{I}"}})', 6, by, w=9,
                            legend="{{state}}", text_mode="name", color_mode="value", desc="Last/active boot pool scrub state."))
    boot_panels.append(stat("Boot Pool Status", f'max by (status) (truenas_boot_pool_status{{instance=~"{I}"}})', 15, by, w=9,
                            legend="{{status}}", text_mode="name", color_mode="value", desc="Boot pool status (ONLINE is healthy)."))
    by += 4
    panels.append(row("Boot Environment", y, collapsed=True, panels=boot_panels))
    y += 1

    # ── COLLAPSED ROW: Hardware & IPMI ──────────────────────────────────
    hw_panels = []
    hy = y + 1
    hw_panels.extend([
        stat("IPMI Loaded", f'max(truenas_ipmi_loaded{{instance=~"{I}"}})', 0, hy, w=3, mappings=bmap("Yes", "green", "Not present", GRAY)),
        stat("Power On", f'max(truenas_ipmi_chassis_power_on{{instance=~"{I}"}})', 3, hy, w=3, mappings=UP_MAP),
        stat("GPUs", f'truenas_gpu_count{{instance=~"{I}"}}', 6, hy, w=3),
        stat("Power Overld", f'max(truenas_ipmi_chassis_power_overload{{instance=~"{I}"}})', 9, hy, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("Intrusion", f'max(truenas_ipmi_chassis_intrusion{{instance=~"{I}"}})', 12, hy, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("Drive Fault", f'max(truenas_ipmi_chassis_drive_fault{{instance=~"{I}"}})', 15, hy, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("Fan Fault", f'max(truenas_ipmi_chassis_fan_fault{{instance=~"{I}"}})', 18, hy, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("JBOF", f'truenas_jbof_count{{instance=~"{I}"}}', 21, hy, w=3),
    ])
    hy += 4
    hw_panels.extend([
        stat("SEL Entries", f'truenas_ipmi_sel_entry_count{{instance=~"{I}"}}', 0, hy, w=4),
        stat("SEL Free", f'truenas_ipmi_sel_free_space_bytes{{instance=~"{I}"}}', 4, hy, w=4, unit="bytes"),
        stat("GPU Host Avail", f'sum(truenas_gpu_available_to_host{{instance=~"{I}"}})', 8, hy, w=4,
             desc="GPUs available to the TrueNAS host."),
        stat("GPU Critical", f'sum(truenas_gpu_uses_system_critical_devices{{instance=~"{I}"}})', 12, hy, w=4,
             desc="GPUs using system-critical PCI devices.", thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("ECC Memory", f'max(truenas_host_ecc_memory{{instance=~"{I}"}})', 16, hy, w=4, mappings=bmap("Yes", "green", "Not reported", GRAY)),
        stat("Resilver On", f'max(truenas_pool_resilver_enabled{{instance=~"{I}"}})', 20, hy, w=4, mappings=NEUTRAL_MAP),
    ])
    hy += 4
    hw_panels.append(stat("Physical Cores", f'max(truenas_host_physical_cpu_cores{{instance=~"{I}"}})', 0, hy, w=6, desc="Host physical CPU cores (non-HT)."))
    hw_panels.append(table(
        "Host & Chassis Identity",
        [
            table_target(
                f'label_replace(max by (hostname, version, product_type) (truenas_host_info{{instance=~"{I}"}}), "component", "Host", "__name__", ".*") '
                f'or label_replace(max by (manufacturer, product) (truenas_host_system_info{{instance=~"{I}"}}), "component", "System", "__name__", ".*") '
                f'or label_replace(max by (model) (truenas_host_cpu_info{{instance=~"{I}"}}), "component", "CPU", "__name__", ".*") '
                f'or label_replace(max by (model) (truenas_chassis_hardware{{instance=~"{I}"}}), "component", "Chassis", "__name__", ".*") '
                f'or label_replace(max by (variant) (truenas_hw_virt_variant{{instance=~"{I}"}}), "component", "Hypervisor", "__name__", ".*") '
                f'or label_replace(max by (index, model, vendor, pci_id) (truenas_gpu_info{{instance=~"{I}"}}), "component", "GPU", "__name__", ".*")',
                'A',
            ),
        ],
        6, hy, w=18, h=8,
        desc="Static host, system, CPU, chassis, hypervisor, and GPU identity labels.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {
                    'component': 'Component', 'hostname': 'Hostname', 'version': 'Version', 'product_type': 'Product Type',
                    'manufacturer': 'Manufacturer', 'product': 'Product', 'model': 'Model', 'variant': 'Variant',
                    'index': 'GPU Index', 'vendor': 'Vendor', 'pci_id': 'PCI ID',
                },
                'indexByName': {'Component': 0, 'Hostname': 1, 'Version': 2, 'Product Type': 3, 'Manufacturer': 4, 'Product': 5, 'Model': 6, 'Variant': 7, 'GPU Index': 8, 'Vendor': 9, 'PCI ID': 10},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Component', 'desc': False}]}),
        ],
        sort_col='Component', sort_desc=False,
    ))
    hy += 8
    panels.append(row("Hardware & IPMI", y, collapsed=True, panels=hw_panels))
    y += 1

    # ── COLLAPSED ROW: Advanced Protocols ───────────────────────────────
    proto_panels = []
    py = y + 1
    proto_panels.extend([
        stat("NVMe-oF Sess", f'sum(truenas_nvmet_session_count{{instance=~"{I}"}})', 0, py, w=3),
        stat("NVMe-oF Subs", f'sum(truenas_nvmet_subsys_count{{instance=~"{I}"}})', 3, py, w=3),
        stat("NVMe-oF Ports", f'sum(truenas_nvmet_port_count{{instance=~"{I}"}})', 6, py, w=3),
        stat("NVMe-oF Hosts", f'sum(truenas_nvmet_host_count{{instance=~"{I}"}})', 9, py, w=3),
        stat("NVMe-oF NS", f'sum(truenas_nvmet_namespace_count{{instance=~"{I}"}})', 12, py, w=3),
        stat("FC Hosts", f'sum(truenas_fc_host_count{{instance=~"{I}"}})', 15, py, w=3),
        stat("FC Ports", f'sum(truenas_fc_port_count{{instance=~"{I}"}})', 18, py, w=3),
        stat("HA Disabled", f'truenas_failover_disabled_reason_count{{instance=~"{I}"}}', 21, py, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}]),
    ])
    py += 4
    proto_panels.append(table(
        "Failover Disabled Reasons",
        [table_target(f'truenas_failover_disabled_reason{{instance=~"{I}"}}', 'A')],
        0, py, w=12, h=6,
        desc="Reasons HA failover is currently disabled.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {'reason': 'Reason'},
                'indexByName': {'Reason': 0},
            }),
        ],
    ))
    proto_panels.append(table(
        "Failover Node Reboot Required",
        [table_target(f'truenas_failover_node_reboot_required{{instance=~"{I}"}}', 'A')],
        12, py, w=12, h=6,
        desc="Failover nodes with a documented reboot-required reason.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'node': 'Node', 'Value': 'Reboot Required'},
                'indexByName': {'Node': 0, 'Reboot Required': 1},
            }),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Reboot Required"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Required", "red", "No", "green")}]}],
    ))
    py += 6
    panels.append(row("Advanced Protocols (NVMe-oF / FC / HA)", y, collapsed=True, panels=proto_panels))
    y += 1

    # ── COLLAPSED ROW: Audit & Directory Services ───────────────────────
    audit_panels = []
    ay = y + 1
    audit_panels.extend([
        stat("Audit Used", f'truenas_audit_dataset_used_bytes{{instance=~"{I}"}}', 0, ay, w=4, unit="bytes"),
        stat("Audit Avail", f'truenas_audit_dataset_available_bytes{{instance=~"{I}"}}', 4, ay, w=4, unit="bytes"),
        stat("Audit Quota", f'truenas_audit_quota_bytes{{instance=~"{I}"}}', 8, ay, w=4, unit="bytes"),
        stat("Audit Reserve", f'truenas_audit_reservation_bytes{{instance=~"{I}"}}', 12, ay, w=4, unit="bytes"),
        stat("Warn Fill %", f'truenas_audit_quota_fill_warning_percent{{instance=~"{I}"}}', 16, ay, w=4, unit="percent"),
        stat("Crit Fill %", f'truenas_audit_quota_fill_critical_percent{{instance=~"{I}"}}', 20, ay, w=4, unit="percent"),
    ])
    ay += 4
    audit_panels.extend([
        stat("Retention", f'truenas_audit_retention_days{{instance=~"{I}"}}', 0, ay, w=6, unit="d",
             desc="Configured local audit retention."),
        stat("Remote Log", f'max(truenas_audit_remote_logging_enabled{{instance=~"{I}"}})', 6, ay, w=6,
             desc="Remote audit logging enabled (optional).", mappings=NEUTRAL_MAP),
        stat("Directory Svc", DIRSVC_STATE, 12, ay, w=6, desc=DIRSVC_DESC, mappings=DIRSVC_MAP),
        stat("Dir Faults", f'sum(truenas_directoryservices_fault_present{{instance=~"{I}"}})', 18, ay, w=6,
             mappings=[{"type": "value", "options": {"0": {"text": "None", "color": "green", "index": 0}}}], thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
    ])
    ay += 4
    audit_panels.append(table(
        "Directory Service Type",
        [table_target(f'truenas_directoryservices_service_type{{instance=~"{I}"}}', 'A')],
        0, ay, w=12, h=6,
        desc="Configured directory service type (always 1 when configured).",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {'service_type': 'Service Type'},
                'indexByName': {'Service Type': 0},
            }),
        ],
    ))
    audit_panels.append(table(
        "Directory Service Status",
        [table_target(f'max by (service, status) (truenas_directoryservices_status{{instance=~"{I}"}})', 'A'),
         table_target(f'max by (service) (truenas_directoryservices_healthy{{instance=~"{I}"}})', 'B')],
        12, ay, w=12, h=6,
        desc="Directory service status. service=\"none\" with status DISABLED means no directory service is configured (healthy flag 0 is expected then).",
        transforms=[
            outer_join('service'),
            tf('organize', {
                'excludeByName': {'Time': True, 'Value #A': True},
                'renameByName': {'service': 'Service', 'status': 'Status', 'Value #B': 'Healthy flag'},
                'indexByName': {'Service': 0, 'Status': 1, 'Healthy flag': 2},
            }),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Status"}, "properties": [
            {"id": "custom.cellOptions", "value": {"type": "color-text"}},
            {"id": "mappings", "value": [{"type": "value", "options": {
                "DISABLED": {"text": "Disabled", "color": "#808080", "index": 0},
                "HEALTHY": {"text": "Healthy", "color": "green", "index": 1},
                "FAULTED": {"text": "Faulted", "color": "red", "index": 2},
                "JOINING": {"text": "Joining", "color": "yellow", "index": 3},
                "LEAVING": {"text": "Leaving", "color": "yellow", "index": 4}}}]}]}],
    ))
    ay += 6
    panels.append(row("Audit & Directory Services", y, collapsed=True, panels=audit_panels))
    y += 1

    # ── COLLAPSED ROW: System Configuration ─────────────────────────────
    cfg_panels = []
    cy = y + 1
    cfg_panels.extend([
        stat("HTTPS Port", f'truenas_ui_https_port{{instance=~"{I}"}}', 0, cy, w=4),
        stat("Reporting On", f'max(truenas_reporting_enabled{{instance=~"{I}"}})', 4, cy, w=4, mappings=NEUTRAL_MAP),
        stat("Exporters", f'truenas_reporting_exporter_count{{instance=~"{I}"}}', 8, cy, w=4),
        stat("Static Routes", f'truenas_static_route_count{{instance=~"{I}"}}', 12, cy, w=4),
        stat("Tunables", f'truenas_tunable_count{{instance=~"{I}"}}', 16, cy, w=4),
        stat("Init Scripts", f'truenas_initshutdownscript_count{{instance=~"{I}"}}', 20, cy, w=4),
    ])
    cy += 4
    cfg_panels.extend([
        stat("Upd AutoChk", f'max(truenas_update_autocheck_enabled{{instance=~"{I}"}})', 0, cy, w=4, mappings=NEUTRAL_MAP,
             desc="Automatic update checks enabled."),
        stat("Upd Profile", f'clamp_max(count(truenas_update_profile_info{{instance=~"{I}"}}), 1)', 4, cy, w=4, mappings=NEUTRAL_MAP,
             desc="Update profile information present."),
        stat("NTP Servers", f'max(truenas_ntp_server_count{{instance=~"{I}"}})', 8, cy, w=4,
             desc="Configured NTP servers."),
        stat("Tier0 Days", f'max(truenas_reporting_tier0_retention_days{{instance=~"{I}"}})', 12, cy, w=4, unit="d",
             desc="Reporting tier0 retention period."),
        stat("Tier1 Days", f'max(truenas_reporting_tier1_retention_days{{instance=~"{I}"}})', 16, cy, w=4, unit="d",
             desc="Reporting tier1 retention period."),
        stat("Tier1 Int", f'max(truenas_reporting_tier1_update_interval_seconds{{instance=~"{I}"}})', 20, cy, w=4, unit="s",
             desc="Reporting tier1 update interval."),
    ])
    cy += 4
    cfg_panels.extend([
        stat("Catalog Cfg", f'max(truenas_catalog_config_present{{instance=~"{I}"}})', 0, cy, w=4, mappings=NEUTRAL_MAP,
             desc="Catalog config payload present."),
        stat("Pref Trains", f'max(truenas_catalog_preferred_train_count{{instance=~"{I}"}})', 4, cy, w=4,
             desc="Preferred catalog trains configured."),
        stat("NTP Burst", f'max(truenas_ntp_server_burst_count{{instance=~"{I}"}})', 8, cy, w=4,
             desc="NTP servers with burst enabled."),
        stat("NTP Iburst", f'max(truenas_ntp_server_iburst_count{{instance=~"{I}"}})', 12, cy, w=4,
             desc="NTP servers with iburst enabled."),
        stat("NTP Min Poll", f'max(truenas_ntp_server_min_poll_minutes{{instance=~"{I}"}})', 16, cy, w=4, unit="m",
             desc="Minimum configured NTP poll interval."),
        stat("NTP Max Poll", f'max(truenas_ntp_server_max_poll_minutes{{instance=~"{I}"}})', 20, cy, w=4, unit="m",
             desc="Maximum configured NTP poll interval."),
    ])
    cy += 4
    cfg_panels.extend([
        stat("FS Paths", f'truenas_filesystem_path_count{{instance=~"{I}"}}', 0, cy, w=6, desc="Filesystem paths being scraped."),
        stat("NTP Prefer", f'max(truenas_ntp_server_prefer_count{{instance=~"{I}"}})', 6, cy, w=6, desc="NTP servers marked prefer."),
    ])
    cfg_panels.append(table(
        "System Identity",
        [
            table_target(
                f'label_replace(truenas_system_global_id{{instance=~"{I}"}}, "field", "Global ID", "__name__", ".*") '
                f'or label_replace(truenas_system_host_id{{instance=~"{I}"}}, "field", "Host ID", "__name__", ".*") '
                f'or label_replace(truenas_system_product_type{{instance=~"{I}"}}, "field", "Product Type", "__name__", ".*") '
                f'or label_replace(truenas_system_state{{instance=~"{I}"}}, "field", "State", "__name__", ".*") '
                f'or label_replace(truenas_system_version{{instance=~"{I}"}}, "field", "Version", "__name__", ".*") '
                f'or label_replace(truenas_systemdataset_pool{{instance=~"{I}"}}, "field", "System Dataset Pool", "__name__", ".*")',
                'A',
            ),
        ],
        12, cy, w=12, h=8,
        desc="Static system identity labels: global/host ID, product type, current state, version, and system dataset pool.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'Value': True},
                'renameByName': {
                    'field': 'Field', 'global_id': 'Global ID', 'host_id': 'Host ID', 'product_type': 'Product Type',
                    'state': 'State', 'version': 'Version', 'pool': 'Pool',
                },
                'indexByName': {'Field': 0, 'Global ID': 1, 'Host ID': 2, 'Product Type': 3, 'State': 4, 'Version': 5, 'Pool': 6},
            }),
        ],
    ))
    cy += 8
    panels.append(row("System Configuration", y, collapsed=True, panels=cfg_panels))
    y += 1

    # ── COLLAPSED ROW: Dataset Deep-Dive ────────────────────────────────
    ds_panels = []
    dy = y + 1
    ds_panels.append(bargauge(
        "Top Datasets by Used Bytes",
        [tgt(f'topk(15, truenas_dataset_used_bytes{{instance=~"{I}", dataset=~"$dataset"}})', '{{dataset}}', 'A')],
        0, dy, unit="bytes", desc="Datasets by documented used-space value.",
    ))
    ds_panels.append(bargauge(
        "Datasets by Available Space (Bottom 15)",
        [tgt(f'bottomk(15, truenas_dataset_available_bytes{{instance=~"{I}", dataset=~"$dataset"}} > 0)', '{{dataset}}', 'A')],
        12, dy, unit="bytes", desc="Datasets with least available space.",
    ))
    dy += 8
    ds_panels.append(bargauge(
        "Dataset Snapshot Counts",
        [tgt(f'topk(15, truenas_dataset_snapshot_count{{instance=~"{I}", dataset=~"$dataset"}} > 0)', '{{dataset}}', 'A')],
        0, dy, unit="short", decimals=0,
        desc="Datasets with the most snapshots. Partial on TrueNAS 27: per-dataset counts cost one API call each, so the "
             "exporter fills at most DATASET_SNAPSHOT_FALLBACK_LIMIT datasets (default 25). See 'Snapshots' on the Pools tab for the total.",
        thresholds=[{"color": "blue", "value": None}],
    ))
    ds_panels.append(bargauge(
        "Dataset Compression Ratio",
        [tgt(f'sort_desc(truenas_dataset_compression_ratio{{instance=~"{I}", dataset=~"$dataset"}})', '{{dataset}}', 'A')],
        12, dy, unit="none", decimals=2, min_value=1, desc="Compression ratio per dataset (1.00 = no savings).",
        thresholds=[{"color": "blue", "value": None}],
    ))
    dy += 8
    ds_panels.append(bargauge(
        "Datasets Using Snapshot Space",
        [tgt(f'topk(15, truenas_dataset_used_by_snapshots_bytes{{instance=~"{I}", dataset=~"$dataset"}} > 0)', '{{dataset}}', 'A')],
        0, dy, unit="bytes", desc="Datasets consuming the most space in snapshots.",
    ))
    ds_panels.append(bargauge(
        "Datasets with Reservations",
        [tgt(f'topk(15, truenas_dataset_reservation_bytes{{instance=~"{I}", dataset=~"$dataset"}} > 0)', '{{dataset}}', 'A')],
        12, dy, h=8, unit="bytes", desc="Datasets with explicit ZFS reservations.",
        thresholds=[{"color": "blue", "value": None}],
    ))
    ds_panels[-1]["fieldConfig"]["defaults"]["noValue"] = "No datasets have a reservation"
    dy += 8
    ds_panels.append(table(
        "Dataset Capacity Detail",
        [
            table_target(f'max by (dataset) (truenas_dataset_used_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'A'),
            table_target(f'max by (dataset) (truenas_dataset_available_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'B'),
            table_target(f'max by (dataset) (truenas_dataset_compression_ratio{{instance=~"{I}", dataset=~"$dataset"}})', 'C'),
            table_target(f'max by (dataset) (truenas_dataset_encrypted{{instance=~"{I}", dataset=~"$dataset"}})', 'D'),
            table_target(f'max by (dataset) (truenas_dataset_quota_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'E'),
            table_target(f'max by (dataset) (truenas_dataset_snapshot_count{{instance=~"{I}", dataset=~"$dataset"}})', 'F'),
            table_target(f'100 * max by (dataset) (truenas_dataset_used_bytes{{instance=~"{I}", dataset=~"$dataset"}}) / clamp_min(max by (dataset) (truenas_dataset_used_bytes{{instance=~"{I}", dataset=~"$dataset"}}) + max by (dataset) (truenas_dataset_available_bytes{{instance=~"{I}", dataset=~"$dataset"}}), 1)', 'G'),
            table_target(f'max by (dataset) (truenas_dataset_refquota_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'H'),
            table_target(f'max by (dataset) (truenas_dataset_reservation_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'I'),
            table_target(f'max by (dataset) (truenas_dataset_used_by_snapshots_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'J'),
        ],
        0, dy,
        desc="Detailed dataset capacity, encryption, quota, and snapshot info.",
        transforms=[
            outer_join('dataset'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'dataset': 'Dataset', 'Value #A': 'Used', 'Value #B': 'Available', 'Value #C': 'Compression', 'Value #D': 'Encrypted', 'Value #E': 'Quota', 'Value #F': 'Snapshots', 'Value #G': 'Used %', 'Value #H': 'Refquota', 'Value #I': 'Reservation', 'Value #J': 'Snapshot Space'},
                'indexByName': {'Dataset': 0, 'Used %': 1, 'Used': 2, 'Available': 3, 'Quota': 4, 'Refquota': 5, 'Reservation': 6, 'Snapshot Space': 7, 'Snapshots': 8, 'Compression': 9, 'Encrypted': 10},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Used %', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Used %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
            {"matcher": {"id": "byName", "options": "Used"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Available"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Quota"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Refquota"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Reservation"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Snapshot Space"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Encrypted"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        ],
        sort_col='Used %',
    ))
    dy += 10
    ds_panels.append(table(
        "Dataset Policy Detail",
        [
            table_target(f'max by (dataset) (truenas_dataset_key_loaded{{instance=~"{I}", dataset=~"$dataset"}})', 'A'),
            table_target(f'max by (dataset) (truenas_dataset_locked{{instance=~"{I}", dataset=~"$dataset"}})', 'B'),
            table_target(f'max by (dataset) (truenas_dataset_readonly{{instance=~"{I}", dataset=~"$dataset"}})', 'C'),
            table_target(f'max by (dataset) (truenas_dataset_atime{{instance=~"{I}", dataset=~"$dataset"}})', 'D'),
            table_target(f'max by (dataset) (truenas_dataset_exec{{instance=~"{I}", dataset=~"$dataset"}})', 'E'),
            table_target(f'max by (dataset) (truenas_dataset_quota_warning_percent{{instance=~"{I}", dataset=~"$dataset"}})', 'F'),
            table_target(f'max by (dataset) (truenas_dataset_quota_critical_percent{{instance=~"{I}", dataset=~"$dataset"}})', 'G'),
            table_target(f'max by (dataset) (truenas_dataset_refquota_warning_percent{{instance=~"{I}", dataset=~"$dataset"}})', 'H'),
            table_target(f'max by (dataset) (truenas_dataset_refquota_critical_percent{{instance=~"{I}", dataset=~"$dataset"}})', 'I'),
            table_target(f'max by (dataset) (truenas_dataset_refreservation_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'J'),
            table_target(f'max by (dataset) (truenas_dataset_used_by_children_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'K'),
            table_target(f'max by (dataset) (truenas_dataset_used_by_dataset_bytes{{instance=~"{I}", dataset=~"$dataset"}})', 'L'),
            table_target(f'time() - max by (dataset) (truenas_dataset_creation_timestamp_seconds{{instance=~"{I}", dataset=~"$dataset"}})', 'M'),
        ],
        0, dy,
        desc="Dataset encryption, policy flags, quota thresholds, and age.",
        transforms=[
            outer_join('dataset'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'dataset': 'Dataset', 'Value #A': 'Key Loaded', 'Value #B': 'Locked', 'Value #C': 'Readonly', 'Value #D': 'Atime', 'Value #E': 'Exec', 'Value #F': 'Quota Warn %', 'Value #G': 'Quota Crit %', 'Value #H': 'Refquota Warn %', 'Value #I': 'Refquota Crit %', 'Value #J': 'Refreservation', 'Value #K': 'Used by Children', 'Value #L': 'Used by Dataset', 'Value #M': 'Age'},
                'indexByName': {'Dataset': 0, 'Age': 1, 'Quota Warn %': 2, 'Quota Crit %': 3, 'Refquota Warn %': 4, 'Refquota Crit %': 5, 'Key Loaded': 6, 'Locked': 7, 'Readonly': 8, 'Atime': 9, 'Exec': 10, 'Refreservation': 11, 'Used by Children': 12, 'Used by Dataset': 13},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Quota Crit %', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Quota Warn %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
            {"matcher": {"id": "byName", "options": "Quota Crit %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 85}, {"color": "red", "value": 95}]}}]},
            {"matcher": {"id": "byName", "options": "Refquota Warn %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
            {"matcher": {"id": "byName", "options": "Refquota Crit %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 85}, {"color": "red", "value": 95}]}}]},
            {"matcher": {"id": "byName", "options": "Age"}, "properties": [{"id": "unit", "value": "s"}]},
            {"matcher": {"id": "byName", "options": "Refreservation"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Used by Children"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Used by Dataset"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Key Loaded"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
            {"matcher": {"id": "byName", "options": "Locked"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
            {"matcher": {"id": "byName", "options": "Readonly"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
            {"matcher": {"id": "byName", "options": "Atime"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
            {"matcher": {"id": "byName", "options": "Exec"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        ],
        sort_col='Quota Crit %',
    ))
    dy += 10
    panels.append(row("Dataset Deep-Dive", y, collapsed=True, panels=ds_panels))
    y += 1

    # ── COLLAPSED ROW: Exporter + Advanced ZFS ──────────────────────────
    api_panels = []
    apy = y + 1
    api_panels.extend([
        stat("Exporter Up", f'min(truenas_up{{instance=~"{I}"}})', 0, apy, w=3, mappings=UP_MAP, desc="Exporter can reach the TrueNAS API."),
        stat("Scrape Time", f'max(truenas_scrape_duration_seconds{{instance=~"{I}"}})', 3, apy, w=3, unit="s",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 10}, {"color": "red", "value": 30}], graph=True),
        stat("Event Stream", f'max(truenas_event_stream_up{{instance=~"{I}"}})', 6, apy, w=3, mappings=UP_MAP),
        stat("Methods OK %", f'100 * avg(truenas_api_call_success{{instance=~"{I}", method=~"$method"}})', 9, apy, w=3, unit="percent",
             desc="Share of API methods whose latest scrape call succeeded (not a call-level success rate).",
             thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 95}, {"color": "green", "value": 99}], graph=True),
        stat("API Errors (1h)", f'sum(increase(truenas_api_call_errors_total{{instance=~"{I}"}}[1h]))' + ZERO_IF_UP, 12, apy, w=3, decimals=0,
             desc="API call errors in the last hour; returns to 0 after recovery.",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 10}], graph=True),
        stat("Coll Errors (1h)", f'sum(increase(truenas_collector_errors_total{{instance=~"{I}"}}[1h]))' + ZERO_IF_UP, 15, apy, w=3, decimals=0,
             desc="Collector errors in the last hour; returns to 0 after recovery.",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}]),
        stat("Scrape Age", f'time() - max(truenas_last_scrape_timestamp_seconds{{instance=~"{I}"}})', 18, apy, w=3, unit="s", decimals=0, desc="Seconds since the last scrape attempt; check Exporter Up for success.",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 120}, {"color": "red", "value": 600}]),
        stat("Features On", f'sum(truenas_feature_enabled{{instance=~"{I}"}})', 21, apy, w=3, desc="Enabled platform feature flags."),
    ])
    apy += 4
    api_panels.extend([
        stat("Oldest Alert Age", f'time() - clamp_min(max(truenas_alert_oldest_timestamp_seconds{{instance=~"{I}"}}), 1)', 0, apy, w=3, unit="s", desc="Age of the oldest active alert."),
        stat("Repl Parallel", f'max(truenas_replication_max_parallel{{instance=~"{I}"}})', 3, apy, w=3, desc="Configured maximum replication parallelism."),
        stat("Boot Env Active", f'sum(truenas_boot_env_active{{instance=~"{I}"}})', 6, apy, w=3, desc="Boot environments active now."),
        stat("Boot Env Next", f'sum(truenas_boot_env_activated{{instance=~"{I}"}})', 9, apy, w=3, desc="Boot environments selected for the next boot."),
        stat("Demand Access/s", f'max(truenas_zfs_demand_accesses_per_second{{instance=~"{I}"}})', 12, apy, w=3, unit="ops", color_mode="value", desc="Total ARC demand accesses per second."),
        stat("Data IO Hit %", rate_pct("demand_data_io_hits_per_second", "demand_data_accesses_per_second"), 15, apy, w=3, unit="percent", decimals=2, color_mode="value", desc="Demand-data I/O hits (prefetch in flight) ÷ demand-data accesses, from rates."),
        stat("Meta IO Hit %", rate_pct("demand_metadata_io_hits_per_second", "demand_metadata_accesses_per_second"), 18, apy, w=3, unit="percent", decimals=2, color_mode="value", desc="Demand-metadata I/O hits ÷ accesses, from rates."),
        stat("L2ARC Miss %", rate_pct("l2arc_misses_per_second", "l2arc_accesses_per_second"), 21, apy, w=3, unit="percent", decimals=1, color_mode="value", desc="L2ARC misses ÷ accesses, from rates. N/A without L2ARC traffic."),
    ])
    apy += 4
    api_panels.append(timeseries(
        "Exporter & Event Stream Health",
        [
            tgt(f'truenas_up{{instance=~"{I}"}}', 'Exporter up', 'A'),
            tgt(f'truenas_event_stream_up{{instance=~"{I}"}}', 'Event stream {{event}}', 'B'),
            tgt(f'sum(rate(truenas_collector_errors_total{{instance=~"{I}"}}[$__rate_interval]))', 'Collector error rate', 'C'),
        ],
        0, apy, desc="Telemetry collection health (collector errors shown as a rate, not a lifetime total).",
    ))
    api_panels.append(timeseries(
        "Scrape Duration Over Time",
        [tgt(f'truenas_scrape_duration_seconds{{instance=~"{I}"}}', 'Scrape time', 'A')],
        12, apy, unit="s", desc="Exporter scrape duration trend.",
    ))
    apy += 8
    api_panels.append(timeseries(
        "API Method Duration (Top 12)",
        [tgt(f'topk(12, truenas_api_call_duration_seconds{{instance=~"{I}", method=~"$method"}})', '{{method}}', 'A')],
        0, apy, unit="s", desc="Slowest API methods.",
    ))
    api_panels.append(table(
        "API Method Success",
        [table_target(f'sort(max by (method) (truenas_api_call_success{{instance=~"{I}", method=~"$method"}}))', 'A')],
        12, apy, w=12, h=8,
        desc="Latest success flag per API method, failures first. Replaces an unreadable per-method timeline (D4).",
        transforms=[tf('organize', {'excludeByName': {'Time': True},
                                    'renameByName': {'method': 'Method', 'Value': 'Last call'},
                                    'indexByName': {'Method': 0, 'Last call': 1}})],
        overrides=[{"matcher": {"id": "byName", "options": "Last call"}, "properties": [
            {"id": "custom.cellOptions", "value": {"type": "color-text"}},
            {"id": "mappings", "value": bmap("OK", "green", "Failed", "red")}]}],
    ))
    apy += 8
    api_panels.append(histogram(
        "API Duration Distribution",
        [tgt(f'truenas_api_call_duration_seconds{{instance=~"{I}", method=~"$method"}}', '{{method}}', 'A')],
        0, apy, w=12, unit="s", desc="API method duration spread.",
    ))
    api_panels.append(timeseries(
        "Event Messages Rate",
        [tgt(f'rate(truenas_event_messages_total{{instance=~"{I}"}}[5m])', 'Events/s', 'A')],
        12, apy, unit="ops", desc="Event stream message rate.",
    ))
    apy += 8
    api_panels.append(timeseries(
        "Advanced ZFS Ratios",
        [
            tgt(rate_pct("demand_data_io_hits_per_second", "demand_data_accesses_per_second"), 'Data I/O hit %', 'A'),
            tgt(rate_pct("demand_data_misses_per_second", "demand_data_accesses_per_second"), 'Data miss %', 'B'),
            tgt(rate_pct("demand_metadata_io_hits_per_second", "demand_metadata_accesses_per_second"), 'Metadata I/O hit %', 'C'),
            tgt(rate_pct("demand_meta_misses_per_second", "demand_metadata_accesses_per_second"), 'Metadata miss %', 'D'),
            tgt(rate_pct("l2arc_hits_per_second", "l2arc_accesses_per_second"), 'L2ARC hit %', 'E'),
            tgt(rate_pct("l2arc_misses_per_second", "l2arc_accesses_per_second"), 'L2ARC miss %', 'F'),
        ],
        0, apy, unit="percent", min_value=0, max_value=100,
        desc="ARC/L2ARC percentages computed from realtime rates (hits or misses ÷ accesses). The upstream *_ratio fields are not used: 27.0 RC.1 sends 0.",
    ))
    api_panels.append(timeseries(
        "Advanced ZFS Access & Miss Rates",
        [
            tgt(f'truenas_zfs_demand_accesses_per_second{{instance=~"{I}"}}', 'Demand accesses/s', 'A'),
            tgt(f'truenas_zfs_demand_data_misses_per_second{{instance=~"{I}"}}', 'Data misses/s', 'B'),
            tgt(f'truenas_zfs_demand_meta_misses_per_second{{instance=~"{I}"}}', 'Metadata misses/s', 'C'),
            tgt(f'truenas_zfs_l2arc_accesses_per_second{{instance=~"{I}"}}', 'L2ARC accesses/s', 'D'),
            tgt(f'truenas_zfs_l2arc_hits_per_second{{instance=~"{I}"}}', 'L2ARC hits/s', 'E'),
            tgt(f'truenas_zfs_l2arc_misses_per_second{{instance=~"{I}"}}', 'L2ARC misses/s', 'F'),
        ],
        12, apy, unit="ops", desc="Advanced demand and L2ARC activity rates.",
    ))
    apy += 8
    api_panels.append(table(
        "Exporter Version",
        [table_target(f'max by (version) (truenas_exporter_info{{instance=~"{I}"}})', 'A')],
        0, apy, w=12, h=8,
        desc="Exporter build version label currently active per instance.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'version': 'Version', 'Value': 'Present'},
                'indexByName': {'Version': 0, 'Present': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Version', 'desc': False}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Present"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-text"}}, {"id": "mappings", "value": bmap("Running", "green", "—", GRAY)}]},
        ],
        sort_col='Version', sort_desc=False,
    ))
    api_panels.append(table(
        "Boot Environment Flags",
        [
            table_target(f'max by (name) (truenas_boot_env_active{{instance=~"{I}"}})', 'A'),
            table_target(f'max by (name) (truenas_boot_env_activated{{instance=~"{I}"}})', 'B'),
            table_target(f'max by (name) (truenas_boot_env_keep{{instance=~"{I}"}})', 'C'),
        ],
        12, apy, w=12, h=8,
        desc="Current, next-boot, and retention flags for rollback planning.",
        transforms=[
            outer_join('name'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'Boot Environment', 'Value #A': 'Active Now', 'Value #B': 'Next Boot', 'Value #C': 'Keep'},
                'indexByName': {'Boot Environment': 0, 'Active Now': 1, 'Next Boot': 2, 'Keep': 3},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Active Now', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Active Now"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Active", "green", "—", GRAY)}]},
            {"matcher": {"id": "byName", "options": "Next Boot"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Next", "blue", "—", GRAY)}]},
            {"matcher": {"id": "byName", "options": "Keep"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": bmap("Kept", "blue", "—", GRAY)}]},
        ],
        sort_col='Active Now',
    ))
    apy += 8
    api_table_targets = [
        table_target(f'max by (method) (truenas_api_call_duration_seconds{{instance=~"{I}", method=~"$method"}})', 'A'),
        table_target(f'max by (method) (truenas_api_call_success{{instance=~"{I}", method=~"$method"}})', 'B'),
        table_target(f'sum by (method) (truenas_api_call_errors_total{{instance=~"{I}", method=~"$method"}})', 'C'),
    ]
    api_table_transforms = [
        outer_join('method'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True, 'error_type': True},
            'renameByName': {'method': 'Method', 'Value #A': 'Duration s', 'Value #B': 'Success', 'Value #C': 'Errors'},
            'indexByName': {'Method': 0, 'Duration s': 1, 'Success': 2, 'Errors': 3},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Duration s', 'desc': True}]}),
    ]
    api_overrides = [
        {"matcher": {"id": "byName", "options": "Duration s"}, "properties": [{"id": "unit", "value": "s"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 0.2}, {"color": "red", "value": 1.0}]}}]},
        {"matcher": {"id": "byName", "options": "Success"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-text"}}, {"id": "mappings", "value": bmap("OK", "green", "Failed", "red")}]},
    ]
    api_panels.append(table(
        "API Method Detail", api_table_targets, 0, apy,
        desc="Per-method duration, success flag, and errors.",
        overrides=api_overrides, transforms=api_table_transforms, sort_col='Duration s',
    ))
    apy += 10
    api_panels.append(table(
        "Generic Event Field Extraction",
        [
            table_target(
                f'label_replace(truenas_event_boolean_value{{instance=~"{I}"}}, "kind", "boolean", "__name__", ".*") '
                f'or label_replace(truenas_event_numeric_value{{instance=~"{I}"}}, "kind", "numeric", "__name__", ".*") '
                f'or label_replace(truenas_event_list_length{{instance=~"{I}"}}, "kind", "list_length", "__name__", ".*") '
                f'or label_replace(truenas_event_status_value{{instance=~"{I}"}}, "kind", "status", "__name__", ".*")',
                'A',
            ),
        ],
        0, apy, w=12, h=8,
        desc="Fallback per-event-field values extracted for undocumented event payload fields (path identifies the field).",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'event': 'Event', 'path': 'Path', 'kind': 'Kind', 'status': 'Status', 'Value': 'Value'},
                'indexByName': {'Event': 0, 'Path': 1, 'Kind': 2, 'Value': 3, 'Status': 4},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Event', 'desc': False}]}),
        ],
        sort_col='Event', sort_desc=False,
    ))
    api_panels.append(table(
        "Generic Method Field Extraction",
        [
            table_target(
                f'label_replace(truenas_method_boolean_value{{instance=~"{I}", method=~"$method"}}, "kind", "boolean", "__name__", ".*") '
                f'or label_replace(truenas_method_numeric_value{{instance=~"{I}", method=~"$method"}}, "kind", "numeric", "__name__", ".*") '
                f'or label_replace(truenas_method_list_length{{instance=~"{I}", method=~"$method"}}, "kind", "list_length", "__name__", ".*") '
                f'or label_replace(truenas_method_status_value{{instance=~"{I}", method=~"$method"}}, "kind", "status", "__name__", ".*")',
                'A',
            ),
        ],
        12, apy, w=12, h=8,
        desc="Fallback per-method-field values extracted for undocumented API method result fields (path identifies the field).",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'method': 'Method', 'path': 'Path', 'kind': 'Kind', 'status': 'Status', 'Value': 'Value'},
                'indexByName': {'Method': 0, 'Path': 1, 'Kind': 2, 'Value': 3, 'Status': 4},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Method', 'desc': False}]}),
        ],
        sort_col='Method', sort_desc=False,
    ))
    apy += 8
    api_panels.append(table(
        "Event Last Message Age",
        [table_target(f'time() - truenas_event_last_message_timestamp_seconds{{instance=~"{I}"}}', 'A')],
        0, apy, w=24, h=6,
        desc="Seconds since the last message was received for each subscribed event.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'event': 'Event', 'Value': 'Age'},
                'indexByName': {'Event': 0, 'Age': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Age', 'desc': True}]}),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Age"}, "properties": [{"id": "unit", "value": "s"}]}],
        sort_col='Age',
    ))
    apy += 6
    api_panels.extend([
        timeseries("Generic Series Budget Usage", [tgt(f'truenas_generic_series{{instance=~"{I}"}}', '{{source}}')], 0, apy, w=12, h=6, desc="Generic series retained; each source has its own MAX_GENERIC_SERIES budget."),
        timeseries("Generic Series Limit Hits", [tgt(f'rate(truenas_generic_series_limit_hits_total{{instance=~"{I}"}}[$__rate_interval])', '{{source}}')], 12, apy, w=12, h=6, desc="Extraction branches omitted at the configured budget. Descendant samples are not counted individually."),
    ])
    panels.append(row("Exporter + Advanced ZFS", y, collapsed=True, panels=api_panels))
    y += 1

    # ── Validate grid ───────────────────────────────────────────────────
    for panel in panels:
        gp = panel.get('gridPos', {})
        assert gp.get('x', 0) + gp.get('w', 0) <= 24, f"Panel overflow: {panel.get('title', '')}"

    dashboard = {
        "title": "TrueNAS - Operations Center",
        "uid": "truenas-operations-center-3",
        "description": (
            "Comprehensive TrueNAS dashboard: system health, CPU, memory, ZFS pools & ARC, "
            "disks, network, services, shares, apps, VMs, boot environments, hardware/IPMI, "
            "alerts, tasks, security, advanced protocols, and exporter diagnostics."
        ),
        "tags": ["truenas", "storage", "operations", "zfs", "exporter"],
        "schemaVersion": 42,
        "version": 10,
        "refresh": "30s",
        "timezone": "browser",
        "graphTooltip": 1,
        "time": {"from": "now-6h", "to": "now"},
        "timepicker": {},
        "weekStart": "",
        "fiscalYearStartMonth": 0,
        "preload": False,
        "editable": True,
        "annotations": {
            "list": [
                {
                    "builtIn": 1,
                    "datasource": {"type": "grafana", "uid": "-- Grafana --"},
                    "enable": True,
                    "hide": True,
                    "iconColor": "rgba(0, 211, 255, 1)",
                    "name": "Annotations & Alerts",
                    "type": "dashboard",
                },
                {
                    "datasource": copy.deepcopy(DS),
                    "enable": True,
                    "expr": 'ALERTS{alertstate="firing"}',
                    "hide": False,
                    "iconColor": "red",
                    "name": "Firing Alerts",
                    "step": "60s",
                    "tagKeys": "alertname,severity",
                    "titleFormat": "{{ alertname }}",
                    "textFormat": "{{ severity }}",
                    "type": "tags",
                },
            ]
        },
        "links": [],
        "panels": panels,
        "templating": {
            "list": [
                {"name": "DS_PROMETHEUS", "label": "Datasource", "type": "datasource", "query": "prometheus", "refresh": 1, "includeAll": False, "options": [], "regex": "", "current": {"text": "Prometheus", "value": "prometheus"}},
                qvar("instance", "Instance", 'label_values(truenas_up, instance)'),
                qvar("pool", "Pool", f'label_values(truenas_pool_size_bytes{{instance=~"{I}"}}, pool)'),
                qvar("dataset", "Dataset", f'label_values(truenas_dataset_used_bytes{{instance=~"{I}"}}, dataset)'),
                qvar("disk", "Disk", f'label_values(truenas_disk_size_bytes{{instance=~"{I}"}}, disk)'),
                qvar("interface", "Interface", f'label_values(truenas_interface_link_up{{instance=~"{I}"}}, interface)'),
                qvar("service", "Service", f'label_values(truenas_service_running{{instance=~"{I}"}}, service)'),
                qvar("app", "App", f'label_values(truenas_app_cpu_percent{{instance=~"{I}"}}, app)'),
                qvar("task_type", "Task Type", f'label_values(truenas_task_count{{instance=~"{I}"}}, task_type)'),
                qvar("level", "Alert Level", f'label_values(truenas_alert_count_by_level{{instance=~"{I}"}}, level)'),
                qvar("method", "API Method", f'label_values(truenas_api_call_duration_seconds{{instance=~"{I}"}}, method)'),
            ]
        },
    }
    collapsed_panels = []
    current_row = None
    for panel in dashboard["panels"]:
        if panel.get("type") == "row":
            panel["collapsed"] = True
            panel.setdefault("panels", [])
            collapsed_panels.append(panel)
            current_row = panel
        elif current_row is None:
            collapsed_panels.append(panel)
        else:
            current_row["panels"].append(panel)
    dashboard["panels"] = collapsed_panels
    for r in collapsed_panels:
        shorten_titles(r.get("panels", []))
    return finalize(dashboard)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate the canonical TrueNAS Grafana dashboard.")
    parser.add_argument("--check", action="store_true", help="Fail when the committed dashboard differs.")
    args = parser.parse_args()
    dashboard = build_dashboard()
    rendered = json.dumps(dashboard, indent=2) + "\n"
    if not args.check:
        OUT.parent.mkdir(parents=True, exist_ok=True)
    check_or_write(OUT, rendered, check=args.check, description="Dashboard")
