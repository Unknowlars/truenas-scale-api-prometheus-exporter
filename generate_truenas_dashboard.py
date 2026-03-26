import copy
import json
from pathlib import Path


DS = {"type": "prometheus", "uid": "${DS_PROMETHEUS}"}
PLUGIN_VERSION = "12.4.0"
OUT = Path("truenas-exporter-dashboard.json")


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
         mappings=None, graph=False, color_mode="background", graph_mode=None):
    return {
        "type": "stat",
        "id": IDS.next(),
        "title": title,
        "description": desc,
        "datasource": copy.deepcopy(DS),
        "targets": [tgt(expr)],
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": mappings or [],
                "thresholds": {"mode": "absolute", "steps": thresholds or [{"color": "blue", "value": 0}]},
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
            "textMode": "auto",
            "wideLayout": True,
        },
        "pluginVersion": PLUGIN_VERSION,
    }


def timeseries(title, targets, x, y, w=12, h=8, unit="short", desc="", stacked=False,
               bars=False, fill=15, overrides=None, transforms=None):
    return {
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
            "legend": {
                "calcs": ["lastNotNull", "max"],
                "displayMode": "table",
                "placement": "bottom",
                "showLegend": True,
            },
            "tooltip": {"hideZeros": False, "mode": "multi", "sort": "desc"},
        },
        "transformations": transforms or [],
        "pluginVersion": PLUGIN_VERSION,
    }


def bargauge(title, targets, x, y, w=12, h=8, unit="short", desc="", min_value=0,
             max_value=None, thresholds=None, transforms=None):
    defaults = {
        "color": {"mode": "thresholds"},
        "mappings": [],
        "min": min_value,
        "thresholds": {
            "mode": "absolute",
            "steps": thresholds or [
                {"color": "green", "value": 0},
                {"color": "yellow", "value": 70},
                {"color": "red", "value": 90},
            ],
        },
        "unit": unit,
    }
    if max_value is not None:
        defaults["max"] = max_value
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
            "namePlacement": "auto",
            "valueMode": "color",
            "showUnfilled": True,
            "sizing": "auto",
            "minVizHeight": 16,
            "maxVizHeight": 300,
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
                "mappings": [],
                "min": min_value,
                "max": max_value,
                "thresholds": {
                    "mode": "absolute",
                    "steps": thresholds or [
                        {"color": "green", "value": 0},
                        {"color": "yellow", "value": 0.6},
                        {"color": "red", "value": 0.85},
                    ],
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
    return {
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
                "mappings": mappings or [],
                "thresholds": {"mode": "absolute", "steps": [{"color": "green", "value": 0}]},
            },
            "overrides": overrides or [],
        },
        "gridPos": {"x": x, "y": y, "w": w, "h": h},
        "options": {
            "alignValue": "left",
            "mergeValues": True,
            "rowHeight": 0.8,
            "showValue": "auto",
            "legend": {"displayMode": "list", "placement": "bottom", "showLegend": True},
            "tooltip": {"hideZeros": False, "mode": "single", "sort": "none"},
        },
        "pluginVersion": PLUGIN_VERSION,
    }


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


BOOL_MAP = [
    {
        "type": "value",
        "options": {
            "0": {"color": "red", "index": 0, "text": "No"},
            "1": {"color": "green", "index": 1, "text": "Yes"},
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

STATE_OVERRIDES = [
    {
        "matcher": {"id": "byType", "options": "number"},
        "properties": [
            {
                "id": "mappings",
                "value": [
                    {
                        "type": "value",
                        "options": {
                            "0": {"text": "Down", "color": "red"},
                            "1": {"text": "Up", "color": "green"},
                        },
                    }
                ],
            }
        ],
    }
]

I = '$instance'


def build_dashboard():
    panels = []
    y = 0

    panels.append(text_panel(
        "# TrueNAS Operations Center\n\n"
        "Comprehensive monitoring covering **system health, CPU, memory, ZFS pools & ARC, disks, network, "
        "services, shares, apps, VMs, boot environments, hardware, alerts, tasks, and exporter diagnostics**.\n\n"
        "> **Tip:** start with `$instance`, then narrow by `$pool`, `$dataset`, `$disk`, `$service`, `$app`, or `$method`. "
        "Collapsed detail rows keep the default view fast.",
        0, y, h=4,
    ))
    y += 4

    # ── ROW: Overview ───────────────────────────────────────────────────
    panels.append(row("System Overview", y))
    y += 1
    panels.extend([
        stat("Status", f'min(truenas_up{{instance=~"{I}"}})', 0, y, w=2, desc="Exporter reachable.", mappings=UP_MAP),
        stat("Ready", f'min(truenas_system_ready{{instance=~"{I}"}})', 2, y, w=2, desc="Middleware reports system ready.", mappings=UP_MAP),
        stat("Uptime", f'max(truenas_host_uptime_seconds{{instance=~"{I}"}})', 4, y, w=2, unit="s", desc="Host uptime."),
        stat("CPU Cores", f'max(truenas_host_cpu_cores{{instance=~"{I}"}})', 6, y, w=2, desc="Total CPU cores (incl. HT)."),
        stat("RAM", f'max(truenas_host_physical_memory_bytes{{instance=~"{I}"}})', 8, y, w=2, unit="bytes", desc="Total physical RAM."),
        stat("Pools", f'truenas_pool_count{{instance=~"{I}"}}', 10, y, w=2, desc="Number of storage pools."),
        stat("Disks", f'truenas_disk_count{{instance=~"{I}"}}', 12, y, w=2, desc="Number of disks."),
        stat("Datasets", f'truenas_dataset_count{{instance=~"{I}"}}', 14, y, w=2, desc="Number of datasets."),
        stat("Alerts", f'sum(truenas_alert_count_by_level{{instance=~"{I}", level=~"$level"}})', 16, y, w=2,
             desc="Active alerts.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Update", f'max(truenas_update_available{{instance=~"{I}"}})', 18, y, w=2, desc="Update available.", mappings=BOOL_MAP),
        stat("Services", f'truenas_service_count{{instance=~"{I}"}}', 20, y, w=2, desc="Number of services."),
        stat("Apps", f'truenas_app_count{{instance=~"{I}"}}', 22, y, w=2, desc="Number of apps."),
    ])
    y += 4
    panels.extend([
        stat("CPU Used", f'avg(truenas_cpu_usage_percent{{instance=~"{I}"}})', 0, y, w=3, unit="percent",
             desc="Average CPU utilization.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 70}, {"color": "red", "value": 90}], graph=True),
        stat("RAM Used", f'100 * (sum(truenas_memory_physical_used_bytes{{instance=~"{I}"}}) / clamp_min(sum(truenas_memory_physical_total_bytes{{instance=~"{I}"}}), 1))', 3, y, w=3, unit="percent",
             desc="Physical memory in use.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}], graph=True),
        stat("Pool Used", f'100 * (sum(truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}}) / clamp_min(sum(truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}}), 1))', 6, y, w=3, unit="percent",
             desc="Aggregate pool utilization.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}], graph=True),
        stat("ARC Hit %", f'100 * avg(truenas_zfs_arc_hit_ratio{{instance=~"{I}"}})', 9, y, w=3, unit="percent",
             desc="ZFS ARC cache hit ratio.", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
        stat("Load 1m", f'avg(truenas_host_load_average{{instance=~"{I}", window="1m"}})', 12, y, w=3,
             desc="1-minute load average.", graph=True),
        stat("NFS Clients", f'sum(truenas_nfs_client_count{{instance=~"{I}"}})', 15, y, w=3, desc="Active NFS clients.", graph=True),
        stat("SMB Sessions", f'sum(truenas_smb_session_count{{instance=~"{I}"}})', 18, y, w=3, desc="Active SMB sessions.", graph=True),
        stat("Scrape Time", f'max(truenas_scrape_duration_seconds{{instance=~"{I}"}})', 21, y, w=3, unit="s",
             desc="Exporter scrape duration.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 10}, {"color": "red", "value": 30}], graph=True),
    ])
    y += 4

    # ── ROW: CPU & Load ─────────────────────────────────────────────────
    panels.append(row("CPU & Load", y))
    y += 1
    panels.append(timeseries(
        "CPU Breakdown",
        [
            tgt(f'avg(truenas_cpu_user_percent{{instance=~"{I}"}})', 'User %', 'A'),
            tgt(f'avg(truenas_cpu_system_percent{{instance=~"{I}"}})', 'System %', 'B'),
            tgt(f'avg(truenas_cpu_iowait_percent{{instance=~"{I}"}})', 'I/O Wait %', 'C'),
            tgt(f'avg(truenas_cpu_interrupt_percent{{instance=~"{I}"}})', 'Interrupt %', 'D'),
            tgt(f'avg(truenas_cpu_idle_percent{{instance=~"{I}"}})', 'Idle %', 'E'),
        ],
        0, y, unit="percent", stacked=True,
        desc="CPU time breakdown by category. I/O wait indicates storage bottlenecks.",
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
        "Per-Core CPU Usage",
        [tgt(f'truenas_cpu_core_usage_percent{{instance=~"{I}"}}', 'Core {{core}}', 'A')],
        0, y, unit="percent", fill=5,
        desc="Per-core utilization. Helps identify single-threaded bottlenecks.",
    ))
    panels.append(timeseries(
        "CPU Temperature per Core",
        [tgt(f'truenas_cpu_temperature_celsius{{instance=~"{I}"}}', 'Core {{core}}', 'A')],
        12, y, unit="celsius",
        desc="Per-core CPU temperatures. Sustained high temps indicate cooling issues.",
        overrides=[{"matcher": {"id": "byType", "options": "number"}, "properties": [
            {"id": "thresholds", "value": {"mode": "absolute", "steps": [
                {"color": "green", "value": 0}, {"color": "yellow", "value": 70}, {"color": "red", "value": 85}
            ]}},
            {"id": "custom.thresholdsStyle", "value": {"mode": "line+area"}},
        ]}],
    ))
    y += 8

    # ── ROW: Memory & Swap ──────────────────────────────────────────────
    panels.append(row("Memory & Swap", y))
    y += 1
    panels.extend([
        stat("Total RAM", f'truenas_memory_physical_total_bytes{{instance=~"{I}"}}', 0, y, w=4, unit="bytes", desc="Total physical RAM."),
        stat("Used RAM", f'truenas_memory_physical_used_bytes{{instance=~"{I}"}}', 4, y, w=4, unit="bytes", desc="Physical RAM in use."),
        stat("Available", f'truenas_memory_physical_available_bytes{{instance=~"{I}"}}', 8, y, w=4, unit="bytes", desc="Available RAM (free + reclaimable)."),
        stat("Cached", f'truenas_memory_physical_cached_bytes{{instance=~"{I}"}}', 12, y, w=4, unit="bytes", desc="Page cache."),
        stat("Swap Used", f'truenas_memory_swap_used_bytes{{instance=~"{I}"}}', 16, y, w=4, unit="bytes",
             desc="Swap in use. Any swap usage may indicate memory pressure.",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 1073741824}]),
        stat("ECC", f'max(truenas_host_ecc_memory{{instance=~"{I}"}})', 20, y, w=4, desc="ECC memory present.", mappings=BOOL_MAP),
    ])
    y += 4
    panels.append(timeseries(
        "Memory Composition Over Time",
        [
            tgt(f'truenas_memory_physical_used_bytes{{instance=~"{I}"}}', 'Used', 'A'),
            tgt(f'truenas_memory_physical_cached_bytes{{instance=~"{I}"}}', 'Cached', 'B'),
            tgt(f'truenas_memory_physical_buffers_bytes{{instance=~"{I}"}}', 'Buffers', 'C'),
            tgt(f'truenas_memory_physical_free_bytes{{instance=~"{I}"}}', 'Free', 'D'),
            tgt(f'truenas_zfs_arc_size_bytes{{instance=~"{I}"}}', 'ARC Size', 'E'),
        ],
        0, y, unit="bytes", stacked=False,
        desc="Memory breakdown over time. ARC overlaps with cached — it's reclaimable.",
    ))
    panels.append(timeseries(
        "Swap Usage Over Time",
        [
            tgt(f'truenas_memory_swap_total_bytes{{instance=~"{I}"}}', 'Swap Total', 'A'),
            tgt(f'truenas_memory_swap_used_bytes{{instance=~"{I}"}}', 'Swap Used', 'B'),
            tgt(f'truenas_memory_swap_free_bytes{{instance=~"{I}"}}', 'Swap Free', 'C'),
        ],
        12, y, unit="bytes",
        desc="Swap space trends. Increasing swap usage is a red flag.",
    ))
    y += 8

    # ── ROW: Storage & Pools ────────────────────────────────────────────
    panels.append(row("Storage & Pools", y))
    y += 1
    panels.extend([
        stat("Pool Count", f'truenas_pool_count{{instance=~"{I}"}}', 0, y, w=3, desc="Number of pools."),
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
        "Pool Utilization",
        [tgt(f'100 * truenas_pool_allocated_bytes{{instance=~"{I}", pool=~"$pool"}} / clamp_min(truenas_pool_size_bytes{{instance=~"{I}", pool=~"$pool"}}, 1)', '{{pool}}', 'A')],
        0, y, unit="percent", max_value=100,
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
            tgt(f'truenas_pool_scan_percent{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} scan %', 'A'),
        ],
        18, y, w=6, unit="percent",
        desc="Active scrub or resilver progress per pool.",
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
        table_target(f'max by (pool) (truenas_pool_dedup_ratio{{instance=~"{I}", pool=~"$pool"}})', 'G'),
        table_target(f'max by (pool) (truenas_pool_autotrim_enabled{{instance=~"{I}", pool=~"$pool"}})', 'H'),
    ]
    pool_table_transforms = [
        outer_join('pool'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {
                'pool': 'Pool', 'Value #A': 'Size', 'Value #B': 'Allocated', 'Value #C': 'Free',
                'Value #D': 'Frag %', 'Value #E': 'Healthy', 'Value #F': 'Used %',
                'Value #G': 'Dedup Ratio', 'Value #H': 'Autotrim',
            },
            'indexByName': {'Pool': 0, 'Used %': 1, 'Allocated': 2, 'Free': 3, 'Size': 4, 'Frag %': 5, 'Dedup Ratio': 6, 'Autotrim': 7, 'Healthy': 8},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Used %', 'desc': True}]}),
    ]
    pool_overrides = [
        {"matcher": {"id": "byName", "options": "Used %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
        {"matcher": {"id": "byName", "options": "Healthy"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": UP_MAP}]},
        {"matcher": {"id": "byName", "options": "Autotrim"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        {"matcher": {"id": "byName", "options": "Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Allocated"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Free"}, "properties": [{"id": "unit", "value": "bytes"}]},
    ]
    panels.append(table(
        "Pool Inventory", pool_table_targets, 0, y, h=10,
        desc="Pool inventory with fill ratio, fragmentation, dedup ratio, autotrim, and health.",
        overrides=pool_overrides, transforms=pool_table_transforms, sort_col='Used %',
    ))
    y += 10
    # Vdev errors
    vdev_error_targets = [
        table_target(f'max by (pool, vdev) (truenas_pool_vdev_read_errors{{instance=~"{I}", pool=~"$pool"}})', 'A'),
        table_target(f'max by (pool, vdev) (truenas_pool_vdev_write_errors{{instance=~"{I}", pool=~"$pool"}})', 'B'),
        table_target(f'max by (pool, vdev) (truenas_pool_vdev_checksum_errors{{instance=~"{I}", pool=~"$pool"}})', 'C'),
    ]
    vdev_error_transforms = [
        outer_join('pool'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {'pool': 'Pool', 'vdev': 'Vdev', 'Value #A': 'Read Errors', 'Value #B': 'Write Errors', 'Value #C': 'Checksum Errors'},
            'indexByName': {'Pool': 0, 'Vdev': 1, 'Read Errors': 2, 'Write Errors': 3, 'Checksum Errors': 4},
        }),
    ]
    vdev_error_overrides = [
        {"matcher": {"id": "byName", "options": n}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "red", "value": 1}]}}]}
        for n in ("Read Errors", "Write Errors", "Checksum Errors")
    ]
    panels.append(table(
        "Pool Vdev Errors", vdev_error_targets, 0, y, h=8,
        desc="Any non-zero error count warrants investigation.",
        overrides=vdev_error_overrides, transforms=vdev_error_transforms,
    ))
    y += 8
    panels.append(timeseries(
        "Pool Scrub ETA",
        [tgt(f'truenas_pool_scan_seconds_remaining{{instance=~"{I}", pool=~"$pool"}}', '{{pool}}', 'A')],
        0, y, unit="s", desc="Estimated seconds remaining for active pool scans.",
    ))
    panels.append(timeseries(
        "Pool Realtime I/O",
        [
            tgt(f'truenas_pool_realtime_read_bytes_per_second{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} read', 'A'),
            tgt(f'truenas_pool_realtime_write_bytes_per_second{{instance=~"{I}", pool=~"$pool"}}', '{{pool}} write', 'B'),
        ],
        12, y, unit="Bps", desc="Per-pool read/write throughput.",
    ))
    y += 8

    # ── ROW: ZFS ARC & Cache ────────────────────────────────────────────
    panels.append(row("ZFS ARC & Cache", y))
    y += 1
    panels.extend([
        stat("ARC Hit %", f'100 * truenas_zfs_arc_hit_ratio{{instance=~"{I}"}}', 0, y, w=3, unit="percent",
             desc="ARC cache hit ratio.", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
        stat("ARC Size", f'truenas_zfs_arc_size_bytes{{instance=~"{I}"}}', 3, y, w=3, unit="bytes", desc="Current ARC size."),
        stat("ARC Max", f'truenas_zfs_arc_max_size_bytes{{instance=~"{I}"}}', 6, y, w=3, unit="bytes", desc="Maximum ARC size."),
        stat("ARC Min", f'truenas_zfs_arc_min_size_bytes{{instance=~"{I}"}}', 9, y, w=3, unit="bytes", desc="Minimum ARC size."),
        stat("ARC Free", f'truenas_zfs_arc_free_memory_bytes{{instance=~"{I}"}}', 12, y, w=3, unit="bytes", desc="ARC free memory."),
        stat("ARC Avail", f'truenas_zfs_arc_available_bytes{{instance=~"{I}"}}', 15, y, w=3, unit="bytes", desc="ARC available memory."),
        stat("L2ARC Hit %", f'100 * truenas_zfs_l2arc_hit_ratio{{instance=~"{I}"}}', 18, y, w=3, unit="percent",
             desc="L2ARC hit ratio.", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 50}, {"color": "green", "value": 80}], graph=True),
        stat("Data Hit %", f'100 * truenas_zfs_demand_data_hit_ratio{{instance=~"{I}"}}', 21, y, w=3, unit="percent",
             desc="Demand data hit ratio.", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
    ])
    y += 4
    panels.append(timeseries(
        "ARC Hit & Miss Rates",
        [
            tgt(f'truenas_zfs_arc_hits_per_second{{instance=~"{I}"}}', 'Hits/s', 'A'),
            tgt(f'truenas_zfs_arc_misses_per_second{{instance=~"{I}"}}', 'Misses/s', 'B'),
        ],
        0, y, unit="ops",
        desc="ARC hit and miss rates. A rising miss rate means the working set exceeds ARC.",
    ))
    panels.append(timeseries(
        "ARC Size Over Time",
        [
            tgt(f'truenas_zfs_arc_size_bytes{{instance=~"{I}"}}', 'ARC Size', 'A'),
            tgt(f'truenas_zfs_arc_min_size_bytes{{instance=~"{I}"}}', 'ARC Min', 'B'),
            tgt(f'truenas_zfs_arc_max_size_bytes{{instance=~"{I}"}}', 'ARC Max', 'C'),
        ],
        12, y, unit="bytes",
        desc="ARC size with min/max bounds. ARC growing to max is normal.",
    ))
    y += 8
    panels.append(timeseries(
        "ARC & L2ARC Hit Ratios",
        [
            tgt(f'100 * truenas_zfs_arc_hit_ratio{{instance=~"{I}"}}', 'ARC hit %', 'A'),
            tgt(f'100 * truenas_zfs_l2arc_hit_ratio{{instance=~"{I}"}}', 'L2ARC hit %', 'B'),
            tgt(f'100 * truenas_zfs_demand_data_hit_ratio{{instance=~"{I}"}}', 'Data hit %', 'C'),
            tgt(f'100 * truenas_zfs_demand_meta_hit_ratio{{instance=~"{I}"}}', 'Meta hit %', 'D'),
        ],
        0, y, w=8, unit="percent",
        desc="Cache hit ratios — higher is better.",
    ))
    panels.append(timeseries(
        "Demand Data & Metadata Rates",
        [
            tgt(f'truenas_zfs_demand_data_accesses_per_second{{instance=~"{I}"}}', 'Data accesses/s', 'A'),
            tgt(f'truenas_zfs_demand_data_hits_per_second{{instance=~"{I}"}}', 'Data hits/s', 'B'),
            tgt(f'truenas_zfs_demand_metadata_accesses_per_second{{instance=~"{I}"}}', 'Meta accesses/s', 'C'),
            tgt(f'truenas_zfs_demand_meta_hits_per_second{{instance=~"{I}"}}', 'Meta hits/s', 'D'),
        ],
        8, y, w=8, unit="ops",
        desc="Demand access rates for data and metadata.",
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
        stat("Disk Count", f'truenas_disk_count{{instance=~"{I}"}}', 0, y, w=4, desc="Number of disks."),
        stat("Hottest Disk", f'max(truenas_disk_temperature_celsius{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 4, y, w=4, unit="celsius",
             desc="Highest disk temperature.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 40}, {"color": "red", "value": 50}], graph=True),
        stat("Avg Busy", f'avg(truenas_disk_busy_percent{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 8, y, w=4, unit="percent",
             desc="Average disk busy %.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 60}, {"color": "red", "value": 85}], graph=True),
        stat("Temp Alerts", f'sum(truenas_disk_temperature_alert_count{{instance=~"{I}"}})', 12, y, w=4,
             desc="Disk temperature alerts.", thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("Total Capacity", f'sum(truenas_disk_size_bytes{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 16, y, w=4, unit="bytes", desc="Total raw disk capacity."),
        stat("Used Disks", f'count(truenas_disk_in_use{{instance=~"{I}", disk=~"$disk"}} == 1)', 20, y, w=4, desc="Disks in use by a pool."),
    ])
    y += 4
    panels.append(timeseries(
        "Disk Throughput by Device",
        [
            tgt(f'topk(8, truenas_disk_read_bytes_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'read {{disk}}', 'A'),
            tgt(f'topk(8, truenas_disk_write_bytes_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'write {{disk}}', 'B'),
        ],
        0, y, unit="Bps", desc="Read/write throughput for the busiest devices.",
    ))
    panels.append(timeseries(
        "Disk IOPS by Device",
        [
            tgt(f'topk(8, truenas_disk_read_ops_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'read {{disk}}', 'A'),
            tgt(f'topk(8, truenas_disk_write_ops_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'write {{disk}}', 'B'),
        ],
        12, y, unit="iops", desc="Read/write IOPS per device.",
    ))
    y += 8
    panels.append(timeseries(
        "Disk Busy %",
        [tgt(f'topk(8, truenas_disk_busy_percent{{instance=~"{I}", disk=~"$disk", disk!="total"}})', '{{disk}}', 'A')],
        0, y, unit="percent", desc="Disk utilization saturation.",
    ))
    panels.append(timeseries(
        "Disk Temperature Over Time",
        [tgt(f'truenas_disk_temperature_celsius{{instance=~"{I}", disk=~"$disk", disk!="total"}}', '{{disk}}', 'A')],
        12, y, unit="celsius", desc="Per-disk temperatures over time.",
    ))
    y += 8
    panels.append(bargauge(
        "Disk Temperatures",
        [tgt(f'truenas_disk_temperature_celsius{{instance=~"{I}", disk=~"$disk", disk!="total"}}', '{{disk}}', 'A')],
        0, y, unit="celsius",
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 40}, {"color": "red", "value": 50}],
    ))
    disk_bar_transforms = [
        tf('labelsToFields', {'mode': 'columns', 'source': 'labels'}),
        tf('reduce', {'reducers': ['lastNotNull']}),
        tf('organize', {'excludeByName': {'Time': True}}),
        tf('sortBy', {'fields': [{'displayName': 'lastNotNull', 'desc': True}]}),
    ]
    panels.append(barchart(
        "Disk Sizes",
        [tgt(f'truenas_disk_size_bytes{{instance=~"{I}", disk=~"$disk", disk!="total"}}', '{{disk}}', 'A')],
        12, y, unit="bytes", transforms=disk_bar_transforms,
    ))
    y += 8
    # Disk inventory table with SMART & rotational info
    disk_table_targets = [
        table_target(f'max by (disk) (truenas_disk_size_bytes{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'A'),
        table_target(f'max by (disk) (truenas_disk_busy_percent{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'B'),
        table_target(f'max by (disk) (truenas_disk_temperature_celsius{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'C'),
        table_target(f'max by (disk) (truenas_disk_read_bytes_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'D'),
        table_target(f'max by (disk) (truenas_disk_write_bytes_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'E'),
        table_target(f'max by (disk) (truenas_disk_read_ops_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'F'),
        table_target(f'max by (disk) (truenas_disk_write_ops_per_second{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'G'),
        table_target(f'max by (disk) (truenas_disk_smart_enabled{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'H'),
        table_target(f'max by (disk) (truenas_disk_rotational{{instance=~"{I}", disk=~"$disk", disk!="total"}})', 'J'),
    ]
    disk_table_transforms = [
        outer_join('disk'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {
                'disk': 'Disk', 'Value #A': 'Size', 'Value #B': 'Busy %', 'Value #C': 'Temp C',
                'Value #D': 'Read B/s', 'Value #E': 'Write B/s', 'Value #F': 'Read IOPS', 'Value #G': 'Write IOPS',
                'Value #H': 'SMART', 'Value #J': 'HDD',
            },
            'indexByName': {'Disk': 0, 'Busy %': 1, 'Temp C': 2, 'Read B/s': 3, 'Write B/s': 4, 'Read IOPS': 5, 'Write IOPS': 6, 'Size': 7, 'SMART': 8, 'HDD': 9},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Busy %', 'desc': True}]}),
    ]
    disk_overrides = [
        {"matcher": {"id": "byName", "options": "Busy %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 60}, {"color": "red", "value": 85}]}}]},
        {"matcher": {"id": "byName", "options": "Temp C"}, "properties": [{"id": "unit", "value": "celsius"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 40}, {"color": "red", "value": 50}]}}]},
        {"matcher": {"id": "byName", "options": "Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Read B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
        {"matcher": {"id": "byName", "options": "Write B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
        {"matcher": {"id": "byName", "options": "Read IOPS"}, "properties": [{"id": "unit", "value": "iops"}]},
        {"matcher": {"id": "byName", "options": "Write IOPS"}, "properties": [{"id": "unit", "value": "iops"}]},
        {"matcher": {"id": "byName", "options": "SMART"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        {"matcher": {"id": "byName", "options": "HDD"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": [{"type": "value", "options": {"0": {"color": "blue", "text": "SSD/NVMe"}, "1": {"color": "orange", "text": "HDD"}}}]}]},
    ]
    panels.append(table(
        "Disk Inventory", disk_table_targets, 0, y,
        desc="Per-disk health, performance, SMART status, and type.",
        overrides=disk_overrides, transforms=disk_table_transforms, sort_col='Busy %',
    ))
    y += 10

    # ── ROW: Network & Interfaces ───────────────────────────────────────
    panels.append(row("Network & Interfaces", y))
    y += 1
    panels.extend([
        stat("Interfaces", f'truenas_interface_count{{instance=~"{I}"}}', 0, y, w=3, desc="Network interface count."),
        stat("Gateway OK", f'min(truenas_network_gateway_reachable{{instance=~"{I}"}})', 3, y, w=3, desc="Default gateway reachable.", mappings=UP_MAP),
        stat("Nameservers", f'truenas_network_nameservers{{instance=~"{I}"}}', 6, y, w=3, desc="Configured nameservers."),
        stat("Default Routes", f'truenas_network_default_routes{{instance=~"{I}"}}', 9, y, w=3, desc="Number of default routes."),
        stat("DNS Resolvers", f'truenas_dns_resolver_count{{instance=~"{I}"}}', 12, y, w=3, desc="Configured DNS resolvers."),
        stat("Pending Changes", f'max(truenas_interface_has_pending_changes{{instance=~"{I}"}})', 15, y, w=3, desc="Unapplied network changes.", mappings=BOOL_MAP),
        stat("Checkin Wait", f'max(truenas_interface_checkin_waiting_seconds{{instance=~"{I}"}})', 18, y, w=3, unit="s", desc="Seconds until pending changes auto-rollback."),
        stat("HTTP Proxy", f'max(truenas_network_httpproxy_configured{{instance=~"{I}"}})', 21, y, w=3, desc="HTTP proxy configured.", mappings=BOOL_MAP),
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
        0, y, w=12, desc="Link up/down events.", overrides=STATE_OVERRIDES,
    ))
    panels.append(bargauge(
        "Interface MTU",
        [tgt(f'truenas_interface_mtu{{instance=~"{I}", interface=~"$interface"}}', '{{interface}}', 'A')],
        12, y, unit="short", desc="MTU per interface.",
        thresholds=[{"color": "blue", "value": 0}, {"color": "green", "value": 9000}],
    ))
    y += 8

    # ── ROW: Services & Shares ──────────────────────────────────────────
    panels.append(row("Services & Shares", y))
    y += 1
    panels.extend([
        stat("Services", f'truenas_service_count{{instance=~"{I}"}}', 0, y, w=2, desc="Total services."),
        stat("Running", f'count(truenas_service_running{{instance=~"{I}", service=~"$service"}} == 1)', 2, y, w=2, desc="Running services."),
        stat("SMB Shares", f'sum(truenas_smb_share_count{{instance=~"{I}"}})', 4, y, w=2, desc="Configured SMB shares."),
        stat("NFS Shares", f'sum(truenas_nfs_share_count{{instance=~"{I}"}})', 6, y, w=2, desc="Configured NFS shares."),
        stat("WebDAV", f'sum(truenas_webdav_share_count{{instance=~"{I}"}})', 8, y, w=2, desc="WebDAV shares."),
        stat("iSCSI Tgts", f'sum(truenas_iscsi_target_count{{instance=~"{I}"}})', 10, y, w=2, desc="iSCSI targets."),
        stat("SMB Sess", f'sum(truenas_smb_session_count{{instance=~"{I}"}})', 12, y, w=2, desc="Active SMB sessions.", graph=True),
        stat("SMB Files", f'sum(truenas_smb_open_file_count{{instance=~"{I}"}})', 14, y, w=2, desc="Open SMB files.", graph=True),
        stat("NFS v3", f'sum(truenas_nfs_v3_client_count{{instance=~"{I}"}})', 16, y, w=2, desc="NFSv3 clients.", graph=True),
        stat("NFS v4", f'sum(truenas_nfs_v4_client_count{{instance=~"{I}"}})', 18, y, w=2, desc="NFSv4 clients.", graph=True),
        stat("iSCSI Cli", f'sum(truenas_iscsi_client_count{{instance=~"{I}"}})', 20, y, w=2, desc="iSCSI clients.", graph=True),
        stat("NVMe-oF", f'sum(truenas_nvmet_session_count{{instance=~"{I}"}})', 22, y, w=2, desc="NVMe-oF sessions.", graph=True),
    ])
    y += 4
    panels.append(state_timeline(
        "Service Runtime State",
        [tgt(f'truenas_service_running{{instance=~"{I}", service=~"$service"}}', '{{service}}', 'A')],
        0, y, w=12, desc="Service running/stopped history.", overrides=STATE_OVERRIDES,
    ))
    panels.append(piechart(
        "Protocol Activity Mix",
        [
            tgt(f'sum(truenas_smb_connection_count{{instance=~"{I}"}})', 'SMB', 'A'),
            tgt(f'sum(truenas_nfs_client_count{{instance=~"{I}"}})', 'NFS', 'B'),
            tgt(f'sum(truenas_iscsi_client_count{{instance=~"{I}"}})', 'iSCSI', 'C'),
            tgt(f'sum(truenas_nvmet_session_count{{instance=~"{I}"}})', 'NVMe-oF', 'D'),
        ],
        12, y, w=12, desc="Relative protocol activity.",
    ))
    y += 8
    panels.append(timeseries(
        "NFS Operations/s",
        [tgt(f'truenas_nfs_server_ops_per_second{{instance=~"{I}"}}', 'NFS ops/s', 'A')],
        0, y, unit="ops", desc="NFS server operations per second.",
    ))
    panels.append(timeseries(
        "SMB Activity Over Time",
        [
            tgt(f'sum(truenas_smb_session_count{{instance=~"{I}"}})', 'Sessions', 'A'),
            tgt(f'sum(truenas_smb_connection_count{{instance=~"{I}"}})', 'Connections', 'B'),
            tgt(f'sum(truenas_smb_open_file_count{{instance=~"{I}"}})', 'Open Files', 'C'),
        ],
        12, y, unit="short", desc="SMB sessions, connections, and open files over time.",
    ))
    y += 8
    # iSCSI detail stats
    panels.extend([
        stat("Portals", f'sum(truenas_iscsi_portal_count{{instance=~"{I}"}})', 0, y, w=3, desc="iSCSI portals."),
        stat("Extents", f'sum(truenas_iscsi_extent_count{{instance=~"{I}"}})', 3, y, w=3, desc="iSCSI extents."),
        stat("Initiators", f'sum(truenas_iscsi_initiator_count{{instance=~"{I}"}})', 6, y, w=3, desc="iSCSI initiator groups."),
        stat("ALUA", f'max(truenas_iscsi_alua_enabled{{instance=~"{I}"}})', 9, y, w=3, desc="iSCSI ALUA protocol.", mappings=BOOL_MAP),
        stat("iSER", f'max(truenas_iscsi_iser_enabled{{instance=~"{I}"}})', 12, y, w=3, desc="iSCSI iSER (RDMA) protocol.", mappings=BOOL_MAP),
        stat("SMB Multi", f'max(truenas_smb_multichannel_enabled{{instance=~"{I}"}})', 15, y, w=3, desc="SMB multichannel.", mappings=BOOL_MAP),
        stat("NFSv4 On", f'max(truenas_nfs_v4_enabled{{instance=~"{I}"}})', 18, y, w=3, desc="NFSv4 enabled.", mappings=BOOL_MAP),
        stat("NFS Threads", f'max(truenas_nfs_servers{{instance=~"{I}"}})', 21, y, w=3, desc="NFS server threads."),
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
        {"matcher": {"id": "byName", "options": "Running"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": UP_MAP}]},
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
        stat("NVIDIA GPU", f'max(truenas_docker_nvidia_present{{instance=~"{I}"}})', 15, y, w=3, desc="NVIDIA GPU available.", mappings=BOOL_MAP),
        stat("Catalog Trains", f'truenas_catalog_train_count{{instance=~"{I}"}}', 18, y, w=3, desc="App catalog trains."),
        stat("Outdated Imgs", f'count(truenas_app_state{{instance=~"{I}"}}) or vector(0)', 21, y, w=3, desc="App state entries."),
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
        "App Block I/O",
        [
            tgt(f'topk(8, truenas_app_blkio_read_bytes{{instance=~"{I}", app=~"$app"}})', 'read {{app}}', 'A'),
            tgt(f'topk(8, truenas_app_blkio_write_bytes{{instance=~"{I}", app=~"$app"}})', 'write {{app}}', 'B'),
        ],
        0, y, unit="bytes", desc="Read/write volume by app.",
    ))
    panels.append(timeseries(
        "App Network",
        [
            tgt(f'topk(8, truenas_app_net_rx_bytes_per_second{{instance=~"{I}", app=~"$app"}})', 'rx {{app}}', 'A'),
            tgt(f'topk(8, truenas_app_net_tx_bytes_per_second{{instance=~"{I}", app=~"$app"}})', 'tx {{app}}', 'B'),
        ],
        12, y, unit="Bps", desc="App network ingress/egress.",
    ))
    y += 8
    app_table_targets = [
        table_target(f'max by (app) (truenas_app_cpu_percent{{instance=~"{I}", app=~"$app"}})', 'A'),
        table_target(f'max by (app) (truenas_app_memory_bytes{{instance=~"{I}", app=~"$app"}})', 'B'),
        table_target(f'max by (app) (truenas_app_net_rx_bytes_per_second{{instance=~"{I}", app=~"$app"}})', 'C'),
        table_target(f'max by (app) (truenas_app_net_tx_bytes_per_second{{instance=~"{I}", app=~"$app"}})', 'D'),
    ]
    app_table_transforms = [
        outer_join('app'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {'app': 'App', 'Value #A': 'CPU %', 'Value #B': 'Memory', 'Value #C': 'RX B/s', 'Value #D': 'TX B/s'},
            'indexByName': {'App': 0, 'CPU %': 1, 'Memory': 2, 'RX B/s': 3, 'TX B/s': 4},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Memory', 'desc': True}]}),
    ]
    app_overrides = [
        {"matcher": {"id": "byName", "options": "CPU %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 50}, {"color": "red", "value": 80}]}}]},
        {"matcher": {"id": "byName", "options": "Memory"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "RX B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
        {"matcher": {"id": "byName", "options": "TX B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
    ]
    panels.append(table(
        "App Inventory", app_table_targets, 0, y,
        desc="App resource footprint.", overrides=app_overrides, transforms=app_table_transforms, sort_col='Memory',
    ))
    y += 10

    # ── ROW: Virtualization ─────────────────────────────────────────────
    panels.append(row("Virtualization (VMs & Incus)", y))
    y += 1
    panels.extend([
        stat("VM Count", f'sum(truenas_vm_count{{instance=~"{I}"}})', 0, y, w=3, desc="Virtual machines."),
        stat("Virt Support", f'max(truenas_vm_supports_virtualization{{instance=~"{I}"}})', 3, y, w=3, desc="KVM/HW virt available.", mappings=BOOL_MAP),
        stat("Max vCPUs", f'max(truenas_vm_maximum_supported_vcpus{{instance=~"{I}"}})', 6, y, w=3, desc="Maximum supported vCPUs."),
        stat("VM Avail RAM", f'sum(truenas_vm_available_memory_bytes{{instance=~"{I}"}})', 9, y, w=3, unit="bytes", desc="Available memory for VMs."),
        stat("Incus Inst", f'sum(truenas_virt_instance_count{{instance=~"{I}"}})', 12, y, w=3, desc="Incus/LXD instances."),
        stat("Incus Vols", f'sum(truenas_virt_volume_count{{instance=~"{I}"}})', 15, y, w=3, desc="Incus storage volumes."),
        stat("IOMMU", f'max(truenas_iommu_enabled{{instance=~"{I}"}})', 18, y, w=3, desc="IOMMU/PCI passthrough.", mappings=BOOL_MAP),
        stat("VM Mem Used", f'sum(truenas_vm_vmemory_in_use_bytes{{instance=~"{I}"}})', 21, y, w=3, unit="bytes", desc="VM memory in use."),
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
        [tgt(f'truenas_virt_instance_cpu_usage_percent{{instance=~"{I}"}}', '{{instance}}', 'A')],
        12, y, unit="percent", desc="Per-instance CPU usage.",
    ))
    y += 8
    panels.append(timeseries(
        "Incus Instance Memory",
        [tgt(f'truenas_virt_instance_mem_bytes{{instance=~"{I}"}}', '{{instance}}', 'A')],
        0, y, unit="bytes", desc="Per-instance memory usage.",
    ))
    panels.append(bargauge(
        "Incus Volume Sizes",
        [tgt(f'truenas_virt_volume_size_bytes{{instance=~"{I}"}}', '{{volume}}', 'A')],
        12, y, unit="bytes", desc="Incus storage volume sizes.",
    ))
    y += 8

    # ── ROW: Alerts, Tasks & Updates ────────────────────────────────────
    panels.append(row("Alerts, Tasks & Updates", y))
    y += 1
    panels.extend([
        stat("Total Alerts", f'sum(truenas_alert_count_by_level{{instance=~"{I}", level=~"$level"}})', 0, y, w=3,
             desc="Active alerts.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Critical", f'sum(truenas_alert_count_by_level{{instance=~"{I}", level="CRITICAL"}})', 3, y, w=3,
             desc="Critical alerts.", thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}], graph=True),
        stat("Warning", f'sum(truenas_alert_count_by_level{{instance=~"{I}", level="WARNING"}})', 6, y, w=3,
             desc="Warning alerts.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Tasks", f'sum(truenas_task_count{{instance=~"{I}"}})', 9, y, w=3, desc="Scheduled tasks."),
        stat("Tasks On", f'sum(truenas_task_enabled{{instance=~"{I}"}})', 12, y, w=3, desc="Enabled tasks."),
        stat("Cloud Bkp", f'sum(truenas_cloud_backup_task_count{{instance=~"{I}"}})', 15, y, w=3, desc="Cloud backup tasks."),
        stat("Cron Jobs", f'truenas_cronjob_count{{instance=~"{I}"}}', 18, y, w=3, desc="Configured cron jobs."),
        stat("Reboot Req", f'max(truenas_system_reboot_required{{instance=~"{I}"}})', 21, y, w=3, desc="Reboot pending.", mappings=BOOL_MAP),
    ])
    y += 4
    panels.append(piechart(
        "Alert Level Distribution",
        [tgt(f'truenas_alert_count_by_level{{instance=~"{I}", level=~"$level"}}', '{{level}}', 'A')],
        0, y, w=8, desc="Current alert severity mix.",
    ))
    task_type_transforms = [
        tf('labelsToFields', {'mode': 'columns', 'source': 'labels'}),
        tf('reduce', {'reducers': ['lastNotNull']}),
        tf('organize', {'excludeByName': {'Time': True}}),
    ]
    panels.append(barchart(
        "Tasks by Type",
        [tgt(f'count by (task_type) (truenas_task_state{{instance=~"{I}", task_type=~"$task_type"}})', '{{task_type}}', 'A')],
        8, y, w=8, desc="Scheduled work breakdown.", transforms=task_type_transforms,
    ))
    panels.append(timeseries(
        "Alert Count Over Time",
        [tgt(f'truenas_alert_count{{instance=~"{I}"}}', 'Alerts', 'A')],
        16, y, w=8, desc="Alert count trend.",
    ))
    y += 8
    # Task state detail table
    panels.append(table(
        "Task State Detail",
        [
            table_target(f'max by (name, task_type, state) (truenas_task_state{{instance=~"{I}", task_type=~"$task_type"}} == 1)', 'A'),
            table_target(f'max by (name) (truenas_task_enabled{{instance=~"{I}", task_type=~"$task_type"}})', 'B'),
            table_target(f'time() - max by (name) (truenas_task_last_run_timestamp_seconds{{instance=~"{I}", task_type=~"$task_type"}})', 'C'),
        ],
        0, y, desc="Task status, enablement, and last run age.",
        transforms=[
            outer_join('name'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'Task', 'task_type': 'Type', 'state': 'State', 'Value #A': 'Active', 'Value #B': 'Enabled', 'Value #C': 'Last Run Age'},
                'indexByName': {'Task': 0, 'Type': 1, 'State': 2, 'Enabled': 3, 'Last Run Age': 4, 'Active': 5},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Task', 'desc': False}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Active"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": UP_MAP}]},
            {"matcher": {"id": "byName", "options": "Enabled"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
            {"matcher": {"id": "byName", "options": "Last Run Age"}, "properties": [{"id": "unit", "value": "s"}]},
        ],
        sort_col='Task', sort_desc=False,
    ))
    y += 10

    # ── ROW: Security & Platform ────────────────────────────────────────
    panels.append(row("Security & Platform", y))
    y += 1
    panels.extend([
        stat("2FA", f'max(truenas_2fa_enabled{{instance=~"{I}"}})', 0, y, w=3, desc="Two-factor auth.", mappings=BOOL_MAP),
        stat("SSH", f'max(truenas_ssh_enabled{{instance=~"{I}"}})', 3, y, w=3, desc="SSH service.", mappings=BOOL_MAP),
        stat("SSH Passwd", f'max(truenas_ssh_password_auth{{instance=~"{I}"}})', 6, y, w=3, desc="SSH password auth.", mappings=BOOL_MAP),
        stat("FTP", f'max(truenas_ftp_enabled{{instance=~"{I}"}})', 9, y, w=3, desc="FTP enabled.", mappings=BOOL_MAP),
        stat("SNMP", f'max(truenas_snmp_enabled{{instance=~"{I}"}})', 12, y, w=3, desc="SNMP enabled.", mappings=BOOL_MAP),
        stat("FIPS", f'max(truenas_fips_enabled{{instance=~"{I}"}})', 15, y, w=3, desc="FIPS mode.", mappings=BOOL_MAP),
        stat("KMIP", f'max(truenas_kmip_enabled{{instance=~"{I}"}})', 18, y, w=3, desc="KMIP key management.", mappings=BOOL_MAP),
        stat("UPS", f'max(truenas_ups_configured{{instance=~"{I}"}})', 21, y, w=3, desc="UPS configured.", mappings=BOOL_MAP),
    ])
    y += 4
    panels.extend([
        stat("Production", f'max(truenas_is_production{{instance=~"{I}"}})', 0, y, w=3, desc="Marked as production.", mappings=BOOL_MAP),
        stat("iX Hardware", f'max(truenas_is_ix_hardware{{instance=~"{I}"}})', 3, y, w=3, desc="iXsystems hardware.", mappings=BOOL_MAP),
        stat("TN Connect", f'max(truenas_tn_connect_enabled{{instance=~"{I}"}})', 6, y, w=3, desc="TrueNAS Connect.", mappings=BOOL_MAP),
        stat("TrueCommand", f'max(truenas_managed_by_truecommand{{instance=~"{I}"}})', 9, y, w=3, desc="Managed by TrueCommand.", mappings=BOOL_MAP),
        stat("Mail Conf", f'max(truenas_mail_configured{{instance=~"{I}"}})', 12, y, w=3, desc="Email configured.", mappings=BOOL_MAP),
        stat("Support", f'max(truenas_support_available{{instance=~"{I}"}})', 15, y, w=3, desc="Proactive support.", mappings=BOOL_MAP),
        stat("Dir Svc OK", f'max(truenas_directoryservices_healthy{{instance=~"{I}"}})', 18, y, w=3, desc="Directory services healthy.", mappings=UP_MAP),
        stat("Sessions", f'max(truenas_auth_sessions_active{{instance=~"{I}"}})', 21, y, w=3, desc="Active API sessions."),
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
        overrides=[{"matcher": {"id": "byName", "options": "Count"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}]}}]}],
        sort_col='Count',
    ))
    panels.append(table(
        "Certificate Expiry",
        [table_target(f'truenas_certificate_days_to_expiry{{instance=~"{I}"}}', 'A')],
        12, y, w=12, h=10,
        desc="Days until certificate expires. Negative = already expired.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'name': 'Certificate', 'Value': 'Days to Expiry'},
                'indexByName': {'Certificate': 0, 'Days to Expiry': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Days to Expiry', 'desc': False}]}),
        ],
        overrides=[{"matcher": {"id": "byName", "options": "Days to Expiry"}, "properties": [{"id": "unit", "value": "short"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "red", "value": None}, {"color": "yellow", "value": 14}, {"color": "green", "value": 30}]}}]}],
        sort_col='Days to Expiry', sort_desc=False,
    ))
    y += 10

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
        stat("Keep BEs", f'truenas_boot_env_keep_count{{instance=~"{I}"}}', 18, by, w=3),
        stat("Scan %", f'truenas_boot_pool_scan_percent{{instance=~"{I}"}}', 21, by, w=3, unit="percent"),
    ])
    by += 4
    boot_panels.append(gauge(
        "Boot Pool Usage",
        f'truenas_boot_pool_allocated_bytes{{instance=~"{I}"}} / clamp_min(truenas_boot_pool_size_bytes{{instance=~"{I}"}}, 1)',
        0, by, w=6, desc="Boot pool fill ratio.",
    ))
    boot_panels.append(bargauge(
        "Boot Environment Sizes",
        [tgt(f'truenas_boot_env_size_bytes{{instance=~"{I}"}}', '{{name}}', 'A')],
        6, by, w=18, unit="bytes", desc="Size per boot environment.",
    ))
    by += 8
    panels.append(row("Boot Environment", y, collapsed=True, panels=boot_panels))
    y += 1

    # ── COLLAPSED ROW: Hardware & IPMI ──────────────────────────────────
    hw_panels = []
    hy = y + 1
    hw_panels.extend([
        stat("IPMI Loaded", f'max(truenas_ipmi_loaded{{instance=~"{I}"}})', 0, hy, w=3, mappings=BOOL_MAP),
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
        stat("ECC Memory", f'max(truenas_host_ecc_memory{{instance=~"{I}"}})', 8, hy, w=4, mappings=BOOL_MAP),
        stat("Phys Cores", f'max(truenas_host_physical_cpu_cores{{instance=~"{I}"}})', 12, hy, w=4, desc="Physical CPU cores (no HT)."),
        stat("UPS Status", f'count(truenas_ups_status{{instance=~"{I}"}})', 16, hy, w=4),
        stat("Resilver On", f'max(truenas_pool_resilver_enabled{{instance=~"{I}"}})', 20, hy, w=4, mappings=BOOL_MAP),
    ])
    hy += 4
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
    proto_panels.append(timeseries(
        "FC Port Status",
        [tgt(f'truenas_fc_port_online{{instance=~"{I}"}}', '{{port}}', 'A')],
        0, py, desc="Fibre Channel port online status.",
    ))
    proto_panels.append(timeseries(
        "FC Port Speed",
        [tgt(f'truenas_fc_port_speed_gbit{{instance=~"{I}"}}', '{{port}}', 'A')],
        12, py, unit="short", desc="FC port link speed in Gbit/s.",
    ))
    py += 8
    panels.append(row("Advanced Protocols (NVMe-oF / FC / HA)", y, collapsed=True, panels=proto_panels))
    y += 1

    # ── COLLAPSED ROW: Audit & Directory Services ───────────────────────
    audit_panels = []
    ay = y + 1
    audit_panels.extend([
        stat("Audit Used", f'truenas_audit_dataset_used_bytes{{instance=~"{I}"}}', 0, ay, w=4, unit="bytes"),
        stat("Audit Avail", f'truenas_audit_dataset_available_bytes{{instance=~"{I}"}}', 4, ay, w=4, unit="bytes"),
        stat("Warn Fill %", f'truenas_audit_quota_fill_warning_percent{{instance=~"{I}"}}', 8, ay, w=4, unit="percent"),
        stat("Crit Fill %", f'truenas_audit_quota_fill_critical_percent{{instance=~"{I}"}}', 12, ay, w=4, unit="percent"),
        stat("Dir Svc OK", f'max(truenas_directoryservices_healthy{{instance=~"{I}"}})', 16, ay, w=4, mappings=UP_MAP),
        stat("Dir Faults", f'count(truenas_directoryservices_fault_reason{{instance=~"{I}"}})', 20, ay, w=4,
             thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
    ])
    ay += 4
    panels.append(row("Audit & Directory Services", y, collapsed=True, panels=audit_panels))
    y += 1

    # ── COLLAPSED ROW: System Configuration ─────────────────────────────
    cfg_panels = []
    cy = y + 1
    cfg_panels.extend([
        stat("Console Menu", f'max(truenas_consolemenu_enabled{{instance=~"{I}"}})', 0, cy, w=3, mappings=BOOL_MAP),
        stat("Serial Cons", f'max(truenas_serialconsole_enabled{{instance=~"{I}"}})', 3, cy, w=3, mappings=BOOL_MAP),
        stat("HTTPS Port", f'truenas_ui_https_port{{instance=~"{I}"}}', 6, cy, w=3),
        stat("Reporting On", f'max(truenas_reporting_enabled{{instance=~"{I}"}})', 9, cy, w=3, mappings=BOOL_MAP),
        stat("Exporters", f'truenas_reporting_exporter_count{{instance=~"{I}"}}', 12, cy, w=3),
        stat("Static Routes", f'truenas_static_route_count{{instance=~"{I}"}}', 15, cy, w=3),
        stat("Tunables", f'truenas_tunable_count{{instance=~"{I}"}}', 18, cy, w=3),
        stat("Init Scripts", f'truenas_initshutdownscript_count{{instance=~"{I}"}}', 21, cy, w=3),
    ])
    cy += 4
    panels.append(row("System Configuration", y, collapsed=True, panels=cfg_panels))
    y += 1

    # ── COLLAPSED ROW: Dataset Deep-Dive ────────────────────────────────
    ds_panels = []
    dy = y + 1
    ds_panels.append(bargauge(
        "Top Datasets by Referenced Bytes",
        [tgt(f'topk(15, truenas_dataset_referenced_bytes{{instance=~"{I}", dataset=~"$dataset"}})', '{{dataset}}', 'A')],
        0, dy, unit="bytes", desc="Datasets by referenced data size.",
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
        0, dy, unit="short", desc="Datasets with most snapshots.",
    ))
    ds_panels.append(bargauge(
        "Dataset Compression Ratio",
        [tgt(f'sort_desc(truenas_dataset_compression_ratio{{instance=~"{I}", dataset=~"$dataset"}})', '{{dataset}}', 'A')],
        12, dy, unit="short", desc="Compression effectiveness per dataset.",
    ))
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
        ],
        0, dy,
        desc="Detailed dataset capacity, encryption, quota, and snapshot info.",
        transforms=[
            outer_join('dataset'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'dataset': 'Dataset', 'Value #A': 'Used', 'Value #B': 'Available', 'Value #C': 'Compression', 'Value #D': 'Encrypted', 'Value #E': 'Quota', 'Value #F': 'Snapshots', 'Value #G': 'Used %'},
                'indexByName': {'Dataset': 0, 'Used %': 1, 'Used': 2, 'Available': 3, 'Quota': 4, 'Snapshots': 5, 'Compression': 6, 'Encrypted': 7},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Used %', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Used %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
            {"matcher": {"id": "byName", "options": "Used"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Available"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Quota"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Encrypted"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        ],
        sort_col='Used %',
    ))
    dy += 10
    panels.append(row("Dataset Deep-Dive", y, collapsed=True, panels=ds_panels))
    y += 1

    # ── COLLAPSED ROW: Exporter & API Diagnostics ───────────────────────
    api_panels = []
    apy = y + 1
    api_panels.extend([
        stat("Exporter Up", f'min(truenas_up{{instance=~"{I}"}})', 0, apy, w=3, mappings=UP_MAP),
        stat("Scrape Time", f'max(truenas_scrape_duration_seconds{{instance=~"{I}"}})', 3, apy, w=3, unit="s",
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 10}, {"color": "red", "value": 30}], graph=True),
        stat("Event Stream", f'max(truenas_event_stream_up{{instance=~"{I}"}})', 6, apy, w=3, mappings=UP_MAP),
        stat("API Success %", f'100 * avg(truenas_api_call_success{{instance=~"{I}", method=~"$method"}})', 9, apy, w=3, unit="percent",
             thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 95}, {"color": "green", "value": 99}], graph=True),
        stat("API Errors", f'sum(truenas_api_call_errors_total{{instance=~"{I}"}})', 12, apy, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 10}], graph=True),
        stat("Coll Errors", f'sum(truenas_collector_errors_total{{instance=~"{I}"}}) or vector(0)', 15, apy, w=3,
             thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}]),
        stat("Boot Changes", f'truenas_system_boot_changes_total{{instance=~"{I}"}}', 18, apy, w=3, desc="Reboot count proxy."),
        stat("FS Paths", f'truenas_filesystem_path_count{{instance=~"{I}"}}', 21, apy, w=3, desc="Filesystem paths scraped."),
    ])
    apy += 4
    api_panels.append(timeseries(
        "Exporter & Event Stream Health",
        [
            tgt(f'truenas_up{{instance=~"{I}"}}', 'Exporter up', 'A'),
            tgt(f'truenas_event_stream_up{{instance=~"{I}"}}', 'Event stream up', 'B'),
            tgt(f'sum(truenas_collector_errors_total{{instance=~"{I}"}}) or vector(0)', 'Collector errors', 'C'),
        ],
        0, apy, desc="Telemetry collection health.",
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
    api_panels.append(state_timeline(
        "API Method Success",
        [tgt(f'truenas_api_call_success{{instance=~"{I}", method=~"$method"}}', '{{method}}', 'A')],
        12, apy, w=12, desc="Per-method success state.", overrides=STATE_OVERRIDES,
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
        {"matcher": {"id": "byName", "options": "Success"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": UP_MAP}]},
    ]
    api_panels.append(table(
        "API Method Detail", api_table_targets, 0, apy,
        desc="Per-method duration, success flag, and errors.",
        overrides=api_overrides, transforms=api_table_transforms, sort_col='Duration s',
    ))
    apy += 10
    panels.append(row("Exporter & API Diagnostics", y, collapsed=True, panels=api_panels))
    y += 1

    # ── Validate grid ───────────────────────────────────────────────────
    for panel in panels:
        gp = panel.get('gridPos', {})
        assert gp.get('x', 0) + gp.get('w', 0) <= 24, f"Panel overflow: {panel.get('title', '')}"

    dashboard = {
        "title": "TrueNAS - Operations Center",
        "uid": "truenas-operations-center",
        "description": (
            "Comprehensive TrueNAS dashboard: system health, CPU, memory, ZFS pools & ARC, "
            "disks, network, services, shares, apps, VMs, boot environments, hardware/IPMI, "
            "alerts, tasks, security, advanced protocols, and exporter diagnostics."
        ),
        "tags": ["truenas", "storage", "operations", "zfs", "exporter"],
        "schemaVersion": 42,
        "version": 1,
        "refresh": "30s",
        "timezone": "browser",
        "graphTooltip": 1,
        "time": {"from": "now-12h", "to": "now"},
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
                {"name": "DS_PROMETHEUS", "type": "datasource", "query": "prometheus", "refresh": 1, "includeAll": False, "options": [], "regex": "", "current": {"text": "Prometheus", "value": "prometheus"}},
                qvar("instance", "Instance", 'label_values(truenas_up, instance)'),
                qvar("pool", "Pool", f'label_values(truenas_pool_size_bytes{{instance=~"{I}"}}, pool)'),
                qvar("dataset", "Dataset", f'label_values(truenas_dataset_used_bytes{{instance=~"{I}"}}, dataset)'),
                qvar("disk", "Disk", f'label_values(truenas_disk_size_bytes{{instance=~"{I}"}}, disk)'),
                qvar("interface", "Interface", f'label_values(truenas_interface_link_up{{instance=~"{I}"}}, interface)'),
                qvar("service", "Service", f'label_values(truenas_service_running{{instance=~"{I}"}}, service)'),
                qvar("app", "App", f'label_values(truenas_app_cpu_percent{{instance=~"{I}"}}, app)'),
                qvar("task_type", "Task Type", f'label_values(truenas_task_state{{instance=~"{I}"}}, task_type)'),
                qvar("level", "Alert Level", f'label_values(truenas_alert_count_by_level{{instance=~"{I}"}}, level)'),
                qvar("method", "API Method", f'label_values(truenas_api_call_duration_seconds{{instance=~"{I}"}}, method)'),
            ]
        },
    }
    return dashboard


if __name__ == "__main__":
    dashboard = build_dashboard()
    OUT.write_text(json.dumps(dashboard, indent=2) + "\n")
