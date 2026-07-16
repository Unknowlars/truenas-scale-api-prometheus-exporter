"""Prometheus metric declarations and public metric contract objects."""

from dataclasses import dataclass
from typing import Literal, cast

from prometheus_client import Counter, Gauge, disable_created_metrics

from .version import __version__


@dataclass(frozen=True)
class MetricSpec:
    variable: str
    name: str
    metric_type: Literal["gauge", "counter"]
    help: str
    labels: tuple[str, ...]
    metric: Gauge | Counter


METRIC_SPECS: list[MetricSpec] = []
_METRIC_SPEC_BY_ID: dict[int, MetricSpec] = {}


def _declare_metric(
    variable: str,
    name: str,
    help_text: str,
    labels: list[str] | tuple[str, ...],
    metric_type: Literal["gauge", "counter"],
) -> Gauge | Counter:
    label_tuple = tuple(labels)
    metric = Gauge(name, help_text, label_tuple) if metric_type == "gauge" else Counter(name, help_text, label_tuple)
    spec = MetricSpec(variable, name, metric_type, help_text, label_tuple, metric)
    METRIC_SPECS.append(spec)
    _METRIC_SPEC_BY_ID[id(metric)] = spec
    return metric


def declare_gauge(variable: str, name: str, help_text: str, labels: list[str] | tuple[str, ...] = ()) -> Gauge:
    return cast(Gauge, _declare_metric(variable, name, help_text, labels, "gauge"))


def declare_counter(variable: str, name: str, help_text: str, labels: list[str] | tuple[str, ...] = ()) -> Counter:
    return cast(Counter, _declare_metric(variable, name, help_text, labels, "counter"))


def metric_spec(metric: Gauge | Counter) -> MetricSpec:
    return _METRIC_SPEC_BY_ID[id(metric)]


def metric_name(metric: Gauge | Counter) -> str:
    return metric_spec(metric).name


def metric_help(metric: Gauge | Counter) -> str:
    return metric_spec(metric).help


def metric_labels(metric: Gauge | Counter) -> tuple[str, ...]:
    return metric_spec(metric).labels

disable_created_metrics()
EXPORTER_VERSION = __version__

# ---------------------------------------------------------------------------
# Exporter health
# ---------------------------------------------------------------------------
SCRAPE_SUCCESS = declare_gauge("SCRAPE_SUCCESS", "truenas_up", "1 if last scrape succeeded, 0 otherwise")
LAST_SCRAPE_TS = declare_gauge("LAST_SCRAPE_TS", "truenas_last_scrape_timestamp_seconds", "Unix timestamp of last scrape attempt")
SCRAPE_DURATION = declare_gauge("SCRAPE_DURATION", "truenas_scrape_duration_seconds", "Duration of last scrape in seconds")

# ---------------------------------------------------------------------------
# API call diagnostics
# ---------------------------------------------------------------------------
API_CALL_SUCCESS = declare_gauge("API_CALL_SUCCESS", "truenas_api_call_success", "1 if API method call succeeded in latest scrape", ["method"])
API_CALL_DURATION = declare_gauge("API_CALL_DURATION", "truenas_api_call_duration_seconds", "Duration of API method call", ["method"])
# Counter (not Gauge): accumulates errors without creating stale zero-value 'none'
# series that pollute Prometheus when a method recovers from a previous failure.
API_CALL_ERRORS_TOTAL = declare_counter("API_CALL_ERRORS_TOTAL", 
    "truenas_api_call_errors_total",
    "Total API call errors per method and error type since exporter start",
    ["method", "error_type"],
)

# ---------------------------------------------------------------------------
# System / host
# ---------------------------------------------------------------------------
SYSTEM_STATE = declare_gauge("SYSTEM_STATE", "truenas_system_state", "System state enum mapped to label with value 1", ["state"])
SYSTEM_READY = declare_gauge("SYSTEM_READY", "truenas_system_ready", "1 if system state is READY")
SYSTEM_REBOOT_REQUIRED = declare_gauge("SYSTEM_REBOOT_REQUIRED", "truenas_system_reboot_required", "1 if a system reboot is pending")
SYSTEM_REBOOT_REASON = declare_gauge("SYSTEM_REBOOT_REASON", "truenas_system_reboot_reason", "Pending reboot reason as label", ["reason"])

HOST_INFO = declare_gauge("HOST_INFO", "truenas_host_info", "Static host info exported as labels", ["hostname", "version", "product_type"])
HOST_UPTIME_SECONDS = declare_gauge("HOST_UPTIME_SECONDS", "truenas_host_uptime_seconds", "Host uptime in seconds")
HOST_PHYSICAL_MEMORY_BYTES = declare_gauge("HOST_PHYSICAL_MEMORY_BYTES", "truenas_host_physical_memory_bytes", "Host physical memory in bytes")
HOST_CPU_CORES = declare_gauge("HOST_CPU_CORES", "truenas_host_cpu_cores", "Host CPU core count")
HOST_PHYSICAL_CPU_CORES = declare_gauge("HOST_PHYSICAL_CPU_CORES", "truenas_host_physical_cpu_cores", "Host physical CPU cores (non-HT)")
HOST_LOAD_AVERAGE = declare_gauge("HOST_LOAD_AVERAGE", "truenas_host_load_average", "Host load average", ["window"])

TRUENAS_IS_PRODUCTION = declare_gauge("TRUENAS_IS_PRODUCTION", "truenas_is_production", "1 if system is marked as production")
TRUENAS_IS_IX_HARDWARE = declare_gauge("TRUENAS_IS_IX_HARDWARE", "truenas_is_ix_hardware", "1 if running on iXsystems hardware")

# ---------------------------------------------------------------------------
# Boot pool
# ---------------------------------------------------------------------------
BOOT_POOL_HEALTHY = declare_gauge("BOOT_POOL_HEALTHY", "truenas_boot_pool_healthy", "1 if boot pool is healthy")
BOOT_POOL_STATUS = declare_gauge("BOOT_POOL_STATUS", "truenas_boot_pool_status", "Boot pool status as label", ["status"])
BOOT_POOL_SIZE_BYTES = declare_gauge("BOOT_POOL_SIZE_BYTES", "truenas_boot_pool_size_bytes", "Boot pool total size in bytes")
BOOT_POOL_ALLOCATED_BYTES = declare_gauge("BOOT_POOL_ALLOCATED_BYTES", "truenas_boot_pool_allocated_bytes", "Boot pool allocated bytes")
BOOT_POOL_FREE_BYTES = declare_gauge("BOOT_POOL_FREE_BYTES", "truenas_boot_pool_free_bytes", "Boot pool free bytes")
BOOT_POOL_DISK_COUNT = declare_gauge("BOOT_POOL_DISK_COUNT", "truenas_boot_pool_disk_count", "Number of disks in boot pool")
BOOT_POOL_SCAN_STATE = declare_gauge("BOOT_POOL_SCAN_STATE", "truenas_boot_pool_scan_state", "Boot pool scrub/resilver state as label", ["state"])
BOOT_POOL_SCAN_PERCENT = declare_gauge("BOOT_POOL_SCAN_PERCENT", "truenas_boot_pool_scan_percent", "Boot pool active scan percentage (0 to 100)")

# ---------------------------------------------------------------------------
# Data pools
# ---------------------------------------------------------------------------
POOL_COUNT = declare_gauge("POOL_COUNT", "truenas_pool_count", "Number of pools")
POOL_HEALTHY = declare_gauge("POOL_HEALTHY", "truenas_pool_healthy", "Pool healthy flag (1 healthy, 0 not)", ["pool"])
POOL_STATUS = declare_gauge("POOL_STATUS", "truenas_pool_status", "Pool status enum mapped to 1", ["pool", "status"])
POOL_SIZE_BYTES = declare_gauge("POOL_SIZE_BYTES", "truenas_pool_size_bytes", "Pool total size in bytes", ["pool"])
POOL_ALLOCATED_BYTES = declare_gauge("POOL_ALLOCATED_BYTES", "truenas_pool_allocated_bytes", "Pool allocated bytes", ["pool"])
POOL_FREE_BYTES = declare_gauge("POOL_FREE_BYTES", "truenas_pool_free_bytes", "Pool free bytes", ["pool"])
POOL_SCAN_PERCENT = declare_gauge("POOL_SCAN_PERCENT", "truenas_pool_scan_percent", "Active pool scan/scrub percentage (0 to 100)", ["pool"])
POOL_FRAGMENTATION = declare_gauge("POOL_FRAGMENTATION", "truenas_pool_fragmentation_percent", "Pool fragmentation percentage (0 to 100)", ["pool"])
POOL_AUTOTRIM_ENABLED = declare_gauge("POOL_AUTOTRIM_ENABLED", "truenas_pool_autotrim_enabled", "1 if autotrim is enabled on the pool", ["pool"])
POOL_DEDUP_RATIO = declare_gauge("POOL_DEDUP_RATIO", "truenas_pool_dedup_ratio", "Pool deduplication ratio (1.0 means no dedup savings)", ["pool"])
POOL_EXPAND_SIZE_BYTES = declare_gauge("POOL_EXPAND_SIZE_BYTES", "truenas_pool_expand_size_bytes", "Pool expandable size in bytes", ["pool"])
POOL_DEDUP_TABLE_SIZE_BYTES = declare_gauge("POOL_DEDUP_TABLE_SIZE_BYTES", "truenas_pool_dedup_table_size_bytes", "Size of the pool deduplication table in bytes", ["pool"])
POOL_EXPAND_REFLOWED_BYTES = declare_gauge("POOL_EXPAND_REFLOWED_BYTES", "truenas_pool_expand_reflowed_bytes", "API-reported bytes_reflowed value for the active pool expansion", ["pool"])
POOL_EXPAND_TO_REFLOW_BYTES = declare_gauge("POOL_EXPAND_TO_REFLOW_BYTES", "truenas_pool_expand_to_reflow_bytes", "API-reported bytes_to_reflow value for the active pool expansion", ["pool"])
POOL_EXPAND_PERCENT = declare_gauge("POOL_EXPAND_PERCENT", "truenas_pool_expand_percent", "Active pool expansion completion percentage (0 to 100)", ["pool"])

# ---------------------------------------------------------------------------
# Datasets
# ---------------------------------------------------------------------------
DATASET_COUNT = declare_gauge("DATASET_COUNT", "truenas_dataset_count", "Total number of datasets returned by query")
DATASET_USED_BYTES = declare_gauge("DATASET_USED_BYTES", "truenas_dataset_used_bytes", "Dataset used space in bytes", ["dataset"])
DATASET_AVAILABLE_BYTES = declare_gauge("DATASET_AVAILABLE_BYTES", "truenas_dataset_available_bytes", "Dataset available space in bytes", ["dataset"])
DATASET_REFERENCED_BYTES = declare_gauge("DATASET_REFERENCED_BYTES", "truenas_dataset_referenced_bytes", "Dataset referenced bytes", ["dataset"])
DATASET_QUOTA_BYTES = declare_gauge("DATASET_QUOTA_BYTES", "truenas_dataset_quota_bytes", "Dataset quota in bytes (0 = no quota)", ["dataset"])
DATASET_REFQUOTA_BYTES = declare_gauge("DATASET_REFQUOTA_BYTES", "truenas_dataset_refquota_bytes", "Dataset refquota in bytes (0 = no quota)", ["dataset"])
DATASET_SNAPSHOT_COUNT = declare_gauge("DATASET_SNAPSHOT_COUNT", "truenas_dataset_snapshot_count", "Number of snapshots for dataset", ["dataset"])
DATASET_COMPRESSION_RATIO = declare_gauge("DATASET_COMPRESSION_RATIO", "truenas_dataset_compression_ratio", "Dataset compression ratio", ["dataset"])
DATASET_ENCRYPTED = declare_gauge("DATASET_ENCRYPTED", "truenas_dataset_encrypted", "1 if dataset is encrypted", ["dataset"])
DATASET_RESERVATION_BYTES = declare_gauge("DATASET_RESERVATION_BYTES", "truenas_dataset_reservation_bytes", "Dataset reservation in bytes", ["dataset"])
DATASET_REFRESERVATION_BYTES = declare_gauge("DATASET_REFRESERVATION_BYTES", "truenas_dataset_refreservation_bytes", "Dataset refreservation in bytes", ["dataset"])
DATASET_USED_BY_CHILDREN_BYTES = declare_gauge("DATASET_USED_BY_CHILDREN_BYTES", "truenas_dataset_used_by_children_bytes", "Dataset space used by child datasets in bytes", ["dataset"])
DATASET_USED_BY_DATASET_BYTES = declare_gauge("DATASET_USED_BY_DATASET_BYTES", "truenas_dataset_used_by_dataset_bytes", "Dataset space used by the dataset itself in bytes", ["dataset"])
DATASET_USED_BY_SNAPSHOTS_BYTES = declare_gauge("DATASET_USED_BY_SNAPSHOTS_BYTES", "truenas_dataset_used_by_snapshots_bytes", "Dataset space used by snapshots in bytes", ["dataset"])
DATASET_READONLY = declare_gauge("DATASET_READONLY", "truenas_dataset_readonly", "1 if dataset readonly is enabled", ["dataset"])
DATASET_ATIME = declare_gauge("DATASET_ATIME", "truenas_dataset_atime", "1 if dataset atime updates are enabled", ["dataset"])
DATASET_EXEC = declare_gauge("DATASET_EXEC", "truenas_dataset_exec", "1 if dataset allows executable files", ["dataset"])
DATASET_KEY_LOADED = declare_gauge("DATASET_KEY_LOADED", "truenas_dataset_key_loaded", "1 if encrypted dataset keys are loaded", ["dataset"])
DATASET_LOCKED = declare_gauge("DATASET_LOCKED", "truenas_dataset_locked", "1 if encrypted dataset is locked", ["dataset"])
DATASET_QUOTA_WARNING_PERCENT = declare_gauge("DATASET_QUOTA_WARNING_PERCENT", "truenas_dataset_quota_warning_percent", "Dataset quota warning threshold percentage", ["dataset"])
DATASET_QUOTA_CRITICAL_PERCENT = declare_gauge("DATASET_QUOTA_CRITICAL_PERCENT", "truenas_dataset_quota_critical_percent", "Dataset quota critical threshold percentage", ["dataset"])
DATASET_REFQUOTA_WARNING_PERCENT = declare_gauge("DATASET_REFQUOTA_WARNING_PERCENT", "truenas_dataset_refquota_warning_percent", "Dataset refquota warning threshold percentage", ["dataset"])
DATASET_REFQUOTA_CRITICAL_PERCENT = declare_gauge("DATASET_REFQUOTA_CRITICAL_PERCENT", "truenas_dataset_refquota_critical_percent", "Dataset refquota critical threshold percentage", ["dataset"])
DATASET_CREATION_TS = declare_gauge("DATASET_CREATION_TS", "truenas_dataset_creation_timestamp_seconds", "Dataset creation timestamp as Unix seconds", ["dataset"])

# ---------------------------------------------------------------------------
# Disks
# ---------------------------------------------------------------------------
DISK_COUNT = declare_gauge("DISK_COUNT", "truenas_disk_count", "Number of disks")
DISK_SIZE_BYTES = declare_gauge("DISK_SIZE_BYTES", "truenas_disk_size_bytes", "Disk size in bytes", ["disk"])
DISK_TEMPERATURE_C = declare_gauge("DISK_TEMPERATURE_C", "truenas_disk_temperature_celsius", "Disk temperature in Celsius", ["disk"])
DISK_TEMP_ALERT_COUNT = declare_gauge("DISK_TEMP_ALERT_COUNT", "truenas_disk_temperature_alert_count", "Temperature alert count per disk", ["disk"])
DISK_TEMP_AGG_C = declare_gauge("DISK_TEMP_AGG_C", "truenas_disk_temperature_agg_celsius", "Aggregated disk temperature metrics", ["disk", "kind"])

# ---------------------------------------------------------------------------
# Network
# ---------------------------------------------------------------------------
INTERFACE_COUNT = declare_gauge("INTERFACE_COUNT", "truenas_interface_count", "Number of network interfaces")
INTERFACE_LINK_UP = declare_gauge("INTERFACE_LINK_UP", "truenas_interface_link_up", "1 if interface link is up", ["interface"])
NETWORK_DEFAULT_ROUTES = declare_gauge("NETWORK_DEFAULT_ROUTES", "truenas_network_default_routes", "Number of default routes")
NETWORK_NAMESERVERS = declare_gauge("NETWORK_NAMESERVERS", "truenas_network_nameservers", "Number of configured nameservers")
NETWORK_GATEWAY_REACHABLE = declare_gauge("NETWORK_GATEWAY_REACHABLE", "truenas_network_gateway_reachable", "1 if the default IPv4 gateway is reachable")
NETWORK_DEFAULT_GATEWAY_CONFIGURED = declare_gauge("NETWORK_DEFAULT_GATEWAY_CONFIGURED", "truenas_network_default_gateway_configured", "1 if an applied default network route is configured")

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
SERVICE_COUNT = declare_gauge("SERVICE_COUNT", "truenas_service_count", "Number of services")
SERVICE_ENABLED = declare_gauge("SERVICE_ENABLED", "truenas_service_enabled", "1 if service is enabled", ["service"])
SERVICE_RUNNING = declare_gauge("SERVICE_RUNNING", "truenas_service_running", "1 if service is running", ["service"])

# ---------------------------------------------------------------------------
# NFS / SMB shares
# ---------------------------------------------------------------------------
NFS_SHARE_COUNT = declare_gauge("NFS_SHARE_COUNT", "truenas_nfs_share_count", "Number of configured NFS shares")
SMB_SHARE_COUNT = declare_gauge("SMB_SHARE_COUNT", "truenas_smb_share_count", "Number of configured SMB shares")

# ---------------------------------------------------------------------------
# Alerts
# ---------------------------------------------------------------------------
ALERT_COUNT = declare_gauge("ALERT_COUNT", "truenas_alert_count", "Total number of active alerts")
ALERT_COUNT_BY_LEVEL = declare_gauge("ALERT_COUNT_BY_LEVEL", "truenas_alert_count_by_level", "Alert count by level", ["level"])
ALERT_COUNT_BY_SOURCE = declare_gauge("ALERT_COUNT_BY_SOURCE", "truenas_alert_count_by_source", "Alert count by source component", ["source"])
ALERT_COUNT_BY_CLASS = declare_gauge("ALERT_COUNT_BY_CLASS", "truenas_alert_count_by_class", "Alert count by class and level", ["klass", "level"])
ALERT_COUNT_BY_NODE = declare_gauge("ALERT_COUNT_BY_NODE", "truenas_alert_count_by_node", "Alert count by node", ["node"])
ALERT_DISMISSED_COUNT = declare_gauge("ALERT_DISMISSED_COUNT", "truenas_alert_dismissed_count", "Number of dismissed alerts")
ALERT_ONE_SHOT_COUNT = declare_gauge("ALERT_ONE_SHOT_COUNT", "truenas_alert_one_shot_count", "Number of one-shot alerts")
ALERT_OLDEST_TS = declare_gauge("ALERT_OLDEST_TS", "truenas_alert_oldest_timestamp_seconds", "Unix timestamp of the oldest current alert")
ALERT_LAST_OCCURRENCE_TS = declare_gauge("ALERT_LAST_OCCURRENCE_TS", "truenas_alert_last_occurrence_timestamp_seconds", "Most recent alert occurrence timestamp by level", ["level"])

# ---------------------------------------------------------------------------
# Jobs
# ---------------------------------------------------------------------------
JOB_ACTIVE_COUNT = declare_gauge("JOB_ACTIVE_COUNT", "truenas_job_active_count", "Number of active jobs in WAITING or RUNNING state")
JOB_ACTIVE_COUNT_BY_STATE = declare_gauge("JOB_ACTIVE_COUNT_BY_STATE", "truenas_job_active_count_by_state", "Number of active jobs by state", ["state"])
JOB_ACTIVE_COUNT_BY_METHOD = declare_gauge("JOB_ACTIVE_COUNT_BY_METHOD", "truenas_job_active_count_by_method", "Number of active jobs by method and state", ["method", "state"])
JOB_ABORTABLE_ACTIVE_COUNT = declare_gauge("JOB_ABORTABLE_ACTIVE_COUNT", "truenas_job_abortable_active_count", "Number of active abortable jobs")
JOB_TRANSIENT_ACTIVE_COUNT = declare_gauge("JOB_TRANSIENT_ACTIVE_COUNT", "truenas_job_transient_active_count", "Number of active transient jobs")
JOB_OLDEST_ACTIVE_TS = declare_gauge("JOB_OLDEST_ACTIVE_TS", "truenas_job_oldest_active_timestamp_seconds", "Unix timestamp of the oldest active job by state", ["state"])
JOB_PROGRESS_PERCENT = declare_gauge("JOB_PROGRESS_PERCENT", "truenas_job_progress_percent", "Maximum running job progress percent by method", ["method"])

# ---------------------------------------------------------------------------
# Updates
# ---------------------------------------------------------------------------
UPDATE_STATUS = declare_gauge("UPDATE_STATUS", "truenas_update_status", "Update status as label with value 1", ["status"])
UPDATE_AVAILABLE = declare_gauge("UPDATE_AVAILABLE", "truenas_update_available", "1 if an update is available")

# ---------------------------------------------------------------------------
# Certificates
# ---------------------------------------------------------------------------
CERT_COUNT = declare_gauge("CERT_COUNT", "truenas_certificate_count", "Number of certificates")
CERT_DAYS_TO_EXPIRY = declare_gauge("CERT_DAYS_TO_EXPIRY", 
    "truenas_certificate_days_to_expiry",
    "Days until certificate expires (negative = already expired)",
    ["name", "issuer"],
)
CERT_EXPIRY_TIMESTAMP_SECONDS = declare_gauge(
    "CERT_EXPIRY_TIMESTAMP_SECONDS",
    "truenas_certificate_expiry_timestamp_seconds",
    "Certificate expiry time as a Unix timestamp",
    ["name"],
)

# ---------------------------------------------------------------------------
# Directory services
# ---------------------------------------------------------------------------
DIRECTORYSERVICES_HEALTHY = declare_gauge("DIRECTORYSERVICES_HEALTHY", 
    "truenas_directoryservices_healthy",
    "1 if directory service appears healthy",
    ["service"],
)
DIRECTORYSERVICES_STATUS = declare_gauge("DIRECTORYSERVICES_STATUS", 
    "truenas_directoryservices_status",
    "Directory service status as label",
    ["service", "status"],
)
DIRECTORYSERVICES_FAULT_REASON = declare_gauge("DIRECTORYSERVICES_FAULT_REASON", 
    "truenas_directoryservices_fault_reason",
    "Directory service fault reason as label",
    ["service", "reason"],
)

# ---------------------------------------------------------------------------
# Docker / Apps
# ---------------------------------------------------------------------------
DOCKER_NVIDIA_PRESENT = declare_gauge("DOCKER_NVIDIA_PRESENT", "truenas_docker_nvidia_present", "1 if NVIDIA GPU is present for Docker")
DOCKER_NETWORK_COUNT = declare_gauge("DOCKER_NETWORK_COUNT", "truenas_docker_network_count", "Number of Docker networks")
DOCKER_STATUS = declare_gauge("DOCKER_STATUS", "truenas_docker_status", "Docker daemon status", ["status"])
APP_COUNT = declare_gauge("APP_COUNT", "truenas_app_count", "Number of applications")
APP_STATE = declare_gauge("APP_STATE", "truenas_app_state", "Per-app state as label — always 1", ["app", "state"])
APP_UPGRADE_AVAILABLE = declare_gauge("APP_UPGRADE_AVAILABLE", "truenas_app_upgrade_available", "1 if an app upgrade is available", ["app"])
APP_IMAGE_UPDATES_AVAILABLE = declare_gauge("APP_IMAGE_UPDATES_AVAILABLE", "truenas_app_image_updates_available", "1 if updated app container images are available", ["app"])
APP_CUSTOM = declare_gauge("APP_CUSTOM", "truenas_app_custom", "1 if the app is a custom app", ["app"])
APP_MIGRATED = declare_gauge("APP_MIGRATED", "truenas_app_migrated", "1 if the app was migrated from Kubernetes", ["app"])
APP_CONTAINER_COUNT = declare_gauge("APP_CONTAINER_COUNT", "truenas_app_container_count", "Number of active containers for an app", ["app"])
APP_USED_PORT_COUNT = declare_gauge("APP_USED_PORT_COUNT", "truenas_app_used_port_count", "Number of active workload port mappings for an app", ["app"])
APP_USED_HOST_IP_COUNT = declare_gauge("APP_USED_HOST_IP_COUNT", "truenas_app_used_host_ip_count", "Number of host IPs used by an app", ["app"])
APP_CONTAINER_STATE_COUNT = declare_gauge("APP_CONTAINER_STATE_COUNT", "truenas_app_container_state_count", "Count of app containers by runtime state", ["app", "state"])

# ---------------------------------------------------------------------------
# NFS / iSCSI client counts (dedicated gauges)
# ---------------------------------------------------------------------------
NFS_CLIENT_COUNT = declare_gauge("NFS_CLIENT_COUNT", "truenas_nfs_client_count", "Number of NFS clients")
NFS_V3_CLIENT_COUNT = declare_gauge("NFS_V3_CLIENT_COUNT", "truenas_nfs_v3_client_count", "Number of active NFSv3 clients")
NFS_V4_CLIENT_COUNT = declare_gauge("NFS_V4_CLIENT_COUNT", "truenas_nfs_v4_client_count", "Number of active NFSv4 clients")
ISCSI_CLIENT_COUNT = declare_gauge("ISCSI_CLIENT_COUNT", "truenas_iscsi_client_count", "Number of iSCSI clients")

# ---------------------------------------------------------------------------
# Interface extras (MTU, type)
# ---------------------------------------------------------------------------
INTERFACE_MTU = declare_gauge("INTERFACE_MTU", "truenas_interface_mtu", "Interface MTU in bytes", ["interface"])
INTERFACE_TYPE = declare_gauge("INTERFACE_TYPE", "truenas_interface_type", "Interface type (PHYSICAL/BRIDGE/etc)", ["interface", "type"])

# ---------------------------------------------------------------------------
# VMs
# ---------------------------------------------------------------------------
VM_COUNT = declare_gauge("VM_COUNT", "truenas_vm_count", "Number of virtual machines")
VM_AVAILABLE_MEMORY_BYTES = declare_gauge("VM_AVAILABLE_MEMORY_BYTES", "truenas_vm_available_memory_bytes", "Available memory for VMs")
VM_VMEMORY_IN_USE_BYTES = declare_gauge("VM_VMEMORY_IN_USE_BYTES", "truenas_vm_vmemory_in_use_bytes", "Virtual memory in use by VMs in bytes", ["state"])

# ---------------------------------------------------------------------------
# Tasks (replication, cloudsync, rsync, snapshot)
# ---------------------------------------------------------------------------
TASK_ENABLED = declare_gauge("TASK_ENABLED", "truenas_task_enabled", "1 if task is enabled", ["task_type", "name"])
TASK_STATE = declare_gauge("TASK_STATE", 
    "truenas_task_state",
    "Task last run state as label with value 1",
    ["task_type", "name", "state"],
)
TASK_LAST_RUN_TS = declare_gauge("TASK_LAST_RUN_TS", 
    "truenas_task_last_run_timestamp_seconds",
    "Unix timestamp of task last run completion",
    ["task_type", "name"],
)
TASK_COUNT = declare_gauge("TASK_COUNT", "truenas_task_count", "Number of configured tasks", ["task_type"])

# Snapshot task limits
SNAPSHOT_TASK_MAX_COUNT = declare_gauge("SNAPSHOT_TASK_MAX_COUNT", "truenas_snapshot_task_max_count", "Maximum number of snapshot tasks allowed")
SNAPSHOT_TASK_MAX_TOTAL_COUNT = declare_gauge("SNAPSHOT_TASK_MAX_TOTAL_COUNT", "truenas_snapshot_task_max_total_count", "Maximum total snapshot tasks allowed")

# ---------------------------------------------------------------------------
# IPMI
# ---------------------------------------------------------------------------
IPMI_LOADED = declare_gauge("IPMI_LOADED", "truenas_ipmi_loaded", "1 if IPMI kernel module is loaded")
IPMI_CHASSIS_POWER_ON = declare_gauge("IPMI_CHASSIS_POWER_ON", "truenas_ipmi_chassis_power_on", "1 if chassis power is on")
IPMI_CHASSIS_POWER_OVERLOAD = declare_gauge("IPMI_CHASSIS_POWER_OVERLOAD", "truenas_ipmi_chassis_power_overload", "1 if power overload detected")
IPMI_CHASSIS_INTRUSION = declare_gauge("IPMI_CHASSIS_INTRUSION", "truenas_ipmi_chassis_intrusion", "1 if chassis intrusion detected")
IPMI_CHASSIS_DRIVE_FAULT = declare_gauge("IPMI_CHASSIS_DRIVE_FAULT", "truenas_ipmi_chassis_drive_fault", "1 if drive fault detected")
IPMI_CHASSIS_FAN_FAULT = declare_gauge("IPMI_CHASSIS_FAN_FAULT", "truenas_ipmi_chassis_fan_fault", "1 if fan fault detected")
IPMI_SEL_ENTRY_COUNT = declare_gauge("IPMI_SEL_ENTRY_COUNT", "truenas_ipmi_sel_entry_count", "Number of entries in IPMI System Event Log")
IPMI_SEL_FREE_SPACE_BYTES = declare_gauge("IPMI_SEL_FREE_SPACE_BYTES", "truenas_ipmi_sel_free_space_bytes", "Free space in IPMI SEL in bytes")

# ---------------------------------------------------------------------------
# HA failover
# ---------------------------------------------------------------------------
FAILOVER_DISABLED_REASON_COUNT = declare_gauge("FAILOVER_DISABLED_REASON_COUNT", 
    "truenas_failover_disabled_reason_count",
    "Number of reasons HA failover is currently disabled",
)
FAILOVER_DISABLED_REASON = declare_gauge("FAILOVER_DISABLED_REASON", 
    "truenas_failover_disabled_reason",
    "HA failover disabled reason as label with value 1",
    ["reason"],
)

# ---------------------------------------------------------------------------
# System extras (version, product type, identity)
# ---------------------------------------------------------------------------
SYSTEM_PRODUCT_TYPE = declare_gauge("SYSTEM_PRODUCT_TYPE", "truenas_system_product_type", "System product type as label", ["product_type"])
SYSTEM_VERSION = declare_gauge("SYSTEM_VERSION", "truenas_system_version", "TrueNAS version as label", ["version"])
# System identity — host_id is stable (safe label); boot_id changes every reboot so
# we track it as a Counter increment rather than a UUID label, which would create
# a new zombie series in Prometheus after every reboot.
SYSTEM_HOST_ID = declare_gauge("SYSTEM_HOST_ID", 
    "truenas_system_host_id",
    "Always 1; host_id label is a stable UUID, does not change between reboots",
    ["host_id"],
)
SYSTEM_BOOT_CHANGES_TOTAL = declare_counter("SYSTEM_BOOT_CHANGES_TOTAL", 
    "truenas_system_boot_changes_total",
    "Number of boot ID changes detected since exporter start (proxy for reboot count)",
)
SYSTEM_MANAGED_BY_TRUECOMMAND = declare_gauge("SYSTEM_MANAGED_BY_TRUECOMMAND", "truenas_managed_by_truecommand", "1 if managed by TrueCommand")

# ---------------------------------------------------------------------------
# Update extras
# ---------------------------------------------------------------------------
UPDATE_VERSION_AVAILABLE = declare_gauge("UPDATE_VERSION_AVAILABLE", "truenas_update_version_available", "1 = version available", ["version"])

# ---------------------------------------------------------------------------
# Boot environments
# ---------------------------------------------------------------------------
BOOT_ENV_COUNT = declare_gauge("BOOT_ENV_COUNT", "truenas_boot_env_count", "Total number of boot environments")
BOOT_ENV_ACTIVE_COUNT = declare_gauge("BOOT_ENV_ACTIVE_COUNT", "truenas_boot_env_active_count", "Number of active boot environments")
BOOT_ENV_KEEP_COUNT = declare_gauge("BOOT_ENV_KEEP_COUNT", "truenas_boot_env_keep_count", "Number of boot environments marked keep=true")
BOOT_ENV_SIZE_BYTES = declare_gauge("BOOT_ENV_SIZE_BYTES", "truenas_boot_env_size_bytes", "Size of boot environment in bytes", ["name"])
BOOT_ENV_ACTIVE = declare_gauge("BOOT_ENV_ACTIVE", "truenas_boot_env_active", "1 if boot environment is active", ["name"])
BOOT_ENV_KEEP = declare_gauge("BOOT_ENV_KEEP", "truenas_boot_env_keep", "1 if boot environment is marked keep", ["name"])
BOOT_ENV_ACTIVATED = declare_gauge("BOOT_ENV_ACTIVATED", "truenas_boot_env_activated", "1 if boot environment is selected for the next boot", ["name"])
BOOT_ENV_ACTIVATED_COUNT = declare_gauge("BOOT_ENV_ACTIVATED_COUNT", "truenas_boot_env_activated_count", "Number of boot environments selected for the next boot")
BOOT_ENV_USED_BYTES = declare_gauge(
    "BOOT_ENV_USED_BYTES",
    "truenas_boot_environment_used_bytes",
    "Bytes used by the boot environment",
    ["name"],
)

# ---------------------------------------------------------------------------
# VM / Virtualization extras
# ---------------------------------------------------------------------------
VM_SUPPORTS_VIRTUALIZATION = declare_gauge("VM_SUPPORTS_VIRTUALIZATION", "truenas_vm_supports_virtualization", "1 if KVM/hardware virt is available")
VM_MAX_VCPUS = declare_gauge("VM_MAX_VCPUS", "truenas_vm_maximum_supported_vcpus", "Maximum vCPUs the system can offer")
HW_VIRT_VARIANT = declare_gauge("HW_VIRT_VARIANT", "truenas_hw_virt_variant", "Hardware virtualization variant", ["variant"])
VM_FLAG_INTEL_VMX = declare_gauge("VM_FLAG_INTEL_VMX", "truenas_vm_flag_intel_vmx", "1 if Intel VT-x/VMX flag is present")
VM_FLAG_AMD_RVI = declare_gauge("VM_FLAG_AMD_RVI", "truenas_vm_flag_amd_rvi", "1 if AMD RVI/NPT flag is present")
VM_FLAG_UNRESTRICTED_GUEST = declare_gauge("VM_FLAG_UNRESTRICTED_GUEST", 
    "truenas_vm_flag_unrestricted_guest",
    "1 if unrestricted guest support is present",
)
VM_FLAG_AMD_ASIDS = declare_gauge("VM_FLAG_AMD_ASIDS", "truenas_vm_flag_amd_asids", "Number of AMD ASIDs when reported")
VM_FLAG_AMD_ASIDS_SUPPORTED = declare_gauge("VM_FLAG_AMD_ASIDS_SUPPORTED", "truenas_vm_flag_amd_asids_supported", "1 if AMD Address Space Identifiers are supported")
VM_VIRTUALIZATION_DETAILS_SUPPORTED = declare_gauge("VM_VIRTUALIZATION_DETAILS_SUPPORTED", 
    "truenas_vm_virtualization_details_supported",
    "1 if vm.virtualization_details reports virtualization support",
)
VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT = declare_gauge("VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT", 
    "truenas_vm_virtualization_details_error_present",
    "1 if vm.virtualization_details reports an error",
)

# ---------------------------------------------------------------------------
# Virt (Incus/LXD — TrueNAS 25.x new resource type)
# ---------------------------------------------------------------------------
VIRT_INSTANCE_COUNT = declare_gauge("VIRT_INSTANCE_COUNT", "truenas_virt_instance_count", "Number of Incus/LXD virtual instances")
VIRT_INSTANCE_RUNNING = declare_gauge("VIRT_INSTANCE_RUNNING", "truenas_virt_instance_running", "1 if Incus instance is running", ["name", "type"])
VIRT_INSTANCE_CPU = declare_gauge("VIRT_INSTANCE_CPU", "truenas_virt_instance_cpu_usage_percent", "Incus instance CPU usage %", ["name"])
VIRT_INSTANCE_MEM = declare_gauge("VIRT_INSTANCE_MEM", "truenas_virt_instance_mem_bytes", "Incus instance memory usage bytes", ["name"])
VIRT_VOLUME_COUNT = declare_gauge("VIRT_VOLUME_COUNT", "truenas_virt_volume_count", "Number of Incus storage volumes")
VIRT_VOLUME_SIZE_BYTES = declare_gauge("VIRT_VOLUME_SIZE_BYTES", "truenas_virt_volume_size_bytes", "Incus volume size bytes", ["name", "pool"])
VIRT_GLOBAL_STATE = declare_gauge("VIRT_GLOBAL_STATE", "truenas_virt_global_state", "Virt/Incus global state", ["state"])

# ---------------------------------------------------------------------------
# Fibre Channel
# ---------------------------------------------------------------------------
FC_HOST_COUNT = declare_gauge("FC_HOST_COUNT", "truenas_fc_host_count", "Number of Fibre Channel host adapters")
FC_PORT_COUNT = declare_gauge("FC_PORT_COUNT", "truenas_fc_port_count", "Number of Fibre Channel ports")
FC_PORT_SPEED = declare_gauge("FC_PORT_SPEED", "truenas_fc_port_speed_gbit", "FC port link speed in Gbit/s", ["port"])
FC_PORT_ONLINE = declare_gauge("FC_PORT_ONLINE", "truenas_fc_port_online", "1 if FC port is online", ["port"])

# ---------------------------------------------------------------------------
# NVMe-oF
# ---------------------------------------------------------------------------
NVMET_SESSION_COUNT = declare_gauge("NVMET_SESSION_COUNT", "truenas_nvmet_session_count", "Number of active NVMe-oF sessions")
NVMET_SUBSYS_COUNT = declare_gauge("NVMET_SUBSYS_COUNT", "truenas_nvmet_subsys_count", "Number of NVMe-oF subsystems")
NVMET_PORT_COUNT = declare_gauge("NVMET_PORT_COUNT", "truenas_nvmet_port_count", "Number of NVMe-oF ports")

# ---------------------------------------------------------------------------
# iSCSI protocol extras
# ---------------------------------------------------------------------------
ISCSI_ALUA_ENABLED = declare_gauge("ISCSI_ALUA_ENABLED", "truenas_iscsi_alua_enabled", "1 if iSCSI ALUA protocol is enabled")
ISCSI_ISER_ENABLED = declare_gauge("ISCSI_ISER_ENABLED", "truenas_iscsi_iser_enabled", "1 if iSCSI iSER (RDMA) protocol is enabled")
ISCSI_SESSION_COUNT = declare_gauge("ISCSI_SESSION_COUNT", "truenas_iscsi_session_count", "Number of active iSCSI sessions")
ISCSI_SESSION_ISER_COUNT = declare_gauge("ISCSI_SESSION_ISER_COUNT", 
    "truenas_iscsi_session_iser_count",
    "Number of active iSCSI sessions using iSER",
)
ISCSI_SESSION_OFFLOAD_COUNT = declare_gauge("ISCSI_SESSION_OFFLOAD_COUNT", 
    "truenas_iscsi_session_offload_count",
    "Number of active iSCSI sessions using offload",
)
ISCSI_SESSION_IMMEDIATE_DATA_COUNT = declare_gauge("ISCSI_SESSION_IMMEDIATE_DATA_COUNT", 
    "truenas_iscsi_session_immediate_data_count",
    "Number of active iSCSI sessions with immediate-data enabled",
)

# ---------------------------------------------------------------------------
# Network extras
# ---------------------------------------------------------------------------
INTERFACE_HAS_PENDING_CHANGES = declare_gauge("INTERFACE_HAS_PENDING_CHANGES", "truenas_interface_has_pending_changes", "1 if there are uncommitted network configuration changes")
INTERFACE_CHECKIN_WAITING_SECONDS = declare_gauge("INTERFACE_CHECKIN_WAITING_SECONDS", "truenas_interface_checkin_waiting_seconds", "Seconds until pending network changes auto-rollback (0 = no rollback pending)")

# ---------------------------------------------------------------------------
# App extras
# ---------------------------------------------------------------------------
APP_AVAILABLE_SPACE_BYTES = declare_gauge("APP_AVAILABLE_SPACE_BYTES", "truenas_app_available_space_bytes", "Bytes available for new app installs")
APP_WEBDAV_SHARE_COUNT = declare_gauge("APP_WEBDAV_SHARE_COUNT", "truenas_webdav_share_count", "Number of WebDAV (WebShare) shares")
WEBSHARE_ENABLED = declare_gauge("WEBSHARE_ENABLED", "truenas_webshare_enabled", "1 if WebShare passkey authentication is enabled (v26+)")

# ---------------------------------------------------------------------------
# UPS
# ---------------------------------------------------------------------------
UPS_STATUS = declare_gauge("UPS_STATUS", "truenas_ups_status", "UPS status string as label", ["status"])
UPS_CONFIGURED = declare_gauge("UPS_CONFIGURED", "truenas_ups_configured", "1 if a UPS device is configured")

# ---------------------------------------------------------------------------
# Catalog
# ---------------------------------------------------------------------------
CATALOG_TRAIN_COUNT = declare_gauge("CATALOG_TRAIN_COUNT", "truenas_catalog_train_count", "Number of app catalog trains available")
CATALOG_CONFIG_PRESENT = declare_gauge("CATALOG_CONFIG_PRESENT", "truenas_catalog_config_present", "1 if catalog.config returned a config payload")
CATALOG_PREFERRED_TRAIN_COUNT = declare_gauge("CATALOG_PREFERRED_TRAIN_COUNT", 
    "truenas_catalog_preferred_train_count",
    "Number of preferred catalog trains configured",
)

# ---------------------------------------------------------------------------
# Security / FIPS
# ---------------------------------------------------------------------------
FIPS_AVAILABLE = declare_gauge("FIPS_AVAILABLE", "truenas_fips_available", "1 if FIPS is available on this system")
FIPS_ENABLED = declare_gauge("FIPS_ENABLED", "truenas_fips_enabled", "1 if FIPS mode is currently enabled")

# ---------------------------------------------------------------------------
# Feature flags
# ---------------------------------------------------------------------------
FEATURE_ENABLED = declare_gauge("FEATURE_ENABLED", "truenas_feature_enabled", "1 if feature is enabled", ["feature"])

# ---------------------------------------------------------------------------
# Hardware / Chassis
# ---------------------------------------------------------------------------
CHASSIS_HARDWARE = declare_gauge("CHASSIS_HARDWARE", "truenas_chassis_hardware", "Chassis hardware model", ["model"])

# ---------------------------------------------------------------------------
# TrueNAS Connect (cloud management)
# ---------------------------------------------------------------------------
TN_CONNECT_ENABLED = declare_gauge("TN_CONNECT_ENABLED", "truenas_tn_connect_enabled", "1 if TrueNAS Connect is enabled")
TN_CONNECT_STATUS = declare_gauge("TN_CONNECT_STATUS", "truenas_tn_connect_status", "TrueNAS Connect status", ["status"])

# ---------------------------------------------------------------------------
# TrueCommand (full status)
# ---------------------------------------------------------------------------
TRUECOMMAND_STATUS = declare_gauge("TRUECOMMAND_STATUS", "truenas_truecommand_status", "TrueCommand connection status", ["status"])

# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------
AUDIT_DATASET_USED_BYTES = declare_gauge("AUDIT_DATASET_USED_BYTES", "truenas_audit_dataset_used_bytes", "Audit dataset used space in bytes")
AUDIT_DATASET_AVAILABLE_BYTES = declare_gauge("AUDIT_DATASET_AVAILABLE_BYTES", "truenas_audit_dataset_available_bytes", "Audit dataset available space in bytes")
AUDIT_QUOTA_FILL_WARNING_PERCENT = declare_gauge("AUDIT_QUOTA_FILL_WARNING_PERCENT", "truenas_audit_quota_fill_warning_percent", "Audit quota fill warning threshold percentage")
AUDIT_QUOTA_FILL_CRITICAL_PERCENT = declare_gauge("AUDIT_QUOTA_FILL_CRITICAL_PERCENT", "truenas_audit_quota_fill_critical_percent", "Audit quota fill critical threshold percentage")
AUDIT_RETENTION_DAYS = declare_gauge("AUDIT_RETENTION_DAYS", "truenas_audit_retention_days", "Configured local audit retention in days")
AUDIT_RESERVATION_BYTES = declare_gauge("AUDIT_RESERVATION_BYTES", "truenas_audit_reservation_bytes", "Configured audit dataset reservation in bytes")
AUDIT_QUOTA_BYTES = declare_gauge("AUDIT_QUOTA_BYTES", "truenas_audit_quota_bytes", "Configured audit dataset quota in bytes")
AUDIT_REMOTE_LOGGING_ENABLED = declare_gauge("AUDIT_REMOTE_LOGGING_ENABLED", "truenas_audit_remote_logging_enabled", "1 if remote audit logging is enabled")

# ---------------------------------------------------------------------------
# Pool warnings
# ---------------------------------------------------------------------------
POOL_WARNING = declare_gauge("POOL_WARNING", "truenas_pool_warning", "Pool warning flag (1 if warning present)", ["pool"])

# ---------------------------------------------------------------------------
# Filesystem paths
# ---------------------------------------------------------------------------
FILESYSTEM_PATH_COUNT = declare_gauge("FILESYSTEM_PATH_COUNT", "truenas_filesystem_path_count", "Number of filesystem paths being scraped")

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
METHOD_NUMERIC_VALUE = declare_gauge("METHOD_NUMERIC_VALUE", "truenas_method_numeric_value", "Numeric value from method result", ["method", "path"])
METHOD_BOOLEAN_VALUE = declare_gauge("METHOD_BOOLEAN_VALUE", "truenas_method_boolean_value", "Boolean value from method result (1/0)", ["method", "path"])
METHOD_STATUS_VALUE = declare_gauge("METHOD_STATUS_VALUE", "truenas_method_status_value", "Status string from method result", ["method", "path", "status"])
METHOD_LIST_LENGTH = declare_gauge("METHOD_LIST_LENGTH", "truenas_method_list_length", "List length from method result", ["method", "path"])

# ---------------------------------------------------------------------------
# Event stream metrics
# ---------------------------------------------------------------------------
EVENT_STREAM_UP = declare_gauge("EVENT_STREAM_UP", "truenas_event_stream_up", "1 when event subscription is active", ["event"])
EVENT_LAST_MESSAGE_TS = declare_gauge("EVENT_LAST_MESSAGE_TS", "truenas_event_last_message_timestamp_seconds", "Last event message timestamp", ["event"])
EVENT_MESSAGES_TOTAL = declare_counter("EVENT_MESSAGES_TOTAL", "truenas_event_messages_total", "Total event messages received", ["event"])
EVENT_NUMERIC_VALUE = declare_gauge("EVENT_NUMERIC_VALUE", "truenas_event_numeric_value", "Numeric values from event payload", ["event", "path"])
EVENT_BOOLEAN_VALUE = declare_gauge("EVENT_BOOLEAN_VALUE", "truenas_event_boolean_value", "Boolean values from event payload (1/0)", ["event", "path"])
EVENT_STATUS_VALUE = declare_gauge("EVENT_STATUS_VALUE", "truenas_event_status_value", "Status values from event payload", ["event", "path", "status"])
EVENT_LIST_LENGTH = declare_gauge("EVENT_LIST_LENGTH", "truenas_event_list_length", "List length from event payload", ["event", "path"])

# ---------------------------------------------------------------------------
# Realtime host metrics (from reporting.realtime event stream)
# These provide live CPU / RAM / disk I/O / network / ZFS ARC readings.
# ---------------------------------------------------------------------------

# CPU usage (updated every time a reporting.realtime event arrives, ~1s interval)
CPU_USAGE_PERCENT = declare_gauge("CPU_USAGE_PERCENT", "truenas_cpu_usage_percent", "Total host CPU usage percent (0 to 100, all cores combined)")
CPU_USER_PERCENT = declare_gauge("CPU_USER_PERCENT", "truenas_cpu_user_percent", "Host CPU user-space usage percent (0 to 100); falls back to total CPU usage when user split is unavailable")
CPU_SYSTEM_PERCENT = declare_gauge("CPU_SYSTEM_PERCENT", "truenas_cpu_system_percent", "Host CPU kernel usage percent (0 to 100)")
CPU_IOWAIT_PERCENT = declare_gauge("CPU_IOWAIT_PERCENT", "truenas_cpu_iowait_percent", "Host CPU I/O wait percent (0 to 100)")
CPU_IDLE_PERCENT = declare_gauge("CPU_IDLE_PERCENT", "truenas_cpu_idle_percent", "Host CPU idle percent (0 to 100); inferred as 100-total usage when idle split is unavailable")
CPU_INTERRUPT_PERCENT = declare_gauge("CPU_INTERRUPT_PERCENT", "truenas_cpu_interrupt_percent", "Host CPU interrupt/hardware IRQ percent (0 to 100)")
CPU_CORE_USAGE_PERCENT = declare_gauge("CPU_CORE_USAGE_PERCENT", "truenas_cpu_core_usage_percent", "Per-CPU-core usage percent (0 to 100)", ["core"])
CPU_TEMPERATURE_C = declare_gauge("CPU_TEMPERATURE_C", "truenas_cpu_temperature_celsius", "Per-CPU-core temperature in Celsius", ["core"])

# Memory (live values from reporting.realtime)
MEMORY_PHYSICAL_TOTAL_BYTES = declare_gauge("MEMORY_PHYSICAL_TOTAL_BYTES", "truenas_memory_physical_total_bytes", "Total physical RAM in bytes")
MEMORY_PHYSICAL_AVAILABLE_BYTES = declare_gauge("MEMORY_PHYSICAL_AVAILABLE_BYTES", "truenas_memory_physical_available_bytes", "Available physical RAM in bytes")
MEMORY_PHYSICAL_FREE_BYTES = declare_gauge("MEMORY_PHYSICAL_FREE_BYTES", "truenas_memory_physical_free_bytes", "Free physical RAM in bytes")
MEMORY_PHYSICAL_CACHED_BYTES = declare_gauge("MEMORY_PHYSICAL_CACHED_BYTES", "truenas_memory_physical_cached_bytes", "Page cache bytes")
MEMORY_PHYSICAL_BUFFERS_BYTES = declare_gauge("MEMORY_PHYSICAL_BUFFERS_BYTES", "truenas_memory_physical_buffers_bytes", "Buffer cache bytes")
MEMORY_PHYSICAL_USED_BYTES = declare_gauge("MEMORY_PHYSICAL_USED_BYTES", "truenas_memory_physical_used_bytes", "Used physical RAM in bytes (total - available)")
MEMORY_SWAP_TOTAL_BYTES = declare_gauge("MEMORY_SWAP_TOTAL_BYTES", "truenas_memory_swap_total_bytes", "Swap total in bytes")
MEMORY_SWAP_FREE_BYTES = declare_gauge("MEMORY_SWAP_FREE_BYTES", "truenas_memory_swap_free_bytes", "Swap free in bytes")
MEMORY_SWAP_USED_BYTES = declare_gauge("MEMORY_SWAP_USED_BYTES", "truenas_memory_swap_used_bytes", "Swap used in bytes")

# Disk I/O rates (per disk, from reporting.realtime)
DISK_READ_BYTES_RATE = declare_gauge("DISK_READ_BYTES_RATE", "truenas_disk_read_bytes_per_second", "Disk read throughput in bytes/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_WRITE_BYTES_RATE = declare_gauge("DISK_WRITE_BYTES_RATE", "truenas_disk_write_bytes_per_second", "Disk write throughput in bytes/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_READ_OPS_RATE = declare_gauge("DISK_READ_OPS_RATE", "truenas_disk_read_ops_per_second", "Disk read operations/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_WRITE_OPS_RATE = declare_gauge("DISK_WRITE_OPS_RATE", "truenas_disk_write_ops_per_second", "Disk write operations/sec (instantaneous snapshot from realtime API)", ["disk"])
DISK_BUSY_PERCENT = declare_gauge("DISK_BUSY_PERCENT", "truenas_disk_busy_percent", "Disk busy percentage (0–100)", ["disk"])

# Network I/O rates (per interface, from reporting.realtime)
NETWORK_RX_BYTES_RATE = declare_gauge("NETWORK_RX_BYTES_RATE", "truenas_network_rx_bytes_per_second", "Network interface receive bytes/sec (instantaneous snapshot from realtime API)", ["interface"])
NETWORK_TX_BYTES_RATE = declare_gauge("NETWORK_TX_BYTES_RATE", "truenas_network_tx_bytes_per_second", "Network interface transmit bytes/sec (instantaneous snapshot from realtime API)", ["interface"])

# ZFS ARC (from reporting.realtime or memory/zfs subsection in v25)
ZFS_ARC_SIZE_BYTES = declare_gauge("ZFS_ARC_SIZE_BYTES", "truenas_zfs_arc_size_bytes", "ZFS ARC current size in bytes")
ZFS_ARC_MAX_SIZE_BYTES = declare_gauge("ZFS_ARC_MAX_SIZE_BYTES", "truenas_zfs_arc_max_size_bytes", "ZFS ARC maximum allowed size in bytes")
ZFS_ARC_MIN_SIZE_BYTES = declare_gauge("ZFS_ARC_MIN_SIZE_BYTES", "truenas_zfs_arc_min_size_bytes", "ZFS ARC minimum size in bytes")
ZFS_ARC_HIT_RATIO = declare_gauge("ZFS_ARC_HIT_RATIO", "truenas_zfs_arc_hit_ratio", "ZFS ARC cache hit ratio (0.0–1.0)")
ZFS_ARC_HITS_RATE = declare_gauge("ZFS_ARC_HITS_RATE", "truenas_zfs_arc_hits_per_second", "ZFS ARC hits per second (instantaneous snapshot from realtime API)")
ZFS_ARC_MISSES_RATE = declare_gauge("ZFS_ARC_MISSES_RATE", "truenas_zfs_arc_misses_per_second", "ZFS ARC misses per second (instantaneous snapshot from realtime API)")

# ZFS ARC v25+ (from memory section in v25.10)
ZFS_ARC_FREE_MEMORY_BYTES = declare_gauge("ZFS_ARC_FREE_MEMORY_BYTES", "truenas_zfs_arc_free_memory_bytes", "ZFS ARC free memory in bytes (v25+)")
ZFS_ARC_AVAILABLE_BYTES = declare_gauge("ZFS_ARC_AVAILABLE_BYTES", "truenas_zfs_arc_available_bytes", "ZFS ARC available memory in bytes (v25+)")

# ZFS demand data stats (v25+)
ZFS_DEMAND_DATA_ACCESSES_RATE = declare_gauge("ZFS_DEMAND_DATA_ACCESSES_RATE", "truenas_zfs_demand_data_accesses_per_second", "ZFS demand data accesses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_HITS_RATE = declare_gauge("ZFS_DEMAND_DATA_HITS_RATE", "truenas_zfs_demand_data_hits_per_second", "ZFS demand data hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_MISSES_RATE = declare_gauge("ZFS_DEMAND_DATA_MISSES_RATE", "truenas_zfs_demand_data_misses_per_second", "ZFS demand data misses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_HIT_RATIO = declare_gauge("ZFS_DEMAND_DATA_HIT_RATIO", "truenas_zfs_demand_data_hit_ratio", "ZFS demand data hit ratio (0.0-1.0)")
ZFS_DEMAND_DATA_IO_HIT_RATIO = declare_gauge("ZFS_DEMAND_DATA_IO_HIT_RATIO", "truenas_zfs_demand_data_io_hit_ratio", "ZFS demand data IO hit ratio (0.0-1.0)")
ZFS_DEMAND_DATA_MISS_RATIO = declare_gauge("ZFS_DEMAND_DATA_MISS_RATIO", "truenas_zfs_demand_data_miss_ratio", "ZFS demand data miss ratio (0.0-1.0)")

# ZFS demand metadata stats (v25+)
ZFS_DEMAND_META_HITS_RATE = declare_gauge("ZFS_DEMAND_META_HITS_RATE", "truenas_zfs_demand_meta_hits_per_second", "ZFS demand metadata hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_MISSES_RATE = declare_gauge("ZFS_DEMAND_META_MISSES_RATE", "truenas_zfs_demand_meta_misses_per_second", "ZFS demand metadata misses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_HIT_RATIO = declare_gauge("ZFS_DEMAND_META_HIT_RATIO", "truenas_zfs_demand_meta_hit_ratio", "ZFS demand metadata hit ratio (0.0-1.0)")

# L2ARC cache stats (v25+)
ZFS_L2ARC_HITS_RATE = declare_gauge("ZFS_L2ARC_HITS_RATE", "truenas_zfs_l2arc_hits_per_second", "L2ARC cache hits per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_MISSES_RATE = declare_gauge("ZFS_L2ARC_MISSES_RATE", "truenas_zfs_l2arc_misses_per_second", "L2ARC cache misses per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_HIT_RATIO = declare_gauge("ZFS_L2ARC_HIT_RATIO", "truenas_zfs_l2arc_hit_ratio", "L2ARC cache hit ratio (0.0-1.0)")
ZFS_L2ARC_READ_BYTES_RATE = declare_gauge("ZFS_L2ARC_READ_BYTES_RATE", "truenas_zfs_l2arc_read_bytes_per_second", "L2ARC read bytes per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_WRITE_BYTES_RATE = declare_gauge("ZFS_L2ARC_WRITE_BYTES_RATE", "truenas_zfs_l2arc_write_bytes_per_second", "L2ARC write bytes per second (instantaneous snapshot from realtime API)")

# ZFS demand totals and I/O-hit sub-counters (v25+ realtime — previously missing)
ZFS_DEMAND_ACCESSES_RATE = declare_gauge("ZFS_DEMAND_ACCESSES_RATE", "truenas_zfs_demand_accesses_per_second", "ZFS ARC total demand accesses per second (data + metadata, instantaneous snapshot from realtime API)")
ZFS_DEMAND_DATA_IO_HITS_RATE = declare_gauge("ZFS_DEMAND_DATA_IO_HITS_RATE", "truenas_zfs_demand_data_io_hits_per_second", "ZFS demand data I/O hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_ACCESSES_RATE = declare_gauge("ZFS_DEMAND_META_ACCESSES_RATE", "truenas_zfs_demand_metadata_accesses_per_second", "ZFS demand metadata accesses per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_IO_HITS_RATE = declare_gauge("ZFS_DEMAND_META_IO_HITS_RATE", "truenas_zfs_demand_metadata_io_hits_per_second", "ZFS demand metadata I/O hits per second (instantaneous snapshot from realtime API)")
ZFS_DEMAND_META_IO_HIT_RATIO = declare_gauge("ZFS_DEMAND_META_IO_HIT_RATIO", "truenas_zfs_demand_metadata_io_hit_ratio", "ZFS demand metadata I/O hit ratio (0.0-1.0)")
ZFS_DEMAND_META_MISS_RATIO = declare_gauge("ZFS_DEMAND_META_MISS_RATIO", "truenas_zfs_demand_metadata_miss_ratio", "ZFS demand metadata miss ratio (0.0-1.0)")
ZFS_L2ARC_ACCESSES_RATE = declare_gauge("ZFS_L2ARC_ACCESSES_RATE", "truenas_zfs_l2arc_accesses_per_second", "ZFS L2ARC total accesses per second (instantaneous snapshot from realtime API)")
ZFS_L2ARC_MISS_RATIO = declare_gauge("ZFS_L2ARC_MISS_RATIO", "truenas_zfs_l2arc_miss_ratio", "ZFS L2ARC miss ratio (0.0-1.0)")

# Pool real-time I/O (from reporting.realtime pools section — v25+)
POOL_REALTIME_READ_BYTES = declare_gauge("POOL_REALTIME_READ_BYTES", "truenas_pool_realtime_read_bytes_per_second", "Pool read throughput in bytes/sec (instantaneous snapshot from realtime API)", ["pool"])
POOL_REALTIME_WRITE_BYTES = declare_gauge("POOL_REALTIME_WRITE_BYTES", "truenas_pool_realtime_write_bytes_per_second", "Pool write throughput in bytes/sec (instantaneous snapshot from realtime API)", ["pool"])

# App/Container stats (from app.stats event in v25)
APP_CPU_PERCENT = declare_gauge("APP_CPU_PERCENT", "truenas_app_cpu_percent", "App container CPU usage percent (0 to 100)", ["app"])
APP_MEMORY_BYTES = declare_gauge("APP_MEMORY_BYTES", "truenas_app_memory_bytes", "App container memory usage bytes", ["app"])
APP_NET_RX_BYTES_RATE = declare_gauge("APP_NET_RX_BYTES_RATE", "truenas_app_net_rx_bytes_per_second", "App container network receive bytes/sec (instantaneous snapshot from realtime API)", ["app", "interface"])
APP_NET_TX_BYTES_RATE = declare_gauge("APP_NET_TX_BYTES_RATE", "truenas_app_net_tx_bytes_per_second", "App container network transmit bytes/sec (instantaneous snapshot from realtime API)", ["app", "interface"])
APP_BLKIO_READ_BYTES = declare_gauge("APP_BLKIO_READ_BYTES", "truenas_app_blkio_read_bytes", "App container block I/O read bytes", ["app"])
APP_BLKIO_WRITE_BYTES = declare_gauge("APP_BLKIO_WRITE_BYTES", "truenas_app_blkio_write_bytes", "App container block I/O write bytes", ["app"])

# ---------------------------------------------------------------------------
# Pool vdev error counters (from pool.query topology/stats)
# ---------------------------------------------------------------------------
POOL_VDEV_READ_ERRORS = declare_gauge("POOL_VDEV_READ_ERRORS", 
    "truenas_pool_vdev_read_errors",
    "Read errors on pool vdev since last scrub clear",
    ["pool", "vdev"],
)
POOL_VDEV_WRITE_ERRORS = declare_gauge("POOL_VDEV_WRITE_ERRORS", 
    "truenas_pool_vdev_write_errors",
    "Write errors on pool vdev since last scrub clear",
    ["pool", "vdev"],
)
POOL_VDEV_CHECKSUM_ERRORS = declare_gauge("POOL_VDEV_CHECKSUM_ERRORS", 
    "truenas_pool_vdev_checksum_errors",
    "Checksum errors on pool vdev since last scrub clear",
    ["pool", "vdev"],
)

# ---------------------------------------------------------------------------
# SMB / NFS session metrics
# ---------------------------------------------------------------------------
SMB_SESSION_COUNT = declare_gauge("SMB_SESSION_COUNT", "truenas_smb_session_count", "Number of active SMB sessions")
SMB_OPEN_FILE_COUNT = declare_gauge("SMB_OPEN_FILE_COUNT", "truenas_smb_open_file_count", "Number of SMB open files")
SMB_CONNECTION_COUNT = declare_gauge("SMB_CONNECTION_COUNT", "truenas_smb_connection_count", "Number of active SMB connections")
NFS_SERVER_STAT_OPS = declare_gauge("NFS_SERVER_STAT_OPS", "truenas_nfs_server_ops_per_second", "NFS server operations per second (instantaneous snapshot from realtime API)")

# ---------------------------------------------------------------------------
# GPU
# ---------------------------------------------------------------------------
GPU_COUNT = declare_gauge("GPU_COUNT", "truenas_gpu_count", "Number of GPU devices visible to the host")
GPU_INFO = declare_gauge("GPU_INFO", 
    "truenas_gpu_info",
    "GPU device info — always 1; carry identifying labels",
    ["index", "model", "vendor", "pci_id"],
)
GPU_AVAILABLE_TO_HOST = declare_gauge("GPU_AVAILABLE_TO_HOST", "truenas_gpu_available_to_host", "1 if the GPU is available to the TrueNAS host", ["index"])
GPU_USES_CRITICAL_DEVICES = declare_gauge("GPU_USES_CRITICAL_DEVICES", "truenas_gpu_uses_system_critical_devices", "1 if the GPU uses system-critical PCI devices", ["index"])

# ---------------------------------------------------------------------------
# JBOF (Just a Bunch of Flash) hardware
# ---------------------------------------------------------------------------
JBOF_COUNT = declare_gauge("JBOF_COUNT", "truenas_jbof_count", "Number of JBOF enclosures connected")

# ---------------------------------------------------------------------------
# Active API sessions
# ---------------------------------------------------------------------------
AUTH_SESSIONS_ACTIVE = declare_gauge("AUTH_SESSIONS_ACTIVE", "truenas_auth_sessions_active", "Number of active authenticated API sessions")

# ---------------------------------------------------------------------------
# Additional host info from system.info
# ---------------------------------------------------------------------------
HOST_ECC_MEMORY = declare_gauge("HOST_ECC_MEMORY", "truenas_host_ecc_memory", "1 if host RAM is ECC-protected")
HOST_CPU_MODEL = declare_gauge("HOST_CPU_MODEL", 
    "truenas_host_cpu_info",
    "Always 1; CPU model string in label",
    ["model"],
)
HOST_SYSTEM_INFO = declare_gauge("HOST_SYSTEM_INFO", 
    "truenas_host_system_info",
    "Always 1; hardware manufacturer/product labels from DMI",
    ["manufacturer", "product"],
)

# ---------------------------------------------------------------------------
# Disk extended info (from disk.query with extra fields)
# ---------------------------------------------------------------------------
DISK_ROTATIONAL = declare_gauge("DISK_ROTATIONAL", "truenas_disk_rotational", "1 if disk is rotational (HDD), 0 if SSD/NVMe", ["disk"])
DISK_SMART_ENABLED = declare_gauge("DISK_SMART_ENABLED", "truenas_disk_smart_enabled", "1 if S.M.A.R.T. is enabled for disk", ["disk"])
DISK_INFO = declare_gauge("DISK_INFO", "truenas_disk_info", "Disk identity info — always 1", ["disk", "model", "serial", "bus"])

# ---------------------------------------------------------------------------
# Pool scan detailed stats (from pool.query scan sub-object)
# ---------------------------------------------------------------------------
POOL_SCAN_ERRORS = declare_gauge("POOL_SCAN_ERRORS", "truenas_pool_scan_errors", "Errors found in last pool scan", ["pool"])
POOL_SCAN_BYTES_PROCESSED = declare_gauge("POOL_SCAN_BYTES_PROCESSED", "truenas_pool_scan_bytes_processed", "Bytes processed in last pool scan", ["pool"])
POOL_SCAN_BYTES_TOTAL = declare_gauge("POOL_SCAN_BYTES_TOTAL", "truenas_pool_scan_bytes_total", "Total bytes to process in last pool scan", ["pool"])
POOL_SCAN_SECONDS_REMAINING = declare_gauge("POOL_SCAN_SECONDS_REMAINING", "truenas_pool_scan_seconds_remaining", "Estimated seconds remaining in active pool scan", ["pool"])
POOL_LAST_SCAN_TS = declare_gauge("POOL_LAST_SCAN_TS", "truenas_pool_last_scan_timestamp_seconds", "Unix timestamp of last pool scan end", ["pool"])

# ---------------------------------------------------------------------------
# Exporter self-identification (v5)
# ---------------------------------------------------------------------------
EXPORTER_INFO = declare_gauge("EXPORTER_INFO", "truenas_exporter_info", "Exporter version info — always 1", ["version"])
EXPORTER_INFO.labels(version=EXPORTER_VERSION).set(1)

# Collector-level error counter (v5) — makes silent try/except failures visible
COLLECTOR_ERRORS_TOTAL = declare_counter("COLLECTOR_ERRORS_TOTAL", 
    "truenas_collector_errors_total",
    "Total collector-level errors since exporter start",
    ["collector"],
)

# ---------------------------------------------------------------------------
# Pool scrub task scheduling (v5 — pool.scrub.query)
# ---------------------------------------------------------------------------
POOL_SCRUB_TASK_COUNT = declare_gauge("POOL_SCRUB_TASK_COUNT", "truenas_pool_scrub_task_count", "Number of configured pool scrub tasks")
POOL_SCRUB_TASK_ENABLED = declare_gauge("POOL_SCRUB_TASK_ENABLED", "truenas_pool_scrub_task_enabled", "1 if scrub task is enabled", ["pool"])
POOL_SCRUB_TASK_STATE = declare_gauge("POOL_SCRUB_TASK_STATE", "truenas_pool_scrub_task_state", "Scrub task last-run state as label", ["pool", "state"])
POOL_SCRUB_LAST_RUN_TS = declare_gauge("POOL_SCRUB_LAST_RUN_TS", "truenas_pool_scrub_last_run_timestamp_seconds", "Unix timestamp of last scrub task run", ["pool"])

# ---------------------------------------------------------------------------
# Snapshots (v5 — pool.snapshot.query)
# ---------------------------------------------------------------------------
SNAPSHOT_TOTAL_COUNT = declare_gauge("SNAPSHOT_TOTAL_COUNT", "truenas_snapshot_count", "Total number of ZFS snapshots")
SNAPSHOT_OLDEST_TS = declare_gauge("SNAPSHOT_OLDEST_TS", "truenas_snapshot_oldest_timestamp_seconds", "Unix timestamp of the oldest ZFS snapshot (0 if no snapshots)")

# ---------------------------------------------------------------------------
# SMART test results (legacy declarations; no documented 25.10.2 producer)
# ---------------------------------------------------------------------------
SMART_TEST_LAST_RESULT = declare_gauge("SMART_TEST_LAST_RESULT", 
    "truenas_smart_test_last_result",
    "Last SMART test result — 1 = SUCCESS, 0 = FAILED",
    ["disk"],
)
SMART_TEST_LAST_TIMESTAMP = declare_gauge("SMART_TEST_LAST_TIMESTAMP", 
    "truenas_smart_test_last_timestamp_seconds",
    "Unix timestamp of last SMART test for disk",
    ["disk"],
)

# ---------------------------------------------------------------------------
# Pool resilver config (v5)
# ---------------------------------------------------------------------------
POOL_RESILVER_ENABLED = declare_gauge("POOL_RESILVER_ENABLED", "truenas_pool_resilver_enabled", "1 if resilver priority scheduling is enabled")

# ---------------------------------------------------------------------------
# Cloud backup tasks (v5 — cloud_backup.query)
# ---------------------------------------------------------------------------
CLOUD_BACKUP_TASK_COUNT = declare_gauge("CLOUD_BACKUP_TASK_COUNT", "truenas_cloud_backup_task_count", "Number of configured cloud backup tasks")
CLOUD_BACKUP_TASK_ENABLED = declare_gauge("CLOUD_BACKUP_TASK_ENABLED", "truenas_cloud_backup_task_enabled", "1 if cloud backup task is enabled", ["name"])
CLOUD_BACKUP_TASK_STATE = declare_gauge("CLOUD_BACKUP_TASK_STATE", "truenas_cloud_backup_task_state", "Cloud backup task state as label", ["name", "state"])

# ---------------------------------------------------------------------------
# Cron jobs (v5 — cronjob.query)
# ---------------------------------------------------------------------------
CRONJOB_COUNT = declare_gauge("CRONJOB_COUNT", "truenas_cronjob_count", "Number of configured cron jobs")
CRONJOB_ENABLED = declare_gauge("CRONJOB_ENABLED", "truenas_cronjob_enabled", "1 if cron job is enabled", ["name"])

# ---------------------------------------------------------------------------
# Disk in-use (v5 — disk.get_used)
# ---------------------------------------------------------------------------
DISK_IN_USE = declare_gauge("DISK_IN_USE", "truenas_disk_in_use", "1 if disk is in use by a pool", ["disk"])

# ---------------------------------------------------------------------------
# DNS resolvers (v5 — dns.query)
# ---------------------------------------------------------------------------
DNS_RESOLVER_COUNT = declare_gauge("DNS_RESOLVER_COUNT", "truenas_dns_resolver_count", "Number of configured DNS resolvers")

# ---------------------------------------------------------------------------
# Protocol configs (v5)
# ---------------------------------------------------------------------------
SMB_MULTICHANNEL_ENABLED = declare_gauge("SMB_MULTICHANNEL_ENABLED", "truenas_smb_multichannel_enabled", "1 if SMB multichannel is enabled")
NFS_V4_ENABLED = declare_gauge("NFS_V4_ENABLED", "truenas_nfs_v4_enabled", "1 if NFSv4 is enabled")
NFS_SERVERS = declare_gauge("NFS_SERVERS", "truenas_nfs_servers", "Number of NFS server threads configured")
NFS_RDMA_ENABLED = declare_gauge("NFS_RDMA_ENABLED", "truenas_nfs_rdma_enabled", "1 if NFS over RDMA is enabled")
SMB1_ENABLED = declare_gauge("SMB1_ENABLED", "truenas_smb1_enabled", "1 if legacy SMB1 protocol support is enabled")
SMB_NTLMV1_AUTH_ENABLED = declare_gauge("SMB_NTLMV1_AUTH_ENABLED", "truenas_smb_ntlmv1_auth_enabled", "1 if insecure SMB NTLMv1 authentication is enabled")
SMB_ENCRYPTION_MODE = declare_gauge(
    "SMB_ENCRYPTION_MODE",
    "truenas_smb_encryption_mode",
    "Configured SMB transport encryption mode",
    ["mode"],
)
SSH_ENABLED = declare_gauge("SSH_ENABLED", "truenas_ssh_enabled", "1 if SSH service is enabled to start automatically")
SSH_PASSWORD_AUTH = declare_gauge("SSH_PASSWORD_AUTH", "truenas_ssh_password_auth", "1 if SSH password authentication is enabled")
FTP_ENABLED = declare_gauge("FTP_ENABLED", "truenas_ftp_enabled", "1 if FTP service is enabled to start automatically")
SNMP_ENABLED = declare_gauge("SNMP_ENABLED", "truenas_snmp_enabled", "1 if SNMP service is enabled to start automatically")

# ---------------------------------------------------------------------------
# System advanced/general config (v5)
# ---------------------------------------------------------------------------
CONSOLEMENU_ENABLED = declare_gauge("CONSOLEMENU_ENABLED", "truenas_consolemenu_enabled", "1 if serial console menu is enabled")
SERIALCONSOLE_ENABLED = declare_gauge("SERIALCONSOLE_ENABLED", "truenas_serialconsole_enabled", "1 if serial console is enabled")
UI_HTTPS_PORT = declare_gauge("UI_HTTPS_PORT", "truenas_ui_https_port", "Web UI HTTPS port number")

# ---------------------------------------------------------------------------
# KMIP / support / systemdataset (v5)
# ---------------------------------------------------------------------------
KMIP_ENABLED = declare_gauge("KMIP_ENABLED", "truenas_kmip_enabled", "1 if KMIP key management is enabled")
SUPPORT_AVAILABLE = declare_gauge("SUPPORT_AVAILABLE", "truenas_support_available", "1 if proactive support is available")
SUPPORT_AVAILABLE_AND_ENABLED = declare_gauge("SUPPORT_AVAILABLE_AND_ENABLED", 
    "truenas_support_available_and_enabled",
    "1 if support is both available and enabled",
)
SUPPORT_CONFIG_ENABLED = declare_gauge("SUPPORT_CONFIG_ENABLED", 
    "truenas_support_config_enabled",
    "1 if support.config reports support enabled",
)
SYSTEMDATASET_POOL = declare_gauge("SYSTEMDATASET_POOL", "truenas_systemdataset_pool", "System dataset pool as label", ["pool"])

# ---------------------------------------------------------------------------
# Priority gap metrics (bounded-cardinality dedicated collectors)
# ---------------------------------------------------------------------------
APP_DOCKERHUB_PULL_LIMIT_TOTAL = declare_gauge("APP_DOCKERHUB_PULL_LIMIT_TOTAL", 
    "truenas_app_dockerhub_pull_limit_total",
    "Total DockerHub pull limit window size",
)
APP_DOCKERHUB_PULL_LIMIT_REMAINING = declare_gauge("APP_DOCKERHUB_PULL_LIMIT_REMAINING", 
    "truenas_app_dockerhub_pull_limit_remaining",
    "Remaining DockerHub pulls in current window",
)
APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS = declare_gauge("APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS", 
    "truenas_app_dockerhub_pull_limit_window_seconds",
    "DockerHub rate-limit window duration in seconds",
)
APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS = declare_gauge("APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS",
    "truenas_app_dockerhub_pull_limit_remaining_window_seconds",
    "Seconds remaining in the current DockerHub pull-limit window",
)
APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT = declare_gauge("APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT", 
    "truenas_app_dockerhub_rate_limit_error_present",
    "1 if app.image.dockerhub_rate_limit reports an error",
)

DIRECTORYSERVICES_CONFIG_ENABLED = declare_gauge("DIRECTORYSERVICES_CONFIG_ENABLED", 
    "truenas_directoryservices_config_enabled",
    "1 if directoryservices.config is enabled",
)
DIRECTORYSERVICES_ACCOUNT_CACHE_ENABLED = declare_gauge("DIRECTORYSERVICES_ACCOUNT_CACHE_ENABLED", 
    "truenas_directoryservices_account_cache_enabled",
    "1 if directoryservices account cache is enabled",
)
DIRECTORYSERVICES_DNS_UPDATES_ENABLED = declare_gauge("DIRECTORYSERVICES_DNS_UPDATES_ENABLED", 
    "truenas_directoryservices_dns_updates_enabled",
    "1 if directoryservices DNS updates are enabled",
)
DIRECTORYSERVICES_TIMEOUT_SECONDS = declare_gauge("DIRECTORYSERVICES_TIMEOUT_SECONDS", 
    "truenas_directoryservices_timeout_seconds",
    "Directoryservices timeout in seconds",
)
DIRECTORYSERVICES_SERVICE_TYPE = declare_gauge("DIRECTORYSERVICES_SERVICE_TYPE", 
    "truenas_directoryservices_service_type",
    "Directoryservices service type label (always 1)",
    ["service_type"],
)
DIRECTORYSERVICES_KERBEROS_CONFIGURED = declare_gauge("DIRECTORYSERVICES_KERBEROS_CONFIGURED", 
    "truenas_directoryservices_kerberos_configured",
    "1 if directoryservices kerberos configuration is present",
)
DIRECTORYSERVICES_FAULT_PRESENT = declare_gauge("DIRECTORYSERVICES_FAULT_PRESENT",
    "truenas_directoryservices_fault_present",
    "1 if the enabled directory service reports FAULTED status",
    ["service"],
)

SYSTEM_SECURITY_FIPS_CONFIGURED = declare_gauge("SYSTEM_SECURITY_FIPS_CONFIGURED", 
    "truenas_system_security_fips_configured",
    "1 if system.security.config reports FIPS configured",
)
SYSTEM_SECURITY_GPOS_STIG = declare_gauge("SYSTEM_SECURITY_GPOS_STIG", 
    "truenas_system_security_gpos_stig",
    "1 if system.security.config reports GPOS STIG enabled",
)
SYSTEM_SECURITY_PASSWORD_MIN_LENGTH = declare_gauge("SYSTEM_SECURITY_PASSWORD_MIN_LENGTH", 
    "truenas_system_security_password_min_length",
    "Configured minimum password length",
)
SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS = declare_gauge("SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS", 
    "truenas_system_security_password_min_age_days",
    "Configured minimum password age in days",
)
SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS = declare_gauge("SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS", 
    "truenas_system_security_password_max_age_days",
    "Configured maximum password age in days",
)
SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS = declare_gauge("SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS", 
    "truenas_system_security_password_warn_age_days",
    "Configured password expiration warning age in days",
)
SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT = declare_gauge("SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT", 
    "truenas_system_security_password_history_count",
    "Configured password history length",
)

UPDATE_AUTOCHECK_ENABLED = declare_gauge("UPDATE_AUTOCHECK_ENABLED", 
    "truenas_update_autocheck_enabled",
    "1 if automatic update checks are enabled",
)
UPDATE_PROFILE_INFO = declare_gauge("UPDATE_PROFILE_INFO", 
    "truenas_update_profile_info",
    "Update profile information label (always 1)",
    ["profile"],
)

NTP_SERVER_COUNT = declare_gauge("NTP_SERVER_COUNT", "truenas_ntp_server_count", "Total configured NTP servers")
NTP_SERVER_ACTIVE_COUNT = declare_gauge("NTP_SERVER_ACTIVE_COUNT", "truenas_ntp_server_active_count", "Configured NTP servers marked active")
NTP_SERVER_REACHABLE_COUNT = declare_gauge("NTP_SERVER_REACHABLE_COUNT", "truenas_ntp_server_reachable_count", "NTP servers currently reachable")
NTP_SERVER_PREFER_COUNT = declare_gauge("NTP_SERVER_PREFER_COUNT", "truenas_ntp_server_prefer_count", "Configured NTP servers marked prefer")
NTP_SERVER_BURST_COUNT = declare_gauge("NTP_SERVER_BURST_COUNT", "truenas_ntp_server_burst_count", "Configured NTP servers with burst enabled")
NTP_SERVER_IBURST_COUNT = declare_gauge("NTP_SERVER_IBURST_COUNT", "truenas_ntp_server_iburst_count", "Configured NTP servers with iburst enabled")
NTP_SERVER_MIN_POLL_MINUTES = declare_gauge("NTP_SERVER_MIN_POLL_MINUTES", 
    "truenas_ntp_server_min_poll_minutes",
    "Minimum configured NTP poll interval (minutes)",
)
NTP_SERVER_MAX_POLL_MINUTES = declare_gauge("NTP_SERVER_MAX_POLL_MINUTES", 
    "truenas_ntp_server_max_poll_minutes",
    "Maximum configured NTP poll interval (minutes)",
)

# ---------------------------------------------------------------------------
# Users / groups / routes / tunables / privileges (v5)
# ---------------------------------------------------------------------------
LOCAL_USER_COUNT = declare_gauge("LOCAL_USER_COUNT", "truenas_local_user_count", "Number of local user accounts")
LOCAL_GROUP_COUNT = declare_gauge("LOCAL_GROUP_COUNT", "truenas_local_group_count", "Number of local groups")
STATIC_ROUTE_COUNT = declare_gauge("STATIC_ROUTE_COUNT", "truenas_static_route_count", "Number of static routes")
TUNABLE_COUNT = declare_gauge("TUNABLE_COUNT", "truenas_tunable_count", "Number of kernel tunables configured")
PRIVILEGE_COUNT = declare_gauge("PRIVILEGE_COUNT", "truenas_privilege_count", "Number of RBAC privilege entries")

# ---------------------------------------------------------------------------
# iSCSI inventory (v5)
# ---------------------------------------------------------------------------
ISCSI_TARGET_COUNT = declare_gauge("ISCSI_TARGET_COUNT", "truenas_iscsi_target_count", "Number of iSCSI targets")
ISCSI_PORTAL_COUNT = declare_gauge("ISCSI_PORTAL_COUNT", "truenas_iscsi_portal_count", "Number of iSCSI portals")
ISCSI_EXTENT_COUNT = declare_gauge("ISCSI_EXTENT_COUNT", "truenas_iscsi_extent_count", "Number of iSCSI extents")
ISCSI_INITIATOR_COUNT = declare_gauge("ISCSI_INITIATOR_COUNT", "truenas_iscsi_initiator_count", "Number of iSCSI initiator groups")

# ---------------------------------------------------------------------------
# NVMe-oF extended (v5)
# ---------------------------------------------------------------------------
NVMET_HOST_COUNT = declare_gauge("NVMET_HOST_COUNT", "truenas_nvmet_host_count", "Number of NVMe-oF allowed hosts")
NVMET_NAMESPACE_COUNT = declare_gauge("NVMET_NAMESPACE_COUNT", "truenas_nvmet_namespace_count", "Number of NVMe-oF namespaces")

# ---------------------------------------------------------------------------
# Network config (v5)
# ---------------------------------------------------------------------------
NETWORK_HTTPPROXY_CONFIGURED = declare_gauge("NETWORK_HTTPPROXY_CONFIGURED", "truenas_network_httpproxy_configured", "1 if HTTP proxy is configured")

# ---------------------------------------------------------------------------
# Docker images / app volumes (v5)
# ---------------------------------------------------------------------------
DOCKER_IMAGE_COUNT = declare_gauge("DOCKER_IMAGE_COUNT", "truenas_docker_image_count", "Number of Docker container images")

# ---------------------------------------------------------------------------
# Replication / reporting config (v5)
# ---------------------------------------------------------------------------
REPLICATION_MAX_PARALLEL = declare_gauge("REPLICATION_MAX_PARALLEL", "truenas_replication_max_parallel", "Maximum parallel replication tasks allowed")
REPORTING_EXPORTER_COUNT = declare_gauge("REPORTING_EXPORTER_COUNT", "truenas_reporting_exporter_count", "Number of reporting exporter plugins")
REPORTING_ENABLED = declare_gauge("REPORTING_ENABLED", "truenas_reporting_enabled", "1 if the reporting service is enabled to start automatically")
REPORTING_TIER0_RETENTION_DAYS = declare_gauge("REPORTING_TIER0_RETENTION_DAYS", 
    "truenas_reporting_tier0_retention_days",
    "Reporting tier0 retention in days",
)
REPORTING_TIER1_RETENTION_DAYS = declare_gauge("REPORTING_TIER1_RETENTION_DAYS", 
    "truenas_reporting_tier1_retention_days",
    "Reporting tier1 retention in days",
)
REPORTING_TIER1_UPDATE_INTERVAL_SECONDS = declare_gauge("REPORTING_TIER1_UPDATE_INTERVAL_SECONDS", 
    "truenas_reporting_tier1_update_interval_seconds",
    "Reporting tier1 update interval in seconds",
)

# ---------------------------------------------------------------------------
# IOMMU / 2FA / mail / alerts (v5)
# ---------------------------------------------------------------------------
IOMMU_ENABLED = declare_gauge("IOMMU_ENABLED", "truenas_iommu_enabled", "1 if IOMMU/PCI passthrough is enabled")
TWOFACTOR_ENABLED = declare_gauge("TWOFACTOR_ENABLED", "truenas_2fa_enabled", "1 if two-factor authentication is enabled")
MAIL_CONFIGURED = declare_gauge("MAIL_CONFIGURED", "truenas_mail_configured", "1 if outgoing email (SMTP) is configured")
ALERTSERVICE_COUNT = declare_gauge("ALERTSERVICE_COUNT", "truenas_alertservice_count", "Number of alert notification services")
ALERTSERVICE_ENABLED = declare_gauge("ALERTSERVICE_ENABLED", "truenas_alertservice_enabled", "1 if alert service is enabled", ["name", "type"])

# ---------------------------------------------------------------------------
# Init/shutdown scripts / keychain / system global ID (v5)
# ---------------------------------------------------------------------------
INITSHUTDOWNSCRIPT_COUNT = declare_gauge("INITSHUTDOWNSCRIPT_COUNT", "truenas_initshutdownscript_count", "Number of init/shutdown scripts")
KEYCHAIN_CREDENTIAL_COUNT = declare_gauge("KEYCHAIN_CREDENTIAL_COUNT", "truenas_keychain_credential_count", "Number of SSH/keychain credentials")
SYSTEM_GLOBAL_ID = declare_gauge("SYSTEM_GLOBAL_ID", "truenas_system_global_id", "Always 1; system global unique ID as label", ["global_id"])

# Update download status (update.status)
UPDATE_DOWNLOAD_PROGRESS_PERCENT = declare_gauge("UPDATE_DOWNLOAD_PROGRESS_PERCENT", "truenas_update_download_progress_percent", "Current update download completion percentage (0 to 100)")
