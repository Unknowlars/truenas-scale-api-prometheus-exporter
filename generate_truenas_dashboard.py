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


def build_dashboard():
    panels = []
    y = 0

    panels.append(text_panel(
        "# TrueNAS Operations Center\n\n"
        "Focused on **operations, storage pressure, protocol health, app load, and exporter reliability** for your TrueNAS host.\n\n"
        "> **Tip:** start with `$instance`, then narrow by `$pool`, `$dataset`, `$disk`, `$service`, `$app`, or `$method`. Collapsed detail rows keep the default view fast.",
        0,
        y,
        h=4,
    ))
    y += 4

    panels.append(row("Overview", y))
    y += 1
    overview_stats = [
        stat("Exporter Up", 'min(truenas_up{instance=~"$instance"})', 0, y, desc="Whether the exporter is reachable.", mappings=UP_MAP),
        stat("System Ready", 'min(truenas_system_ready{instance=~"$instance"})', 3, y, desc="Whether middleware reports the system as ready.", mappings=UP_MAP),
        stat("Pools Healthy", 'min(truenas_pool_healthy{instance=~"$instance", pool=~"$pool"})', 6, y, desc="Lowest health state across selected pools.", mappings=UP_MAP),
        stat("Alerts", 'sum(truenas_alert_count_by_level{instance=~"$instance", level=~"$level"})', 9, y, desc="Current alert volume across selected levels.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Update Avail", 'max(truenas_update_available{instance=~"$instance"})', 12, y, desc="Whether TrueNAS reports a pending update.", mappings=BOOL_MAP),
        stat("CPU Used", 'avg(truenas_cpu_usage_percent{instance=~"$instance"})', 15, y, unit="percent", desc="Average CPU utilization.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 70}, {"color": "red", "value": 90}], graph=True),
        stat("RAM Used", '100 * (sum(truenas_memory_physical_used_bytes{instance=~"$instance"}) / clamp_min(sum(truenas_memory_physical_total_bytes{instance=~"$instance"}), 1))', 18, y, unit="percent", desc="Physical memory currently in use.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}], graph=True),
        stat("Scrape Time", 'max(truenas_scrape_duration_seconds{instance=~"$instance"})', 21, y, unit="s", desc="Exporter scrape wall time.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 10}, {"color": "red", "value": 30}], graph=True),
    ]
    panels.extend(overview_stats)
    y += 4
    panels.append(timeseries(
        "CPU Load and Pressure",
        [
            tgt('avg(truenas_cpu_usage_percent{instance=~"$instance"})', 'CPU used %', 'A'),
            tgt('avg(truenas_cpu_iowait_percent{instance=~"$instance"})', 'I/O wait %', 'B'),
            tgt('avg(truenas_host_load_average{instance=~"$instance", window="1m"})', 'Load 1m', 'C'),
            tgt('avg(truenas_host_load_average{instance=~"$instance", window="5m"})', 'Load 5m', 'D'),
        ],
        0,
        y,
        unit="short",
        desc="CPU usage plus load average helps separate pure compute pressure from queueing and I/O wait.",
    ))
    panels.append(timeseries(
        "Memory and ARC Composition",
        [
            tgt('sum(truenas_memory_physical_used_bytes{instance=~"$instance"})', 'RAM used', 'A'),
            tgt('sum(truenas_memory_physical_available_bytes{instance=~"$instance"})', 'RAM available', 'B'),
            tgt('sum(truenas_zfs_arc_size_bytes{instance=~"$instance"})', 'ARC size', 'C'),
            tgt('sum(truenas_memory_swap_used_bytes{instance=~"$instance"})', 'Swap used', 'D'),
        ],
        12,
        y,
        unit="bytes",
        desc="Correlates memory pressure with ZFS ARC growth and swap usage.",
        stacked=False,
    ))
    y += 8
    panels.append(timeseries(
        "Network Throughput",
        [
            tgt('sum(truenas_network_rx_bytes_per_second{instance=~"$instance", interface=~"$interface"})', 'RX total', 'A'),
            tgt('sum(truenas_network_tx_bytes_per_second{instance=~"$instance", interface=~"$interface"})', 'TX total', 'B'),
        ],
        0,
        y,
        unit="Bps",
        desc="Aggregate interface throughput for the selected interfaces.",
    ))
    panels.append(state_timeline(
        "Interface Link State",
        [tgt('truenas_interface_link_up{instance=~"$instance", interface=~"$interface"}', '{{interface}}', 'A')],
        12,
        y,
        w=12,
        desc="Shows flapping or maintenance events on selected network interfaces.",
        overrides=STATE_OVERRIDES,
    ))
    y += 8

    panels.append(row("Storage and ZFS", y))
    y += 1
    storage_stats = [
        stat("Pool Count", 'count(truenas_pool_size_bytes{instance=~"$instance", pool=~"$pool"})', 0, y, w=4, desc="Selected pool count."),
        stat("Dataset Count", 'count(truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"})', 4, y, w=4, desc="Selected dataset count."),
        stat("Snapshots", 'sum(truenas_snapshot_count{instance=~"$instance"})', 8, y, w=4, desc="Total snapshots across the appliance."),
        stat("Pool Used %", '100 * (sum(truenas_pool_allocated_bytes{instance=~"$instance", pool=~"$pool"}) / clamp_min(sum(truenas_pool_size_bytes{instance=~"$instance", pool=~"$pool"}), 1))', 12, y, w=4, unit="percent", desc="Aggregate used capacity across selected pools.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}], graph=True),
        stat("ARC Hit Ratio", '100 * avg(truenas_zfs_arc_hit_ratio{instance=~"$instance"})', 16, y, w=4, unit="percent", desc="Read cache effectiveness.", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 70}, {"color": "green", "value": 90}], graph=True),
        stat("Boot Pool OK", 'min(truenas_boot_pool_healthy{instance=~"$instance"})', 20, y, w=4, desc="Boot pool health state.", mappings=UP_MAP),
    ]
    panels.extend(storage_stats)
    y += 4
    panels.append(bargauge(
        "Pool Utilization",
        [tgt('100 * truenas_pool_allocated_bytes{instance=~"$instance", pool=~"$pool"} / clamp_min(truenas_pool_size_bytes{instance=~"$instance", pool=~"$pool"}, 1)', '{{pool}}', 'A')],
        0,
        y,
        unit="percent",
        desc="Fast ranking of which pools are consuming the most capacity.",
        max_value=100,
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}],
    ))
    panels.append(bargauge(
        "Top Dataset Utilization",
        [tgt('topk(10, 100 * truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"} / clamp_min(truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"} + truenas_dataset_available_bytes{instance=~"$instance", dataset=~"$dataset"}, 1))', '{{dataset}}', 'A')],
        12,
        y,
        unit="percent",
        desc="Highlights the datasets closest to filling their available space.",
        max_value=100,
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}],
    ))
    y += 8
    panels.append(timeseries(
        "Pool Capacity Trends",
        [
            tgt('truenas_pool_allocated_bytes{instance=~"$instance", pool=~"$pool"}', '{{pool}} allocated', 'A'),
            tgt('truenas_pool_free_bytes{instance=~"$instance", pool=~"$pool"}', '{{pool}} free', 'B'),
        ],
        0,
        y,
        unit="bytes",
        desc="Pool allocated and free space over time for capacity planning.",
    ))
    panels.append(timeseries(
        "ARC and L2ARC Effectiveness",
        [
            tgt('100 * truenas_zfs_arc_hit_ratio{instance=~"$instance"}', 'ARC hit %', 'A'),
            tgt('100 * truenas_zfs_l2arc_hit_ratio{instance=~"$instance"}', 'L2ARC hit %', 'B'),
            tgt('truenas_zfs_l2arc_read_bytes_per_second{instance=~"$instance"}', 'L2ARC read', 'C'),
            tgt('truenas_zfs_l2arc_write_bytes_per_second{instance=~"$instance"}', 'L2ARC write', 'D'),
        ],
        12,
        y,
        unit="short",
        desc="Shows whether cache tiers are reducing disk reads or simply churning.",
    ))
    y += 8
    panels.append(gauge(
        "Boot Pool Scan",
        'max(truenas_boot_pool_scan_percent{instance=~"$instance"}) / 100',
        0,
        y,
        unit="percentunit",
        desc="Current boot pool resilver/scrub progress if a scan is active.",
        min_value=0,
        max_value=1,
    ))
    panels.append(histogram(
        "Dataset Size Distribution",
        [tgt('truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"}', '{{dataset}}', 'A')],
        6,
        y,
        unit="bytes",
        desc="Distribution shape of current dataset sizes to spot very large outliers.",
    ))
    panels.append(state_timeline(
        "Pool Health Timeline",
        [tgt('truenas_pool_healthy{instance=~"$instance", pool=~"$pool"}', '{{pool}}', 'A')],
        18,
        y,
        w=6,
        desc="Historical pool up/down state.",
        overrides=STATE_OVERRIDES,
    ))
    y += 8
    pool_table_targets = [
        table_target('max by (pool) (truenas_pool_size_bytes{instance=~"$instance", pool=~"$pool"})', 'A'),
        table_target('max by (pool) (truenas_pool_allocated_bytes{instance=~"$instance", pool=~"$pool"})', 'B'),
        table_target('max by (pool) (truenas_pool_free_bytes{instance=~"$instance", pool=~"$pool"})', 'C'),
        table_target('max by (pool) (truenas_pool_fragmentation_percent{instance=~"$instance", pool=~"$pool"})', 'D'),
        table_target('max by (pool) (truenas_pool_healthy{instance=~"$instance", pool=~"$pool"})', 'E'),
        table_target('100 * max by (pool) (truenas_pool_allocated_bytes{instance=~"$instance", pool=~"$pool"}) / clamp_min(max by (pool) (truenas_pool_size_bytes{instance=~"$instance", pool=~"$pool"}), 1)', 'F'),
    ]
    pool_table_transforms = [
        outer_join('pool'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {
                'pool': 'Pool',
                'Value #A': 'Size',
                'Value #B': 'Allocated',
                'Value #C': 'Free',
                'Value #D': 'Frag %',
                'Value #E': 'Healthy',
                'Value #F': 'Used %',
            },
            'indexByName': {'Pool': 0, 'Used %': 1, 'Allocated': 2, 'Free': 3, 'Size': 4, 'Frag %': 5, 'Healthy': 6},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Used %', 'desc': True}]}),
    ]
    pool_overrides = [
        {"matcher": {"id": "byName", "options": "Used %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
        {"matcher": {"id": "byName", "options": "Healthy"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": UP_MAP}]},
        {"matcher": {"id": "byName", "options": "Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Allocated"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Free"}, "properties": [{"id": "unit", "value": "bytes"}]},
    ]
    panels.append(table(
        "Pool Inventory",
        pool_table_targets,
        0,
        y,
        h=10,
        desc="Current pool inventory with fill ratio, fragmentation, and health in one sortable table.",
        overrides=pool_overrides,
        transforms=pool_table_transforms,
        sort_col='Used %',
    ))
    y += 10

    panels.append(row("Disk and Network Detail", y))
    y += 1
    disk_stats = [
        stat("Disk Count", 'count(truenas_disk_size_bytes{instance=~"$instance", disk=~"$disk", disk!="total"})', 0, y, w=4, desc="Selected disk count."),
        stat("Hottest Disk", 'max(truenas_disk_temperature_celsius{instance=~"$instance", disk=~"$disk", disk!="total"})', 4, y, w=4, unit="celsius", desc="Highest reported disk temperature.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 40}, {"color": "red", "value": 50}], graph=True),
        stat("Avg Busy", 'avg(truenas_disk_busy_percent{instance=~"$instance", disk=~"$disk", disk!="total"})', 8, y, w=4, unit="percent", desc="Average disk busy percentage.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 60}, {"color": "red", "value": 85}], graph=True),
        stat("Iface Count", 'count(truenas_interface_link_up{instance=~"$instance", interface=~"$interface"})', 12, y, w=4, desc="Selected interface count."),
        stat("Gateway Reach", 'min(truenas_network_gateway_reachable{instance=~"$instance"})', 16, y, w=4, desc="Whether the configured gateway is reachable.", mappings=UP_MAP),
        stat("Pending Net Chg", 'max(truenas_interface_has_pending_changes{instance=~"$instance"})', 20, y, w=4, desc="Whether unapplied network changes are waiting.", mappings=BOOL_MAP),
    ]
    panels.extend(disk_stats)
    y += 4
    panels.append(timeseries(
        "Disk Throughput by Device",
        [
            tgt('topk(8, truenas_disk_read_bytes_per_second{instance=~"$instance", disk=~"$disk", disk!="total"})', 'read {{disk}}', 'A'),
            tgt('topk(8, truenas_disk_write_bytes_per_second{instance=~"$instance", disk=~"$disk", disk!="total"})', 'write {{disk}}', 'B'),
        ],
        0,
        y,
        unit="Bps",
        desc="Read/write throughput for the busiest selected devices.",
    ))
    panels.append(timeseries(
        "Disk Busy and Temperature",
        [
            tgt('topk(8, truenas_disk_busy_percent{instance=~"$instance", disk=~"$disk", disk!="total"})', 'busy {{disk}}', 'A'),
            tgt('topk(8, truenas_disk_temperature_celsius{instance=~"$instance", disk=~"$disk", disk!="total"})', 'temp {{disk}}', 'B'),
        ],
        12,
        y,
        unit="short",
        desc="Pairs performance saturation with thermals to expose unhealthy disks.",
    ))
    y += 8
    panels.append(bargauge(
        "Disk Temperatures",
        [tgt('truenas_disk_temperature_celsius{instance=~"$instance", disk=~"$disk", disk!="total"}', '{{disk}}', 'A')],
        0,
        y,
        unit="celsius",
        desc="Temperature ranking of disks.",
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
        [tgt('truenas_disk_size_bytes{instance=~"$instance", disk=~"$disk", disk!="total"}', '{{disk}}', 'A')],
        12,
        y,
        unit="bytes",
        desc="Disk capacity comparison by device.",
        transforms=disk_bar_transforms,
    ))
    y += 8
    disk_table_targets = [
        table_target('max by (disk) (truenas_disk_size_bytes{instance=~"$instance", disk=~"$disk", disk!="total"})', 'A'),
        table_target('max by (disk) (truenas_disk_busy_percent{instance=~"$instance", disk=~"$disk", disk!="total"})', 'B'),
        table_target('max by (disk) (truenas_disk_temperature_celsius{instance=~"$instance", disk=~"$disk", disk!="total"})', 'C'),
        table_target('max by (disk) (truenas_disk_read_bytes_per_second{instance=~"$instance", disk=~"$disk", disk!="total"})', 'D'),
        table_target('max by (disk) (truenas_disk_write_bytes_per_second{instance=~"$instance", disk=~"$disk", disk!="total"})', 'E'),
    ]
    disk_table_transforms = [
        outer_join('disk'),
        tf('organize', {
            'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
            'renameByName': {
                'disk': 'Disk',
                'Value #A': 'Size',
                'Value #B': 'Busy %',
                'Value #C': 'Temp C',
                'Value #D': 'Read B/s',
                'Value #E': 'Write B/s',
            },
            'indexByName': {'Disk': 0, 'Busy %': 1, 'Temp C': 2, 'Read B/s': 3, 'Write B/s': 4, 'Size': 5},
        }),
        tf('sortBy', {'fields': [{'displayName': 'Busy %', 'desc': True}]}),
    ]
    disk_overrides = [
        {"matcher": {"id": "byName", "options": "Busy %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 60}, {"color": "red", "value": 85}]}}]},
        {"matcher": {"id": "byName", "options": "Temp C"}, "properties": [{"id": "unit", "value": "celsius"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 40}, {"color": "red", "value": 50}]}}]},
        {"matcher": {"id": "byName", "options": "Size"}, "properties": [{"id": "unit", "value": "bytes"}]},
        {"matcher": {"id": "byName", "options": "Read B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
        {"matcher": {"id": "byName", "options": "Write B/s"}, "properties": [{"id": "unit", "value": "Bps"}]},
    ]
    panels.append(table(
        "Disk Inventory",
        disk_table_targets,
        0,
        y,
        desc="Per-disk health, utilization, and throughput in one filterable view.",
        overrides=disk_overrides,
        transforms=disk_table_transforms,
        sort_col='Busy %',
    ))
    y += 10

    panels.append(row("Services and Protocols", y))
    y += 1
    service_stats = [
        stat("Services", 'count(truenas_service_running{instance=~"$instance", service=~"$service"})', 0, y, desc="Selected services."),
        stat("SMB Shares", 'sum(truenas_smb_share_count{instance=~"$instance"})', 3, y, desc="Configured SMB shares."),
        stat("NFS Shares", 'sum(truenas_nfs_share_count{instance=~"$instance"})', 6, y, desc="Configured NFS shares."),
        stat("iSCSI Targets", 'sum(truenas_iscsi_target_count{instance=~"$instance"})', 9, y, desc="Configured iSCSI targets."),
        stat("SMB Sessions", 'sum(truenas_smb_session_count{instance=~"$instance"})', 12, y, desc="Current SMB sessions.", graph=True),
        stat("SMB Open Files", 'sum(truenas_smb_open_file_count{instance=~"$instance"})', 15, y, desc="Current open SMB files.", graph=True),
        stat("NFS Clients", 'sum(truenas_nfs_client_count{instance=~"$instance"})', 18, y, desc="Active NFS clients.", graph=True),
        stat("iSCSI Clients", 'sum(truenas_iscsi_client_count{instance=~"$instance"})', 21, y, desc="Active iSCSI clients.", graph=True),
    ]
    panels.extend(service_stats)
    y += 4
    panels.append(state_timeline(
        "Service Runtime State",
        [tgt('truenas_service_running{instance=~"$instance", service=~"$service"}', '{{service}}', 'A')],
        0,
        y,
        w=12,
        desc="Shows when selected services were running or stopped.",
        overrides=STATE_OVERRIDES,
    ))
    panels.append(piechart(
        "Protocol Activity Mix",
        [
            tgt('sum(truenas_smb_connection_count{instance=~"$instance"})', 'SMB connections', 'A'),
            tgt('sum(truenas_nfs_client_count{instance=~"$instance"})', 'NFS clients', 'B'),
            tgt('sum(truenas_iscsi_client_count{instance=~"$instance"})', 'iSCSI clients', 'C'),
            tgt('sum(truenas_nvmet_session_count{instance=~"$instance"})', 'NVMe-oF sessions', 'D'),
        ],
        12,
        y,
        w=12,
        desc="Relative protocol activity from the currently exposed services.",
    ))
    y += 8
    panels.append(timeseries(
        "Protocol Throughput and Ops",
        [
            tgt('sum(truenas_nfs_server_ops_per_second{instance=~"$instance"})', 'NFS ops/s', 'A'),
            tgt('sum(truenas_smb_connection_count{instance=~"$instance"})', 'SMB connections', 'B'),
            tgt('sum(truenas_iscsi_client_count{instance=~"$instance"})', 'iSCSI clients', 'C'),
        ],
        0,
        y,
        unit="short",
        desc="Tracks client and protocol activity over time to catch contention or drop-offs.",
    ))
    service_bar_transforms = [
        tf('labelsToFields', {'mode': 'columns', 'source': 'labels'}),
        tf('reduce', {'reducers': ['lastNotNull']}),
        tf('organize', {'excludeByName': {'Time': True}}),
    ]
    panels.append(barchart(
        "Service Enablement",
        [tgt('truenas_service_enabled{instance=~"$instance", service=~"$service"}', '{{service}}', 'A')],
        12,
        y,
        unit="short",
        desc="Which services are configured to start automatically.",
        transforms=service_bar_transforms,
    ))
    y += 8
    service_table_targets = [
        table_target('max by (service) (truenas_service_running{instance=~"$instance", service=~"$service"})', 'A'),
        table_target('max by (service) (truenas_service_enabled{instance=~"$instance", service=~"$service"})', 'B'),
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
        "Service Inventory",
        service_table_targets,
        0,
        y,
        desc="Pairs current runtime state with boot enablement.",
        overrides=service_overrides,
        transforms=service_table_transforms,
        sort_col='Service',
        sort_desc=False,
    ))
    y += 10

    panels.append(row("Apps and Virtualization", y))
    y += 1
    app_stats = [
        stat("Apps", 'sum(truenas_app_count{instance=~"$instance"})', 0, y, w=4, desc="Installed apps."),
        stat("Docker Images", 'sum(truenas_docker_image_count{instance=~"$instance"})', 4, y, w=4, desc="Image count."),
        stat("Docker Nets", 'sum(truenas_docker_network_count{instance=~"$instance"})', 8, y, w=4, desc="Docker network count."),
        stat("Docker Running", 'max(truenas_docker_status{instance=~"$instance"})', 12, y, w=4, desc="Whether Docker service is running.", mappings=UP_MAP),
        stat("VM Count", 'sum(truenas_vm_count{instance=~"$instance"})', 16, y, w=4, desc="Configured virtual machines."),
        stat("Virt Instances", 'sum(truenas_virt_instance_count{instance=~"$instance"})', 20, y, w=4, desc="Incus/LXD style instances reported by TrueNAS."),
    ]
    panels.extend(app_stats)
    y += 4
    panels.append(bargauge(
        "Top Apps by CPU",
        [tgt('topk(10, truenas_app_cpu_percent{instance=~"$instance", app=~"$app"})', '{{app}}', 'A')],
        0,
        y,
        unit="percent",
        desc="Which apps currently consume the most CPU.",
        max_value=100,
        thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 50}, {"color": "red", "value": 80}],
    ))
    panels.append(bargauge(
        "Top Apps by Memory",
        [tgt('topk(10, truenas_app_memory_bytes{instance=~"$instance", app=~"$app"})', '{{app}}', 'A')],
        12,
        y,
        unit="bytes",
        desc="Top memory consumers among deployed apps.",
    ))
    y += 8
    panels.append(timeseries(
        "App I/O",
        [
            tgt('topk(8, truenas_app_blkio_read_bytes{instance=~"$instance", app=~"$app"})', 'read {{app}}', 'A'),
            tgt('topk(8, truenas_app_blkio_write_bytes{instance=~"$instance", app=~"$app"})', 'write {{app}}', 'B'),
        ],
        0,
        y,
        unit="bytes",
        desc="Read/write volume by app; useful for spotting noisy containers.",
    ))
    panels.append(timeseries(
        "App Network",
        [
            tgt('topk(8, truenas_app_net_rx_bytes_per_second{instance=~"$instance", app=~"$app"})', 'rx {{app}}', 'A'),
            tgt('topk(8, truenas_app_net_tx_bytes_per_second{instance=~"$instance", app=~"$app"})', 'tx {{app}}', 'B'),
        ],
        12,
        y,
        unit="Bps",
        desc="Ingress and egress rates by app.",
    ))
    y += 8
    panels.append(piechart(
        "Platform Capacity Mix",
        [
            tgt('sum(truenas_app_count{instance=~"$instance"})', 'Apps', 'A'),
            tgt('sum(truenas_vm_count{instance=~"$instance"})', 'VMs', 'B'),
            tgt('sum(truenas_virt_volume_count{instance=~"$instance"})', 'Virt volumes', 'C'),
            tgt('sum(truenas_docker_network_count{instance=~"$instance"})', 'Docker networks', 'D'),
        ],
        0,
        y,
        w=8,
        desc="A quick sense of how the host is partitioned across app and virtualization primitives.",
    ))
    panels.append(timeseries(
        "Virtualization Memory and Limits",
        [
            tgt('sum(truenas_vm_available_memory_bytes{instance=~"$instance"})', 'VM available memory', 'A'),
            tgt('sum(truenas_vm_vmemory_in_use_mb{instance=~"$instance"}) * 1024 * 1024', 'VM memory in use', 'B'),
            tgt('sum(truenas_vm_maximum_supported_vcpus{instance=~"$instance"})', 'Max supported vCPUs', 'C'),
        ],
        8,
        y,
        w=16,
        unit="short",
        desc="Capacity indicators for the virtualization subsystem.",
    ))
    y += 8
    app_table_targets = [
        table_target('max by (app) (truenas_app_cpu_percent{instance=~"$instance", app=~"$app"})', 'A'),
        table_target('max by (app) (truenas_app_memory_bytes{instance=~"$instance", app=~"$app"})', 'B'),
        table_target('max by (app) (truenas_app_net_rx_bytes_per_second{instance=~"$instance", app=~"$app"})', 'C'),
        table_target('max by (app) (truenas_app_net_tx_bytes_per_second{instance=~"$instance", app=~"$app"})', 'D'),
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
        "App Inventory",
        app_table_targets,
        0,
        y,
        desc="Current app resource footprint.",
        overrides=app_overrides,
        transforms=app_table_transforms,
        sort_col='Memory',
    ))
    y += 10

    panels.append(row("Alerts, Tasks, and API", y))
    y += 1
    alert_stats = [
        stat("Total Alerts", 'sum(truenas_alert_count_by_level{instance=~"$instance", level=~"$level"})', 0, y, desc="All current alerts.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Critical", 'sum(truenas_alert_count_by_level{instance=~"$instance", level="CRITICAL"})', 3, y, desc="Critical alerts only.", thresholds=[{"color": "green", "value": 0}, {"color": "red", "value": 1}], graph=True),
        stat("Warning", 'sum(truenas_alert_count_by_level{instance=~"$instance", level="WARNING"})', 6, y, desc="Warning alerts only.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 5}], graph=True),
        stat("Tasks", 'sum(truenas_task_count{instance=~"$instance"})', 9, y, desc="Scheduled task count."),
        stat("Tasks Enabled", 'sum(truenas_task_enabled{instance=~"$instance"})', 12, y, desc="Enabled scheduled tasks."),
        stat("Cloud Backups", 'sum(truenas_cloud_backup_task_count{instance=~"$instance"})', 15, y, desc="Cloud backup task count."),
        stat("API Success %", '100 * avg(truenas_api_call_success{instance=~"$instance", method=~"$method"})', 18, y, unit="percent", desc="Current success ratio across selected API methods.", thresholds=[{"color": "red", "value": 0}, {"color": "yellow", "value": 95}, {"color": "green", "value": 99}], graph=True),
        stat("API Errors", 'sum(truenas_api_call_errors_total{instance=~"$instance"})', 21, y, desc="Cumulative API call errors emitted by the exporter.", thresholds=[{"color": "green", "value": 0}, {"color": "yellow", "value": 1}, {"color": "red", "value": 10}], graph=True),
    ]
    panels.extend(alert_stats)
    y += 4
    panels.append(piechart(
        "Alert Level Distribution",
        [tgt('truenas_alert_count_by_level{instance=~"$instance", level=~"$level"}', '{{level}}', 'A')],
        0,
        y,
        w=8,
        desc="Current mix of alert severities.",
    ))
    task_type_transforms = [
        tf('labelsToFields', {'mode': 'columns', 'source': 'labels'}),
        tf('reduce', {'reducers': ['lastNotNull']}),
        tf('organize', {'excludeByName': {'Time': True}}),
    ]
    panels.append(barchart(
        "Tasks by Type",
        [tgt('count by (task_type) (truenas_task_state{instance=~"$instance", task_type=~"$task_type"})', '{{task_type}}', 'A')],
        8,
        y,
        w=8,
        desc="Breaks scheduled work down by task_type label.",
        transforms=task_type_transforms,
    ))
    panels.append(histogram(
        "API Duration Distribution",
        [tgt('truenas_api_call_duration_seconds{instance=~"$instance", method=~"$method"}', '{{method}}', 'A')],
        16,
        y,
        w=8,
        unit="s",
        desc="Shows spread of current API method durations to surface expensive calls.",
    ))
    y += 8
    panels.append(timeseries(
        "API Method Duration",
        [tgt('topk(12, truenas_api_call_duration_seconds{instance=~"$instance", method=~"$method"})', '{{method}}', 'A')],
        0,
        y,
        unit="s",
        desc="Tracks the slowest middleware methods observed by the exporter.",
    ))
    panels.append(state_timeline(
        "API Method Success",
        [tgt('truenas_api_call_success{instance=~"$instance", method=~"$method"}', '{{method}}', 'A')],
        12,
        y,
        w=12,
        desc="Flips red when a specific method stops succeeding.",
        overrides=STATE_OVERRIDES,
    ))
    y += 8
    api_table_targets = [
        table_target('max by (method) (truenas_api_call_duration_seconds{instance=~"$instance", method=~"$method"})', 'A'),
        table_target('max by (method) (truenas_api_call_success{instance=~"$instance", method=~"$method"})', 'B'),
        table_target('sum by (method) (truenas_api_call_errors_total{instance=~"$instance", method=~"$method"})', 'C'),
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
    panels.append(table(
        "API Method Detail",
        api_table_targets,
        0,
        y,
        desc="Per-method duration, success flag, and cumulative error count.",
        overrides=api_overrides,
        transforms=api_table_transforms,
        sort_col='Duration s',
    ))
    y += 10

    panels.append(row("Security and Platform", y))
    y += 1
    security_stats = [
        stat("2FA", 'max(truenas_2fa_enabled{instance=~"$instance"})', 0, y, desc="Two-factor auth enabled.", mappings=BOOL_MAP),
        stat("SSH", 'max(truenas_ssh_enabled{instance=~"$instance"})', 3, y, desc="SSH service enabled.", mappings=BOOL_MAP),
        stat("SSH Passwd", 'max(truenas_ssh_password_auth{instance=~"$instance"})', 6, y, desc="Password auth enabled for SSH.", mappings=BOOL_MAP),
        stat("FTP", 'max(truenas_ftp_enabled{instance=~"$instance"})', 9, y, desc="FTP enabled.", mappings=BOOL_MAP),
        stat("SNMP", 'max(truenas_snmp_enabled{instance=~"$instance"})', 12, y, desc="SNMP enabled.", mappings=BOOL_MAP),
        stat("FIPS", 'max(truenas_fips_enabled{instance=~"$instance"})', 15, y, desc="FIPS mode enabled.", mappings=BOOL_MAP),
        stat("KMIP", 'max(truenas_kmip_enabled{instance=~"$instance"})', 18, y, desc="KMIP configured and enabled.", mappings=BOOL_MAP),
        stat("UPS", 'max(truenas_ups_configured{instance=~"$instance"})', 21, y, desc="UPS integration configured.", mappings=BOOL_MAP),
    ]
    panels.extend(security_stats)
    y += 4
    panels.append(piechart(
        "Security Feature Mix",
        [
            tgt('sum(truenas_2fa_enabled{instance=~"$instance"})', '2FA', 'A'),
            tgt('sum(truenas_fips_enabled{instance=~"$instance"})', 'FIPS', 'B'),
            tgt('sum(truenas_kmip_enabled{instance=~"$instance"})', 'KMIP', 'C'),
            tgt('sum(truenas_ssh_enabled{instance=~"$instance"})', 'SSH', 'D'),
            tgt('sum(truenas_snmp_enabled{instance=~"$instance"})', 'SNMP', 'E'),
        ],
        0,
        y,
        desc="Enabled security-related capabilities at a glance.",
    ))
    panels.append(timeseries(
        "Exporter and Event Stream Health",
        [
            tgt('truenas_up{instance=~"$instance"}', 'Exporter up', 'A'),
            tgt('truenas_event_stream_up{instance=~"$instance"}', 'Event stream up', 'B'),
            tgt('truenas_last_scrape_timestamp_seconds{instance=~"$instance"}', 'Last scrape ts', 'C'),
        ],
        8,
        y,
        w=16,
        unit="short",
        desc="Signals whether telemetry collection is healthy and current.",
    ))
    y += 8
    panels.append(table(
        "Security and Identity Counts",
        [
            table_target(
                'label_replace(max(truenas_local_user_count{instance=~"$instance"}), "category", "Local Users", "__name__", ".*") '
                'or label_replace(max(truenas_local_group_count{instance=~"$instance"}), "category", "Local Groups", "__name__", ".*") '
                'or label_replace(max(truenas_certificate_count{instance=~"$instance"}), "category", "Certificates", "__name__", ".*") '
                'or label_replace(max(truenas_privilege_count{instance=~"$instance"}), "category", "Privileges", "__name__", ".*") '
                'or label_replace(max(truenas_keychain_credential_count{instance=~"$instance"}), "category", "Keychain Creds", "__name__", ".*")',
                'A'
            ),
        ],
        0,
        y,
        desc="Identity and trust object counts exposed by the appliance.",
        transforms=[
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'category': 'Category', 'Value': 'Count'},
                'indexByName': {'Category': 0, 'Count': 1},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Count', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Count"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}]}}]},
        ],
        sort_col='Count',
    ))
    y += 10

    detail_children = []
    detail_y = y + 1
    detail_children.append(table(
        "Task State Detail",
        [
            table_target('max by (name, task_type, state) (truenas_task_state{instance=~"$instance", task_type=~"$task_type"} == 1)', 'A'),
            table_target('max by (name) (truenas_task_enabled{instance=~"$instance", task_type=~"$task_type"})', 'B'),
            table_target('time() - max by (name) (truenas_task_last_run_timestamp_seconds{instance=~"$instance", task_type=~"$task_type"})', 'C'),
        ],
        0,
        detail_y,
        desc="Raw task status rows from the exporter.",
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
        sort_col='Task',
        sort_desc=False,
    ))
    detail_y += 10
    detail_children.append(table(
        "Dataset Capacity Detail",
        [
            table_target('max by (dataset) (truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"})', 'A'),
            table_target('max by (dataset) (truenas_dataset_available_bytes{instance=~"$instance", dataset=~"$dataset"})', 'B'),
            table_target('max by (dataset) (truenas_dataset_compression_ratio{instance=~"$instance", dataset=~"$dataset"})', 'C'),
            table_target('max by (dataset) (truenas_dataset_encrypted{instance=~"$instance", dataset=~"$dataset"})', 'D'),
            table_target('100 * max by (dataset) (truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"}) / clamp_min(max by (dataset) (truenas_dataset_used_bytes{instance=~"$instance", dataset=~"$dataset"}) + max by (dataset) (truenas_dataset_available_bytes{instance=~"$instance", dataset=~"$dataset"}), 1)', 'E'),
        ],
        0,
        detail_y,
        desc="Deeper dataset capacity and encryption detail.",
        transforms=[
            outer_join('dataset'),
            tf('organize', {
                'excludeByName': {'Time': True, '__name__': True, 'instance': True, 'job': True},
                'renameByName': {'dataset': 'Dataset', 'Value #A': 'Used', 'Value #B': 'Available', 'Value #C': 'Compression', 'Value #D': 'Encrypted', 'Value #E': 'Used %'},
                'indexByName': {'Dataset': 0, 'Used %': 1, 'Used': 2, 'Available': 3, 'Compression': 4, 'Encrypted': 5},
            }),
            tf('sortBy', {'fields': [{'displayName': 'Used %', 'desc': True}]}),
        ],
        overrides=[
            {"matcher": {"id": "byName", "options": "Used %"}, "properties": [{"id": "unit", "value": "percent"}, {"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "thresholds", "value": {"mode": "absolute", "steps": [{"color": "green", "value": 0}, {"color": "yellow", "value": 75}, {"color": "red", "value": 90}]}}]},
            {"matcher": {"id": "byName", "options": "Used"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Available"}, "properties": [{"id": "unit", "value": "bytes"}]},
            {"matcher": {"id": "byName", "options": "Encrypted"}, "properties": [{"id": "custom.cellOptions", "value": {"type": "color-background"}}, {"id": "mappings", "value": BOOL_MAP}]},
        ],
        sort_col='Used %',
    ))
    detail_y += 10
    panels.append(row("Collapsed Detail Tables", y, collapsed=True, panels=detail_children))
    y += 1

    for panel in panels:
        gp = panel.get('gridPos', {})
        assert gp.get('x', 0) + gp.get('w', 0) <= 24, f"Panel overflow: {panel.get('title', '')}"

    dashboard = {
        "title": "TrueNAS - Operations Center",
        "uid": "truenas-operations-center",
        "description": "Operational dashboard for a TrueNAS host: health, storage pressure, protocol activity, app load, security posture, and exporter/API behavior.",
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
        "links": [
            {"title": "TrueNAS UI", "url": "http://192.168.0.247/", "icon": "external link", "type": "link", "targetBlank": True},
            {"title": "Prometheus", "url": "http://192.168.0.247:9090/graph", "icon": "external link", "type": "link", "targetBlank": True},
            {"title": "Exporter Metrics", "url": "http://192.168.0.247:9108/metrics", "icon": "external link", "type": "link", "targetBlank": True},
        ],
        "panels": panels,
        "templating": {
            "list": [
                {"name": "DS_PROMETHEUS", "type": "datasource", "query": "prometheus", "refresh": 1, "includeAll": False, "options": [], "regex": "", "current": {"text": "Prometheus", "value": "prometheus"}},
                qvar("instance", "Instance", 'label_values(truenas_up, instance)'),
                qvar("pool", "Pool", 'label_values(truenas_pool_size_bytes{instance=~"$instance"}, pool)'),
                qvar("dataset", "Dataset", 'label_values(truenas_dataset_used_bytes{instance=~"$instance"}, dataset)'),
                qvar("disk", "Disk", 'label_values(truenas_disk_size_bytes{instance=~"$instance"}, disk)'),
                qvar("interface", "Interface", 'label_values(truenas_interface_link_up{instance=~"$instance"}, interface)'),
                qvar("service", "Service", 'label_values(truenas_service_running{instance=~"$instance"}, service)'),
                qvar("app", "App", 'label_values(truenas_app_cpu_percent{instance=~"$instance"}, app)'),
                qvar("task_type", "Task Type", 'label_values(truenas_task_state{instance=~"$instance"}, task_type)'),
                qvar("level", "Alert Level", 'label_values(truenas_alert_count_by_level{instance=~"$instance"}, level)'),
                qvar("method", "API Method", 'label_values(truenas_api_call_duration_seconds{instance=~"$instance"}, method)'),
            ]
        },
    }
    return dashboard


if __name__ == "__main__":
    dashboard = build_dashboard()
    OUT.write_text(json.dumps(dashboard, indent=2) + "\n")
    print(f"Wrote {OUT} with {len(dashboard['panels'])} top-level panels")
