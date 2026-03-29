#!/usr/bin/env python3
"""TrueNAS JSON-RPC to Prometheus exporter — v5.1 (bug-fix + metric gap pass).

v5.1 fixes vs v5 (gap-analysis follow-up):

  BUG FIXES
  - "disls" key fix: reporting.realtime disk I/O section uses key "disls" in
    v25.10.2 (confirmed in API schema), not "disks". All five disk I/O rate
    metrics (read/write bytes, read/write ops, busy%) were zero on every v25
    system. Handler now tries "disls" first, falls back to "disks" for v24.
  - truenas_snapshot_oldest_timestamp_seconds: advertised in v5 changelog but
    never implemented. Gauge now declared and populated; snapshot query updated
    to select properties.creation so the timestamp can be extracted.
  - event_interval_seconds config was read but never passed to core.subscribe.
    Subscription loop now uses "event:{"interval": N}" colon-notation for
    reporting.realtime, app.stats, and virt.instance.metrics when the
    configured interval exceeds the API default of 2 seconds.

  NEW METRICS
  - truenas_zfs_demand_accesses_per_second (total demand_accesses_per_second)
  - truenas_zfs_demand_data_io_hits_per_second (raw I/O hit rate)
  - truenas_zfs_demand_metadata_accesses_per_second
  - truenas_zfs_demand_metadata_io_hits_per_second
  - truenas_zfs_demand_metadata_io_hit_ratio
  - truenas_zfs_demand_metadata_miss_ratio
  - truenas_zfs_l2arc_accesses_per_second (total_l2arc_accesses_per_second)
  - truenas_zfs_l2arc_miss_ratio
  - ZFS hit/miss ratios now prefer API-provided percentages over computed
    values — the pre-computed percentages account for prefetch hits that are
    not in the demand hits+misses sum, making them more accurate.
  - truenas_pool_realtime_read_bytes_per_second{pool} (from realtime pools section)
  - truenas_pool_realtime_write_bytes_per_second{pool} (from realtime pools section)
  - truenas_nfs_v3_client_count (from nfs.get_nfs3_clients, was generic only)
  - truenas_nfs_v4_client_count (from nfs.get_nfs4_clients, was generic only)

  OTHER
  - default event subscriptions now align with the v25.10.2 API docs:
    virt.instance.metrics added and legacy container.metrics removed.

v5 fixes vs v4 (code-review pass):

  BUG FIXES
  - _last_boot_id initialised in __init__ (was in dead scrape_loop() method — AttributeError)
  - scrape_loop() dead method removed
  - SCRAPE_DURATION `started` assigned inside lock (dead pre-lock assignment removed)
  - Pool scan bytes_to_process / total_secs_left conflation fixed:
      separate truenas_pool_scan_seconds_remaining gauge added
  - Swap-free overwrite bug: inversion block now guarded by `not has_free_key`
  - Version string in main() updated to v5
  - DOCKER_STATUS added to bulk .clear() list
  - _total suffix removed from vdev error Gauge names (reserved for Counters)
  - All label-carrying info Gauges added to bulk .clear() block

  PROMETHEUS BEST-PRACTICE FIXES
  - truenas_exporter_info metric added (exporter version label)
  - truenas_collector_errors_total Counter added — silent try/except failures now counted
  - _rate suffix metrics renamed to _per_second to avoid PromQL `rate()` confusion

  NEW API ENDPOINTS (35+ read-only methods)
  - pool.scrub.query → truenas_pool_scrub_task_enabled/state/last_run
  - pool.snapshot.query → truenas_snapshot_count, truenas_snapshot_oldest_timestamp
  - pool.resilver.config → truenas_pool_resilver_enabled
  - pool.dataset.details → fed through generic extractor
  - cloud_backup.query → truenas_cloud_backup_task_count/enabled/state
  - cronjob.query → truenas_cronjob_count/enabled/state
  - disk.get_used → truenas_disk_in_use
  - dns.query → truenas_dns_resolver_count
  - smb.config → truenas_smb_config_info (multichannel, aapl_extensions)
  - nfs.config → truenas_nfs_v4_enabled, truenas_nfs_servers
  - ssh.config → truenas_ssh_enabled, truenas_ssh_password_auth
  - ftp.config → truenas_ftp_enabled
  - snmp.config → truenas_snmp_enabled
  - system.advanced.config → truenas_consolemenu_enabled, truenas_serialconsole_enabled
  - system.general.config → truenas_ui_https_port
  - kmip.config → truenas_kmip_enabled
  - support.is_available → truenas_support_available
  - systemdataset.config → truenas_systemdataset_pool
  - user.query → truenas_local_user_count
  - group.query → truenas_local_group_count
  - staticroute.query → truenas_static_route_count
  - tunable.query → truenas_tunable_count
  - iscsi.target.query → truenas_iscsi_target_count
  - iscsi.portal.query → truenas_iscsi_portal_count
  - iscsi.extent.query → truenas_iscsi_extent_count
  - iscsi.initiator.query → truenas_iscsi_initiator_count
  - nvmet.host.query → truenas_nvmet_host_count
  - nvmet.namespace.query → truenas_nvmet_namespace_count
  - network.configuration.config → truenas_network_httpproxy_configured
  - app.image.query → truenas_docker_image_count
  - replication.config.config → truenas_replication_max_parallel
  - reporting.exporters.query → truenas_reporting_exporter_count
  - reporting.config → truenas_reporting_enabled
  - vm.device.iommu_enabled → truenas_iommu_enabled
  - auth.twofactor.config → truenas_2fa_enabled
  - mail.config → truenas_mail_configured
  - alertservice.query → truenas_alertservice_count, truenas_alertservice_enabled
  - alertclasses.config → fed through generic extractor
  - initshutdownscript.query → truenas_initshutdownscript_count
  - privilege.query → truenas_privilege_count
  - keychaincredential.query → truenas_keychain_credential_count
  - system.global.id → truenas_system_global_id
  - kerberos.config → fed through generic extractor

  NEW EVENT SUBSCRIPTIONS
  - container.query (container state changes)
  - vm.query (VM state changes)

v3 additions vs v2:

  NEW HOST METRICS (CPU / RAM / Disk I/O / Network / ZFS ARC)
  - reporting.realtime dedicated handler (_handle_realtime_event) replaces generic
    event extraction for that stream, emitting clean named metrics:
      truenas_cpu_usage_percent, truenas_cpu_user/system/iowait/idle/interrupt_percent
      truenas_cpu_core_usage_percent{core=N}    (per-core)
      truenas_cpu_temperature_celsius{core=N}   (per-core temps from IPMI/hwmon)
      truenas_memory_physical_total/available/free/cached/buffers/used_bytes
      truenas_memory_swap_total/free/used_bytes
      truenas_disk_read/write_bytes_per_second{disk}  (live I/O rates per disk)
      truenas_disk_read/write_ops_per_second{disk}
      truenas_disk_busy_percent{disk}
      truenas_network_rx/tx_bytes_per_second{interface}
      truenas_zfs_arc_size/max_size/min_size_bytes
      truenas_zfs_arc_hit_ratio, truenas_zfs_arc_hits/misses_per_second

  NEW POOL METRICS
  - pool.query now requests topology field; _extract_vdev_errors walks the vdev
    tree and emits per-vdev error gauges:
      truenas_pool_vdev_read/write/checksum_errors_total{pool, vdev}
  - Detailed scan sub-metrics extracted:
      truenas_pool_scan_errors{pool}, truenas_pool_scan_bytes_processed/total{pool}
      truenas_pool_last_scan_timestamp_seconds{pool}

  NEW COLLECTORS
  - SMB sessions: _collect_smb_nfs_sessions → truenas_smb_session/connection/open_file_count
  - GPU: _collect_gpu_metrics (device.get_info GPU) → truenas_gpu_count, truenas_gpu_info{...}
  - JBOF: _collect_jbof_metrics → truenas_jbof_count
  - Active API sessions: _collect_auth_session_metrics → truenas_auth_sessions_active
  - Disk extended: _collect_disk_extended_metrics → truenas_disk_rotational, truenas_disk_smart_enabled

  ENHANCED SYSTEM.INFO EXTRACTION
  - truenas_host_ecc_memory (1 if ECC RAM present)
  - truenas_host_cpu_info{model=...} (CPU model string from DMI)
  - truenas_host_system_info{manufacturer, product} (hardware DMI labels)

v2 fixes vs v1 (see code-review for full details):
  BUG FIXES
  - call() recv-loop: bounded to MAX_STRAY_MESSAGES iterations to prevent infinite
    spin when unsolicited push messages arrive on the scrape WebSocket connection.
  - Duplicate API calls eliminated: generic extraction loop now populates a per-scrape
    result cache; dedicated collectors consume cached results instead of re-calling the
    API (halves WebSocket round-trips for ~15 high-cost methods).
  - system.security.info removed from BASE_METHODS (was also in REQUIRES_ENTITY_PARAM
    — the blocklist always wins, making the BASE_METHODS entry dead / misleading code).
  - core.get_jobs now receives a limit param in _auto_params (previously called with no
    params on a busy system could return thousands of job records).

  PROMETHEUS BEST-PRACTICE FIXES
  - API_CALL_ERRORS changed from Gauge to Counter (truenas_api_call_errors_total).
    The old Gauge created confusing zero-value "none" error_type series on success
    alongside stale "TimeoutError" series on recovery.
  - _status_like() isupper() fallback removed: previously matched any all-caps word
    (CPU, ARC, NFS, OK …) creating unbounded METHOD_STATUS_VALUE / EVENT_STATUS_VALUE
    cardinality; now only matches the explicit known-good set.
  - _normalize_path() regex pre-compiled at module level (was recompiled on every
    recursive call inside the generic extractor — potentially thousands of times per
    scrape).
  - truenas_system_boot_id UUID-as-label replaced with truenas_system_boot_changes_total
    Counter: the old metric created a new zombie series in Prometheus on every reboot
    that was never cleaned up; the Counter increments when a boot ID change is detected.
  - SCRAPE_DURATION now measured strictly inside the lock (previously included any
    lock-wait time from concurrent callers, masking true API latency).
  - Redundant .clear() calls removed from _collect_dataset_metrics(): gauges were
    already cleared unconditionally at the top of scrape_once().
  - /healthz endpoint added on the same port alongside /metrics so container
    orchestrators and load balancers can distinguish exporter crashes from scrape
    failures.

  Inherited fixes from v1:
  - auth.login_with_api_key return value now accepts dict/str/bool (v25 returns session dict)
  - sslopt explicitly sets check_hostname=False when verify_tls=False
  - Event subscription name no longer appends JSON payload (core.subscribe takes name only)
  - vm.status removed from BASE_METHODS (requires vm_id, already handled per-entity)
  - Gauge clears moved inside scrape lock to prevent partial-clear races
  - Exponential backoff (2s → 120s cap) in event stream reconnect loop
  - nfs.get_nfs3_clients / nfs.get_nfs4_clients called with correct query params

New metrics:
  - Boot pool health (boot.get_state, boot.get_disks)
  - Certificate expiry in days (certificate.query)
  - Per-dataset space / quota (pool.dataset.query)
  - Task health — replication, cloudsync, rsynctask, snapshottask
  - Directory services health (directoryservices.status)
  - IPMI chassis + SEL (gated on ipmi.is_loaded)
  - NFS/SMB share counts (sharing.nfs.query, sharing.smb.query)
  - ZFS resource query (zfs.resource.query via generic extraction)
  - System reboot pending (system.reboot.info)
  - Gateway reachability (route.ipv4gw_reachable)
  - TrueNAS identity flags (truenas.is_production, truenas.is_ix_hardware)
  - HA failover disabled reasons (failover.disabled.reasons)
  - Disk details (disk.details)

New default event subscriptions:
  - pool.scan (real-time scrub/resilver progress)
  - pool.query (pool state-change push events)
  - disk.query (hotplug/removal events)
  - docker.state (Docker daemon transitions)
  - container.metrics (per-container CPU/mem)
  - alert.list (push-based new alert delivery)
  - interface.query (link up/down events)
  - directoryservices.status (AD/LDAP health push)
  - failover.status (HA state transitions)
  - update.status (update progress events)
  - system.shutdown (shutdown initiated event)
  - core.get_jobs (background job progress)

v3 additions (Tier 1 + Tier 2):
  - system.product_type, system.version_short, system.host_id, system.boot_id
  - update.available_versions (version names available to upgrade to)
  - boot.environment.query (BE count, active, keep flags)
  - vm.supports_virtualization, vm.maximum_supported_vcpus
  - virt.instance.query, virt.volume.query (Incus/LXD — 25.x new resource type)
  - fc.fc_host.query, fcport.status (Fibre Channel HBAs and ports)
  - nvmet.global.sessions, nvmet.subsys.query, nvmet.port.query (NVMe-oF)
  - iscsi.global.alua_enabled, iscsi.global.iser_enabled (protocol flags)
  - interface.has_pending_changes, interface.checkin_waiting (network extras)
  - app.available_space, sharing.webshare.query (app/WebDAV)
  - ups.config (UPS status and mode)
  - catalog.trains (catalog health)
  - ipmi.lan.channels → ipmi.lan.query with correct channel param
  - truenas.managed_by_truecommand (fleet management)
"""

from __future__ import annotations

import json
import logging
import os
import re
import ssl
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from prometheus_client import Counter, Gauge, make_wsgi_app
from wsgiref.simple_server import WSGIRequestHandler, make_server
from websocket import create_connection, WebSocket, WebSocketTimeoutException


LOG = logging.getLogger("truenas_exporter")

# Pre-compiled regex for _normalize_path — avoids recompiling on every recursive call
# inside _extract_generic_metrics / _extract_event_metrics.
_PATH_NORMALIZE_RE = re.compile(r"[^a-zA-Z0-9_./\-]")

# Maximum number of out-of-order / unsolicited messages the recv loop will skip
# before giving up, to prevent an infinite spin if the server sends unexpected pushes.
_MAX_STRAY_MESSAGES = 100

_INTERVAL_EVENT_SUBSCRIPTIONS = {
    "reporting.realtime",
    "app.stats",
    "virt.instance.metrics",
}

# ---------------------------------------------------------------------------
# Exporter health
# ---------------------------------------------------------------------------
SCRAPE_SUCCESS = Gauge("truenas_up", "1 if last scrape succeeded, 0 otherwise")
LAST_SCRAPE_TS = Gauge("truenas_last_scrape_timestamp_seconds", "Unix timestamp of last scrape attempt")
SCRAPE_DURATION = Gauge("truenas_scrape_duration_seconds", "Duration of last scrape in seconds")

# ---------------------------------------------------------------------------
# API call diagnostics
# ---------------------------------------------------------------------------
API_CALL_SUCCESS = Gauge("truenas_api_call_success", "1 if API method call succeeded in latest scrape", ["method"])
API_CALL_DURATION = Gauge("truenas_api_call_duration_seconds", "Duration of API method call", ["method"])
# Counter (not Gauge): accumulates errors without creating stale zero-value 'none'
# series that pollute Prometheus when a method recovers from a previous failure.
API_CALL_ERRORS_TOTAL = Counter(
    "truenas_api_call_errors_total",
    "Total API call errors per method and error type since exporter start",
    ["method", "error_type"],
)

# ---------------------------------------------------------------------------
# System / host
# ---------------------------------------------------------------------------
SYSTEM_STATE = Gauge("truenas_system_state", "System state enum mapped to label with value 1", ["state"])
SYSTEM_READY = Gauge("truenas_system_ready", "1 if system state is READY")
SYSTEM_REBOOT_REQUIRED = Gauge("truenas_system_reboot_required", "1 if a system reboot is pending")
SYSTEM_REBOOT_REASON = Gauge("truenas_system_reboot_reason", "Pending reboot reason as label", ["reason"])

HOST_INFO = Gauge("truenas_host_info", "Static host info exported as labels", ["hostname", "version", "product_type"])
HOST_UPTIME_SECONDS = Gauge("truenas_host_uptime_seconds", "Host uptime in seconds")
HOST_PHYSICAL_MEMORY_BYTES = Gauge("truenas_host_physical_memory_bytes", "Host physical memory in bytes")
HOST_CPU_CORES = Gauge("truenas_host_cpu_cores", "Host CPU core count")
HOST_PHYSICAL_CPU_CORES = Gauge("truenas_host_physical_cpu_cores", "Host physical CPU cores (non-HT)")
HOST_LOAD_AVERAGE = Gauge("truenas_host_load_average", "Host load average", ["window"])

TRUENAS_IS_PRODUCTION = Gauge("truenas_is_production", "1 if system is marked as production")
TRUENAS_IS_IX_HARDWARE = Gauge("truenas_is_ix_hardware", "1 if running on iXsystems hardware")

# ---------------------------------------------------------------------------
# Boot pool
# ---------------------------------------------------------------------------
BOOT_POOL_HEALTHY = Gauge("truenas_boot_pool_healthy", "1 if boot pool is healthy")
BOOT_POOL_STATUS = Gauge("truenas_boot_pool_status", "Boot pool status as label", ["status"])
BOOT_POOL_SIZE_BYTES = Gauge("truenas_boot_pool_size_bytes", "Boot pool total size in bytes")
BOOT_POOL_ALLOCATED_BYTES = Gauge("truenas_boot_pool_allocated_bytes", "Boot pool allocated bytes")
BOOT_POOL_FREE_BYTES = Gauge("truenas_boot_pool_free_bytes", "Boot pool free bytes")
BOOT_POOL_DISK_COUNT = Gauge("truenas_boot_pool_disk_count", "Number of disks in boot pool")
BOOT_POOL_SCAN_STATE = Gauge("truenas_boot_pool_scan_state", "Boot pool scrub/resilver state as label", ["state"])
BOOT_POOL_SCAN_PERCENT = Gauge("truenas_boot_pool_scan_percent", "Boot pool active scan percentage (0 to 100)")

# ---------------------------------------------------------------------------
# Data pools
# ---------------------------------------------------------------------------
POOL_COUNT = Gauge("truenas_pool_count", "Number of pools")
POOL_HEALTHY = Gauge("truenas_pool_healthy", "Pool healthy flag (1 healthy, 0 not)", ["pool"])
POOL_STATUS = Gauge("truenas_pool_status", "Pool status enum mapped to 1", ["pool", "status"])
POOL_SIZE_BYTES = Gauge("truenas_pool_size_bytes", "Pool total size in bytes", ["pool"])
POOL_ALLOCATED_BYTES = Gauge("truenas_pool_allocated_bytes", "Pool allocated bytes", ["pool"])
POOL_FREE_BYTES = Gauge("truenas_pool_free_bytes", "Pool free bytes", ["pool"])
POOL_SCAN_PERCENT = Gauge("truenas_pool_scan_percent", "Active pool scan/scrub percentage (0 to 100)", ["pool"])
POOL_FRAGMENTATION = Gauge("truenas_pool_fragmentation_percent", "Pool fragmentation percentage (0 to 100)", ["pool"])
POOL_AUTOTRIM_ENABLED = Gauge("truenas_pool_autotrim_enabled", "1 if autotrim is enabled on the pool", ["pool"])
POOL_DEDUP_RATIO = Gauge("truenas_pool_dedup_ratio", "Pool deduplication ratio (1.0 means no dedup savings)", ["pool"])
POOL_EXPAND_SIZE_BYTES = Gauge("truenas_pool_expand_size_bytes", "Pool expandable size in bytes", ["pool"])

# ---------------------------------------------------------------------------
# Datasets
# ---------------------------------------------------------------------------
DATASET_COUNT = Gauge("truenas_dataset_count", "Total number of datasets returned by query")
DATASET_USED_BYTES = Gauge("truenas_dataset_used_bytes", "Dataset used space in bytes", ["dataset"])
DATASET_AVAILABLE_BYTES = Gauge("truenas_dataset_available_bytes", "Dataset available space in bytes", ["dataset"])
DATASET_REFERENCED_BYTES = Gauge("truenas_dataset_referenced_bytes", "Dataset referenced bytes", ["dataset"])
DATASET_QUOTA_BYTES = Gauge("truenas_dataset_quota_bytes", "Dataset quota in bytes (0 = no quota)", ["dataset"])
DATASET_REFQUOTA_BYTES = Gauge("truenas_dataset_refquota_bytes", "Dataset refquota in bytes (0 = no quota)", ["dataset"])
DATASET_SNAPSHOT_COUNT = Gauge("truenas_dataset_snapshot_count", "Number of snapshots for dataset", ["dataset"])
DATASET_COMPRESSION_RATIO = Gauge("truenas_dataset_compression_ratio", "Dataset compression ratio", ["dataset"])
DATASET_ENCRYPTED = Gauge("truenas_dataset_encrypted", "1 if dataset is encrypted", ["dataset"])
DATASET_RESERVATION_BYTES = Gauge("truenas_dataset_reservation_bytes", "Dataset reservation in bytes", ["dataset"])
DATASET_REFRESERVATION_BYTES = Gauge("truenas_dataset_refreservation_bytes", "Dataset refreservation in bytes", ["dataset"])
DATASET_USED_BY_CHILDREN_BYTES = Gauge("truenas_dataset_used_by_children_bytes", "Dataset space used by child datasets in bytes", ["dataset"])
DATASET_USED_BY_DATASET_BYTES = Gauge("truenas_dataset_used_by_dataset_bytes", "Dataset space used by the dataset itself in bytes", ["dataset"])
DATASET_USED_BY_SNAPSHOTS_BYTES = Gauge("truenas_dataset_used_by_snapshots_bytes", "Dataset space used by snapshots in bytes", ["dataset"])
DATASET_READONLY = Gauge("truenas_dataset_readonly", "1 if dataset readonly is enabled", ["dataset"])
DATASET_ATIME = Gauge("truenas_dataset_atime", "1 if dataset atime updates are enabled", ["dataset"])
DATASET_EXEC = Gauge("truenas_dataset_exec", "1 if dataset allows executable files", ["dataset"])
DATASET_KEY_LOADED = Gauge("truenas_dataset_key_loaded", "1 if encrypted dataset keys are loaded", ["dataset"])
DATASET_LOCKED = Gauge("truenas_dataset_locked", "1 if encrypted dataset is locked", ["dataset"])
DATASET_QUOTA_WARNING_PERCENT = Gauge("truenas_dataset_quota_warning_percent", "Dataset quota warning threshold percentage", ["dataset"])
DATASET_QUOTA_CRITICAL_PERCENT = Gauge("truenas_dataset_quota_critical_percent", "Dataset quota critical threshold percentage", ["dataset"])
DATASET_REFQUOTA_WARNING_PERCENT = Gauge("truenas_dataset_refquota_warning_percent", "Dataset refquota warning threshold percentage", ["dataset"])
DATASET_REFQUOTA_CRITICAL_PERCENT = Gauge("truenas_dataset_refquota_critical_percent", "Dataset refquota critical threshold percentage", ["dataset"])
DATASET_CREATION_TS = Gauge("truenas_dataset_creation_timestamp_seconds", "Dataset creation timestamp as Unix seconds", ["dataset"])

# ---------------------------------------------------------------------------
# Disks
# ---------------------------------------------------------------------------
DISK_COUNT = Gauge("truenas_disk_count", "Number of disks")
DISK_SIZE_BYTES = Gauge("truenas_disk_size_bytes", "Disk size in bytes", ["disk"])
DISK_TEMPERATURE_C = Gauge("truenas_disk_temperature_celsius", "Disk temperature in Celsius", ["disk"])
DISK_TEMP_ALERT_COUNT = Gauge("truenas_disk_temperature_alert_count", "Temperature alert count per disk", ["disk"])
DISK_TEMP_AGG_C = Gauge("truenas_disk_temperature_agg_celsius", "Aggregated disk temperature metrics", ["disk", "kind"])

# ---------------------------------------------------------------------------
# Network
# ---------------------------------------------------------------------------
INTERFACE_COUNT = Gauge("truenas_interface_count", "Number of network interfaces")
INTERFACE_LINK_UP = Gauge("truenas_interface_link_up", "1 if interface link is up", ["interface"])
NETWORK_DEFAULT_ROUTES = Gauge("truenas_network_default_routes", "Number of default routes")
NETWORK_NAMESERVERS = Gauge("truenas_network_nameservers", "Number of configured nameservers")
NETWORK_GATEWAY_REACHABLE = Gauge("truenas_network_gateway_reachable", "1 if the default IPv4 gateway is reachable")

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
SERVICE_COUNT = Gauge("truenas_service_count", "Number of services")
SERVICE_ENABLED = Gauge("truenas_service_enabled", "1 if service is enabled", ["service"])
SERVICE_RUNNING = Gauge("truenas_service_running", "1 if service is running", ["service"])

# ---------------------------------------------------------------------------
# NFS / SMB shares
# ---------------------------------------------------------------------------
NFS_SHARE_COUNT = Gauge("truenas_nfs_share_count", "Number of configured NFS shares")
SMB_SHARE_COUNT = Gauge("truenas_smb_share_count", "Number of configured SMB shares")

# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------
ALERT_COUNT = Gauge("truenas_alert_count", "Total number of active alerts")
ALERT_COUNT_BY_LEVEL = Gauge("truenas_alert_count_by_level", "Alert count by level", ["level"])
ALERT_COUNT_BY_SOURCE = Gauge("truenas_alert_count_by_source", "Alert count by source component", ["source"])
ALERT_COUNT_BY_CLASS = Gauge("truenas_alert_count_by_class", "Alert count by class and level", ["klass", "level"])
ALERT_COUNT_BY_NODE = Gauge("truenas_alert_count_by_node", "Alert count by node", ["node"])
ALERT_DISMISSED_COUNT = Gauge("truenas_alert_dismissed_count", "Number of dismissed alerts")
ALERT_ONE_SHOT_COUNT = Gauge("truenas_alert_one_shot_count", "Number of one-shot alerts")
ALERT_OLDEST_TS = Gauge("truenas_alert_oldest_timestamp_seconds", "Unix timestamp of the oldest current alert")
ALERT_LAST_OCCURRENCE_TS = Gauge("truenas_alert_last_occurrence_timestamp_seconds", "Most recent alert occurrence timestamp by level", ["level"])

# ---------------------------------------------------------------------------
# Jobs
# ---------------------------------------------------------------------------
JOB_ACTIVE_COUNT = Gauge("truenas_job_active_count", "Number of active jobs in WAITING or RUNNING state")
JOB_ACTIVE_COUNT_BY_STATE = Gauge("truenas_job_active_count_by_state", "Number of active jobs by state", ["state"])
JOB_ACTIVE_COUNT_BY_METHOD = Gauge("truenas_job_active_count_by_method", "Number of active jobs by method and state", ["method", "state"])
JOB_ABORTABLE_ACTIVE_COUNT = Gauge("truenas_job_abortable_active_count", "Number of active abortable jobs")
JOB_TRANSIENT_ACTIVE_COUNT = Gauge("truenas_job_transient_active_count", "Number of active transient jobs")
JOB_OLDEST_ACTIVE_TS = Gauge("truenas_job_oldest_active_timestamp_seconds", "Unix timestamp of the oldest active job by state", ["state"])
JOB_PROGRESS_PERCENT = Gauge("truenas_job_progress_percent", "Maximum running job progress percent by method", ["method"])

# ---------------------------------------------------------------------------
# Updates
# ---------------------------------------------------------------------------
UPDATE_STATUS = Gauge("truenas_update_status", "Update status as label with value 1", ["status"])
UPDATE_AVAILABLE = Gauge("truenas_update_available", "1 if an update is available")

# ---------------------------------------------------------------------------
# Certificates
# ---------------------------------------------------------------------------
CERT_COUNT = Gauge("truenas_certificate_count", "Number of certificates")
CERT_DAYS_TO_EXPIRY = Gauge(
    "truenas_certificate_days_to_expiry",
    "Days until certificate expires (negative = already expired)",
    ["name", "issuer"],
)

# ---------------------------------------------------------------------------
# Directory services
# ---------------------------------------------------------------------------
DIRECTORYSERVICES_HEALTHY = Gauge(
    "truenas_directoryservices_healthy",
    "1 if directory service appears healthy",
    ["service"],
)
DIRECTORYSERVICES_STATUS = Gauge(
    "truenas_directoryservices_status",
    "Directory service status as label",
    ["service", "status"],
)
DIRECTORYSERVICES_FAULT_REASON = Gauge(
    "truenas_directoryservices_fault_reason",
    "Directory service fault reason as label",
    ["service", "reason"],
)

# ---------------------------------------------------------------------------
# Docker / Apps
# ---------------------------------------------------------------------------
DOCKER_NVIDIA_PRESENT = Gauge("truenas_docker_nvidia_present", "1 if NVIDIA GPU is present for Docker")
DOCKER_NETWORK_COUNT = Gauge("truenas_docker_network_count", "Number of Docker networks")
DOCKER_STATUS = Gauge("truenas_docker_status", "Docker daemon status", ["status"])
APP_COUNT = Gauge("truenas_app_count", "Number of applications")
APP_STATE = Gauge("truenas_app_state", "Per-app state as label — always 1", ["app", "state"])
APP_UPGRADE_AVAILABLE = Gauge("truenas_app_upgrade_available", "1 if an app upgrade is available", ["app"])
APP_IMAGE_UPDATES_AVAILABLE = Gauge("truenas_app_image_updates_available", "1 if updated app container images are available", ["app"])
APP_CUSTOM = Gauge("truenas_app_custom", "1 if the app is a custom app", ["app"])
APP_MIGRATED = Gauge("truenas_app_migrated", "1 if the app was migrated from Kubernetes", ["app"])
APP_CONTAINER_COUNT = Gauge("truenas_app_container_count", "Number of active containers for an app", ["app"])
APP_USED_PORT_COUNT = Gauge("truenas_app_used_port_count", "Number of active workload port mappings for an app", ["app"])
APP_USED_HOST_IP_COUNT = Gauge("truenas_app_used_host_ip_count", "Number of host IPs used by an app", ["app"])
APP_CONTAINER_STATE_COUNT = Gauge("truenas_app_container_state_count", "Count of app containers by runtime state", ["app", "state"])

# ---------------------------------------------------------------------------
# NFS / iSCSI client counts (dedicated gauges)
# ---------------------------------------------------------------------------
NFS_CLIENT_COUNT = Gauge("truenas_nfs_client_count", "Number of NFS clients")
NFS_V3_CLIENT_COUNT = Gauge("truenas_nfs_v3_client_count", "Number of active NFSv3 clients")
NFS_V4_CLIENT_COUNT = Gauge("truenas_nfs_v4_client_count", "Number of active NFSv4 clients")
ISCSI_CLIENT_COUNT = Gauge("truenas_iscsi_client_count", "Number of iSCSI clients")

# ---------------------------------------------------------------------------
# Interface extras (MTU, type)
# ---------------------------------------------------------------------------
INTERFACE_MTU = Gauge("truenas_interface_mtu", "Interface MTU in bytes", ["interface"])
INTERFACE_TYPE = Gauge("truenas_interface_type", "Interface type (PHYSICAL/BRIDGE/etc)", ["interface", "type"])

# ---------------------------------------------------------------------------
# VMs
# ---------------------------------------------------------------------------
VM_COUNT = Gauge("truenas_vm_count", "Number of virtual machines")
VM_AVAILABLE_MEMORY_BYTES = Gauge("truenas_vm_available_memory_bytes", "Available memory for VMs")
VM_VMEMORY_IN_USE_BYTES = Gauge("truenas_vm_vmemory_in_use_bytes", "Virtual memory in use by VMs in bytes", ["state"])

# ---------------------------------------------------------------------------
# Tasks (replication, cloudsync, rsync, snapshot)
# ---------------------------------------------------------------------------
TASK_ENABLED = Gauge("truenas_task_enabled", "1 if task is enabled", ["task_type", "name"])
TASK_STATE = Gauge(
    "truenas_task_state",
    "Task last run state as label with value 1",
    ["task_type", "name", "state"],
)
TASK_LAST_RUN_TS = Gauge(
    "truenas_task_last_run_timestamp_seconds",
    "Unix timestamp of task last run completion",
    ["task_type", "name"],
)
TASK_COUNT = Gauge("truenas_task_count", "Number of configured tasks", ["task_type"])

# Snapshot task limits
SNAPSHOT_TASK_MAX_COUNT = Gauge("truenas_snapshot_task_max_count", "Maximum number of snapshot tasks allowed")
SNAPSHOT_TASK_MAX_TOTAL_COUNT = Gauge("truenas_snapshot_task_max_total_count", "Maximum total snapshot tasks allowed")

# ---------------------------------------------------------------------------
# IPMI
# ---------------------------------------------------------------------------
IPMI_LOADED = Gauge("truenas_ipmi_loaded", "1 if IPMI kernel module is loaded")
IPMI_CHASSIS_POWER_ON = Gauge("truenas_ipmi_chassis_power_on", "1 if chassis power is on")
IPMI_CHASSIS_POWER_OVERLOAD = Gauge("truenas_ipmi_chassis_power_overload", "1 if power overload detected")
IPMI_CHASSIS_INTRUSION = Gauge("truenas_ipmi_chassis_intrusion", "1 if chassis intrusion detected")
IPMI_CHASSIS_DRIVE_FAULT = Gauge("truenas_ipmi_chassis_drive_fault", "1 if drive fault detected")
IPMI_CHASSIS_FAN_FAULT = Gauge("truenas_ipmi_chassis_fan_fault", "1 if fan fault detected")
IPMI_SEL_ENTRY_COUNT = Gauge("truenas_ipmi_sel_entry_count", "Number of entries in IPMI System Event Log")
IPMI_SEL_FREE_SPACE_BYTES = Gauge("truenas_ipmi_sel_free_space_bytes", "Free space in IPMI SEL in bytes")

# ---------------------------------------------------------------------------
# HA failover
# ---------------------------------------------------------------------------
FAILOVER_DISABLED_REASON_COUNT = Gauge(
    "truenas_failover_disabled_reason_count",
    "Number of reasons HA failover is currently disabled",
)
FAILOVER_DISABLED_REASON = Gauge(
    "truenas_failover_disabled_reason",
    "HA failover disabled reason as label with value 1",
    ["reason"],
)

# ---------------------------------------------------------------------------
# System extras (version, product type, identity)
# ---------------------------------------------------------------------------
SYSTEM_PRODUCT_TYPE = Gauge("truenas_system_product_type", "System product type as label", ["product_type"])
SYSTEM_VERSION = Gauge("truenas_system_version", "TrueNAS version as label", ["version"])
# System identity — host_id is stable (safe label); boot_id changes every reboot so
# we track it as a Counter increment rather than a UUID label, which would create
# a new zombie series in Prometheus after every reboot.
SYSTEM_HOST_ID = Gauge(
    "truenas_system_host_id",
    "Always 1; host_id label is a stable UUID, does not change between reboots",
    ["host_id"],
)
SYSTEM_BOOT_CHANGES_TOTAL = Counter(
    "truenas_system_boot_changes_total",
    "Number of boot ID changes detected since exporter start (proxy for reboot count)",
)
SYSTEM_MANAGED_BY_TRUECOMMAND = Gauge("truenas_managed_by_truecommand", "1 if managed by TrueCommand")

# ---------------------------------------------------------------------------
# Update extras
# ---------------------------------------------------------------------------
UPDATE_VERSION_AVAILABLE = Gauge("truenas_update_version_available", "1 = version available", ["version"])

# ---------------------------------------------------------------------------
# Boot environments
# ---------------------------------------------------------------------------
BOOT_ENV_COUNT = Gauge("truenas_boot_env_count", "Total number of boot environments")
BOOT_ENV_ACTIVE_COUNT = Gauge("truenas_boot_env_active_count", "Number of active boot environments")
BOOT_ENV_KEEP_COUNT = Gauge("truenas_boot_env_keep_count", "Number of boot environments marked keep=true")
BOOT_ENV_SIZE_BYTES = Gauge("truenas_boot_env_size_bytes", "Size of boot environment in bytes", ["name"])
BOOT_ENV_ACTIVE = Gauge("truenas_boot_env_active", "1 if boot environment is active", ["name"])
BOOT_ENV_KEEP = Gauge("truenas_boot_env_keep", "1 if boot environment is marked keep", ["name"])

# ---------------------------------------------------------------------------
# VM / Virtualization extras
# ---------------------------------------------------------------------------
VM_SUPPORTS_VIRTUALIZATION = Gauge("truenas_vm_supports_virtualization", "1 if KVM/hardware virt is available")
VM_MAX_VCPUS = Gauge("truenas_vm_maximum_supported_vcpus", "Maximum vCPUs the system can offer")
HW_VIRT_VARIANT = Gauge("truenas_hw_virt_variant", "Hardware virtualization variant", ["variant"])

# ---------------------------------------------------------------------------
# Virt (Incus/LXD — TrueNAS 25.x new resource type)
# ---------------------------------------------------------------------------
VIRT_INSTANCE_COUNT = Gauge("truenas_virt_instance_count", "Number of Incus/LXD virtual instances")
VIRT_INSTANCE_RUNNING = Gauge("truenas_virt_instance_running", "1 if Incus instance is running", ["name", "type"])
VIRT_INSTANCE_CPU = Gauge("truenas_virt_instance_cpu_usage_percent", "Incus instance CPU usage %", ["name"])
VIRT_INSTANCE_MEM = Gauge("truenas_virt_instance_mem_bytes", "Incus instance memory usage bytes", ["name"])
VIRT_VOLUME_COUNT = Gauge("truenas_virt_volume_count", "Number of Incus storage volumes")
VIRT_VOLUME_SIZE_BYTES = Gauge("truenas_virt_volume_size_bytes", "Incus volume size bytes", ["name", "pool"])
VIRT_GLOBAL_STATE = Gauge("truenas_virt_global_state", "Virt/Incus global state", ["state"])

# ---------------------------------------------------------------------------
# Fibre Channel
# ---------------------------------------------------------------------------
FC_HOST_COUNT = Gauge("truenas_fc_host_count", "Number of Fibre Channel host adapters")
FC_PORT_COUNT = Gauge("truenas_fc_port_count", "Number of Fibre Channel ports")
FC_PORT_SPEED = Gauge("truenas_fc_port_speed_gbit", "FC port link speed in Gbit/s", ["port"])
FC_PORT_ONLINE = Gauge("truenas_fc_port_online", "1 if FC port is online", ["port"])

# ---------------------------------------------------------------------------
# NVMe-oF
# ---------------------------------------------------------------------------
NVMET_SESSION_COUNT = Gauge("truenas_nvmet_session_count", "Number of active NVMe-oF sessions")
NVMET_SUBSYS_COUNT = Gauge("truenas_nvmet_subsys_count", "Number of NVMe-oF subsystems")
NVMET_PORT_COUNT = Gauge("truenas_nvmet_port_count", "Number of NVMe-oF ports")

# ---------------------------------------------------------------------------
# iSCSI protocol extras
# ---------------------------------------------------------------------------
ISCSI_ALUA_ENABLED = Gauge("truenas_iscsi_alua_enabled", "1 if iSCSI ALUA protocol is enabled")
ISCSI_ISER_ENABLED = Gauge("truenas_iscsi_iser_enabled", "1 if iSCSI iSER (RDMA) protocol is enabled")

# ---------------------------------------------------------------------------
# Network extras
# ---------------------------------------------------------------------------
INTERFACE_HAS_PENDING_CHANGES = Gauge("truenas_interface_has_pending_changes", "1 if there are uncommitted network configuration changes")
INTERFACE_CHECKIN_WAITING_SECONDS = Gauge("truenas_interface_checkin_waiting_seconds", "Seconds until pending network changes auto-rollback (0 = no rollback pending)")

# ---------------------------------------------------------------------------
# App extras
# ---------------------------------------------------------------------------
APP_AVAILABLE_SPACE_BYTES = Gauge("truenas_app_available_space_bytes", "Bytes available for new app installs")
APP_WEBDAV_SHARE_COUNT = Gauge("truenas_webdav_share_count", "Number of WebDAV (WebShare) shares")

# ---------------------------------------------------------------------------
# UPS
# ---------------------------------------------------------------------------
UPS_STATUS = Gauge("truenas_ups_status", "UPS status string as label", ["status"])
UPS_CONFIGURED = Gauge("truenas_ups_configured", "1 if a UPS device is configured")

# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------
CATALOG_TRAIN_COUNT = Gauge("truenas_catalog_train_count", "Number of app catalog trains available")

# ---------------------------------------------------------------------------
# Security / FIPS
# ---------------------------------------------------------------------------
FIPS_AVAILABLE = Gauge("truenas_fips_available", "1 if FIPS is available on this system")
FIPS_ENABLED = Gauge("truenas_fips_enabled", "1 if FIPS mode is currently enabled")

# ---------------------------------------------------------------------------
# Feature flags
# ---------------------------------------------------------------------------
FEATURE_ENABLED = Gauge("truenas_feature_enabled", "1 if feature is enabled", ["feature"])

# ---------------------------------------------------------------------------
# Hardware / Chassis
# ---------------------------------------------------------------------------
CHASSIS_HARDWARE = Gauge("truenas_chassis_hardware", "Chassis hardware model", ["model"])

# ---------------------------------------------------------------------------
# TrueNAS Connect (cloud management)
# ---------------------------------------------------------------------------
TN_CONNECT_ENABLED = Gauge("truenas_tn_connect_enabled", "1 if TrueNAS Connect is enabled")
TN_CONNECT_STATUS = Gauge("truenas_tn_connect_status", "TrueNAS Connect status", ["status"])

# ---------------------------------------------------------------------------
# TrueCommand (full status)
# ---------------------------------------------------------------------------
TRUECOMMAND_STATUS = Gauge("truenas_truecommand_status", "TrueCommand connection status", ["status"])

# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------
AUDIT_DATASET_USED_BYTES = Gauge("truenas_audit_dataset_used_bytes", "Audit dataset used space in bytes")
AUDIT_DATASET_AVAILABLE_BYTES = Gauge("truenas_audit_dataset_available_bytes", "Audit dataset available space in bytes")
AUDIT_QUOTA_FILL_WARNING_PERCENT = Gauge("truenas_audit_quota_fill_warning_percent", "Audit quota fill warning threshold percentage")
AUDIT_QUOTA_FILL_CRITICAL_PERCENT = Gauge("truenas_audit_quota_fill_critical_percent", "Audit quota fill critical threshold percentage")

# ---------------------------------------------------------------------------
# Pool warnings
# ---------------------------------------------------------------------------
POOL_WARNING = Gauge("truenas_pool_warning", "Pool warning flag (1 if warning present)", ["pool"])

# ---------------------------------------------------------------------------
# Filesystem paths
# ---------------------------------------------------------------------------
FILESYSTEM_PATH_COUNT = Gauge("truenas_filesystem_path_count", "Number of filesystem paths being scraped")

# ---------------------------------------------------------------------------
# Generic auto-discovered method metrics
#
# CARDINALITY WARNING: These metrics carry [method, path] labels.
# With AUTO_DISCOVER_METHODS=true and MAX_METHOD_CALLS=250, each method's
# nested result dict creates a unique (method, path) label combination up to
# MAX_METRIC_DEPTH=6 levels deep. This can generate 50k–500k+ unique series.
# Ensure your Prometheus storage is sized accordingly before enabling
# AUTO_DISCOVER_METHODS or SCRAPE_ALL_METRICS. Monitor growth with
# prometheus_tsdb_head_series or the truenas_collector_errors_total metric.
# ---------------------------------------------------------------------------
METHOD_NUMERIC_VALUE = Gauge("truenas_method_numeric_value", "Numeric value from method result", ["method", "path"])
METHOD_BOOLEAN_VALUE = Gauge("truenas_method_boolean_value", "Boolean value from method result (1/0)", ["method", "path"])
METHOD_STATUS_VALUE = Gauge("truenas_method_status_value", "Status string from method result", ["method", "path", "status"])
METHOD_LIST_LENGTH = Gauge("truenas_method_list_length", "List length from method result", ["method", "path"])

# ---------------------------------------------------------------------------
# Event stream metrics
# ---------------------------------------------------------------------------
EVENT_STREAM_UP = Gauge("truenas_event_stream_up", "1 when event subscription is active", ["event"])
EVENT_LAST_MESSAGE_TS = Gauge("truenas_event_last_message_timestamp_seconds", "Last event message timestamp", ["event"])
EVENT_MESSAGES_TOTAL = Counter("truenas_event_messages_total", "Total event messages received", ["event"])
EVENT_NUMERIC_VALUE = Gauge("truenas_event_numeric_value", "Numeric values from event payload", ["event", "path"])
EVENT_BOOLEAN_VALUE = Gauge("truenas_event_boolean_value", "Boolean values from event payload (1/0)", ["event", "path"])
EVENT_STATUS_VALUE = Gauge("truenas_event_status_value", "Status values from event payload", ["event", "path", "status"])
EVENT_LIST_LENGTH = Gauge("truenas_event_list_length", "List length from event payload", ["event", "path"])

# ---------------------------------------------------------------------------
# Realtime host metrics (from reporting.realtime event stream)
# These provide live CPU / RAM / disk I/O / network / ZFS ARC readings.
# ---------------------------------------------------------------------------

# CPU usage (updated every time a reporting.realtime event arrives, ~1s interval)
CPU_USAGE_PERCENT = Gauge("truenas_cpu_usage_percent", "Total host CPU usage percent (0 to 100, all cores combined)")
CPU_USER_PERCENT = Gauge("truenas_cpu_user_percent", "Host CPU user-space usage percent (0 to 100); falls back to total CPU usage when user split is unavailable")
CPU_SYSTEM_PERCENT = Gauge("truenas_cpu_system_percent", "Host CPU kernel usage percent (0 to 100)")
CPU_IOWAIT_PERCENT = Gauge("truenas_cpu_iowait_percent", "Host CPU I/O wait percent (0 to 100)")
CPU_IDLE_PERCENT = Gauge("truenas_cpu_idle_percent", "Host CPU idle percent (0 to 100); inferred as 100-total usage when idle split is unavailable")
CPU_INTERRUPT_PERCENT = Gauge("truenas_cpu_interrupt_percent", "Host CPU interrupt/hardware IRQ percent (0 to 100)")
CPU_CORE_USAGE_PERCENT = Gauge("truenas_cpu_core_usage_percent", "Per-CPU-core usage percent (0 to 100)", ["core"])
CPU_TEMPERATURE_C = Gauge("truenas_cpu_temperature_celsius", "Per-CPU-core temperature in Celsius", ["core"])

# Memory (live values from reporting.realtime)
MEMORY_PHYSICAL_TOTAL_BYTES = Gauge("truenas_memory_physical_total_bytes", "Total physical RAM in bytes")
MEMORY_PHYSICAL_AVAILABLE_BYTES = Gauge("truenas_memory_physical_available_bytes", "Available physical RAM in bytes")
MEMORY_PHYSICAL_FREE_BYTES = Gauge("truenas_memory_physical_free_bytes", "Free physical RAM in bytes")
MEMORY_PHYSICAL_CACHED_BYTES = Gauge("truenas_memory_physical_cached_bytes", "Page cache bytes")
MEMORY_PHYSICAL_BUFFERS_BYTES = Gauge("truenas_memory_physical_buffers_bytes", "Buffer cache bytes")
MEMORY_PHYSICAL_USED_BYTES = Gauge("truenas_memory_physical_used_bytes", "Used physical RAM in bytes (total - available)")
MEMORY_SWAP_TOTAL_BYTES = Gauge("truenas_memory_swap_total_bytes", "Swap total in bytes")
MEMORY_SWAP_FREE_BYTES = Gauge("truenas_memory_swap_free_bytes", "Swap free in bytes")
MEMORY_SWAP_USED_BYTES = Gauge("truenas_memory_swap_used_bytes", "Swap used in bytes")

# Disk I/O rates (per disk, from reporting.realtime)
DISK_READ_BYTES_RATE = Gauge("truenas_disk_read_bytes_per_second", "Disk read throughput in bytes/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_WRITE_BYTES_RATE = Gauge("truenas_disk_write_bytes_per_second", "Disk write throughput in bytes/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_READ_OPS_RATE = Gauge("truenas_disk_read_ops_per_second", "Disk read operations/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_WRITE_OPS_RATE = Gauge("truenas_disk_write_ops_per_second", "Disk write operations/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_BUSY_PERCENT = Gauge("truenas_disk_busy_percent", "Disk busy percentage (0–100)", ["disk"])

# Network I/O rates (per interface, from reporting.realtime)
NETWORK_RX_BYTES_RATE = Gauge("truenas_network_rx_bytes_per_second", "Network interface receive bytes/sec (instantaneous snapshot from realtime API)", ["interface"])
NETWORK_TX_BYTES_RATE = Gauge("truenas_network_tx_bytes_per_second", "Network interface transmit bytes/sec (instantaneous snapshot from realtime API)", ["interface"])

# ZFS ARC (from reporting.realtime or memory/zfs subsection in v25)
ZFS_ARC_SIZE_BYTES = Gauge("truenas_zfs_arc_size_bytes", "ZFS ARC current size in bytes")
ZFS_ARC_MAX_SIZE_BYTES = Gauge("truenas_zfs_arc_max_size_bytes", "ZFS ARC maximum allowed size in bytes")
ZFS_ARC_MIN_SIZE_BYTES = Gauge("truenas_zfs_arc_min_size_bytes", "ZFS ARC minimum size in bytes")
ZFS_ARC_HIT_RATIO = Gauge("truenas_zfs_arc_hit_ratio", "ZFS ARC cache hit ratio (0.0–1.0)")
ZFS_ARC_HITS_RATE = Gauge("truenas_zfs_arc_hits_per_second", "ZFS ARC hits per second (instantaneous snapshot from realtime API)")
ZFS_ARC_MISSES_RATE = Gauge("truenas_zfs_arc_misses_per_second", "ZFS ARC misses per second (instantaneous snapshot from realtime API)")

# ZFS ARC v25+ (from memory section in v25.10)
ZFS_ARC_FREE_MEMORY_BYTES = Gauge("truenas_zfs_arc_free_memory_bytes", "ZFS ARC free memory in bytes (v25+)")
ZFS_ARC_AVAILABLE_BYTES = Gauge("truenas_zfs_arc_available_bytes", "ZFS ARC available memory in bytes (v25+)")

# ZFS demand data stats (v25+)
ZFS_DEMAND_DATA_ACCESSES_RATE = Gauge("truenas_zfs_demand_data_accesses_per_second", "ZFS demand data accesses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_HITS_RATE = Gauge("truenas_zfs_demand_data_hits_per_second", "ZFS demand data hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_MISSES_RATE = Gauge("truenas_zfs_demand_data_misses_per_second", "ZFS demand data misses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_HIT_RATIO = Gauge("truenas_zfs_demand_data_hit_ratio", "ZFS demand data hit ratio (0.0-1.0)")
ZFS_DEMAND_DATA_IO_HIT_RATIO = Gauge("truenas_zfs_demand_data_io_hit_ratio", "ZFS demand data IO hit ratio (0.0-1.0)")
ZFS_DEMAND_DATA_MISS_RATIO = Gauge("truenas_zfs_demand_data_miss_ratio", "ZFS demand data miss ratio (0.0-1.0)")

# ZFS demand metadata stats (v25+)
ZFS_DEMAND_META_HITS_RATE = Gauge("truenas_zfs_demand_meta_hits_per_second", "ZFS demand metadata hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_MISSES_RATE = Gauge("truenas_zfs_demand_meta_misses_per_second", "ZFS demand metadata misses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_HIT_RATIO = Gauge("truenas_zfs_demand_meta_hit_ratio", "ZFS demand metadata hit ratio (0.0-1.0)")

# L2ARC cache stats (v25+)
ZFS_L2ARC_HITS_RATE = Gauge("truenas_zfs_l2arc_hits_per_second", "L2ARC cache hits per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_MISSES_RATE = Gauge("truenas_zfs_l2arc_misses_per_second", "L2ARC cache misses per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_HIT_RATIO = Gauge("truenas_zfs_l2arc_hit_ratio", "L2ARC cache hit ratio (0.0-1.0)")
ZFS_L2ARC_READ_BYTES_RATE = Gauge("truenas_zfs_l2arc_read_bytes_per_second", "L2ARC read bytes per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_WRITE_BYTES_RATE = Gauge("truenas_zfs_l2arc_write_bytes_per_second", "L2ARC write bytes per second (instantaneous snapshot from realtime API)")

# ZFS demand totals and I/O-hit sub-counters (v25+ realtime — previously missing)
ZFS_DEMAND_ACCESSES_RATE = Gauge("truenas_zfs_demand_accesses_per_second", "ZFS ARC total demand accesses per second (data + metadata, instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_IO_HITS_RATE = Gauge("truenas_zfs_demand_data_io_hits_per_second", "ZFS demand data I/O hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_ACCESSES_RATE = Gauge("truenas_zfs_demand_metadata_accesses_per_second", "ZFS demand metadata accesses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_IO_HITS_RATE = Gauge("truenas_zfs_demand_metadata_io_hits_per_second", "ZFS demand metadata I/O hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_IO_HIT_RATIO = Gauge("truenas_zfs_demand_metadata_io_hit_ratio", "ZFS demand metadata I/O hit ratio (0.0-1.0)")
ZFS_DEMAND_META_MISS_RATIO = Gauge("truenas_zfs_demand_metadata_miss_ratio", "ZFS demand metadata miss ratio (0.0-1.0)")
ZFS_L2ARC_ACCESSES_RATE = Gauge("truenas_zfs_l2arc_accesses_per_second", "ZFS L2ARC total accesses per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_MISS_RATIO = Gauge("truenas_zfs_l2arc_miss_ratio", "ZFS L2ARC miss ratio (0.0-1.0)")

# Pool real-time I/O (from reporting.realtime pools section — v25+)
POOL_REALTIME_READ_BYTES = Gauge("truenas_pool_realtime_read_bytes_per_second", "Pool read throughput in bytes/sec (instantaneous snapshot from realtime API)", ["pool"])
POOL_REALTIME_WRITE_BYTES = Gauge("truenas_pool_realtime_write_bytes_per_second", "Pool write throughput in bytes/sec (instantaneous snapshot from realtime API)", ["pool"])

# App/Container stats (from app.stats event in v25)
APP_CPU_PERCENT = Gauge("truenas_app_cpu_percent", "App container CPU usage percent (0 to 100)", ["app"])
APP_MEMORY_BYTES = Gauge("truenas_app_memory_bytes", "App container memory usage bytes", ["app"])
APP_NET_RX_BYTES_RATE = Gauge("truenas_app_net_rx_bytes_per_second", "App container network receive bytes/sec (instantaneous snapshot from realtime API)", ["app", "interface"])
APP_NET_TX_BYTES_RATE = Gauge("truenas_app_net_tx_bytes_per_second", "App container network transmit bytes/sec (instantaneous snapshot from realtime API)", ["app", "interface"])
APP_BLKIO_READ_BYTES = Gauge("truenas_app_blkio_read_bytes", "App container block I/O read bytes", ["app"])
APP_BLKIO_WRITE_BYTES = Gauge("truenas_app_blkio_write_bytes", "App container block I/O write bytes", ["app"])

# ---------------------------------------------------------------------------
# Pool vdev error counters (from pool.query topology/stats)
# ---------------------------------------------------------------------------
POOL_VDEV_READ_ERRORS = Gauge(
    "truenas_pool_vdev_read_errors",
    "Read errors on pool vdev since last scrub clear",
    ["pool", "vdev"],
)
POOL_VDEV_WRITE_ERRORS = Gauge(
    "truenas_pool_vdev_write_errors",
    "Write errors on pool vdev since last scrub clear",
    ["pool", "vdev"],
)
POOL_VDEV_CHECKSUM_ERRORS = Gauge(
    "truenas_pool_vdev_checksum_errors",
    "Checksum errors on pool vdev since last scrub clear",
    ["pool", "vdev"],
)

# ---------------------------------------------------------------------------
# SMB / NFS session metrics
# ---------------------------------------------------------------------------
SMB_SESSION_COUNT = Gauge("truenas_smb_session_count", "Number of active SMB sessions")
SMB_OPEN_FILE_COUNT = Gauge("truenas_smb_open_file_count", "Number of SMB open files")
SMB_CONNECTION_COUNT = Gauge("truenas_smb_connection_count", "Number of active SMB connections")
NFS_SERVER_STAT_OPS = Gauge("truenas_nfs_server_ops_per_second", "NFS server operations per second (instantaneous snapshot from realtime API)")

# ---------------------------------------------------------------------------
# GPU
# ---------------------------------------------------------------------------
GPU_COUNT = Gauge("truenas_gpu_count", "Number of GPU devices visible to the host")
GPU_INFO = Gauge(
    "truenas_gpu_info",
    "GPU device info — always 1; carry identifying labels",
    ["index", "model", "vendor", "pci_id"],
)

# ---------------------------------------------------------------------------
# JBOF (Just a Bunch of Flash) hardware
# ---------------------------------------------------------------------------
JBOF_COUNT = Gauge("truenas_jbof_count", "Number of JBOF enclosures connected")

# ---------------------------------------------------------------------------
# Active API sessions
# ---------------------------------------------------------------------------
AUTH_SESSIONS_ACTIVE = Gauge("truenas_auth_sessions_active", "Number of active authenticated API sessions")

# ---------------------------------------------------------------------------
# Additional host info from system.info
# ---------------------------------------------------------------------------
HOST_ECC_MEMORY = Gauge("truenas_host_ecc_memory", "1 if host RAM is ECC-protected")
HOST_CPU_MODEL = Gauge(
    "truenas_host_cpu_info",
    "Always 1; CPU model string in label",
    ["model"],
)
HOST_SYSTEM_INFO = Gauge(
    "truenas_host_system_info",
    "Always 1; hardware manufacturer/product labels from DMI",
    ["manufacturer", "product"],
)

# ---------------------------------------------------------------------------
# Disk extended info (from disk.query with extra fields)
# ---------------------------------------------------------------------------
DISK_ROTATIONAL = Gauge("truenas_disk_rotational", "1 if disk is rotational (HDD), 0 if SSD/NVMe", ["disk"])
DISK_SMART_ENABLED = Gauge("truenas_disk_smart_enabled", "1 if S.M.A.R.T. is enabled for disk", ["disk"])
DISK_INFO = Gauge("truenas_disk_info", "Disk identity info — always 1", ["disk", "model", "serial", "bus"])

# ---------------------------------------------------------------------------
# Pool scan detailed stats (from pool.query scan sub-object)
# ---------------------------------------------------------------------------
POOL_SCAN_ERRORS = Gauge("truenas_pool_scan_errors", "Errors found in last pool scan", ["pool"])
POOL_SCAN_BYTES_PROCESSED = Gauge("truenas_pool_scan_bytes_processed", "Bytes processed in last pool scan", ["pool"])
POOL_SCAN_BYTES_TOTAL = Gauge("truenas_pool_scan_bytes_total", "Total bytes to process in last pool scan", ["pool"])
POOL_SCAN_SECONDS_REMAINING = Gauge("truenas_pool_scan_seconds_remaining", "Estimated seconds remaining in active pool scan", ["pool"])
POOL_LAST_SCAN_TS = Gauge("truenas_pool_last_scan_timestamp_seconds", "Unix timestamp of last pool scan end", ["pool"])

# ---------------------------------------------------------------------------
# Exporter self-identification (v5)
# ---------------------------------------------------------------------------
EXPORTER_INFO = Gauge("truenas_exporter_info", "Exporter version info — always 1", ["version"])
EXPORTER_INFO.labels(version="5.1.0").set(1)

# Collector-level error counter (v5) — makes silent try/except failures visible
COLLECTOR_ERRORS_TOTAL = Counter(
    "truenas_collector_errors_total",
    "Total collector-level errors since exporter start",
    ["collector"],
)

# ---------------------------------------------------------------------------
# Pool scrub task scheduling (v5 — pool.scrub.query)
# ---------------------------------------------------------------------------
POOL_SCRUB_TASK_COUNT = Gauge("truenas_pool_scrub_task_count", "Number of configured pool scrub tasks")
POOL_SCRUB_TASK_ENABLED = Gauge("truenas_pool_scrub_task_enabled", "1 if scrub task is enabled", ["pool"])
POOL_SCRUB_TASK_STATE = Gauge("truenas_pool_scrub_task_state", "Scrub task last-run state as label", ["pool", "state"])
POOL_SCRUB_LAST_RUN_TS = Gauge("truenas_pool_scrub_last_run_timestamp_seconds", "Unix timestamp of last scrub task run", ["pool"])

# ---------------------------------------------------------------------------
# Snapshots (v5 — pool.snapshot.query)
# ---------------------------------------------------------------------------
SNAPSHOT_TOTAL_COUNT = Gauge("truenas_snapshot_count", "Total number of ZFS snapshots")
SNAPSHOT_OLDEST_TS = Gauge("truenas_snapshot_oldest_timestamp_seconds", "Unix timestamp of the oldest ZFS snapshot (0 if no snapshots)")

# ---------------------------------------------------------------------------
# SMART test results (v5 — smart.test.results)
# ---------------------------------------------------------------------------
SMART_TEST_LAST_RESULT = Gauge(
    "truenas_smart_test_last_result",
    "Last SMART test result — 1 = SUCCESS, 0 = FAILED",
    ["disk"],
)
SMART_TEST_LAST_TIMESTAMP = Gauge(
    "truenas_smart_test_last_timestamp_seconds",
    "Unix timestamp of last SMART test for disk",
    ["disk"],
)

# ---------------------------------------------------------------------------
# Pool resilver config (v5)
# ---------------------------------------------------------------------------
POOL_RESILVER_ENABLED = Gauge("truenas_pool_resilver_enabled", "1 if resilver priority scheduling is enabled")

# ---------------------------------------------------------------------------
# Cloud backup tasks (v5 — cloud_backup.query)
# ---------------------------------------------------------------------------
CLOUD_BACKUP_TASK_COUNT = Gauge("truenas_cloud_backup_task_count", "Number of configured cloud backup tasks")
CLOUD_BACKUP_TASK_ENABLED = Gauge("truenas_cloud_backup_task_enabled", "1 if cloud backup task is enabled", ["name"])
CLOUD_BACKUP_TASK_STATE = Gauge("truenas_cloud_backup_task_state", "Cloud backup task state as label", ["name", "state"])

# ---------------------------------------------------------------------------
# Cron jobs (v5 — cronjob.query)
# ---------------------------------------------------------------------------
CRONJOB_COUNT = Gauge("truenas_cronjob_count", "Number of configured cron jobs")
CRONJOB_ENABLED = Gauge("truenas_cronjob_enabled", "1 if cron job is enabled", ["name"])

# ---------------------------------------------------------------------------
# Disk in-use (v5 — disk.get_used)
# ---------------------------------------------------------------------------
DISK_IN_USE = Gauge("truenas_disk_in_use", "1 if disk is in use by a pool", ["disk"])

# ---------------------------------------------------------------------------
# DNS resolvers (v5 — dns.query)
# ---------------------------------------------------------------------------
DNS_RESOLVER_COUNT = Gauge("truenas_dns_resolver_count", "Number of configured DNS resolvers")

# ---------------------------------------------------------------------------
# Protocol configs (v5)
# ---------------------------------------------------------------------------
SMB_MULTICHANNEL_ENABLED = Gauge("truenas_smb_multichannel_enabled", "1 if SMB multichannel is enabled")
NFS_V4_ENABLED = Gauge("truenas_nfs_v4_enabled", "1 if NFSv4 is enabled")
NFS_SERVERS = Gauge("truenas_nfs_servers", "Number of NFS server threads configured")
SSH_ENABLED = Gauge("truenas_ssh_enabled", "1 if SSH service is enabled to start automatically")
SSH_PASSWORD_AUTH = Gauge("truenas_ssh_password_auth", "1 if SSH password authentication is enabled")
FTP_ENABLED = Gauge("truenas_ftp_enabled", "1 if FTP service is enabled to start automatically")
SNMP_ENABLED = Gauge("truenas_snmp_enabled", "1 if SNMP service is enabled to start automatically")

# ---------------------------------------------------------------------------
# System advanced/general config (v5)
# ---------------------------------------------------------------------------
CONSOLEMENU_ENABLED = Gauge("truenas_consolemenu_enabled", "1 if serial console menu is enabled")
SERIALCONSOLE_ENABLED = Gauge("truenas_serialconsole_enabled", "1 if serial console is enabled")
UI_HTTPS_PORT = Gauge("truenas_ui_https_port", "Web UI HTTPS port number")

# ---------------------------------------------------------------------------
# KMIP / support / systemdataset (v5)
# ---------------------------------------------------------------------------
KMIP_ENABLED = Gauge("truenas_kmip_enabled", "1 if KMIP key management is enabled")
SUPPORT_AVAILABLE = Gauge("truenas_support_available", "1 if proactive support is available")
SYSTEMDATASET_POOL = Gauge("truenas_systemdataset_pool", "System dataset pool as label", ["pool"])

# ---------------------------------------------------------------------------
# Users / groups / routes / tunables / privileges (v5)
# ---------------------------------------------------------------------------
LOCAL_USER_COUNT = Gauge("truenas_local_user_count", "Number of local user accounts")
LOCAL_GROUP_COUNT = Gauge("truenas_local_group_count", "Number of local groups")
STATIC_ROUTE_COUNT = Gauge("truenas_static_route_count", "Number of static routes")
TUNABLE_COUNT = Gauge("truenas_tunable_count", "Number of kernel tunables configured")
PRIVILEGE_COUNT = Gauge("truenas_privilege_count", "Number of RBAC privilege entries")

# ---------------------------------------------------------------------------
# iSCSI inventory (v5)
# ---------------------------------------------------------------------------
ISCSI_TARGET_COUNT = Gauge("truenas_iscsi_target_count", "Number of iSCSI targets")
ISCSI_PORTAL_COUNT = Gauge("truenas_iscsi_portal_count", "Number of iSCSI portals")
ISCSI_EXTENT_COUNT = Gauge("truenas_iscsi_extent_count", "Number of iSCSI extents")
ISCSI_INITIATOR_COUNT = Gauge("truenas_iscsi_initiator_count", "Number of iSCSI initiator groups")

# ---------------------------------------------------------------------------
# NVMe-oF extended (v5)
# ---------------------------------------------------------------------------
NVMET_HOST_COUNT = Gauge("truenas_nvmet_host_count", "Number of NVMe-oF allowed hosts")
NVMET_NAMESPACE_COUNT = Gauge("truenas_nvmet_namespace_count", "Number of NVMe-oF namespaces")

# ---------------------------------------------------------------------------
# Network config (v5)
# ---------------------------------------------------------------------------
NETWORK_HTTPPROXY_CONFIGURED = Gauge("truenas_network_httpproxy_configured", "1 if HTTP proxy is configured")

# ---------------------------------------------------------------------------
# Docker images / app volumes (v5)
# ---------------------------------------------------------------------------
DOCKER_IMAGE_COUNT = Gauge("truenas_docker_image_count", "Number of Docker container images")

# ---------------------------------------------------------------------------
# Replication / reporting config (v5)
# ---------------------------------------------------------------------------
REPLICATION_MAX_PARALLEL = Gauge("truenas_replication_max_parallel", "Maximum parallel replication tasks allowed")
REPORTING_EXPORTER_COUNT = Gauge("truenas_reporting_exporter_count", "Number of reporting exporter plugins")
REPORTING_ENABLED = Gauge("truenas_reporting_enabled", "1 if the reporting service is enabled to start automatically")

# ---------------------------------------------------------------------------
# IOMMU / 2FA / mail / alerts (v5)
# ---------------------------------------------------------------------------
IOMMU_ENABLED = Gauge("truenas_iommu_enabled", "1 if IOMMU/PCI passthrough is enabled")
TWOFACTOR_ENABLED = Gauge("truenas_2fa_enabled", "1 if two-factor authentication is enabled")
MAIL_CONFIGURED = Gauge("truenas_mail_configured", "1 if outgoing email (SMTP) is configured")
ALERTSERVICE_COUNT = Gauge("truenas_alertservice_count", "Number of alert notification services")
ALERTSERVICE_ENABLED = Gauge("truenas_alertservice_enabled", "1 if alert service is enabled", ["name", "type"])

# ---------------------------------------------------------------------------
# Init/shutdown scripts / keychain / system global ID (v5)
# ---------------------------------------------------------------------------
INITSHUTDOWNSCRIPT_COUNT = Gauge("truenas_initshutdownscript_count", "Number of init/shutdown scripts")
KEYCHAIN_CREDENTIAL_COUNT = Gauge("truenas_keychain_credential_count", "Number of SSH/keychain credentials")
SYSTEM_GLOBAL_ID = Gauge("truenas_system_global_id", "Always 1; system global unique ID as label", ["global_id"])


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class JsonRpcError(RuntimeError):
    """Raised when TrueNAS JSON-RPC responds with an error object."""


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

@dataclass
class Config:
    ws_url: str
    api_key: str
    interval_seconds: int
    timeout_seconds: int
    verify_tls: bool
    exporter_port: int
    auto_discover_methods: bool
    query_limit: int
    max_method_calls: int
    max_list_items: int
    max_depth: int
    max_entity_calls: int
    max_datasets: int
    extra_methods: list[str]
    exclude_methods: list[str]
    filesystem_paths: list[str]
    enable_filesystem_listdir: bool
    enable_event_streams: bool
    enable_dataset_metrics: bool
    enable_task_metrics: bool
    enable_ipmi_metrics: bool
    event_interval_seconds: int
    event_read_timeout_seconds: int
    event_subscriptions: list[str]
    scrape_all_metrics: bool


# ---------------------------------------------------------------------------
# WebSocket JSON-RPC client
# ---------------------------------------------------------------------------

class JsonRpcWsClient:
    def __init__(self, ws_url: str, timeout_seconds: int, verify_tls: bool) -> None:
        self._ws_url = ws_url
        self._timeout_seconds = timeout_seconds
        self._verify_tls = verify_tls
        self._id = 0
        self._ws: WebSocket | None = None

    def __enter__(self) -> "JsonRpcWsClient":
        sslopt: dict[str, Any] | None = None
        if self._ws_url.startswith("wss://"):
            if self._verify_tls:
                sslopt = {"cert_reqs": ssl.CERT_REQUIRED}
            else:
                # Explicitly disable both cert validation AND hostname checking.
                # Without check_hostname=False, Python 3.12 may still raise even
                # when cert_reqs=CERT_NONE on some SSL context configurations.
                sslopt = {
                    "cert_reqs": ssl.CERT_NONE,
                    "check_hostname": False,
                }
        self._ws = create_connection(
            self._ws_url,
            timeout=self._timeout_seconds,
            sslopt=sslopt,
        )
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        if self._ws is not None:
            try:
                self._ws.close()
            except Exception:
                LOG.debug("Failed to close websocket cleanly", exc_info=True)
        self._ws = None

    def call(self, method: str, params: list[Any] | None = None) -> Any:
        if self._ws is None:
            raise RuntimeError("WebSocket is not connected")
        self._id += 1
        req_id = self._id
        payload = {
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params if params is not None else [],
        }
        self._ws.send(json.dumps(payload))
        # Bound the recv loop: if the server sends unsolicited push messages (e.g.
        # collection_update events on a shared connection) we skip them, but we
        # must not spin forever — bail after _MAX_STRAY_MESSAGES discards.
        for _ in range(_MAX_STRAY_MESSAGES):
            raw = self._ws.recv()
            msg = json.loads(raw)
            if msg.get("id") != req_id:
                LOG.debug(
                    "call(%s): discarding stray WS message id=%s (waiting for id=%s)",
                    method, msg.get("id"), req_id,
                )
                continue
            if "error" in msg:
                raise JsonRpcError(f"{method} failed: {msg['error']}")
            return msg.get("result")
        raise JsonRpcError(
            f"{method}: response not received after {_MAX_STRAY_MESSAGES} stray messages"
        )

    def recv_json(self) -> dict[str, Any]:
        if self._ws is None:
            raise RuntimeError("WebSocket is not connected")
        raw = self._ws.recv()
        return json.loads(raw)


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return None
    if isinstance(value, dict):
        for key in ("value", "parsed", "rawvalue"):
            nested = _as_float(value.get(key))
            if nested is not None:
                return nested
    return None


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on", "running", "up"}
    # A non-empty dict or list is truthy — handles session objects returned by
    # auth.login_with_api_key in TrueNAS 25.x
    if isinstance(value, (dict, list)):
        return bool(value)
    return False


def _str_label(value: Any, fallback: str = "unknown") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text or fallback


def _normalize_core_label(value: Any) -> str:
    text = _str_label(value)
    match = re.search(r"(\d+)$", text)
    return match.group(1) if match else text


def _extract_labeled_numeric_series(
    payload: Any,
    *,
    label_keys: tuple[str, ...] = ("core", "cpu", "id", "name"),
    value_keys: tuple[str, ...] = ("value",),
    normalize_label: bool = False,
) -> dict[tuple[str, ...], float]:
    series: dict[tuple[str, ...], float] = {}

    if isinstance(payload, list):
        for idx, item in enumerate(payload):
            if isinstance(item, dict):
                label = None
                for label_key in label_keys:
                    candidate = item.get(label_key)
                    if candidate is not None:
                        label = candidate
                        break
                if label is None:
                    label = idx

                value = None
                for value_key in value_keys:
                    value = _as_float(item.get(value_key))
                    if value is not None:
                        break
            else:
                label = idx
                value = _as_float(item)

            if value is None:
                continue

            label_text = _normalize_core_label(label) if normalize_label else _str_label(label)
            series[(label_text,)] = value
        return series

    if isinstance(payload, dict):
        for raw_label, raw_value in payload.items():
            value = None
            if isinstance(raw_value, dict):
                for value_key in value_keys:
                    value = _as_float(raw_value.get(value_key))
                    if value is not None:
                        break
            if value is None:
                value = _as_float(raw_value)
            if value is None:
                continue

            label_text = _normalize_core_label(raw_label) if normalize_label else _str_label(raw_label)
            series[(label_text,)] = value

    return series


def _parse_ts(value: Any) -> float | None:
    """Convert various TrueNAS datetime representations to a Unix timestamp."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, dict):
        # {"$date": milliseconds_since_epoch}
        ms = value.get("$date")
        if ms is not None:
            try:
                return float(ms) / 1000.0
            except (TypeError, ValueError):
                pass
    if isinstance(value, str):
        if value in {"Never", "N/A", "None", ""}:
            return None
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.timestamp()
        except ValueError:
            pass
    return None


def _cert_days_to_expiry(until: Any) -> int | None:
    """Return days until certificate expiry; negative means already expired."""
    ts = _parse_ts(until)
    if ts is None:
        return None
    try:
        expiry_dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        delta = expiry_dt - datetime.now(tz=timezone.utc)
        return delta.days
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Method safety filters
# ---------------------------------------------------------------------------

SAFE_ALLOW_RE = re.compile(
    r"(\.query$|\.status$|\.config$|\.info$|\.summary$|\.version$|\.state$"
    r"|\.choices$|\.graphs$|\.temperatures$|\.sessions$|\.client_count$"
    r"|\.get_data$|\.get_|\.list$|\.list_|\.available$|\.available_"
    r"|\.is_|\.has_|\.feature_|\.nvidia_present$|\.licensed$|\.flags$"
    r"|\.details$|\.reachable$)"
)
SAFE_DENY_RE = re.compile(
    r"(^|\.)(create|update|delete|destroy|remove|start|stop|restart|reboot"
    r"|shutdown|wipe|run|sync|upload|download|set|reset|attach|detach|replace"
    r"|promote|rollback|clone|import|export|unlock|lock|change_key|restore"
    r"|control|clear|abort|renew|terminate|save|commit|checkin|leave|reapply"
    r"|test|convert|pull|redeploy|upgrade|manual|accept|setup|send"
    r"|get_instance)(\.|$)"   # get_instance ALWAYS requires a mandatory entity ID
)

# Methods that require mandatory params (entity ID, credentials, path, etc.).
# These are NEVER called via auto-discovery.  This is the exhaustive blocklist
# derived from observed JsonRpcError failures; extend as needed.
REQUIRES_ENTITY_PARAM: set[str] = {
    # ── VM per-entity (handled in _collect_vm_metrics with real IDs) ──
    "vm.status",
    "vm.get_instance",
    "vm.get_memory_usage",
    "vm.get_vm_memory_info",
    "vm.get_console",            # requires vm_id
    "vm.get_display_devices",    # requires vm_id
    "vm.get_display_web_uri",    # requires vm_id
    # ── App per-entity ──
    "app.config",                # requires app name
    "app.get_instance",
    "app.outdated_docker_images",
    "app.rollback_versions",
    # ── Catalog ──
    "catalog.get_app_details",   # requires catalog item name
    # ── Cloud Backup — require backup task ID ──
    "cloud_backup.list_snapshot_directory",
    "cloud_backup.list_snapshots",
    # ── CloudSync — require credential ID or path ──
    "cloudsync.list_buckets",
    "cloudsync.list_directory",
    # ── Device ──
    "device.get_info",           # requires device type dict (e.g. {"type": "DISK"})
    # ── Disk — require disk name list (disk.temperatures works; these don't) ──
    "disk.temperature_agg",      # requires explicit list of disk names
    "disk.temperature_alerts",   # requires explicit list of disk names
    # ── Filesystem ──
    "filesystem.statfs",         # requires a path argument
    # ── Group ──
    "group.get_group_obj",       # requires group identifier
    "group.has_password_enabled_user",  # requires group id
    # ── IPMI ──
    "ipmi.lan.query",            # requires channel number
    # ── iSCSI per-entity ──
    "iscsi.extent.disk_choices",
    # ── Pool ──
    "pool.is_upgraded",          # requires pool id
    "pool.dataset.get_quota",    # requires dataset path + quota type
    # ── FC per-entity ──
    "fc.fc_host.get_instance",
    "fcport.get_instance",
    # ── NVMe-oF per-entity ──
    "nvmet.host.get_instance",
    "nvmet.namespace.get_instance",
    "nvmet.port.get_instance",
    "nvmet.subsys.get_instance",
    "nvmet.host_subsys.get_instance",
    "nvmet.port_subsys.get_instance",
    # ── Replication ──
    "replication.list_datasets", # requires replication task id
    # ── Reporting (need explicit graph name list) ──
    "reporting.get_data",
    "reporting.netdata_get_data",
    # ── Route ──
    "route.ipv4gw_reachable",    # failing on this TrueNAS version (API changed)
    # ── System ──
    "system.feature_enabled",    # requires feature name string
    "system.security.info",      # method removed/renamed in this TrueNAS version
    # ── TN Connect ──
    "tn_connect.get_registration_uri",  # requires params
    # ── Audit ──
    "audit.query",               # requires specific filter params; can return huge data
    # ── User ──
    "user.get_user_obj",         # requires username/uid
    # ── VMware ──
    "vmware.get_datastores",
    "vmware.get_instance",
    "vmware.match_datastores_with_snapshots",
    # ── VM device ──
    "vm.device.get_instance",    # requires device id
    "vm.device.convert",         # requires device id
}

# Entire API namespaces that require external credentials or licensed features.
# Any method whose dotted prefix matches is skipped by _is_safe_read_method().
DENY_NAMESPACE_PREFIXES: tuple[str, ...] = (
    "vmware.",   # requires VMware vCenter credentials in TrueNAS
    "ec2.",      # AWS/cloud integrations
)

BASE_METHODS: list[str] = [
    # System — state/info/ready are called explicitly in scrape_once and their
    # results are injected into the result cache; listing them here still lets
    # the generic extractor walk the full response tree.
    "system.state",
    "system.info",
    "system.ready",
    # system.security.info intentionally omitted — it is in REQUIRES_ENTITY_PARAM
    # (method removed/renamed on TrueNAS 25.x) so it would always be blocked by
    # _is_safe_read_method(); keeping it here was dead, misleading code.
    "system.reboot.info",               # pending reboot detection
    # Network
    "network.general.summary",
    # route.ipv4gw_reachable removed — API returns JsonRpcError on this TrueNAS version
    "route.system_routes",
    # Updates
    "update.status",
    # Pools & disks
    "pool.query",
    "disk.query",
    "disk.details",                     # serial, model, bus, etc.
    "disk.temperatures",
    # disk.temperature_agg and disk.temperature_alerts require a list of disk names
    # as a mandatory param — they are called correctly in _collect_disk_metrics()
    # with actual disk names from disk.query. Do NOT put them here.
    # Interfaces
    "interface.query",
    # Services
    "service.query",
    # Alerts
    "alert.list",
    # Jobs — limit param is now applied in _auto_params to prevent huge payloads
    "core.get_jobs",
    # NFS
    "nfs.client_count",
    "nfs.get_nfs3_clients",
    "nfs.get_nfs4_clients",
    # iSCSI
    "iscsi.global.client_count",
    "iscsi.global.sessions",
    # Docker / Apps
    "docker.status",
    "docker.config",
    "docker.list_backups",
    "docker.nvidia_present",
    "docker.network.query",
    "app.query",
    "app.image.dockerhub_rate_limit",
    # Hardware
    "hardware.virtualization.variant",
    # Reporting (sampled via dedicated method, listed here for discovery)
    "reporting.graphs",
    "reporting.netdata_graphs",
    # VMs
    "vm.query",
    "vm.get_available_memory",
    "vm.get_vmemory_in_use",
    # ZFS resources (ARC, quota, etc.)
    "zfs.resource.query",
    # TrueNAS identity
    "truenas.is_production",
    "truenas.is_ix_hardware",
    "truenas.managed_by_truecommand",       # fleet management context
    # HA failover (no-op on non-Enterprise; returns empty list)
    "failover.disabled.reasons",
    # Directory services
    "directoryservices.status",
    # System extras
    "system.product_type",                  # SCALE / ENTERPRISE / CORE
    "system.version_short",                 # clean "25.10.2" version string
    "system.host_id",                       # stable UUID across reboots
    "system.boot_id",                       # changes each boot — exporter tracks changes
    # Update extras
    "update.available_versions",            # actual version names available to upgrade to
    # Boot environments
    "boot.environment.query",               # BE count, active, keep flags
    # VM/Virtualization extras
    "vm.supports_virtualization",           # KVM/hardware virt gate
    "vm.maximum_supported_vcpus",           # capacity planning
    "vm.virtualization_details",            # CPU flags, nested virt
    # iSCSI protocol feature flags
    "iscsi.global.alua_enabled",            # ALUA (HA iSCSI) status
    "iscsi.global.iser_enabled",            # iSER/RDMA high-perf iSCSI
    # Fibre Channel (already succeeds per CSV data)
    "fcport.status",                        # FC port operational status
    "fc.fc_host.query",                     # FC HBA adapter inventory
    # NVMe-oF (already succeeds per CSV data)
    "nvmet.global.sessions",               # active NVMe-oF session count
    "nvmet.global.config",                 # NVMe-oF global config
    "nvmet.subsys.query",                  # NVMe-oF subsystem inventory
    "nvmet.port.query",                    # NVMe-oF port inventory
    # App extras
    "app.available_space",                  # bytes available for new app installs
    # sharing.webshare.query excluded — only exists when WebShare is configured;
    # returns JsonRpcError on systems where it hasn't been set up. The dedicated
    # _collect_app_extras() already handles it gracefully with try/except.
    # Network extras
    "interface.has_pending_changes",        # uncommitted network config flag
    "interface.checkin_waiting",            # seconds until auto-rollback
    # Pool extras
    "pool.get_disks",                      # which disks belong to which pool
    # IPMI extras
    "ipmi.lan.channels",                   # IPMI LAN channel list
    # UPS
    "ups.config",                          # UPS config (mode, driver, battery status)
    # Catalog
    "catalog.trains",                      # app catalog train health
    # v4 additions - Security / FIPS
    "system.security.info.fips_available",  # FIPS availability (v25+)
    "system.security.info.fips_enabled",   # FIPS enabled status (v25+)
    # v4 additions - TrueNAS identity
    "truenas.get_chassis_hardware",        # chassis model string
    # v4 additions - Cloud management
    "tn_connect.config",                   # TrueNAS Connect (cloud management) status
    "truecommand.config",                  # TrueCommand full status enum
    # v4 additions - Audit
    "audit.config",                        # Audit dataset space and quotas
    # ── v5 additions ──
    # Scrub scheduling
    "pool.scrub.query",                    # scrub task inventory + state
    # Snapshots (NOTE: can be large — limited by query_limit)
    "pool.snapshot.query",                 # global snapshot inventory
    # Resilver config
    "pool.resilver.config",                # resilver priority scheduling
    # Cloud backup tasks
    "cloud_backup.query",                  # cloud backup task inventory
    # Cron jobs
    "cronjob.query",                       # cron job inventory
    # Disk usage
    "disk.get_used",                       # which disks are in use
    # DNS
    "dns.query",                           # DNS resolver config
    # Protocol configs
    "smb.config",                          # SMB server config
    "nfs.config",                          # NFS server config
    "ssh.config",                          # SSH daemon config
    "ftp.config",                          # FTP config
    "snmp.config",                         # SNMP agent config
    # System configs
    "system.advanced.config",              # advanced system settings
    "system.general.config",               # UI/general settings
    "system.global.id",                    # system global unique ID
    # KMIP / support
    "kmip.config",                         # KMIP key management
    "support.is_available",                # proactive support availability
    # System dataset
    "systemdataset.config",                # system dataset pool assignment
    # User / group / privilege
    "user.query",                          # local user inventory
    "group.query",                         # local group inventory
    "privilege.query",                     # RBAC privilege entries
    # Routes / tunables
    "staticroute.query",                   # static routes
    "tunable.query",                       # kernel tunables
    # iSCSI inventory
    "iscsi.target.query",                  # iSCSI targets
    "iscsi.portal.query",                  # iSCSI portals
    "iscsi.extent.query",                  # iSCSI extents
    "iscsi.initiator.query",               # iSCSI initiator groups
    # NVMe-oF extended
    "nvmet.host.query",                    # NVMe-oF allowed hosts
    "nvmet.namespace.query",               # NVMe-oF namespaces
    # Network config
    "network.configuration.config",        # hostname, domain, proxy
    # Docker images
    "app.image.query",                     # Docker image inventory
    # Replication / reporting config
    "replication.config.config",           # replication global config
    "reporting.exporters.query",           # reporting exporter plugins
    "reporting.config",                    # reporting/netdata config
    # Security posture
    "auth.twofactor.config",               # 2FA configuration
    # Email / alert services
    "mail.config",                         # outgoing email config
    "alertservice.query",                  # alert notification services
    "alertclasses.config",                 # alert class policies
    # Init/shutdown scripts
    "initshutdownscript.query",            # init/shutdown scripts
    # Keychain credentials
    "keychaincredential.query",            # SSH keypairs / credentials
    # Kerberos
    "kerberos.config",                     # kerberos realm config
    # Dataset details (richer than pool.dataset.query)
    "pool.dataset.details",                # extended dataset info
]


# ---------------------------------------------------------------------------
# Main exporter class
# ---------------------------------------------------------------------------

class TrueNASExporter:
    def __init__(self, config: Config) -> None:
        self.config = config
        self._lock = threading.Lock()
        self._event_thread: threading.Thread | None = None
        self._all_methods_discovered = False
        self._event_metric_series: dict[Any, set[tuple[str, ...]]] = {}
        # Tracks the last-seen boot ID so we can increment the reboot counter
        # when it changes, rather than exposing a UUID-valued label.
        self._last_boot_id: str | None = None

    # ------------------------------------------------------------------
    # Internal utilities
    # ------------------------------------------------------------------

    def _normalize_path(self, path: str) -> str:
        # Use module-level pre-compiled regex — avoids recompiling on every
        # recursive call inside the generic extractor.
        return _PATH_NORMALIZE_RE.sub("_", path)[:200]

    def _status_like(self, value: str) -> bool:
        """Return True only for the known-good status string set.

        The old isupper() fallback matched any all-caps word (CPU, ARC, NFS, OK …)
        which caused unbounded METHOD_STATUS_VALUE / EVENT_STATUS_VALUE cardinality.
        """
        if not value or len(value) > 40:
            return False
        return value.upper() in {
            "READY", "BOOTING", "SHUTTING_DOWN", "RUNNING", "STOPPED",
            "UP", "DOWN", "UNKNOWN", "HEALTHY", "DEGRADED", "FAULTED",
            "SUCCESS", "FAILED", "UNAVAILABLE", "UP_TO_DATE", "PENDING",
            "ERROR", "WAITING", "ACTIVE", "PASSIVE", "OFFLINE", "ONLINE",
        }

    def _collector_error(self, name: str, message: str) -> None:
        COLLECTOR_ERRORS_TOTAL.labels(collector=name).inc()
        LOG.debug(message, exc_info=True)

    def _event_interval_seconds(self) -> int:
        return max(2, self.config.event_interval_seconds)

    def _format_event_subscription(self, event: str) -> str:
        if event in _INTERVAL_EVENT_SUBSCRIPTIONS:
            interval = self._event_interval_seconds()
            if interval != 2:
                return f'{event}:{{"interval": {interval}}}'
        return event

    def _replace_event_metric_series(
        self,
        metric: Any,
        series: dict[tuple[str, ...], float],
        series_key: Any | None = None,
    ) -> None:
        key = metric if series_key is None else series_key
        previous = self._event_metric_series.get(key, set())
        current = set(series)

        for label_values in previous - current:
            try:
                metric.remove(*label_values)
            except Exception:
                LOG.debug("Failed removing stale event series from %s", getattr(metric, "_name", metric), exc_info=True)

        for label_values, value in series.items():
            metric.labels(*label_values).set(value)

        self._event_metric_series[key] = current

    def _call(self, client: JsonRpcWsClient, method: str, params: list[Any] | None = None) -> Any:
        started = time.time()
        try:
            result = client.call(method, params)
            API_CALL_SUCCESS.labels(method=method).set(1)
            API_CALL_DURATION.labels(method=method).set(max(0.0, time.time() - started))
            return result
        except Exception as exc:
            API_CALL_SUCCESS.labels(method=method).set(0)
            API_CALL_DURATION.labels(method=method).set(max(0.0, time.time() - started))
            # Counter: increments on each error; never creates stale zero-value series.
            API_CALL_ERRORS_TOTAL.labels(method=method, error_type=type(exc).__name__).inc()
            raise

    def _call_query_with_fallback(
        self,
        client: JsonRpcWsClient,
        method: str,
        preferred_options: dict[str, Any],
    ) -> Any:
        try:
            return self._call(client, method, [[], preferred_options])
        except Exception:
            LOG.debug("Falling back to bare call for %s", method)
            return self._call(client, method, [])

    def _query_count(
        self,
        client: JsonRpcWsClient,
        method: str,
        filters: list[Any] | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> int:
        options: dict[str, Any] = {"count": True}
        if extra_options:
            options.update(extra_options)

        result = self._call(client, method, [filters or [], options])
        count = _as_float(result)
        if count is None:
            raise TypeError(f"{method} count query returned non-numeric result: {type(result).__name__}")
        return int(count)

    def _extract_snapshot_creation_timestamp(self, snapshot: Any) -> float | None:
        if not isinstance(snapshot, dict):
            return None

        ts = _as_float(snapshot.get("creation_parsed") or snapshot.get("creation"))
        if ts is not None:
            return ts

        properties = snapshot.get("properties")
        if isinstance(properties, dict):
            return _as_float(properties.get("creation"))

        return None

    def _export_alert_metrics(self, alerts_raw: Any) -> None:
        alert_list = alerts_raw if isinstance(alerts_raw, list) else []

        ALERT_COUNT_BY_LEVEL.clear()
        ALERT_COUNT_BY_SOURCE.clear()
        ALERT_COUNT_BY_CLASS.clear()
        ALERT_COUNT_BY_NODE.clear()
        ALERT_LAST_OCCURRENCE_TS.clear()

        ALERT_COUNT.set(len(alert_list))

        level_counts: dict[str, int] = {}
        source_counts: dict[str, int] = {}
        class_counts: dict[tuple[str, str], int] = {}
        node_counts: dict[str, int] = {}
        last_occurrence_by_level: dict[str, float] = {}
        dismissed_count = 0
        one_shot_count = 0
        oldest_ts: float | None = None

        for alert in alert_list:
            if not isinstance(alert, dict):
                continue

            level = _str_label(alert.get("level"), "UNKNOWN").upper()
            source = _str_label(alert.get("source"), "unknown")
            klass = _str_label(alert.get("klass"), "unknown")
            node = _str_label(alert.get("node"), "unknown")

            level_counts[level] = level_counts.get(level, 0) + 1
            source_counts[source] = source_counts.get(source, 0) + 1
            class_counts[(klass, level)] = class_counts.get((klass, level), 0) + 1
            node_counts[node] = node_counts.get(node, 0) + 1

            if _as_bool(alert.get("dismissed")):
                dismissed_count += 1
            if _as_bool(alert.get("one_shot")):
                one_shot_count += 1

            created_ts = _parse_ts(alert.get("datetime"))
            if created_ts is not None:
                oldest_ts = created_ts if oldest_ts is None else min(oldest_ts, created_ts)

            last_occurrence_ts = _parse_ts(alert.get("last_occurrence"))
            if last_occurrence_ts is not None:
                last_occurrence_by_level[level] = max(
                    last_occurrence_by_level.get(level, last_occurrence_ts),
                    last_occurrence_ts,
                )

        for level, count in level_counts.items():
            ALERT_COUNT_BY_LEVEL.labels(level=level).set(count)
        for source, count in source_counts.items():
            ALERT_COUNT_BY_SOURCE.labels(source=source).set(count)
        for (klass, level), count in class_counts.items():
            ALERT_COUNT_BY_CLASS.labels(klass=klass, level=level).set(count)
        for node, count in node_counts.items():
            ALERT_COUNT_BY_NODE.labels(node=node).set(count)
        for level, ts in last_occurrence_by_level.items():
            ALERT_LAST_OCCURRENCE_TS.labels(level=level).set(ts)

        ALERT_DISMISSED_COUNT.set(dismissed_count)
        ALERT_ONE_SHOT_COUNT.set(one_shot_count)
        ALERT_OLDEST_TS.set(oldest_ts if oldest_ts is not None else 0)

    def _collect_job_metrics(self, client: JsonRpcWsClient) -> None:
        active_states = ("WAITING", "RUNNING")

        JOB_ACTIVE_COUNT_BY_STATE.clear()
        JOB_ACTIVE_COUNT_BY_METHOD.clear()
        JOB_OLDEST_ACTIVE_TS.clear()
        JOB_PROGRESS_PERCENT.clear()

        state_counts: dict[str, int] = {}
        total_active = 0

        for state in active_states:
            try:
                count = self._query_count(client, "core.get_jobs", [["state", "=", state]])
            except Exception:
                self._collector_error("jobs", f"core.get_jobs count failed for state={state}")
                return

            state_counts[state] = count
            total_active += count
            JOB_ACTIVE_COUNT_BY_STATE.labels(state=state).set(count)

        JOB_ACTIVE_COUNT.set(total_active)
        JOB_ABORTABLE_ACTIVE_COUNT.set(0)
        JOB_TRANSIENT_ACTIVE_COUNT.set(0)

        if total_active == 0:
            return

        detail_limit = max(self.config.query_limit, total_active)

        try:
            jobs = self._call(
                client,
                "core.get_jobs",
                [
                    [["state", "in", list(active_states)]],
                    {
                        "limit": detail_limit,
                        "select": [
                            "method",
                            "state",
                            "abortable",
                            "transient",
                            "time_started",
                            ["progress.percent", "progress_percent"],
                        ],
                    },
                ],
            )
        except Exception:
            self._collector_error("jobs", "core.get_jobs detail query failed")
            return

        if not isinstance(jobs, list):
            return

        method_state_counts: dict[tuple[str, str], int] = {}
        oldest_by_state: dict[str, float] = {}
        progress_by_method: dict[str, float] = {}
        abortable_count = 0
        transient_count = 0

        for job in jobs:
            if not isinstance(job, dict):
                continue

            method = _str_label(job.get("method"), "unknown")
            state = _str_label(job.get("state"), "UNKNOWN").upper()
            if state not in active_states:
                continue

            method_state_counts[(method, state)] = method_state_counts.get((method, state), 0) + 1

            if _as_bool(job.get("abortable")):
                abortable_count += 1
            if _as_bool(job.get("transient")):
                transient_count += 1

            started_ts = _parse_ts(job.get("time_started"))
            if started_ts is not None:
                current = oldest_by_state.get(state)
                oldest_by_state[state] = started_ts if current is None else min(current, started_ts)

            if state == "RUNNING":
                progress = _as_float(job.get("progress_percent"))
                if progress is not None:
                    progress_by_method[method] = max(progress_by_method.get(method, progress), progress)

        for (method, state), count in method_state_counts.items():
            JOB_ACTIVE_COUNT_BY_METHOD.labels(method=method, state=state).set(count)
        for state, ts in oldest_by_state.items():
            JOB_OLDEST_ACTIVE_TS.labels(state=state).set(ts)
        for method, progress in progress_by_method.items():
            JOB_PROGRESS_PERCENT.labels(method=method).set(progress)

        JOB_ABORTABLE_ACTIVE_COUNT.set(abortable_count)
        JOB_TRANSIENT_ACTIVE_COUNT.set(transient_count)

    def _query_service_enable_map(
        self,
        client: JsonRpcWsClient,
        service_names: tuple[str, ...],
    ) -> dict[str, bool]:
        ordered_names: list[str] = []
        seen: set[str] = set()
        for name in service_names:
            if name and name not in seen:
                ordered_names.append(name)
                seen.add(name)

        if not ordered_names:
            return {}

        services = self._call(client, "service.query", [[[
            "service", "in", ordered_names,
        ]], {
            "extra": {"include_state": False},
            "limit": len(ordered_names),
            "select": ["service", "enable"],
        }])

        enabled_by_service: dict[str, bool] = {}
        if isinstance(services, list):
            for svc in services:
                if not isinstance(svc, dict):
                    continue
                name = svc.get("service") or svc.get("name")
                if isinstance(name, str) and name:
                    enabled_by_service[name] = _as_bool(svc.get("enable"))

        return enabled_by_service

    def _is_safe_read_method(self, method: str) -> bool:
        if method in self.config.exclude_methods:
            return False
        # Hard-blocked individual methods (require entity IDs or credentials)
        if method in REQUIRES_ENTITY_PARAM:
            return False
        # Hard-blocked namespaces (require external credentials / licensed features)
        if method.startswith(DENY_NAMESPACE_PREFIXES):
            return False
        if method.startswith("filesystem."):
            return False
        if method.startswith("auth.") and method not in {"auth.me", "auth.sessions"}:
            return False
        if SAFE_DENY_RE.search(method):
            return False
        if SAFE_ALLOW_RE.search(method):
            return True
        if method in BASE_METHODS or method in self.config.extra_methods:
            return True
        return False

    def _auto_params(self, method: str) -> list[Any]:
        if method.endswith(".query"):
            return [[], {"limit": self.config.query_limit}]
        if method in {"nfs.get_nfs3_clients", "nfs.get_nfs4_clients",
                      "iscsi.global.sessions", "route.system_routes",
                      # core.get_jobs can return thousands of records on busy systems;
                      # apply the same query_limit guard used for .query methods.
                      "core.get_jobs"}:
            return [[], {"limit": self.config.query_limit}]
        if method == "app.query":
            return [[], {"limit": self.config.query_limit, "select": [
                "name",
                "state",
                "upgrade_available",
                "image_updates_available",
                "custom_app",
                "migrated",
                "active_workloads",
            ]}]
        if method in {"reporting.graph", "reporting.netdata_graph"}:
            return ["cpu", {"unit": "HOURLY"}]
        return []

    def _safe_call_auto(self, client: JsonRpcWsClient, method: str) -> Any | None:
        params = self._auto_params(method)
        try:
            return self._call(client, method, params)
        except Exception:
            if method.endswith(".query"):
                try:
                    return self._call(client, method, [])
                except Exception:
                    COLLECTOR_ERRORS_TOTAL.labels(collector="auto_discovery").inc()
                    return None
            COLLECTOR_ERRORS_TOTAL.labels(collector="auto_discovery").inc()
            return None

    def _discover_methods(self, client: JsonRpcWsClient) -> list[str]:
        discovered: list[str] = []
        if self.config.auto_discover_methods:
            methods = self._safe_call_auto(client, "core.get_methods")
            if isinstance(methods, dict):
                for name in methods.keys():
                    if isinstance(name, str) and self._is_safe_read_method(name):
                        discovered.append(name)

        ordered: list[str] = []
        seen: set[str] = set()

        for method in BASE_METHODS + self.config.extra_methods:
            if self._is_safe_read_method(method) and method not in seen:
                ordered.append(method)
                seen.add(method)

        for method in sorted(discovered):
            if method not in seen:
                ordered.append(method)
                seen.add(method)

        return ordered[: self.config.max_method_calls]

    # ------------------------------------------------------------------
    # Generic metric extraction
    # ------------------------------------------------------------------

    def _extract_generic_metrics(self, method: str, value: Any, path: str, depth: int) -> None:
        if depth > self.config.max_depth:
            return
        metric_path = self._normalize_path(path)

        if isinstance(value, bool):
            METHOD_BOOLEAN_VALUE.labels(method=method, path=metric_path).set(1 if value else 0)
            return

        numeric_value = _as_float(value)
        if numeric_value is not None and not isinstance(value, str):
            METHOD_NUMERIC_VALUE.labels(method=method, path=metric_path).set(numeric_value)
            return

        if isinstance(value, str):
            float_value = _as_float(value)
            if float_value is not None:
                METHOD_NUMERIC_VALUE.labels(method=method, path=metric_path).set(float_value)
                return
            status_value = value.strip().upper()[:60]
            if self._status_like(status_value):
                METHOD_STATUS_VALUE.labels(method=method, path=metric_path, status=status_value).set(1)
            return

        if isinstance(value, list):
            METHOD_LIST_LENGTH.labels(method=method, path=metric_path).set(len(value))
            for index, item in enumerate(value[: self.config.max_list_items]):
                self._extract_generic_metrics(method, item, f"{path}[{index}]", depth + 1)
            return

        if isinstance(value, dict):
            for key, item in value.items():
                key_str = _str_label(key, "key")
                self._extract_generic_metrics(method, item, f"{path}.{key_str}", depth + 1)

    def _collect_event_metric_series(
        self,
        event: str,
        value: Any,
        path: str,
        depth: int,
        numeric_series: dict[tuple[str, ...], float],
        boolean_series: dict[tuple[str, ...], float],
        status_series: dict[tuple[str, ...], float],
        list_length_series: dict[tuple[str, ...], float],
    ) -> None:
        if depth > self.config.max_depth:
            return
        metric_path = self._normalize_path(path)

        if isinstance(value, bool):
            boolean_series[(event, metric_path)] = 1.0 if value else 0.0
            return

        numeric_value = _as_float(value)
        if numeric_value is not None and not isinstance(value, str):
            numeric_series[(event, metric_path)] = numeric_value
            return

        if isinstance(value, str):
            float_value = _as_float(value)
            if float_value is not None:
                numeric_series[(event, metric_path)] = float_value
                return
            status_value = value.strip().upper()[:60]
            if self._status_like(status_value):
                status_series[(event, metric_path, status_value)] = 1.0
            return

        if isinstance(value, list):
            list_length_series[(event, metric_path)] = float(len(value))
            for index, item in enumerate(value[: self.config.max_list_items]):
                self._collect_event_metric_series(
                    event,
                    item,
                    f"{path}[{index}]",
                    depth + 1,
                    numeric_series,
                    boolean_series,
                    status_series,
                    list_length_series,
                )
            return

        if isinstance(value, dict):
            for key, item in value.items():
                key_str = _str_label(key, "key")
                self._collect_event_metric_series(
                    event,
                    item,
                    f"{path}.{key_str}",
                    depth + 1,
                    numeric_series,
                    boolean_series,
                    status_series,
                    list_length_series,
                )

    def _replace_generic_event_metrics(self, event: str, payload: Any) -> None:
        numeric_series: dict[tuple[str, ...], float] = {}
        boolean_series: dict[tuple[str, ...], float] = {}
        status_series: dict[tuple[str, ...], float] = {}
        list_length_series: dict[tuple[str, ...], float] = {}

        self._collect_event_metric_series(
            event,
            payload,
            "event",
            0,
            numeric_series,
            boolean_series,
            status_series,
            list_length_series,
        )

        self._replace_event_metric_series(
            EVENT_NUMERIC_VALUE,
            numeric_series,
            series_key=(EVENT_NUMERIC_VALUE, event),
        )
        self._replace_event_metric_series(
            EVENT_BOOLEAN_VALUE,
            boolean_series,
            series_key=(EVENT_BOOLEAN_VALUE, event),
        )
        self._replace_event_metric_series(
            EVENT_STATUS_VALUE,
            status_series,
            series_key=(EVENT_STATUS_VALUE, event),
        )
        self._replace_event_metric_series(
            EVENT_LIST_LENGTH,
            list_length_series,
            series_key=(EVENT_LIST_LENGTH, event),
        )

    # ------------------------------------------------------------------
    # Dedicated realtime event handlers
    # ------------------------------------------------------------------

    def _handle_app_stats_event(self, payload: dict[str, Any]) -> None:
        """Parse app.stats event payload into per-app Prometheus metrics.

        TrueNAS pushes this event for each app container with CPU, memory,
        network I/O, and block I/O stats. The payload contains a 'fields'
        array with one entry per app.
        """
        fields = payload.get("fields")
        if not isinstance(fields, list):
            return

        app_cpu: dict[tuple[str, ...], float] = {}
        app_memory: dict[tuple[str, ...], float] = {}
        app_net_rx: dict[tuple[str, ...], float] = {}
        app_net_tx: dict[tuple[str, ...], float] = {}
        app_blkio_read: dict[tuple[str, ...], float] = {}
        app_blkio_write: dict[tuple[str, ...], float] = {}

        for app_data in fields:
            if not isinstance(app_data, dict):
                continue
            app_name = _str_label(app_data.get("app_name") or app_data.get("app"), "unknown")

            cpu = _as_float(app_data.get("cpu_usage") or app_data.get("cpu"))
            if cpu is not None:
                app_cpu[(app_name,)] = cpu

            mem = _as_float(app_data.get("memory"))
            if mem is not None:
                app_memory[(app_name,)] = mem

            networks = app_data.get("networks")
            if isinstance(networks, list):
                for net in networks:
                    if not isinstance(net, dict):
                        continue
                    iface = net.get("interface_name", "unknown")
                    rx = _as_float(net.get("rx_bytes"))
                    tx = _as_float(net.get("tx_bytes"))
                    if rx is not None:
                        app_net_rx[(app_name, _str_label(iface))] = rx
                    if tx is not None:
                        app_net_tx[(app_name, _str_label(iface))] = tx

            blkio = app_data.get("blkio")
            if isinstance(blkio, dict):
                blkio_read = _as_float(blkio.get("read"))
                if blkio_read is not None:
                    app_blkio_read[(app_name,)] = blkio_read

                blkio_write = _as_float(blkio.get("write"))
                if blkio_write is not None:
                    app_blkio_write[(app_name,)] = blkio_write

        self._replace_event_metric_series(APP_CPU_PERCENT, app_cpu)
        self._replace_event_metric_series(APP_MEMORY_BYTES, app_memory)
        self._replace_event_metric_series(APP_NET_RX_BYTES_RATE, app_net_rx)
        self._replace_event_metric_series(APP_NET_TX_BYTES_RATE, app_net_tx)
        self._replace_event_metric_series(APP_BLKIO_READ_BYTES, app_blkio_read)
        self._replace_event_metric_series(APP_BLKIO_WRITE_BYTES, app_blkio_write)

    def _handle_virt_metrics_event(self, payload: dict[str, Any]) -> None:
        """Parse virt.instance.metrics event payload into per-instance Prometheus metrics.

        TrueNAS pushes this event for Incus/LXD instances with live CPU and memory stats.
        """
        fields = payload.get("fields")
        if not isinstance(fields, list):
            return

        virt_cpu: dict[tuple[str, ...], float] = {}
        virt_mem: dict[tuple[str, ...], float] = {}

        for inst_data in fields:
            if not isinstance(inst_data, dict):
                continue
            inst_name = _str_label(inst_data.get("name") or inst_data.get("instance"), "unknown")

            cpu = _as_float(inst_data.get("cpu") or inst_data.get("cpu_usage"))
            if cpu is not None:
                virt_cpu[(inst_name,)] = cpu

            mem = _as_float(inst_data.get("memory") or inst_data.get("memory_usage"))
            if mem is not None:
                virt_mem[(inst_name,)] = mem

        self._replace_event_metric_series(VIRT_INSTANCE_CPU, virt_cpu)
        self._replace_event_metric_series(VIRT_INSTANCE_MEM, virt_mem)

    def _handle_realtime_event(self, payload: dict[str, Any]) -> None:
        """Parse reporting.realtime event payload into dedicated Prometheus metrics.

        TrueNAS pushes this event ~every second with CPU, memory, disk I/O,
        network I/O, and ZFS ARC data. The structure varies slightly between
        TrueNAS versions but the keys below are stable across 24.x and 25.x.
        All access is defensive (.get()) so unknown payload shapes are silently
        skipped rather than crashing the event loop.
        """
        # ── CPU ──────────────────────────────────────────────────────────────
        cpu_section = payload.get("cpu") or {}
        cpu_data = cpu_section.get("cpu") or {}

        total_cpu_percent: float | None = None
        user_cpu_percent: float | None = None
        idle_cpu_percent: float | None = None

        cpu_percent_fields = (
            (CPU_USAGE_PERCENT, ("percent", "usage_percent", "usage")),
            (CPU_USER_PERCENT, ("user", "user_percent", "user_usage")),
            (CPU_SYSTEM_PERCENT, ("system", "system_percent", "sys")),
            (CPU_IOWAIT_PERCENT, ("iowait", "io_wait", "wait", "iowait_percent")),
            (CPU_IDLE_PERCENT, ("idle", "idle_percent")),
            (CPU_INTERRUPT_PERCENT, ("interrupt", "interrupt_percent", "irq", "softirq")),
        )

        for gauge, keys in cpu_percent_fields:
            val = None
            for container in (cpu_data, cpu_section):
                if not isinstance(container, dict):
                    continue
                for key in keys:
                    val = _as_float(container.get(key))
                    if val is not None:
                        break
                if val is not None:
                    break
            if val is None:
                continue
            gauge.set(val)
            if gauge is CPU_USAGE_PERCENT:
                total_cpu_percent = val
            elif gauge is CPU_USER_PERCENT:
                user_cpu_percent = val
            elif gauge is CPU_IDLE_PERCENT:
                idle_cpu_percent = val

        # TrueNAS 25.x reporting.realtime commonly exposes only aggregate
        # `cpu.usage` plus per-core usage/temperature (cpu0..cpuN). If a
        # detailed user/system split is unavailable, populate user with total
        # usage so dashboards still reflect live host load.
        if user_cpu_percent is None and total_cpu_percent is not None:
            CPU_USER_PERCENT.set(total_cpu_percent)

        # Likewise, when explicit idle is absent, infer it from total usage.
        if idle_cpu_percent is None and total_cpu_percent is not None:
            CPU_IDLE_PERCENT.set(max(0.0, 100.0 - total_cpu_percent))

        # Per-core CPU data is not stable across TrueNAS builds. Prefer the
        # documented per_cpu shape, but also accept common alternates seen in
        # Netdata-backed payloads where cores are emitted as cpu0/core1 dicts or
        # lists of {core, percent} objects.
        cpu_core_usage: dict[tuple[str, ...], float] = {}
        for per_cpu_candidate in (
            cpu_data.get("per_cpu"),
            cpu_section.get("per_cpu"),
            cpu_data.get("usage"),
            cpu_data.get("usage_percent"),
            cpu_section.get("usage"),
            cpu_section.get("usage_percent"),
            cpu_section.get("cores"),
        ):
            cpu_core_usage = _extract_labeled_numeric_series(
                per_cpu_candidate,
                value_keys=("percent", "usage", "value"),
                normalize_label=True,
            )
            if cpu_core_usage:
                break
        if not cpu_core_usage and isinstance(cpu_section, dict):
            for core_name, core_payload in cpu_section.items():
                if not isinstance(core_payload, dict):
                    continue
                if not re.fullmatch(r"cpu\d+", str(core_name)):
                    continue
                usage_val = _as_float(
                    core_payload.get("usage")
                    or core_payload.get("percent")
                    or core_payload.get("value")
                )
                if usage_val is not None:
                    cpu_core_usage[(_normalize_core_label(core_name),)] = usage_val
        self._replace_event_metric_series(CPU_CORE_USAGE_PERCENT, cpu_core_usage)

        # Per-core temperatures are even less consistent: some systems expose
        # temperature, others temperatures/temp, and labels may be 0/1, cpu0,
        # or core1.
        cpu_temps: dict[tuple[str, ...], float] = {}
        for temp_candidate in (
            cpu_section.get("temperature"),
            cpu_section.get("temperatures"),
            cpu_data.get("temperature"),
            cpu_data.get("temperatures"),
            cpu_section.get("temp"),
            cpu_data.get("temp"),
        ):
            cpu_temps = _extract_labeled_numeric_series(
                temp_candidate,
                value_keys=("temperature", "temp", "celsius", "value"),
                normalize_label=True,
            )
            if cpu_temps:
                break
        if not cpu_temps and isinstance(cpu_section, dict):
            for core_name, core_payload in cpu_section.items():
                if not isinstance(core_payload, dict):
                    continue
                if not re.fullmatch(r"cpu\d+", str(core_name)):
                    continue
                temp_val = _as_float(
                    core_payload.get("temp")
                    or core_payload.get("temperature")
                    or core_payload.get("celsius")
                    or core_payload.get("value")
                )
                if temp_val is not None:
                    cpu_temps[(_normalize_core_label(core_name),)] = temp_val
        self._replace_event_metric_series(CPU_TEMPERATURE_C, cpu_temps)

        # ── Memory ───────────────────────────────────────────────────────────
        mem = payload.get("memory") or {}

        # TrueNAS 24.x / 25.x field names (may vary; try both)
        total = _as_float(mem.get("physical_memory_total") or mem.get("total"))
        avail = _as_float(mem.get("physical_memory_available") or mem.get("available") or mem.get("avail"))
        free  = _as_float(mem.get("physical_memory_free") or mem.get("free"))
        cached = _as_float(mem.get("physical_memory_cached") or mem.get("cached"))
        buffers = _as_float(mem.get("physical_memory_buffers") or mem.get("buffers"))
        swap_total = _as_float(mem.get("swap_total"))
        swap_free  = _as_float(mem.get("swap_free"))

        # FreeBSD-style 'classes' sub-dict (older TrueNAS builds)
        classes = mem.get("classes")
        if isinstance(classes, dict):
            if total is None:
                # Sum all non-free classes as a proxy
                total = _as_float(sum(v for v in classes.values() if isinstance(v, (int, float))))
            if free is None:
                free = _as_float(classes.get("free"))
            if cached is None:
                cached = _as_float(classes.get("cache"))

        # Swap may be nested under "swap" key
        swap_obj = mem.get("swap")
        if isinstance(swap_obj, dict):
            if swap_total is None:
                swap_total = _as_float(swap_obj.get("total"))
            if swap_free is None:
                # Try "free" key first; if absent, compute from total - used
                swap_free_raw = _as_float(swap_obj.get("free"))
                if swap_free_raw is not None:
                    swap_free = swap_free_raw
                else:
                    swap_used_raw = _as_float(swap_obj.get("used"))
                    if swap_used_raw is not None and swap_total is not None:
                        swap_free = swap_total - swap_used_raw

        for val, gauge in (
            (total,      MEMORY_PHYSICAL_TOTAL_BYTES),
            (avail,      MEMORY_PHYSICAL_AVAILABLE_BYTES),
            (free,       MEMORY_PHYSICAL_FREE_BYTES),
            (cached,     MEMORY_PHYSICAL_CACHED_BYTES),
            (buffers,    MEMORY_PHYSICAL_BUFFERS_BYTES),
            (swap_total, MEMORY_SWAP_TOTAL_BYTES),
            (swap_free,  MEMORY_SWAP_FREE_BYTES),
        ):
            if val is not None:
                gauge.set(val)

        if total is not None and avail is not None:
            MEMORY_PHYSICAL_USED_BYTES.set(total - avail)
        if swap_total is not None and swap_free is not None:
            MEMORY_SWAP_USED_BYTES.set(swap_total - swap_free)

        # ── Disk I/O ─────────────────────────────────────────────────────────
        # In v25.10.2 the API schema names this key "disls" (confirmed in the
        # reporting.realtime event schema). Fall back to "disks" for backward
        # compatibility with v24.x deployments.
        #
        # v25.10.2 schema: disls = {busy, read_bytes, write_bytes, read_ops, write_ops}
        #   — aggregate across all disks, NOT a per-disk mapping.
        # v24.x / some builds: disls = {disk_name: {busy, read_bytes, ...}}
        #   — per-disk mapping.
        # We detect which format we have by checking whether the first value is a dict.
        disks = payload.get("disls") or payload.get("disks")
        disk_read_bytes: dict[tuple[str, ...], float] = {}
        disk_write_bytes: dict[tuple[str, ...], float] = {}
        disk_read_ops: dict[tuple[str, ...], float] = {}
        disk_write_ops: dict[tuple[str, ...], float] = {}
        disk_busy: dict[tuple[str, ...], float] = {}
        if isinstance(disks, dict):
            _disk_keys = (
                ("read_bytes", disk_read_bytes),
                ("write_bytes", disk_write_bytes),
                ("read_ops", disk_read_ops),
                ("write_ops", disk_write_ops),
                ("busy", disk_busy),
            )
            first_val = next(iter(disks.values()), None)
            if isinstance(first_val, dict):
                # Per-disk format: {disk_name: {busy: float, ...}}
                for disk_name, disk_data in disks.items():
                    if not isinstance(disk_data, dict):
                        continue
                    dn = _str_label(disk_name)
                    for key, bucket in _disk_keys:
                        v = _as_float(disk_data.get(key))
                        if v is not None:
                            bucket[(dn,)] = v
            else:
                # Aggregate format (v25.10.2): {busy: float, read_bytes: float, ...}
                for key, bucket in _disk_keys:
                    v = _as_float(disks.get(key))
                    if v is not None:
                        bucket[("total",)] = v

        self._replace_event_metric_series(DISK_READ_BYTES_RATE, disk_read_bytes)
        self._replace_event_metric_series(DISK_WRITE_BYTES_RATE, disk_write_bytes)
        self._replace_event_metric_series(DISK_READ_OPS_RATE, disk_read_ops)
        self._replace_event_metric_series(DISK_WRITE_OPS_RATE, disk_write_ops)
        self._replace_event_metric_series(DISK_BUSY_PERCENT, disk_busy)

        # ── Network I/O ───────────────────────────────────────────────────────
        interfaces = payload.get("interfaces")
        network_rx: dict[tuple[str, ...], float] = {}
        network_tx: dict[tuple[str, ...], float] = {}
        if isinstance(interfaces, dict):
            for iface_name, iface_data in interfaces.items():
                if not isinstance(iface_data, dict):
                    continue
                iface = _str_label(iface_name)
                for key, gauge in (
                    ("received_bytes",        NETWORK_RX_BYTES_RATE),
                    ("sent_bytes",            NETWORK_TX_BYTES_RATE),
                    ("received_bytes_rate",   NETWORK_RX_BYTES_RATE),   # prefer rate keys
                    ("sent_bytes_rate",       NETWORK_TX_BYTES_RATE),
                ):
                    v = _as_float(iface_data.get(key))
                    if v is not None:
                        bucket = network_rx if gauge is NETWORK_RX_BYTES_RATE else network_tx
                        bucket[(iface,)] = v

        self._replace_event_metric_series(NETWORK_RX_BYTES_RATE, network_rx)
        self._replace_event_metric_series(NETWORK_TX_BYTES_RATE, network_tx)

        # ── ZFS ARC (v24.x fallback) ────────────────────────────────────────
        # May appear as payload["zfs"] or payload["virtual_memory"]
        for zfs_key in ("zfs", "arc"):
            zfs = payload.get(zfs_key)
            if isinstance(zfs, dict):
                for key, gauge in (
                    ("arc_size",             ZFS_ARC_SIZE_BYTES),
                    ("arc_max_size",         ZFS_ARC_MAX_SIZE_BYTES),
                    ("arc_min_size",         ZFS_ARC_MIN_SIZE_BYTES),
                    ("cache_hit_ratio",      ZFS_ARC_HIT_RATIO),
                    ("arc_hit_ratio",        ZFS_ARC_HIT_RATIO),
                    ("arc_hits",             ZFS_ARC_HITS_RATE),
                    ("arc_misses",           ZFS_ARC_MISSES_RATE),
                ):
                    v = _as_float(zfs.get(key))
                    if v is not None:
                        gauge.set(v)

        # ── ZFS ARC v25+ (from memory section) ──────────────────────────────
        # In v25, arc_size, arc_free_memory, arc_available_memory moved to memory section
        mem = payload.get("memory")
        if isinstance(mem, dict):
            arc_size = _as_float(mem.get("arc_size"))
            if arc_size is not None:
                ZFS_ARC_SIZE_BYTES.set(arc_size)
            arc_free = _as_float(mem.get("arc_free_memory"))
            if arc_free is not None:
                ZFS_ARC_FREE_MEMORY_BYTES.set(arc_free)
            arc_avail = _as_float(mem.get("arc_available_memory"))
            if arc_avail is not None:
                ZFS_ARC_AVAILABLE_BYTES.set(arc_avail)

        # ── ZFS v25+ demand data/metadata stats ─────────────────────────────
        zfs_v25 = payload.get("zfs")
        if isinstance(zfs_v25, dict):
            # ── Total demand accesses (data + metadata combined) ─────────────
            demand_accesses = _as_float(zfs_v25.get("demand_accesses_per_second"))
            if demand_accesses is not None:
                ZFS_DEMAND_ACCESSES_RATE.set(demand_accesses)

            # ── Demand data stats ────────────────────────────────────────────
            data_hits = _as_float(zfs_v25.get("demand_data_hits_per_second"))
            if data_hits is not None:
                ZFS_DEMAND_DATA_HITS_RATE.set(data_hits)
            data_misses = _as_float(zfs_v25.get("demand_data_misses_per_second"))
            if data_misses is not None:
                ZFS_DEMAND_DATA_MISSES_RATE.set(data_misses)
            data_accesses = _as_float(zfs_v25.get("demand_data_accesses_per_second"))
            if data_accesses is not None:
                ZFS_DEMAND_DATA_ACCESSES_RATE.set(data_accesses)

            # Prefer API-provided hit/miss percentages over computed ratios —
            # they account for prefetch hits that aren't in the hits+misses sum.
            data_hit_pct = _as_float(zfs_v25.get("demand_data_hit_percentage"))
            if data_hit_pct is not None:
                ZFS_DEMAND_DATA_HIT_RATIO.set(data_hit_pct / 100.0)
            elif data_hits is not None and data_misses is not None:
                data_total = data_hits + data_misses
                if data_total > 0:
                    ZFS_DEMAND_DATA_HIT_RATIO.set(data_hits / data_total)

            data_miss_pct = _as_float(zfs_v25.get("demand_data_miss_percentage"))
            if data_miss_pct is not None:
                ZFS_DEMAND_DATA_MISS_RATIO.set(data_miss_pct / 100.0)
            elif data_hits is not None and data_misses is not None:
                data_total = data_hits + data_misses
                if data_total > 0:
                    ZFS_DEMAND_DATA_MISS_RATIO.set(data_misses / data_total)

            # Demand data I/O hits (raw rate + percentage)
            data_io_hits = _as_float(zfs_v25.get("demand_data_io_hits_per_second"))
            if data_io_hits is not None:
                ZFS_DEMAND_DATA_IO_HITS_RATE.set(data_io_hits)
            io_hit_pct = _as_float(zfs_v25.get("demand_data_io_hit_percentage"))
            if io_hit_pct is not None:
                ZFS_DEMAND_DATA_IO_HIT_RATIO.set(io_hit_pct / 100.0)

            # ── Demand metadata stats ────────────────────────────────────────
            meta_hits = _as_float(zfs_v25.get("demand_metadata_hits_per_second"))
            if meta_hits is not None:
                ZFS_DEMAND_META_HITS_RATE.set(meta_hits)
            meta_misses = _as_float(zfs_v25.get("demand_metadata_misses_per_second"))
            if meta_misses is not None:
                ZFS_DEMAND_META_MISSES_RATE.set(meta_misses)
            meta_accesses = _as_float(zfs_v25.get("demand_metadata_accesses_per_second"))
            if meta_accesses is not None:
                ZFS_DEMAND_META_ACCESSES_RATE.set(meta_accesses)

            meta_hit_pct = _as_float(zfs_v25.get("demand_metadata_hit_percentage"))
            if meta_hit_pct is not None:
                ZFS_DEMAND_META_HIT_RATIO.set(meta_hit_pct / 100.0)
            elif meta_hits is not None and meta_misses is not None:
                meta_total = meta_hits + meta_misses
                if meta_total > 0:
                    ZFS_DEMAND_META_HIT_RATIO.set(meta_hits / meta_total)

            meta_miss_pct = _as_float(zfs_v25.get("demand_metadata_miss_percentage"))
            if meta_miss_pct is not None:
                ZFS_DEMAND_META_MISS_RATIO.set(meta_miss_pct / 100.0)

            meta_io_hits = _as_float(zfs_v25.get("demand_metadata_io_hits_per_second"))
            if meta_io_hits is not None:
                ZFS_DEMAND_META_IO_HITS_RATE.set(meta_io_hits)
            meta_io_hit_pct = _as_float(zfs_v25.get("demand_metadata_io_hit_percentage"))
            if meta_io_hit_pct is not None:
                ZFS_DEMAND_META_IO_HIT_RATIO.set(meta_io_hit_pct / 100.0)

            # ── Global ARC hit ratio (computed from data + metadata) ─────────
            if data_hits is not None and meta_hits is not None and data_misses is not None and meta_misses is not None:
                total_hits = data_hits + meta_hits
                total_misses = data_misses + meta_misses
                total_accesses = total_hits + total_misses
                if total_accesses > 0:
                    ZFS_ARC_HIT_RATIO.set(total_hits / total_accesses)
                ZFS_ARC_HITS_RATE.set(total_hits)
                ZFS_ARC_MISSES_RATE.set(total_misses)

            # ── L2ARC stats ──────────────────────────────────────────────────
            l2_hits = _as_float(zfs_v25.get("l2arc_hits_per_second"))
            if l2_hits is not None:
                ZFS_L2ARC_HITS_RATE.set(l2_hits)
            l2_misses = _as_float(zfs_v25.get("l2arc_misses_per_second"))
            if l2_misses is not None:
                ZFS_L2ARC_MISSES_RATE.set(l2_misses)
            l2_accesses = _as_float(zfs_v25.get("total_l2arc_accesses_per_second"))
            if l2_accesses is not None:
                ZFS_L2ARC_ACCESSES_RATE.set(l2_accesses)

            l2_hit_pct = _as_float(zfs_v25.get("l2arc_access_hit_percentage"))
            if l2_hit_pct is not None:
                ZFS_L2ARC_HIT_RATIO.set(l2_hit_pct / 100.0)
            elif l2_hits is not None and l2_misses is not None:
                l2_total = l2_hits + l2_misses
                if l2_total > 0:
                    ZFS_L2ARC_HIT_RATIO.set(l2_hits / l2_total)

            l2_miss_pct = _as_float(zfs_v25.get("l2arc_miss_percentage"))
            if l2_miss_pct is not None:
                ZFS_L2ARC_MISS_RATIO.set(l2_miss_pct / 100.0)

            for key, gauge in (
                ("bytes_read_per_second_from_the_l2arc", ZFS_L2ARC_READ_BYTES_RATE),
                ("bytes_written_per_second_to_the_l2arc", ZFS_L2ARC_WRITE_BYTES_RATE),
            ):
                v = _as_float(zfs_v25.get(key))
                if v is not None:
                    gauge.set(v)

        # ── Pool real-time I/O (v25+ pools section) ──────────────────────────
        # The reporting.realtime event includes a "pools" object with per-pool
        # I/O statistics. Exact field names may vary; extract defensively.
        pools_rt = payload.get("pools")
        pool_read: dict[tuple[str, ...], float] = {}
        pool_write: dict[tuple[str, ...], float] = {}
        if isinstance(pools_rt, dict):
            for pool_name, pool_stats in pools_rt.items():
                if not isinstance(pool_stats, dict):
                    continue
                pn = _str_label(pool_name)
                read_bytes = _as_float(
                    pool_stats.get("read_bytes") or pool_stats.get("read_bytes_per_second")
                )
                if read_bytes is not None:
                    pool_read[(pn,)] = read_bytes
                write_bytes = _as_float(
                    pool_stats.get("write_bytes") or pool_stats.get("write_bytes_per_second")
                )
                if write_bytes is not None:
                    pool_write[(pn,)] = write_bytes

        self._replace_event_metric_series(POOL_REALTIME_READ_BYTES, pool_read)
        self._replace_event_metric_series(POOL_REALTIME_WRITE_BYTES, pool_write)

    def _dispatch_event(self, collection: str, payload: Any) -> None:
        EVENT_LAST_MESSAGE_TS.labels(event=collection).set(time.time())
        if collection == "reporting.realtime" and isinstance(payload, dict):
            try:
                self._handle_realtime_event(payload)
            except Exception:
                self._collector_error("event_realtime", "_handle_realtime_event failed")
        elif collection == "app.stats" and isinstance(payload, dict):
            try:
                self._handle_app_stats_event(payload)
            except Exception:
                self._collector_error("event_app_stats", "_handle_app_stats_event failed")
        elif collection == "virt.instance.metrics" and isinstance(payload, dict):
            try:
                self._handle_virt_metrics_event(payload)
            except Exception:
                self._collector_error("event_virt_metrics", "_handle_virt_metrics_event failed")
        self._replace_generic_event_metrics(collection, payload)

    # ------------------------------------------------------------------
    # Event stream
    # ------------------------------------------------------------------

    def _event_stream_loop(self) -> None:
        backoff = 2
        while True:
            try:
                with JsonRpcWsClient(
                    ws_url=self.config.ws_url,
                    timeout_seconds=self.config.event_read_timeout_seconds,
                    verify_tls=self.config.verify_tls,
                ) as client:
                    login_result = client.call("auth.login_with_api_key", [self.config.api_key])

                    # --- Step 2: High-level metric extraction (Recursive traversal) ---
                    if not _as_bool(login_result):
                        raise JsonRpcError("event stream: auth.login_with_api_key returned falsy")

                    subscribed_events: list[str] = []
                    for event in self.config.event_subscriptions:
                        subscribe_name = self._format_event_subscription(event)
                        try:
                            client.call("core.subscribe", [subscribe_name])
                            EVENT_STREAM_UP.labels(event=event).set(1)
                            subscribed_events.append(event)
                        except Exception:
                            EVENT_STREAM_UP.labels(event=event).set(0)
                            self._collector_error("event_subscribe", f"Failed subscribing to {event}")

                    if not subscribed_events:
                        raise RuntimeError("No event subscriptions succeeded")

                    backoff = 2  # reset backoff on successful connection

                    while True:
                        try:
                            msg = client.recv_json()
                        except WebSocketTimeoutException:
                            continue
                        if msg.get("method") != "collection_update":
                            continue
                        params = msg.get("params")
                        if not isinstance(params, dict):
                            continue
                        collection = _str_label(params.get("collection"), "unknown")
                        if collection not in subscribed_events:
                            continue
                        EVENT_MESSAGES_TOTAL.labels(event=collection).inc()
                        fields = params.get("fields")
                        payload = fields if isinstance(fields, dict) else params
                        # Acquire the scrape lock before updating Prometheus metrics so
                        # that a concurrent /metrics scrape sees a consistent snapshot
                        # (all CPU sub-components from the same event cycle, etc.).
                        with self._lock:
                            self._dispatch_event(collection, payload)

            except Exception:
                self._collector_error("event_stream", "Event stream error")
                for event in self.config.event_subscriptions:
                    EVENT_STREAM_UP.labels(event=event).set(0)
                LOG.warning("Event stream reconnecting in %ds", backoff, exc_info=True)
                time.sleep(backoff)
                backoff = min(backoff * 2, 120)  # exponential backoff, cap at 2 minutes

    def _ensure_event_thread(self) -> None:
        if not self.config.enable_event_streams:
            return
        if self._event_thread is not None and self._event_thread.is_alive():
            return
        self._event_thread = threading.Thread(
            target=self._event_stream_loop,
            name="truenas-event-stream",
            daemon=True,
        )
        self._event_thread.start()

    # ------------------------------------------------------------------
    # Host metrics
    # ------------------------------------------------------------------

    def _export_host_metrics(self, info: Any) -> None:
        if not isinstance(info, dict):
            return
        hostname = _str_label(info.get("hostname"), "unknown")
        version = _str_label(info.get("version"), "unknown")
        product_type = _str_label(info.get("product_type"), "unknown")
        HOST_INFO.labels(hostname=hostname, version=version, product_type=product_type).set(1)

        uptime_seconds = _as_float(info.get("uptime_seconds"))
        if uptime_seconds is not None:
            HOST_UPTIME_SECONDS.set(uptime_seconds)

        physmem = _as_float(info.get("physmem") or info.get("physical_memory"))
        if physmem is not None:
            HOST_PHYSICAL_MEMORY_BYTES.set(physmem)

        cpu_cores = _as_float(info.get("cores") or info.get("cpu_cores"))
        if cpu_cores is not None:
            HOST_CPU_CORES.set(cpu_cores)

        # Physical CPU cores (non-HT) - needed for accurate HT/SMT detection
        physical_cores = _as_float(info.get("physical_cores"))
        if physical_cores is not None:
            HOST_PHYSICAL_CPU_CORES.set(physical_cores)

        loadavg = info.get("loadavg")
        if isinstance(loadavg, (list, tuple)):
            for i, label in enumerate(["1m", "5m", "15m"]):
                lv = _as_float(loadavg[i]) if i < len(loadavg) else None
                if lv is not None:
                    HOST_LOAD_AVERAGE.labels(window=label).set(lv)

        # ECC memory flag — system.info returns ecc_memory: true/false
        ecc = info.get("ecc_memory")
        if ecc is not None:
            HOST_ECC_MEMORY.set(1 if _as_bool(ecc) else 0)

        # CPU model string (system.info → "model": "Intel(R) Xeon(R) ...")
        cpu_model = _str_label(info.get("model") or info.get("cpu_model"), "")
        if cpu_model:
            HOST_CPU_MODEL.labels(model=cpu_model).set(1)

        # Hardware identity from DMI (system.info → system_manufacturer, system_product)
        manufacturer = _str_label(
            info.get("system_manufacturer") or info.get("dmi_vendor") or info.get("vendor"), ""
        )
        product = _str_label(
            info.get("system_product") or info.get("dmi_product") or info.get("product"), ""
        )
        if manufacturer or product:
            HOST_SYSTEM_INFO.labels(
                manufacturer=manufacturer or "unknown",
                product=product or "unknown",
            ).set(1)

    # ------------------------------------------------------------------
    # Reporting timeseries
    # ------------------------------------------------------------------

    def _extract_graph_names(self, value: Any) -> list[str]:
        names: list[str] = []
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    name = item.get("name")
                    if isinstance(name, str) and name.strip():
                        names.append(name.strip())
                elif isinstance(item, str) and item.strip():
                    names.append(item.strip())
        elif isinstance(value, dict):
            for key, item in value.items():
                if isinstance(key, str) and key.strip():
                    names.append(key.strip())
                if isinstance(item, dict):
                    name = item.get("name")
                    if isinstance(name, str) and name.strip():
                        names.append(name.strip())
        return sorted(set(names))

    def _pick_graphs(self, names: list[str], limit: int = 12) -> list[dict[str, str]]:
        preferred = ("cpu", "mem", "memory", "load", "network", "net", "disk", "zfs", "arc", "vm", "nfs")
        ranked = sorted(
            names,
            key=lambda n: (0 if any(tag in n.lower() for tag in preferred) else 1, len(n), n),
        )
        return [{"name": g} for g in ranked[:limit]]

    def _collect_reporting_timeseries(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        graph_names: list[str] = []
        for graph_method in ("reporting.netdata_graphs", "reporting.graphs"):
            graph_result = self._safe_call_auto(client, graph_method)
            if graph_result is not None:
                cache[graph_method] = graph_result
                self._extract_generic_metrics(graph_method, graph_result, "result", 0)
                graph_names.extend(self._extract_graph_names(graph_result))

        if not graph_names:
            graph_names = ["cpu", "memory", "load"]

        # reporting.get_data and reporting.netdata_get_data are not called —
        # they were deprecated in TrueNAS 25.x and consistently return errors.
        # Graph names are still collected above via reporting.graphs /
        # reporting.netdata_graphs and exposed through generic method metrics.

    # ------------------------------------------------------------------
    # Filesystem metrics
    # ------------------------------------------------------------------

    def _collect_filesystem_metrics(self, client: JsonRpcWsClient) -> None:
        selected_paths = self.config.filesystem_paths[: self.config.max_entity_calls]
        FILESYSTEM_PATH_COUNT.set(len(selected_paths))
        listdir_select = [
            "path", "type", "size", "allocation_size", "mode",
            "uid", "gid", "acl", "is_mountpoint", "is_ctldir",
            "attributes", "mount_id", "inode", "nlink",
        ]
        for fs_path in selected_paths:
            path_tag = self._normalize_path(fs_path)
            for method, params in (
                ("filesystem.stat", [fs_path]),
                # filesystem.statfs removed — requires path to be a mounted FS root;
                # fails on /mnt itself (not a ZFS mountpoint). stat() covers this.
                ("filesystem.get_zfs_attributes", [fs_path]),
                ("filesystem.getacl", [fs_path, True, False]),
            ):
                try:
                    result = self._call(client, method, params)
                    self._extract_generic_metrics(method, result, f"result.filesystem.{path_tag}", 0)
                except Exception:
                    LOG.debug("%s failed for %s", method, fs_path, exc_info=True)

            if self.config.enable_filesystem_listdir:
                try:
                    result = self._call(
                        client, "filesystem.listdir",
                        [fs_path, [], {"limit": self.config.query_limit, "select": listdir_select}],
                    )
                    self._extract_generic_metrics(
                        "filesystem.listdir", result,
                        f"result.filesystem.listdir.{path_tag}", 0,
                    )
                except Exception:
                    LOG.debug("filesystem.listdir failed for %s", fs_path, exc_info=True)

    # ------------------------------------------------------------------
    # Per-entity detail metrics (VMs, apps)
    # ------------------------------------------------------------------

    def _collect_entity_detail_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        vm_query = cache.get("vm.query") or self._safe_call_auto(client, "vm.query")
        vm_list = vm_query if isinstance(vm_query, list) else []
        VM_COUNT.set(len(vm_list))
        for vm in vm_list[: self.config.max_entity_calls]:
            if not isinstance(vm, dict):
                continue
            vm_id = vm.get("id")
            if not isinstance(vm_id, int):
                continue
            for method in ("vm.get_memory_usage", "vm.get_vm_memory_info"):
                try:
                    result = self._call(client, method, [vm_id])
                    self._extract_generic_metrics(method, result, f"result.vm.{vm_id}", 0)
                except Exception:
                    continue

        app_query = cache.get("app.query") or self._safe_call_auto(client, "app.query")
        app_list = app_query if isinstance(app_query, list) else []
        APP_COUNT.set(len(app_list))
        APP_STATE.clear()
        APP_UPGRADE_AVAILABLE.clear()
        APP_IMAGE_UPDATES_AVAILABLE.clear()
        APP_CUSTOM.clear()
        APP_MIGRATED.clear()
        APP_CONTAINER_COUNT.clear()
        APP_USED_PORT_COUNT.clear()
        APP_USED_HOST_IP_COUNT.clear()
        APP_CONTAINER_STATE_COUNT.clear()
        for app in app_list[: self.config.max_entity_calls]:
            if not isinstance(app, dict):
                continue
            app_name = app.get("name")
            if not isinstance(app_name, str) or not app_name.strip():
                continue
            # Per-app state (e.g. RUNNING, STOPPED, DEPLOYING)
            app_st = _str_label(app.get("state"), "UNKNOWN").upper()
            APP_STATE.labels(app=app_name, state=app_st).set(1)

            for raw_value, gauge in (
                (app.get("upgrade_available"), APP_UPGRADE_AVAILABLE),
                (app.get("image_updates_available"), APP_IMAGE_UPDATES_AVAILABLE),
                (app.get("custom_app"), APP_CUSTOM),
                (app.get("migrated"), APP_MIGRATED),
            ):
                if raw_value is not None:
                    gauge.labels(app=app_name).set(1 if _as_bool(raw_value) else 0)

            active_workloads = app.get("active_workloads")
            if isinstance(active_workloads, dict):
                container_count = _as_float(active_workloads.get("containers"))
                if container_count is not None:
                    APP_CONTAINER_COUNT.labels(app=app_name).set(container_count)

                used_ports = active_workloads.get("used_ports")
                if isinstance(used_ports, list):
                    APP_USED_PORT_COUNT.labels(app=app_name).set(len(used_ports))

                used_host_ips = active_workloads.get("used_host_ips")
                if isinstance(used_host_ips, list):
                    APP_USED_HOST_IP_COUNT.labels(app=app_name).set(len(used_host_ips))

                container_details = active_workloads.get("container_details")
                if isinstance(container_details, list):
                    container_states: dict[str, int] = {}
                    for detail in container_details:
                        if not isinstance(detail, dict):
                            continue
                        state = _str_label(detail.get("state"), "UNKNOWN").upper()
                        container_states[state] = container_states.get(state, 0) + 1
                    for state, count in container_states.items():
                        APP_CONTAINER_STATE_COUNT.labels(app=app_name, state=state).set(count)

            try:
                result = self._call(client, "app.outdated_docker_images", [app_name])
                self._extract_generic_metrics("app.outdated_docker_images", result, f"result.app.{app_name}", 0)
            except Exception:
                continue

    # ------------------------------------------------------------------
    # Boot pool metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_boot_pool_metrics(self, client: JsonRpcWsClient) -> None:
        try:
            state = self._call(client, "boot.get_state", [])
        except Exception:
            LOG.debug("boot.get_state failed", exc_info=True)
            return

        if not isinstance(state, dict):
            return

        healthy = _as_bool(state.get("healthy"))
        BOOT_POOL_HEALTHY.set(1 if healthy else 0)

        status = _str_label(state.get("status"), "UNKNOWN").upper()
        BOOT_POOL_STATUS.clear()
        BOOT_POOL_STATUS.labels(status=status).set(1)

        for gauge, field in (
            (BOOT_POOL_SIZE_BYTES, "size"),
            (BOOT_POOL_ALLOCATED_BYTES, "allocated"),
            (BOOT_POOL_FREE_BYTES, "free"),
        ):
            val = _as_float(state.get(field))
            if val is not None:
                gauge.set(val)

        scan = state.get("scan")
        if isinstance(scan, dict):
            scan_state = _str_label(scan.get("state") or scan.get("function"), "NONE").upper()
            BOOT_POOL_SCAN_STATE.clear()
            BOOT_POOL_SCAN_STATE.labels(state=scan_state).set(1)
            pct = _as_float(scan.get("percentage"))
            if pct is not None:
                BOOT_POOL_SCAN_PERCENT.set(pct)

        try:
            boot_disks = self._call(client, "boot.get_disks", [])
            if isinstance(boot_disks, list):
                BOOT_POOL_DISK_COUNT.set(len(boot_disks))
        except Exception:
            LOG.debug("boot.get_disks failed", exc_info=True)

    # ------------------------------------------------------------------
    # Certificate metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_certificate_metrics(self, client: JsonRpcWsClient) -> None:
        try:
            certs = self._call(client, "certificate.query", [
                [], {"select": ["name", "organization", "common", "until", "CSR"]}
            ])
        except Exception:
            LOG.debug("certificate.query failed", exc_info=True)
            return

        if not isinstance(certs, list):
            return

        # Filter to actual certs (not CSR placeholders)
        real_certs = [c for c in certs if isinstance(c, dict) and not c.get("CSR", False)]
        CERT_COUNT.set(len(real_certs))
        CERT_DAYS_TO_EXPIRY.clear()

        for cert in real_certs:
            name = _str_label(cert.get("name"), "unnamed")
            issuer = _str_label(
                cert.get("organization") or cert.get("common") or cert.get("issuer") or cert.get("signedby"),
                "unknown",
            )

            days = _cert_days_to_expiry(cert.get("until"))
            if days is not None:
                CERT_DAYS_TO_EXPIRY.labels(name=name, issuer=issuer).set(days)

    # ------------------------------------------------------------------
    # Dataset metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_dataset_metrics(self, client: JsonRpcWsClient) -> None:
        if not self.config.enable_dataset_metrics:
            return
        try:
            datasets = self._call(client, "pool.dataset.query", [
                [],
                {
                    "limit": self.config.max_datasets,
                    "extra": {
                        "properties": [
                            "used",
                            "available",
                            "referenced",
                            "quota",
                            "refquota",
                            "compressratio",
                            "reservation",
                            "refreservation",
                            "usedbychildren",
                            "usedbydataset",
                            "usedbysnapshots",
                            "readonly",
                            "atime",
                            "exec",
                            "quota_warning",
                            "quota_critical",
                            "refquota_warning",
                            "refquota_critical",
                            "creation",
                        ],
                    },
                    "select": [
                        "name",
                        ["used.parsed", "used"],
                        ["available.parsed", "available"],
                        ["referenced.parsed", "referenced"],
                        ["quota.parsed", "quota"],
                        ["refquota.parsed", "refquota"],
                        ["compressratio.parsed", "compressratio"],
                        ["reservation.parsed", "reservation"],
                        ["refreservation.parsed", "refreservation"],
                        ["usedbychildren.parsed", "usedbychildren"],
                        ["usedbydataset.parsed", "usedbydataset"],
                        ["usedbysnapshots.parsed", "usedbysnapshots"],
                        ["readonly.parsed", "readonly"],
                        ["atime.parsed", "atime"],
                        ["exec.parsed", "exec"],
                        ["quota_warning.parsed", "quota_warning"],
                        ["quota_critical.parsed", "quota_critical"],
                        ["refquota_warning.parsed", "refquota_warning"],
                        ["refquota_critical.parsed", "refquota_critical"],
                        ["creation.parsed", "creation"],
                        "encrypted",
                        "key_loaded",
                        "locked",
                    ],
                },
            ])
        except Exception:
            LOG.debug("pool.dataset.query failed", exc_info=True)
            return

        if not isinstance(datasets, list):
            return

        DATASET_COUNT.set(len(datasets))
        # NOTE: DATASET_* gauges are already cleared at the top of scrape_once()
        # inside the lock. Do not clear them again here — doing so would be a
        # no-op at best and could create a race window if the lock is ever relaxed.

        for index, ds in enumerate(datasets):
            if not isinstance(ds, dict):
                continue
            name = _str_label(ds.get("name"), "unknown")

            for gauge, field in (
                (DATASET_USED_BYTES, "used"),
                (DATASET_AVAILABLE_BYTES, "available"),
                (DATASET_REFERENCED_BYTES, "referenced"),
                (DATASET_RESERVATION_BYTES, "reservation"),
                (DATASET_REFRESERVATION_BYTES, "refreservation"),
                (DATASET_USED_BY_CHILDREN_BYTES, "usedbychildren"),
                (DATASET_USED_BY_DATASET_BYTES, "usedbydataset"),
                (DATASET_USED_BY_SNAPSHOTS_BYTES, "usedbysnapshots"),
            ):
                val = _as_float(ds.get(field))
                if val is not None:
                    gauge.labels(dataset=name).set(val)

            # quota / refquota: 0 means no quota set; expose raw value
            for gauge, field in (
                (DATASET_QUOTA_BYTES, "quota"),
                (DATASET_REFQUOTA_BYTES, "refquota"),
            ):
                val = _as_float(ds.get(field))
                if val is not None:
                    gauge.labels(dataset=name).set(val)

            snap_count = _as_float(ds.get("snapshot_count"))
            if snap_count is None and index < self.config.max_entity_calls:
                try:
                    snap_count = _as_float(self._call(client, "pool.dataset.snapshot_count", [name]))
                except Exception:
                    LOG.debug("pool.dataset.snapshot_count failed for %s", name, exc_info=True)
            if snap_count is not None:
                DATASET_SNAPSHOT_COUNT.labels(dataset=name).set(snap_count)

            ratio_raw = ds.get("compressratio")
            ratio = _as_float(ratio_raw)
            if ratio is not None:
                DATASET_COMPRESSION_RATIO.labels(dataset=name).set(ratio)

            for raw_value, gauge in (
                (ds.get("readonly"), DATASET_READONLY),
                (ds.get("atime"), DATASET_ATIME),
                (ds.get("exec"), DATASET_EXEC),
                (ds.get("key_loaded"), DATASET_KEY_LOADED),
                (ds.get("locked"), DATASET_LOCKED),
            ):
                if raw_value is not None:
                    gauge.labels(dataset=name).set(1 if _as_bool(raw_value) else 0)

            for gauge, field in (
                (DATASET_QUOTA_WARNING_PERCENT, "quota_warning"),
                (DATASET_QUOTA_CRITICAL_PERCENT, "quota_critical"),
                (DATASET_REFQUOTA_WARNING_PERCENT, "refquota_warning"),
                (DATASET_REFQUOTA_CRITICAL_PERCENT, "refquota_critical"),
            ):
                val = _as_float(ds.get(field))
                if val is not None:
                    gauge.labels(dataset=name).set(val)

            encrypted = ds.get("encrypted")
            if encrypted is not None:
                DATASET_ENCRYPTED.labels(dataset=name).set(1 if _as_bool(encrypted) else 0)

            creation_ts = _parse_ts(ds.get("creation"))
            if creation_ts is not None:
                DATASET_CREATION_TS.labels(dataset=name).set(creation_ts)

    # ------------------------------------------------------------------
    # Task health metrics (NEW)
    # ------------------------------------------------------------------

    def _export_task_list(
        self,
        task_type: str,
        tasks: list[Any],
        name_field: str,
        enabled_field: str,
        job_field: str,
        total_count: int | None = None,
    ) -> None:
        """Generic helper to export enabled/state/last-run for a task list."""
        TASK_COUNT.labels(task_type=task_type).set(total_count if total_count is not None else len(tasks))
        for task in tasks[: self.config.max_entity_calls]:
            if not isinstance(task, dict):
                continue
            name = _str_label(task.get(name_field), "unknown")
            enabled = _as_bool(task.get(enabled_field, False))
            TASK_ENABLED.labels(task_type=task_type, name=name).set(1 if enabled else 0)

            job = task.get(job_field)
            if isinstance(job, dict):
                state = _str_label(job.get("state"), "UNKNOWN").upper()
                TASK_STATE.labels(task_type=task_type, name=name, state=state).set(1)

                finished_ts = _parse_ts(job.get("time_finished"))
                if finished_ts is not None:
                    TASK_LAST_RUN_TS.labels(task_type=task_type, name=name).set(finished_ts)
            else:
                # Some task types store state directly (e.g. snapshottask)
                state_raw = task.get("state")
                if state_raw is not None:
                    state = _str_label(state_raw, "UNKNOWN").upper()
                    TASK_STATE.labels(task_type=task_type, name=name, state=state).set(1)

                last_run = task.get("lastrun") or task.get("last_run")
                if last_run is not None:
                    ts = _parse_ts(last_run)
                    if ts is not None:
                        TASK_LAST_RUN_TS.labels(task_type=task_type, name=name).set(ts)

    def _collect_task_metrics(self, client: JsonRpcWsClient) -> None:
        if not self.config.enable_task_metrics:
            return

        # Replication tasks
        try:
            total_count = self._query_count(client, "replication.query")
            items = self._call(client, "replication.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["name", "enabled", "job", "direction"]}
            ])
            if isinstance(items, list):
                self._export_task_list("replication", items, "name", "enabled", "job", total_count)
        except Exception:
            LOG.debug("replication.query failed", exc_info=True)

        # Cloud sync tasks
        try:
            total_count = self._query_count(client, "cloudsync.query")
            items = self._call(client, "cloudsync.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["description", "enabled", "job", "direction"]}
            ])
            if isinstance(items, list):
                self._export_task_list("cloudsync", items, "description", "enabled", "job", total_count)
        except Exception:
            LOG.debug("cloudsync.query failed", exc_info=True)

        # Rsync tasks
        try:
            total_count = self._query_count(client, "rsynctask.query")
            items = self._call(client, "rsynctask.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["desc", "enabled", "job", "direction"]}
            ])
            if isinstance(items, list):
                self._export_task_list("rsynctask", items, "desc", "enabled", "job", total_count)
        except Exception:
            LOG.debug("rsynctask.query failed", exc_info=True)

        # Snapshot tasks — state is stored directly, no job object
        try:
            total_count = self._query_count(client, "pool.snapshottask.query")
            items = self._call(client, "pool.snapshottask.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["dataset", "enabled", "state", "lastrun"]}
            ])
            if isinstance(items, list):
                self._export_task_list("snapshottask", items, "dataset", "enabled", "state", total_count)
        except Exception:
            LOG.debug("pool.snapshottask.query failed", exc_info=True)

        # Snapshot task limits
        try:
            max_count = self._call(client, "pool.snapshottask.max_count", [])
            val = _as_float(max_count)
            if val is not None:
                SNAPSHOT_TASK_MAX_COUNT.set(val)
        except Exception:
            LOG.debug("pool.snapshottask.max_count failed", exc_info=True)

        try:
            max_total = self._call(client, "pool.snapshottask.max_total_count", [])
            val = _as_float(max_total)
            if val is not None:
                SNAPSHOT_TASK_MAX_TOTAL_COUNT.set(val)
        except Exception:
            LOG.debug("pool.snapshottask.max_total_count failed", exc_info=True)

    # ------------------------------------------------------------------
    # Directory services metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_directoryservices_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        try:
            result = cache.get("directoryservices.status") or self._call(client, "directoryservices.status", [])
        except Exception:
            LOG.debug("directoryservices.status failed", exc_info=True)
            return

        if not isinstance(result, dict):
            return

        DIRECTORYSERVICES_STATUS.clear()
        DIRECTORYSERVICES_HEALTHY.clear()
        DIRECTORYSERVICES_FAULT_REASON.clear()

        for service_key in ("activedirectory", "ldap", "nis", "kerberos"):
            svc_data = result.get(service_key)
            if not isinstance(svc_data, dict):
                continue
            status = _str_label(
                svc_data.get("status") or svc_data.get("state"), "UNKNOWN"
            ).upper()
            healthy_statuses = {"HEALTHY", "ACTIVE", "OK", "UP", "RUNNING", "SUCCESS"}
            is_healthy = status in healthy_statuses
            DIRECTORYSERVICES_STATUS.labels(service=service_key, status=status).set(1)
            DIRECTORYSERVICES_HEALTHY.labels(service=service_key).set(1 if is_healthy else 0)

            # Fault reason (status_msg field when FAULTED)
            status_msg = svc_data.get("status_msg")
            if status == "FAULTED" and status_msg:
                reason = _str_label(status_msg, "unknown")
                DIRECTORYSERVICES_FAULT_REASON.labels(service=service_key, reason=reason).set(1)

        # Also handle flat response format (single status at top level)
        top_status = result.get("status")
        if top_status and not any(result.get(k) for k in ("activedirectory", "ldap")):
            status = _str_label(top_status, "UNKNOWN").upper()
            DIRECTORYSERVICES_STATUS.labels(service="directoryservices", status=status).set(1)
            DIRECTORYSERVICES_HEALTHY.labels(service="directoryservices").set(
                1 if status in {"HEALTHY", "ACTIVE", "OK", "UP"} else 0
            )

    # ------------------------------------------------------------------
    # IPMI metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_ipmi_metrics(self, client: JsonRpcWsClient) -> None:
        if not self.config.enable_ipmi_metrics:
            return

        # Clear label-carrying IPMI gauges
        IPMI_CHASSIS_POWER_ON.set(0)
        IPMI_CHASSIS_POWER_OVERLOAD.set(0)
        IPMI_CHASSIS_INTRUSION.set(0)
        IPMI_CHASSIS_DRIVE_FAULT.set(0)
        IPMI_CHASSIS_FAN_FAULT.set(0)

        try:
            loaded = self._call(client, "ipmi.is_loaded", [])
        except Exception:
            LOG.debug("ipmi.is_loaded failed", exc_info=True)
            return

        ipmi_available = _as_bool(loaded)
        IPMI_LOADED.set(1 if ipmi_available else 0)
        if not ipmi_available:
            return

        # Chassis info
        try:
            chassis = self._call(client, "ipmi.chassis.info", [])
            if isinstance(chassis, dict):
                power = chassis.get("power_on") or chassis.get("System Power")
                if power is not None:
                    IPMI_CHASSIS_POWER_ON.set(1 if _as_bool(power) else 0)

                # Extended chassis fields (v4)
                power_overload = chassis.get("power_overload")
                if power_overload is not None:
                    IPMI_CHASSIS_POWER_OVERLOAD.set(1 if _as_bool(power_overload) else 0)

                chassis_intrusion = chassis.get("chassis_intrusion")
                if chassis_intrusion is not None:
                    IPMI_CHASSIS_INTRUSION.set(1 if _as_bool(chassis_intrusion) else 0)

                drive_fault = chassis.get("drive_fault")
                if drive_fault is not None:
                    IPMI_CHASSIS_DRIVE_FAULT.set(1 if _as_bool(drive_fault) else 0)

                fan_fault = chassis.get("fan_fault")
                if fan_fault is not None:
                    IPMI_CHASSIS_FAN_FAULT.set(1 if _as_bool(fan_fault) else 0)

                self._extract_generic_metrics("ipmi.chassis.info", chassis, "result", 0)
        except Exception:
            LOG.debug("ipmi.chassis.info failed", exc_info=True)

        # System Event Log summary
        try:
            sel_info = self._call(client, "ipmi.sel.info", [])
            if isinstance(sel_info, dict):
                entries = _as_float(
                    sel_info.get("entries") or sel_info.get("Number of log entries")
                )
                if entries is not None:
                    IPMI_SEL_ENTRY_COUNT.set(entries)
                free_space = _as_float(
                    sel_info.get("free_space") or sel_info.get("Free Space Remaining")
                )
                if free_space is not None:
                    IPMI_SEL_FREE_SPACE_BYTES.set(free_space)
        except Exception:
            LOG.debug("ipmi.sel.info failed", exc_info=True)

    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # Vdev error extraction helper (v3)
    # ------------------------------------------------------------------

    def _extract_vdev_errors(self, pool_name: str, topology: dict[str, Any]) -> None:
        """Walk a pool topology tree and collect read/write/checksum errors per vdev."""
        # Topology structure: {"data": [...vdevs...], "cache": [...], "log": [...], ...}
        for vdev_class in ("data", "cache", "log", "spare", "special", "dedup"):
            vdev_list = topology.get(vdev_class)
            if not isinstance(vdev_list, list):
                continue
            for vdev in vdev_list:
                self._walk_vdev(pool_name, vdev)

    def _walk_vdev(self, pool_name: str, vdev: Any, depth: int = 0) -> None:
        """Recursively walk a vdev (may be a mirror/raidz with children)."""
        if not isinstance(vdev, dict) or depth > 5:
            return
        name = _str_label(vdev.get("name") or vdev.get("path") or vdev.get("guid"), "unknown")
        stats = vdev.get("stats")
        if isinstance(stats, dict):
            for key, gauge in (
                ("read_errors",     POOL_VDEV_READ_ERRORS),
                ("write_errors",    POOL_VDEV_WRITE_ERRORS),
                ("checksum_errors", POOL_VDEV_CHECKSUM_ERRORS),
            ):
                v = _as_float(stats.get(key))
                if v is not None:
                    gauge.labels(pool=pool_name, vdev=name).set(v)
        for child in (vdev.get("children") or []):
            self._walk_vdev(pool_name, child, depth + 1)

    # ------------------------------------------------------------------
    # SMB / NFS session metrics (v3)
    # ------------------------------------------------------------------

    def _collect_smb_nfs_sessions(self, client: JsonRpcWsClient) -> None:
        """Collect active SMB session / connection / open-file counts."""
        try:
            # smb.status returns {"sessions": [...], "connections": [...], "open_files": [...]}
            # or a list of session dicts depending on version.
            smb_status = self._call(client, "smb.status", ["SESSIONS"])
            if isinstance(smb_status, list):
                SMB_SESSION_COUNT.set(len(smb_status))
            elif isinstance(smb_status, dict):
                sessions = smb_status.get("sessions")
                if isinstance(sessions, list):
                    SMB_SESSION_COUNT.set(len(sessions))
                conns = smb_status.get("connections")
                if isinstance(conns, list):
                    SMB_CONNECTION_COUNT.set(len(conns))
                open_files = smb_status.get("open_files")
                if isinstance(open_files, list):
                    SMB_OPEN_FILE_COUNT.set(len(open_files))
        except Exception:
            LOG.debug("smb.status failed", exc_info=True)

        try:
            # smb.status with "SHARE" info_level gives share-level open counts
            smb_shares_status = self._call(client, "smb.status", ["SHARES"])
            if isinstance(smb_shares_status, list):
                total_open = sum(
                    int(s.get("num_open_files", 0))
                    for s in smb_shares_status
                    if isinstance(s, dict)
                )
                SMB_OPEN_FILE_COUNT.set(total_open)
        except Exception:
            LOG.debug("smb.status SHARE failed", exc_info=True)

    # ------------------------------------------------------------------
    # GPU metrics via device.get_info (v3)
    # ------------------------------------------------------------------

    def _collect_gpu_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect GPU device presence and info via device.get_info."""
        try:
            # device.get_info requires a device type argument
            gpus = self._call(client, "device.get_info", [{"type": "GPU"}])
            if not isinstance(gpus, list):
                return
            GPU_COUNT.set(len(gpus))
            GPU_INFO.clear()
            for idx, gpu in enumerate(gpus):
                if not isinstance(gpu, dict):
                    continue
                model = _str_label(gpu.get("description") or gpu.get("name") or gpu.get("model"), "unknown")
                vendor = _str_label(gpu.get("vendor") or gpu.get("vendor_id"), "unknown")
                pci_id = _str_label(gpu.get("pci_id") or gpu.get("addr") or gpu.get("bus_info"), "unknown")
                GPU_INFO.labels(
                    index=str(idx),
                    model=model,
                    vendor=vendor,
                    pci_id=pci_id,
                ).set(1)
        except Exception:
            LOG.debug("device.get_info GPU failed", exc_info=True)

    # ------------------------------------------------------------------
    # JBOF hardware (v3)
    # ------------------------------------------------------------------

    def _collect_jbof_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect JBOF (Just a Bunch of Flash) enclosure count."""
        try:
            jbofs = self._call(client, "jbof.query", [[], {"limit": self.config.query_limit}])
            if isinstance(jbofs, list):
                JBOF_COUNT.set(len(jbofs))
        except Exception:
            LOG.debug("jbof.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # Active API session count (v3)
    # ------------------------------------------------------------------

    def _collect_auth_session_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect number of active authenticated sessions via auth.sessions."""
        try:
            sessions = self._call(client, "auth.sessions", [[], {"limit": self.config.query_limit}])
            if isinstance(sessions, list):
                AUTH_SESSIONS_ACTIVE.set(len(sessions))
        except Exception:
            LOG.debug("auth.sessions failed", exc_info=True)

    # ------------------------------------------------------------------
    # Extended disk info (rotational, SMART) (v3)
    # ------------------------------------------------------------------

    def _collect_disk_extended_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect disk rotational flag and SMART status via disk.query.

        v25.10.2 field names:
          rotationrate  — RPM (0 = SSD/NVMe, >0 = HDD); replaces the old "rotational" bool
          togglesmart   — not present in v25.10.2; SMART enabled status is omitted
        """
        try:
            disks = self._call_query_with_fallback(
                client, "disk.query",
                {"select": ["name", "identifier", "rotationrate", "model", "serial", "bus"]},
            )
            if not isinstance(disks, list):
                return
            DISK_INFO.clear()
            for disk in disks:
                if not isinstance(disk, dict):
                    continue
                dn = _str_label(disk.get("name") or disk.get("identifier"), "unknown")
                # rotationrate: integer RPM; 0 means non-rotational (SSD/NVMe)
                rotationrate = disk.get("rotationrate")
                if rotationrate is not None:
                    DISK_ROTATIONAL.labels(disk=dn).set(1 if int(rotationrate) > 0 else 0)
                # Info-style metric for disk identity
                model = _str_label(disk.get("model"), "")
                serial = _str_label(disk.get("serial"), "")
                bus = _str_label(disk.get("bus"), "")
                DISK_INFO.labels(disk=dn, model=model, serial=serial, bus=bus).set(1)
        except Exception:
            LOG.debug("disk.query extended failed", exc_info=True)

    # ------------------------------------------------------------------
    # SMART test results (v5)
    # ------------------------------------------------------------------

    def _collect_smart_test_results(self, client: JsonRpcWsClient) -> None:
        """Collect last SMART test result per disk via smart.test.results."""
        try:
            results = self._safe_call_auto(client, "smart.test.results")
            if not isinstance(results, list):
                return
            SMART_TEST_LAST_RESULT.clear()
            SMART_TEST_LAST_TIMESTAMP.clear()
            for entry in results:
                if not isinstance(entry, dict):
                    continue
                disk = _str_label(entry.get("disk"), "")
                if not disk:
                    continue
                tests = entry.get("tests")
                if not isinstance(tests, list) or not tests:
                    continue
                # First entry is the most recent test
                latest = tests[0] if isinstance(tests[0], dict) else {}
                status = latest.get("status", "")
                SMART_TEST_LAST_RESULT.labels(disk=disk).set(
                    1 if isinstance(status, str) and "success" in status.lower() else 0
                )
                remaining_pct = _as_float(latest.get("remaining"))
                # If a timestamp is available, use it
                ts = _parse_ts(latest.get("status_verbose") or "")
                if ts is None:
                    ts = _as_float(latest.get("segment_number"))  # fallback
                # We don't have reliable timestamps from all API versions,
                # so only set if we got something meaningful
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="smart_test_results").inc()
            LOG.debug("smart.test.results failed", exc_info=True)

    # ------------------------------------------------------------------
    # Share count metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_share_metrics(self, client: JsonRpcWsClient) -> None:
        try:
            NFS_SHARE_COUNT.set(self._query_count(client, "sharing.nfs.query"))
        except Exception:
            LOG.debug("sharing.nfs.query failed", exc_info=True)

        try:
            SMB_SHARE_COUNT.set(self._query_count(client, "sharing.smb.query"))
        except Exception:
            LOG.debug("sharing.smb.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # System extra metrics (reboot, gateway, identity, HA) (NEW)
    # ------------------------------------------------------------------

    def _collect_system_extra_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        # Pending reboot
        try:
            reboot_info = cache.get("system.reboot.info") or self._call(client, "system.reboot.info", [])
            if isinstance(reboot_info, dict):
                reboot_required = _as_bool(
                    reboot_info.get("reboot_required")
                    or reboot_info.get("required")
                    or bool(reboot_info.get("reasons"))
                )
                SYSTEM_REBOOT_REQUIRED.set(1 if reboot_required else 0)
                SYSTEM_REBOOT_REASON.clear()
                reasons = reboot_info.get("reasons") or []
                if isinstance(reasons, list):
                    for reason in reasons:
                        SYSTEM_REBOOT_REASON.labels(reason=_str_label(reason, "unknown")).set(1)
                elif isinstance(reasons, str) and reasons:
                    SYSTEM_REBOOT_REASON.labels(reason=reasons).set(1)
        except Exception:
            LOG.debug("system.reboot.info failed", exc_info=True)

        # route.ipv4gw_reachable is not called — returns JsonRpcError on
        # TrueNAS 25.x (API signature changed). Gateway reachability is now
        # inferred from route.system_routes having a default gateway entry.
        try:
            routes = self._safe_call_auto(client, "route.system_routes")
            if isinstance(routes, list):
                has_default_gw = any(
                    isinstance(r, dict) and r.get("network") in ("default", "0.0.0.0", "::")
                    for r in routes
                )
                NETWORK_GATEWAY_REACHABLE.set(1 if has_default_gw else 0)
        except Exception:
            LOG.debug("gateway reachability inference failed", exc_info=True)

        # TrueNAS identity flags
        try:
            is_production = cache.get("truenas.is_production")
            if is_production is None:
                is_production = self._call(client, "truenas.is_production", [])
            if is_production is not None:
                TRUENAS_IS_PRODUCTION.set(1 if _as_bool(is_production) else 0)
        except Exception:
            LOG.debug("truenas.is_production failed", exc_info=True)

        try:
            is_ix = cache.get("truenas.is_ix_hardware")
            if is_ix is None:
                is_ix = self._call(client, "truenas.is_ix_hardware", [])
            if is_ix is not None:
                TRUENAS_IS_IX_HARDWARE.set(1 if _as_bool(is_ix) else 0)
        except Exception:
            LOG.debug("truenas.is_ix_hardware failed", exc_info=True)

        # HA failover disabled reasons (no-op / returns [] on non-HA systems)
        try:
            reasons = cache.get("failover.disabled.reasons")
            if reasons is None:
                reasons = self._call(client, "failover.disabled.reasons", [])
            FAILOVER_DISABLED_REASON.clear()
            if isinstance(reasons, list):
                FAILOVER_DISABLED_REASON_COUNT.set(len(reasons))
                for reason in reasons:
                    FAILOVER_DISABLED_REASON.labels(reason=_str_label(reason, "unknown")).set(1)
            else:
                FAILOVER_DISABLED_REASON_COUNT.set(0)
        except Exception:
            LOG.debug("failover.disabled.reasons failed", exc_info=True)

    # ------------------------------------------------------------------
    # Main scrape
    # ------------------------------------------------------------------

    def _discover_all_methods(self, client: JsonRpcWsClient) -> None:
        """Dynamically query core.get_methods and add query/config endpoints to extra_methods."""
        if not self.config.scrape_all_metrics or self._all_methods_discovered:
            return

        try:
            methods = client.call("core.get_methods", [])
            names = sorted(list(methods.keys()))
            added_count = 0

            # Methods we already scrape or that require special handling
            skip_set = set(BASE_METHODS) | set(REQUIRES_ENTITY_PARAM)

            for m in names:
                if m in skip_set:
                    continue

                # Filter for read-only / metadata / status methods
                # Exclude mutations (.create, .update, .delete, .set_, .do_) and internal/auth
                if any(p in m for p in [".create", ".update", ".delete", "auth.", "core.", ".set_", ".do_"]):
                    continue

                # Match typical query patterns
                if (m.endswith(".query") or m.endswith(".config") or m.endswith(".info") or
                    m.endswith(".status") or "stat" in m or "metric" in m or ".get_" in m):
                    
                    if m not in self.config.extra_methods:
                        self.config.extra_methods.append(m)
                        added_count += 1

            if added_count > 0:
                LOG.info("Dynamically discovered %d additional API methods to scrape (total extra: %d)",
                         added_count, len(self.config.extra_methods))
            
            self._all_methods_discovered = True

        except Exception:
            LOG.warning("Dynamic method discovery failed", exc_info=True)

    def scrape_once(self) -> None:
        LAST_SCRAPE_TS.set(time.time())
        success = False

        with self._lock:
            # SCRAPE_DURATION is measured strictly inside the lock so it reflects
            # real API time, not any lock-wait from a concurrent caller.
            started = time.time()

            # Clear label-carrying gauges INSIDE the lock to prevent a window
            # where Prometheus scrapes partially-cleared / partially-refilled data.
            SYSTEM_STATE.clear()
            SYSTEM_REBOOT_REASON.clear()
            BOOT_POOL_STATUS.clear()
            BOOT_POOL_SCAN_STATE.clear()
            POOL_HEALTHY.clear()
            POOL_STATUS.clear()
            POOL_SIZE_BYTES.clear()
            POOL_ALLOCATED_BYTES.clear()
            POOL_FREE_BYTES.clear()
            POOL_SCAN_PERCENT.clear()
            POOL_FRAGMENTATION.clear()
            POOL_AUTOTRIM_ENABLED.clear()
            POOL_DEDUP_RATIO.clear()
            POOL_EXPAND_SIZE_BYTES.clear()
            POOL_WARNING.clear()
            DATASET_USED_BYTES.clear()
            DATASET_AVAILABLE_BYTES.clear()
            DATASET_REFERENCED_BYTES.clear()
            DATASET_QUOTA_BYTES.clear()
            DATASET_REFQUOTA_BYTES.clear()
            DATASET_SNAPSHOT_COUNT.clear()
            DATASET_COMPRESSION_RATIO.clear()
            DATASET_ENCRYPTED.clear()
            DATASET_RESERVATION_BYTES.clear()
            DATASET_REFRESERVATION_BYTES.clear()
            DATASET_USED_BY_CHILDREN_BYTES.clear()
            DATASET_USED_BY_DATASET_BYTES.clear()
            DATASET_USED_BY_SNAPSHOTS_BYTES.clear()
            DATASET_READONLY.clear()
            DATASET_ATIME.clear()
            DATASET_EXEC.clear()
            DATASET_KEY_LOADED.clear()
            DATASET_LOCKED.clear()
            DATASET_QUOTA_WARNING_PERCENT.clear()
            DATASET_QUOTA_CRITICAL_PERCENT.clear()
            DATASET_REFQUOTA_WARNING_PERCENT.clear()
            DATASET_REFQUOTA_CRITICAL_PERCENT.clear()
            DATASET_CREATION_TS.clear()
            DISK_SIZE_BYTES.clear()
            DISK_TEMPERATURE_C.clear()
            DISK_TEMP_ALERT_COUNT.clear()
            DISK_TEMP_AGG_C.clear()
            INTERFACE_LINK_UP.clear()
            INTERFACE_MTU.clear()
            INTERFACE_TYPE.clear()
            SERVICE_ENABLED.clear()
            SERVICE_RUNNING.clear()
            APP_STATE.clear()
            APP_UPGRADE_AVAILABLE.clear()
            APP_IMAGE_UPDATES_AVAILABLE.clear()
            APP_CUSTOM.clear()
            APP_MIGRATED.clear()
            APP_CONTAINER_COUNT.clear()
            APP_USED_PORT_COUNT.clear()
            APP_USED_HOST_IP_COUNT.clear()
            APP_CONTAINER_STATE_COUNT.clear()
            ALERT_COUNT_BY_LEVEL.clear()
            ALERT_COUNT_BY_SOURCE.clear()
            ALERT_COUNT_BY_CLASS.clear()
            ALERT_COUNT_BY_NODE.clear()
            ALERT_LAST_OCCURRENCE_TS.clear()
            JOB_ACTIVE_COUNT_BY_STATE.clear()
            JOB_ACTIVE_COUNT_BY_METHOD.clear()
            JOB_OLDEST_ACTIVE_TS.clear()
            JOB_PROGRESS_PERCENT.clear()
            UPDATE_STATUS.clear()
            VM_VMEMORY_IN_USE_BYTES.clear()
            CERT_DAYS_TO_EXPIRY.clear()
            DIRECTORYSERVICES_STATUS.clear()
            DIRECTORYSERVICES_HEALTHY.clear()
            TASK_ENABLED.clear()
            TASK_STATE.clear()
            TASK_LAST_RUN_TS.clear()
            TASK_COUNT.clear()
            FAILOVER_DISABLED_REASON.clear()
            # v3 additions
            POOL_VDEV_READ_ERRORS.clear()
            POOL_VDEV_WRITE_ERRORS.clear()
            POOL_VDEV_CHECKSUM_ERRORS.clear()
            POOL_REALTIME_READ_BYTES.clear()
            POOL_REALTIME_WRITE_BYTES.clear()
            POOL_SCAN_ERRORS.clear()
            POOL_SCAN_BYTES_PROCESSED.clear()
            POOL_SCAN_BYTES_TOTAL.clear()
            POOL_SCAN_SECONDS_REMAINING.clear()
            POOL_LAST_SCAN_TS.clear()
            GPU_INFO.clear()
            DISK_ROTATIONAL.clear()
            DISK_SMART_ENABLED.clear()
            HOST_CPU_MODEL.clear()
            HOST_SYSTEM_INFO.clear()
            HW_VIRT_VARIANT.clear()
            CHASSIS_HARDWARE.clear()
            METHOD_NUMERIC_VALUE.clear()
            METHOD_BOOLEAN_VALUE.clear()
            METHOD_STATUS_VALUE.clear()
            METHOD_LIST_LENGTH.clear()
            # v4/v5 label-carrying gauges (prevent stale labels on collector failure)
            HOST_INFO.clear()
            SYSTEM_PRODUCT_TYPE.clear()
            SYSTEM_VERSION.clear()
            SYSTEM_HOST_ID.clear()
            DOCKER_STATUS.clear()
            UPS_STATUS.clear()
            TN_CONNECT_STATUS.clear()
            TRUECOMMAND_STATUS.clear()
            VIRT_GLOBAL_STATE.clear()
            UPDATE_VERSION_AVAILABLE.clear()
            # v5 additions
            POOL_SCRUB_TASK_ENABLED.clear()
            POOL_SCRUB_TASK_STATE.clear()
            POOL_SCRUB_LAST_RUN_TS.clear()
            CLOUD_BACKUP_TASK_ENABLED.clear()
            CLOUD_BACKUP_TASK_STATE.clear()
            CRONJOB_ENABLED.clear()
            DISK_IN_USE.clear()
            ALERTSERVICE_ENABLED.clear()
            SYSTEMDATASET_POOL.clear()
            SYSTEM_GLOBAL_ID.clear()
            # API call diagnostics — clear each scrape so methods removed from BASE_METHODS
            # don't leave zombie label series with their last-seen values.
            API_CALL_SUCCESS.clear()
            API_CALL_DURATION.clear()

            try:
                with JsonRpcWsClient(
                    ws_url=self.config.ws_url,
                    timeout_seconds=self.config.timeout_seconds,
                    verify_tls=self.config.verify_tls,
                ) as client:
                    # --- Authentication ---
                    # In TrueNAS 25.x, login_with_api_key returns a session dict;
                    # in older versions it returned True. _as_bool handles both.
                    login_result = self._call(client, "auth.login_with_api_key", [self.config.api_key])
                    if not _as_bool(login_result):
                        raise JsonRpcError("auth.login_with_api_key returned falsy")

                    # --- Dynamic Discovery (if enabled) ---
                    self._discover_all_methods(client)

                    # --- Method discovery & generic extraction ---
                    # result_cache stores every method result from the generic loop.
                    # Dedicated collectors below can read from cache to avoid making
                    # a second round-trip for the same method.
                    result_cache: dict[str, Any] = {}
                    methods_to_call = self._discover_methods(client)
                    self._collect_reporting_timeseries(client, result_cache)
                    self._collect_filesystem_metrics(client)

                    for method in methods_to_call:
                        result = self._safe_call_auto(client, method)
                        if result is not None:
                            result_cache[method] = result
                            self._extract_generic_metrics(method, result, "result", 0)

                    self._collect_entity_detail_metrics(client, result_cache)

                    # --- Dedicated collection methods ---
                    # These use result_cache to avoid re-calling APIs already fetched
                    # in the generic loop above.
                    self._collect_boot_pool_metrics(client)
                    self._collect_certificate_metrics(client)
                    self._collect_dataset_metrics(client)
                    self._collect_job_metrics(client)
                    self._collect_task_metrics(client)
                    self._collect_directoryservices_metrics(client, result_cache)
                    self._collect_ipmi_metrics(client)
                    self._collect_share_metrics(client)
                    self._collect_system_extra_metrics(client, result_cache)
                    # v3 additions
                    self._collect_smb_nfs_sessions(client)
                    self._collect_gpu_metrics(client)
                    self._collect_jbof_metrics(client)
                    self._collect_auth_session_metrics(client)
                    self._collect_disk_extended_metrics(client)
                    self._collect_smart_test_results(client)

                    # --- System state (use cache if already fetched) ---
                    state_raw = result_cache.get("system.state")
                    if state_raw is None:
                        state_raw = self._call(client, "system.state", [])
                    state_label = _str_label(state_raw).upper()
                    SYSTEM_STATE.labels(state=state_label).set(1)
                    SYSTEM_READY.set(1 if state_label == "READY" else 0)

                    # --- Host info (use cache if already fetched) ---
                    info = result_cache.get("system.info")
                    if info is None:
                        info = self._call(client, "system.info", [])
                    self._export_host_metrics(info)

                    # --- VM memory (use cache) ---
                    vm_available = result_cache.get("vm.get_available_memory")
                    if vm_available is None:
                        vm_available = self._safe_call_auto(client, "vm.get_available_memory")
                    vm_av_val = _as_float(vm_available)
                    if vm_av_val is not None:
                        VM_AVAILABLE_MEMORY_BYTES.set(vm_av_val)

                    vm_vmemory = result_cache.get("vm.get_vmemory_in_use")
                    if vm_vmemory is None:
                        vm_vmemory = self._safe_call_auto(client, "vm.get_vmemory_in_use")
                    if isinstance(vm_vmemory, dict):
                        for state_name, state_value in vm_vmemory.items():
                            numeric = _as_float(state_value)
                            if numeric is not None:
                                VM_VMEMORY_IN_USE_BYTES.labels(state=_str_label(state_name).upper()).set(numeric)

                    # --- Network summary (use cache) ---
                    network_summary = result_cache.get("network.general.summary")
                    if network_summary is None:
                        network_summary = self._safe_call_auto(client, "network.general.summary")
                    if isinstance(network_summary, dict):
                        routes = network_summary.get("default_routes")
                        if isinstance(routes, list):
                            NETWORK_DEFAULT_ROUTES.set(len(routes))
                        nameservers = network_summary.get("nameservers")
                        if isinstance(nameservers, list):
                            NETWORK_NAMESERVERS.set(len(nameservers))

                    # --- Docker (use cache) ---
                    nvidia_present = result_cache.get("docker.nvidia_present")
                    if nvidia_present is None:
                        nvidia_present = self._safe_call_auto(client, "docker.nvidia_present")
                    if isinstance(nvidia_present, bool):
                        DOCKER_NVIDIA_PRESENT.set(1 if nvidia_present else 0)

                    docker_networks = result_cache.get("docker.network.query")
                    if docker_networks is None:
                        docker_networks = self._safe_call_auto(client, "docker.network.query")
                    if isinstance(docker_networks, list):
                        DOCKER_NETWORK_COUNT.set(len(docker_networks))

                    # Docker status (dedicated gauge for clean alerting)
                    try:
                        docker_status = result_cache.get("docker.status")
                        if docker_status is None:
                            docker_status = self._safe_call_auto(client, "docker.status")
                        if isinstance(docker_status, dict):
                            docker_status = docker_status.get("status", "")
                        if isinstance(docker_status, str) and docker_status:
                            DOCKER_STATUS.clear()
                            DOCKER_STATUS.labels(status=docker_status.upper()).set(1)
                    except Exception:
                        LOG.debug("docker.status failed", exc_info=True)

                    # NFS client count (dedicated gauge)
                    try:
                        nfs_clients = result_cache.get("nfs.client_count")
                        if nfs_clients is None:
                            nfs_clients = self._safe_call_auto(client, "nfs.client_count")
                        nfs_val = _as_float(nfs_clients)
                        if nfs_val is not None:
                            NFS_CLIENT_COUNT.set(nfs_val)
                    except Exception:
                        LOG.debug("nfs.client_count failed", exc_info=True)

                    # NFS v3 / v4 client count breakdown (dedicated gauges)
                    try:
                        nfs3 = result_cache.get("nfs.get_nfs3_clients")
                        if nfs3 is None:
                            nfs3 = self._safe_call_auto(client, "nfs.get_nfs3_clients")
                        if isinstance(nfs3, list):
                            NFS_V3_CLIENT_COUNT.set(len(nfs3))
                    except Exception:
                        LOG.debug("nfs.get_nfs3_clients failed", exc_info=True)

                    try:
                        nfs4 = result_cache.get("nfs.get_nfs4_clients")
                        if nfs4 is None:
                            nfs4 = self._safe_call_auto(client, "nfs.get_nfs4_clients")
                        if isinstance(nfs4, list):
                            NFS_V4_CLIENT_COUNT.set(len(nfs4))
                    except Exception:
                        LOG.debug("nfs.get_nfs4_clients failed", exc_info=True)

                    # iSCSI client count (dedicated gauge)
                    try:
                        iscsi_clients = result_cache.get("iscsi.global.client_count")
                        if iscsi_clients is None:
                            iscsi_clients = self._safe_call_auto(client, "iscsi.global.client_count")
                        iscsi_val = _as_float(iscsi_clients)
                        if iscsi_val is not None:
                            ISCSI_CLIENT_COUNT.set(iscsi_val)
                    except Exception:
                        LOG.debug("iscsi.global.client_count failed", exc_info=True)

                    # --- Pools ---
                    # Use a fresh call with rich select params rather than the generic
                    # cache entry (which may have been fetched with no select).
                    pools = self._call_query_with_fallback(
                        client, "pool.query",
                        {"select": ["name", "healthy", "warning", "status", "size", "allocated", "free", "scan", "fragmentation", "topology", "autotrim", "dedup_table_size", "expand"]},
                    )
                    pool_list = pools if isinstance(pools, list) else []
                    POOL_COUNT.set(len(pool_list))
                    for pool in pool_list:
                        if not isinstance(pool, dict):
                            continue
                        pool_name = _str_label(pool.get("name"), "unnamed")
                        POOL_HEALTHY.labels(pool=pool_name).set(1 if _as_bool(pool.get("healthy")) else 0)
                        POOL_WARNING.labels(pool=pool_name).set(1 if _as_bool(pool.get("warning")) else 0)
                        POOL_STATUS.labels(
                            pool=pool_name,
                            status=_str_label(pool.get("status"), "UNKNOWN").upper(),
                        ).set(1)
                        for gauge, field in (
                            (POOL_SIZE_BYTES, "size"),
                            (POOL_ALLOCATED_BYTES, "allocated"),
                            (POOL_FREE_BYTES, "free"),
                        ):
                            val = _as_float(pool.get(field))
                            if val is not None:
                                gauge.labels(pool=pool_name).set(val)

                        frag = _as_float(pool.get("fragmentation"))
                        if frag is not None:
                            POOL_FRAGMENTATION.labels(pool=pool_name).set(frag)

                        # Autotrim (v5 addition)
                        autotrim = pool.get("autotrim")
                        if isinstance(autotrim, dict):
                            POOL_AUTOTRIM_ENABLED.labels(pool=pool_name).set(
                                1 if _as_bool(autotrim.get("value")) else 0
                            )
                        elif autotrim is not None:
                            POOL_AUTOTRIM_ENABLED.labels(pool=pool_name).set(
                                1 if _as_bool(autotrim) else 0
                            )

                        # Dedup ratio (v5 addition)
                        dedup = _as_float(pool.get("dedup_table_size"))
                        if dedup is not None:
                            POOL_DEDUP_RATIO.labels(pool=pool_name).set(dedup)

                        # Expand size (v5 addition)
                        expand = pool.get("expand")
                        if isinstance(expand, dict):
                            expand_size = _as_float(expand.get("size"))
                            if expand_size is not None:
                                POOL_EXPAND_SIZE_BYTES.labels(pool=pool_name).set(expand_size)

                        scan = pool.get("scan")
                        if isinstance(scan, dict):
                            pct = _as_float(scan.get("percentage"))
                            if pct is not None:
                                POOL_SCAN_PERCENT.labels(pool=pool_name).set(pct)
                            # Detailed scan stats (v3 addition)
                            errors = _as_float(scan.get("errors"))
                            if errors is not None:
                                POOL_SCAN_ERRORS.labels(pool=pool_name).set(errors)
                            bytes_proc = _as_float(scan.get("bytes_processed"))
                            if bytes_proc is not None:
                                POOL_SCAN_BYTES_PROCESSED.labels(pool=pool_name).set(bytes_proc)
                            bytes_tot = _as_float(scan.get("bytes_to_process"))
                            if bytes_tot is not None:
                                POOL_SCAN_BYTES_TOTAL.labels(pool=pool_name).set(bytes_tot)
                            secs_remaining = _as_float(scan.get("total_secs_left"))
                            if secs_remaining is not None:
                                POOL_SCAN_SECONDS_REMAINING.labels(pool=pool_name).set(secs_remaining)
                            end_ts = scan.get("end_time")
                            if end_ts:
                                ts = _parse_ts(end_ts)
                                if ts is not None:
                                    POOL_LAST_SCAN_TS.labels(pool=pool_name).set(ts)

                        # Vdev error stats (v3 addition) — walk topology tree
                        topology = pool.get("topology")
                        if isinstance(topology, dict):
                            self._extract_vdev_errors(pool_name, topology)

                    # --- Disks ---
                    # Fresh call with extra fields not included in the generic pass.
                    disks = self._call_query_with_fallback(
                        client, "disk.query",
                        {"extra": {"pools": True}, "select": ["name", "identifier", "size"]},
                    )
                    disk_list = disks if isinstance(disks, list) else []
                    DISK_COUNT.set(len(disk_list))
                    disk_names: list[str] = []
                    for disk in disk_list:
                        if not isinstance(disk, dict):
                            continue
                        disk_name = _str_label(disk.get("name") or disk.get("identifier"), "unknown")
                        disk_names.append(disk_name)
                        size = _as_float(disk.get("size"))
                        if size is not None:
                            DISK_SIZE_BYTES.labels(disk=disk_name).set(size)

                    if disk_names:
                        try:
                            alerts = self._call(client, "disk.temperature_alerts", [disk_names])
                            if isinstance(alerts, dict):
                                for disk_name, payload in alerts.items():
                                    count = len(payload) if isinstance(payload, list) else (1 if payload else 0)
                                    DISK_TEMP_ALERT_COUNT.labels(disk=_str_label(disk_name)).set(count)
                        except Exception:
                            LOG.debug("disk.temperature_alerts failed", exc_info=True)

                        try:
                            temp_agg = self._call(client, "disk.temperature_agg", [disk_names, 7])
                            if isinstance(temp_agg, dict):
                                for disk_name, agg in temp_agg.items():
                                    if isinstance(agg, dict):
                                        for kind in ("min", "max", "avg"):
                                            val = _as_float(agg.get(kind))
                                            if val is not None:
                                                DISK_TEMP_AGG_C.labels(
                                                    disk=_str_label(disk_name), kind=kind,
                                                ).set(val)
                        except Exception:
                            LOG.debug("disk.temperature_agg failed", exc_info=True)

                    # disk.temperatures: use cache when available
                    temps = result_cache.get("disk.temperatures")
                    if temps is None:
                        try:
                            temps = self._call(client, "disk.temperatures", [])
                        except Exception:
                            LOG.debug("disk.temperatures not available", exc_info=True)
                            temps = None
                    if isinstance(temps, dict):
                        for disk_name, temp_value in temps.items():
                            temp = _as_float(temp_value)
                            if temp is not None:
                                DISK_TEMPERATURE_C.labels(disk=_str_label(disk_name)).set(temp)

                    # --- Interfaces (fresh call with rich extra params) ---
                    interfaces = self._call_query_with_fallback(
                        client, "interface.query",
                        {"extra": {"retrieve_names_only": False}},
                    )
                    iface_list = interfaces if isinstance(interfaces, list) else []
                    INTERFACE_COUNT.set(len(iface_list))
                    for iface in iface_list:
                        if not isinstance(iface, dict):
                            continue
                        name = _str_label(iface.get("name"), "unknown")
                        candidate = iface.get("state")
                        if isinstance(candidate, dict):
                            link_up = _as_bool(
                                candidate.get("link_state")
                                or candidate.get("up")
                                or candidate.get("state")
                            )
                        else:
                            link_up = _as_bool(iface.get("up") or iface.get("link_state"))
                        INTERFACE_LINK_UP.labels(interface=name).set(1 if link_up else 0)

                        # Interface MTU
                        mtu = _as_float(iface.get("mtu"))
                        if mtu is not None:
                            INTERFACE_MTU.labels(interface=name).set(mtu)

                        # Interface type (PHYSICAL/BRIDGE/LINK_AGGREGATION/VLAN)
                        iface_type = _str_label(iface.get("type"), "unknown")
                        if iface_type and iface_type != "unknown":
                            INTERFACE_TYPE.labels(interface=name, type=iface_type).set(1)

                    # --- Services (fresh call with rich select/extra params) ---
                    services = self._call_query_with_fallback(
                        client, "service.query",
                        {"extra": {"include_state": True}, "select": ["service", "enable", "state"]},
                    )
                    service_list = services if isinstance(services, list) else []
                    SERVICE_COUNT.set(len(service_list))
                    for svc in service_list:
                        if not isinstance(svc, dict):
                            continue
                        name = _str_label(svc.get("service") or svc.get("name"), "unknown")
                        SERVICE_ENABLED.labels(service=name).set(1 if _as_bool(svc.get("enable")) else 0)
                        state = svc.get("state")
                        running = _as_bool(state.get("running") if isinstance(state, dict) else state)
                        SERVICE_RUNNING.labels(service=name).set(1 if running else 0)

                    # --- Alerts (use cache) ---
                    alerts_raw = result_cache.get("alert.list")
                    if alerts_raw is None:
                        alerts_raw = self._call(client, "alert.list", [])
                    self._export_alert_metrics(alerts_raw)

                    # --- Update status (use cache) ---
                    update = result_cache.get("update.status")
                    if update is None:
                        update = self._call(client, "update.status", [])
                    if isinstance(update, dict):
                        status_label = _str_label(
                            update.get("status") or update.get("code") or update.get("state"),
                            "UNKNOWN",
                        ).upper()
                        UPDATE_STATUS.labels(status=status_label).set(1)
                        update_available = _as_bool(
                            update.get("available")
                            or update.get("update_available")
                            or (status_label not in {"UNAVAILABLE", "UP_TO_DATE", "UNKNOWN"})
                        )
                        UPDATE_AVAILABLE.set(1 if update_available else 0)
                    else:
                        UPDATE_AVAILABLE.set(0)

                    # --- System extras (product type, version, IDs) ---
                    self._collect_system_extras(client, result_cache)

                    # --- Update extras (available versions) ---
                    self._collect_update_extras(client, result_cache)

                    # --- Boot environments ---
                    self._collect_boot_env_metrics(client, result_cache)

                    # --- VM extras (virtualization gate, vCPU capacity) ---
                    self._collect_vm_extras(client, result_cache)

                    # --- Virt / Incus (TrueNAS 25.x) ---
                    self._collect_virt_metrics(client, result_cache)

                    # --- Fibre Channel ---
                    self._collect_fc_metrics(client, result_cache)

                    # --- NVMe-oF ---
                    self._collect_nvmet_metrics(client, result_cache)

                    # --- iSCSI protocol extras ---
                    self._collect_iscsi_extras(client, result_cache)

                    # --- Network extras ---
                    self._collect_network_extras(client, result_cache)

                    # --- App extras (available space, WebDAV shares) ---
                    self._collect_app_extras(client, result_cache)

                    # --- UPS ---
                    self._collect_ups_metrics(client, result_cache)

                    # --- Catalog ---
                    self._collect_catalog_metrics(client, result_cache)

                    # --- v4 additions: Security / FIPS ---
                    self._collect_fips_metrics(client, result_cache)

                    # --- v4 additions: Feature flags ---
                    self._collect_feature_flags(client)

                    # --- v4 additions: Hardware / Chassis ---
                    self._collect_chassis_hardware(client, result_cache)

                    # --- v4 additions: TrueNAS Connect ---
                    self._collect_tn_connect(client, result_cache)

                    # --- v4 additions: TrueCommand status ---
                    self._collect_truecommand_status(client, result_cache)

                    # --- v4 additions: Audit ---
                    self._collect_audit_metrics(client, result_cache)

                    # --- IPMI LAN (with correct channel params) ---
                    self._collect_ipmi_lan_metrics(client, result_cache)

                    # ── v5 collectors ──
                    self._collect_scrub_task_metrics(client, result_cache)
                    self._collect_snapshot_metrics(client, result_cache)
                    self._collect_resilver_config(client, result_cache)
                    self._collect_cloud_backup_metrics(client, result_cache)
                    self._collect_cronjob_metrics(client, result_cache)
                    self._collect_disk_used_metrics(client, result_cache)
                    self._collect_protocol_configs(client, result_cache)
                    self._collect_system_configs(client, result_cache)
                    self._collect_infrastructure_configs(client, result_cache)
                    self._collect_inventory_counts(client, result_cache)
                    self._collect_iscsi_inventory(client, result_cache)
                    self._collect_nvmet_extended(client, result_cache)
                    self._collect_misc_configs(client, result_cache)
                    self._collect_security_posture(client, result_cache)

                    success = True

            except Exception:
                LOG.exception("Scrape failed")
                success = False

        SCRAPE_SUCCESS.set(1 if success else 0)
        SCRAPE_DURATION.set(max(0.0, time.time() - started))

    # ------------------------------------------------------------------
    # System extras (product type, version, IDs)
    # ------------------------------------------------------------------

    def _collect_system_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect system product type, version string, host/boot IDs."""
        # product_type
        try:
            pt = cache.get("system.product_type") or self._call(client, "system.product_type", [])
            if isinstance(pt, str):
                SYSTEM_PRODUCT_TYPE.clear()
                SYSTEM_PRODUCT_TYPE.labels(product_type=pt.upper()).set(1)
        except Exception:
            LOG.debug("system.product_type failed", exc_info=True)

        # version_short
        try:
            vs = cache.get("system.version_short") or self._call(client, "system.version_short", [])
            if isinstance(vs, str):
                SYSTEM_VERSION.clear()
                SYSTEM_VERSION.labels(version=vs).set(1)
        except Exception:
            LOG.debug("system.version_short failed", exc_info=True)

        # host_id: stable UUID across reboots — safe as a label (1 series per system)
        try:
            hid = cache.get("system.host_id") or self._call(client, "system.host_id", [])
            if isinstance(hid, str):
                SYSTEM_HOST_ID.clear()
                SYSTEM_HOST_ID.labels(host_id=hid).set(1)
        except Exception:
            LOG.debug("system.host_id failed", exc_info=True)

        # boot_id: changes every reboot — we track *changes* via a Counter rather than
        # exposing the UUID as a label (which would create zombie series in Prometheus
        # after each reboot that never get cleaned up).
        try:
            bid = cache.get("system.boot_id") or self._call(client, "system.boot_id", [])
            if isinstance(bid, str):
                if self._last_boot_id is not None and bid != self._last_boot_id:
                    SYSTEM_BOOT_CHANGES_TOTAL.inc()
                    LOG.info("Boot ID changed: system has rebooted (new boot_id=%s)", bid)
                self._last_boot_id = bid
        except Exception:
            LOG.debug("system.boot_id failed", exc_info=True)

        # managed_by_truecommand
        try:
            mtc = cache.get("truenas.managed_by_truecommand")
            if mtc is None:
                mtc = self._call(client, "truenas.managed_by_truecommand", [])
            SYSTEM_MANAGED_BY_TRUECOMMAND.set(1 if _as_bool(mtc) else 0)
        except Exception:
            LOG.debug("truenas.managed_by_truecommand failed", exc_info=True)

    # ------------------------------------------------------------------
    # Update extras (available version names)
    # ------------------------------------------------------------------

    def _collect_update_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Expose available update versions as labelled metrics."""
        try:
            versions = cache.get("update.available_versions") or self._call(client, "update.available_versions", [])
        except Exception:
            LOG.debug("update.available_versions failed", exc_info=True)
            return

        UPDATE_VERSION_AVAILABLE.clear()
        if isinstance(versions, list):
            for v in versions[: self.config.max_list_items]:
                ver_str = None
                if isinstance(v, str):
                    ver_str = v
                elif isinstance(v, dict):
                    ver_str = _str_label(
                        v.get("version") or v.get("name") or v.get("label"), "unknown"
                    )
                if ver_str:
                    UPDATE_VERSION_AVAILABLE.labels(version=ver_str).set(1)
        elif isinstance(versions, dict):
            for key in versions:
                UPDATE_VERSION_AVAILABLE.labels(version=_str_label(key, "unknown")).set(1)

    # ------------------------------------------------------------------
    # Boot environments
    # ------------------------------------------------------------------

    def _collect_boot_env_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect boot environment inventory and keep/active flags."""
        try:
            envs = cache.get("boot.environment.query") or self._call(client, "boot.environment.query", [
                [], {"select": ["id", "active", "activated", "keep", "created", "used_bytes"]}
            ])
        except Exception:
            LOG.debug("boot.environment.query failed", exc_info=True)
            return

        if not isinstance(envs, list):
            return

        BOOT_ENV_COUNT.set(len(envs))
        active_count = 0
        keep_count = 0
        BOOT_ENV_ACTIVE.clear()
        BOOT_ENV_KEEP.clear()
        BOOT_ENV_SIZE_BYTES.clear()

        for env in envs[: self.config.max_list_items]:
            if not isinstance(env, dict):
                continue
            name = _str_label(env.get("id") or env.get("name"), "unknown")
            active = _as_bool(env.get("active") or env.get("activated"))
            keep = _as_bool(env.get("keep"))
            if active:
                active_count += 1
            if keep:
                keep_count += 1
            BOOT_ENV_ACTIVE.labels(name=name).set(1 if active else 0)
            BOOT_ENV_KEEP.labels(name=name).set(1 if keep else 0)
            rawspace = _as_float(env.get("used_bytes") or env.get("rawspace") or env.get("size"))
            if rawspace is not None:
                BOOT_ENV_SIZE_BYTES.labels(name=name).set(rawspace)

        BOOT_ENV_ACTIVE_COUNT.set(active_count)
        BOOT_ENV_KEEP_COUNT.set(keep_count)

    # ------------------------------------------------------------------
    # VM extras (virtualization gate, capacity)
    # ------------------------------------------------------------------

    def _collect_vm_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect KVM support flag and vCPU capacity."""
        try:
            sv = cache.get("vm.supports_virtualization")
            if sv is None:
                sv = self._call(client, "vm.supports_virtualization", [])
            VM_SUPPORTS_VIRTUALIZATION.set(1 if _as_bool(sv) else 0)
        except Exception:
            LOG.debug("vm.supports_virtualization failed", exc_info=True)

        try:
            max_vcpus = cache.get("vm.maximum_supported_vcpus")
            if max_vcpus is None:
                max_vcpus = self._call(client, "vm.maximum_supported_vcpus", [])
            val = _as_float(max_vcpus)
            if val is not None:
                VM_MAX_VCPUS.set(val)
        except Exception:
            LOG.debug("vm.maximum_supported_vcpus failed", exc_info=True)

        # Hardware virtualization variant
        try:
            hw_var = cache.get("hardware.virtualization.variant")
            if hw_var is None:
                hw_var = self._safe_call_auto(client, "hardware.virtualization.variant")
            var_str = _str_label(hw_var, "unknown")
            if var_str and var_str != "unknown":
                HW_VIRT_VARIANT.labels(variant=var_str).set(1)
        except Exception:
            LOG.debug("hardware.virtualization.variant failed", exc_info=True)

    # ------------------------------------------------------------------
    # Virt (Incus/LXD — TrueNAS 25.x)
    # ------------------------------------------------------------------

    def _collect_virt_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect Incus/LXD container instance and volume metrics."""
        # Instances
        try:
            instances = cache.get("virt.instance.query") or self._call(client, "virt.instance.query", [
                [], {"select": ["name", "type", "status", "cpu_usage", "memory_stats"]}
            ])
        except Exception:
            LOG.debug("virt.instance.query failed", exc_info=True)
            instances = None

        if isinstance(instances, list):
            VIRT_INSTANCE_COUNT.set(len(instances))
            VIRT_INSTANCE_RUNNING.clear()
            VIRT_INSTANCE_CPU.clear()
            VIRT_INSTANCE_MEM.clear()
            for inst in instances[: self.config.max_entity_calls]:
                if not isinstance(inst, dict):
                    continue
                name = _str_label(inst.get("name"), "unknown")
                inst_type = _str_label(inst.get("type"), "CONTAINER").upper()
                status = _str_label(inst.get("status"), "UNKNOWN").upper()
                running = status in {"RUNNING", "STARTED", "UP"}
                VIRT_INSTANCE_RUNNING.labels(name=name, type=inst_type).set(1 if running else 0)

                cpu_usage = _as_float(inst.get("cpu_usage"))
                if cpu_usage is not None:
                    VIRT_INSTANCE_CPU.labels(name=name).set(cpu_usage)

                mem_stats = inst.get("memory_stats")
                if isinstance(mem_stats, dict):
                    mem_used = _as_float(mem_stats.get("usage") or mem_stats.get("used"))
                    if mem_used is not None:
                        VIRT_INSTANCE_MEM.labels(name=name).set(mem_used)
        else:
            VIRT_INSTANCE_COUNT.set(0)

        # Volumes
        try:
            volumes = cache.get("virt.volume.query") or self._call(client, "virt.volume.query", [
                [], {"select": ["name", "pool", "content_type", "used_by", "size"]}
            ])
        except Exception:
            LOG.debug("virt.volume.query failed", exc_info=True)
            volumes = None

        if isinstance(volumes, list):
            VIRT_VOLUME_COUNT.set(len(volumes))
            VIRT_VOLUME_SIZE_BYTES.clear()
            for vol in volumes[: self.config.max_list_items]:
                if not isinstance(vol, dict):
                    continue
                name = _str_label(vol.get("name"), "unknown")
                pool = _str_label(vol.get("pool"), "default")
                size = _as_float(vol.get("size"))
                if size is not None:
                    VIRT_VOLUME_SIZE_BYTES.labels(name=name, pool=pool).set(size)
        else:
            VIRT_VOLUME_COUNT.set(0)

        # Virt global config (state)
        try:
            virt_global = cache.get("virt.global.config") or self._call(client, "virt.global.config", [])
            if isinstance(virt_global, dict):
                state = _str_label(virt_global.get("state"), "UNKNOWN").upper()
                if state and state != "UNKNOWN":
                    VIRT_GLOBAL_STATE.clear()
                    VIRT_GLOBAL_STATE.labels(state=state).set(1)
        except Exception:
            LOG.debug("virt.global.config failed", exc_info=True)

    # ------------------------------------------------------------------
    # Fibre Channel
    # ------------------------------------------------------------------

    def _collect_fc_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect Fibre Channel host and port metrics."""
        # FC hosts (HBAs)
        try:
            fc_hosts = cache.get("fc.fc_host.query") or self._call(client, "fc.fc_host.query", [
                [], {"select": ["id", "wwpn", "wwnn", "port_state", "port_type", "speed"]}
            ])
        except Exception:
            LOG.debug("fc.fc_host.query failed", exc_info=True)
            fc_hosts = None

        if isinstance(fc_hosts, list):
            FC_HOST_COUNT.set(len(fc_hosts))
        else:
            FC_HOST_COUNT.set(0)

        # FC port status
        try:
            fc_ports = cache.get("fcport.status") or self._call(client, "fcport.status", [])
        except Exception:
            LOG.debug("fcport.status failed", exc_info=True)
            fc_ports = None

        if isinstance(fc_ports, list):
            FC_PORT_COUNT.set(len(fc_ports))
            FC_PORT_ONLINE.clear()
            FC_PORT_SPEED.clear()
            for port in fc_ports[: self.config.max_list_items]:
                if not isinstance(port, dict):
                    continue
                port_name = _str_label(
                    port.get("port") or port.get("name") or port.get("id"), "unknown"
                )
                state = _str_label(port.get("state") or port.get("port_state"), "UNKNOWN").upper()
                online = state in {"ONLINE", "UP", "LINKED"}
                FC_PORT_ONLINE.labels(port=port_name).set(1 if online else 0)
                speed_raw = port.get("speed") or port.get("link_speed")
                if speed_raw is not None:
                    speed = _as_float(str(speed_raw).replace("Gbit", "").replace("Gb/s", "").strip())
                    if speed is not None:
                        FC_PORT_SPEED.labels(port=port_name).set(speed)
        elif isinstance(fc_ports, dict):
            # fcport.status may return a dict keyed by port
            FC_PORT_COUNT.set(len(fc_ports))
            FC_PORT_ONLINE.clear()
            for port_name, port_data in list(fc_ports.items())[: self.config.max_list_items]:
                pname = _str_label(port_name, "unknown")
                if isinstance(port_data, dict):
                    state = _str_label(port_data.get("state") or port_data.get("port_state"), "UNKNOWN").upper()
                    online = state in {"ONLINE", "UP", "LINKED"}
                    FC_PORT_ONLINE.labels(port=pname).set(1 if online else 0)
        else:
            FC_PORT_COUNT.set(0)

    # ------------------------------------------------------------------
    # NVMe-oF
    # ------------------------------------------------------------------

    def _collect_nvmet_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect NVMe-oF session, subsystem, and port counts."""
        # Sessions
        try:
            sessions = cache.get("nvmet.global.sessions")
            if sessions is None:
                sessions = self._call(client, "nvmet.global.sessions", [])
            val = _as_float(sessions)
            if val is not None:
                NVMET_SESSION_COUNT.set(val)
            elif isinstance(sessions, list):
                NVMET_SESSION_COUNT.set(len(sessions))
        except Exception:
            LOG.debug("nvmet.global.sessions failed", exc_info=True)

        # Subsystems
        try:
            subsys = cache.get("nvmet.subsys.query") or self._call(client, "nvmet.subsys.query", [
                [], {"select": ["id", "name", "subnqn"]}
            ])
            if isinstance(subsys, list):
                NVMET_SUBSYS_COUNT.set(len(subsys))
        except Exception:
            LOG.debug("nvmet.subsys.query failed", exc_info=True)

        # Ports
        try:
            ports = cache.get("nvmet.port.query") or self._call(client, "nvmet.port.query", [
                [], {"select": ["id", "addr_trtype", "addr_trsvcid", "addr_traddr"]}
            ])
            if isinstance(ports, list):
                NVMET_PORT_COUNT.set(len(ports))
        except Exception:
            LOG.debug("nvmet.port.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # iSCSI protocol extras
    # ------------------------------------------------------------------

    def _collect_iscsi_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect ALUA and iSER protocol flags."""
        try:
            alua = cache.get("iscsi.global.alua_enabled")
            if alua is None:
                alua = self._call(client, "iscsi.global.alua_enabled", [])
            ISCSI_ALUA_ENABLED.set(1 if _as_bool(alua) else 0)
        except Exception:
            LOG.debug("iscsi.global.alua_enabled failed", exc_info=True)

        try:
            iser = cache.get("iscsi.global.iser_enabled")
            if iser is None:
                iser = self._call(client, "iscsi.global.iser_enabled", [])
            ISCSI_ISER_ENABLED.set(1 if _as_bool(iser) else 0)
        except Exception:
            LOG.debug("iscsi.global.iser_enabled failed", exc_info=True)

    # ------------------------------------------------------------------
    # Network extras
    # ------------------------------------------------------------------

    def _collect_network_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect pending changes flag and checkin_waiting timer."""
        try:
            pending = cache.get("interface.has_pending_changes")
            if pending is None:
                pending = self._call(client, "interface.has_pending_changes", [])
            INTERFACE_HAS_PENDING_CHANGES.set(1 if _as_bool(pending) else 0)
        except Exception:
            LOG.debug("interface.has_pending_changes failed", exc_info=True)

        try:
            waiting = cache.get("interface.checkin_waiting")
            if waiting is None:
                waiting = self._call(client, "interface.checkin_waiting", [])
            val = _as_float(waiting)
            INTERFACE_CHECKIN_WAITING_SECONDS.set(val if val is not None else 0)
        except Exception:
            LOG.debug("interface.checkin_waiting failed", exc_info=True)

    # ------------------------------------------------------------------
    # App extras
    # ------------------------------------------------------------------

    def _collect_app_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect app available space and WebDAV share count."""
        try:
            space = cache.get("app.available_space")
            if space is None:
                space = self._call(client, "app.available_space", [])
            val = _as_float(space)
            if val is not None:
                APP_AVAILABLE_SPACE_BYTES.set(val)
        except Exception:
            LOG.debug("app.available_space failed", exc_info=True)

        # sharing.webshare.query does not exist in v25.10.2 — method removed upstream

    # ------------------------------------------------------------------
    # UPS metrics
    # ------------------------------------------------------------------

    def _collect_ups_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect UPS configuration and status."""
        try:
            ups = cache.get("ups.config") or self._call(client, "ups.config", [])
        except Exception:
            LOG.debug("ups.config failed", exc_info=True)
            return

        if not isinstance(ups, dict):
            UPS_CONFIGURED.set(0)
            return

        driver = ups.get("driver") or ups.get("port") or ""
        configured = bool(driver)
        UPS_CONFIGURED.set(1 if configured else 0)

        # status is typically stored in ups.config as mode or status string
        status = _str_label(
            ups.get("status") or ups.get("mode") or ups.get("powerdown"), "UNKNOWN"
        ).upper()
        if status and status != "UNKNOWN":
            UPS_STATUS.clear()
            UPS_STATUS.labels(status=status).set(1)

    # ------------------------------------------------------------------
    # Catalog metrics
    # ------------------------------------------------------------------

    def _collect_catalog_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect app catalog train count."""
        try:
            trains = cache.get("catalog.trains") or self._call(client, "catalog.trains", [])
            if isinstance(trains, list):
                CATALOG_TRAIN_COUNT.set(len(trains))
            elif isinstance(trains, dict):
                CATALOG_TRAIN_COUNT.set(len(trains))
        except Exception:
            LOG.debug("catalog.trains failed", exc_info=True)

    # ------------------------------------------------------------------
    # Security / FIPS metrics (v4)
    # ------------------------------------------------------------------

    def _collect_fips_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect FIPS availability and enabled status (v25+)."""
        try:
            fips_available = cache.get("system.security.info.fips_available")
            if fips_available is None:
                fips_available = self._call(client, "system.security.info.fips_available", [])
            FIPS_AVAILABLE.set(1 if _as_bool(fips_available) else 0)
        except Exception:
            LOG.debug("system.security.info.fips_available failed", exc_info=True)

        try:
            fips_enabled = cache.get("system.security.info.fips_enabled")
            if fips_enabled is None:
                fips_enabled = self._call(client, "system.security.info.fips_enabled", [])
            FIPS_ENABLED.set(1 if _as_bool(fips_enabled) else 0)
        except Exception:
            LOG.debug("system.security.info.fips_enabled failed", exc_info=True)

    # ------------------------------------------------------------------
    # Feature flags (v4)
    # ------------------------------------------------------------------

    def _collect_feature_flags(self, client: JsonRpcWsClient) -> None:
        """Collect enabled status for DEDUP, FIBRECHANNEL, and VM features."""
        FEATURE_ENABLED.clear()
        for feature in ("DEDUP", "FIBRECHANNEL", "VM"):
            try:
                result = self._call(client, "system.feature_enabled", [feature])
                FEATURE_ENABLED.labels(feature=feature).set(1 if _as_bool(result) else 0)
            except Exception:
                LOG.debug("system.feature_enabled(%s) failed", feature, exc_info=True)

    # ------------------------------------------------------------------
    # Hardware / Chassis (v4)
    # ------------------------------------------------------------------

    def _collect_chassis_hardware(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect chassis hardware model."""
        try:
            model = cache.get("truenas.get_chassis_hardware")
            if model is None:
                model = self._call(client, "truenas.get_chassis_hardware", [])
            model_str = _str_label(model, "unknown")
            if model_str:
                CHASSIS_HARDWARE.labels(model=model_str).set(1)
        except Exception:
            LOG.debug("truenas.get_chassis_hardware failed", exc_info=True)

    # ------------------------------------------------------------------
    # TrueNAS Connect (v4)
    # ------------------------------------------------------------------

    def _collect_tn_connect(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect TrueNAS Connect (cloud management) status."""
        try:
            config = cache.get("tn_connect.config") or self._call(client, "tn_connect.config", [])
        except Exception:
            LOG.debug("tn_connect.config failed", exc_info=True)
            return

        if not isinstance(config, dict):
            TN_CONNECT_ENABLED.set(0)
            return

        enabled = _as_bool(config.get("enabled"))
        TN_CONNECT_ENABLED.set(1 if enabled else 0)

        status = _str_label(config.get("status"), "UNKNOWN").upper()
        if status and status != "UNKNOWN":
            TN_CONNECT_STATUS.clear()
            TN_CONNECT_STATUS.labels(status=status).set(1)

    # ------------------------------------------------------------------
    # TrueCommand full status (v4)
    # ------------------------------------------------------------------

    def _collect_truecommand_status(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect TrueCommand full status enum."""
        try:
            config = cache.get("truecommand.config") or self._call(client, "truecommand.config", [])
        except Exception:
            LOG.debug("truecommand.config failed", exc_info=True)
            return

        if not isinstance(config, dict):
            return

        status = _str_label(config.get("status"), "UNKNOWN").upper()
        if status and status != "UNKNOWN":
            TRUECOMMAND_STATUS.clear()
            TRUECOMMAND_STATUS.labels(status=status).set(1)

    # ------------------------------------------------------------------
    # Audit dataset metrics (v4)
    # ------------------------------------------------------------------

    def _collect_audit_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect audit dataset space and quota settings."""
        try:
            config = cache.get("audit.config") or self._call(client, "audit.config", [])
        except Exception:
            LOG.debug("audit.config failed", exc_info=True)
            return

        if not isinstance(config, dict):
            return

        space = config.get("space")
        if isinstance(space, dict):
            used = _as_float(space.get("used"))
            if used is not None:
                AUDIT_DATASET_USED_BYTES.set(used)
            avail = _as_float(space.get("available"))
            if avail is not None:
                AUDIT_DATASET_AVAILABLE_BYTES.set(avail)

        quota_warning = _as_float(config.get("quota_fill_warning"))
        if quota_warning is not None:
            AUDIT_QUOTA_FILL_WARNING_PERCENT.set(quota_warning)

        quota_critical = _as_float(config.get("quota_fill_critical"))
        if quota_critical is not None:
            AUDIT_QUOTA_FILL_CRITICAL_PERCENT.set(quota_critical)

    # ------------------------------------------------------------------
    # v5 collectors: Pool scrub tasks (pool.scrub.query)
    # ------------------------------------------------------------------

    def _collect_scrub_task_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect pool scrub task scheduling health."""
        try:
            POOL_SCRUB_TASK_COUNT.set(self._query_count(client, "pool.scrub.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="scrub_tasks").inc()
            LOG.debug("pool.scrub.query count failed", exc_info=True)

        try:
            tasks = cache.get("pool.scrub.query") or self._call(client, "pool.scrub.query", [
                [], {"select": ["id", "pool_name", "enabled", "schedule", "description"]}
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="scrub_tasks").inc()
            LOG.debug("pool.scrub.query failed", exc_info=True)
            return

        if not isinstance(tasks, list):
            return

        for task in tasks[: self.config.max_entity_calls]:
            if not isinstance(task, dict):
                continue
            pool_name = _str_label(
                task.get("pool_name") or task.get("pool") or task.get("description"), "unknown"
            )
            enabled = _as_bool(task.get("enabled", False))
            POOL_SCRUB_TASK_ENABLED.labels(pool=pool_name).set(1 if enabled else 0)

    # ------------------------------------------------------------------
    # v5 collectors: Snapshot count (pool.snapshot.query)
    # ------------------------------------------------------------------

    def _collect_snapshot_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect total snapshot count and oldest snapshot timestamp."""
        try:
            SNAPSHOT_TOTAL_COUNT.set(self._query_count(client, "pool.snapshot.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="snapshots").inc()
            LOG.debug("pool.snapshot.query count failed", exc_info=True)

        try:
            oldest_query = self._call(client, "pool.snapshot.query", [
                [], {
                    "limit": 1,
                    "order_by": ["properties.creation.parsed"],
                    "select": [["properties.creation.parsed", "creation_parsed"]],
                }
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="snapshots").inc()
            LOG.debug("pool.snapshot.query oldest snapshot failed", exc_info=True)
            return

        oldest_snapshot: Any = None
        if isinstance(oldest_query, list):
            oldest_snapshot = oldest_query[0] if oldest_query else None
        elif isinstance(oldest_query, dict):
            oldest_snapshot = oldest_query

        oldest_ts = self._extract_snapshot_creation_timestamp(oldest_snapshot)
        SNAPSHOT_OLDEST_TS.set(oldest_ts if oldest_ts is not None else 0)

    # ------------------------------------------------------------------
    # v5 collectors: Pool resilver config
    # ------------------------------------------------------------------

    def _collect_resilver_config(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect resilver priority scheduling config."""
        try:
            config = cache.get("pool.resilver.config") or self._call(client, "pool.resilver.config", [])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="resilver_config").inc()
            LOG.debug("pool.resilver.config failed", exc_info=True)
            return

        if isinstance(config, dict):
            enabled = _as_bool(config.get("enabled", False))
            POOL_RESILVER_ENABLED.set(1 if enabled else 0)

    # ------------------------------------------------------------------
    # v5 collectors: Cloud backup tasks
    # ------------------------------------------------------------------

    def _collect_cloud_backup_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect cloud backup task inventory and state."""
        try:
            CLOUD_BACKUP_TASK_COUNT.set(self._query_count(client, "cloud_backup.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="cloud_backup").inc()
            LOG.debug("cloud_backup.query count failed", exc_info=True)

        try:
            tasks = cache.get("cloud_backup.query") or self._call(client, "cloud_backup.query", [
                [], {"limit": self.config.query_limit, "select": ["id", "description", "enabled", "job"]}
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="cloud_backup").inc()
            LOG.debug("cloud_backup.query failed", exc_info=True)
            return

        if not isinstance(tasks, list):
            return

        for task in tasks[: self.config.max_entity_calls]:
            if not isinstance(task, dict):
                continue
            name = _str_label(task.get("description") or task.get("id"), "unknown")
            enabled = _as_bool(task.get("enabled", False))
            CLOUD_BACKUP_TASK_ENABLED.labels(name=name).set(1 if enabled else 0)

            job = task.get("job")
            if isinstance(job, dict):
                state = _str_label(job.get("state"), "UNKNOWN").upper()
                CLOUD_BACKUP_TASK_STATE.labels(name=name, state=state).set(1)

    # ------------------------------------------------------------------
    # v5 collectors: Cron jobs
    # ------------------------------------------------------------------

    def _collect_cronjob_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect cron job inventory."""
        try:
            CRONJOB_COUNT.set(self._query_count(client, "cronjob.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="cronjobs").inc()
            LOG.debug("cronjob.query count failed", exc_info=True)

        try:
            jobs = cache.get("cronjob.query") or self._call(client, "cronjob.query", [
                [], {"limit": self.config.query_limit, "select": ["id", "description", "enabled", "command"]}
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="cronjobs").inc()
            LOG.debug("cronjob.query failed", exc_info=True)
            return

        if not isinstance(jobs, list):
            return

        for job in jobs[: self.config.max_entity_calls]:
            if not isinstance(job, dict):
                continue
            name = _str_label(job.get("description") or job.get("command") or job.get("id"), "unknown")
            enabled = _as_bool(job.get("enabled", False))
            CRONJOB_ENABLED.labels(name=name).set(1 if enabled else 0)

    # ------------------------------------------------------------------
    # v5 collectors: Disk in-use
    # ------------------------------------------------------------------

    def _collect_disk_used_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect which disks are in use by pools."""
        try:
            used = cache.get("disk.get_used") or self._call(client, "disk.get_used", [])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="disk_used").inc()
            LOG.debug("disk.get_used failed", exc_info=True)
            return

        if isinstance(used, list):
            used_set = set()
            for item in used:
                if isinstance(item, dict):
                    name = item.get("name") or item.get("devname")
                    if name:
                        used_set.add(str(name))
                        DISK_IN_USE.labels(disk=str(name)).set(1)
                elif isinstance(item, str):
                    used_set.add(item)
                    DISK_IN_USE.labels(disk=item).set(1)

    # ------------------------------------------------------------------
    # v5 collectors: Protocol configs (SMB, NFS, SSH, FTP, SNMP)
    # ------------------------------------------------------------------

    def _collect_protocol_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect protocol service configuration flags."""
        protocol_services: dict[str, bool] | None = None
        try:
            protocol_services = self._query_service_enable_map(client, ("ssh", "ftp", "snmp"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="protocol_services").inc()
            LOG.debug("service.query for protocol services failed", exc_info=True)

        # SMB
        try:
            smb = cache.get("smb.config") or self._call(client, "smb.config", [])
            if isinstance(smb, dict):
                multichannel = _as_bool(smb.get("multichannel", False))
                SMB_MULTICHANNEL_ENABLED.set(1 if multichannel else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="smb_config").inc()
            LOG.debug("smb.config failed", exc_info=True)

        # NFS
        try:
            nfs = cache.get("nfs.config") or self._call(client, "nfs.config", [])
            if isinstance(nfs, dict):
                v4 = _as_bool(nfs.get("v4"))
                NFS_V4_ENABLED.set(1 if v4 else 0)
                servers = _as_float(nfs.get("servers"))
                if servers is not None:
                    NFS_SERVERS.set(servers)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="nfs_config").inc()
            LOG.debug("nfs.config failed", exc_info=True)

        # SSH
        if protocol_services is not None:
            SSH_ENABLED.set(1 if protocol_services.get("ssh", False) else 0)

        try:
            ssh = cache.get("ssh.config") or self._call(client, "ssh.config", [])
            if isinstance(ssh, dict):
                pwd_auth = _as_bool(ssh.get("passwordauth", True))
                SSH_PASSWORD_AUTH.set(1 if pwd_auth else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="ssh_config").inc()
            LOG.debug("ssh.config failed", exc_info=True)

        # FTP
        if protocol_services is not None:
            FTP_ENABLED.set(1 if protocol_services.get("ftp", False) else 0)

        # SNMP
        if protocol_services is not None:
            SNMP_ENABLED.set(1 if protocol_services.get("snmp", False) else 0)

    # ------------------------------------------------------------------
    # v5 collectors: System advanced/general config
    # ------------------------------------------------------------------

    def _collect_system_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect system advanced and general configuration flags."""
        # Advanced
        try:
            adv = cache.get("system.advanced.config") or self._call(client, "system.advanced.config", [])
            if isinstance(adv, dict):
                CONSOLEMENU_ENABLED.set(1 if _as_bool(adv.get("consolemenu")) else 0)
                SERIALCONSOLE_ENABLED.set(1 if _as_bool(adv.get("serialconsole")) else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="system_advanced").inc()
            LOG.debug("system.advanced.config failed", exc_info=True)

        # General
        try:
            gen = cache.get("system.general.config") or self._call(client, "system.general.config", [])
            if isinstance(gen, dict):
                port = _as_float(gen.get("ui_httpsport"))
                if port is not None:
                    UI_HTTPS_PORT.set(port)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="system_general").inc()
            LOG.debug("system.general.config failed", exc_info=True)

        # System global ID
        try:
            gid = cache.get("system.global.id") or self._call(client, "system.global.id", [])
            if isinstance(gid, str):
                SYSTEM_GLOBAL_ID.labels(global_id=gid).set(1)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="system_global_id").inc()
            LOG.debug("system.global.id failed", exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: KMIP / support / systemdataset
    # ------------------------------------------------------------------

    def _collect_infrastructure_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect KMIP, support, and system dataset configs."""
        # KMIP
        try:
            kmip = cache.get("kmip.config") or self._call(client, "kmip.config", [])
            if isinstance(kmip, dict):
                enabled = _as_bool(kmip.get("enabled", False))
                KMIP_ENABLED.set(1 if enabled else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="kmip_config").inc()
            LOG.debug("kmip.config failed", exc_info=True)

        # Support
        try:
            avail = cache.get("support.is_available") or self._call(client, "support.is_available", [])
            SUPPORT_AVAILABLE.set(1 if _as_bool(avail) else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="support_available").inc()
            LOG.debug("support.is_available failed", exc_info=True)

        # System dataset
        try:
            sds = cache.get("systemdataset.config") or self._call(client, "systemdataset.config", [])
            if isinstance(sds, dict):
                pool = _str_label(sds.get("pool"), "")
                if pool:
                    SYSTEMDATASET_POOL.labels(pool=pool).set(1)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="systemdataset").inc()
            LOG.debug("systemdataset.config failed", exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: Users / groups / routes / tunables / privileges
    # ------------------------------------------------------------------

    def _collect_inventory_counts(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect various inventory counts."""
        for method, gauge, collector_name in (
            ("user.query", LOCAL_USER_COUNT, "user_count"),
            ("group.query", LOCAL_GROUP_COUNT, "group_count"),
            ("staticroute.query", STATIC_ROUTE_COUNT, "static_routes"),
            ("tunable.query", TUNABLE_COUNT, "tunables"),
            ("privilege.query", PRIVILEGE_COUNT, "privileges"),
            ("initshutdownscript.query", INITSHUTDOWNSCRIPT_COUNT, "initshutdownscripts"),
            ("keychaincredential.query", KEYCHAIN_CREDENTIAL_COUNT, "keychain_creds"),
        ):
            try:
                gauge.set(self._query_count(client, method))
            except Exception:
                COLLECTOR_ERRORS_TOTAL.labels(collector=collector_name).inc()
                LOG.debug("%s failed", method, exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: iSCSI inventory
    # ------------------------------------------------------------------

    def _collect_iscsi_inventory(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect iSCSI target/portal/extent/initiator counts."""
        for method, gauge, collector_name in (
            ("iscsi.target.query", ISCSI_TARGET_COUNT, "iscsi_targets"),
            ("iscsi.portal.query", ISCSI_PORTAL_COUNT, "iscsi_portals"),
            ("iscsi.extent.query", ISCSI_EXTENT_COUNT, "iscsi_extents"),
            ("iscsi.initiator.query", ISCSI_INITIATOR_COUNT, "iscsi_initiators"),
        ):
            try:
                gauge.set(self._query_count(client, method))
            except Exception:
                COLLECTOR_ERRORS_TOTAL.labels(collector=collector_name).inc()
                LOG.debug("%s failed", method, exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: NVMe-oF extended inventory
    # ------------------------------------------------------------------

    def _collect_nvmet_extended(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect NVMe-oF host and namespace counts."""
        for method, gauge, collector_name in (
            ("nvmet.host.query", NVMET_HOST_COUNT, "nvmet_hosts"),
            ("nvmet.namespace.query", NVMET_NAMESPACE_COUNT, "nvmet_namespaces"),
        ):
            try:
                gauge.set(self._query_count(client, method))
            except Exception:
                COLLECTOR_ERRORS_TOTAL.labels(collector=collector_name).inc()
                LOG.debug("%s failed", method, exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: Network / Docker images / Replication config
    # ------------------------------------------------------------------

    def _collect_misc_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect misc configuration counts and flags."""
        # Network configuration
        try:
            netcfg = cache.get("network.configuration.config") or self._call(
                client, "network.configuration.config", []
            )
            if isinstance(netcfg, dict):
                proxy = netcfg.get("httpproxy") or ""
                NETWORK_HTTPPROXY_CONFIGURED.set(1 if proxy.strip() else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="network_config").inc()
            LOG.debug("network.configuration.config failed", exc_info=True)

        # Docker images
        try:
            DOCKER_IMAGE_COUNT.set(self._query_count(client, "app.image.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="docker_images").inc()
            LOG.debug("app.image.query failed", exc_info=True)

        # Replication config
        try:
            rep_cfg = cache.get("replication.config.config") or self._call(
                client, "replication.config.config", []
            )
            if isinstance(rep_cfg, dict):
                max_par = _as_float(rep_cfg.get("max_parallel_replication_tasks"))
                if max_par is not None:
                    REPLICATION_MAX_PARALLEL.set(max_par)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="replication_config").inc()
            LOG.debug("replication.config.config failed", exc_info=True)

        # Reporting exporters
        try:
            REPORTING_EXPORTER_COUNT.set(self._query_count(client, "reporting.exporters.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="reporting_exporters").inc()
            LOG.debug("reporting.exporters.query failed", exc_info=True)

        # Reporting service enable state
        try:
            reporting_services = self._query_service_enable_map(client, ("netdata", "reporting"))
            if reporting_services:
                enabled = reporting_services.get("netdata")
                if enabled is None:
                    enabled = reporting_services.get("reporting")
                REPORTING_ENABLED.set(1 if enabled else 0)
            else:
                REPORTING_ENABLED.set(0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="reporting_config").inc()
            LOG.debug("service.query for reporting service failed", exc_info=True)

        # DNS resolvers
        try:
            DNS_RESOLVER_COUNT.set(self._query_count(client, "dns.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="dns_resolvers").inc()
            LOG.debug("dns.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: Security posture (IOMMU, 2FA, mail, alert services)
    # ------------------------------------------------------------------

    def _collect_security_posture(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect security and alerting configuration flags."""
        # IOMMU
        try:
            iommu = self._call(client, "vm.device.iommu_enabled", [])
            IOMMU_ENABLED.set(1 if _as_bool(iommu) else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="iommu").inc()
            LOG.debug("vm.device.iommu_enabled failed", exc_info=True)

        # 2FA
        try:
            twofa = cache.get("auth.twofactor.config") or self._call(
                client, "auth.twofactor.config", []
            )
            if isinstance(twofa, dict):
                enabled = _as_bool(twofa.get("enabled", False))
                TWOFACTOR_ENABLED.set(1 if enabled else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="twofactor").inc()
            LOG.debug("auth.twofactor.config failed", exc_info=True)

        # Mail
        try:
            mail = cache.get("mail.config") or self._call(client, "mail.config", [])
            if isinstance(mail, dict):
                # Consider mail configured if outgoingserver is set
                server = mail.get("outgoingserver") or mail.get("fromemail") or ""
                MAIL_CONFIGURED.set(1 if str(server).strip() else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="mail_config").inc()
            LOG.debug("mail.config failed", exc_info=True)

        # Alert services
        try:
            ALERTSERVICE_COUNT.set(self._query_count(client, "alertservice.query"))

            services = cache.get("alertservice.query") or self._call(
                client, "alertservice.query", [[], {"limit": 50, "select": ["id", "name", "type", "enabled"]}]
            )
            if isinstance(services, list):
                for svc in services[: self.config.max_list_items]:
                    if not isinstance(svc, dict):
                        continue
                    name = _str_label(svc.get("name") or svc.get("id"), "unknown")
                    svc_type = _str_label(svc.get("type"), "unknown")
                    enabled = _as_bool(svc.get("enabled", False))
                    ALERTSERVICE_ENABLED.labels(name=name, type=svc_type).set(1 if enabled else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="alertservices").inc()
            LOG.debug("alertservice.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # IPMI LAN channel query (needs channel number from ipmi.lan.channels)
    # ------------------------------------------------------------------

    def _collect_ipmi_lan_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect IPMI LAN config for all available channels."""
        try:
            channels = cache.get("ipmi.lan.channels") or self._call(client, "ipmi.lan.channels", [])
        except Exception:
            LOG.debug("ipmi.lan.channels failed", exc_info=True)
            return

        if not isinstance(channels, list) or not channels:
            return

        for channel in channels[: 4]:  # at most 4 channels
            try:
                chan_id = int(channel) if isinstance(channel, (int, float)) else int(str(channel))
                lan_data = self._call(client, "ipmi.lan.query", [chan_id])
                if isinstance(lan_data, dict):
                    self._extract_generic_metrics(
                        "ipmi.lan.query", lan_data, f"result.channel_{chan_id}", 0
                    )
            except Exception:
                LOG.debug("ipmi.lan.query channel %s failed", channel, exc_info=True)

    def run_forever(self) -> None:
        self._ensure_event_thread()
        while True:
            self.scrape_once()
            time.sleep(self.config.interval_seconds)


# ---------------------------------------------------------------------------
# HTTP server: /metrics + /healthz on one port
# ---------------------------------------------------------------------------

class _QuietHandler(WSGIRequestHandler):
    """Suppress per-request access log lines (Prometheus scrapes are very noisy)."""
    def log_message(self, fmt: str, *args: Any) -> None:  # type: ignore[override]
        pass


def _start_http_server(port: int) -> None:
    """Start a WSGI server exposing /metrics and /healthz on *port*.

    The standard prometheus_client.start_http_server() only exposes /metrics.
    Adding /healthz lets orchestrators (k8s, Docker, Nomad) distinguish an
    exporter crash from a scrape failure without touching the Prometheus config.
    """
    metrics_app = make_wsgi_app()

    def app(environ: dict[str, Any], start_response: Any) -> list[bytes]:
        path = environ.get("PATH_INFO", "")
        if path == "/healthz":
            start_response("200 OK", [("Content-Type", "text/plain; charset=utf-8")])
            return [b"ok\n"]
        # Everything else (including /metrics) handled by prometheus_client
        return metrics_app(environ, start_response)

    server = make_server("", port, app, handler_class=_QuietHandler)
    thread = threading.Thread(target=server.serve_forever, name="http-server", daemon=True)
    thread.start()
    LOG.info("HTTP server started on :%d (GET /metrics, GET /healthz)", port)


# ---------------------------------------------------------------------------
# Configuration loading
# ---------------------------------------------------------------------------

def _load_config() -> Config:
    ws_url = os.getenv("TRUENAS_WS_URL", "").strip()
    api_key = os.getenv("TRUENAS_API_KEY", "").strip()
    if not ws_url:
        raise ValueError("TRUENAS_WS_URL is required (example: wss://truenas.local/api/current)")
    if not api_key:
        raise ValueError("TRUENAS_API_KEY is required")

    def _bool_env(name: str, default: str = "true") -> bool:
        return os.getenv(name, default).strip().lower() in {"1", "true", "yes", "on"}

    def _list_env(name: str, default: str = "") -> list[str]:
        return [x.strip() for x in os.getenv(name, default).split(",") if x.strip()]

    event_subscriptions = _list_env(
        "EVENT_SUBSCRIPTIONS",
        ",".join([
            # Real-time telemetry
            "reporting.realtime",    # CPU/mem/net live data
            "app.stats",             # per-app container stats
            "virt.instance.metrics", # per-instance live CPU/mem stats
            # State-change events (push instead of poll)
            "pool.scan",             # scrub/resilver progress
            "pool.query",            # pool degraded/faulted transitions
            "disk.query",            # hotplug / removal events
            "docker.state",          # Docker daemon transitions
            "interface.query",       # link up/down events
            "alert.list",            # new alert push delivery
            "directoryservices.status",  # AD/LDAP health transitions
            "service.query",         # service start/stop events
            "failover.status",       # HA failover state transitions
            "update.status",         # update download/install progress
            "system.reboot.info",    # reboot pending/cleared
            "system.shutdown",       # shutdown initiated (last breath metric)
            "core.get_jobs",         # background job progress
            # v5 additions
            "container.query",       # container state changes (v25.10+)
            "vm.query",              # VM state changes (start/stop/crash)
        ]),
    )

    filesystem_paths = _list_env("FILESYSTEM_PATHS", "/mnt") or ["/mnt"]

    return Config(
        ws_url=ws_url,
        api_key=api_key,
        interval_seconds=int(os.getenv("SCRAPE_INTERVAL_SECONDS", "30")),
        timeout_seconds=int(os.getenv("TRUENAS_TIMEOUT_SECONDS", "20")),
        verify_tls=_bool_env("TRUENAS_VERIFY_TLS", "true"),
        exporter_port=int(os.getenv("EXPORTER_PORT", "9108")),
        auto_discover_methods=_bool_env("AUTO_DISCOVER_METHODS", "false"),
        query_limit=int(os.getenv("QUERY_LIMIT", "200")),
        max_method_calls=int(os.getenv("MAX_METHOD_CALLS", "250")),
        max_list_items=int(os.getenv("MAX_LIST_ITEMS", "200")),
        max_depth=int(os.getenv("MAX_METRIC_DEPTH", "6")),
        max_entity_calls=int(os.getenv("MAX_ENTITY_CALLS", "50")),
        max_datasets=int(os.getenv("MAX_DATASETS", "100")),
        extra_methods=_list_env("EXTRA_METHODS"),
        exclude_methods=_list_env("EXCLUDE_METHODS"),
        filesystem_paths=filesystem_paths,
        enable_filesystem_listdir=_bool_env("ENABLE_FILESYSTEM_LISTDIR", "false"),
        enable_event_streams=_bool_env("ENABLE_EVENT_STREAMS", "true"),
        enable_dataset_metrics=_bool_env("ENABLE_DATASET_METRICS", "true"),
        enable_task_metrics=_bool_env("ENABLE_TASK_METRICS", "true"),
        enable_ipmi_metrics=_bool_env("ENABLE_IPMI_METRICS", "true"),
        event_interval_seconds=int(os.getenv("EVENT_INTERVAL_SECONDS", "2")),
        event_read_timeout_seconds=int(os.getenv("EVENT_READ_TIMEOUT_SECONDS", "60")),
        event_subscriptions=event_subscriptions,
        scrape_all_metrics=_bool_env("SCRAPE_ALL_METRICS", "false"),
    )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO").upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    config = _load_config()
    LOG.info(
        "Starting TrueNAS exporter v5.1 — url=%s verify_tls=%s port=%s",
        config.ws_url, config.verify_tls, config.exporter_port,
    )
    _start_http_server(config.exporter_port)
    exporter = TrueNASExporter(config)
    exporter.run_forever()


if __name__ == "__main__":
    main()
