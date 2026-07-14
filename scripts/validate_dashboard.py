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


def walk_panels(panels: Iterable[dict[str, Any]]) -> Iterable[dict[str, Any]]:
    for panel in panels:
        yield panel
        nested = panel.get("panels")
        if isinstance(nested, list):
            yield from walk_panels(item for item in nested if isinstance(item, dict))


def referenced_metric_names(dashboard: dict[str, Any]) -> set[str]:
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


if __name__ == "__main__":
    main()
