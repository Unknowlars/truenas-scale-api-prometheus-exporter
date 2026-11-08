#!/usr/bin/env python3
"""Validate dashboard structure and exporter metric references."""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Iterable
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DASHBOARD = REPO_ROOT / "grafana-dashboard" / "operations-center-dashboard.json"
CONTRACT = REPO_ROOT / "docs" / "metrics-contract.json"
METRIC_RE = re.compile(r"\btruenas_[a-zA-Z_:][a-zA-Z0-9_:]*\b")

# Compatibility-owned metrics that intentionally have no safe, documented
# TrueNAS SCALE 25.10.2 producer. They remain in the public metric contract so
# existing consumers do not see a removal, but dashboards must not query them.
UNAVAILABLE_DASHBOARD_METRICS = frozenset(
    {
        "truenas_consolemenu_enabled",
        "truenas_dataset_referenced_bytes",
        "truenas_cloud_backup_task_state",
        "truenas_directoryservices_account_cache_enabled",
        "truenas_directoryservices_dns_updates_enabled",
        "truenas_directoryservices_kerberos_configured",
        "truenas_directoryservices_timeout_seconds",
        "truenas_disk_smart_enabled",
        "truenas_disk_temperature_alert_count",
        "truenas_fc_port_online",
        "truenas_fc_port_speed_gbit",
        "truenas_kmip_enabled",
        "truenas_mail_configured",
        "truenas_memory_physical_buffers_bytes",
        "truenas_memory_physical_cached_bytes",
        "truenas_memory_physical_free_bytes",
        "truenas_memory_swap_free_bytes",
        "truenas_memory_swap_total_bytes",
        "truenas_memory_swap_used_bytes",
        "truenas_network_httpproxy_configured",
        "truenas_nfs_server_ops_per_second",
        "truenas_ntp_server_active_count",
        "truenas_ntp_server_reachable_count",
        "truenas_pool_scrub_last_run_timestamp_seconds",
        "truenas_pool_scrub_task_state",
        "truenas_pool_vdev_checksum_errors",
        "truenas_pool_vdev_read_errors",
        "truenas_pool_vdev_write_errors",
        "truenas_smart_test_last_result",
        "truenas_smart_test_last_timestamp_seconds",
        "truenas_serialconsole_enabled",
        "truenas_ssh_password_auth",
        "truenas_support_config_enabled",
        "truenas_task_last_run_timestamp_seconds",
        "truenas_task_state",
        "truenas_system_security_password_warn_age_days",
        "truenas_tn_connect_enabled",
        "truenas_tn_connect_status",
        "truenas_truecommand_status",
        "truenas_ups_configured",
        "truenas_ups_status",
        "truenas_virt_global_state",
        "truenas_virt_volume_size_bytes",
        "truenas_zfs_arc_hit_ratio",
        "truenas_zfs_arc_hits_per_second",
        "truenas_zfs_arc_max_size_bytes",
        "truenas_zfs_arc_min_size_bytes",
        "truenas_zfs_arc_misses_per_second",
    }
)

DEPRECATED_DASHBOARD_METRIC_REPLACEMENTS = {
    "truenas_boot_env_size_bytes": "truenas_boot_environment_used_bytes",
    "truenas_certificate_days_to_expiry": "truenas_certificate_expiry_timestamp_seconds",
    "truenas_directoryservices_fault_reason": "truenas_directoryservices_fault_present",
    "truenas_network_gateway_reachable": "truenas_network_default_gateway_configured",
    "truenas_pool_dedup_ratio": "truenas_pool_dedup_table_size_bytes",
    "truenas_pool_expand_size_bytes": "truenas_pool_expand_reflowed_bytes / "
    "truenas_pool_expand_to_reflow_bytes / truenas_pool_expand_percent",
    "truenas_vm_flag_amd_asids": "truenas_vm_flag_amd_asids_supported",
}
DEPRECATED_DASHBOARD_METRICS = frozenset(DEPRECATED_DASHBOARD_METRIC_REPLACEMENTS)

# D2: TrueNAS 27.0 RC.1 sends 0 for the upstream hit/miss percentage fields
# while hits ~= accesses. Dashboards must derive percentages from the
# *_per_second rates instead of querying these series.
UNRELIABLE_RATIO_RE = re.compile(r"\btruenas_zfs_\w*_(?:hit|miss)_(?:ratio|percentage)\b")
# D1: truenas_alert_count includes dismissed alerts; outstanding alerts are
# alert_count minus alert_dismissed_count.
OUTSTANDING_ALERTS_RE = re.compile(
    r"truenas_alert_count\{[^}]*\}\)\s*-\s*\(sum\(truenas_alert_dismissed_count")
# D7: "No data" takes the base threshold colour, so it must be neutral grey.
NEUTRAL_COLOR = "#7B828C"
# D8: longest stat title that fits a tile of the given width (grid columns).
TITLE_LIMITS = {2: 7, 3: 11, 4: 16, 5: 20, 6: 24}


def walk_panels(panels: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
    for panel in panels:
        yield panel
        nested = panel.get("panels")
        if isinstance(nested, list):
            yield from walk_panels(item for item in nested if isinstance(item, dict))


def referenced_metric_names(dashboard: dict[str, Any]) -> set[str]:
    if "apiVersion" in dashboard:
        return set(METRIC_RE.findall(json.dumps(dashboard.get("spec", {}))))
    panels = list(walk_panels(dashboard.get("panels", [])))
    expressions = [
        target["expr"]
        for panel in panels
        for target in panel.get("targets", [])
        if isinstance(target, dict) and isinstance(target.get("expr"), str)
    ]

    templating = dashboard.get("templating", {}).get("list", [])
    for variable in templating:
        query = variable.get("definition") or variable.get("query")
        if isinstance(query, dict):
            query = query.get("query")
        if isinstance(query, str):
            expressions.append(query)

    return {name for expression in expressions for name in METRIC_RE.findall(expression)}


def dashboard_validation_errors(dashboard: dict[str, Any], contract: dict[str, Any]) -> list[str]:
    if "apiVersion" in dashboard:
        spec = dashboard.get("spec", {})
        elements = spec.get("elements", {})
        errors = []

        def check_refs(value: Any) -> None:
            if isinstance(value, dict):
                ref = value.get("element")
                if isinstance(ref, dict) and ref.get("name") not in elements:
                    errors.append(f"missing dashboard element: {ref.get('name')}")
                for child in value.values():
                    check_refs(child)
            elif isinstance(value, list):
                for child in value:
                    check_refs(child)

        check_refs(spec.get("layout", {}))
        panels = []
        for element in elements.values():
            panel = element.get("spec", {})
            queries = panel.get("data", {}).get("spec", {}).get("queries", [])
            panels.append({"id": panel.get("id"), "title": panel.get("title"), "targets": [
                item.get("spec", {}).get("query", {}).get("spec", {}) for item in queries
            ]})
        classic = {"panels": panels}
        errors.extend(dashboard_validation_errors(classic, contract))
        missing = referenced_metric_names(dashboard) - {m["name"] for m in contract["metrics"]}
        if missing:
            errors.append("undefined exporter metrics: " + ", ".join(sorted(missing)))
        return errors
    metric_names = {metric["name"] for metric in contract["metrics"]}
    panels = list(walk_panels(dashboard.get("panels", [])))

    errors: list[str] = []
    ids = [panel.get("id") for panel in panels if isinstance(panel.get("id"), int)]
    duplicates = sorted(panel_id for panel_id, count in Counter(ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate dashboard panel IDs: {duplicates}")

    for panel in panels:
        grid = panel.get("gridPos", {})
        if isinstance(grid, dict) and grid.get("x", 0) + grid.get("w", 0) > 24:
            errors.append(f"panel exceeds 24 columns: {panel.get('title', panel.get('id'))}")

    expressions = [
        target["expr"]
        for panel in panels
        for target in panel.get("targets", [])
        if isinstance(target, dict) and isinstance(target.get("expr"), str)
    ]
    unreliable = sorted({m for e in expressions for m in UNRELIABLE_RATIO_RE.findall(e)})
    if unreliable:
        errors.append("dashboard queries unreliable upstream ratio metrics (compute from rates): "
                      + ", ".join(unreliable))
    if panels and not any(OUTSTANDING_ALERTS_RE.search(e) for e in expressions):
        errors.append("dashboard lacks the outstanding-alerts expression "
                      "(truenas_alert_count minus truenas_alert_dismissed_count)")
    for panel in panels:
        if panel.get("type") not in ("stat", "bargauge", "gauge"):
            continue
        steps = panel.get("fieldConfig", {}).get("defaults", {}).get("thresholds", {}).get("steps", [])
        if steps and steps[0].get("color") != NEUTRAL_COLOR:
            errors.append(f"no-data colour is not neutral for panel: {panel.get('title', panel.get('id'))}")
        width = panel.get("gridPos", {}).get("w")
        if panel.get("type") == "stat" and len(panel.get("title", "")) > TITLE_LIMITS.get(width, 99):
            errors.append(f"stat title too long for w={width}: {panel.get('title')}")

    referenced = referenced_metric_names(dashboard)
    missing = sorted(referenced - metric_names)
    if missing:
        errors.append("dashboard references undefined exporter metrics: " + ", ".join(missing))
    unavailable = sorted(referenced & UNAVAILABLE_DASHBOARD_METRICS)
    if unavailable:
        errors.append("dashboard references unavailable exporter metrics: " + ", ".join(unavailable))
    deprecated = sorted(referenced & DEPRECATED_DASHBOARD_METRICS)
    if deprecated:
        replacements = ", ".join(
            f"{name} (use {DEPRECATED_DASHBOARD_METRIC_REPLACEMENTS[name]})" for name in deprecated
        )
        errors.append("dashboard references deprecated exporter metrics: " + replacements)
    return errors


def main() -> None:
    dashboard = json.loads(DASHBOARD.read_text(encoding="utf-8"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    panels = list(walk_panels(dashboard.get("panels", [])))
    referenced = referenced_metric_names(dashboard)
    errors = dashboard_validation_errors(dashboard, contract)
    if errors:
        raise SystemExit("\n".join(errors))

    print(f"dashboard_ok panels={len(panels)} metric_references={len(referenced)}")
    tabbed = json.loads((DASHBOARD.parent / "truenas-mission-control.json").read_text(encoding="utf-8"))
    errors = dashboard_validation_errors(tabbed, contract)
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"mission_control_dashboard_ok elements={len(tabbed['spec']['elements'])}")


if __name__ == "__main__":
    main()
