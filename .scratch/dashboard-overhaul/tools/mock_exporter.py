#!/usr/bin/env python3
"""Synthetic TrueNAS exporter for sanitized dashboard renders.

Every name is fictional (host "nas-demo", pools "tank"/"flash", generic app
names). The metric surface is derived from docs/metrics-contract.json so
every contract metric that the real exporter can produce is present, with
hand-tuned values for the series dashboards care about and deliberate
reproductions of the live-review defects:

  D1  4 alerts, 3 dismissed -> 1 outstanding
  D2  *_hit_percentage / *_hit_ratio = 0 while hits ~= accesses
  D3  directory services disabled (service="none", status="DISABLED")
  D10 a finished scrub reporting 101.39 %
  D13 a USB disk reporting 0 degC

Profiles: --profile 27 (aggregate disk="total" I/O, no CPU user/system split)
or --profile 25.10 (per-disk I/O, CPU split present).

Modes:
  serve  : HTTP /metrics on --port (values follow wall-clock time)
  dump   : OpenMetrics with timestamps for promtool backfill
           (--hours history ending --end-offset minutes ago)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

CONTRACT = json.loads(Path(__file__).with_name("metrics-contract.json").read_text()
                      if Path(__file__).with_name("metrics-contract.json").exists()
                      else (Path(__file__).resolve().parents[3] / "docs" / "metrics-contract.json").read_text())

# Metrics with no documented producer (scripts/validate_dashboard.py
# UNAVAILABLE_DASHBOARD_METRICS) and deprecated aliases stay absent here too.
ABSENT = {
    "truenas_consolemenu_enabled", "truenas_dataset_referenced_bytes",
    "truenas_cloud_backup_task_state", "truenas_directoryservices_account_cache_enabled",
    "truenas_directoryservices_dns_updates_enabled", "truenas_directoryservices_kerberos_configured",
    "truenas_directoryservices_timeout_seconds", "truenas_disk_smart_enabled",
    "truenas_disk_temperature_alert_count", "truenas_fc_port_online", "truenas_fc_port_speed_gbit",
    "truenas_kmip_enabled", "truenas_mail_configured", "truenas_memory_physical_buffers_bytes",
    "truenas_memory_physical_cached_bytes", "truenas_memory_physical_free_bytes",
    "truenas_memory_swap_free_bytes", "truenas_memory_swap_total_bytes",
    "truenas_memory_swap_used_bytes", "truenas_network_httpproxy_configured",
    "truenas_nfs_server_ops_per_second", "truenas_ntp_server_active_count",
    "truenas_ntp_server_reachable_count", "truenas_pool_scrub_last_run_timestamp_seconds",
    "truenas_pool_scrub_task_state", "truenas_pool_vdev_checksum_errors",
    "truenas_pool_vdev_read_errors", "truenas_pool_vdev_write_errors",
    "truenas_smart_test_last_result", "truenas_smart_test_last_timestamp_seconds",
    "truenas_serialconsole_enabled", "truenas_ssh_password_auth",
    "truenas_support_config_enabled", "truenas_task_last_run_timestamp_seconds",
    "truenas_task_state", "truenas_system_security_password_warn_age_days",
    "truenas_tn_connect_enabled", "truenas_tn_connect_status", "truenas_truecommand_status",
    "truenas_ups_configured", "truenas_ups_status", "truenas_virt_global_state",
    "truenas_virt_volume_size_bytes", "truenas_zfs_arc_hit_ratio",
    "truenas_zfs_arc_hits_per_second", "truenas_zfs_arc_max_size_bytes",
    "truenas_zfs_arc_min_size_bytes", "truenas_zfs_arc_misses_per_second",
    "truenas_boot_env_size_bytes", "truenas_certificate_days_to_expiry",
    "truenas_directoryservices_fault_reason", "truenas_network_gateway_reachable",
    "truenas_pool_dedup_ratio", "truenas_pool_expand_size_bytes", "truenas_vm_flag_amd_asids",
}
# Features this demo system does not have: their series are simply absent,
# which is what the real exporter does when a subsystem is not present.
ABSENT_PREFIXES = (
    "truenas_ipmi_", "truenas_ups_", "truenas_failover_", "truenas_fc_",
    "truenas_nvmet_", "truenas_jbof_", "truenas_kmip_", "truenas_vm_vmemory",
    "truenas_gpu_available", "truenas_gpu_uses", "truenas_gpu_info",
    "truenas_job_progress", "truenas_job_oldest", "truenas_api_call_errors_total",
    "truenas_pool_expand_", "truenas_pool_scan_seconds_remaining",
    "truenas_generic_series_limit_hits_total",
)

GiB, TiB = 1024 ** 3, 1024 ** 4
POOLS = {"tank": (43.6 * TiB, 0.72, 11.0), "flash": (3.6 * TiB, 0.38, 3.0)}
HDDS = ["sda", "sdb", "sdc", "sdd", "sde", "sdf"]
SSDS = ["nvme0n1", "nvme1n1"]
USB = ["sdg"]
DISKS = HDDS + SSDS + USB
APPS = ["media-server", "photo-library", "file-sync", "home-automation",
        "dns-filter", "reverse-proxy", "password-vault"]
DATASETS = ["tank", "tank/media", "tank/media/movies", "tank/media/tv", "tank/backups",
            "tank/photos", "tank/documents", "flash", "flash/apps", "flash/vms",
            "flash/apps/media-server", "flash/apps/photo-library"]
IFACES = {"eno1": (1, 1500, 10000), "eno2": (0, 1500, 0), "br0": (1, 9000, 10000)}
SERVICES = {"cifs": (1, 1), "nfs": (1, 1), "ssh": (1, 1), "smartd": (1, 1),
            "ftp": (0, 0), "iscsitarget": (0, 0), "snmp": (0, 0), "ups": (0, 0)}
METHODS = ["pool.query", "disk.query", "app.query", "pool.dataset.query", "alert.list",
           "system.info", "interface.query", "service.query", "sharing.smb.query",
           "update.status", "reporting.realtime", "boot.environment.query",
           "virt.instance.query", "certificate.query", "zfs.snapshot.query"]
TASK_TYPES = {"cloudsync": 2, "replication": 3, "rsync": 0, "pool.snapshottask": 4,
              "pool.scrub": 2, "smart": 2}


def h(*parts) -> float:
    """Deterministic 0..1 from labels (stable across restarts)."""
    d = hashlib.sha1("|".join(map(str, parts)).encode()).digest()
    return int.from_bytes(d[:4], "big") / 2 ** 32


def wave(t, period, phase=0.0, amp=1.0):
    return amp * math.sin(2 * math.pi * (t / period + phase))


def busy(t, key, base, amp, period=1800):
    """Smooth, bounded, plausible utilisation curve."""
    p = h(key)
    v = base + wave(t, period, p, amp) + wave(t, period / 3.7, p * 3, amp * 0.35) \
        + wave(t, 97, p * 7, amp * 0.12)
    return max(0.0, v)


class Gen:
    def __init__(self, profile: str):
        self.profile = profile
        self.p27 = profile == "27"

    def series(self, t: float):
        """Yield (name, labels-dict, value)."""
        out = []
        add = lambda n, v, **l: out.append((n, l, v))  # noqa: E731
        start = t - 1_900_000  # booted ~22 days ago

        # ---- system / host --------------------------------------------
        add("truenas_up", 1)
        add("truenas_system_ready", 1)
        add("truenas_system_state", 1, state="READY")
        add("truenas_host_uptime_seconds", t - start)
        add("truenas_host_cpu_cores", 16)
        add("truenas_host_physical_cpu_cores", 8)
        add("truenas_host_physical_memory_bytes", 64 * GiB)
        add("truenas_host_ecc_memory", 1)
        add("truenas_host_info", 1, hostname="nas-demo",
            version="27.0.0" if self.p27 else "25.10.2", product_type="COMMUNITY_EDITION")
        add("truenas_host_cpu_info", 1, model="Example CPU 8-Core")
        add("truenas_host_system_info", 1, manufacturer="Example Systems", product="Demo Board")
        add("truenas_system_version", 1, version="27.0.0" if self.p27 else "25.10.2")
        add("truenas_system_product_type", 1, product_type="COMMUNITY_EDITION")
        add("truenas_chassis_hardware", 1, model="DEMO-CHASSIS")
        add("truenas_system_global_id", 1, global_id="00000000demo")
        add("truenas_system_host_id", 1, host_id="00000000demo")
        add("truenas_exporter_info", 1, version="5.2.0rc1")
        add("truenas_hw_virt_variant", 1, variant="kvm")
        for w, f in (("1m", 1.0), ("5m", 0.9), ("15m", 0.8)):
            add("truenas_host_load_average", f * busy(t, "load", 3.2, 1.6, 2400), window=w)

        # ---- CPU ------------------------------------------------------
        cores = [busy(t, f"core{c}", 18 + 10 * h("c", c), 12, 1500) for c in range(16)]
        cores = [min(100, c) for c in cores]
        add("truenas_cpu_usage_percent", sum(cores) / 16)
        for c, v in enumerate(cores):
            add("truenas_cpu_core_usage_percent", v, core=str(c))
            add("truenas_cpu_temperature_celsius", 44 + v * 0.35 + 3 * h("tc", c), core=str(c))
        nan = float("nan")
        total = sum(cores) / 16
        add("truenas_cpu_user_percent", nan if self.p27 else total * 0.62)
        add("truenas_cpu_system_percent", nan if self.p27 else total * 0.3)
        add("truenas_cpu_idle_percent", nan if self.p27 else 100 - total)
        add("truenas_cpu_iowait_percent", nan if self.p27 else total * 0.05)
        add("truenas_cpu_interrupt_percent", nan if self.p27 else total * 0.03)

        # ---- memory / ARC -------------------------------------------
        mem_total = 62.7 * GiB
        arc = 30 * GiB + wave(t, 7200, 0.2, 2.5 * GiB)
        services_mem = 14 * GiB + wave(t, 3000, 0.5, 1.5 * GiB)
        used = arc + services_mem
        add("truenas_memory_physical_total_bytes", mem_total)
        add("truenas_memory_physical_used_bytes", used)
        add("truenas_memory_physical_available_bytes", mem_total - services_mem)
        add("truenas_zfs_arc_size_bytes", arc)
        add("truenas_zfs_arc_free_memory_bytes", mem_total - used)
        add("truenas_zfs_arc_available_bytes", 6 * GiB + wave(t, 5000, 0.1, GiB))
        dacc = busy(t, "dacc", 900, 500, 1100)
        macc = busy(t, "macc", 2400, 900, 1300)
        add("truenas_zfs_demand_data_accesses_per_second", dacc)
        add("truenas_zfs_demand_data_hits_per_second", dacc * 0.985)
        add("truenas_zfs_demand_data_misses_per_second", dacc * 0.015)
        add("truenas_zfs_demand_metadata_accesses_per_second", macc)
        add("truenas_zfs_demand_meta_hits_per_second", macc * 0.997)
        add("truenas_zfs_demand_meta_misses_per_second", macc * 0.003)
        add("truenas_zfs_demand_accesses_per_second", dacc + macc)
        add("truenas_zfs_l2arc_accesses_per_second", 0)
        add("truenas_zfs_l2arc_hits_per_second", 0)
        add("truenas_zfs_l2arc_misses_per_second", 0)
        add("truenas_zfs_l2arc_read_bytes_per_second", 0)
        add("truenas_zfs_l2arc_write_bytes_per_second", 0)
        # D2: upstream sends zero percentages/ratios
        for n in ("truenas_zfs_demand_data_hit_ratio", "truenas_zfs_demand_meta_hit_ratio",
                  "truenas_zfs_l2arc_hit_ratio", "truenas_zfs_demand_data_io_hit_ratio",
                  "truenas_zfs_demand_metadata_io_hit_ratio", "truenas_zfs_l2arc_miss_ratio",
                  "truenas_zfs_demand_data_miss_ratio", "truenas_zfs_demand_metadata_miss_ratio"):
            add(n, 0)

        # ---- pools ----------------------------------------------------
        add("truenas_pool_count", len(POOLS))
        for pool, (size, frac, frag) in POOLS.items():
            growth = (t - (time.time() - 6 * 3600)) / 86400 * 0.002  # +0.2 %/day
            alloc = size * (frac + growth)
            add("truenas_pool_size_bytes", size, pool=pool)
            add("truenas_pool_allocated_bytes", alloc, pool=pool)
            add("truenas_pool_free_bytes", size - alloc, pool=pool)
            add("truenas_pool_realtime_total_bytes", size, pool=pool)
            add("truenas_pool_realtime_used_bytes", alloc, pool=pool)
            add("truenas_pool_realtime_available_bytes", size - alloc, pool=pool)
            add("truenas_pool_fragmentation_percent", frag, pool=pool)
            add("truenas_pool_healthy", 1, pool=pool)
            add("truenas_pool_warning", 0, pool=pool)
            add("truenas_pool_status", 1, pool=pool, status="ONLINE")
            add("truenas_pool_status_code", 1, pool=pool, status_code="OK")
            add("truenas_pool_autotrim_enabled", 1 if pool == "flash" else 0, pool=pool)
            add("truenas_pool_dedup_table_size_bytes", 0, pool=pool)
            add("truenas_pool_freeing_bytes", 0, pool=pool)
            add("truenas_pool_features_upgraded", 1, pool=pool)
            add("truenas_pool_resilver_enabled", 1)
            rd = busy(t, "prd" + pool, 60e6 if pool == "tank" else 140e6, 40e6, 900)
            wr = busy(t, "pwr" + pool, 25e6 if pool == "tank" else 70e6, 20e6, 1100)
            if not self.p27:  # 27.0 realtime sends pool capacity only (live-verified)
                add("truenas_pool_realtime_read_bytes_per_second", rd, pool=pool)
                add("truenas_pool_realtime_write_bytes_per_second", wr, pool=pool)
            # D10: tank's finished scrub reports > 100 %
            pct = 101.39 if pool == "tank" else 100.0
            add("truenas_pool_scan_percent", pct, pool=pool)
            add("truenas_pool_scan_state", 1, pool=pool, state="FINISHED")
            add("truenas_pool_scan_function", 1, pool=pool, function="SCRUB")
            add("truenas_pool_scan_errors", 0, pool=pool)
            add("truenas_pool_scan_bytes_processed", alloc, pool=pool)
            add("truenas_pool_scan_bytes_total", alloc, pool=pool)
            add("truenas_pool_last_scan_timestamp_seconds",
                t - (9 if pool == "tank" else 23) * 86400, pool=pool)
            add("truenas_pool_scrub_task_enabled", 1, pool=pool)
        add("truenas_pool_scrub_task_count", 2)

        # ---- boot pool -----------------------------------------------
        add("truenas_boot_pool_healthy", 1)
        add("truenas_boot_pool_size_bytes", 232 * GiB)
        add("truenas_boot_pool_allocated_bytes", 21 * GiB)
        add("truenas_boot_pool_free_bytes", 211 * GiB)
        add("truenas_boot_pool_disk_count", 2)
        add("truenas_boot_pool_status", 1, status="ONLINE")
        add("truenas_boot_pool_scan_state", 1, state="FINISHED")
        add("truenas_boot_pool_scan_percent", 100)
        add("truenas_boot_env_count", 3)
        add("truenas_boot_env_active_count", 1)
        add("truenas_boot_env_activated_count", 1)
        add("truenas_boot_env_keep_count", 1)
        for i, be in enumerate(["27.0.0" if self.p27 else "25.10.2", "25.10.1", "25.04.2"]):
            add("truenas_boot_environment_used_bytes", (6.2 - i * 1.4) * GiB, name=be)
            add("truenas_boot_env_active", 1 if i == 0 else 0, name=be)
            add("truenas_boot_env_activated", 1 if i == 0 else 0, name=be)
            add("truenas_boot_env_keep", 1 if i == 2 else 0, name=be)

        # ---- disks ----------------------------------------------------
        add("truenas_disk_count", len(DISKS))
        for d in DISKS:
            hdd = d in HDDS
            size = 12e12 if hdd else (2e12 if d in SSDS else 0.5e12)
            add("truenas_disk_size_bytes", size, disk=d)
            temp = 0.0 if d in USB else (35 + 6 * h("t", d) + wave(t, 5400, h(d), 1.2)) if hdd \
                else 41 + 5 * h("t", d) + wave(t, 2000, h(d), 2)
            add("truenas_disk_temperature_celsius", temp, disk=d)
            if d not in USB:
                for kind in ("min", "max", "avg"):
                    add("truenas_disk_temperature_agg_celsius",
                        temp + {"min": -2, "max": 2, "avg": 0}[kind], disk=d, kind=kind)
            add("truenas_disk_in_use", 0 if d in USB else 1, disk=d)
            add("truenas_disk_rotational", 1 if hdd else 0, disk=d)
            add("truenas_disk_sed_capable", 0, disk=d)
            add("truenas_disk_sed_status", 1, disk=d, status="UNSUPPORTED")
            add("truenas_disk_info", 1, disk=d, model="DEMO-HDD-12T" if hdd else
                ("DEMO-NVME-2T" if d in SSDS else "DEMO-USB"), serial=f"DEMO{DISKS.index(d):04d}",
                bus="SATA" if hdd else ("NVME" if d in SSDS else "USB"))
        io = {}
        for d in HDDS + SSDS:
            io[d] = dict(
                read_bytes=busy(t, "rb" + d, 12e6 if d in HDDS else 70e6, 9e6, 800),
                write_bytes=busy(t, "wb" + d, 5e6 if d in HDDS else 35e6, 4e6, 950),
                read_ops=busy(t, "ro" + d, 90 if d in HDDS else 1800, 60, 700),
                write_ops=busy(t, "wo" + d, 45 if d in HDDS else 900, 30, 900),
                busy=min(100, busy(t, "bz" + d, 22 if d in HDDS else 9, 14, 1200)))
        names = {"read_bytes": "truenas_disk_read_bytes_per_second",
                 "write_bytes": "truenas_disk_write_bytes_per_second",
                 "read_ops": "truenas_disk_read_ops_per_second",
                 "write_ops": "truenas_disk_write_ops_per_second",
                 "busy": "truenas_disk_busy_percent"}
        for key, metric in names.items():
            if self.p27:  # 27: aggregate only
                vals = [v[key] for v in io.values()]
                add(metric, (sum(vals) / len(vals)) if key == "busy" else sum(vals), disk="total")
            else:
                for d, v in io.items():
                    add(metric, v[key], disk=d)

        # ---- datasets -------------------------------------------------
        add("truenas_dataset_count", len(DATASETS))
        snaps_total = 0
        for i, ds in enumerate(DATASETS):
            pool = ds.split("/")[0]
            size, frac, _ = POOLS[pool]
            share = (0.5 if "/" not in ds else 0.25 * h("u", ds) + 0.02)
            used = size * frac * share
            avail = size * (1 - frac) * (0.2 if "documents" in ds else 1.0)
            add("truenas_dataset_used_bytes", used, dataset=ds)
            add("truenas_dataset_available_bytes", avail, dataset=ds)
            add("truenas_dataset_compression_ratio", 1.0 + 1.3 * h("c", ds), dataset=ds)
            add("truenas_dataset_used_by_snapshots_bytes", used * 0.08 * h("s", ds), dataset=ds)
            add("truenas_dataset_used_by_dataset_bytes", used * 0.9, dataset=ds)
            add("truenas_dataset_used_by_children_bytes", used * 0.1, dataset=ds)
            add("truenas_dataset_logical_used_bytes", used * 1.2, dataset=ds)
            add("truenas_dataset_logical_referenced_bytes", used * 1.1, dataset=ds)
            add("truenas_dataset_reservation_bytes", 0, dataset=ds)
            add("truenas_dataset_refreservation_bytes", 0, dataset=ds)
            add("truenas_dataset_quota_bytes", 2 * TiB if "documents" in ds else 0, dataset=ds)
            add("truenas_dataset_refquota_bytes", 0, dataset=ds)
            # D12: on 27 only the first N datasets get a count (fallback limit)
            if not self.p27 or i < 4:
                n = int(30 * h("n", ds))
                snaps_total += n
                add("truenas_dataset_snapshot_count", n, dataset=ds)
            for flag, val in (("encrypted", 1 if "documents" in ds else 0),
                              ("key_loaded", 1 if "documents" in ds else 0),
                              ("locked", 0), ("readonly", 0), ("atime", 0), ("exec", 1),
                              ("dedup_enabled", 0)):
                add(f"truenas_dataset_{flag}", val, dataset=ds)
            add("truenas_dataset_copies", 1, dataset=ds)
            add("truenas_dataset_recordsize_bytes", 1048576 if "media" in ds else 131072, dataset=ds)
            add("truenas_dataset_creation_timestamp_seconds", start - 86400 * 400 * h("cr", ds), dataset=ds)
            add("truenas_dataset_sync_mode", 1, dataset=ds, mode="STANDARD")
        add("truenas_snapshot_count", 214)
        add("truenas_snapshot_oldest_timestamp_seconds", t - 86400 * 61)

        # ---- network --------------------------------------------------
        add("truenas_interface_count", len(IFACES))
        for i, (ifc, (up, mtu, speed)) in enumerate(IFACES.items()):
            add("truenas_interface_link_up", up, interface=ifc)
            add("truenas_interface_realtime_link_up", up, interface=ifc)
            add("truenas_interface_mtu", mtu, interface=ifc)
            add("truenas_interface_realtime_speed_mbits", speed, interface=ifc)
            add("truenas_interface_type", 1, interface=ifc,
                type="BRIDGE" if ifc.startswith("br") else "PHYSICAL")
            rx = busy(t, "rx" + ifc, 35e6, 30e6, 700) if up else 0
            tx = busy(t, "tx" + ifc, 12e6, 10e6, 800) if up else 0
            add("truenas_network_rx_bytes_per_second", rx, interface=ifc)
            add("truenas_network_tx_bytes_per_second", tx, interface=ifc)
        add("truenas_interface_has_pending_changes", 0)
        add("truenas_interface_checkin_waiting_seconds", float("nan"))
        add("truenas_network_default_gateway_configured", 1)
        add("truenas_network_nameservers", 2)
        add("truenas_network_default_routes", 1)
        add("truenas_dns_resolver_count", 2)
        add("truenas_static_route_count", 0)

        # ---- services & shares ---------------------------------------
        add("truenas_service_count", len(SERVICES))
        for s, (en, run) in SERVICES.items():
            add("truenas_service_enabled", en, service=s)
            add("truenas_service_running", run, service=s)
        for n, v in (("smb_share_count", 6), ("nfs_share_count", 3), ("iscsi_target_count", 0),
                     ("nfs_client_count", 2), ("nfs_v3_client_count", 0), ("nfs_v4_client_count", 2),
                     ("iscsi_client_count", 0), ("smb1_enabled", 0), ("smb_ntlmv1_auth_enabled", 0),
                     ("nfs_rdma_enabled", 0), ("webdav_share_count", 0), ("webshare_enabled", 0),
                     ("iscsi_portal_count", 0), ("iscsi_extent_count", 0), ("iscsi_initiator_count", 0),
                     ("iscsi_session_count", 0), ("iscsi_alua_enabled", 0), ("iscsi_iser_enabled", 0),
                     ("smb_multichannel_enabled", 0), ("nfs_v4_enabled", 1),
                     ("iscsi_session_iser_count", 0), ("iscsi_session_offload_count", 0),
                     ("iscsi_session_immediate_data_count", 0), ("nfs_servers", 8)):
            add("truenas_" + n, v)
        add("truenas_smb_session_count", round(busy(t, "smbs", 4, 3, 3000)))
        add("truenas_smb_connection_count", round(busy(t, "smbc", 5, 3, 3000)))
        add("truenas_smb_open_file_count", round(busy(t, "smbf", 25, 20, 2000)))
        add("truenas_smb_encryption_mode", 1, mode="DEFAULT")

        # ---- apps / docker -------------------------------------------
        add("truenas_app_count", len(APPS))
        add("truenas_app_available_space_bytes", 1.9 * TiB)
        add("truenas_docker_image_count", 14)
        add("truenas_docker_network_count", 9)
        add("truenas_docker_status", 1, status="RUNNING")
        add("truenas_docker_nvidia_present", 0)
        add("truenas_catalog_train_count", 3)
        add("truenas_catalog_preferred_train_count", 1)
        add("truenas_catalog_config_present", 1)
        add("truenas_app_dockerhub_rate_limit_error_present", 0)
        add("truenas_app_dockerhub_pull_limit_remaining", 94)
        add("truenas_app_dockerhub_pull_limit_total", 100)
        add("truenas_app_dockerhub_pull_limit_window_seconds", 21600)
        add("truenas_app_dockerhub_pull_limit_remaining_window_seconds", 21600 - (t % 21600))
        for i, a in enumerate(APPS):
            stopped = a == "password-vault"
            add("truenas_app_state", 1, app=a, state="STOPPED" if stopped else "RUNNING")
            cpu = 0 if stopped else busy(t, "acpu" + a, 1.5 + 6 * h("ac", a), 2.5, 900)
            add("truenas_app_cpu_percent", cpu, app=a)
            add("truenas_app_memory_bytes", 0 if stopped else (0.2 + 2.5 * h("am", a)) * GiB
                + wave(t, 4000, h(a), 0.05 * GiB), app=a)
            n = 1 + int(3 * h("cn", a))
            add("truenas_app_container_count", n, app=a)
            add("truenas_app_container_state_count", 0 if stopped else n, app=a, state="running")
            if stopped:
                add("truenas_app_container_state_count", n, app=a, state="exited")
            add("truenas_app_upgrade_available", 1 if i in (1, 4) else 0, app=a)
            add("truenas_app_image_updates_available", 1 if i == 1 else 0, app=a)
            add("truenas_app_custom", 1 if i == 5 else 0, app=a)
            add("truenas_app_migrated", 0, app=a)
            elapsed = t - 1.7e9  # absolute-time counter: continuous across backfill and live
            add("truenas_app_blkio_read_bytes", elapsed * (2e5 + 1e6 * h("br", a)), app=a)
            add("truenas_app_blkio_write_bytes", elapsed * (1e5 + 5e5 * h("bw", a)), app=a)
            if not stopped:
                add("truenas_app_net_rx_bytes_per_second", busy(t, "arx" + a, 2e5 + 3e6 * h("rx", a), 2e5, 600),
                    app=a, interface="eth0")
                add("truenas_app_net_tx_bytes_per_second", busy(t, "atx" + a, 1e5 + 8e5 * h("tx", a), 1e5, 600),
                    app=a, interface="eth0")

        # ---- virtualisation -------------------------------------------
        add("truenas_vm_count", 0)
        add("truenas_vm_supports_virtualization", 1)
        add("truenas_vm_virtualization_details_supported", 1)
        add("truenas_vm_virtualization_details_error_present", 0)
        add("truenas_vm_maximum_supported_vcpus", 255)
        add("truenas_vm_available_memory_bytes", 18 * GiB)
        add("truenas_iommu_enabled", 1)
        for f in ("intel_vmx", "unrestricted_guest"):
            add("truenas_vm_flag_" + f, 0)
        add("truenas_vm_flag_amd_rvi", 1)
        add("truenas_vm_flag_amd_asids_supported", 1)
        add("truenas_virt_instance_count", 2)
        add("truenas_virt_volume_count", 0)
        for name, typ, run in (("dev-container", "CONTAINER", 1), ("test-vm", "VM", 0)):
            add("truenas_virt_instance_running", run, name=name, type=typ)
            add("truenas_virt_instance_cpu_usage_percent", busy(t, "vi" + name, 4, 3, 900) if run else 0, name=name)
            add("truenas_virt_instance_mem_bytes", (1.4 * GiB + wave(t, 3000, 0.3, 0.1 * GiB)) if run else 0, name=name)

        # ---- alerts / jobs / tasks -----------------------------------
        add("truenas_alert_count", 4)          # D1
        add("truenas_alert_dismissed_count", 3)
        add("truenas_alert_one_shot_count", 1)
        for lvl, n in (("INFO", 2), ("WARNING", 1), ("NOTICE", 1)):
            add("truenas_alert_count_by_level", n, level=lvl)
            add("truenas_alert_last_occurrence_timestamp_seconds", t - 3600 * (1 + 5 * h(lvl)), level=lvl)
        for k, lvl, n in (("ScrubFinished", "INFO", 2), ("SMARTTestFailed", "WARNING", 1),
                          ("AppUpdate", "NOTICE", 1)):
            add("truenas_alert_count_by_class", n, klass=k, level=lvl)
        add("truenas_alert_count_by_source", 4, source="local")
        add("truenas_alert_count_by_node", 4, node="A")
        add("truenas_alert_oldest_timestamp_seconds", t - 86400 * 3)
        add("truenas_alertservice_count", 2)
        add("truenas_alertservice_enabled", 1, name="1", type="Mail")
        add("truenas_alertservice_enabled", 0, name="2", type="Slack")
        add("truenas_job_active_count", 0)
        add("truenas_job_abortable_active_count", 0)
        add("truenas_job_transient_active_count", 0)
        add("truenas_job_active_count_by_state", 0, state="RUNNING")
        for tt, n in TASK_TYPES.items():
            add("truenas_task_count", n, task_type=tt)
        for name, tt, en in (("Offsite media", "cloudsync", 1), ("Offsite photos", "cloudsync", 0),
                             ("Replicate flash", "replication", 1), ("3", "pool.snapshottask", 1),
                             ("4", "pool.snapshottask", 1)):
            add("truenas_task_enabled", en, name=name, task_type=tt)
        add("truenas_cloud_backup_task_count", 1)
        add("truenas_cloud_backup_task_enabled", 1, name="Offsite docs")
        add("truenas_cloud_backup_task_last_completion_timestamp_seconds", t - 86400 * 0.6, name="Offsite docs")
        add("truenas_cloud_backup_task_duration_seconds", 1840, name="Offsite docs")
        add("truenas_cronjob_count", 2)
        add("truenas_cronjob_enabled", 1, name="cleanup")
        add("truenas_cronjob_enabled", 0, name="report")
        add("truenas_system_reboot_required", 0)
        add("truenas_system_boot_changes_total", 0)
        add("truenas_update_available", 0)
        add("truenas_update_status", 1, status="NORMAL")
        add("truenas_update_download_progress_percent", float("nan"))
        add("truenas_update_autocheck_enabled", 1)
        add("truenas_update_profile_info", 1, profile="GENERAL")
        add("truenas_replication_max_parallel", 5)

        # ---- security -------------------------------------------------
        for n, v in (("2fa_enabled", 0), ("ssh_enabled", 1), ("ftp_enabled", 0), ("snmp_enabled", 0),
                     ("fips_enabled", 0), ("fips_available", 0), ("is_production", 0), ("is_ix_hardware", 0),
                     ("support_available_and_enabled", 0), ("support_available", 0),
                     ("managed_by_truecommand", 0), ("kmip_sync_pending", 0),
                     ("system_security_fips_configured", 0), ("system_security_gpos_stig", 0),
                     ("api_key_count", 3), ("api_key_revoked_count", 0), ("local_user_count", 6),
                     ("local_group_count", 41), ("ui_https_port", 443), ("reporting_enabled", 1),
                     ("reporting_exporter_count", 1), ("tunable_count", 2),
                     ("initshutdownscript_count", 0), ("ntp_server_count", 3),
                     ("ntp_server_burst_count", 0), ("ntp_server_iburst_count", 3),
                     ("ntp_server_prefer_count", 0), ("ntp_server_min_poll_minutes", 6),
                     ("ntp_server_max_poll_minutes", 10), ("reporting_tier0_retention_days", 30),
                     ("reporting_tier1_retention_days", 365),
                     ("reporting_tier1_update_interval_seconds", 300), ("filesystem_path_count", 4),
                     ("audit_retention_days", 7), ("audit_remote_logging_enabled", 0),
                     ("audit_quota_fill_warning_percent", 75), ("audit_quota_fill_critical_percent", 95)):
            add("truenas_" + n, v)
        add("truenas_auth_sessions_active", round(busy(t, "sess", 2, 1.4, 4000)))
        add("truenas_system_security_password_min_length", float("nan"))
        add("truenas_system_security_password_max_age_days", float("nan"))
        add("truenas_system_security_password_history_count", float("nan"))
        add("truenas_system_security_password_min_age_days", float("nan"))
        add("truenas_audit_dataset_used_bytes", 380e6)
        add("truenas_audit_dataset_available_bytes", 2.1 * GiB)
        add("truenas_audit_quota_bytes", 0)
        add("truenas_audit_reservation_bytes", 0)
        for c, days in (("truenas_default", 340), ("lan-wildcard", 23)):
            add("truenas_certificate_expiry_timestamp_seconds", t + days * 86400, name=c)
        add("truenas_api_key_expiry_timestamp_seconds", t + 75 * 86400, name="monitoring")
        # D3: directory services intentionally disabled
        add("truenas_directoryservices_status", 1, service="none", status="DISABLED")
        add("truenas_directoryservices_healthy", 0, service="none")
        add("truenas_directoryservices_fault_present", 0, service="none")
        add("truenas_directoryservices_config_enabled", 0)
        add("truenas_gpu_count", 0)

        # ---- exporter -------------------------------------------------
        add("truenas_scrape_duration_seconds", 2.4 + wave(t, 600, 0.1, 0.6) + 0.3 * h(int(t / 60)))
        add("truenas_last_scrape_timestamp_seconds", t - 8)
        for m in METHODS:
            add("truenas_api_call_success", 1, method=m)
            add("truenas_api_call_duration_seconds",
                0.02 + 0.6 * h("d", m) ** 3 + 0.01 * wave(t, 300, h(m)), method=m)
        for f in ("pool_events", "app_stats", "realtime"):
            add("truenas_feature_enabled", 1, feature=f)
        add("truenas_collector_errors_total", 0, collector="api")
        elapsed = t - 1.7e9
        for ev in ("reporting.realtime", "app.stats", "virt.instance.metrics"):
            add("truenas_event_messages_total", elapsed * (0.5 if ev == "reporting.realtime" else 0.2), event=ev)
            add("truenas_event_last_message_timestamp_seconds", t - 2, event=ev)
            add("truenas_event_stream_up", 0 if (self.p27 and ev == "virt.instance.metrics") else 1, event=ev)
        add("truenas_snapshot_task_max_count", 512)
        add("truenas_snapshot_task_max_total_count", 10000)
        add("truenas_certificate_count", 2)
        add("truenas_privilege_count", 4)
        add("truenas_keychain_credential_count", 1)
        add("truenas_systemdataset_pool", 1, pool="flash")
        add("truenas_zfs_demand_data_io_hits_per_second", dacc * 0.004)
        add("truenas_zfs_demand_metadata_io_hits_per_second", macc * 0.001)
        for pool in POOLS:
            add("truenas_pool_scan_paused", 0, pool=pool)
            add("truenas_pool_scan_start_timestamp_seconds", t - 9 * 86400, pool=pool)
            add("truenas_pool_scan_bytes_issued", POOLS[pool][0] * POOLS[pool][1], pool=pool)
        add("truenas_method_boolean_value", 1, method="system.general.config", path="ui_httpsredirect")
        add("truenas_method_numeric_value", 443, method="system.general.config", path="ui_httpsport")
        add("truenas_event_numeric_value", 16, event="reporting.realtime", path="cpu.cores")
        add("truenas_generic_series", 120, source="method")
        add("truenas_generic_series", 40, source="event")
        return out


def fmt_labels(labels: dict) -> str:
    if not labels:
        return ""
    esc = lambda v: str(v).replace("\\", "\\\\").replace('"', '\\"')  # noqa: E731
    return "{" + ",".join(f'{k}="{esc(v)}"' for k, v in sorted(labels.items())) + "}"


def fmt_val(v: float) -> str:
    if v != v:
        return "NaN"
    return repr(float(v))


TYPES = {m["name"]: m["type"] for m in CONTRACT["metrics"]}
LABELS = {m["name"]: m["labels"] for m in CONTRACT["metrics"]}


def render(gen: Gen, t: float, with_ts: bool) -> list[str]:
    by_name: dict = {}
    for name, labels, v in gen.series(t):
        if name in ABSENT or name.startswith(ABSENT_PREFIXES):
            continue
        if name not in TYPES:
            raise SystemExit(f"mock emits unknown metric {name}")
        if sorted(labels) != sorted(LABELS[name]):
            raise SystemExit(f"label mismatch {name}: {sorted(labels)} vs {LABELS[name]}")
        by_name.setdefault(name, []).append((labels, v))
    lines = []
    for name, rows in sorted(by_name.items()):
        typ = TYPES[name]
        base = name[:-6] if typ == "counter" and name.endswith("_total") else name
        lines.append(f"# TYPE {base} {typ}")
        for labels, v in rows:
            if with_ts:  # backfill must match the live scrape's target labels
                labels = {**labels, "instance": "mock:9108", "job": "truenas_exporter"}
            lines.append(f"{name}{fmt_labels(labels)} {fmt_val(v)}" + (f" {int(t)}" if with_ts else ""))
    return lines


def coverage(gen: Gen) -> None:
    emitted = {n for n, _, _ in gen.series(time.time())}
    contract = set(TYPES)
    missing = sorted(n for n in contract - emitted
                     if n not in ABSENT and not n.startswith(ABSENT_PREFIXES))
    print(f"contract={len(contract)} emitted={len(emitted)} not-emitted(non-absent)={len(missing)}")
    for n in missing:
        print("  ", n)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["serve", "dump", "coverage"])
    ap.add_argument("--profile", choices=["27", "25.10"], default="27")
    ap.add_argument("--port", type=int, default=9108)
    ap.add_argument("--hours", type=float, default=6)
    ap.add_argument("--end-offset", type=float, default=3, help="minutes before now")
    ap.add_argument("--step", type=int, default=30)
    ap.add_argument("--out", default="-")
    a = ap.parse_args()
    gen = Gen(a.profile)
    if a.mode == "coverage":
        coverage(gen)
        return
    if a.mode == "dump":
        end = time.time() - a.end_offset * 60
        t = end - a.hours * 3600
        chunks: dict = {}
        order: list = []
        while t <= end:
            lines = render(gen, t, True)
            cur = None
            for ln in lines:
                if ln.startswith("# TYPE"):
                    cur = ln
                    if cur not in chunks:
                        chunks[cur] = []
                        order.append(cur)
                else:
                    chunks[cur].append(ln)
            t += a.step
        out = open(a.out, "w") if a.out != "-" else None
        w = out.write if out else print
        for hdr in order:
            w(hdr + ("\n" if out else ""))
            for ln in chunks[hdr]:
                w(ln + ("\n" if out else ""))
        w("# EOF" + ("\n" if out else ""))
        return

    class H(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            body = ("\n".join(render(gen, time.time(), False)) + "\n").encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    ThreadingHTTPServer(("0.0.0.0", a.port), H).serve_forever()


if __name__ == "__main__":
    main()
