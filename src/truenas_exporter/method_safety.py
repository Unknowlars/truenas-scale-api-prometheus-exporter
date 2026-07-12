"""Read-only TrueNAS method discovery policy."""

import re

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

_AUTO_SKIP_ERROR_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"missing required (positional )?argument", re.IGNORECASE),
    re.compile(r"takes .* positional argument", re.IGNORECASE),
    re.compile(r"method .* not found", re.IGNORECASE),
    re.compile(r"method does not exist", re.IGNORECASE),
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
    "virt.global.get_network",   # requires explicit virt network identifier
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
    "vm.flags",
    "directoryservices.config",
    "system.security.config",
    "support.is_available_and_enabled",
    "support.config",
    "update.config",
    "system.ntpserver.query",
    "catalog.config",
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
