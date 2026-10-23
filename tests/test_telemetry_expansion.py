"""Synthetic RPC-to-snapshot coverage for the typed telemetry expansion."""

import sys

import pytest
from conftest import make_config

import truenas_exporter as exporter_module

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]


class API:
    def __init__(self, responses=None, version="27.0.0-RC.1"):
        self.responses = responses or {}
        self.version = version
        self.calls = []

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        pass

    def authenticate(self, *_args, **_kwargs):
        pass

    def call(self, method, params=None):
        self.calls.append((method, params))
        if method == "system.version_short":
            return self.version
        if method in self.responses:
            value = self.responses[method]
            if isinstance(value, Exception):
                raise value
            return value
        if method.endswith(".query"):
            return 0 if params and len(params) > 1 and params[1].get("count") else []
        return None


def collect(monkeypatch, api, **config):
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: api)
    exporter = exporter_module.TrueNASExporter(make_config(**config))
    exporter.scrape_once()
    return exporter


def samples(exporter, name):
    return [(s.labels, s.value) for f in exporter.metric_snapshot() for s in f.samples if s.name == name]


def test_scan_details_are_projected_without_extra_pool_requests(monkeypatch):
    api = API({"pool.query": [{"name": "tank", "is_upgraded": False, "dedup_table_quota": 4096,
        "scan": {"function": "SCRUB", "state": "SCANNING", "bytes_issued": 0,
                 "start_time": "2026-01-01T00:00:00Z", "pause": None}}]})
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_pool_scan_bytes_issued") == [({"pool": "tank"}, 0)]
    assert samples(exporter, "truenas_pool_scan_state") == [({"pool": "tank", "state": "SCANNING"}, 1)]
    assert samples(exporter, "truenas_pool_scan_paused") == [({"pool": "tank"}, 0)]
    assert samples(exporter, "truenas_pool_scan_start_timestamp_seconds") == [({"pool": "tank"}, 1767225600)]
    assert samples(exporter, "truenas_pool_features_upgraded") == [({"pool": "tank"}, 0)]
    assert len([m for m, _ in api.calls if m == "pool.query"]) == 1
    assert all(m != "pool.is_upgraded" for m, _ in api.calls)


@pytest.mark.parametrize("version", ["25.10.3", "26.0.0", "27.0.0-RC.1"])
def test_dataset_accounting_and_versioned_projection(monkeypatch, version):
    api = API({"pool.dataset.query": [{"id": "tank/data", "referenced": 2048,
        "logicalused": 4096, "logicalreferenced": 3072, "usedbyrefreservation": 0,
        "recordsize": 131072, "volsize": 0, "copies": 1, "sync": "DISABLED", "deduplication": "OFF"}]}, version)
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_dataset_used_by_refreservation_bytes") == [({"dataset": "tank/data"}, 0)]
    if version.startswith("27."):
        assert samples(exporter, "truenas_dataset_logical_used_bytes") == [({"dataset": "tank/data"}, 4096)]
        assert samples(exporter, "truenas_dataset_referenced_bytes") == [({"dataset": "tank/data"}, 2048)]
        assert samples(exporter, "truenas_dataset_recordsize_bytes") == [({"dataset": "tank/data"}, 131072)]
        assert samples(exporter, "truenas_dataset_copies") == [({"dataset": "tank/data"}, 1)]
        assert samples(exporter, "truenas_dataset_sync_mode") == [({"dataset": "tank/data", "mode": "DISABLED"}, 1)]
        assert samples(exporter, "truenas_dataset_dedup_enabled") == [({"dataset": "tank/data"}, 0)]
    else:
        assert samples(exporter, "truenas_dataset_logical_used_bytes") == []
    params = next(p for m, p in api.calls if m == "pool.dataset.query")
    assert ("logicalused" in params[1]["extra"]["properties"]) == version.startswith("27.")


def test_tiering_config_and_latest_job_are_typed_and_bounded(monkeypatch):
    api = API({
        "zfs.tier.config": {"enabled": True, "max_concurrent_jobs": 2, "max_used_percentage": 80, "special_class_metadata_reserve_pct": 15},
        "zfs.tier.rewrite_job_query": [{"tier_job_id": 7, "dataset_name": "tank/data"}],
        "zfs.tier.rewrite_job_status": {"dataset_name": "tank/data", "status": "RUNNING", "stats": {
            "count_bytes": 0, "total_bytes": 4096, "count_items": 0, "total_items": 4,
            "failures": 0, "success": 0, "start_time": 1767225600, "update_time": 1767225602,
            "name": "private-file", "error": "private-error"}},
    })
    exporter = collect(monkeypatch, api, max_entity_calls=2)
    assert samples(exporter, "truenas_zfs_tier_enabled") == [({}, 1)]
    assert samples(exporter, "truenas_zfs_tier_job_processed_bytes") == [({"dataset": "tank/data"}, 0)]
    assert samples(exporter, "truenas_zfs_tier_job_state") == [({"dataset": "tank/data", "state": "RUNNING"}, 1)]
    assert samples(exporter, "truenas_zfs_tier_job_failed_files") == [({"dataset": "tank/data"}, 0)]
    params = next(p for m, p in api.calls if m == "zfs.tier.rewrite_job_query")
    assert params[0]["query-options"]["limit"] == 2
    assert all("private" not in str(s.labels) for f in exporter.metric_snapshot() for s in f.samples)


@pytest.mark.parametrize("version", ["25.10.3", "26.0.0", "unknown"])
def test_tiering_is_never_requested_on_other_profiles(monkeypatch, version):
    api = API(version=version)
    collect(monkeypatch, api)
    assert not any(m.startswith("zfs.tier.") for m, _ in api.calls)


def test_backup_outcomes_use_projected_fields_without_private_payloads(monkeypatch):
    api = API({"cloud_backup.query": [{"id": 1, "enabled": False, "locked": False,
        "job_state": "SUCCESS", "job_progress": 100,
        "job_started": "2026-01-01T00:00:00Z", "job_finished": "2026-01-01T00:00:05Z"}]})
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_cloud_backup_task_state") == [({"name": "1", "state": "SUCCESS"}, 1)]
    assert samples(exporter, "truenas_cloud_backup_task_last_completion_timestamp_seconds") == [({"name": "1"}, 1767225605)]
    assert samples(exporter, "truenas_cloud_backup_task_locked") == [({"name": "1"}, 0)]
    params = next(p for m, p in api.calls if m == "cloud_backup.query")
    assert ["job.state", "job_state"] in params[1]["select"]
    assert "job" not in params[1]["select"]


def test_sed_status_is_bounded_and_unknown_values_stay_absent(monkeypatch):
    api = API({"disk.query": [{"name": "sda", "sed": True, "sed_status": "LOCKED"},
        {"name": "sdb", "sed": None, "sed_status": "arbitrary-private-error"},
        {"name": "sdc", "sed": False, "sed_status": None}]})
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_disk_sed_capable") == [({"disk": "sda"}, 1), ({"disk": "sdc"}, 0)]
    assert samples(exporter, "truenas_disk_sed_status") == [({"disk": "sda", "status": "LOCKED"}, 1)]
    assert len([m for m, _ in api.calls if m == "disk.query"]) == 1
    params = next(p for m, p in api.calls if m == "disk.query")
    assert params[1]["extra"]["sed_status"] is True
    assert "passwd" not in params[1]["select"]


def test_ups_latest_fresh_samples_keep_zero_and_voltage_dimensions(monkeypatch):
    import time

    now = int(time.time())
    api = API({"service.query": [{"service": "ups", "enable": True, "state": "RUNNING"}],
        "reporting.get_data": [
            {"name": "upscharge", "identifier": "", "legend": ["time", "battery_charge"], "data": [[now - 2, 0], [now, None]]},
            {"name": "upsruntime", "identifier": "", "legend": ["time", "runtime"], "data": [[now, 123]]},
            {"name": "upsvoltage", "identifier": "input", "legend": ["time", "voltage"], "data": [[now, 230]]},
        ]})
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_ups_battery_charge_percent") == [({}, 0)]
    assert samples(exporter, "truenas_ups_runtime_seconds") == [({}, 123)]
    assert samples(exporter, "truenas_ups_voltage_volts") == [({"source": "input"}, 230)]
    assert len([m for m, _ in api.calls if m == "reporting.get_data"]) == 1


def test_ups_is_not_polled_when_service_is_absent(monkeypatch):
    api = API()
    collect(monkeypatch, api)
    assert not any(m == "reporting.get_data" for m, _ in api.calls)


@pytest.mark.parametrize("bad", [None, False, "invalid", float("nan"), -1])
def test_invalid_new_dataset_values_are_not_measurements(monkeypatch, bad):
    api = API({"pool.dataset.query": [{"id": "tank/data", "logicalused": bad, "copies": bad, "sync": bad, "usedbyrefreservation": bad}]})
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_dataset_logical_used_bytes") == []
    assert samples(exporter, "truenas_dataset_copies") == []
    assert samples(exporter, "truenas_dataset_sync_mode") == []
    assert samples(exporter, "truenas_dataset_used_by_refreservation_bytes") == []


def test_new_series_expire_on_missing_sources_and_recover(monkeypatch):
    api = API({"pool.query": [{"name": "tank", "scan": {"state": "SCANNING", "pause": None}}],
        "cloud_backup.query": [{"id": 1, "job_state": "RUNNING", "job_progress": 0}],
        "zfs.tier.config": {"enabled": True},
        "zfs.tier.rewrite_job_query": [{"tier_job_id": 1, "dataset_name": "tank/data"}],
        "zfs.tier.rewrite_job_status": {"dataset_name": "tank/data", "status": "RUNNING", "stats": {"count_bytes": 0}},
    })
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_pool_scan_state")
    assert samples(exporter, "truenas_cloud_backup_task_state")
    assert samples(exporter, "truenas_zfs_tier_job_state")
    original = api.responses
    api.responses = {}
    exporter.scrape_once()
    for name in ("truenas_pool_scan_state", "truenas_cloud_backup_task_state", "truenas_zfs_tier_job_state"):
        assert samples(exporter, name) == []
    api.responses = original
    exporter.scrape_once()
    assert samples(exporter, "truenas_zfs_tier_job_processed_bytes") == [({"dataset": "tank/data"}, 0)]


def test_ups_rejects_stale_malformed_and_wrong_dimension_data(monkeypatch):
    import time

    now = int(time.time())
    api = API({"service.query": [{"service": "ups", "state": "RUNNING"}],
        "reporting.get_data": [
            {"name": "upsvoltage", "identifier": "private-value", "legend": ["time", "voltage"], "data": [[now, 230]]},
            {"name": "upscharge", "legend": ["time", "charge"], "data": [[now - 1000, 80], [now, True], [now, 101]]},
            {"name": "upsruntime", "legend": ["time", "runtime", "unexpected"], "data": [[now, 1, 2]]},
        ]})
    exporter = collect(monkeypatch, api)
    import math

    assert math.isnan(samples(exporter, "truenas_ups_battery_charge_percent")[0][1])
    assert samples(exporter, "truenas_ups_voltage_volts") == []
    assert samples(exporter, "truenas_ups_sample_timestamp_seconds") == []


def test_tier_inventory_caps_detail_requests_and_uses_latest_per_dataset(monkeypatch):
    api = API({"zfs.tier.config": {"enabled": True},
        "zfs.tier.rewrite_job_query": [{"tier_job_id": 3, "dataset_name": "tank/data"},
            {"tier_job_id": 2, "dataset_name": "tank/data"},
            {"tier_job_id": 1, "dataset_name": "tank/other"}],
        "zfs.tier.rewrite_job_status": {"dataset_name": "tank/data", "status": "COMPLETE", "stats": None}})
    exporter = collect(monkeypatch, api, max_entity_calls=2)
    assert [p for m, p in api.calls if m == "zfs.tier.rewrite_job_status"] == [[3]]
    assert samples(exporter, "truenas_zfs_tier_job_inventory_limit_reached") == [({}, 1)]
    assert samples(exporter, "truenas_zfs_tier_jobs_observed") == [({}, 2)]


@pytest.mark.parametrize("failure,up", [(TimeoutError("synthetic timeout"), 0), (runtime.JsonRpcError("unsupported", code=-32601), 1)])
def test_optional_source_failure_keeps_transport_health_truthful(monkeypatch, failure, up):
    api = API({"zfs.tier.config": failure})
    exporter = collect(monkeypatch, api)
    assert samples(exporter, "truenas_up") == [({}, up)]


@pytest.mark.parametrize("version", ["25.10.3", "26.0.0"])
def test_new_hardware_and_backup_options_do_not_leak_to_older_versions(monkeypatch, version):
    api = API(version=version)
    collect(monkeypatch, api)
    disk = next(p for m, p in api.calls if m == "disk.query")
    backup = next(p for m, p in api.calls if m == "cloud_backup.query")
    assert "sed_status" not in disk[1]["extra"]
    assert backup[1]["select"] == ["id", "enabled"]


@pytest.mark.parametrize("jobs", [None, [None], [{}], [{"tier_job_id": True, "dataset_name": "tank/data"}]])
def test_malformed_tier_inventory_does_not_report_a_valid_empty_inventory(monkeypatch, jobs):
    import math

    api = API({"zfs.tier.config": {"enabled": True}, "zfs.tier.rewrite_job_query": jobs})
    exporter = collect(monkeypatch, api)
    assert math.isnan(samples(exporter, "truenas_zfs_tier_jobs_observed")[0][1])
    assert not any(m == "zfs.tier.rewrite_job_status" for m, _ in api.calls)


@pytest.mark.parametrize("bad", [None, "unknown", [], {}])
def test_unknown_new_boolean_fields_never_create_default_zero_series(monkeypatch, bad):
    api = API({"pool.query": [{"name": "tank", "is_upgraded": bad}],
        "disk.query": [{"name": "sda", "sed": bad}],
        "cloud_backup.query": [{"id": 1, "locked": bad}]})
    exporter = collect(monkeypatch, api)
    for name in ("truenas_pool_features_upgraded", "truenas_disk_sed_capable", "truenas_cloud_backup_task_locked"):
        assert samples(exporter, name) == []


def test_first_readiness_waits_for_complete_metric_publication(monkeypatch):
    import threading

    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: API())
    exporter = exporter_module.TrueNASExporter(make_config())
    initial_up = samples(exporter, "truenas_up")
    entered, release = threading.Event(), threading.Event()
    original = runtime.REGISTRY.collect

    def blocked_collection():
        entered.set()
        assert release.wait(5)
        yield from original()

    monkeypatch.setattr(runtime.REGISTRY, "collect", blocked_collection)
    worker = threading.Thread(target=exporter.scrape_once)
    worker.start()
    try:
        assert entered.wait(5)
        assert samples(exporter, "truenas_up") == initial_up
        assert not exporter.is_ready()
    finally:
        release.set()
        worker.join(5)
    assert not worker.is_alive()
    assert exporter.is_ready()
    assert samples(exporter, "truenas_up") == [({}, 1)]
