"""Regression fixtures for documented TrueNAS SCALE 25.10.2 response shapes.

These tests intentionally exercise fixture invariants and pure conversions.  They
do not require a live appliance and do not couple the documentation evidence to
collector scheduling or transport behavior.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from truenas_exporter.collection import _as_bool, _as_float, _parse_ts

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIRECTORY = Path(__file__).parent / "fixtures" / "api_25_10_2"

FIXTURE_DOC_SOURCES = {
    "audit_config.json": "docs/truenas-api/methods/audit/config.md",
    "boot_environment_query.json": "docs/truenas-api/methods/boot/environment/query.md",
    "device_get_info_gpu.json": "docs/truenas-api/methods/device/get_info.md",
    "directoryservices_config_disabled.json": "docs/truenas-api/methods/directoryservices/config.md",
    "directoryservices_status.json": "docs/truenas-api/methods/directoryservices/status.md",
    "disk_query_selected.json": "docs/truenas-api/methods/disk/query.md",
    "dockerhub_rate_limit.json": "docs/truenas-api/methods/app/image/dockerhub_rate_limit.md",
    "ipmi_chassis_info.json": "docs/truenas-api/methods/ipmi/chassis/info.md",
    "ipmi_sel_info.json": "docs/truenas-api/methods/ipmi/sel/info.md",
    "nfs_config.json": "docs/truenas-api/methods/nfs/config.md",
    "pool_dataset_query_selected.json": "docs/truenas-api/methods/pool/dataset/query.md",
    "pool_query.json": "docs/truenas-api/methods/pool/query.md",
    "reporting_realtime_full.json": "docs/truenas-api/events/reporting/realtime.md",
    "reporting_realtime_malformed.json": "docs/truenas-api/events/reporting/realtime.md",
    "reporting_realtime_zero.json": "docs/truenas-api/events/reporting/realtime.md",
    "route_system_routes.json": "docs/truenas-api/methods/route/system_routes.md",
    "system_ntpserver_query.json": "docs/truenas-api/methods/system/ntpserver/query.md",
    "system_reboot_info.json": "docs/truenas-api/methods/system/reboot/info.md",
    "system_security_config.json": "docs/truenas-api/methods/system/security/config.md",
    "update_available_versions.json": "docs/truenas-api/methods/update/available_versions.md",
    "update_status_error.json": "docs/truenas-api/methods/update/status.md",
    "update_status_normal.json": "docs/truenas-api/methods/update/status.md",
    "vm_get_available_memory.json": "docs/truenas-api/methods/vm/get_available_memory.md",
    "vm_get_vmemory_in_use.json": "docs/truenas-api/methods/vm/get_vmemory_in_use.md",
}

DOCUMENTED_ZFS_FIELDS = {
    "bytes_read_per_second_from_the_l2arc",
    "bytes_written_per_second_to_the_l2arc",
    "demand_accesses_per_second",
    "demand_data_accesses_per_second",
    "demand_data_hit_percentage",
    "demand_data_hits_per_second",
    "demand_data_io_hit_percentage",
    "demand_data_io_hits_per_second",
    "demand_data_miss_percentage",
    "demand_data_misses_per_second",
    "demand_metadata_accesses_per_second",
    "demand_metadata_hit_percentage",
    "demand_metadata_hits_per_second",
    "demand_metadata_io_hit_percentage",
    "demand_metadata_io_hits_per_second",
    "demand_metadata_miss_percentage",
    "demand_metadata_misses_per_second",
    "l2arc_access_hit_percentage",
    "l2arc_hits_per_second",
    "l2arc_miss_percentage",
    "l2arc_misses_per_second",
    "total_l2arc_accesses_per_second",
}


def load_fixture(filename: str) -> Any:
    with (FIXTURE_DIRECTORY / filename).open(encoding="utf-8") as fixture_file:
        return json.load(fixture_file)


def iter_mapping_items(value: Any) -> list[tuple[str, Any]]:
    """Return all nested mapping items without serializing fixture values."""
    items: list[tuple[str, Any]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            items.append((key, child))
            items.extend(iter_mapping_items(child))
    elif isinstance(value, list):
        for child in value:
            items.extend(iter_mapping_items(child))
    return items


def test_fixture_inventory_has_local_documentation_evidence() -> None:
    fixture_names = {path.name for path in FIXTURE_DIRECTORY.glob("*.json")}
    assert fixture_names == set(FIXTURE_DOC_SOURCES) | {"conversion_edge_cases.json"}

    for fixture_name, documentation_path in FIXTURE_DOC_SOURCES.items():
        assert (REPOSITORY_ROOT / documentation_path).is_file()
        assert load_fixture(fixture_name) is not None


def test_fixtures_are_synthetic_and_do_not_contain_credentials() -> None:
    sensitive_keys = {
        "api_key",
        "credential",
        "pass",
        "password",
        "private_key",
        "privatekey",
        "secret",
        "token",
    }
    for fixture_path in FIXTURE_DIRECTORY.glob("*.json"):
        for key, value in iter_mapping_items(load_fixture(fixture_path.name)):
            if key.casefold() in sensitive_keys:
                assert value is None or (isinstance(value, str) and value.startswith("REDACTED"))


def test_reporting_realtime_has_every_documented_zfs_field() -> None:
    event = load_fixture("reporting_realtime_full.json")
    fields = event["fields"]

    assert {"cpu", "disls", "interfaces", "memory", "zfs", "pools"} <= fields.keys()
    assert set(fields["zfs"]) == DOCUMENTED_ZFS_FIELDS
    assert all(_as_float(value) is not None for value in fields["zfs"].values())

    percentage_fields = {name for name in DOCUMENTED_ZFS_FIELDS if name.endswith("_percentage")}
    assert percentage_fields
    assert all(0 <= fields["zfs"][name] <= 100 for name in percentage_fields)


def test_reporting_realtime_preserves_documented_zero_values() -> None:
    fields = load_fixture("reporting_realtime_zero.json")["fields"]

    assert set(fields["zfs"]) == DOCUMENTED_ZFS_FIELDS
    for section_name in ("disls", "memory", "zfs"):
        assert all(_as_float(value) == 0.0 for value in fields[section_name].values())

    percentage_fields = {name for name in DOCUMENTED_ZFS_FIELDS if name.endswith("_percentage")}
    assert all(fields["zfs"][name] / 100 == 0 for name in percentage_fields)


def test_reporting_realtime_malformed_values_fail_safely() -> None:
    fields = load_fixture("reporting_realtime_malformed.json")["fields"]

    assert _as_float(fields["memory"]["arc_size"]) is None
    assert _as_float(fields["memory"]["physical_memory_total"]) is None
    assert _as_float(fields["zfs"]["demand_accesses_per_second"]) is None
    assert _as_float(fields["zfs"]["demand_data_hit_percentage"]) is None
    assert "cpu" not in fields


def test_update_and_reboot_documented_nested_shapes() -> None:
    normal = load_fixture("update_status_normal.json")
    error = load_fixture("update_status_error.json")
    available = load_fixture("update_available_versions.json")
    reboot = load_fixture("system_reboot_info.json")

    assert normal["code"] == "NORMAL"
    assert normal["status"]["current_version"]["train"] == "TrueNAS-SCALE-25.10"
    assert normal["status"]["new_version"]["version"] == "25.10.3"
    assert _as_float(normal["update_download_progress"]["percent"]) == 0.0
    assert normal["error"] is None

    assert error["code"] == "ERROR"
    assert error["status"] is None
    assert set(error["error"]) == {"errname", "reason"}
    assert available[0]["version"]["version"] == "25.10.3"

    assert "reboot_required_reasons" in reboot
    assert "reasons" not in reboot
    assert set(reboot["reboot_required_reasons"][0]) == {"code", "reason"}


def test_vm_memory_responses_are_scalar_and_object_preserving_zero() -> None:
    # The pinned 25.10.2 doc labels these "megabytes", but live 25.10.x returns
    # bytes, so the 25.10 profile applies a bytes multiplier of 1.0 (no scaling).
    # This test pins the documented response *shape* — a scalar and an
    # RNP/PRD/RPRD object — and that a real zero is preserved, not the unit math.
    available = load_fixture("vm_get_available_memory.json")
    in_use = load_fixture("vm_get_vmemory_in_use.json")

    assert isinstance(available, int)
    assert available >= 0
    assert set(in_use) == {"RNP", "PRD", "RPRD"}
    assert in_use["RNP"] == 0
    assert all(isinstance(value, int) and value >= 0 for value in in_use.values())


def test_pool_dataset_and_disk_documented_field_shapes() -> None:
    pool = load_fixture("pool_query.json")[0]
    dataset = load_fixture("pool_dataset_query_selected.json")[0]
    disks = load_fixture("disk_query_selected.json")

    assert _as_float(pool["dedup_table_size"]) == 1024**2
    assert "size" not in pool["expand"]
    assert pool["scan"]["percentage"] == 0
    assert pool["scan"]["errors"] == 0
    assert _parse_ts(pool["scan"]["start_time"]) is not None
    assert _as_float(pool["fragmentation"]) == 0.0

    assert _as_float(dataset["used"]) == 0.0
    assert _as_float(dataset["available"]) == 1024**3
    assert dataset["id"] == "tank/data"
    assert "referenced" not in dataset
    assert _as_float(dataset["quota"]) is None
    assert dataset["readonly"]["value"] == "off"
    assert dataset["encrypted"] is False
    assert dataset["key_loaded"] is None

    assert {disk["type"] for disk in disks} == {"HDD", "SSD"}
    ssd = next(disk for disk in disks if disk["type"] == "SSD")
    assert ssd["rotationrate"] is None
    assert ssd["bus"] == "NVME"


def test_directory_security_nfs_ntp_and_dockerhub_shapes() -> None:
    directory_status = load_fixture("directoryservices_status.json")
    directory_config = load_fixture("directoryservices_config_disabled.json")
    security = load_fixture("system_security_config.json")
    nfs = load_fixture("nfs_config.json")
    ntp_servers = load_fixture("system_ntpserver_query.json")
    dockerhub = load_fixture("dockerhub_rate_limit.json")

    assert set(directory_status) == {"type", "status", "status_msg"}
    assert directory_status["status"] == "FAULTED"
    assert directory_config["enable"] is False
    assert directory_config["enable_account_cache"] is False
    assert directory_config["enable_dns_updates"] is False
    assert "account_cache" not in directory_config
    assert "dns_updates" not in directory_config

    assert security["enable_fips"] is False
    assert security["enable_gpos_stig"] is True
    assert "fips" not in security
    assert "stig" not in security

    assert nfs["protocols"] == ["NFSV3", "NFSV4"]
    assert "v4" not in nfs
    assert nfs["allow_nonroot"] is False

    assert [(2 ** server["minpoll"], 2 ** server["maxpoll"]) for server in ntp_servers] == [
        (64, 1024),
        (256, 4096),
    ]
    assert ntp_servers[0]["burst"] is False
    assert ntp_servers[1]["iburst"] is False

    assert dockerhub["remaining_pull_limit"] == 0
    assert dockerhub["total_time_limit_in_secs"] == 21600
    assert dockerhub["remaining_time_limit_in_secs"] == 3600
    assert dockerhub["error"] is None


def test_ipmi_and_gpu_documented_nested_shapes() -> None:
    chassis = load_fixture("ipmi_chassis_info.json")
    sel = load_fixture("ipmi_sel_info.json")
    gpu = load_fixture("device_get_info_gpu.json")[0]

    assert _as_bool(chassis["system_power"]) is True
    assert _as_bool(chassis["power_fault"]) is False
    assert _as_bool(chassis["cooling/fan_fault"]) is False
    assert "power" not in chassis
    assert "fan_fault" not in chassis

    assert _as_float(sel["number_of_log_entries"]) == 0.0
    assert _as_float(sel["events_dropped_due_to_lack_of_space"]) == 0.0
    free_bytes = _as_float(sel["number_of_free_allocation_units"])
    allocation_unit_bytes = _as_float(sel["allocation_unit_size"])
    assert free_bytes is not None
    assert allocation_unit_bytes is not None
    assert free_bytes * allocation_unit_bytes == 1024

    assert gpu["available_to_host"] is True
    assert gpu["uses_system_critical_devices"] is False
    assert gpu["addr"]["pci_slot"] == "0000:01:00.0"
    assert gpu["devices"][0]["pci_id"] == "10de:0000"
    assert "pci_id" not in gpu


@pytest.mark.parametrize(
    ("fixture_key", "expected"),
    [
        ("numeric", [None, 0.0, None, 0.0, 1.5, None, None, 2.5]),
        ("boolean", [False, True, False, True, False, True, False, True, False]),
        ("timestamp", [None, 0.0, 0.0, 1767225600.0, None, None]),
    ],
)
def test_pure_conversion_edges(fixture_key: str, expected: list[Any]) -> None:
    cases = load_fixture("conversion_edge_cases.json")[fixture_key]
    converters = {
        "numeric": _as_float,
        "boolean": _as_bool,
        "timestamp": _parse_ts,
    }

    assert [converters[fixture_key](value) for value in cases] == expected
