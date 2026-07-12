"""Prometheus metric declarations and public metric contract objects."""

from prometheus_client import Counter, Gauge, disable_created_metrics

from .version import __version__

disable_created_metrics()
EXPORTER_VERSION = __version__

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
VM_FLAG_INTEL_VMX = Gauge("truenas_vm_flag_intel_vmx", "1 if Intel VT-x/VMX flag is present")
VM_FLAG_AMD_RVI = Gauge("truenas_vm_flag_amd_rvi", "1 if AMD RVI/NPT flag is present")
VM_FLAG_UNRESTRICTED_GUEST = Gauge(
    "truenas_vm_flag_unrestricted_guest",
    "1 if unrestricted guest support is present",
)
VM_FLAG_AMD_ASIDS = Gauge("truenas_vm_flag_amd_asids", "Number of AMD ASIDs when reported")
VM_VIRTUALIZATION_DETAILS_SUPPORTED = Gauge(
    "truenas_vm_virtualization_details_supported",
    "1 if vm.virtualization_details reports virtualization support",
)
VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT = Gauge(
    "truenas_vm_virtualization_details_error_present",
    "1 if vm.virtualization_details reports an error",
)

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
ISCSI_SESSION_COUNT = Gauge("truenas_iscsi_session_count", "Number of active iSCSI sessions")
ISCSI_SESSION_ISER_COUNT = Gauge(
    "truenas_iscsi_session_iser_count",
    "Number of active iSCSI sessions using iSER",
)
ISCSI_SESSION_OFFLOAD_COUNT = Gauge(
    "truenas_iscsi_session_offload_count",
    "Number of active iSCSI sessions using offload",
)
ISCSI_SESSION_IMMEDIATE_DATA_COUNT = Gauge(
    "truenas_iscsi_session_immediate_data_count",
    "Number of active iSCSI sessions with immediate-data enabled",
)

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
CATALOG_CONFIG_PRESENT = Gauge("truenas_catalog_config_present", "1 if catalog.config returned a config payload")
CATALOG_PREFERRED_TRAIN_COUNT = Gauge(
    "truenas_catalog_preferred_train_count",
    "Number of preferred catalog trains configured",
)

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
EXPORTER_INFO.labels(version=EXPORTER_VERSION).set(1)

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
SUPPORT_AVAILABLE_AND_ENABLED = Gauge(
    "truenas_support_available_and_enabled",
    "1 if support is both available and enabled",
)
SUPPORT_CONFIG_ENABLED = Gauge(
    "truenas_support_config_enabled",
    "1 if support.config reports support enabled",
)
SYSTEMDATASET_POOL = Gauge("truenas_systemdataset_pool", "System dataset pool as label", ["pool"])

# ---------------------------------------------------------------------------
# Priority gap metrics (bounded-cardinality dedicated collectors)
# ---------------------------------------------------------------------------
APP_DOCKERHUB_PULL_LIMIT_TOTAL = Gauge(
    "truenas_app_dockerhub_pull_limit_total",
    "Total DockerHub pull limit window size",
)
APP_DOCKERHUB_PULL_LIMIT_REMAINING = Gauge(
    "truenas_app_dockerhub_pull_limit_remaining",
    "Remaining DockerHub pulls in current window",
)
APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS = Gauge(
    "truenas_app_dockerhub_pull_limit_window_seconds",
    "DockerHub rate-limit window duration in seconds",
)
APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT = Gauge(
    "truenas_app_dockerhub_rate_limit_error_present",
    "1 if app.image.dockerhub_rate_limit reports an error",
)

DIRECTORYSERVICES_CONFIG_ENABLED = Gauge(
    "truenas_directoryservices_config_enabled",
    "1 if directoryservices.config is enabled",
)
DIRECTORYSERVICES_ACCOUNT_CACHE_ENABLED = Gauge(
    "truenas_directoryservices_account_cache_enabled",
    "1 if directoryservices account cache is enabled",
)
DIRECTORYSERVICES_DNS_UPDATES_ENABLED = Gauge(
    "truenas_directoryservices_dns_updates_enabled",
    "1 if directoryservices DNS updates are enabled",
)
DIRECTORYSERVICES_TIMEOUT_SECONDS = Gauge(
    "truenas_directoryservices_timeout_seconds",
    "Directoryservices timeout in seconds",
)
DIRECTORYSERVICES_SERVICE_TYPE = Gauge(
    "truenas_directoryservices_service_type",
    "Directoryservices service type label (always 1)",
    ["service_type"],
)
DIRECTORYSERVICES_KERBEROS_CONFIGURED = Gauge(
    "truenas_directoryservices_kerberos_configured",
    "1 if directoryservices kerberos configuration is present",
)

SYSTEM_SECURITY_FIPS_CONFIGURED = Gauge(
    "truenas_system_security_fips_configured",
    "1 if system.security.config reports FIPS configured",
)
SYSTEM_SECURITY_GPOS_STIG = Gauge(
    "truenas_system_security_gpos_stig",
    "1 if system.security.config reports GPOS STIG enabled",
)
SYSTEM_SECURITY_PASSWORD_MIN_LENGTH = Gauge(
    "truenas_system_security_password_min_length",
    "Configured minimum password length",
)
SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS = Gauge(
    "truenas_system_security_password_min_age_days",
    "Configured minimum password age in days",
)
SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS = Gauge(
    "truenas_system_security_password_max_age_days",
    "Configured maximum password age in days",
)
SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS = Gauge(
    "truenas_system_security_password_warn_age_days",
    "Configured password expiration warning age in days",
)
SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT = Gauge(
    "truenas_system_security_password_history_count",
    "Configured password history length",
)

UPDATE_AUTOCHECK_ENABLED = Gauge(
    "truenas_update_autocheck_enabled",
    "1 if automatic update checks are enabled",
)
UPDATE_PROFILE_INFO = Gauge(
    "truenas_update_profile_info",
    "Update profile information label (always 1)",
    ["profile"],
)

NTP_SERVER_COUNT = Gauge("truenas_ntp_server_count", "Total configured NTP servers")
NTP_SERVER_ACTIVE_COUNT = Gauge("truenas_ntp_server_active_count", "Configured NTP servers marked active")
NTP_SERVER_REACHABLE_COUNT = Gauge("truenas_ntp_server_reachable_count", "NTP servers currently reachable")
NTP_SERVER_PREFER_COUNT = Gauge("truenas_ntp_server_prefer_count", "Configured NTP servers marked prefer")
NTP_SERVER_BURST_COUNT = Gauge("truenas_ntp_server_burst_count", "Configured NTP servers with burst enabled")
NTP_SERVER_IBURST_COUNT = Gauge("truenas_ntp_server_iburst_count", "Configured NTP servers with iburst enabled")
NTP_SERVER_MIN_POLL_MINUTES = Gauge(
    "truenas_ntp_server_min_poll_minutes",
    "Minimum configured NTP poll interval (minutes)",
)
NTP_SERVER_MAX_POLL_MINUTES = Gauge(
    "truenas_ntp_server_max_poll_minutes",
    "Maximum configured NTP poll interval (minutes)",
)

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
REPORTING_TIER0_RETENTION_DAYS = Gauge(
    "truenas_reporting_tier0_retention_days",
    "Reporting tier0 retention in days",
)
REPORTING_TIER1_RETENTION_DAYS = Gauge(
    "truenas_reporting_tier1_retention_days",
    "Reporting tier1 retention in days",
)
REPORTING_TIER1_UPDATE_INTERVAL_SECONDS = Gauge(
    "truenas_reporting_tier1_update_interval_seconds",
    "Reporting tier1 update interval in seconds",
)

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

