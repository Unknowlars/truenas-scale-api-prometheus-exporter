#!/usr/bin/env python3
"""Runtime for the TrueNAS SCALE JSON-RPC Prometheus exporter.

``TrueNASExporter`` polls documented read-only middleware methods on a
background scrape thread and maintains a separate event-stream thread for
subscribed push updates. Collector mode serves the last complete immutable
snapshot; legacy mode exposes the default registry directly for one
compatibility release.

Metric declarations live in ``metrics.py`` and the generated field/source
contract lives in ``docs/api-exporter-parity.md``. Use git history for release
changelogs; this module documents only current behavior.
"""

from __future__ import annotations

import logging
import os
import re
import signal
import sys
import threading
import time
import traceback
from typing import Any, cast
from urllib.parse import urlparse

from prometheus_client import REGISTRY, CollectorRegistry, Gauge
from websocket import WebSocketTimeoutException

from .collection import (
    _as_bool,
    _as_float,
    _as_optional_bool,
    _as_percent,
    _as_ratio,
    _as_size_bytes,
    _cert_days_to_expiry,
    _extract_labeled_numeric_series,
    _first_not_none,
    _link_is_up,
    _normalize_core_label,
    _parse_ts,
    _str_label,
)
from .compat_profiles import PROFILE_25_10, CompatibilityProfile, get_profile
from .config import Config, load_config
from .events import (
    _EVENT_METRICS,
    _EVENT_SOURCE_BY_METRIC_NAME,
    _INTERVAL_EVENT_SUBSCRIPTIONS,
    _REALTIME_EVENT_SCALAR_METRICS,
    INSTANCE_METRICS_EVENT,
    INSTANCE_METRICS_WIRE_ALIASES,
)
from .http import _LANDING_PAGE  # noqa: F401 - compatibility re-export
from .http import start_http_server as _start_http_server
from .method_safety import (
    _AUTO_SKIP_ERROR_PATTERNS,
    BASE_METHODS,
    DENY_NAMESPACE_PREFIXES,
    REQUIRES_ENTITY_PARAM,
    SAFE_ALLOW_RE,
    SAFE_DENY_RE,
    is_documented_read_only_method,
    is_sensitive_read_method,
    is_unsafe_generic_read_method,
)
from .metrics import (
    ALERT_COUNT,
    ALERT_COUNT_BY_CLASS,
    ALERT_COUNT_BY_LEVEL,
    ALERT_COUNT_BY_NODE,
    ALERT_COUNT_BY_SOURCE,
    ALERT_DISMISSED_COUNT,
    ALERT_LAST_OCCURRENCE_TS,
    ALERT_OLDEST_TS,
    ALERT_ONE_SHOT_COUNT,
    ALERTSERVICE_COUNT,
    ALERTSERVICE_ENABLED,
    API_CALL_DURATION,
    API_CALL_ERRORS_TOTAL,
    API_CALL_SUCCESS,
    API_KEY_COUNT,
    API_KEY_EXPIRY_TS,
    API_KEY_REVOKED_COUNT,
    APP_AVAILABLE_SPACE_BYTES,
    APP_BLKIO_READ_BYTES,
    APP_BLKIO_WRITE_BYTES,
    APP_CONTAINER_COUNT,
    APP_CONTAINER_STATE_COUNT,
    APP_COUNT,
    APP_CPU_PERCENT,
    APP_CUSTOM,
    APP_DOCKERHUB_PULL_LIMIT_REMAINING,
    APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS,
    APP_DOCKERHUB_PULL_LIMIT_TOTAL,
    APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS,
    APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT,
    APP_IMAGE_UPDATES_AVAILABLE,
    APP_MEMORY_BYTES,
    APP_MIGRATED,
    APP_NET_RX_BYTES_RATE,
    APP_NET_TX_BYTES_RATE,
    APP_STATE,
    APP_UPGRADE_AVAILABLE,
    APP_USED_HOST_IP_COUNT,
    APP_USED_PORT_COUNT,
    APP_WEBDAV_SHARE_COUNT,
    AUDIT_DATASET_AVAILABLE_BYTES,
    AUDIT_DATASET_USED_BYTES,
    AUDIT_QUOTA_BYTES,
    AUDIT_QUOTA_FILL_CRITICAL_PERCENT,
    AUDIT_QUOTA_FILL_WARNING_PERCENT,
    AUDIT_REMOTE_LOGGING_ENABLED,
    AUDIT_RESERVATION_BYTES,
    AUDIT_RETENTION_DAYS,
    AUTH_SESSIONS_ACTIVE,
    BOOT_ENV_ACTIVATED,
    BOOT_ENV_ACTIVATED_COUNT,
    BOOT_ENV_ACTIVE,
    BOOT_ENV_ACTIVE_COUNT,
    BOOT_ENV_COUNT,
    BOOT_ENV_KEEP,
    BOOT_ENV_KEEP_COUNT,
    BOOT_ENV_SIZE_BYTES,
    BOOT_ENV_USED_BYTES,
    BOOT_POOL_ALLOCATED_BYTES,
    BOOT_POOL_DISK_COUNT,
    BOOT_POOL_FREE_BYTES,
    BOOT_POOL_HEALTHY,
    BOOT_POOL_SCAN_PERCENT,
    BOOT_POOL_SCAN_STATE,
    BOOT_POOL_SIZE_BYTES,
    BOOT_POOL_STATUS,
    CATALOG_CONFIG_PRESENT,
    CATALOG_PREFERRED_TRAIN_COUNT,
    CATALOG_TRAIN_COUNT,
    CERT_COUNT,
    CERT_DAYS_TO_EXPIRY,
    CERT_EXPIRY_TIMESTAMP_SECONDS,
    CHASSIS_HARDWARE,
    CLOUD_BACKUP_TASK_COUNT,
    CLOUD_BACKUP_TASK_ENABLED,
    CLOUD_BACKUP_TASK_STATE,
    COLLECTOR_ERRORS_TOTAL,
    CPU_CORE_USAGE_PERCENT,
    CPU_IDLE_PERCENT,
    CPU_INTERRUPT_PERCENT,
    CPU_IOWAIT_PERCENT,
    CPU_SYSTEM_PERCENT,
    CPU_TEMPERATURE_C,
    CPU_USAGE_PERCENT,
    CPU_USER_PERCENT,
    CRONJOB_COUNT,
    CRONJOB_ENABLED,
    DATASET_ATIME,
    DATASET_AVAILABLE_BYTES,
    DATASET_COMPRESSION_RATIO,
    DATASET_COUNT,
    DATASET_CREATION_TS,
    DATASET_ENCRYPTED,
    DATASET_EXEC,
    DATASET_KEY_LOADED,
    DATASET_LOCKED,
    DATASET_QUOTA_BYTES,
    DATASET_QUOTA_CRITICAL_PERCENT,
    DATASET_QUOTA_WARNING_PERCENT,
    DATASET_READONLY,
    DATASET_REFERENCED_BYTES,
    DATASET_REFQUOTA_BYTES,
    DATASET_REFQUOTA_CRITICAL_PERCENT,
    DATASET_REFQUOTA_WARNING_PERCENT,
    DATASET_REFRESERVATION_BYTES,
    DATASET_RESERVATION_BYTES,
    DATASET_SNAPSHOT_COUNT,
    DATASET_USED_BY_CHILDREN_BYTES,
    DATASET_USED_BY_DATASET_BYTES,
    DATASET_USED_BY_SNAPSHOTS_BYTES,
    DATASET_USED_BYTES,
    DIRECTORYSERVICES_CONFIG_ENABLED,
    DIRECTORYSERVICES_FAULT_PRESENT,
    DIRECTORYSERVICES_FAULT_REASON,
    DIRECTORYSERVICES_HEALTHY,
    DIRECTORYSERVICES_SERVICE_TYPE,
    DIRECTORYSERVICES_STATUS,
    DISK_BUSY_PERCENT,
    DISK_COUNT,
    DISK_IN_USE,
    DISK_INFO,
    DISK_READ_BYTES_RATE,
    DISK_READ_OPS_RATE,
    DISK_ROTATIONAL,
    DISK_SIZE_BYTES,
    DISK_SMART_ENABLED,
    DISK_TEMP_AGG_C,
    DISK_TEMP_ALERT_COUNT,
    DISK_TEMPERATURE_C,
    DISK_WRITE_BYTES_RATE,
    DISK_WRITE_OPS_RATE,
    DNS_RESOLVER_COUNT,
    DOCKER_IMAGE_COUNT,
    DOCKER_NETWORK_COUNT,
    DOCKER_NVIDIA_PRESENT,
    DOCKER_STATUS,
    EVENT_BOOLEAN_VALUE,
    EVENT_LAST_MESSAGE_TS,
    EVENT_LIST_LENGTH,
    EVENT_MESSAGES_TOTAL,
    EVENT_NUMERIC_VALUE,
    EVENT_STATUS_VALUE,
    EVENT_STREAM_UP,
    FAILOVER_DISABLED_REASON,
    FAILOVER_DISABLED_REASON_COUNT,
    FAILOVER_NODE_REBOOT_REQUIRED,
    FC_HOST_COUNT,
    FC_PORT_COUNT,
    FEATURE_ENABLED,
    FILESYSTEM_PATH_COUNT,
    FIPS_AVAILABLE,
    FIPS_ENABLED,
    FTP_ENABLED,
    GPU_AVAILABLE_TO_HOST,
    GPU_COUNT,
    GPU_INFO,
    GPU_USES_CRITICAL_DEVICES,
    HOST_CPU_CORES,
    HOST_CPU_MODEL,
    HOST_ECC_MEMORY,
    HOST_INFO,
    HOST_LOAD_AVERAGE,
    HOST_PHYSICAL_CPU_CORES,
    HOST_PHYSICAL_MEMORY_BYTES,
    HOST_SYSTEM_INFO,
    HOST_UPTIME_SECONDS,
    HW_VIRT_VARIANT,
    INITSHUTDOWNSCRIPT_COUNT,
    INTERFACE_CHECKIN_WAITING_SECONDS,
    INTERFACE_COUNT,
    INTERFACE_HAS_PENDING_CHANGES,
    INTERFACE_LINK_UP,
    INTERFACE_MTU,
    INTERFACE_REALTIME_LINK_UP,
    INTERFACE_REALTIME_SPEED_MBITS,
    INTERFACE_TYPE,
    IOMMU_ENABLED,
    IPMI_CHASSIS_DRIVE_FAULT,
    IPMI_CHASSIS_FAN_FAULT,
    IPMI_CHASSIS_INTRUSION,
    IPMI_CHASSIS_POWER_ON,
    IPMI_CHASSIS_POWER_OVERLOAD,
    IPMI_LOADED,
    IPMI_SEL_ENTRY_COUNT,
    IPMI_SEL_FREE_SPACE_BYTES,
    ISCSI_ALUA_ENABLED,
    ISCSI_CLIENT_COUNT,
    ISCSI_EXTENT_COUNT,
    ISCSI_INITIATOR_COUNT,
    ISCSI_ISER_ENABLED,
    ISCSI_PORTAL_COUNT,
    ISCSI_SESSION_COUNT,
    ISCSI_SESSION_IMMEDIATE_DATA_COUNT,
    ISCSI_SESSION_ISER_COUNT,
    ISCSI_SESSION_OFFLOAD_COUNT,
    ISCSI_TARGET_COUNT,
    JBOF_COUNT,
    JOB_ABORTABLE_ACTIVE_COUNT,
    JOB_ACTIVE_COUNT,
    JOB_ACTIVE_COUNT_BY_METHOD,
    JOB_ACTIVE_COUNT_BY_STATE,
    JOB_OLDEST_ACTIVE_TS,
    JOB_PROGRESS_PERCENT,
    JOB_TRANSIENT_ACTIVE_COUNT,
    KEYCHAIN_CREDENTIAL_COUNT,
    KMIP_SYNC_PENDING,
    LAST_SCRAPE_TS,
    LOCAL_GROUP_COUNT,
    LOCAL_USER_COUNT,
    MEMORY_PHYSICAL_AVAILABLE_BYTES,
    MEMORY_PHYSICAL_TOTAL_BYTES,
    MEMORY_PHYSICAL_USED_BYTES,
    METHOD_BOOLEAN_VALUE,
    METHOD_LIST_LENGTH,
    METHOD_NUMERIC_VALUE,
    METHOD_STATUS_VALUE,
    METRIC_SPECS,
    NETWORK_DEFAULT_GATEWAY_CONFIGURED,
    NETWORK_DEFAULT_ROUTES,
    NETWORK_GATEWAY_REACHABLE,
    NETWORK_NAMESERVERS,
    NETWORK_RX_BYTES_RATE,
    NETWORK_TX_BYTES_RATE,
    NFS_CLIENT_COUNT,
    NFS_RDMA_ENABLED,
    NFS_SERVERS,
    NFS_SHARE_COUNT,
    NFS_V3_CLIENT_COUNT,
    NFS_V4_CLIENT_COUNT,
    NFS_V4_ENABLED,
    NTP_SERVER_BURST_COUNT,
    NTP_SERVER_COUNT,
    NTP_SERVER_IBURST_COUNT,
    NTP_SERVER_MAX_POLL_MINUTES,
    NTP_SERVER_MIN_POLL_MINUTES,
    NTP_SERVER_PREFER_COUNT,
    NVMET_HOST_COUNT,
    NVMET_NAMESPACE_COUNT,
    NVMET_PORT_COUNT,
    NVMET_SESSION_COUNT,
    NVMET_SUBSYS_COUNT,
    POOL_ALLOCATED_BYTES,
    POOL_AUTOTRIM_ENABLED,
    POOL_COUNT,
    POOL_DEDUP_RATIO,
    POOL_DEDUP_TABLE_SIZE_BYTES,
    POOL_EXPAND_PERCENT,
    POOL_EXPAND_REFLOWED_BYTES,
    POOL_EXPAND_SIZE_BYTES,
    POOL_EXPAND_TO_REFLOW_BYTES,
    POOL_FRAGMENTATION,
    POOL_FREE_BYTES,
    POOL_HEALTHY,
    POOL_LAST_SCAN_TS,
    POOL_REALTIME_AVAILABLE_BYTES,
    POOL_REALTIME_READ_BYTES,
    POOL_REALTIME_TOTAL_BYTES,
    POOL_REALTIME_USED_BYTES,
    POOL_REALTIME_WRITE_BYTES,
    POOL_RESILVER_ENABLED,
    POOL_SCAN_BYTES_PROCESSED,
    POOL_SCAN_BYTES_TOTAL,
    POOL_SCAN_ERRORS,
    POOL_SCAN_PERCENT,
    POOL_SCAN_SECONDS_REMAINING,
    POOL_SCRUB_LAST_RUN_TS,
    POOL_SCRUB_TASK_COUNT,
    POOL_SCRUB_TASK_ENABLED,
    POOL_SCRUB_TASK_STATE,
    POOL_SIZE_BYTES,
    POOL_STATUS,
    POOL_STATUS_CODE,
    POOL_VDEV_CHECKSUM_ERRORS,
    POOL_VDEV_READ_ERRORS,
    POOL_VDEV_WRITE_ERRORS,
    POOL_WARNING,
    PRIVILEGE_COUNT,
    REPLICATION_MAX_PARALLEL,
    REPORTING_ENABLED,
    REPORTING_EXPORTER_COUNT,
    REPORTING_TIER0_RETENTION_DAYS,
    REPORTING_TIER1_RETENTION_DAYS,
    REPORTING_TIER1_UPDATE_INTERVAL_SECONDS,
    SCRAPE_DURATION,
    SCRAPE_SUCCESS,
    SERVICE_COUNT,
    SERVICE_ENABLED,
    SERVICE_RUNNING,
    SMB1_ENABLED,
    SMB_CONNECTION_COUNT,
    SMB_ENCRYPTION_MODE,
    SMB_MULTICHANNEL_ENABLED,
    SMB_NTLMV1_AUTH_ENABLED,
    SMB_OPEN_FILE_COUNT,
    SMB_SESSION_COUNT,
    SMB_SHARE_COUNT,
    SNAPSHOT_OLDEST_TS,
    SNAPSHOT_TASK_MAX_COUNT,
    SNAPSHOT_TASK_MAX_TOTAL_COUNT,
    SNAPSHOT_TOTAL_COUNT,
    SNMP_ENABLED,
    SSH_ENABLED,
    STATIC_ROUTE_COUNT,
    SUPPORT_AVAILABLE,
    SUPPORT_AVAILABLE_AND_ENABLED,
    SYSTEM_BOOT_CHANGES_TOTAL,
    SYSTEM_GLOBAL_ID,
    SYSTEM_HOST_ID,
    SYSTEM_MANAGED_BY_TRUECOMMAND,
    SYSTEM_PRODUCT_TYPE,
    SYSTEM_READY,
    SYSTEM_REBOOT_REASON,
    SYSTEM_REBOOT_REQUIRED,
    SYSTEM_SECURITY_FIPS_CONFIGURED,
    SYSTEM_SECURITY_GPOS_STIG,
    SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT,
    SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS,
    SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS,
    SYSTEM_SECURITY_PASSWORD_MIN_LENGTH,
    SYSTEM_STATE,
    SYSTEM_VERSION,
    SYSTEMDATASET_POOL,
    TASK_COUNT,
    TASK_ENABLED,
    TASK_LAST_RUN_TS,
    TASK_STATE,
    TN_CONNECT_STATUS,
    TRUECOMMAND_STATUS,
    TRUENAS_IS_IX_HARDWARE,
    TRUENAS_IS_PRODUCTION,
    TUNABLE_COUNT,
    TWOFACTOR_ENABLED,
    UI_HTTPS_PORT,
    UPDATE_AUTOCHECK_ENABLED,
    UPDATE_AVAILABLE,
    UPDATE_DOWNLOAD_PROGRESS_PERCENT,
    UPDATE_PROFILE_INFO,
    UPDATE_STATUS,
    UPDATE_VERSION_AVAILABLE,
    UPS_STATUS,
    VIRT_GLOBAL_STATE,
    VIRT_INSTANCE_COUNT,
    VIRT_INSTANCE_CPU,
    VIRT_INSTANCE_MEM,
    VIRT_INSTANCE_RUNNING,
    VIRT_VOLUME_COUNT,
    VM_AVAILABLE_MEMORY_BYTES,
    VM_COUNT,
    VM_FLAG_AMD_ASIDS,
    VM_FLAG_AMD_ASIDS_SUPPORTED,
    VM_FLAG_AMD_RVI,
    VM_FLAG_INTEL_VMX,
    VM_FLAG_UNRESTRICTED_GUEST,
    VM_MAX_VCPUS,
    VM_SUPPORTS_VIRTUALIZATION,
    VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT,
    VM_VIRTUALIZATION_DETAILS_SUPPORTED,
    VM_VMEMORY_IN_USE_BYTES,
    WEBSHARE_ENABLED,
    ZFS_ARC_AVAILABLE_BYTES,
    ZFS_ARC_FREE_MEMORY_BYTES,
    ZFS_ARC_SIZE_BYTES,
    ZFS_DEMAND_ACCESSES_RATE,
    ZFS_DEMAND_DATA_ACCESSES_RATE,
    ZFS_DEMAND_DATA_HIT_RATIO,
    ZFS_DEMAND_DATA_HITS_RATE,
    ZFS_DEMAND_DATA_IO_HIT_RATIO,
    ZFS_DEMAND_DATA_IO_HITS_RATE,
    ZFS_DEMAND_DATA_MISS_RATIO,
    ZFS_DEMAND_DATA_MISSES_RATE,
    ZFS_DEMAND_META_ACCESSES_RATE,
    ZFS_DEMAND_META_HIT_RATIO,
    ZFS_DEMAND_META_HITS_RATE,
    ZFS_DEMAND_META_IO_HIT_RATIO,
    ZFS_DEMAND_META_IO_HITS_RATE,
    ZFS_DEMAND_META_MISS_RATIO,
    ZFS_DEMAND_META_MISSES_RATE,
    ZFS_L2ARC_ACCESSES_RATE,
    ZFS_L2ARC_HIT_RATIO,
    ZFS_L2ARC_HITS_RATE,
    ZFS_L2ARC_MISS_RATIO,
    ZFS_L2ARC_MISSES_RATE,
    ZFS_L2ARC_READ_BYTES_RATE,
    ZFS_L2ARC_WRITE_BYTES_RATE,
    metric_name,
)
from .transport import JsonRpcError, JsonRpcWsClient  # noqa: F401 - compatibility re-export
from .version import __version__

# ``runtime`` historically re-exported metric objects as an incidental public
# surface used by downstream tests/integrations. Keep that surface even when a
# deprecated metric no longer has a producer in this API version.
for _metric_spec in METRIC_SPECS:
    globals().setdefault(_metric_spec.variable, _metric_spec.metric)
del _metric_spec

LOG = logging.getLogger("truenas_exporter")
EXPORTER_VERSION = __version__


def _redacted_traceback_text(ws_url: str) -> str:
    exc_text = "".join(traceback.format_exception(*sys.exc_info()))
    parsed = urlparse(ws_url)
    hostname = parsed.hostname
    if not hostname:
        return exc_text
    replacements = {hostname}
    if parsed.port is not None:
        replacements.add(f"{hostname}:{parsed.port}")
    elif parsed.scheme == "wss":
        replacements.add(f"{hostname}:443")
    elif parsed.scheme == "ws":
        replacements.add(f"{hostname}:80")
    for target in sorted(replacements, key=len, reverse=True):
        exc_text = exc_text.replace(target, "<redacted-host>")
    return exc_text


def _log_exception_redacted(
    logger: logging.Logger,
    level: int,
    message: str,
    ws_url: str,
    *args: Any,
) -> None:
    logger.log(level, "%s\n%s", message % args if args else message, _redacted_traceback_text(ws_url))

# Pre-compiled regex for _normalize_path — avoids recompiling on every recursive call
# inside _extract_generic_metrics / _extract_event_metrics.
_PATH_NORMALIZE_RE = re.compile(r"[^a-zA-Z0-9_./\-]")
_SENSITIVE_METRIC_PATH_RE = re.compile(
    r"(?:^|[._/\-])(?:api_?key|arguments?|attributes?|bindpw|client_?secret|commands?|"
    r"config|credential|descriptions?|email|environment|gids?|guids?|ids?|logs?|metadata|"
    r"notes?|pass(?:word|phrase)?|paths?|private_?key|raw|refresh_?token|scripts?|serial|"
    r"secret|token|uids?|usernames?|uuid)(?:$|[._/\-])",
    re.IGNORECASE,
)

_POLL_RESET_EXCLUDED_NAMES = {
    "truenas_up",
    "truenas_last_scrape_timestamp_seconds",
    "truenas_scrape_duration_seconds",
    "truenas_exporter_info",
    "truenas_event_last_message_timestamp_seconds",
    "truenas_event_stream_up",
    "truenas_event_numeric_value",
    "truenas_event_boolean_value",
    "truenas_event_status_value",
    "truenas_event_list_length",
    *_EVENT_SOURCE_BY_METRIC_NAME,
}

# Heavy middleware-side aggregations are slow-moving; refresh them less often
# while re-emitting cached values between refreshes.
DISK_TEMP_AGG_REFRESH_CYCLES = 10
SNAPSHOT_OLDEST_REFRESH_CYCLES = 10
HEAVY_QUERY_CACHE_MAX_STALE_FACTOR = 3


def _set_optional_bool_gauge(gauge: Any, value: Any) -> None:
    parsed = _as_optional_bool(value)
    if parsed is not None:
        gauge.set(1 if parsed else 0)


# ---------------------------------------------------------------------------
# Main exporter class
# ---------------------------------------------------------------------------

class TrueNASExporter:
    def __init__(
        self,
        config: Config,
        compatibility_profile: CompatibilityProfile = PROFILE_25_10,
    ) -> None:
        self.config = config
        self.compatibility_profile = compatibility_profile
        self.exporter_mode = config.exporter_mode
        self._lock = threading.RLock()
        self._event_thread: threading.Thread | None = None
        self._all_methods_discovered = False
        self._event_metric_series: dict[Any, set[tuple[str, ...]]] = {}
        self._collector_event_scalars: dict[str, float] = {}
        self._collector_event_series: dict[str, dict[tuple[str, ...], float]] = {}
        self._collector_event_messages: dict[str, float] = {}
        self._collector_event_stream_up: dict[str, float] = {}
        self._event_last_monotonic: dict[str, float] = {}
        self._expired_events: set[str] = set()
        self._stop_event = threading.Event()
        self._diagnostic_lock = threading.Lock()
        self._api_call_success: dict[str, float] = {}
        self._api_call_duration: dict[str, float] = {}
        self._api_call_errors: dict[tuple[str, str], float] = {}
        self._collector_errors: dict[str, float] = {}
        self._event_message_counts: dict[str, float] = {}
        self._last_scrape_success_monotonic: float | None = None
        self._last_scrape_attempt_monotonic: float | None = None
        self._snapshot_lock = threading.Lock()
        self._last_metric_snapshot_publish_monotonic = 0.0
        self._metric_snapshot_publish_timer: threading.Timer | None = None
        self._reset_poll_metrics()
        # Event-owned realtime scalar gauges are excluded from _reset_poll_metrics
        # (the event stream owns their lifecycle), so before the first event they
        # would read the prometheus_client default of 0.0. In collector mode the
        # initial snapshot below is served on /metrics until the first scrape
        # completes; force these to NaN so that window reports "absent" rather than
        # a fabricated zero (e.g. free-memory 0 / cpu-idle 0 triggering false alerts).
        for event_scalar in _REALTIME_EVENT_SCALAR_METRICS:
            event_scalar.set(float("nan"))
        self._metric_snapshot = tuple(REGISTRY.collect())
        self._scrape_thread: threading.Thread | None = None
        # Tracks the last-seen boot ID so we can increment the reboot counter
        # when it changes, rather than exposing a UUID-valued label.
        self._last_boot_id: str | None = None
        self._auto_skipped_methods: set[str] = set()
        self._auto_skipped_at: dict[str, float] = {}
        self._has_detected_concrete_profile = False
        self._disk_temp_agg_cycle = 0
        self._disk_temp_agg_disk_names: tuple[str, ...] = ()
        self._disk_temp_agg_cache: dict[tuple[str, str], float] = {}
        self._disk_temp_agg_last_success_cycle: int | None = None
        self._disk_temp_agg_last_attempt_cycle: int | None = None
        self._snapshot_oldest_cycle = 0
        self._snapshot_oldest_cached_value: float | None = None
        self._snapshot_oldest_has_cache = False
        self._snapshot_oldest_last_success_cycle: int | None = None
        self._snapshot_oldest_last_attempt_cycle: int | None = None

    # ------------------------------------------------------------------
    # Internal utilities
    # ------------------------------------------------------------------

    def _normalize_path(self, path: str) -> str:
        # Use module-level pre-compiled regex — avoids recompiling on every
        # recursive call inside the generic extractor.
        return _PATH_NORMALIZE_RE.sub("_", path)[:200]

    def _is_collector_mode(self) -> bool:
        return self.exporter_mode == "collector"

    def _reset_poll_metrics(self) -> None:
        """Start a scrape from a fresh polling snapshot.

        Labelled polling series are removed and scalar polling gauges become NaN
        until their documented source successfully produces a value.  Event-owned
        telemetry and cumulative counters have independent lifetime rules.
        """
        for spec in METRIC_SPECS:
            if spec.metric_type != "gauge" or spec.name in _POLL_RESET_EXCLUDED_NAMES:
                continue
            if spec.labels:
                spec.metric.clear()
            else:
                cast(Gauge, spec.metric).set(float("nan"))

    def _reset_poll_cycle_metrics(self) -> None:
        self._reset_poll_metrics()

        # Clear label-carrying gauges INSIDE the lock to prevent a window where
        # Prometheus scrapes partially-cleared / partially-refilled data.
        SYSTEM_STATE.clear()
        SYSTEM_REBOOT_REASON.clear()
        API_KEY_EXPIRY_TS.clear()
        FAILOVER_NODE_REBOOT_REQUIRED.clear()
        BOOT_POOL_STATUS.clear()
        BOOT_POOL_SCAN_STATE.clear()
        POOL_HEALTHY.clear()
        POOL_STATUS.clear()
        POOL_STATUS_CODE.clear()
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
        UPDATE_PROFILE_INFO.clear()
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
        DIRECTORYSERVICES_SERVICE_TYPE.clear()
        # API call diagnostics — clear each scrape so methods removed from BASE_METHODS
        # don't leave zombie label series with their last-seen values.
        API_CALL_SUCCESS.clear()
        API_CALL_DURATION.clear()

    def _poll_metrics_are_too_stale(self) -> bool:
        last_success = self._last_scrape_success_monotonic
        if last_success is None:
            return False
        # Bound stale data retention across repeated pre-auth failures.  The
        # window is intentionally longer than readiness so dashboards can show
        # last-known values with truenas_up=0 during short outages.
        max_age = max(3 * self.config.interval_seconds, 300)
        return time.monotonic() - last_success > max_age

    def _event_is_fresh(self, event: str, now: float | None = None) -> bool:
        updated = self._event_last_monotonic.get(event)
        if updated is None:
            return False
        current = time.monotonic() if now is None else now
        return current - updated <= self.config.event_stale_after_seconds

    def _clear_cached_event_metrics(self, event: str) -> None:
        """Remove the previous complete snapshot for one dedicated event."""

        for metric in _EVENT_METRICS.get(event, ()):
            name = metric_name(metric)
            self._collector_event_scalars.pop(name, None)
            self._collector_event_series.pop(name, None)

    def _clear_generic_event_metrics(self, event: str) -> None:
        if not self.config.enable_generic_event_metrics or self._is_collector_mode():
            return
        for metric in (
            EVENT_NUMERIC_VALUE,
            EVENT_BOOLEAN_VALUE,
            EVENT_STATUS_VALUE,
            EVENT_LIST_LENGTH,
        ):
            self._replace_event_metric_series(metric, {}, series_key=(metric, event))

    def _expire_stale_events(self, force: bool = False) -> None:
        """Invalidate event telemetry. Caller must hold ``self._lock``."""
        now = time.monotonic()
        events = set(_EVENT_METRICS) | set(self._event_last_monotonic)
        for event in events:
            if not force and self._event_is_fresh(event, now):
                continue
            if event in self._expired_events:
                continue
            self._expired_events.add(event)
            self._clear_cached_event_metrics(event)
            self._clear_generic_event_metrics(event)
            if self._is_collector_mode():
                continue
            for metric in _EVENT_METRICS.get(event, ()):
                if metric in _REALTIME_EVENT_SCALAR_METRICS:
                    metric.set(float("nan"))
                else:
                    self._replace_event_metric_series(metric, {})

    def _publish_cached_events_to_default_registry(self) -> None:
        """Publish collector-mode event caches for the full-parity registry bridge."""
        with self._lock:
            for event, metrics in _EVENT_METRICS.items():
                fresh = self._event_is_fresh(event)
                for metric in metrics:
                    name = metric_name(metric)
                    if metric in _REALTIME_EVENT_SCALAR_METRICS:
                        value = self._collector_event_scalars.get(name)
                        metric.set(value if fresh and value is not None else float("nan"))
                        continue
                    metric.clear()
                    if not fresh:
                        continue
                    for labels, value in self._collector_event_series.get(name, {}).items():
                        metric.labels(*labels).set(value)

            EVENT_LAST_MESSAGE_TS.clear()
            for event, value in self._collector_event_messages.items():
                EVENT_LAST_MESSAGE_TS.labels(event=event).set(value)
            EVENT_STREAM_UP.clear()
            for event, value in self._collector_event_stream_up.items():
                EVENT_STREAM_UP.labels(event=event).set(value)

    def is_ready(self) -> bool:
        last_success = self._last_scrape_success_monotonic
        if last_success is None:
            return False
        max_age = max(
            self.config.scrape_budget_seconds * 2,
            self.config.interval_seconds * 2,
            30,
        )
        return time.monotonic() - last_success <= max_age

    def stop(self) -> None:
        self._stop_event.set()

    def metric_snapshot(self) -> tuple[Any, ...]:
        """Return the last complete immutable-by-convention metric snapshot."""
        with self._snapshot_lock:
            return self._metric_snapshot

    def _publish_metric_snapshot(self) -> None:
        families = tuple(REGISTRY.collect())
        with self._snapshot_lock:
            self._metric_snapshot = families
            self._last_metric_snapshot_publish_monotonic = time.monotonic()
            self._metric_snapshot_publish_timer = None

    def _publish_metric_snapshot_locked(self) -> None:
        """Timer-fired publish target: must acquire the scrape lock itself.

        Unlike the other publish call sites (scrape tail, event dispatch),
        which already run inside ``self._lock``, a ``threading.Timer`` fires
        on its own thread with no lock held. Without acquiring ``self._lock``
        here, the timer can race a concurrent ``scrape_once`` that has wiped
        the registry mid-cycle and publish a partial snapshot as "complete".
        """
        with self._lock:
            self._publish_metric_snapshot()

    def _publish_metric_snapshot_throttled(self, minimum_interval_seconds: float = 1.0) -> None:
        now = time.monotonic()
        publish_now = False
        timer: threading.Timer | None = None
        with self._snapshot_lock:
            elapsed = now - self._last_metric_snapshot_publish_monotonic
            if elapsed >= minimum_interval_seconds:
                if self._metric_snapshot_publish_timer is not None:
                    self._metric_snapshot_publish_timer.cancel()
                    self._metric_snapshot_publish_timer = None
                publish_now = True
            elif (
                self._metric_snapshot_publish_timer is None
                or not self._metric_snapshot_publish_timer.is_alive()
            ):
                timer = threading.Timer(
                    minimum_interval_seconds - elapsed,
                    self._publish_metric_snapshot_locked,
                )
                timer.daemon = True
                self._metric_snapshot_publish_timer = timer
        if timer is not None:
            timer.start()
        if publish_now:
            self._publish_metric_snapshot()

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

    def _collector_error(self, name: str, message: str, *, exc_info: bool = True) -> None:
        COLLECTOR_ERRORS_TOTAL.labels(collector=name).inc()
        with self._diagnostic_lock:
            self._collector_errors[name] = self._collector_errors.get(name, 0.0) + 1.0
        LOG.debug(message, exc_info=exc_info)

    def _profile_for_version_short(self, version: str) -> CompatibilityProfile:
        normalized = version.strip()
        if normalized.startswith("TrueNAS-SCALE-"):
            normalized = normalized.removeprefix("TrueNAS-SCALE-")
        if normalized.startswith("25.10."):
            return get_profile("25.10")
        if normalized.startswith("26.0."):
            return get_profile("26.0")
        return get_profile("unknown")

    def _note_profile(self, detected_profile: CompatibilityProfile) -> None:
        # Profile reads stay lock-free: CPython attribute-reference reads are atomic.
        # Guard writes with auto-skip clearing so both exporter threads see a coherent update.
        with self._lock:
            current_profile = self.compatibility_profile
            if detected_profile.name == "unknown":
                if (
                    self._has_detected_concrete_profile
                    and current_profile.name in {"25.10", "26.0"}
                ):
                    return
                if current_profile is not detected_profile or current_profile.name != detected_profile.name:
                    cleared = len(self._auto_skipped_methods)
                    self._auto_skipped_methods.clear()
                    self._auto_skipped_at.clear()
                    LOG.info(
                        "Cleared %d auto-skipped methods after compatibility profile change: %s -> %s",
                        cleared,
                        current_profile.name,
                        detected_profile.name,
                    )
                self.compatibility_profile = detected_profile
                return

            if current_profile is not detected_profile or current_profile.name != detected_profile.name:
                cleared = len(self._auto_skipped_methods)
                self._auto_skipped_methods.clear()
                self._auto_skipped_at.clear()
                LOG.info(
                    "Cleared %d auto-skipped methods after compatibility profile change: %s -> %s",
                    cleared,
                    current_profile.name,
                    detected_profile.name,
                )
            self.compatibility_profile = detected_profile
            self._has_detected_concrete_profile = True

    def _bootstrap_connection(self, client: JsonRpcWsClient) -> Any | None:
        """Authenticate and select the compatibility profile before telemetry."""

        client.authenticate(
            self.config.api_key,
            call=lambda method, params: self._call(client, method, params),
        )
        try:
            version_short = self._call(client, "system.version_short", [])
        except Exception:
            self._note_profile(get_profile("unknown"))
            self._collector_error(
                "version_detection",
                "system.version_short detection failed; using unknown compatibility profile",
                exc_info=False,
            )
            return None

        if isinstance(version_short, str):
            self._note_profile(self._profile_for_version_short(version_short))
            return version_short

        self._note_profile(get_profile("unknown"))
        self._collector_error(
            "version_detection",
            f"system.version_short returned malformed {type(version_short).__name__}; "
            "using unknown compatibility profile",
            exc_info=False,
        )
        return version_short

    def _profile_normalized_bytes(self, method: str, value: Any) -> float | None:
        numeric = _as_float(value)
        if numeric is None or numeric < 0:
            return None
        conversion = self.compatibility_profile.unit_conversions.get(method)
        if conversion is None:
            return numeric
        return numeric * conversion.multiplier

    def _response_scalar(self, value: Any) -> Any:
        if isinstance(value, dict):
            for field_name in ("value", "parsed", "rawvalue"):
                if field_name in value:
                    return self._response_scalar(value[field_name])
        return value

    def _response_field(self, item: dict[str, Any], *field_names: str) -> Any:
        for field_name in field_names:
            if field_name in item:
                return self._response_scalar(item[field_name])
        properties = item.get("properties")
        if isinstance(properties, dict):
            for field_name in field_names:
                if field_name in properties:
                    return self._response_scalar(properties[field_name])
        return None

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
                LOG.debug("Failed removing stale event series from %s", metric_name(metric), exc_info=True)

        for label_values, value in series.items():
            metric.labels(*label_values).set(value)

        self._event_metric_series[key] = current

    def _call(self, client: JsonRpcWsClient, method: str, params: list[Any] | None = None) -> Any:
        self._require_profile_method(method)
        started = time.time()
        try:
            result = client.call(method, params)
            duration = max(0.0, time.time() - started)
            API_CALL_SUCCESS.labels(method=method).set(1)
            API_CALL_DURATION.labels(method=method).set(duration)
            with self._diagnostic_lock:
                self._api_call_success[method] = 1.0
                self._api_call_duration[method] = duration
            return result
        except Exception as exc:
            duration = max(0.0, time.time() - started)
            API_CALL_SUCCESS.labels(method=method).set(0)
            API_CALL_DURATION.labels(method=method).set(duration)
            # Counter: increments on each error; never creates stale zero-value series.
            API_CALL_ERRORS_TOTAL.labels(method=method, error_type=type(exc).__name__).inc()
            with self._diagnostic_lock:
                self._api_call_success[method] = 0.0
                self._api_call_duration[method] = duration
                key = (method, type(exc).__name__)
                self._api_call_errors[key] = self._api_call_errors.get(key, 0.0) + 1.0
            raise

    def _call_query_with_fallback(
        self,
        client: JsonRpcWsClient,
        method: str,
        preferred_options: dict[str, Any],
        *,
        allow_bare_fallback: bool = True,
    ) -> Any:
        try:
            return self._call(client, method, [[], preferred_options])
        except Exception:
            if not allow_bare_fallback:
                raise
            LOG.debug("Falling back to bare call for %s", method)
            return self._call(client, method, [])

    def _query_count(
        self,
        client: JsonRpcWsClient,
        method: str,
        filters: list[Any] | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> int:
        self._require_profile_method(method)
        options: dict[str, Any] = {"count": True}
        if extra_options:
            options.update(extra_options)

        result = self._call(client, method, [filters or [], options])
        if type(result) is not int or result < 0:
            raise TypeError(
                f"{method} count query returned invalid nonnegative integer: "
                f"{result!r} ({type(result).__name__})"
            )
        return result

    def _count_or_len(
        self,
        client: JsonRpcWsClient,
        method: str,
        items: list[Any],
        limit: int,
        filters: list[Any] | None = None,
        extra_options: dict[str, Any] | None = None,
    ) -> int:
        if len(items) < limit:
            return len(items)
        return self._query_count(client, method, filters, extra_options)

    def _require_profile_method(self, method: str) -> None:
        if self.compatibility_profile.allows_method(method):
            return
        if method in self.compatibility_profile.removed_methods:
            self._collector_error(
                "profile_removed_method_suppressed",
                f"Suppressed removed method {method!r} for {self.compatibility_profile.name} profile",
                exc_info=False,
            )
            raise RuntimeError(
                f"method {method!r} was removed and is outside the "
                f"{self.compatibility_profile.name} compatibility profile"
            )
        self._collector_error(
            "profile_method_blocked",
            f"Blocked method {method!r} outside {self.compatibility_profile.name} profile",
            exc_info=False,
        )
        raise RuntimeError(
            f"method {method!r} is outside the {self.compatibility_profile.name} compatibility profile"
        )

    def _extract_snapshot_creation_timestamp(self, snapshot: Any) -> float | None:
        if not isinstance(snapshot, dict):
            return None

        ts = _parse_ts(_first_not_none(snapshot.get("creation_parsed"), snapshot.get("creation")))
        if ts is not None:
            return ts

        properties = snapshot.get("properties")
        if isinstance(properties, dict):
            return _parse_ts(properties.get("creation"))

        return None

    def _extract_smart_test_timestamp(self, test: Any) -> float | None:
        if not isinstance(test, dict):
            return None

        def _candidate_ts(value: Any) -> float | None:
            ts = _parse_ts(value)
            if ts is not None:
                return ts
            if isinstance(value, dict):
                for nested_key in ("value", "parsed", "rawvalue", "time", "timestamp", "datetime"):
                    ts = _parse_ts(value.get(nested_key))
                    if ts is not None:
                        return ts
            return None

        for key in (
            "timestamp",
            "time_finished",
            "finished_at",
            "time_started",
            "started_at",
            "datetime",
            "date",
            "created_at",
            "created",
            "updated_at",
            "end_time",
        ):
            ts = _candidate_ts(test.get(key))
            if ts is not None:
                return ts

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

            if _as_optional_bool(alert.get("dismissed")) is True:
                dismissed_count += 1
            if _as_optional_bool(alert.get("one_shot")) is True:
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
        if oldest_ts is not None:
            ALERT_OLDEST_TS.set(oldest_ts)

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
                # Exact per-state counts intentionally retained: the counts are
                # used to size the subsequent detail query limit and to populate
                # the per-state gauge without fetching all jobs twice.
                count = self._query_count(client, "core.get_jobs", [["state", "=", state]])
            except Exception:
                self._collector_error("jobs", f"core.get_jobs count failed for state={state}")
                return

            state_counts[state] = count
            total_active += count
            JOB_ACTIVE_COUNT_BY_STATE.labels(state=state).set(count)

        JOB_ACTIVE_COUNT.set(total_active)

        if total_active == 0:
            JOB_ABORTABLE_ACTIVE_COUNT.set(0)
            JOB_TRANSIENT_ACTIVE_COUNT.set(0)
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

            if _as_optional_bool(job.get("abortable")) is True:
                abortable_count += 1
            if _as_optional_bool(job.get("transient")) is True:
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
        cache: dict[str, Any] | None = None,
    ) -> dict[str, bool]:
        ordered_names: list[str] = []
        seen: set[str] = set()
        for name in service_names:
            if name and name not in seen:
                ordered_names.append(name)
                seen.add(name)

        if not ordered_names:
            return {}

        cached_services = cache.get("service.query") if cache is not None else None
        if isinstance(cached_services, list):
            services = [
                svc
                for svc in cached_services
                if isinstance(svc, dict)
                and (svc.get("service") or svc.get("name")) in seen
            ]
        else:
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
                service_name = svc.get("service") or svc.get("name")
                if isinstance(service_name, str) and service_name:
                    enabled = _as_optional_bool(svc.get("enable"))
                    if enabled is not None:
                        enabled_by_service[service_name] = enabled

        return enabled_by_service

    def _is_safe_read_method(self, method: str) -> bool:
        if method in self.config.exclude_methods:
            return False
        if (
            not is_documented_read_only_method(method, self.compatibility_profile)
            or is_sensitive_read_method(method)
            or is_unsafe_generic_read_method(method)
        ):
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
        if method not in BASE_METHODS and not self.compatibility_profile.allows_telemetry_method(method):
            return False
        if SAFE_DENY_RE.search(method):
            return False
        return bool(SAFE_ALLOW_RE.fullmatch(method)) and self.compatibility_profile.allows_method(method)

    def _auto_params(self, method: str) -> list[Any]:
        if method == "app.query":
            return [[], {"limit": self.compatibility_profile.query_limit_for(method, self.config.query_limit), "select": [
                "name",
                "state",
                "upgrade_available",
                "image_updates_available",
                "custom_app",
                "migrated",
                "active_workloads",
            ]}]
        if method == "disk.query":
            return [[], {"limit": self.compatibility_profile.query_limit_for(method, self.config.query_limit), "select": [
                "name", "identifier", "size", "type", "rotationrate", "pool",
            ]}]
        if method == "vm.query":
            return [[], {"limit": self.compatibility_profile.query_limit_for(method, self.config.query_limit), "select": [
                "id", "name", "status", "autostart", "vcpus", "memory",
            ]}]
        if method == "alertservice.query":
            return [[], {"limit": self.compatibility_profile.query_limit_for(method, self.config.query_limit), "select": [
                "id", "name", "type__title", "enabled",
            ]}]
        if method.endswith(".query"):
            return [[], {"limit": self.compatibility_profile.query_limit_for(method, self.config.query_limit)}]
        if method in {"nfs.get_nfs3_clients", "nfs.get_nfs4_clients",
                      "iscsi.global.sessions", "route.system_routes",
                      # core.get_jobs can return thousands of records on busy systems;
                      # apply the same query_limit guard used for .query methods.
                      "core.get_jobs"}:
            return [[], {"limit": self.compatibility_profile.query_limit_for(method, self.config.query_limit)}]
        if method in {"disk.details", "ipmi.chassis.info", "zfs.resource.query"}:
            return [{}]
        if method == "vm.get_available_memory":
            return [False]
        if method in {"reporting.graph", "reporting.netdata_graph"}:
            return ["cpu", {"unit": "HOURLY"}]
        return []

    def _should_runtime_skip_method(self, exc: Exception) -> bool:
        message = str(exc)
        return any(pattern.search(message) for pattern in _AUTO_SKIP_ERROR_PATTERNS)

    def _safe_call_auto(self, client: JsonRpcWsClient, method: str) -> Any | None:
        if method in self._auto_skipped_methods:
            skipped_at = self._auto_skipped_at.get(method)
            if skipped_at is None or time.monotonic() - skipped_at < 86400:
                return None
            self._auto_skipped_methods.discard(method)
            self._auto_skipped_at.pop(method, None)

        params = self._auto_params(method)
        try:
            return self._call(client, method, params)
        except Exception as exc:
            if self._should_runtime_skip_method(exc):
                self._auto_skipped_methods.add(method)
                self._auto_skipped_at[method] = time.monotonic()
                LOG.info("Auto-skip method after runtime error: %s", method)
                COLLECTOR_ERRORS_TOTAL.labels(collector="auto_discovery_skipped").inc()
                return None
            COLLECTOR_ERRORS_TOTAL.labels(collector="auto_discovery").inc()
            return None

    def _discover_methods(self, client: JsonRpcWsClient) -> list[str]:
        discovered: list[str] = []
        if self.config.auto_discover_methods:
            methods = self._safe_call_auto(client, "core.get_methods")
            if isinstance(methods, dict):
                for name in methods:
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
        if depth > self.config.max_depth or _SENSITIVE_METRIC_PATH_RE.search(path):
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
        if depth > self.config.max_depth or _SENSITIVE_METRIC_PATH_RE.search(path):
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

    def _cache_app_stats_event(self, payload: dict[str, Any]) -> None:
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

            cpu = _as_float(_first_not_none(app_data.get("cpu_usage"), app_data.get("cpu")))
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
                    iface = _str_label(net.get("interface_name"), "unknown")
                    rx = _as_float(net.get("rx_bytes"))
                    tx = _as_float(net.get("tx_bytes"))
                    if rx is not None:
                        app_net_rx[(app_name, iface)] = rx
                    if tx is not None:
                        app_net_tx[(app_name, iface)] = tx

            blkio = app_data.get("blkio")
            if isinstance(blkio, dict):
                blkio_read = _as_float(blkio.get("read"))
                if blkio_read is not None:
                    app_blkio_read[(app_name,)] = blkio_read
                blkio_write = _as_float(blkio.get("write"))
                if blkio_write is not None:
                    app_blkio_write[(app_name,)] = blkio_write

        self._collector_event_series[metric_name(APP_CPU_PERCENT)] = app_cpu
        self._collector_event_series[metric_name(APP_MEMORY_BYTES)] = app_memory
        self._collector_event_series[metric_name(APP_NET_RX_BYTES_RATE)] = app_net_rx
        self._collector_event_series[metric_name(APP_NET_TX_BYTES_RATE)] = app_net_tx
        self._collector_event_series[metric_name(APP_BLKIO_READ_BYTES)] = app_blkio_read
        self._collector_event_series[metric_name(APP_BLKIO_WRITE_BYTES)] = app_blkio_write

    def _cache_virt_metrics_event(self, payload: dict[str, Any]) -> None:
        fields: Any = payload.get("fields", payload)
        instances: list[dict[str, Any]] = []
        if isinstance(fields, list):
            instances = [item for item in fields if isinstance(item, dict)]
        elif isinstance(fields, dict):
            for instance_name, instance_metrics in fields.items():
                if not isinstance(instance_metrics, dict):
                    continue
                instances.append({"name": instance_name, **instance_metrics})
        else:
            return

        virt_cpu: dict[tuple[str, ...], float] = {}
        virt_mem: dict[tuple[str, ...], float] = {}

        for inst_data in instances:
            inst_name = _str_label(inst_data.get("name") or inst_data.get("instance"), "unknown")

            cpu = _as_float(_first_not_none(inst_data.get("cpu"), inst_data.get("cpu_usage")))
            if cpu is not None:
                virt_cpu[(inst_name,)] = cpu

            mem = _as_float(_first_not_none(inst_data.get("memory"), inst_data.get("memory_usage")))
            if mem is not None:
                virt_mem[(inst_name,)] = mem

        self._collector_event_series[metric_name(VIRT_INSTANCE_CPU)] = virt_cpu
        self._collector_event_series[metric_name(VIRT_INSTANCE_MEM)] = virt_mem

    def _cache_realtime_event(self, payload: dict[str, Any]) -> None:
        cpu_section = payload.get("cpu") or {}
        cpu_data = cpu_section.get("cpu") if isinstance(cpu_section, dict) else {}
        if not isinstance(cpu_data, dict):
            cpu_data = {}

        total_cpu_percent = _as_float(_first_not_none(
            cpu_data.get("percent"),
            cpu_data.get("usage"),
            cpu_section.get("percent") if isinstance(cpu_section, dict) else None,
        ))
        if total_cpu_percent is not None:
            self._collector_event_scalars[metric_name(CPU_USAGE_PERCENT)] = total_cpu_percent

        user_cpu_percent = _as_float(_first_not_none(
            cpu_data.get("user"), cpu_section.get("user") if isinstance(cpu_section, dict) else None
        ))
        if user_cpu_percent is not None:
            self._collector_event_scalars[metric_name(CPU_USER_PERCENT)] = user_cpu_percent

        system_cpu_percent = _as_float(_first_not_none(
            cpu_data.get("system"), cpu_section.get("system") if isinstance(cpu_section, dict) else None
        ))
        if system_cpu_percent is not None:
            self._collector_event_scalars[metric_name(CPU_SYSTEM_PERCENT)] = system_cpu_percent

        idle_cpu_percent = _as_float(_first_not_none(
            cpu_data.get("idle"), cpu_section.get("idle") if isinstance(cpu_section, dict) else None
        ))
        if idle_cpu_percent is not None:
            self._collector_event_scalars[metric_name(CPU_IDLE_PERCENT)] = idle_cpu_percent

        iowait_cpu_percent = _as_float(_first_not_none(
            cpu_data.get("iowait"), cpu_section.get("iowait") if isinstance(cpu_section, dict) else None
        ))
        if iowait_cpu_percent is not None:
            self._collector_event_scalars[metric_name(CPU_IOWAIT_PERCENT)] = iowait_cpu_percent

        interrupt_cpu_percent = _as_float(_first_not_none(
            cpu_data.get("interrupt"), cpu_section.get("interrupt") if isinstance(cpu_section, dict) else None
        ))
        if interrupt_cpu_percent is not None:
            self._collector_event_scalars[metric_name(CPU_INTERRUPT_PERCENT)] = interrupt_cpu_percent

        cpu_core_usage: dict[tuple[str, ...], float] = {}
        for per_cpu_candidate in (
            cpu_data.get("per_cpu"),
            cpu_section.get("per_cpu") if isinstance(cpu_section, dict) else None,
            cpu_data.get("usage"),
            cpu_section.get("usage") if isinstance(cpu_section, dict) else None,
        ):
            cpu_core_usage = _extract_labeled_numeric_series(
                per_cpu_candidate,
                value_keys=("percent", "usage", "value"),
                normalize_label=True,
            )
            if cpu_core_usage:
                break
        if isinstance(cpu_section, dict):
            sibling_core_usage: dict[tuple[str, ...], float] = {}
            for core_name, core_data in cpu_section.items():
                if not re.fullmatch(r"cpu\d+", str(core_name)) or not isinstance(core_data, dict):
                    continue
                usage = _as_float(core_data.get("usage"))
                if usage is not None:
                    sibling_core_usage[(_normalize_core_label(core_name),)] = usage
            if sibling_core_usage:
                cpu_core_usage = sibling_core_usage
        self._collector_event_series[metric_name(CPU_CORE_USAGE_PERCENT)] = cpu_core_usage

        cpu_temps: dict[tuple[str, ...], float] = {}
        for temp_candidate in (
            cpu_section.get("temperature") if isinstance(cpu_section, dict) else None,
            cpu_section.get("temperatures") if isinstance(cpu_section, dict) else None,
            cpu_data.get("temperature"),
            cpu_data.get("temperatures"),
        ):
            cpu_temps = _extract_labeled_numeric_series(
                temp_candidate,
                value_keys=("temperature", "temp", "celsius", "value"),
                normalize_label=True,
            )
            if cpu_temps:
                break
        if isinstance(cpu_section, dict):
            sibling_cpu_temps: dict[tuple[str, ...], float] = {}
            for core_name, core_data in cpu_section.items():
                if not re.fullmatch(r"cpu\d+", str(core_name)) or not isinstance(core_data, dict):
                    continue
                temp = _as_float(core_data.get("temp"))
                if temp is not None:
                    sibling_cpu_temps[(_normalize_core_label(core_name),)] = temp
            if sibling_cpu_temps:
                cpu_temps = sibling_cpu_temps
        self._collector_event_series[metric_name(CPU_TEMPERATURE_C)] = cpu_temps

        mem = payload.get("memory")
        if isinstance(mem, dict):
            total = _as_float(mem.get("physical_memory_total"))
            avail = _as_float(mem.get("physical_memory_available"))

            if total is not None:
                self._collector_event_scalars[metric_name(MEMORY_PHYSICAL_TOTAL_BYTES)] = total
            if avail is not None:
                self._collector_event_scalars[metric_name(MEMORY_PHYSICAL_AVAILABLE_BYTES)] = avail
            if total is not None and avail is not None:
                self._collector_event_scalars[metric_name(MEMORY_PHYSICAL_USED_BYTES)] = total - avail

            arc_size = _as_float(mem.get("arc_size"))
            if arc_size is not None:
                self._collector_event_scalars[metric_name(ZFS_ARC_SIZE_BYTES)] = arc_size
            arc_free = _as_float(mem.get("arc_free_memory"))
            if arc_free is not None:
                self._collector_event_scalars[metric_name(ZFS_ARC_FREE_MEMORY_BYTES)] = arc_free
            arc_avail = _as_float(mem.get("arc_available_memory"))
            if arc_avail is not None:
                self._collector_event_scalars[metric_name(ZFS_ARC_AVAILABLE_BYTES)] = arc_avail

        zfs = payload.get("zfs")
        if isinstance(zfs, dict):
            zfs_value_metrics = (
                ("demand_accesses_per_second", ZFS_DEMAND_ACCESSES_RATE),
                ("demand_data_accesses_per_second", ZFS_DEMAND_DATA_ACCESSES_RATE),
                ("demand_data_hits_per_second", ZFS_DEMAND_DATA_HITS_RATE),
                ("demand_data_io_hits_per_second", ZFS_DEMAND_DATA_IO_HITS_RATE),
                ("demand_data_misses_per_second", ZFS_DEMAND_DATA_MISSES_RATE),
                ("demand_metadata_accesses_per_second", ZFS_DEMAND_META_ACCESSES_RATE),
                ("demand_metadata_hits_per_second", ZFS_DEMAND_META_HITS_RATE),
                ("demand_metadata_io_hits_per_second", ZFS_DEMAND_META_IO_HITS_RATE),
                ("demand_metadata_misses_per_second", ZFS_DEMAND_META_MISSES_RATE),
                ("l2arc_hits_per_second", ZFS_L2ARC_HITS_RATE),
                ("l2arc_misses_per_second", ZFS_L2ARC_MISSES_RATE),
                ("total_l2arc_accesses_per_second", ZFS_L2ARC_ACCESSES_RATE),
                ("bytes_read_per_second_from_the_l2arc", ZFS_L2ARC_READ_BYTES_RATE),
                ("bytes_written_per_second_to_the_l2arc", ZFS_L2ARC_WRITE_BYTES_RATE),
            )
            for field, gauge in zfs_value_metrics:
                value = _as_float(zfs.get(field))
                if value is not None:
                    self._collector_event_scalars[metric_name(gauge)] = value

            zfs_percent_metrics = (
                ("demand_data_hit_percentage", ZFS_DEMAND_DATA_HIT_RATIO),
                ("demand_data_io_hit_percentage", ZFS_DEMAND_DATA_IO_HIT_RATIO),
                ("demand_data_miss_percentage", ZFS_DEMAND_DATA_MISS_RATIO),
                ("demand_metadata_hit_percentage", ZFS_DEMAND_META_HIT_RATIO),
                ("demand_metadata_io_hit_percentage", ZFS_DEMAND_META_IO_HIT_RATIO),
                ("demand_metadata_miss_percentage", ZFS_DEMAND_META_MISS_RATIO),
                ("l2arc_access_hit_percentage", ZFS_L2ARC_HIT_RATIO),
                ("l2arc_miss_percentage", ZFS_L2ARC_MISS_RATIO),
            )
            for field, gauge in zfs_percent_metrics:
                value = _as_percent(zfs.get(field))
                if value is not None:
                    self._collector_event_scalars[metric_name(gauge)] = value / 100.0

        # TrueNAS 25.10.2 names this realtime disk I/O map "disls"; accept the
        # older "disks" spelling as a compatibility fallback.
        disks = _first_not_none(payload.get("disls"), payload.get("disks"))
        disk_read_bytes: dict[tuple[str, ...], float] = {}
        disk_write_bytes: dict[tuple[str, ...], float] = {}
        disk_read_ops: dict[tuple[str, ...], float] = {}
        disk_write_ops: dict[tuple[str, ...], float] = {}
        disk_busy: dict[tuple[str, ...], float] = {}
        if isinstance(disks, dict):
            first_val = next(iter(disks.values()), None)
            keys = (
                ("read_bytes", disk_read_bytes),
                ("write_bytes", disk_write_bytes),
                ("read_ops", disk_read_ops),
                ("write_ops", disk_write_ops),
                ("busy", disk_busy),
            )
            if isinstance(first_val, dict):
                for disk_name, disk_data in disks.items():
                    if not isinstance(disk_data, dict):
                        continue
                    dn = _str_label(disk_name)
                    for key, bucket in keys:
                        val = _as_float(disk_data.get(key))
                        if val is not None:
                            bucket[(dn,)] = val
            else:
                for key, bucket in keys:
                    val = _as_float(disks.get(key))
                    if val is not None:
                        bucket[("total",)] = val

        self._collector_event_series[metric_name(DISK_READ_BYTES_RATE)] = disk_read_bytes
        self._collector_event_series[metric_name(DISK_WRITE_BYTES_RATE)] = disk_write_bytes
        self._collector_event_series[metric_name(DISK_READ_OPS_RATE)] = disk_read_ops
        self._collector_event_series[metric_name(DISK_WRITE_OPS_RATE)] = disk_write_ops
        self._collector_event_series[metric_name(DISK_BUSY_PERCENT)] = disk_busy

        interfaces = payload.get("interfaces")
        network_rx: dict[tuple[str, ...], float] = {}
        network_tx: dict[tuple[str, ...], float] = {}
        interface_speed: dict[tuple[str, ...], float] = {}
        interface_link_up: dict[tuple[str, ...], float] = {}
        if isinstance(interfaces, dict):
            for iface_name, iface_data in interfaces.items():
                if not isinstance(iface_data, dict):
                    continue
                iface = _str_label(iface_name)
                rx = _as_float(iface_data.get("received_bytes_rate"))
                tx = _as_float(iface_data.get("sent_bytes_rate"))
                speed = _as_float(iface_data.get("speed"))
                link_up = _link_is_up(iface_data.get("link_state"))
                if rx is not None:
                    network_rx[(iface,)] = rx
                if tx is not None:
                    network_tx[(iface,)] = tx
                if speed is not None:
                    interface_speed[(iface,)] = speed
                if link_up is not None:
                    interface_link_up[(iface,)] = 1.0 if link_up else 0.0
        self._collector_event_series[metric_name(NETWORK_RX_BYTES_RATE)] = network_rx
        self._collector_event_series[metric_name(NETWORK_TX_BYTES_RATE)] = network_tx
        self._collector_event_series[metric_name(INTERFACE_REALTIME_SPEED_MBITS)] = interface_speed
        self._collector_event_series[metric_name(INTERFACE_REALTIME_LINK_UP)] = interface_link_up

        pools_rt = payload.get("pools")
        pool_read: dict[tuple[str, ...], float] = {}
        pool_write: dict[tuple[str, ...], float] = {}
        pool_used: dict[tuple[str, ...], float] = {}
        pool_available: dict[tuple[str, ...], float] = {}
        pool_total: dict[tuple[str, ...], float] = {}
        if isinstance(pools_rt, dict):
            for pool_name, pool_stats in pools_rt.items():
                if not isinstance(pool_stats, dict):
                    continue
                pn = _str_label(pool_name)
                read_bytes = _as_float(_first_not_none(pool_stats.get("read_bytes"), pool_stats.get("read_bytes_per_second")))
                write_bytes = _as_float(_first_not_none(pool_stats.get("write_bytes"), pool_stats.get("write_bytes_per_second")))
                used = _as_float(pool_stats.get("used"))
                available = _as_float(pool_stats.get("available"))
                total = _as_float(pool_stats.get("total"))
                if read_bytes is not None:
                    pool_read[(pn,)] = read_bytes
                if write_bytes is not None:
                    pool_write[(pn,)] = write_bytes
                if used is not None:
                    pool_used[(pn,)] = used
                if available is not None:
                    pool_available[(pn,)] = available
                if total is not None:
                    pool_total[(pn,)] = total

        self._collector_event_series[metric_name(POOL_REALTIME_READ_BYTES)] = pool_read
        self._collector_event_series[metric_name(POOL_REALTIME_WRITE_BYTES)] = pool_write
        self._collector_event_series[metric_name(POOL_REALTIME_USED_BYTES)] = pool_used
        self._collector_event_series[metric_name(POOL_REALTIME_AVAILABLE_BYTES)] = pool_available
        self._collector_event_series[metric_name(POOL_REALTIME_TOTAL_BYTES)] = pool_total

    def _dispatch_event(self, collection: str, payload: Any) -> None:
        # v25 virt.instance.metrics and v26 container.metrics are the same source
        # under different names; normalize to the canonical key so caching and
        # freshness use one identity regardless of TrueNAS version.
        if collection in INSTANCE_METRICS_WIRE_ALIASES:
            collection = INSTANCE_METRICS_EVENT
        now = time.time()
        self._collector_event_messages[collection] = now

        valid_payload = True
        if collection == "reporting.realtime":
            valid_payload = isinstance(payload, dict) and any(
                key in payload
                for key in ("cpu", "disls", "interfaces", "memory", "zfs", "pools")
            )
        elif collection == "app.stats":
            valid_payload = isinstance(payload, dict) and isinstance(
                payload.get("fields"), list
            )
        elif collection == INSTANCE_METRICS_EVENT:
            if not isinstance(payload, dict):
                valid_payload = False
            elif "fields" in payload:
                valid_payload = isinstance(payload.get("fields"), (dict, list))
            else:
                valid_payload = not payload or all(
                    isinstance(value, dict) for value in payload.values()
                )

        if collection in _EVENT_METRICS:
            self._clear_cached_event_metrics(collection)
        if not valid_payload:
            self._event_last_monotonic.pop(collection, None)
            self._expired_events.add(collection)
            self._clear_generic_event_metrics(collection)
            if not self._is_collector_mode():
                self._publish_cached_events_to_default_registry()
                self._publish_metric_snapshot_throttled()
            return

        if collection == "reporting.realtime":
            self._cache_realtime_event(payload)
        elif collection == "app.stats":
            self._cache_app_stats_event(payload)
        elif collection == INSTANCE_METRICS_EVENT:
            self._cache_virt_metrics_event(payload)

        self._event_last_monotonic[collection] = time.monotonic()
        self._expired_events.discard(collection)
        if not self._is_collector_mode():
            self._publish_cached_events_to_default_registry()
        if self.config.enable_generic_event_metrics and not self._is_collector_mode():
            self._replace_generic_event_metrics(collection, payload)
        if not self._is_collector_mode():
            self._publish_metric_snapshot_throttled()

    # ------------------------------------------------------------------
    # Event stream
    # ------------------------------------------------------------------

    def _event_stream_loop(self) -> None:
        backoff = 2
        while not self._stop_event.is_set():
            subscribed_events: dict[str, str] = {}
            try:
                with JsonRpcWsClient(
                    ws_url=self.config.ws_url,
                    timeout_seconds=min(
                        self.config.event_read_timeout_seconds,
                        self.config.event_stale_after_seconds,
                    ),
                    verify_tls=self.config.verify_tls,
                    ca_file=self.config.ca_file,
                ) as client:
                    self._bootstrap_connection(client)

                    for event in self.config.event_subscriptions:
                        if not self.compatibility_profile.allows_event(event):
                            with self._lock:
                                self._collector_event_stream_up[event] = 0.0
                            if event in self.compatibility_profile.removed_events:
                                self._collector_error(
                                    "profile_removed_event_suppressed",
                                    f"Suppressed removed event {event!r} for {self.compatibility_profile.name} profile",
                                    exc_info=False,
                                )
                                continue
                            self._collector_error(
                                "event_subscribe_blocked",
                                f"Blocked event {event!r} outside {self.compatibility_profile.name} profile",
                                exc_info=False,
                            )
                            continue
                        self._require_profile_method("core.subscribe")
                        subscribe_name = self._format_event_subscription(event)
                        try:
                            subscription_id = client.call("core.subscribe", [subscribe_name])
                            if not isinstance(subscription_id, str) or not subscription_id.strip():
                                raise RuntimeError(
                                    f"Invalid subscription id for {event}: {type(subscription_id).__name__}"
                                )
                            with self._lock:
                                self._collector_event_stream_up[event] = 1.0
                                if not self._is_collector_mode():
                                    self._publish_cached_events_to_default_registry()
                            subscribed_events[event] = subscription_id
                        except Exception:
                            with self._lock:
                                self._collector_event_stream_up[event] = 0.0
                                if not self._is_collector_mode():
                                    self._publish_cached_events_to_default_registry()
                            self._collector_error("event_subscribe", f"Failed subscribing to {event}")

                    if not subscribed_events:
                        raise RuntimeError("No event subscriptions succeeded")

                    backoff = 2  # reset backoff on successful connection
                    last_message_monotonic = time.monotonic()
                    connection_dead = False

                    try:
                        while not self._stop_event.is_set():
                            try:
                                msg = client.recv_json()
                            except WebSocketTimeoutException:
                                msg = None

                            if isinstance(msg, dict) and msg.get("method") == "collection_update":
                                # A genuine collection_update proves the connection is
                                # alive right now; reset before any deadline check.
                                last_message_monotonic = time.monotonic()
                            else:
                                # Evaluate the idle deadline on every recv_json() return
                                # that isn't a fresh collection_update, not just on socket
                                # timeout — a connection that keeps delivering other WS
                                # traffic (server notifications, non-subscription
                                # messages) would otherwise never trip the dead-connection
                                # check even with the subscription itself long dead.
                                idle_seconds = time.monotonic() - last_message_monotonic
                                if idle_seconds >= self.config.event_read_timeout_seconds:
                                    connection_dead = True
                                    raise RuntimeError(
                                        f"No event stream messages received for "
                                        f"{idle_seconds:.0f}s; assuming dead connection"
                                    ) from None
                                with self._lock:
                                    self._expire_stale_events()
                                continue

                            params = msg.get("params")
                            if not isinstance(params, dict):
                                continue
                            collection = _str_label(params.get("collection"), "unknown")
                            if collection not in subscribed_events:
                                continue
                            EVENT_MESSAGES_TOTAL.labels(event=collection).inc()
                            with self._diagnostic_lock:
                                self._event_message_counts[collection] = (
                                    self._event_message_counts.get(collection, 0.0) + 1.0
                                )
                            fields = params.get("fields")
                            payload = fields if isinstance(fields, dict) else params
                            # Acquire the scrape lock before updating Prometheus metrics so
                            # that a concurrent /metrics scrape sees a consistent snapshot
                            # (all CPU sub-components from the same event cycle, etc.).
                            with self._lock:
                                self._expire_stale_events()
                                self._dispatch_event(collection, payload)
                    finally:
                        # A connection judged dead by the idle-deadline check is not worth
                        # unsubscribing from — each core.unsubscribe call would block up to
                        # the socket timeout on a socket that is not going to answer, adding
                        # up to N x timeout of delay before reconnect. Still clear local
                        # state below so metrics reflect the teardown immediately.
                        if not connection_dead:
                            self._require_profile_method("core.unsubscribe")
                        for event, subscription_id in list(subscribed_events.items()):
                            if not connection_dead:
                                try:
                                    client.call("core.unsubscribe", [subscription_id])
                                except Exception:
                                    self._collector_error(
                                        "event_unsubscribe",
                                        f"Failed unsubscribing from {event}",
                                    )
                            with self._lock:
                                self._collector_event_stream_up[event] = 0.0
                                self._clear_cached_event_metrics(event)
                                self._clear_generic_event_metrics(event)
                                self._event_last_monotonic.pop(event, None)
                                self._expired_events.add(event)
                                if not self._is_collector_mode():
                                    self._publish_cached_events_to_default_registry()

            except Exception:
                if self._stop_event.is_set():
                    break
                self._collector_error("event_stream", "Event stream error")
                with self._lock:
                    self._expire_stale_events(force=True)
                    for event in self.config.event_subscriptions:
                        self._collector_event_stream_up[event] = 0.0
                    if not self._is_collector_mode():
                        self._publish_cached_events_to_default_registry()
                _log_exception_redacted(
                    LOG,
                    logging.WARNING,
                    "Event stream reconnecting in %ds",
                    self.config.ws_url,
                    backoff,
                )
                if self._stop_event.wait(backoff):
                    break
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

    def _export_host_metrics(self, info: Any, product_type_value: Any = None) -> None:
        if not isinstance(info, dict):
            return
        hostname = _str_label(info.get("hostname"), "unknown")
        version = _str_label(info.get("version"), "unknown")
        product_type = _str_label(product_type_value, "unknown")
        HOST_INFO.labels(hostname=hostname, version=version, product_type=product_type).set(1)

        uptime_seconds = _as_float(info.get("uptime_seconds"))
        if uptime_seconds is not None:
            HOST_UPTIME_SECONDS.set(uptime_seconds)

        physmem = _as_float(_first_not_none(info.get("physmem"), info.get("physical_memory")))
        if physmem is not None:
            HOST_PHYSICAL_MEMORY_BYTES.set(physmem)

        cpu_cores = _as_float(_first_not_none(info.get("cores"), info.get("cpu_cores")))
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
            _set_optional_bool_gauge(HOST_ECC_MEMORY, ecc)

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
        # Phase 2: graph discovery calls (reporting.netdata_graphs, reporting.graphs)
        # are only useful for generic method metric extraction.  Skip them entirely
        # when generic metrics are disabled to avoid two wasted API round-trips.
        if not self.config.enable_generic_method_metrics:
            return

        for graph_method in ("reporting.netdata_graphs", "reporting.graphs"):
            graph_result = self._safe_call_auto(client, graph_method)
            if graph_result is not None:
                cache[graph_method] = graph_result
                self._extract_generic_metrics(graph_method, graph_result, "result", 0)

    # ------------------------------------------------------------------
    # Filesystem metrics
    # ------------------------------------------------------------------

    def _collect_filesystem_metrics(self, client: JsonRpcWsClient) -> None:
        if not self.config.enable_generic_method_metrics:
            return
        selected_paths = self.config.filesystem_paths[: self.config.max_entity_calls]
        FILESYSTEM_PATH_COUNT.set(len(selected_paths))
        listdir_select = [
            "path", "type", "size", "allocation_size", "mode",
            "uid", "gid", "acl", "is_mountpoint", "is_ctldir",
            "attributes", "mount_id", "inode", "nlink",
        ]
        for path_index, fs_path in enumerate(selected_paths):
            path_tag = f"configured_slot_{path_index}"
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
        try:
            VM_COUNT.set(self._query_count(client, "vm.query"))
        except Exception:
            LOG.debug("vm.query count failed", exc_info=True)
        if self.config.enable_generic_method_metrics:
            vm_query = cache.get("vm.query") or self._safe_call_auto(client, "vm.query")
            vm_list = vm_query if isinstance(vm_query, list) else []
            for vm_index, vm in enumerate(vm_list[: self.config.max_entity_calls]):
                if not isinstance(vm, dict):
                    continue
                vm_id = vm.get("id")
                if not isinstance(vm_id, int):
                    continue
                for method in ("vm.get_memory_usage", "vm.get_vm_memory_info"):
                    try:
                        result = self._call(client, method, [vm_id])
                        self._extract_generic_metrics(
                            method, result, f"result.vm.configured_entity_{vm_index}", 0
                        )
                    except Exception:
                        continue

        app_query = cache.get("app.query") or self._safe_call_auto(client, "app.query")
        app_list = app_query if isinstance(app_query, list) else []
        try:
            APP_COUNT.set(
                self._count_or_len(client, "app.query", app_list, self.config.query_limit)
            )
        except Exception:
            LOG.debug("app.query count failed", exc_info=True)
        APP_STATE.clear()
        APP_UPGRADE_AVAILABLE.clear()
        APP_IMAGE_UPDATES_AVAILABLE.clear()
        APP_CUSTOM.clear()
        APP_MIGRATED.clear()
        APP_CONTAINER_COUNT.clear()
        APP_USED_PORT_COUNT.clear()
        APP_USED_HOST_IP_COUNT.clear()
        APP_CONTAINER_STATE_COUNT.clear()
        for app_index, app in enumerate(app_list[: self.config.max_entity_calls]):
            if not isinstance(app, dict):
                continue
            app_name = app.get("name")
            if not isinstance(app_name, str) or not app_name.strip():
                continue
            # Per-app state (e.g. RUNNING, STOPPED, DEPLOYING)
            app_st = self._response_field(app, "state")
            if isinstance(app_st, str) and app_st:
                APP_STATE.labels(app=app_name, state=app_st.upper()).set(1)

            for raw_value, gauge in (
                (self._response_field(app, "upgrade_available"), APP_UPGRADE_AVAILABLE),
                (
                    self._response_field(app, "image_updates_available"),
                    APP_IMAGE_UPDATES_AVAILABLE,
                ),
                (self._response_field(app, "custom_app"), APP_CUSTOM),
                (self._response_field(app, "migrated"), APP_MIGRATED),
            ):
                if raw_value is not None:
                    _set_optional_bool_gauge(gauge.labels(app=app_name), raw_value)

            active_workloads = self._response_field(app, "active_workloads")
            if isinstance(active_workloads, dict):
                container_count = _as_float(
                    self._response_field(active_workloads, "containers")
                )
                if container_count is not None:
                    APP_CONTAINER_COUNT.labels(app=app_name).set(container_count)

                used_ports = self._response_field(active_workloads, "used_ports")
                if isinstance(used_ports, list):
                    APP_USED_PORT_COUNT.labels(app=app_name).set(len(used_ports))

                used_host_ips = self._response_field(active_workloads, "used_host_ips")
                if isinstance(used_host_ips, list):
                    APP_USED_HOST_IP_COUNT.labels(app=app_name).set(len(used_host_ips))

                container_details = self._response_field(
                    active_workloads, "container_details"
                )
                if isinstance(container_details, list):
                    container_states: dict[str, int] = {}
                    for detail in container_details:
                        if not isinstance(detail, dict):
                            continue
                        state = detail.get("state")
                        if isinstance(state, str) and state:
                            normalized = state.upper()
                            container_states[normalized] = container_states.get(normalized, 0) + 1
                    for state, count in container_states.items():
                        APP_CONTAINER_STATE_COUNT.labels(app=app_name, state=state).set(count)

            if self.config.enable_generic_method_metrics:
                try:
                    result = self._call(client, "app.outdated_docker_images", [app_name])
                    self._extract_generic_metrics(
                        "app.outdated_docker_images",
                        result,
                        f"result.app.configured_entity_{app_index}",
                        0,
                    )
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

        _set_optional_bool_gauge(BOOT_POOL_HEALTHY, state.get("healthy"))

        status = state.get("status")
        BOOT_POOL_STATUS.clear()
        if isinstance(status, str) and status:
            BOOT_POOL_STATUS.labels(status=status.upper()).set(1)

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
            scan_state = _first_not_none(scan.get("state"), scan.get("function"))
            BOOT_POOL_SCAN_STATE.clear()
            if isinstance(scan_state, str) and scan_state:
                BOOT_POOL_SCAN_STATE.labels(state=scan_state.upper()).set(1)
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
                [], {"select": ["name", "until", "CSR"]}
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
            # The 25.10.2 query schema does not expose an issuer field. Keep the
            # legacy label set but do not mislabel subject data as the issuer.
            issuer = "unknown"

            days = _cert_days_to_expiry(cert.get("until"))
            if days is not None:
                CERT_DAYS_TO_EXPIRY.labels(name=name, issuer=issuer).set(days)
            expiry_ts = _parse_ts(cert.get("until"))
            if expiry_ts is not None:
                CERT_EXPIRY_TIMESTAMP_SECONDS.labels(name=name).set(expiry_ts)

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
                        "id",
                        ["used.parsed", "used"],
                        ["available.parsed", "available"],
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

        try:
            DATASET_COUNT.set(
                self._count_or_len(
                    client, "pool.dataset.query", datasets, self.config.max_datasets
                )
            )
        except Exception:
            LOG.debug("pool.dataset.query count failed", exc_info=True)
        # NOTE: DATASET_* gauges are already cleared at the top of scrape_once()
        # inside the lock. Do not clear them again here — doing so would be a
        # no-op at best and could create a race window if the lock is ever relaxed.

        for index, ds in enumerate(datasets):
            if not isinstance(ds, dict):
                continue
            raw_name = _first_not_none(ds.get("id"), ds.get("name"))
            if not isinstance(raw_name, str) or not raw_name:
                continue
            name = raw_name

            for gauge, field in (
                (DATASET_USED_BYTES, "used"),
                (DATASET_AVAILABLE_BYTES, "available"),
                (DATASET_RESERVATION_BYTES, "reservation"),
                (DATASET_REFRESERVATION_BYTES, "refreservation"),
                (DATASET_USED_BY_CHILDREN_BYTES, "usedbychildren"),
                (DATASET_USED_BY_DATASET_BYTES, "usedbydataset"),
                (DATASET_USED_BY_SNAPSHOTS_BYTES, "usedbysnapshots"),
            ):
                val = _as_float(self._response_field(ds, field))
                if val is not None:
                    gauge.labels(dataset=name).set(val)

            # quota / refquota: 0 means no quota set; expose raw value
            for gauge, field in (
                (DATASET_QUOTA_BYTES, "quota"),
                (DATASET_REFQUOTA_BYTES, "refquota"),
            ):
                val = _as_float(self._response_field(ds, field))
                if val is not None:
                    gauge.labels(dataset=name).set(val)

            snap_count = _as_float(self._response_field(ds, "snapshot_count"))
            fallback_limit = self.config.dataset_snapshot_fallback_limit
            if snap_count is None and fallback_limit > 0 and index < min(fallback_limit, self.config.max_entity_calls):
                try:
                    snap_count = _as_float(self._call(client, "pool.dataset.snapshot_count", [name]))
                except Exception:
                    LOG.debug("pool.dataset.snapshot_count failed for %s", name, exc_info=True)
            if snap_count is not None:
                DATASET_SNAPSHOT_COUNT.labels(dataset=name).set(snap_count)

            ratio_raw = self._response_field(ds, "compressratio")
            ratio = _as_ratio(ratio_raw)
            if ratio is not None:
                DATASET_COMPRESSION_RATIO.labels(dataset=name).set(ratio)

            for raw_value, gauge in (
                (self._response_field(ds, "readonly"), DATASET_READONLY),
                (self._response_field(ds, "atime"), DATASET_ATIME),
                (self._response_field(ds, "exec"), DATASET_EXEC),
                (self._response_field(ds, "key_loaded"), DATASET_KEY_LOADED),
                (self._response_field(ds, "locked"), DATASET_LOCKED),
            ):
                if raw_value is not None:
                    _set_optional_bool_gauge(gauge.labels(dataset=name), raw_value)

            for gauge, field in (
                (DATASET_QUOTA_WARNING_PERCENT, "quota_warning"),
                (DATASET_QUOTA_CRITICAL_PERCENT, "quota_critical"),
                (DATASET_REFQUOTA_WARNING_PERCENT, "refquota_warning"),
                (DATASET_REFQUOTA_CRITICAL_PERCENT, "refquota_critical"),
            ):
                val = _as_percent(self._response_field(ds, field))
                if val is not None:
                    gauge.labels(dataset=name).set(val)

            encrypted = self._response_field(ds, "encrypted")
            if encrypted is not None:
                _set_optional_bool_gauge(DATASET_ENCRYPTED.labels(dataset=name), encrypted)

            creation_ts = _parse_ts(self._response_field(ds, "creation"))
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
        *,
        fallback_name_field: str | None = None,
        outcome_field: str | None = None,
        outcome_ts_field: str | None = None,
        total_count: int | None = None,
    ) -> None:
        """Export documented task identity and enablement fields."""
        TASK_COUNT.labels(task_type=task_type).set(total_count if total_count is not None else len(tasks))
        for task in tasks[: self.config.max_entity_calls]:
            if not isinstance(task, dict):
                continue
            raw_name = task.get(name_field)
            if not isinstance(raw_name, (str, int)) and fallback_name_field is not None:
                raw_name = task.get(fallback_name_field)
            if not isinstance(raw_name, (str, int)):
                continue
            name = str(raw_name)
            _set_optional_bool_gauge(
                TASK_ENABLED.labels(task_type=task_type, name=name),
                task.get(enabled_field),
            )
            if outcome_field is None:
                continue
            self._export_task_outcome(task_type, name, task.get(outcome_field), outcome_ts_field)

    def _normalize_task_state(self, value: Any) -> str | None:
        raw = value.get("state") if isinstance(value, dict) else value
        if raw is None:
            return None
        state = _str_label(raw, "").upper()
        if not state:
            return None
        if state in {
            "PENDING",
            "RUNNING",
            "SUCCESS",
            "FINISHED",
            "ERROR",
            "FAILED",
            "WAITING",
            "ABORTED",
            "HOLD",
            "UNKNOWN",
        }:
            return state
        return "UNKNOWN"

    def _export_task_outcome(
        self,
        task_type: str,
        name: str,
        outcome: Any,
        timestamp_field: str | None,
    ) -> None:
        if not isinstance(outcome, dict):
            return
        state = self._normalize_task_state(outcome)
        if state is not None:
            TASK_STATE.labels(task_type=task_type, name=name, state=state).set(1)
        if timestamp_field is None:
            return
        ts = _parse_ts(outcome.get(timestamp_field))
        if ts is not None:
            TASK_LAST_RUN_TS.labels(task_type=task_type, name=name).set(ts)

    def _collect_task_metrics(self, client: JsonRpcWsClient) -> None:
        if not self.config.enable_task_metrics:
            return

        # Phase 2: each task type uses a single list query; count is derived
        # from len(items) to avoid a separate _query_count round-trip.

        # Replication tasks
        try:
            items = self._call(client, "replication.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["id", "name", "enabled", "state"]}
            ])
            if isinstance(items, list):
                total = self._count_or_len(
                    client, "replication.query", items, self.config.query_limit
                )
                self._export_task_list(
                    "replication",
                    items,
                    "name",
                    "enabled",
                    fallback_name_field="id",
                    outcome_field="state",
                    outcome_ts_field="datetime",
                    total_count=total,
                )
        except Exception:
            LOG.debug("replication.query failed", exc_info=True)

        # Cloud sync tasks
        try:
            items = self._call(client, "cloudsync.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["id", "description", "enabled", "job"]}
            ])
            if isinstance(items, list):
                total = self._count_or_len(
                    client, "cloudsync.query", items, self.config.query_limit
                )
                self._export_task_list(
                    "cloudsync",
                    items,
                    "description",
                    "enabled",
                    fallback_name_field="id",
                    outcome_field="job",
                    outcome_ts_field="time_finished",
                    total_count=total,
                )
        except Exception:
            LOG.debug("cloudsync.query failed", exc_info=True)

        # Rsync tasks
        try:
            items = self._call(client, "rsynctask.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["id", "enabled", "job"]}
            ])
            if isinstance(items, list):
                total = self._count_or_len(
                    client, "rsynctask.query", items, self.config.query_limit
                )
                self._export_task_list(
                    "rsynctask",
                    items,
                    "id",
                    "enabled",
                    outcome_field="job",
                    outcome_ts_field="time_finished",
                    total_count=total,
                )
        except Exception:
            LOG.debug("rsynctask.query failed", exc_info=True)

        # Snapshot tasks — state is stored directly, no job object
        try:
            items = self._call(client, "pool.snapshottask.query", [
                [], {"limit": self.config.query_limit,
                     "select": ["id", "enabled", "state"]}
            ])
            if isinstance(items, list):
                total = self._count_or_len(
                    client, "pool.snapshottask.query", items, self.config.query_limit
                )
                self._export_task_list(
                    "snapshottask",
                    items,
                    "id",
                    "enabled",
                    outcome_field="state",
                    outcome_ts_field="datetime",
                    total_count=total,
                )
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
        result = None
        try:
            result = cache.get("directoryservices.status") or self._call(client, "directoryservices.status", [])
        except Exception:
            LOG.debug("directoryservices.status failed", exc_info=True)

        if isinstance(result, dict):
            DIRECTORYSERVICES_STATUS.clear()
            DIRECTORYSERVICES_HEALTHY.clear()
            DIRECTORYSERVICES_FAULT_REASON.clear()
            service_type = result.get("type")
            raw_status = result.get("status")
            if service_type is None and raw_status is None:
                service = "none"
                status = "DISABLED"
            elif isinstance(service_type, str) and isinstance(raw_status, str):
                service = _str_label(service_type).lower()
                status = _str_label(raw_status).upper()
            else:
                return
            faulted = status == "FAULTED"

            DIRECTORYSERVICES_STATUS.labels(service=service, status=status).set(1)
            DIRECTORYSERVICES_HEALTHY.labels(service=service).set(1 if status == "HEALTHY" else 0)
            DIRECTORYSERVICES_FAULT_PRESENT.labels(service=service).set(1 if faulted else 0)
            DIRECTORYSERVICES_CONFIG_ENABLED.set(1 if service_type is not None else 0)
            if service_type is not None:
                DIRECTORYSERVICES_SERVICE_TYPE.labels(
                    service_type=_str_label(service_type, "unknown").upper()
                ).set(1)
            if faulted:
                # status_msg can contain administrator/domain data. Preserve the
                # legacy label contract without exporting the message itself.
                DIRECTORYSERVICES_FAULT_REASON.labels(
                    service=service, reason="redacted"
                ).set(1)

        # directoryservices.config contains bind credentials in this API version
        # and cannot be field-selected. Its legacy config-detail metrics therefore
        # remain NaN instead of fetching a secret-bearing response.

    # ------------------------------------------------------------------
    # IPMI metrics (NEW)
    # ------------------------------------------------------------------

    def _collect_ipmi_metrics(self, client: JsonRpcWsClient) -> None:
        if not self.config.enable_ipmi_metrics:
            return

        try:
            loaded = self._call(client, "ipmi.is_loaded", [])
        except Exception:
            LOG.debug("ipmi.is_loaded failed", exc_info=True)
            return

        ipmi_available = _as_optional_bool(loaded)
        if ipmi_available is None:
            return
        IPMI_LOADED.set(1 if ipmi_available else 0)
        if not ipmi_available:
            return

        # Chassis info
        try:
            chassis = self._call(client, "ipmi.chassis.info", [{}])
            if isinstance(chassis, dict):
                power = chassis.get("system_power")
                if power is not None:
                    _set_optional_bool_gauge(IPMI_CHASSIS_POWER_ON, power)

                # Extended chassis fields (v4)
                power_overload = chassis.get("power_overload")
                if power_overload is not None:
                    _set_optional_bool_gauge(IPMI_CHASSIS_POWER_OVERLOAD, power_overload)

                chassis_intrusion = chassis.get("chassis_intrusion")
                if chassis_intrusion is not None:
                    _set_optional_bool_gauge(IPMI_CHASSIS_INTRUSION, chassis_intrusion)

                drive_fault = chassis.get("drive_fault")
                if drive_fault is not None:
                    _set_optional_bool_gauge(IPMI_CHASSIS_DRIVE_FAULT, drive_fault)

                fan_fault = chassis.get("cooling/fan_fault")
                if fan_fault is not None:
                    _set_optional_bool_gauge(IPMI_CHASSIS_FAN_FAULT, fan_fault)

                if self.config.enable_generic_method_metrics:
                    self._extract_generic_metrics("ipmi.chassis.info", chassis, "result", 0)
        except Exception:
            LOG.debug("ipmi.chassis.info failed", exc_info=True)

        # System Event Log summary
        try:
            sel_info = self._call(client, "ipmi.sel.info", [])
            if isinstance(sel_info, dict):
                entries = _as_float(sel_info.get("number_of_log_entries"))
                if entries is not None:
                    IPMI_SEL_ENTRY_COUNT.set(entries)
                free_space = _as_size_bytes(sel_info.get("free_space_remaining"))
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
        """Populate SMB session/connection/open-file counts from smb.status (v26+).

        smb.status returns per-session records that include usernames and client
        IP addresses. Only the *count* of each list is recorded — no session
        field is ever turned into a metric label, so no PII reaches the metrics.
        On 25.10 smb.status was undocumented, so these gauges stay NaN there.
        """
        if not self.compatibility_profile.allows_method("smb.status"):
            return
        # The info_level literals are unverified in the current API docs corpus;
        # live systems validate these names.
        for info_level, gauge in (
            ("SESSIONS", SMB_SESSION_COUNT),
            ("SHARES", SMB_CONNECTION_COUNT),
            ("LOCKS", SMB_OPEN_FILE_COUNT),
        ):
            try:
                result = self._call(client, "smb.status", [info_level])
                if isinstance(result, list):
                    gauge.set(len(result))
            except Exception:
                LOG.debug("smb.status %s failed", info_level, exc_info=True)

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
                model = _str_label(gpu.get("description"), "unknown")
                vendor = _str_label(gpu.get("vendor"), "unknown")
                devices = gpu.get("devices")
                first_device = devices[0] if isinstance(devices, list) and devices else None
                pci_id = _str_label(
                    first_device.get("pci_id") if isinstance(first_device, dict) else None,
                    "unknown",
                )
                GPU_INFO.labels(
                    index=str(idx),
                    model=model,
                    vendor=vendor,
                    pci_id=pci_id,
                ).set(1)
                available_to_host = _as_optional_bool(gpu.get("available_to_host"))
                if available_to_host is not None:
                    GPU_AVAILABLE_TO_HOST.labels(index=str(idx)).set(
                        1 if available_to_host else 0
                    )
                uses_critical_devices = _as_optional_bool(
                    gpu.get("uses_system_critical_devices")
                )
                if uses_critical_devices is not None:
                    GPU_USES_CRITICAL_DEVICES.labels(index=str(idx)).set(
                        1 if uses_critical_devices else 0
                    )
        except Exception:
            LOG.debug("device.get_info GPU failed", exc_info=True)

    # ------------------------------------------------------------------
    # JBOF hardware (v3)
    # ------------------------------------------------------------------

    def _collect_jbof_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect JBOF (Just a Bunch of Flash) enclosure count."""
        try:
            JBOF_COUNT.set(self._query_count(client, "jbof.query"))
        except Exception:
            LOG.debug("jbof.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # Active API session count (v3)
    # ------------------------------------------------------------------

    def _collect_auth_session_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect number of active authenticated sessions via auth.sessions."""
        try:
            AUTH_SESSIONS_ACTIVE.set(self._query_count(client, "auth.sessions"))
        except Exception:
            LOG.debug("auth.sessions failed", exc_info=True)

    # ------------------------------------------------------------------
    # Extended disk info (rotational, SMART) (v3)
    # ------------------------------------------------------------------

    def _collect_disk_extended_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect disk rotational flag and SMART status via disk.query.

        v25.10.2 field names:
          rotationrate  — RPM, nullable for SSDs and devices without rotation data
          type          — documented disk media type used when rotationrate is null
          togglesmart   — not present in v25.10.2; SMART enabled status is omitted
        """
        try:
            disks = cache.get("disk.query")
            if disks is None:
                disks = self._call_query_with_fallback(
                    client, "disk.query",
                    {
                        "extra": {"pools": True},
                        "select": [
                            "name",
                            "identifier",
                            "size",
                            "pool",
                            "type",
                            "rotationrate",
                            "model",
                            "bus",
                        ],
                    },
                    allow_bare_fallback=False,
                )
                cache["disk.query"] = disks
            if not isinstance(disks, list):
                return
            DISK_INFO.clear()
            for disk in disks:
                if not isinstance(disk, dict):
                    continue
                dn = _str_label(disk.get("name") or disk.get("identifier"), "unknown")
                rotationrate = _as_float(disk.get("rotationrate"))
                disk_type = _str_label(disk.get("type"), "").upper()
                if rotationrate is not None:
                    DISK_ROTATIONAL.labels(disk=dn).set(1 if rotationrate > 0 else 0)
                elif disk_type in {"SSD", "NVME"}:
                    DISK_ROTATIONAL.labels(disk=dn).set(0)
                elif disk_type in {"HDD"}:
                    DISK_ROTATIONAL.labels(disk=dn).set(1)
                # Info-style metric for disk identity
                model = _str_label(disk.get("model"), "")
                bus = _str_label(disk.get("bus"), "")
                DISK_INFO.labels(disk=dn, model=model, serial="redacted", bus=bus).set(1)
        except Exception:
            LOG.debug("disk.query extended failed", exc_info=True)

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
    # API key inventory
    # ------------------------------------------------------------------

    def _collect_api_key_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect bounded API key inventory without fetching key material."""
        try:
            keys = self._call(
                client,
                "api_key.query",
                [
                    [],
                    {
                        "limit": self.config.query_limit,
                        "select": ["id", "name", "expires_at", "revoked"],
                    },
                ],
            )
        except Exception:
            LOG.debug("api_key.query failed", exc_info=True)
            return

        if not isinstance(keys, list):
            return

        API_KEY_EXPIRY_TS.clear()
        try:
            API_KEY_COUNT.set(
                self._count_or_len(client, "api_key.query", keys, self.config.query_limit)
            )
        except Exception:
            LOG.debug("api_key.query count failed", exc_info=True)

        for key in keys[: self.config.max_entity_calls]:
            if not isinstance(key, dict):
                continue
            raw_name = key.get("name")
            if not isinstance(raw_name, str) or not raw_name:
                continue
            expires_at = _parse_ts(key.get("expires_at"))
            if expires_at is not None:
                API_KEY_EXPIRY_TS.labels(name=raw_name).set(expires_at)

        try:
            API_KEY_REVOKED_COUNT.set(
                self._query_count(client, "api_key.query", [["revoked", "=", True]])
            )
        except Exception:
            LOG.debug("api_key.query revoked count failed", exc_info=True)

    # ------------------------------------------------------------------
    # v26 zpool status details
    # ------------------------------------------------------------------

    def _collect_zpool_status_metrics(self, client: JsonRpcWsClient) -> None:
        """Collect v26-only zpool status_code values when the active profile allows it."""
        if not self.compatibility_profile.allows_method("zpool.query"):
            return
        try:
            zpools = self._call(client, "zpool.query", [{}])
        except Exception:
            LOG.debug("zpool.query failed", exc_info=True)
            return

        if not isinstance(zpools, list):
            return

        POOL_STATUS_CODE.clear()
        for pool in zpools[: self.config.max_entity_calls]:
            if not isinstance(pool, dict):
                continue
            raw_pool_name = pool.get("name")
            raw_status_code = pool.get("status_code")
            if not isinstance(raw_pool_name, str) or not raw_pool_name:
                continue
            if not isinstance(raw_status_code, str) or not raw_status_code:
                continue
            POOL_STATUS_CODE.labels(
                pool=raw_pool_name,
                status_code=raw_status_code.upper(),
            ).set(1)

    # ------------------------------------------------------------------
    # System extra metrics (reboot, gateway, identity, HA) (NEW)
    # ------------------------------------------------------------------

    def _collect_failover_reboot_info(self, client: JsonRpcWsClient) -> None:
        try:
            reboot_info = self._call(client, "failover.reboot.info", [])
        except Exception:
            LOG.debug("failover.reboot.info failed", exc_info=True)
            return

        if not isinstance(reboot_info, dict):
            return

        FAILOVER_NODE_REBOOT_REQUIRED.clear()
        for node_label, field in (
            ("this_node", "this_node"),
            ("other_node", "other_node"),
        ):
            node_info = reboot_info.get(field)
            if not isinstance(node_info, dict):
                continue
            reasons = node_info.get("reboot_required_reasons")
            if isinstance(reasons, list):
                FAILOVER_NODE_REBOOT_REQUIRED.labels(node=node_label).set(
                    1 if reasons else 0
                )

    def _collect_system_extra_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        # Pending reboot
        try:
            reboot_info = cache.get("system.reboot.info") or self._call(client, "system.reboot.info", [])
            if isinstance(reboot_info, dict):
                reasons = reboot_info.get("reboot_required_reasons")
                SYSTEM_REBOOT_REASON.clear()
                if isinstance(reasons, list):
                    codes = [
                        reason["code"].upper()
                        for reason in reasons
                        if isinstance(reason, dict)
                        and isinstance(reason.get("code"), str)
                        and reason["code"]
                    ]
                    if not reasons:
                        SYSTEM_REBOOT_REQUIRED.set(0)
                    elif codes:
                        SYSTEM_REBOOT_REQUIRED.set(1)
                        for code in codes:
                            SYSTEM_REBOOT_REASON.labels(reason=code).set(1)
        except Exception:
            LOG.debug("system.reboot.info failed", exc_info=True)

        # route presence does not prove reachability. Keep the old metric as a
        # compatibility alias and publish the correctly named replacement.
        try:
            routes = self._safe_call_auto(client, "route.system_routes")
            if isinstance(routes, list):
                has_default_gw = any(
                    isinstance(r, dict)
                    and r.get("network")
                    in ("default", "0.0.0.0", "0.0.0.0/0", "::", "::/0")
                    for r in routes
                )
                NETWORK_GATEWAY_REACHABLE.set(1 if has_default_gw else 0)
                NETWORK_DEFAULT_GATEWAY_CONFIGURED.set(1 if has_default_gw else 0)
        except Exception:
            LOG.debug("gateway reachability inference failed", exc_info=True)

        # TrueNAS identity flags
        try:
            is_production = cache.get("truenas.is_production")
            if is_production is None:
                is_production = self._call(client, "truenas.is_production", [])
            if is_production is not None:
                _set_optional_bool_gauge(TRUENAS_IS_PRODUCTION, is_production)
        except Exception:
            LOG.debug("truenas.is_production failed", exc_info=True)

        try:
            is_ix = cache.get("truenas.is_ix_hardware")
            if is_ix is None:
                is_ix = self._call(client, "truenas.is_ix_hardware", [])
            if is_ix is not None:
                _set_optional_bool_gauge(TRUENAS_IS_IX_HARDWARE, is_ix)
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
                    if isinstance(reason, str) and reason:
                        FAILOVER_DISABLED_REASON.labels(reason=reason).set(1)
        except Exception:
            LOG.debug("failover.disabled.reasons failed", exc_info=True)

        self._collect_failover_reboot_info(client)

    # ------------------------------------------------------------------
    # Main scrape
    # ------------------------------------------------------------------

    def _discover_all_methods(self, client: JsonRpcWsClient) -> None:
        """Dynamically query core.get_methods and add query/config endpoints to extra_methods."""
        if not self.config.scrape_all_metrics or self._all_methods_discovered:
            return

        try:
            methods = self._call(client, "core.get_methods", [])
            names = sorted(list(methods.keys()))
            added_count = 0

            # Methods we already scrape or that require special handling
            skip_set = set(BASE_METHODS) | set(REQUIRES_ENTITY_PARAM)
            extra_method_set = set(self.config.extra_methods)

            for m in names:
                if m in skip_set:
                    continue
                if self._is_safe_read_method(m) and m not in extra_method_set:
                    self.config.extra_methods.append(m)
                    extra_method_set.add(m)
                    added_count += 1

            if added_count > 0:
                LOG.info("Dynamically discovered %d additional API methods to scrape (total extra: %d)",
                         added_count, len(self.config.extra_methods))
            
            self._all_methods_discovered = True

        except Exception:
            _log_exception_redacted(
                LOG,
                logging.WARNING,
                "Dynamic method discovery failed",
                self.config.ws_url,
            )

    def scrape_once(self) -> None:
        LAST_SCRAPE_TS.set(time.time())
        self._last_scrape_attempt_monotonic = time.monotonic()
        success = False
        reset_done = False
        deadline = time.monotonic() + self.config.scrape_budget_seconds

        with self._lock:
            # SCRAPE_DURATION is measured strictly inside the lock so it reflects
            # real API time, not any lock-wait from a concurrent caller.
            started = time.time()

            try:
                with JsonRpcWsClient(
                    ws_url=self.config.ws_url,
                    timeout_seconds=self.config.timeout_seconds,
                    verify_tls=self.config.verify_tls,
                    ca_file=self.config.ca_file,
                    deadline_monotonic=deadline,
                ) as client:
                    # --- Authentication and compatibility profile detection ---
                    version_short = self._bootstrap_connection(client)
                    if version_short is None:
                        raise RuntimeError("version detection failed")
                    self._reset_poll_cycle_metrics()
                    reset_done = True

                    # --- Dynamic Discovery (if enabled) ---
                    if self.config.enable_generic_method_metrics:
                        self._discover_all_methods(client)

                    # --- Method discovery & generic extraction ---
                    # result_cache stores every method result from the generic loop.
                    # Dedicated collectors below can read from cache to avoid making
                    # a second round-trip for the same method.
                    result_cache: dict[str, Any] = {}
                    result_cache["system.version_short"] = version_short
                    methods_to_call = (
                        self._discover_methods(client)
                        if self.config.enable_generic_method_metrics
                        else []
                    )
                    self._collect_reporting_timeseries(client, result_cache)
                    self._collect_filesystem_metrics(client)

                    for method in methods_to_call:
                        result = self._safe_call_auto(client, method)
                        if result is not None:
                            result_cache[method] = result
                            if self.config.enable_generic_method_metrics:
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
                    self._collect_api_key_metrics(client)
                    self._collect_system_extra_metrics(client, result_cache)
                    # v3 additions
                    self._collect_smb_nfs_sessions(client)
                    self._collect_gpu_metrics(client)
                    self._collect_jbof_metrics(client)
                    self._collect_auth_session_metrics(client)
                    self._collect_disk_extended_metrics(client, result_cache)
                    # Legacy SMART test-result gauges intentionally remain unavailable:
                    # 25.10.2 exposes no documented safe RPC for that source.

                    # --- System state (use cache if already fetched) ---
                    state_raw = result_cache.get("system.state")
                    if state_raw is None:
                        state_raw = self._call(client, "system.state", [])
                    if isinstance(state_raw, str) and state_raw:
                        SYSTEM_STATE.labels(state=state_raw.upper()).set(1)
                    ready_raw = result_cache.get("system.ready")
                    if ready_raw is None:
                        ready_raw = self._call(client, "system.ready", [])
                    _set_optional_bool_gauge(SYSTEM_READY, ready_raw)

                    # --- Host info (use cache if already fetched) ---
                    info = result_cache.get("system.info")
                    if info is None:
                        info = self._call(client, "system.info", [])
                    product_type = result_cache.get("system.product_type")
                    if product_type is None:
                        product_type = self._call(client, "system.product_type", [])
                        result_cache["system.product_type"] = product_type
                    self._export_host_metrics(info, product_type)

                    # --- VM memory (use cache) ---
                    vm_available = result_cache.get("vm.get_available_memory")
                    if vm_available is None:
                        vm_available = self._call(client, "vm.get_available_memory", [False])
                    vm_av_val = self._profile_normalized_bytes(
                        "vm.get_available_memory", vm_available
                    )
                    if vm_av_val is not None:
                        VM_AVAILABLE_MEMORY_BYTES.set(vm_av_val)

                    vm_vmemory = result_cache.get("vm.get_vmemory_in_use")
                    if vm_vmemory is None:
                        vm_vmemory = self._safe_call_auto(client, "vm.get_vmemory_in_use")
                    if isinstance(vm_vmemory, dict):
                        for state_name in ("RNP", "PRD", "RPRD"):
                            state_value = vm_vmemory.get(state_name)
                            numeric = self._profile_normalized_bytes(
                                "vm.get_vmemory_in_use", state_value
                            )
                            if numeric is not None:
                                VM_VMEMORY_IN_USE_BYTES.labels(
                                    state=state_name
                                ).set(numeric)

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

                    try:
                        DOCKER_NETWORK_COUNT.set(
                            self._query_count(client, "docker.network.query")
                        )
                    except Exception:
                        LOG.debug("docker.network.query failed", exc_info=True)

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
                        NFS_V3_CLIENT_COUNT.set(
                            self._query_count(client, "nfs.get_nfs3_clients")
                        )
                    except Exception:
                        LOG.debug("nfs.get_nfs3_clients failed", exc_info=True)

                    try:
                        NFS_V4_CLIENT_COUNT.set(
                            self._query_count(client, "nfs.get_nfs4_clients")
                        )
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
                        {
                            "select": [
                                "name",
                                "healthy",
                                "warning",
                                "status",
                                "size",
                                "allocated",
                                "free",
                                "scan",
                                "fragmentation",
                                "autotrim",
                                "dedup_table_size",
                                "expand",
                                "topology",
                            ]
                        },
                    )
                    pool_list = pools if isinstance(pools, list) else []
                    POOL_COUNT.set(len(pool_list))
                    for pool in pool_list:
                        if not isinstance(pool, dict):
                            continue
                        raw_pool_name = pool.get("name")
                        if not isinstance(raw_pool_name, str) or not raw_pool_name:
                            continue
                        pool_name = raw_pool_name
                        _set_optional_bool_gauge(
                            POOL_HEALTHY.labels(pool=pool_name), pool.get("healthy")
                        )
                        _set_optional_bool_gauge(
                            POOL_WARNING.labels(pool=pool_name), pool.get("warning")
                        )
                        pool_status = pool.get("status")
                        if isinstance(pool_status, str) and pool_status:
                            POOL_STATUS.labels(
                                pool=pool_name, status=pool_status.upper()
                            ).set(1)
                        for gauge, field in (
                            (POOL_SIZE_BYTES, "size"),
                            (POOL_ALLOCATED_BYTES, "allocated"),
                            (POOL_FREE_BYTES, "free"),
                        ):
                            val = _as_float(self._response_field(pool, field))
                            if val is not None:
                                gauge.labels(pool=pool_name).set(val)

                        frag = _as_percent(self._response_field(pool, "fragmentation"))
                        if frag is not None:
                            POOL_FRAGMENTATION.labels(pool=pool_name).set(frag)

                        # Autotrim (v5 addition)
                        autotrim = pool.get("autotrim")
                        if isinstance(autotrim, dict):
                            _set_optional_bool_gauge(
                                POOL_AUTOTRIM_ENABLED.labels(pool=pool_name),
                                autotrim.get("value"),
                            )
                        elif autotrim is not None:
                            _set_optional_bool_gauge(
                                POOL_AUTOTRIM_ENABLED.labels(pool=pool_name), autotrim
                            )

                        dedup = _as_float(
                            self._response_field(pool, "dedup_table_size", "dedup_table_quota")
                        )
                        if dedup is not None:
                            POOL_DEDUP_TABLE_SIZE_BYTES.labels(pool=pool_name).set(dedup)

                        expand = pool.get("expand")
                        if isinstance(expand, dict):
                            reflowed = _as_float(
                                self._response_field(expand, "bytes_reflowed", "reflowed")
                            )
                            total = _as_float(
                                self._response_field(expand, "bytes_to_reflow", "to_reflow")
                            )
                            percent = _as_percent(self._response_field(expand, "percentage"))
                            if reflowed is not None:
                                POOL_EXPAND_REFLOWED_BYTES.labels(pool=pool_name).set(reflowed)
                            if total is not None:
                                POOL_EXPAND_TO_REFLOW_BYTES.labels(pool=pool_name).set(total)
                                POOL_EXPAND_SIZE_BYTES.labels(pool=pool_name).set(total)
                            if percent is not None:
                                POOL_EXPAND_PERCENT.labels(pool=pool_name).set(percent)

                        scan = pool.get("scan")
                        if isinstance(scan, dict):
                            pct = _as_float(self._response_field(scan, "percentage", "percent"))
                            if pct is not None:
                                POOL_SCAN_PERCENT.labels(pool=pool_name).set(pct)
                            # Detailed scan stats (v3 addition)
                            errors = _as_float(self._response_field(scan, "errors"))
                            if errors is not None:
                                POOL_SCAN_ERRORS.labels(pool=pool_name).set(errors)
                            bytes_proc = _as_float(
                                self._response_field(scan, "bytes_processed", "processed_bytes")
                            )
                            if bytes_proc is not None:
                                POOL_SCAN_BYTES_PROCESSED.labels(pool=pool_name).set(bytes_proc)
                            bytes_tot = _as_float(
                                self._response_field(scan, "bytes_to_process", "total_bytes")
                            )
                            if bytes_tot is not None:
                                POOL_SCAN_BYTES_TOTAL.labels(pool=pool_name).set(bytes_tot)
                            secs_remaining = _as_float(
                                self._response_field(scan, "total_secs_left", "seconds_remaining")
                            )
                            if secs_remaining is not None:
                                POOL_SCAN_SECONDS_REMAINING.labels(pool=pool_name).set(secs_remaining)
                            end_ts = scan.get("end_time")
                            if end_ts is not None:
                                ts = _parse_ts(end_ts)
                                if ts is not None:
                                    POOL_LAST_SCAN_TS.labels(pool=pool_name).set(ts)

                        topology = pool.get("topology")
                        if isinstance(topology, dict):
                            self._extract_vdev_errors(pool_name, topology)

                    self._collect_zpool_status_metrics(client)

                    # --- Disks ---
                    disks = result_cache.get("disk.query")
                    if disks is None:
                        disks = self._call_query_with_fallback(
                            client, "disk.query",
                            {
                                "extra": {"pools": True},
                                "select": [
                                    "name",
                                    "identifier",
                                    "size",
                                    "pool",
                                    "type",
                                    "rotationrate",
                                    "model",
                                    "bus",
                                ],
                            },
                            allow_bare_fallback=False,
                        )
                        result_cache["disk.query"] = disks
                    disk_list = disks if isinstance(disks, list) else []
                    DISK_COUNT.set(len(disk_list))
                    disk_names: list[str] = []
                    for disk in disk_list:
                        if not isinstance(disk, dict):
                            continue
                        raw_disk_name = _first_not_none(
                            disk.get("name"), disk.get("identifier")
                        )
                        if not isinstance(raw_disk_name, str) or not raw_disk_name:
                            continue
                        disk_name = raw_disk_name
                        disk_names.append(disk_name)
                        DISK_IN_USE.labels(disk=disk_name).set(
                            1 if disk.get("pool") is not None else 0
                        )
                        size = _as_float(disk.get("size"))
                        if size is not None:
                            DISK_SIZE_BYTES.labels(disk=disk_name).set(size)

                    if disk_names:
                        self._collect_disk_temperature_agg(client, disk_names)
                        try:
                            temp_alerts = self._call(
                                client, "disk.temperature_alerts", [disk_names]
                            )
                            if isinstance(temp_alerts, list):
                                alert_counts = dict.fromkeys(disk_names, 0)
                                for alert in temp_alerts:
                                    if not isinstance(alert, dict):
                                        continue
                                    raw_alert_disk = _first_not_none(
                                        alert.get("disk"),
                                        alert.get("device"),
                                        alert.get("name"),
                                    )
                                    args = alert.get("args")
                                    if isinstance(args, dict):
                                        raw_alert_disk = _first_not_none(
                                            raw_alert_disk,
                                            args.get("disk"),
                                            args.get("device"),
                                            args.get("name"),
                                        )
                                    if (
                                        isinstance(raw_alert_disk, str)
                                        and raw_alert_disk in alert_counts
                                    ):
                                        alert_counts[raw_alert_disk] += 1
                                for disk_name, count in alert_counts.items():
                                    DISK_TEMP_ALERT_COUNT.labels(disk=disk_name).set(count)
                        except Exception:
                            LOG.debug("disk.temperature_alerts failed", exc_info=True)

                    # The method requires the disk list and include-thresholds flag.
                    temps = None
                    if disk_names:
                        try:
                            temps = self._call(client, "disk.temperatures", [disk_names, False])
                        except Exception:
                            LOG.debug("disk.temperatures not available", exc_info=True)
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
                        raw_name = iface.get("name")
                        if not isinstance(raw_name, str) or not raw_name:
                            continue
                        name = raw_name
                        candidate = iface.get("state")
                        if isinstance(candidate, dict):
                            link_up = _link_is_up(_first_not_none(
                                candidate.get("link_state"),
                                candidate.get("up"),
                                candidate.get("state"),
                            ))
                        else:
                            link_up = _link_is_up(_first_not_none(iface.get("up"), iface.get("link_state")))
                        if link_up is not None:
                            INTERFACE_LINK_UP.labels(interface=name).set(1 if link_up else 0)

                        # Interface MTU
                        mtu = _as_float(
                            candidate.get("mtu") if isinstance(candidate, dict) else iface.get("mtu")
                        )
                        if mtu is None:
                            mtu = _as_float(iface.get("mtu"))
                        if mtu is not None:
                            INTERFACE_MTU.labels(interface=name).set(mtu)

                        # Interface type (PHYSICAL/BRIDGE/LINK_AGGREGATION/VLAN)
                        iface_type = _str_label(iface.get("type"), "unknown")
                        if iface_type and iface_type != "unknown":
                            INTERFACE_TYPE.labels(interface=name, type=iface_type).set(1)

                    services = result_cache.get("service.query")
                    if services is None:
                        services = self._call_query_with_fallback(
                            client, "service.query",
                            {"extra": {"include_state": True}, "select": ["service", "enable", "state"]},
                        )
                        result_cache["service.query"] = services
                    service_list = services if isinstance(services, list) else []
                    SERVICE_COUNT.set(len(service_list))
                    for svc in service_list:
                        if not isinstance(svc, dict):
                            continue
                        raw_name = _first_not_none(svc.get("service"), svc.get("name"))
                        if not isinstance(raw_name, str) or not raw_name:
                            continue
                        name = raw_name
                        _set_optional_bool_gauge(
                            SERVICE_ENABLED.labels(service=name), svc.get("enable")
                        )
                        state = svc.get("state")
                        running = state.get("running") if isinstance(state, dict) else state
                        _set_optional_bool_gauge(SERVICE_RUNNING.labels(service=name), running)

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
                        raw_code = update.get("code")
                        status_label = raw_code.upper() if isinstance(raw_code, str) else None
                        if status_label in {"NORMAL", "ERROR"}:
                            UPDATE_STATUS.labels(status=status_label).set(1)
                        status = update.get("status")
                        if (
                            status_label == "NORMAL"
                            and isinstance(status, dict)
                            and "new_version" in status
                        ):
                            UPDATE_AVAILABLE.set(
                                1 if status.get("new_version") is not None else 0
                            )
                        download = update.get("update_download_progress")
                        if isinstance(download, dict):
                            percent = _as_percent(download.get("percent"))
                            if percent is not None:
                                UPDATE_DOWNLOAD_PROGRESS_PERCENT.set(percent)

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

                    # UPS configuration is secret-bearing and 25.10.2 has no documented
                    # live-status read method; service.query covers enable/running state.

                    # --- Catalog ---
                    self._collect_catalog_metrics(client, result_cache)

                    # --- v4 additions: Security / FIPS ---
                    self._collect_fips_metrics(client, result_cache)

                    # --- v4 additions: Feature flags ---
                    self._collect_feature_flags(client)

                    # --- v4 additions: Hardware / Chassis ---
                    self._collect_chassis_hardware(client, result_cache)

                    # TrueNAS Connect and TrueCommand config calls include credentials;
                    # their legacy status gauges intentionally remain unavailable.

                    # --- v4 additions: Audit ---
                    self._collect_audit_metrics(client, result_cache)

                    # --- IPMI LAN (with correct channel params) ---
                    self._collect_ipmi_lan_metrics(client, result_cache)

                    # --- v5 collectors ---
                    self._collect_scrub_task_metrics(client, result_cache)
                    self._collect_snapshot_metrics(client, result_cache)
                    self._collect_resilver_config(client, result_cache)
                    self._collect_cloud_backup_metrics(client, result_cache)
                    self._collect_cronjob_metrics(client, result_cache)
                    # DISK_IN_USE is emitted above from documented disk.query pool data.
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
                _log_exception_redacted(
                    LOG,
                    logging.ERROR,
                    "Scrape failed",
                    self.config.ws_url,
                )
                success = False

        if self._is_collector_mode():
            self._publish_cached_events_to_default_registry()
        with self._lock:
            if not success and not reset_done and self._poll_metrics_are_too_stale():
                self._reset_poll_cycle_metrics()
            SCRAPE_SUCCESS.set(1 if success else 0)
            SCRAPE_DURATION.set(max(0.0, time.time() - started))
            if success:
                self._last_scrape_success_monotonic = time.monotonic()
            self._publish_metric_snapshot()

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
            vs = (
                cache["system.version_short"]
                if "system.version_short" in cache
                else self._call(client, "system.version_short", [])
            )
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
            _set_optional_bool_gauge(SYSTEM_MANAGED_BY_TRUECOMMAND, mtc)
        except Exception:
            LOG.debug("truenas.managed_by_truecommand failed", exc_info=True)

    # ------------------------------------------------------------------
    # Update extras (available version names)
    # ------------------------------------------------------------------

    def _collect_update_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Expose available update versions as labelled metrics."""
        versions = None
        try:
            versions = cache.get("update.available_versions") or self._call(client, "update.available_versions", [])
        except Exception:
            LOG.debug("update.available_versions failed", exc_info=True)

        UPDATE_VERSION_AVAILABLE.clear()
        if isinstance(versions, list):
            for v in versions[: self.config.max_list_items]:
                ver_str = None
                if isinstance(v, str):
                    ver_str = v
                elif isinstance(v, dict):
                    version = v.get("version")
                    if isinstance(version, dict):
                        raw_version = version.get("version")
                        if isinstance(raw_version, str):
                            ver_str = raw_version
                if ver_str and ver_str != "unknown":
                    UPDATE_VERSION_AVAILABLE.labels(version=ver_str).set(1)

        try:
            config = cache.get("update.config")
            if config is None:
                config = self._safe_call_auto(client, "update.config")
            if isinstance(config, dict):
                _set_optional_bool_gauge(UPDATE_AUTOCHECK_ENABLED, config.get("autocheck"))
                profile = config.get("profile") or config.get("update_profile") or config.get("train")
                if profile:
                    UPDATE_PROFILE_INFO.clear()
                    UPDATE_PROFILE_INFO.labels(profile=_str_label(profile, "unknown")).set(1)
        except Exception:
            LOG.debug("update.config failed", exc_info=True)

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

        try:
            BOOT_ENV_COUNT.set(
                self._count_or_len(
                    client, "boot.environment.query", envs, self.config.query_limit
                )
            )
        except Exception:
            BOOT_ENV_COUNT.set(len(envs))
        active_count = 0
        activated_count = 0
        keep_count = 0
        BOOT_ENV_ACTIVE.clear()
        BOOT_ENV_KEEP.clear()
        BOOT_ENV_SIZE_BYTES.clear()

        for env in envs[: self.config.max_list_items]:
            if not isinstance(env, dict):
                continue
            name = _str_label(env.get("id") or env.get("name"), "unknown")
            active = _as_optional_bool(env.get("active"))
            activated = _as_optional_bool(env.get("activated"))
            keep = _as_optional_bool(env.get("keep"))
            if active is True:
                active_count += 1
            if activated is True:
                activated_count += 1
            if keep is True:
                keep_count += 1
            if active is not None:
                BOOT_ENV_ACTIVE.labels(name=name).set(1 if active else 0)
            if activated is not None:
                BOOT_ENV_ACTIVATED.labels(name=name).set(1 if activated else 0)
            if keep is not None:
                BOOT_ENV_KEEP.labels(name=name).set(1 if keep else 0)
            rawspace = _as_float(_first_not_none(env.get("used_bytes"), env.get("rawspace"), env.get("size")))
            if rawspace is not None:
                BOOT_ENV_SIZE_BYTES.labels(name=name).set(rawspace)
                BOOT_ENV_USED_BYTES.labels(name=name).set(rawspace)

        BOOT_ENV_ACTIVE_COUNT.set(active_count)
        BOOT_ENV_ACTIVATED_COUNT.set(activated_count)
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
            _set_optional_bool_gauge(VM_SUPPORTS_VIRTUALIZATION, sv)
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

        # vm.flags (bounded, known capability booleans)
        try:
            vm_flags = cache.get("vm.flags")
            if vm_flags is None:
                vm_flags = self._safe_call_auto(client, "vm.flags")
            if isinstance(vm_flags, dict):
                _set_optional_bool_gauge(VM_FLAG_INTEL_VMX, vm_flags.get("intel_vmx"))
                _set_optional_bool_gauge(VM_FLAG_AMD_RVI, vm_flags.get("amd_rvi"))
                _set_optional_bool_gauge(
                    VM_FLAG_UNRESTRICTED_GUEST, vm_flags.get("unrestricted_guest")
                )
                amd_asids = _as_optional_bool(vm_flags.get("amd_asids"))
                if amd_asids is not None:
                    VM_FLAG_AMD_ASIDS.set(1 if amd_asids else 0)
                    VM_FLAG_AMD_ASIDS_SUPPORTED.set(1 if amd_asids else 0)
        except Exception:
            LOG.debug("vm.flags failed", exc_info=True)

        # vm.virtualization_details support/error rollups
        try:
            virt_details = cache.get("vm.virtualization_details")
            if virt_details is None:
                virt_details = self._safe_call_auto(client, "vm.virtualization_details")

            if isinstance(virt_details, dict):
                supported = None
                for key in ("supported", "is_supported", "hardware_virtualization", "virtualization_supported"):
                    if key in virt_details:
                        supported = _as_optional_bool(virt_details.get(key))
                        break
                if supported is None and isinstance(virt_details.get("details"), dict):
                    supported = _as_optional_bool(virt_details["details"].get("supported"))
                if supported is not None:
                    VM_VIRTUALIZATION_DETAILS_SUPPORTED.set(1 if supported else 0)

                error_present = False
                error_value = virt_details.get("error")
                if isinstance(error_value, str):
                    error_present = bool(error_value.strip())
                elif error_value is not None:
                    error_present = _as_bool(error_value)
                if not error_present:
                    error_present = _as_bool(virt_details.get("errors"))
                VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT.set(1 if error_present else 0)
        except Exception:
            LOG.debug("vm.virtualization_details failed", exc_info=True)

    # ------------------------------------------------------------------
    # Virt (Incus/LXD — TrueNAS 25.x)
    # ------------------------------------------------------------------

    def _collect_virt_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect Incus/LXD container instance and volume metrics.

        v26 renamed the virt.* API to container.*; v25 still uses
        virt.instance.query. The active compatibility profile decides which
        method exists. container.query exposes sensitive fields (initenv holds
        per-container environment variables, idmap, etc.), so we request only the
        ``name`` and ``status`` fields via ``select`` and never fetch the full
        object.
        """
        use_container = self.compatibility_profile.allows_method("container.query")
        instance_method = "container.query" if use_container else "virt.instance.query"
        # v26 container.query nests state under ``status.state``; v25
        # virt.instance.query returns a flat ``status`` string plus a ``type``.
        select_fields = ["name", "status"] if use_container else ["name", "type", "status"]

        # Instances
        try:
            instances = cache.get(instance_method) or self._call(client, instance_method, [
                [], {"limit": self.config.query_limit, "select": select_fields}
            ])
        except Exception:
            LOG.debug("%s failed", instance_method, exc_info=True)
            instances = None

        if isinstance(instances, list):
            try:
                VIRT_INSTANCE_COUNT.set(
                    self._count_or_len(
                        client, instance_method, instances, self.config.query_limit
                    )
                )
            except Exception:
                LOG.debug("%s count failed", instance_method, exc_info=True)
            VIRT_INSTANCE_RUNNING.clear()
            for inst in instances[: self.config.max_entity_calls]:
                if not isinstance(inst, dict):
                    continue
                name = _str_label(inst.get("name"), "unknown")
                inst_type = _str_label(inst.get("type"), "CONTAINER").upper()
                status = inst.get("status")
                if isinstance(status, dict):
                    # v26: status is {"state": ..., "pid": ..., "domain_state": ...}
                    status = status.get("state")
                if isinstance(status, str) and status:
                    running = status.upper() in {"RUNNING", "STARTED", "UP"}
                    VIRT_INSTANCE_RUNNING.labels(name=name, type=inst_type).set(
                        1 if running else 0
                    )

                # CPU and memory utilization are event-owned; the query fields
                # named cpu/memory are configuration, not usage.

        # Volumes: v25 only. v26 dropped virt.volume.query and offers no
        # equivalent read-only volume inventory, so VIRT_VOLUME_COUNT stays NaN
        # (unknown) rather than being fabricated as 0.
        if not use_container:
            try:
                volume_count = self._query_count(client, "virt.volume.query")
            except Exception:
                LOG.debug("virt.volume.query failed", exc_info=True)
                volume_count = None
            if volume_count is not None:
                VIRT_VOLUME_COUNT.set(volume_count)

        # virt.global.config (v25) / lxc.config (v26) expose no operational state
        # field, so the global-state and volume-size metrics remain NaN.

    # ------------------------------------------------------------------
    # Fibre Channel
    # ------------------------------------------------------------------

    def _collect_fc_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect Fibre Channel host and port metrics."""
        # FC hosts (HBAs)
        try:
            FC_HOST_COUNT.set(self._query_count(client, "fc.fc_host.query"))
        except Exception:
            LOG.debug("fc.fc_host.query failed", exc_info=True)

        # FC port status entries are opaque; only use documented count mode.
        try:
            FC_PORT_COUNT.set(self._query_count(client, "fcport.status"))
        except Exception:
            LOG.debug("fcport.status failed", exc_info=True)

    # ------------------------------------------------------------------
    # NVMe-oF
    # ------------------------------------------------------------------

    def _collect_nvmet_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect NVMe-oF session, subsystem, and port counts."""
        # Sessions
        try:
            NVMET_SESSION_COUNT.set(self._query_count(client, "nvmet.global.sessions"))
        except Exception:
            LOG.debug("nvmet.global.sessions failed", exc_info=True)

        # Subsystems
        try:
            NVMET_SUBSYS_COUNT.set(self._query_count(client, "nvmet.subsys.query"))
        except Exception:
            LOG.debug("nvmet.subsys.query failed", exc_info=True)

        # Ports
        try:
            NVMET_PORT_COUNT.set(self._query_count(client, "nvmet.port.query"))
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
            _set_optional_bool_gauge(ISCSI_ALUA_ENABLED, alua)
        except Exception:
            LOG.debug("iscsi.global.alua_enabled failed", exc_info=True)

        try:
            iser = cache.get("iscsi.global.iser_enabled")
            if iser is None:
                iser = self._call(client, "iscsi.global.iser_enabled", [])
            _set_optional_bool_gauge(ISCSI_ISER_ENABLED, iser)
        except Exception:
            LOG.debug("iscsi.global.iser_enabled failed", exc_info=True)

        try:
            ISCSI_SESSION_COUNT.set(self._query_count(client, "iscsi.global.sessions"))
            ISCSI_SESSION_ISER_COUNT.set(
                self._query_count(client, "iscsi.global.sessions", [["iser", "=", True]])
            )
            ISCSI_SESSION_OFFLOAD_COUNT.set(
                self._query_count(client, "iscsi.global.sessions", [["offload", "=", True]])
            )
            ISCSI_SESSION_IMMEDIATE_DATA_COUNT.set(
                self._query_count(
                    client, "iscsi.global.sessions", [["immediate_data", "=", True]]
                )
            )
        except Exception:
            LOG.debug("iscsi.global.sessions failed", exc_info=True)

    def _emit_cached_disk_temp_agg(self) -> None:
        for (disk_name, kind), val in self._disk_temp_agg_cache.items():
            DISK_TEMP_AGG_C.labels(disk=disk_name, kind=kind).set(val)

    def _collect_disk_temperature_agg(
        self,
        client: JsonRpcWsClient,
        disk_names: list[str],
    ) -> None:
        """Collect cached 7-day disk temperature aggregates."""
        self._disk_temp_agg_cycle += 1
        current_cycle = self._disk_temp_agg_cycle
        current_disk_names = tuple(disk_names)
        disk_list_changed = current_disk_names != self._disk_temp_agg_disk_names
        if disk_list_changed:
            self._disk_temp_agg_disk_names = current_disk_names
            self._disk_temp_agg_cache = {}
            self._disk_temp_agg_last_success_cycle = None
            self._disk_temp_agg_last_attempt_cycle = None

        last_success = self._disk_temp_agg_last_success_cycle
        last_attempt = self._disk_temp_agg_last_attempt_cycle
        should_refresh = (
            disk_list_changed
            or last_attempt is None
            or current_cycle - last_attempt >= DISK_TEMP_AGG_REFRESH_CYCLES - 1
        )

        if should_refresh:
            self._disk_temp_agg_last_attempt_cycle = current_cycle
            try:
                temp_agg = self._call(client, "disk.temperature_agg", [disk_names, 7])
            except Exception:
                COLLECTOR_ERRORS_TOTAL.labels(collector="disks").inc()
                LOG.debug("disk.temperature_agg failed", exc_info=True)
            else:
                cache: dict[tuple[str, str], float] = {}
                if isinstance(temp_agg, dict):
                    for disk_name, agg in temp_agg.items():
                        if not isinstance(agg, dict):
                            continue
                        disk_label = _str_label(disk_name)
                        for kind in ("min", "max", "avg"):
                            val = _as_float(agg.get(kind))
                            if val is not None:
                                cache[(disk_label, kind)] = val
                self._disk_temp_agg_cache = cache
                self._disk_temp_agg_last_success_cycle = current_cycle
                last_success = current_cycle

        if (
            last_success is not None
            and current_cycle - last_success
            >= DISK_TEMP_AGG_REFRESH_CYCLES * HEAVY_QUERY_CACHE_MAX_STALE_FACTOR
        ):
            self._disk_temp_agg_cache = {}
            self._disk_temp_agg_last_success_cycle = None

        self._emit_cached_disk_temp_agg()

    # ------------------------------------------------------------------
    # Network extras
    # ------------------------------------------------------------------

    def _collect_network_extras(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect pending changes flag and checkin_waiting timer."""
        try:
            pending = cache.get("interface.has_pending_changes")
            if pending is None:
                pending = self._call(client, "interface.has_pending_changes", [])
            _set_optional_bool_gauge(INTERFACE_HAS_PENDING_CHANGES, pending)
        except Exception:
            LOG.debug("interface.has_pending_changes failed", exc_info=True)

        try:
            waiting = cache.get("interface.checkin_waiting")
            if waiting is None:
                waiting = self._call(client, "interface.checkin_waiting", [])
            val = _as_float(waiting)
            if val is not None:
                INTERFACE_CHECKIN_WAITING_SECONDS.set(val)
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

        try:
            rate_limit = cache.get("app.image.dockerhub_rate_limit")
            if rate_limit is None:
                rate_limit = self._safe_call_auto(client, "app.image.dockerhub_rate_limit")

            if isinstance(rate_limit, dict):
                total = _as_float(rate_limit.get("total_pull_limit"))
                remaining = _as_float(rate_limit.get("remaining_pull_limit"))
                window_seconds = _as_float(rate_limit.get("total_time_limit_in_secs"))
                remaining_window_seconds = _as_float(
                    rate_limit.get("remaining_time_limit_in_secs")
                )
                if total is not None:
                    APP_DOCKERHUB_PULL_LIMIT_TOTAL.set(total)
                if remaining is not None:
                    APP_DOCKERHUB_PULL_LIMIT_REMAINING.set(remaining)
                if window_seconds is not None:
                    APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS.set(window_seconds)
                if remaining_window_seconds is not None:
                    APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS.set(
                        remaining_window_seconds
                    )

                error_value = rate_limit.get("error")
                error_present = False
                if isinstance(error_value, str):
                    error_present = bool(error_value.strip())
                elif error_value is not None:
                    error_present = _as_bool(error_value)
                APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT.set(1 if error_present else 0)
        except Exception:
            LOG.debug("app.image.dockerhub_rate_limit failed", exc_info=True)

        # WebShare (v26 successor to WebDAV; the method does not exist on 25.10).
        # Counts only; the config's passkey field is an auth *mode*, not a secret.
        if self.compatibility_profile.allows_method("sharing.webshare.query"):
            try:
                APP_WEBDAV_SHARE_COUNT.set(
                    self._query_count(client, "sharing.webshare.query")
                )
            except Exception:
                LOG.debug("sharing.webshare.query failed", exc_info=True)
            try:
                webshare = cache.get("webshare.config") or self._call(
                    client, "webshare.config", []
                )
                if isinstance(webshare, dict):
                    passkey = webshare.get("passkey")
                    if isinstance(passkey, str) and passkey:
                        WEBSHARE_ENABLED.set(
                            0 if passkey.strip().upper() == "DISABLED" else 1
                        )
            except Exception:
                LOG.debug("webshare.config failed", exc_info=True)

    # ------------------------------------------------------------------
    # Catalog metrics
    # ------------------------------------------------------------------

    def _collect_catalog_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect app catalog train count."""
        try:
            trains = cache.get("catalog.trains") or self._call(client, "catalog.trains", [])
            if isinstance(trains, (list, dict)):
                CATALOG_TRAIN_COUNT.set(len(trains))
        except Exception:
            LOG.debug("catalog.trains failed", exc_info=True)

        try:
            config = cache.get("catalog.config")
            if config is None:
                config = self._safe_call_auto(client, "catalog.config")
            if isinstance(config, dict):
                CATALOG_CONFIG_PRESENT.set(1)
                preferred = config.get("preferred_trains") or config.get("preferred_train") or []
                if isinstance(preferred, list):
                    CATALOG_PREFERRED_TRAIN_COUNT.set(len(preferred))
                elif preferred:
                    CATALOG_PREFERRED_TRAIN_COUNT.set(1)
            elif config is not None:
                CATALOG_CONFIG_PRESENT.set(1)
        except Exception:
            LOG.debug("catalog.config failed", exc_info=True)

    # ------------------------------------------------------------------
    # Security / FIPS metrics (v4)
    # ------------------------------------------------------------------

    def _collect_fips_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect FIPS availability and enabled status (v25+)."""
        try:
            fips_available = cache.get("system.security.info.fips_available")
            if fips_available is None:
                fips_available = self._call(client, "system.security.info.fips_available", [])
            _set_optional_bool_gauge(FIPS_AVAILABLE, fips_available)
        except Exception:
            LOG.debug("system.security.info.fips_available failed", exc_info=True)

        try:
            fips_enabled = cache.get("system.security.info.fips_enabled")
            if fips_enabled is None:
                fips_enabled = self._call(client, "system.security.info.fips_enabled", [])
            _set_optional_bool_gauge(FIPS_ENABLED, fips_enabled)
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
                _set_optional_bool_gauge(FEATURE_ENABLED.labels(feature=feature), result)
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

        retention = _as_float(config.get("retention"))
        if retention is not None:
            AUDIT_RETENTION_DAYS.set(retention)
        reservation_gib = _as_float(config.get("reservation"))
        if reservation_gib is not None:
            AUDIT_RESERVATION_BYTES.set(reservation_gib * 1024**3)
        quota_gib = _as_float(config.get("quota"))
        if quota_gib is not None:
            AUDIT_QUOTA_BYTES.set(quota_gib * 1024**3)
        remote_logging = config.get("remote_logging_enabled")
        parsed_remote_logging = _as_optional_bool(remote_logging)
        if parsed_remote_logging is not None:
            AUDIT_REMOTE_LOGGING_ENABLED.set(1 if parsed_remote_logging else 0)

    # ------------------------------------------------------------------
    # v5 collectors: Pool scrub tasks (pool.scrub.query)
    # ------------------------------------------------------------------

    def _collect_scrub_task_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect pool scrub task scheduling health."""
        try:
            tasks = cache.get("pool.scrub.query") or self._call(client, "pool.scrub.query", [
                [], {"limit": self.config.query_limit, "select": ["id", "pool_name", "enabled"]}
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="scrub_tasks").inc()
            LOG.debug("pool.scrub.query failed", exc_info=True)
            return

        if not isinstance(tasks, list):
            return

        try:
            POOL_SCRUB_TASK_COUNT.set(
                self._count_or_len(
                    client, "pool.scrub.query", tasks, self.config.query_limit
                )
            )
        except Exception:
            LOG.debug("pool.scrub.query count failed", exc_info=True)

        for task in tasks[: self.config.max_entity_calls]:
            if not isinstance(task, dict):
                continue
            pool_name = _str_label(
                task.get("pool_name"), "unknown"
            )
            _set_optional_bool_gauge(
                POOL_SCRUB_TASK_ENABLED.labels(pool=pool_name), task.get("enabled")
            )

    # ------------------------------------------------------------------
    # v5 collectors: Snapshot count (pool.snapshot.query)
    # ------------------------------------------------------------------

    def _collect_snapshot_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect total snapshot count and oldest snapshot timestamp."""
        try:
            # Exact count intentionally retained: fetching all snapshots just to
            # len() them would transfer far more data than a server-side count.
            SNAPSHOT_TOTAL_COUNT.set(self._query_count(client, "pool.snapshot.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="snapshots").inc()
            LOG.debug("pool.snapshot.query count failed", exc_info=True)

        self._collect_snapshot_oldest_metric(client)

    def _emit_cached_snapshot_oldest(self) -> None:
        if self._snapshot_oldest_cached_value is not None:
            SNAPSHOT_OLDEST_TS.set(self._snapshot_oldest_cached_value)

    def _collect_snapshot_oldest_metric(self, client: JsonRpcWsClient) -> None:
        """Collect cached oldest snapshot timestamp."""
        self._snapshot_oldest_cycle += 1
        current_cycle = self._snapshot_oldest_cycle
        last_success = self._snapshot_oldest_last_success_cycle
        last_attempt = self._snapshot_oldest_last_attempt_cycle
        should_refresh = (
            last_attempt is None
            or current_cycle - last_attempt >= SNAPSHOT_OLDEST_REFRESH_CYCLES - 1
        )

        if should_refresh:
            self._snapshot_oldest_last_attempt_cycle = current_cycle
            oldest_query: Any = None
            refresh_succeeded = False
            try:
                # v26 note: pool.snapshot.query returns empty properties {} unless
                # extra.properties requests them, so order_by on
                # properties.creation.parsed would sort None<None and raise EINVAL
                # server-side. The nested select alias also returns {} on v26, so we
                # fetch the full object (limit 1) and let
                # _extract_snapshot_creation_timestamp read properties.creation.parsed.
                oldest_query = self._call(client, "pool.snapshot.query", [
                    [], {
                        "limit": 1,
                        "order_by": ["properties.creation.parsed"],
                        "extra": {"properties": ["creation"]},
                    }
                ])
                refresh_succeeded = True
            except Exception:
                COLLECTOR_ERRORS_TOTAL.labels(collector="snapshots").inc()
                LOG.debug("pool.snapshot.query oldest snapshot failed", exc_info=True)

            if refresh_succeeded:
                oldest_snapshot: Any = None
                if isinstance(oldest_query, list):
                    oldest_snapshot = oldest_query[0] if oldest_query else None
                elif isinstance(oldest_query, dict):
                    oldest_snapshot = oldest_query

                self._snapshot_oldest_cached_value = (
                    self._extract_snapshot_creation_timestamp(oldest_snapshot)
                )
                self._snapshot_oldest_has_cache = True
                self._snapshot_oldest_last_success_cycle = current_cycle
                last_success = current_cycle

        if (
            self._snapshot_oldest_has_cache
            and last_success is not None
            and current_cycle - last_success
            >= SNAPSHOT_OLDEST_REFRESH_CYCLES * HEAVY_QUERY_CACHE_MAX_STALE_FACTOR
        ):
            self._snapshot_oldest_cached_value = None
            self._snapshot_oldest_has_cache = False
            self._snapshot_oldest_last_success_cycle = None

        if self._snapshot_oldest_has_cache:
            self._emit_cached_snapshot_oldest()

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
            _set_optional_bool_gauge(POOL_RESILVER_ENABLED, config.get("enabled"))

    # ------------------------------------------------------------------
    # v5 collectors: Cloud backup tasks
    # ------------------------------------------------------------------

    def _collect_cloud_backup_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect cloud backup task inventory and state."""
        try:
            tasks = cache.get("cloud_backup.query") or self._call(client, "cloud_backup.query", [
                [], {"limit": self.config.query_limit, "select": ["id", "enabled"]}
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="cloud_backup").inc()
            LOG.debug("cloud_backup.query failed", exc_info=True)
            return

        if not isinstance(tasks, list):
            return

        try:
            CLOUD_BACKUP_TASK_COUNT.set(
                self._count_or_len(
                    client, "cloud_backup.query", tasks, self.config.query_limit
                )
            )
        except Exception:
            LOG.debug("cloud_backup.query count failed", exc_info=True)

        for task in tasks[: self.config.max_entity_calls]:
            if not isinstance(task, dict):
                continue
            name = _str_label(task.get("id"), "unknown")
            _set_optional_bool_gauge(
                CLOUD_BACKUP_TASK_ENABLED.labels(name=name), task.get("enabled")
            )


    # ------------------------------------------------------------------
    # v5 collectors: Cron jobs
    # ------------------------------------------------------------------

    def _collect_cronjob_metrics(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect cron job inventory."""
        try:
            jobs = cache.get("cronjob.query") or self._call(client, "cronjob.query", [
                [], {"limit": self.config.query_limit, "select": ["id", "enabled"]}
            ])
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="cronjobs").inc()
            LOG.debug("cronjob.query failed", exc_info=True)
            return

        if not isinstance(jobs, list):
            return

        try:
            CRONJOB_COUNT.set(
                self._count_or_len(client, "cronjob.query", jobs, self.config.query_limit)
            )
        except Exception:
            LOG.debug("cronjob.query count failed", exc_info=True)

        for job in jobs[: self.config.max_entity_calls]:
            if not isinstance(job, dict):
                continue
            name = _str_label(job.get("id"), "unknown")
            _set_optional_bool_gauge(CRONJOB_ENABLED.labels(name=name), job.get("enabled"))

    # ------------------------------------------------------------------
    # v5 collectors: Protocol configs (SMB, NFS, SSH, FTP, SNMP)
    # ------------------------------------------------------------------

    def _collect_protocol_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect protocol service configuration flags."""
        protocol_services: dict[str, bool] | None = None
        try:
            protocol_services = self._query_service_enable_map(
                client, ("ssh", "ftp", "snmp"), cache
            )
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="protocol_services").inc()
            LOG.debug("service.query for protocol services failed", exc_info=True)

        # SMB
        try:
            smb = cache.get("smb.config") or self._call(client, "smb.config", [])
            if isinstance(smb, dict):
                _set_optional_bool_gauge(SMB_MULTICHANNEL_ENABLED, smb.get("multichannel"))
                _set_optional_bool_gauge(SMB1_ENABLED, smb.get("enable_smb1"))
                _set_optional_bool_gauge(SMB_NTLMV1_AUTH_ENABLED, smb.get("ntlmv1_auth"))
                encryption = _str_label(smb.get("encryption"), "UNKNOWN").upper()
                if encryption in {"DEFAULT", "NEGOTIATE", "DESIRED", "REQUIRED"}:
                    SMB_ENCRYPTION_MODE.labels(mode=encryption).set(1)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="smb_config").inc()
            LOG.debug("smb.config failed", exc_info=True)

        # NFS
        try:
            nfs = cache.get("nfs.config") or self._call(client, "nfs.config", [])
            if isinstance(nfs, dict):
                protocols = nfs.get("protocols")
                if isinstance(protocols, list):
                    v4 = "NFSV4" in {_str_label(item).upper() for item in protocols}
                    NFS_V4_ENABLED.set(1 if v4 else 0)
                _set_optional_bool_gauge(NFS_RDMA_ENABLED, nfs.get("rdma"))
                servers = _as_float(nfs.get("servers"))
                if servers is not None:
                    NFS_SERVERS.set(servers)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="nfs_config").inc()
            LOG.debug("nfs.config failed", exc_info=True)

        # SSH
        if protocol_services is not None and "ssh" in protocol_services:
            SSH_ENABLED.set(1 if protocol_services["ssh"] else 0)

        # ssh.config includes host private keys and cannot be field-selected.
        # Preserve the legacy password-auth metric as unavailable (NaN).

        # FTP
        if protocol_services is not None and "ftp" in protocol_services:
            FTP_ENABLED.set(1 if protocol_services["ftp"] else 0)

        # SNMP
        if protocol_services is not None and "snmp" in protocol_services:
            SNMP_ENABLED.set(1 if protocol_services["snmp"] else 0)

    # ------------------------------------------------------------------
    # v5 collectors: System advanced/general config
    # ------------------------------------------------------------------

    def _collect_system_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect non-secret system configuration fields."""
        # system.advanced.config includes anonstats_token, arbitrary banners,
        # and remote syslog endpoints and has no field-selection parameter.
        # Retain the console metric contracts without fetching that response.

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

    def _collect_kmip_sync_pending(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        try:
            pending = cache.get("kmip.kmip_sync_pending")
            if pending is None:
                pending = self._call(client, "kmip.kmip_sync_pending", [])
            _set_optional_bool_gauge(KMIP_SYNC_PENDING, pending)
        except Exception:
            LOG.debug("kmip.kmip_sync_pending failed", exc_info=True)

    def _collect_infrastructure_configs(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect KMIP, support, and system dataset configs."""
        # kmip.config includes endpoint and key-management configuration and
        # cannot be server-side selected. The legacy metric remains NaN.

        self._collect_kmip_sync_pending(client, cache)

        # Support
        try:
            avail = cache.get("support.is_available") or self._call(client, "support.is_available", [])
            _set_optional_bool_gauge(SUPPORT_AVAILABLE, avail)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="support_available").inc()
            LOG.debug("support.is_available failed", exc_info=True)

        try:
            available_enabled = cache.get("support.is_available_and_enabled")
            if available_enabled is None:
                available_enabled = self._safe_call_auto(client, "support.is_available_and_enabled")
            if available_enabled is not None:
                _set_optional_bool_gauge(
                    SUPPORT_AVAILABLE_AND_ENABLED, available_enabled
                )
        except Exception:
            LOG.debug("support.is_available_and_enabled failed", exc_info=True)

        # support.config contains operator contact PII and has no field-selection
        # parameter. SUPPORT_CONFIG_ENABLED therefore remains unavailable.

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
        """Collect various inventory counts.

        Exact count queries intentionally retained: these are pure count-only
        collectors with no accompanying list fetch, so the server-side count is
        the most efficient pattern (no payload transfer).
        """
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
        """Collect iSCSI target/portal/extent/initiator counts.

        Exact count queries intentionally retained — count-only, no list fetch.
        """
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
        """Collect NVMe-oF host and namespace counts.

        Exact count queries intentionally retained — count-only, no list fetch.
        """
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
        # network.configuration.config may contain proxy credentials in the URL
        # and has no field-select parameter. Do not fetch it for one boolean.

        # Docker images (exact count intentionally retained — count-only, no list fetch)
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
            reporting_services = self._query_service_enable_map(
                client, ("netdata", "reporting"), cache
            )
            if reporting_services:
                enabled = reporting_services.get("netdata")
                if enabled is None:
                    enabled = reporting_services.get("reporting")
                REPORTING_ENABLED.set(1 if enabled else 0)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="reporting_config").inc()
            LOG.debug("service.query for reporting service failed", exc_info=True)

        # DNS resolvers
        try:
            DNS_RESOLVER_COUNT.set(self._query_count(client, "dns.query"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="dns_resolvers").inc()
            LOG.debug("dns.query failed", exc_info=True)

        # Reporting config rollups
        try:
            rep_cfg = cache.get("reporting.config")
            if rep_cfg is None:
                rep_cfg = self._safe_call_auto(client, "reporting.config")
            if isinstance(rep_cfg, dict):
                tier0_days = _as_float(_first_not_none(rep_cfg.get("tier0_days"), rep_cfg.get("retention_tier0_days")))
                tier1_days = _as_float(_first_not_none(rep_cfg.get("tier1_days"), rep_cfg.get("retention_tier1_days")))
                tier1_interval = _as_float(
                    rep_cfg.get("tier1_update_interval")
                    or rep_cfg.get("tier1_update_interval_seconds")
                )
                if tier0_days is not None:
                    REPORTING_TIER0_RETENTION_DAYS.set(tier0_days)
                if tier1_days is not None:
                    REPORTING_TIER1_RETENTION_DAYS.set(tier1_days)
                if tier1_interval is not None:
                    REPORTING_TIER1_UPDATE_INTERVAL_SECONDS.set(tier1_interval)
        except Exception:
            LOG.debug("reporting.config failed", exc_info=True)

        # NTP server aggregate rollups (aggregate-only for low cardinality)
        try:
            NTP_SERVER_COUNT.set(self._query_count(client, "system.ntpserver.query"))
            ntp_servers = self._call(client, "system.ntpserver.query", [
                [], {"select": ["prefer", "burst", "iburst", "minpoll", "maxpoll"]}
            ])

            if isinstance(ntp_servers, list):
                prefer_count = 0
                burst_count = 0
                iburst_count = 0
                min_poll_values: list[float] = []
                max_poll_values: list[float] = []
                valid_rollup = True

                for server in ntp_servers:
                    if not isinstance(server, dict):
                        valid_rollup = False
                        continue
                    prefer = _as_optional_bool(server.get("prefer"))
                    burst = _as_optional_bool(server.get("burst"))
                    iburst = _as_optional_bool(server.get("iburst"))
                    if None in {prefer, burst, iburst}:
                        valid_rollup = False
                    if prefer is True:
                        prefer_count += 1
                    if burst is True:
                        burst_count += 1
                    if iburst is True:
                        iburst_count += 1

                    min_poll = _as_float(server.get("minpoll"))
                    max_poll = _as_float(server.get("maxpoll"))
                    if min_poll is not None and -30 <= min_poll <= 30:
                        min_poll_values.append((2.0**min_poll) / 60.0)
                    else:
                        valid_rollup = False
                    if max_poll is not None and -30 <= max_poll <= 30:
                        max_poll_values.append((2.0**max_poll) / 60.0)
                    else:
                        valid_rollup = False

                if valid_rollup:
                    NTP_SERVER_PREFER_COUNT.set(prefer_count)
                    NTP_SERVER_BURST_COUNT.set(burst_count)
                    NTP_SERVER_IBURST_COUNT.set(iburst_count)
                    if min_poll_values:
                        NTP_SERVER_MIN_POLL_MINUTES.set(min(min_poll_values))
                    if max_poll_values:
                        NTP_SERVER_MAX_POLL_MINUTES.set(max(max_poll_values))
        except Exception:
            LOG.debug("system.ntpserver.query failed", exc_info=True)

    # ------------------------------------------------------------------
    # v5 collectors: Security posture (IOMMU, 2FA, mail, alert services)
    # ------------------------------------------------------------------

    def _collect_security_posture(self, client: JsonRpcWsClient, cache: dict[str, Any]) -> None:
        """Collect security and alerting configuration flags."""
        try:
            security_cfg = cache.get("system.security.config")
            if security_cfg is None:
                security_cfg = self._safe_call_auto(client, "system.security.config")
            if isinstance(security_cfg, dict):
                _set_optional_bool_gauge(
                    SYSTEM_SECURITY_FIPS_CONFIGURED, security_cfg.get("enable_fips")
                )
                _set_optional_bool_gauge(
                    SYSTEM_SECURITY_GPOS_STIG, security_cfg.get("enable_gpos_stig")
                )

                for gauge, field in (
                    (SYSTEM_SECURITY_PASSWORD_MIN_LENGTH, "min_password_length"),
                    (SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS, "min_password_age"),
                    (SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS, "max_password_age"),
                    (SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT, "password_history_length"),
                ):
                    value = _as_float(security_cfg.get(field))
                    if value is not None:
                        gauge.set(value)
        except Exception:
            LOG.debug("system.security.config failed", exc_info=True)

        # IOMMU
        try:
            iommu = self._call(client, "vm.device.iommu_enabled", [])
            _set_optional_bool_gauge(IOMMU_ENABLED, iommu)
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="iommu").inc()
            LOG.debug("vm.device.iommu_enabled failed", exc_info=True)

        # 2FA
        try:
            twofa = cache.get("auth.twofactor.config") or self._call(
                client, "auth.twofactor.config", []
            )
            if isinstance(twofa, dict):
                _set_optional_bool_gauge(TWOFACTOR_ENABLED, twofa.get("enabled"))
        except Exception:
            COLLECTOR_ERRORS_TOTAL.labels(collector="twofactor").inc()
            LOG.debug("auth.twofactor.config failed", exc_info=True)

        # mail.config contains SMTP/OAuth credentials and cannot be selected.

        # Alert services
        try:
            ALERTSERVICE_COUNT.set(self._query_count(client, "alertservice.query"))

            services = cache.get("alertservice.query") or self._call(
                client,
                "alertservice.query",
                [[], {"limit": self.config.query_limit, "select": ["id", "type__title", "enabled"]}],
            )
            if isinstance(services, list):
                for svc in services[: self.config.max_list_items]:
                    if not isinstance(svc, dict):
                        continue
                    name = _str_label(svc.get("id"), "unknown")
                    svc_type = _str_label(svc.get("type__title"), "unknown")
                    _set_optional_bool_gauge(
                        ALERTSERVICE_ENABLED.labels(name=name, type=svc_type),
                        svc.get("enabled"),
                    )
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

        if not self.config.enable_generic_method_metrics:
            return

        for channel in channels[: 4]:  # at most 4 channels
            try:
                chan_id = int(channel) if isinstance(channel, (int, float)) else int(str(channel))
                lan_data = self._call(client, "ipmi.lan.query", [{
                    "query-filters": [["channel", "=", chan_id]],
                    "query-options": {"limit": 1},
                    "ipmi-options": {"query-remote": False},
                }])
                if isinstance(lan_data, list):
                    self._extract_generic_metrics(
                        "ipmi.lan.query", lan_data, f"result.channel_{chan_id}", 0
                    )
            except Exception:
                LOG.debug("ipmi.lan.query channel %s failed", channel, exc_info=True)

    def run_forever(self) -> None:
        self._ensure_event_thread()
        while not self._stop_event.is_set():
            self.scrape_once()
            if self._stop_event.wait(self.config.interval_seconds):
                break


class TrueNASCollector:
    """Expose the last complete full-parity background snapshot."""

    def __init__(self, exporter: TrueNASExporter) -> None:
        self.exporter = exporter

    def describe(self):
        return []

    def collect(self):
        yield from self.exporter.metric_snapshot()


_load_config = load_config


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO").upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    config = _load_config()
    # Log the endpoint scheme/path but never the target hostname (safety invariant:
    # no hostname is ever logged — it can leak into container/aggregated logs).
    _parsed_ws_url = urlparse(config.ws_url)
    _safe_ws_url = f"{_parsed_ws_url.scheme}://<redacted-host>{_parsed_ws_url.path}"
    LOG.info(
        "Starting TrueNAS exporter v%s — mode=%s url=%s verify_tls=%s port=%s",
        EXPORTER_VERSION, config.exporter_mode, _safe_ws_url, config.verify_tls, config.exporter_port,
    )
    exporter = TrueNASExporter(config)
    server: Any
    if config.exporter_mode == "collector":
        registry = CollectorRegistry(auto_describe=True)
        registry.register(TrueNASCollector(exporter))  # type: ignore[arg-type]
        server = _start_http_server(
            config.exporter_bind_address,
            config.exporter_port,
            exporter._lock,
            registry=registry,
            lock_metrics=False,
            readiness_check=exporter.is_ready,
        )
        exporter._ensure_event_thread()
        exporter._scrape_thread = threading.Thread(
            target=exporter.run_forever, name="scrape-worker", daemon=True
        )
        exporter._scrape_thread.start()
    else:
        registry = CollectorRegistry(auto_describe=True)
        registry.register(TrueNASCollector(exporter))  # type: ignore[arg-type]
        server = _start_http_server(
            config.exporter_bind_address,
            config.exporter_port,
            exporter._lock,
            registry=registry,
            lock_metrics=False,
            readiness_check=exporter.is_ready,
        )

    def _request_shutdown(signum: int, _frame: Any) -> None:
        LOG.info("Received signal %s; shutting down", signum)
        exporter.stop()

    signal.signal(signal.SIGTERM, _request_shutdown)
    signal.signal(signal.SIGINT, _request_shutdown)

    try:
        if config.exporter_mode == "collector":
            exporter._stop_event.wait()
        else:
            exporter.run_forever()
    finally:
        exporter.stop()
        server.shutdown()
        if exporter._event_thread is not None:
            exporter._event_thread.join(timeout=max(1, config.event_stale_after_seconds + 1))
        if exporter._scrape_thread is not None:
            exporter._scrape_thread.join(timeout=max(1, config.timeout_seconds + 1))


if __name__ == "__main__":
    main()
