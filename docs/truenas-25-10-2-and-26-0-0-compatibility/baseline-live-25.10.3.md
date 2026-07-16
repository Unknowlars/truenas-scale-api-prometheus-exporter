# Live baseline — TrueNAS SCALE 25.10.3 (pre-v26-upgrade)

Captured read-only from the running production exporter (`/metrics` over HTTP) to
compare against the same deployment after upgrading TrueNAS to 26.0. **Sanitized:**
no API key, URL, hostname, host/boot IDs, serials, IPs, or raw response bodies are
recorded — only metric names/types/help, label *keys*, sample counts, NaN status,
and non-identifying method/collector/event names. The unsanitized `.prom` capture
was kept out of git on purpose.

## Environment

- **target**: TrueNAS SCALE 25.10.3 (live, read-only)
- **detected_version_short**: 25.10.3
- **selected_profile**: 25.10 (target 25.10.2)
- **exporter_version**: 5.2.0
- **python**: 3.14.6
- **mode**: collector (docker)
- **metric families**: 415 | **total series**: 1514 | **all-NaN families**: 51

## Post-upgrade verification checklist (expected v25 → v26 diffs)

Run the *same* exporter/config against the upgraded box and compare:

| Signal | v25.10.3 now | Expected on 26.0 | How to check |
| --- | --- | --- | --- |
| Selected profile | `25.10` | `26.0` | `truenas_system_version{version=...}` → `26.0.x`; logs show profile |
| `virt.instance.query` API call | success=1 (attempted) | **series absent** (suppressed before transport) | `truenas_api_call_success{method="virt.instance.query"}` gone |
| `virt.volume.query` API call | success=1 | **series absent** | same family, method label |
| `nvmet.global.sessions` API call | success=1 | **series absent** | same family, method label |
| `virt.instance.metrics` event | `event_stream_up=1` | **0 / absent** | `truenas_event_stream_up{event=...}` |
| Suppression counters | absent | **> 0** | `truenas_collector_errors_total{collector="profile_removed_method_suppressed"}` and `...profile_removed_event_suppressed` |
| Event subscriptions up | app.stats, reporting.realtime, virt.instance.metrics | **only app.stats + reporting.realtime** | `truenas_event_stream_up` |
| `truenas_vm_available_memory_bytes` | **1.83e16 in this capture (old image, inflated ×1024²)** — corrects to ~1.74e10 once the fixed image is deployed | ~1.74e10 (≈16.2 GiB, correct) | see VM-memory note below |
| Metric family set (415) & label keys | baseline below | unchanged except the above | diff `metric_families` in the JSON |

## ✅ VM available-memory unit anomaly (found here, now FIXED)

This capture was taken from the **old** production image and shows
`truenas_vm_available_memory_bytes` ≈ 1.83e16 (16.2 **PiB**). Root cause: the
pinned 25.10.2 doc (`docs/truenas-api/methods/vm/get_available_memory.md`) states
the return is *"in megabytes"*, but live **25.10.3** actually returns **bytes**
(raw ≈ 1.739e10 = 16.2 GiB, on a 31.3 GiB box). The exporter had faithfully
implemented the documented MB→bytes conversion, so the `25.10` profile multiplied
by 1024² and inflated the metric ~1,048,576×.

**Fixed 2026-07-13:** the `25.10` profile now treats both VM memory methods as
bytes (multiplier `1.0`), matching `26.0`. Live re-verification with the patched
code normalized the same raw value to **16.19 GiB**. So:

- After you **redeploy the fixed image** (still on 25.10.3), this metric already
  reads correctly — there is **no v26 "drop" to worry about** anymore; both
  profiles now emit the same byte value.
- If you compare this *old-image* baseline against a fixed deployment, expect
  `truenas_vm_available_memory_bytes` to fall by ~1024² — that is this fix, not a
  regression.

(`vm.get_vmemory_in_use` reads `{RNP:0,PRD:0,RPRD:0}` here — no running VMs — so
its gauges are 0 and won't demonstrate the unit change until VMs are running.)

## API methods attempted (all success=1): 117

These method series should stay success=1 on 26.0 **except** the three removed ones
above, which should vanish entirely. Full list is in `baseline-live-25.10.3.json`.

## Families reporting all-NaN on 25.10.3 (51)

These are the documented-unavailable declarations (no reachable 25.10 producer). On
26.0 the removed-source families may join this set; none should flip to a fabricated 0.

- `truenas_consolemenu_enabled`
- `truenas_cpu_interrupt_percent`
- `truenas_cpu_iowait_percent`
- `truenas_cpu_system_percent`
- `truenas_directoryservices_account_cache_enabled`
- `truenas_directoryservices_dns_updates_enabled`
- `truenas_directoryservices_kerberos_configured`
- `truenas_directoryservices_timeout_seconds`
- `truenas_filesystem_path_count`
- `truenas_interface_checkin_waiting_seconds`
- `truenas_ipmi_chassis_drive_fault`
- `truenas_ipmi_chassis_fan_fault`
- `truenas_ipmi_chassis_intrusion`
- `truenas_ipmi_chassis_power_on`
- `truenas_ipmi_chassis_power_overload`
- `truenas_ipmi_sel_entry_count`
- `truenas_ipmi_sel_free_space_bytes`
- `truenas_kmip_enabled`
- `truenas_mail_configured`
- `truenas_memory_physical_buffers_bytes`
- `truenas_memory_physical_cached_bytes`
- `truenas_memory_physical_free_bytes`
- `truenas_memory_swap_free_bytes`
- `truenas_memory_swap_total_bytes`
- `truenas_memory_swap_used_bytes`
- `truenas_network_httpproxy_configured`
- `truenas_nfs_server_ops_per_second`
- `truenas_ntp_server_active_count`
- `truenas_ntp_server_reachable_count`
- `truenas_serialconsole_enabled`
- `truenas_smb_connection_count`
- `truenas_smb_open_file_count`
- `truenas_smb_session_count`
- `truenas_snapshot_oldest_timestamp_seconds`
- `truenas_ssh_password_auth`
- `truenas_support_config_enabled`
- `truenas_system_security_password_history_count`
- `truenas_system_security_password_max_age_days`
- `truenas_system_security_password_min_age_days`
- `truenas_system_security_password_min_length`
- `truenas_system_security_password_warn_age_days`
- `truenas_tn_connect_enabled`
- `truenas_ups_configured`
- `truenas_virt_instance_count`
- `truenas_virt_volume_count`
- `truenas_webdav_share_count`
- `truenas_zfs_arc_hit_ratio`
- `truenas_zfs_arc_hits_per_second`
- `truenas_zfs_arc_max_size_bytes`
- `truenas_zfs_arc_min_size_bytes`
- `truenas_zfs_arc_misses_per_second`

---
Machine-readable companion: `baseline-live-25.10.3.json` (summary, full api_call_success map, collector errors, and the 415-family inventory with label keys).
