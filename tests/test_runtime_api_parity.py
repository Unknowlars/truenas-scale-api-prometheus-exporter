"""Fixture-backed runtime regressions for the TrueNAS 25.10.2 parity audit."""

from __future__ import annotations

import json
import math
import time
from pathlib import Path
from typing import Any

import pytest
from conftest import make_config

import truenas_exporter as runtime
from truenas_exporter.compat_profiles import PROFILE_25_10, PROFILE_26_0, PROFILE_UNKNOWN

FIXTURES = Path(__file__).parent / "fixtures" / "api_25_10_2"
FIXTURES_V26 = Path(__file__).parent / "fixtures" / "api_26_0_0"


def fixture(name: str) -> Any:
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def fixture_v26(name: str) -> Any:
    return json.loads((FIXTURES_V26 / name).read_text(encoding="utf-8"))


def value(metric: Any) -> float:
    return metric._value.get()


def labeled(metric: Any, *labels: str) -> float:
    return metric.labels(*labels)._value.get()


def test_realtime_zfs_fields_zero_stale_and_recovery() -> None:
    exporter = runtime.TrueNASExporter(make_config())
    full = fixture("reporting_realtime_full.json")["fields"]
    zero = fixture("reporting_realtime_zero.json")["fields"]

    field_metrics = {
        "demand_accesses_per_second": runtime.ZFS_DEMAND_ACCESSES_RATE,
        "demand_data_accesses_per_second": runtime.ZFS_DEMAND_DATA_ACCESSES_RATE,
        "demand_data_hits_per_second": runtime.ZFS_DEMAND_DATA_HITS_RATE,
        "demand_data_io_hits_per_second": runtime.ZFS_DEMAND_DATA_IO_HITS_RATE,
        "demand_data_misses_per_second": runtime.ZFS_DEMAND_DATA_MISSES_RATE,
        "demand_metadata_accesses_per_second": runtime.ZFS_DEMAND_META_ACCESSES_RATE,
        "demand_metadata_hits_per_second": runtime.ZFS_DEMAND_META_HITS_RATE,
        "demand_metadata_io_hits_per_second": runtime.ZFS_DEMAND_META_IO_HITS_RATE,
        "demand_metadata_misses_per_second": runtime.ZFS_DEMAND_META_MISSES_RATE,
        "l2arc_hits_per_second": runtime.ZFS_L2ARC_HITS_RATE,
        "l2arc_misses_per_second": runtime.ZFS_L2ARC_MISSES_RATE,
        "total_l2arc_accesses_per_second": runtime.ZFS_L2ARC_ACCESSES_RATE,
        "bytes_read_per_second_from_the_l2arc": runtime.ZFS_L2ARC_READ_BYTES_RATE,
        "bytes_written_per_second_to_the_l2arc": runtime.ZFS_L2ARC_WRITE_BYTES_RATE,
    }
    percentage_metrics = {
        "demand_data_hit_percentage": runtime.ZFS_DEMAND_DATA_HIT_RATIO,
        "demand_data_io_hit_percentage": runtime.ZFS_DEMAND_DATA_IO_HIT_RATIO,
        "demand_data_miss_percentage": runtime.ZFS_DEMAND_DATA_MISS_RATIO,
        "demand_metadata_hit_percentage": runtime.ZFS_DEMAND_META_HIT_RATIO,
        "demand_metadata_io_hit_percentage": runtime.ZFS_DEMAND_META_IO_HIT_RATIO,
        "demand_metadata_miss_percentage": runtime.ZFS_DEMAND_META_MISS_RATIO,
        "l2arc_access_hit_percentage": runtime.ZFS_L2ARC_HIT_RATIO,
        "l2arc_miss_percentage": runtime.ZFS_L2ARC_MISS_RATIO,
    }

    exporter._dispatch_event("reporting.realtime", full)
    for field, metric in field_metrics.items():
        assert exporter._collector_event_scalars[metric._name] == full["zfs"][field]
    for field, metric in percentage_metrics.items():
        assert exporter._collector_event_scalars[metric._name] == full["zfs"][field] / 100

    exporter._dispatch_event("reporting.realtime", zero)
    for metric in (*field_metrics.values(), *percentage_metrics.values()):
        assert exporter._collector_event_scalars[metric._name] == 0

    exporter._event_last_monotonic["reporting.realtime"] = (
        time.monotonic() - exporter.config.event_stale_after_seconds - 1
    )
    exporter._expire_stale_events()
    assert "reporting.realtime" in exporter._expired_events
    assert not exporter._event_is_fresh("reporting.realtime")

    exporter._dispatch_event("reporting.realtime", full)
    assert "reporting.realtime" not in exporter._expired_events
    assert exporter._event_is_fresh("reporting.realtime")


class _Client:
    def __enter__(self) -> _Client:
        return self

    def __exit__(self, *_args: Any) -> None:
        return None

    def authenticate(self, _api_key: str, call: Any = None) -> None:
        if call is not None:
            call("auth.login_with_api_key", [])


def test_main_scrape_uses_documented_params_units_and_nested_shapes(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, Any]] = []
    pool = fixture("pool_query.json")
    pool[0]["dedup_table_size"] = {"parsed": 1048576}
    pool[0]["scan"]["bytes_processed"] = {"value": 0}
    pool[0]["scan"]["bytes_to_process"] = {"parsed": 0}
    disks = fixture("disk_query_selected.json")
    update = fixture("update_status_normal.json")
    vmemory = fixture("vm_get_vmemory_in_use.json")
    vmemory["UNDOCUMENTED"] = 999

    exporter = runtime.TrueNASExporter(
        make_config(enable_dataset_metrics=False, enable_task_metrics=False)
    )
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: _Client())

    def fake_call(_client: Any, method: str, params: Any = None) -> Any:
        calls.append((method, params))
        if method == "auth.login_with_api_key":
            return True
        if (
            isinstance(params, list)
            and len(params) > 1
            and isinstance(params[1], dict)
            and params[1].get("count")
        ):
            return 0
        responses: dict[str, Any] = {
            "system.version_short": "25.10.2",
            "system.state": "READY",
            "system.ready": False,
            "system.info": {
                "hostname": "synthetic-nas",
                "version": "TrueNAS-SCALE-25.10.2",
                "uptime_seconds": 0,
                "physmem": 0,
                "cores": 0,
                "physical_cores": 0,
                "loadavg": [0, 0, 0],
                "ecc_memory": False,
            },
            "system.product_type": "SCALE",
            "vm.get_available_memory": fixture("vm_get_available_memory.json"),
            "vm.get_vmemory_in_use": vmemory,
            "pool.query": pool,
            "disk.query": disks,
            "disk.temperatures": {"sda": 0, "nvme0n1": None},
            "disk.temperature_agg": {},
            "interface.query": [
                {
                    "name": "enp1s0",
                    "type": "PHYSICAL",
                    "mtu": 1500,
                    "state": {"link_state": "LINK_STATE_DOWN", "mtu": 9000},
                }
            ],
            "service.query": [],
            "alert.list": [],
            "update.status": update,
        }
        if method in responses:
            return responses[method]
        raise runtime.JsonRpcError(f"optional fixture method unavailable: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)
    exporter.scrape_once()

    assert value(runtime.SCRAPE_SUCCESS) == 1
    assert value(runtime.SYSTEM_READY) == 0
    assert labeled(runtime.HOST_INFO, "synthetic-nas", "TrueNAS-SCALE-25.10.2", "SCALE") == 1
    # 25.10 VM memory methods return bytes on live systems (see compat_profiles);
    # the profile multiplier is 1.0, so values pass through unchanged.
    assert value(runtime.VM_AVAILABLE_MEMORY_BYTES) == 8192
    assert labeled(runtime.VM_VMEMORY_IN_USE_BYTES, "RNP") == 0
    assert labeled(runtime.VM_VMEMORY_IN_USE_BYTES, "PRD") == 1024
    vmemory_states = {
        sample.labels["state"]
        for sample in list(runtime.VM_VMEMORY_IN_USE_BYTES.collect())[0].samples
    }
    assert vmemory_states == {"RNP", "PRD", "RPRD"}
    assert labeled(runtime.POOL_FRAGMENTATION, "tank") == 0
    assert labeled(runtime.POOL_DEDUP_TABLE_SIZE_BYTES, "tank") == 1048576
    assert labeled(runtime.POOL_SCAN_BYTES_PROCESSED, "tank") == 0
    assert labeled(runtime.POOL_SCAN_BYTES_TOTAL, "tank") == 0
    assert labeled(runtime.POOL_EXPAND_REFLOWED_BYTES, "tank") == 978944
    assert labeled(runtime.POOL_EXPAND_TO_REFLOW_BYTES, "tank") == 835584
    assert labeled(runtime.POOL_EXPAND_PERCENT, "tank") == pytest.approx(85.35564853556485)
    assert labeled(runtime.DISK_TEMPERATURE_C, "sda") == 0
    assert labeled(runtime.INTERFACE_MTU, "enp1s0") == 9000
    assert labeled(runtime.UPDATE_STATUS, "NORMAL") == 1
    assert value(runtime.UPDATE_AVAILABLE) == 1
    assert value(runtime.UPDATE_DOWNLOAD_PROGRESS_PERCENT) == 0

    assert ("vm.get_available_memory", [False]) in calls
    assert ("disk.temperatures", [["sda", "nvme0n1"], False]) in calls
    assert not any(method in {"smb.status", "smart.test.results"} for method, _ in calls)

    update["status"] = {}
    exporter.scrape_once()
    assert math.isnan(value(runtime.UPDATE_AVAILABLE))


def test_documented_owned_collectors_and_secret_exclusions(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[tuple[str, Any]] = []
    exporter = runtime.TrueNASExporter(make_config(enable_ipmi_metrics=True))

    def fake_call(_client: Any, method: str, params: Any = None) -> Any:
        calls.append((method, params))
        if method == "service.query":
            return [
                {"service": "ssh", "enable": False},
                {"service": "ftp", "enable": False},
                {"service": "snmp", "enable": False},
            ]
        if method == "smb.config":
            return {
                "multichannel": False,
                "enable_smb1": False,
                "ntlmv1_auth": False,
                "encryption": "REQUIRED",
            }
        if method == "nfs.config":
            return fixture("nfs_config.json")
        if method == "directoryservices.status":
            return fixture("directoryservices_status.json")
        if method == "ipmi.is_loaded":
            return True
        if method == "ipmi.chassis.info":
            return fixture("ipmi_chassis_info.json")
        if method == "ipmi.sel.info":
            return fixture("ipmi_sel_info.json")
        if method == "device.get_info":
            return fixture("device_get_info_gpu.json")
        if method == "vm.device.iommu_enabled":
            return False
        if method == "auth.twofactor.config":
            return {"enabled": False}
        if method == "alertservice.query":
            if params[1].get("count"):
                return 1
            return [{"id": 7, "type__title": "Mail", "enabled": False}]
        if method == "system.ntpserver.query":
            if params[1].get("count"):
                return 2
            return fixture("system_ntpserver_query.json")
        if method in {"app.image.query", "dns.query", "reporting.exporters.query"}:
            return 0
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 1}
        if method == "reporting.config":
            return {"tier0_days": 7, "tier1_days": 30, "tier1_update_interval": 300}
        raise runtime.JsonRpcError(f"optional fixture method unavailable: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)
    monkeypatch.setattr(
        exporter,
        "_safe_call_auto",
        lambda client, method: fixture("system_security_config.json")
        if method == "system.security.config"
        else None,
    )

    exporter._collect_protocol_configs(object(), {})
    exporter._collect_directoryservices_metrics(object(), {})
    exporter._collect_ipmi_metrics(object())
    exporter._collect_gpu_metrics(object())
    exporter._collect_app_extras(
        object(), {"app.image.dockerhub_rate_limit": fixture("dockerhub_rate_limit.json")}
    )
    exporter._collect_misc_configs(object(), {"reporting.config": {}})
    exporter._collect_security_posture(
        object(), {"system.security.config": fixture("system_security_config.json")}
    )
    exporter._collect_system_configs(
        object(), {"system.general.config": {"ui_httpsport": 443}}
    )

    assert value(runtime.SMB1_ENABLED) == 0
    assert value(runtime.SMB_NTLMV1_AUTH_ENABLED) == 0
    assert labeled(runtime.SMB_ENCRYPTION_MODE, "REQUIRED") == 1
    assert value(runtime.NFS_V4_ENABLED) == 1
    assert value(runtime.NFS_RDMA_ENABLED) == 0
    assert labeled(runtime.DIRECTORYSERVICES_FAULT_PRESENT, "activedirectory") == 1
    assert labeled(runtime.DIRECTORYSERVICES_FAULT_REASON, "activedirectory", "redacted") == 1
    assert value(runtime.IPMI_CHASSIS_POWER_ON) == 1
    assert value(runtime.IPMI_CHASSIS_FAN_FAULT) == 0
    assert value(runtime.IPMI_SEL_ENTRY_COUNT) == 0
    assert value(runtime.IPMI_SEL_FREE_SPACE_BYTES) == 1024
    assert labeled(runtime.GPU_INFO, "0", "Synthetic GPU", "Synthetic Vendor", "10de:0000") == 1
    assert labeled(runtime.GPU_AVAILABLE_TO_HOST, "0") == 1
    assert labeled(runtime.GPU_USES_CRITICAL_DEVICES, "0") == 0
    assert value(runtime.APP_DOCKERHUB_PULL_LIMIT_REMAINING) == 0
    assert value(runtime.SYSTEM_SECURITY_FIPS_CONFIGURED) == 0
    assert value(runtime.SYSTEM_SECURITY_GPOS_STIG) == 1
    assert math.isnan(value(runtime.SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS))
    assert value(runtime.NTP_SERVER_MIN_POLL_MINUTES) == pytest.approx(2**6 / 60)
    assert value(runtime.NTP_SERVER_MAX_POLL_MINUTES) == pytest.approx(2**12 / 60)
    assert value(runtime.UI_HTTPS_PORT) == 443
    assert math.isnan(value(runtime.NTP_SERVER_ACTIVE_COUNT))
    assert math.isnan(value(runtime.NTP_SERVER_REACHABLE_COUNT))

    assert ("ipmi.chassis.info", [{}]) in calls
    assert any(
        method == "system.ntpserver.query"
        and params[1].get("select") == ["prefer", "burst", "iburst", "minpoll", "maxpoll"]
        for method, params in calls
        if isinstance(params, list) and len(params) > 1 and isinstance(params[1], dict)
    )
    forbidden = {
        "directoryservices.config",
        "kmip.config",
        "mail.config",
        "network.configuration.config",
        "snmp.config",
        "ssh.config",
        "support.config",
        "system.advanced.config",
        "tn_connect.config",
        "truecommand.config",
        "ups.config",
    }
    assert forbidden.isdisjoint(method for method, _ in calls)


def test_generic_secret_paths_method_safety_and_poll_reset(monkeypatch: pytest.MonkeyPatch) -> None:
    exporter = runtime.TrueNASExporter(make_config(enable_generic_method_metrics=True))
    runtime.METHOD_NUMERIC_VALUE.clear()
    exporter._extract_generic_metrics(
        "system.info",
        {
            "password": "123456",
            "description": "42",
            "config": {"unrecognized_secret_name": 99},
            "nested": {"refresh_token": "789", "safe": "5"},
        },
        "result",
        0,
    )
    samples = list(runtime.METHOD_NUMERIC_VALUE.collect())[0].samples
    assert len(samples) == 1
    assert samples[0].labels["path"].endswith("safe")
    assert samples[0].value == 5

    assert exporter._is_safe_read_method("system.ready")
    for method in (
        "boot.scrub",
        "pool.dataset.rename",
        "app.pull_images",
        "mail.config",
        "custom.status",
        "core.get_jobs",
        "jbof.query",
        "nvmet.host.query",
        "pool.get_disks",
        "pool.query",
        "system.advanced.config",
        "virt.instance.query",
    ):
        assert not exporter._is_safe_read_method(method)

    runtime.UPDATE_AVAILABLE.set(1)
    runtime.POOL_SIZE_BYTES.labels(pool="tank").set(1)
    exporter._reset_poll_metrics()
    assert math.isnan(value(runtime.UPDATE_AVAILABLE))
    assert not list(runtime.POOL_SIZE_BYTES.collect())[0].samples

    monkeypatch.setattr(
        exporter,
        "_call",
        lambda *_args, **_kwargs: pytest.fail("undocumented method must not be called"),
    )
    exporter._collect_smb_nfs_sessions(object())
    exporter._collect_smart_test_results(object())


def test_malformed_and_sparse_events_replace_prior_snapshots() -> None:
    exporter = runtime.TrueNASExporter(
        make_config(exporter_mode="legacy", enable_generic_event_metrics=True)
    )
    full = fixture("reporting_realtime_full.json")["fields"]

    exporter._dispatch_event("reporting.realtime", full)
    assert runtime.ZFS_DEMAND_ACCESSES_RATE._name in exporter._collector_event_scalars
    assert runtime.ZFS_L2ARC_HITS_RATE._name in exporter._collector_event_scalars

    exporter._dispatch_event(
        "reporting.realtime", {"zfs": {"demand_accesses_per_second": 0}}
    )
    assert exporter._collector_event_scalars[runtime.ZFS_DEMAND_ACCESSES_RATE._name] == 0
    assert runtime.ZFS_L2ARC_HITS_RATE._name not in exporter._collector_event_scalars

    exporter._dispatch_event("reporting.realtime", {})
    assert runtime.ZFS_DEMAND_ACCESSES_RATE._name not in exporter._collector_event_scalars
    assert not exporter._event_is_fresh("reporting.realtime")
    assert math.isnan(value(runtime.ZFS_DEMAND_ACCESSES_RATE))

    exporter._dispatch_event(
        "app.stats", {"fields": [{"app_name": "demo", "cpu_usage": 1}]}
    )
    assert exporter._collector_event_series[runtime.APP_CPU_PERCENT._name]
    exporter._dispatch_event("app.stats", {"fields": "malformed"})
    assert runtime.APP_CPU_PERCENT._name not in exporter._collector_event_series
    assert not exporter._event_is_fresh("app.stats")


def test_generic_event_series_expire_and_malformed_gpu_booleans_are_absent(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(
        make_config(exporter_mode="legacy", enable_generic_event_metrics=True)
    )
    runtime.EVENT_NUMERIC_VALUE.clear()
    exporter._dispatch_event("service.query", {"safe": 7})
    assert any(
        sample.labels.get("event") == "service.query"
        for sample in list(runtime.EVENT_NUMERIC_VALUE.collect())[0].samples
    )
    exporter._expire_stale_events(force=True)
    assert not any(
        sample.labels.get("event") == "service.query"
        for sample in list(runtime.EVENT_NUMERIC_VALUE.collect())[0].samples
    )

    monkeypatch.setattr(
        exporter,
        "_call",
        lambda _client, method, _params=None: [
            {
                "description": "Sparse GPU",
                "vendor": "Synthetic",
                "devices": [],
                "available_to_host": 2,
                "uses_system_critical_devices": -1,
            }
        ]
        if method == "device.get_info"
        else pytest.fail(f"unexpected call: {method}"),
    )
    exporter._collect_gpu_metrics(object())
    assert not list(runtime.GPU_AVAILABLE_TO_HOST.collect())[0].samples
    assert not list(runtime.GPU_USES_CRITICAL_DEVICES.collect())[0].samples


def test_profile_vm_memory_units_and_malformed_values() -> None:
    v25 = runtime.TrueNASExporter(make_config(), compatibility_profile=PROFILE_25_10)
    v26 = runtime.TrueNASExporter(make_config(), compatibility_profile=PROFILE_26_0)
    unknown = runtime.TrueNASExporter(make_config(), compatibility_profile=PROFILE_UNKNOWN)

    # 25.10 returns bytes (live-verified); multiplier is 1.0, values pass through.
    assert v25._profile_normalized_bytes("vm.get_available_memory", 8192) == 8192
    assert v25._profile_normalized_bytes("vm.get_vmemory_in_use", {"parsed": 1024}) == 1024

    v26_available = fixture_v26("vm_get_available_memory.json")
    v26_vmemory = fixture_v26("vm_get_vmemory_in_use.json")
    assert v26._profile_normalized_bytes("vm.get_available_memory", v26_available) == 8589934592
    assert v26._profile_normalized_bytes("vm.get_vmemory_in_use", v26_vmemory["PRD"]) == 1073741824
    assert unknown._profile_normalized_bytes("vm.get_available_memory", v26_available) == 8589934592

    for malformed in (None, False, -1, float("nan"), float("inf"), "not-a-number"):
        assert v26._profile_normalized_bytes("vm.get_available_memory", malformed) is None


def test_bounded_dataset_and_app_shape_normalizers(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(
        make_config(enable_dataset_metrics=True, enable_task_metrics=False)
    )

    dataset = {
        "name": "tank/v26",
        "properties": {
            "used": {"parsed": 123},
            "available": {"value": 456},
            "quota": {"rawvalue": 0},
            "compressratio": {"parsed": "1.25x"},
            "readonly": {"parsed": False},
            "encrypted": {"parsed": True},
            "creation": {"parsed": "2026-01-01T00:00:00Z"},
        },
    }

    monkeypatch.setattr(
        exporter,
        "_call",
        lambda _client, method, _params=None: [dataset]
        if method == "pool.dataset.query"
        else pytest.fail(f"unexpected dataset call: {method}"),
    )
    monkeypatch.setattr(exporter, "_query_count", lambda *_args, **_kwargs: 1)
    exporter._collect_dataset_metrics(object())

    assert labeled(runtime.DATASET_USED_BYTES, "tank/v26") == 123
    assert labeled(runtime.DATASET_AVAILABLE_BYTES, "tank/v26") == 456
    assert labeled(runtime.DATASET_QUOTA_BYTES, "tank/v26") == 0
    assert labeled(runtime.DATASET_COMPRESSION_RATIO, "tank/v26") == 1.25
    assert labeled(runtime.DATASET_READONLY, "tank/v26") == 0
    assert labeled(runtime.DATASET_ENCRYPTED, "tank/v26") == 1
    assert labeled(runtime.DATASET_CREATION_TS, "tank/v26") == 1767225600

    app = {
        "name": "demo",
        "state": {"value": "RUNNING"},
        "properties": {
            "upgrade_available": {"parsed": False},
            "image_updates_available": {"parsed": True},
            "custom_app": None,
            "migrated": {"value": False},
            "active_workloads": {
                "properties": {
                    "containers": {"parsed": 2},
                    "used_ports": [8080],
                    "used_host_ips": ["127.0.0.1"],
                    "container_details": [{"state": "running"}, {"state": None}],
                },
            },
        },
    }
    monkeypatch.setattr(exporter, "_safe_call_auto", lambda _client, method: [] if method == "vm.query" else [app])
    monkeypatch.setattr(exporter, "_query_count", lambda _client, method, *_args, **_kwargs: 0 if method == "vm.query" else 1)
    exporter._collect_entity_detail_metrics(object(), {})

    assert labeled(runtime.APP_STATE, "demo", "RUNNING") == 1
    assert labeled(runtime.APP_UPGRADE_AVAILABLE, "demo") == 0
    assert labeled(runtime.APP_IMAGE_UPDATES_AVAILABLE, "demo") == 1
    assert labeled(runtime.APP_MIGRATED, "demo") == 0
    assert labeled(runtime.APP_CONTAINER_COUNT, "demo") == 2
    assert labeled(runtime.APP_USED_PORT_COUNT, "demo") == 1
    assert labeled(runtime.APP_USED_HOST_IP_COUNT, "demo") == 1
    assert labeled(runtime.APP_CONTAINER_STATE_COUNT, "demo", "RUNNING") == 1


@pytest.mark.parametrize(
    "malformed",
    [False, -1, 1.5, "2", {"parsed": 2}, float("nan"), float("inf")],
)
def test_count_query_rejects_non_integer_or_negative_shapes(
    monkeypatch: pytest.MonkeyPatch, malformed: Any
) -> None:
    exporter = runtime.TrueNASExporter(make_config())
    monkeypatch.setattr(exporter, "_call", lambda *_args, **_kwargs: malformed)
    with pytest.raises(TypeError, match="nonnegative integer"):
        exporter._query_count(object(), "pool.query")


class _BootstrapClient:
    def __init__(self, version_result: Any = "25.10.2", version_error: Exception | None = None) -> None:
        self.version_result = version_result
        self.version_error = version_error
        self.calls: list[tuple[str, Any]] = []

    def authenticate(self, _api_key: str, call: Any = None) -> None:
        if call is not None:
            call("auth.login_with_api_key", ["redacted-test-key"])

    def call(self, method: str, params: Any = None) -> Any:
        self.calls.append((method, params))
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            if self.version_error is not None:
                raise self.version_error
            return self.version_result
        raise AssertionError(f"unexpected bootstrap call: {method}")


@pytest.mark.parametrize(
    ("version", "expected_profile"),
    [
        ("25.10.2", PROFILE_25_10),
        ("TrueNAS-SCALE-25.10.3", PROFILE_25_10),
        ("26.0.0", PROFILE_26_0),
        ("TrueNAS-SCALE-26.0.1", PROFILE_26_0),
        ("27.1.0", PROFILE_UNKNOWN),
    ],
)
def test_bootstrap_version_detection_selects_profile_once(
    version: str, expected_profile: Any
) -> None:
    exporter = runtime.TrueNASExporter(make_config())
    client = _BootstrapClient(version)

    assert exporter._bootstrap_connection(client) == version
    assert exporter.compatibility_profile is expected_profile
    assert client.calls == [
        ("auth.login_with_api_key", ["redacted-test-key"]),
        ("system.version_short", []),
    ]


def test_bootstrap_malformed_and_failed_detection_fall_back_without_expanding_access(
    caplog: pytest.LogCaptureFixture,
) -> None:
    secret = "sensitive-api-key-value"
    blocked_methods = {
        "virt.instance.query",
        "virt.volume.query",
        "nvmet.global.sessions",
        "reporting.graphs",
        "reporting.netdata_graphs",
    }

    for client in (
        _BootstrapClient({"version": "25.10.2", "token": secret}),
        _BootstrapClient(version_error=RuntimeError(f"boom {secret}")),
    ):
        exporter = runtime.TrueNASExporter(
            make_config(
                auto_discover_methods=True,
                extra_methods=sorted(blocked_methods),
                event_subscriptions=["virt.instance.metrics", "app.stats"],
                enable_generic_method_metrics=True,
            )
        )
        with caplog.at_level("DEBUG", logger="truenas_exporter"):
            exporter._bootstrap_connection(client)

        assert exporter.compatibility_profile is PROFILE_UNKNOWN
        assert blocked_methods.isdisjoint(exporter._discover_methods(object()))
        assert not exporter.compatibility_profile.allows_event("virt.instance.metrics")
        assert exporter.compatibility_profile.allows_event("app.stats")

        recorder = _BootstrapClient("unused")
        for method in blocked_methods:
            with pytest.raises(RuntimeError, match="outside"):
                exporter._call(recorder, method, [])
        assert recorder.calls == []

    assert secret not in caplog.text


def test_profile_gate_blocks_removed_and_prohibited_calls_before_client() -> None:
    class RecordingClient:
        calls: list[tuple[str, Any]] = []

        def call(self, method: str, params: Any = None) -> Any:
            self.calls.append((method, params))
            return 0

    for profile in (PROFILE_26_0, PROFILE_UNKNOWN):
        exporter = runtime.TrueNASExporter(make_config(), compatibility_profile=profile)
        client = RecordingClient()
        for method in (
            "virt.instance.query",
            "virt.volume.query",
            "nvmet.global.sessions",
            "reporting.graphs",
            "reporting.netdata_graphs",
            "pool.is_upgraded",
            "pool.ddt_prefetch",
        ):
            with pytest.raises(RuntimeError, match="outside"):
                exporter._call(client, method, [])
            with pytest.raises(RuntimeError, match="outside"):
                exporter._query_count(client, method)
        assert client.calls == []

    v25_exporter = runtime.TrueNASExporter(make_config(), compatibility_profile=PROFILE_25_10)
    client = RecordingClient()
    assert v25_exporter._query_count(client, "virt.instance.query") == 0
    assert client.calls == [("virt.instance.query", [[], {"count": True}])]


def test_profile_gate_filters_extra_discovered_reporting_and_count_queries(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(
        make_config(
            auto_discover_methods=True,
            extra_methods=[
                "app.image.query",
                "virt.instance.query",
                "reporting.graphs",
                "pool.is_upgraded",
            ],
            enable_generic_method_metrics=True,
        ),
        compatibility_profile=PROFILE_26_0,
    )

    def fake_safe_call(_client: Any, method: str) -> Any:
        if method == "core.get_methods":
            return {
                "app.image.query": {},
                "virt.instance.query": {},
                "reporting.netdata_graphs": {},
                "pool.ddt_prefetch": {},
            }
        return None

    monkeypatch.setattr(exporter, "_safe_call_auto", fake_safe_call)
    discovered = exporter._discover_methods(object())

    assert "app.image.query" not in discovered
    assert "virt.instance.query" not in discovered
    assert "reporting.graphs" not in discovered
    assert "reporting.netdata_graphs" not in discovered
    assert "pool.is_upgraded" not in discovered
    assert "pool.ddt_prefetch" not in discovered

    calls: list[tuple[str, Any]] = []

    class Client:
        def call(self, method: str, params: Any = None) -> int:
            calls.append((method, params))
            return 0

    assert exporter._query_count(Client(), "app.image.query") == 0
    assert calls == [("app.image.query", [[], {"count": True}])]
    calls.clear()

    with pytest.raises(RuntimeError, match="outside"):
        exporter._query_count(Client(), "virt.instance.query")
    assert calls == []


def test_profile_gate_blocks_v26_removed_event_subscription(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    attempts: list[tuple[str, Any]] = []

    class EventClient:
        def __enter__(self) -> EventClient:
            return self

        def __exit__(self, *_args: Any) -> None:
            return None

        def authenticate(self, _api_key: str, call: Any = None) -> None:
            if call is not None:
                call("auth.login_with_api_key", ["redacted-test-key"])

        def call(self, method: str, params: Any = None) -> bool:
            attempts.append((method, params))
            if method == "auth.login_with_api_key":
                return True
            if method == "system.version_short":
                return "26.0.0"
            if method == "core.subscribe" and params == ["app.stats"]:
                raise KeyboardInterrupt
            return True

    exporter = runtime.TrueNASExporter(
        make_config(
            event_subscriptions=["virt.instance.metrics", "app.stats"],
            event_read_timeout_seconds=1,
        ),
        compatibility_profile=PROFILE_26_0,
    )
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: EventClient())

    with pytest.raises(KeyboardInterrupt):
        exporter._event_stream_loop()

    assert ("core.subscribe", ["virt.instance.metrics"]) not in attempts
    assert attempts == [
        ("auth.login_with_api_key", ["redacted-test-key"]),
        ("system.version_short", []),
        ("core.subscribe", ["app.stats"]),
    ]


def test_audit_units_and_configured_default_route_replacements(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(make_config())
    audit = fixture("audit_config.json")
    exporter._collect_audit_metrics(object(), {"audit.config": audit})

    assert value(runtime.AUDIT_DATASET_USED_BYTES) == 0
    assert value(runtime.AUDIT_DATASET_AVAILABLE_BYTES) == 4 * 1024**3
    assert value(runtime.AUDIT_RETENTION_DAYS) == 30
    assert value(runtime.AUDIT_RESERVATION_BYTES) == 2 * 1024**3
    assert value(runtime.AUDIT_QUOTA_BYTES) == 4 * 1024**3
    assert value(runtime.AUDIT_REMOTE_LOGGING_ENABLED) == 0

    routes = fixture("route_system_routes.json")
    monkeypatch.setattr(
        exporter,
        "_safe_call_auto",
        lambda _client, method: routes if method == "route.system_routes" else None,
    )
    monkeypatch.setattr(
        exporter,
        "_call",
        lambda _client, method, _params=None: (_ for _ in ()).throw(
            runtime.JsonRpcError(f"optional fixture method unavailable: {method}")
        ),
    )
    exporter._collect_system_extra_metrics(object(), {})
    assert value(runtime.NETWORK_DEFAULT_GATEWAY_CONFIGURED) == 1
    assert value(runtime.NETWORK_GATEWAY_REACHABLE) == 1

    routes.clear()
    exporter._collect_system_extra_metrics(object(), {})
    assert value(runtime.NETWORK_DEFAULT_GATEWAY_CONFIGURED) == 0
    assert value(runtime.NETWORK_GATEWAY_REACHABLE) == 0


def test_malformed_reboot_reasons_do_not_report_false_negative(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(make_config())
    monkeypatch.setattr(exporter, "_safe_call_auto", lambda *_args: None)
    monkeypatch.setattr(
        exporter,
        "_call",
        lambda _client, method, _params=None: (_ for _ in ()).throw(
            runtime.JsonRpcError(f"optional fixture method unavailable: {method}")
        ),
    )

    exporter._collect_system_extra_metrics(
        object(), {"system.reboot.info": {"reboot_required_reasons": [{"reason": "bad"}]}}
    )
    assert math.isnan(value(runtime.SYSTEM_REBOOT_REQUIRED))

    exporter._collect_system_extra_metrics(
        object(), {"system.reboot.info": {"reboot_required_reasons": []}}
    )
    assert value(runtime.SYSTEM_REBOOT_REQUIRED) == 0


def test_limited_detail_lists_do_not_replace_failed_exact_counts(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(make_config(query_limit=1))
    monkeypatch.setattr(
        exporter,
        "_safe_call_auto",
        lambda _client, method: (
            [{"id": 1, "name": "vm", "status": "STOPPED"}]
            if method == "vm.query"
            else [{"name": "app", "state": "STOPPED"}]
            if method == "app.query"
            else None
        ),
    )
    monkeypatch.setattr(
        exporter,
        "_query_count",
        lambda *_args, **_kwargs: (_ for _ in ()).throw(
            runtime.JsonRpcError("count unavailable")
        ),
    )

    exporter._collect_entity_detail_metrics(object(), {})
    assert math.isnan(value(runtime.VM_COUNT))
    assert math.isnan(value(runtime.APP_COUNT))


def test_generic_filesystem_labels_use_bounded_slots_not_paths(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    exporter = runtime.TrueNASExporter(
        make_config(
            enable_generic_method_metrics=True,
            filesystem_paths=["/mnt/private-dataset"],
            enable_filesystem_listdir=False,
        )
    )
    runtime.METHOD_NUMERIC_VALUE.clear()
    monkeypatch.setattr(exporter, "_call", lambda *_args, **_kwargs: {"size": 1})

    exporter._collect_filesystem_metrics(object())
    paths = {
        sample.labels["path"]
        for sample in list(runtime.METHOD_NUMERIC_VALUE.collect())[0].samples
    }
    assert paths
    assert all("configured_slot_0" in path for path in paths)
    assert all("/mnt" not in path and "private-dataset" not in path for path in paths)


@pytest.mark.parametrize(
    ("timestamp", "expected"),
    [
        (0, 0),
        ("2026-01-01T00:00:00Z", 1767225600),
        ({"$date": 1700000000000}, 1700000000),
        ({"parsed": {"$date": 1700000000000}}, 1700000000),
        (None, None),
        (False, None),
        ("malformed", None),
    ],
)
def test_snapshot_timestamp_documented_and_malformed_forms(timestamp: Any, expected: Any) -> None:
    exporter = runtime.TrueNASExporter(make_config())
    assert exporter._extract_snapshot_creation_timestamp(
        {"properties": {"creation": timestamp}}
    ) == expected
