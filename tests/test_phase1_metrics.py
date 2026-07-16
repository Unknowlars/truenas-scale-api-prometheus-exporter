import json
import math
from pathlib import Path

import pytest
from conftest import make_config

import truenas_exporter as exporter_module

FIXTURES = Path(__file__).parent / "fixtures" / "api_25_10_2"


def gauge_value(gauge):
    return gauge._value.get()


def labeled_value(metric, *label_values):
    return metric.labels(*label_values)._value.get()


def reset_metric(metric):
    if getattr(metric, "_labelnames", ()):  # pragma: no branch
        metric.clear()
    else:
        metric.set(0)


@pytest.fixture(autouse=True)
def reset_gauges():
    for metric in (
        exporter_module.SNAPSHOT_TOTAL_COUNT,
        exporter_module.SNAPSHOT_OLDEST_TS,
        exporter_module.DATASET_USED_BYTES,
        exporter_module.DATASET_REFERENCED_BYTES,
        exporter_module.DATASET_SNAPSHOT_COUNT,
        exporter_module.DATASET_RESERVATION_BYTES,
        exporter_module.DATASET_REFRESERVATION_BYTES,
        exporter_module.DATASET_USED_BY_CHILDREN_BYTES,
        exporter_module.DATASET_USED_BY_DATASET_BYTES,
        exporter_module.DATASET_USED_BY_SNAPSHOTS_BYTES,
        exporter_module.DATASET_READONLY,
        exporter_module.DATASET_ATIME,
        exporter_module.DATASET_EXEC,
        exporter_module.DATASET_KEY_LOADED,
        exporter_module.DATASET_LOCKED,
        exporter_module.DATASET_QUOTA_WARNING_PERCENT,
        exporter_module.DATASET_QUOTA_CRITICAL_PERCENT,
        exporter_module.DATASET_REFQUOTA_WARNING_PERCENT,
        exporter_module.DATASET_REFQUOTA_CRITICAL_PERCENT,
        exporter_module.DATASET_CREATION_TS,
        exporter_module.BOOT_ENV_SIZE_BYTES,
        exporter_module.CERT_DAYS_TO_EXPIRY,
        exporter_module.ALERT_COUNT,
        exporter_module.ALERT_COUNT_BY_LEVEL,
        exporter_module.ALERT_COUNT_BY_SOURCE,
        exporter_module.ALERT_COUNT_BY_CLASS,
        exporter_module.ALERT_COUNT_BY_NODE,
        exporter_module.ALERT_DISMISSED_COUNT,
        exporter_module.ALERT_ONE_SHOT_COUNT,
        exporter_module.ALERT_OLDEST_TS,
        exporter_module.ALERT_LAST_OCCURRENCE_TS,
        exporter_module.JOB_ACTIVE_COUNT,
        exporter_module.JOB_ACTIVE_COUNT_BY_STATE,
        exporter_module.JOB_ACTIVE_COUNT_BY_METHOD,
        exporter_module.JOB_ABORTABLE_ACTIVE_COUNT,
        exporter_module.JOB_TRANSIENT_ACTIVE_COUNT,
        exporter_module.JOB_OLDEST_ACTIVE_TS,
        exporter_module.JOB_PROGRESS_PERCENT,
        exporter_module.APP_COUNT,
        exporter_module.APP_STATE,
        exporter_module.APP_UPGRADE_AVAILABLE,
        exporter_module.APP_IMAGE_UPDATES_AVAILABLE,
        exporter_module.APP_CUSTOM,
        exporter_module.APP_MIGRATED,
        exporter_module.APP_CONTAINER_COUNT,
        exporter_module.APP_USED_PORT_COUNT,
        exporter_module.APP_USED_HOST_IP_COUNT,
        exporter_module.APP_CONTAINER_STATE_COUNT,
        exporter_module.SSH_ENABLED,
        exporter_module.SSH_PASSWORD_AUTH,
        exporter_module.FTP_ENABLED,
        exporter_module.SNMP_ENABLED,
        exporter_module.REPORTING_ENABLED,
        exporter_module.LOCAL_USER_COUNT,
        exporter_module.LOCAL_GROUP_COUNT,
        exporter_module.STATIC_ROUTE_COUNT,
        exporter_module.TUNABLE_COUNT,
        exporter_module.PRIVILEGE_COUNT,
        exporter_module.INITSHUTDOWNSCRIPT_COUNT,
        exporter_module.KEYCHAIN_CREDENTIAL_COUNT,
        exporter_module.ISCSI_TARGET_COUNT,
        exporter_module.ISCSI_PORTAL_COUNT,
        exporter_module.ISCSI_EXTENT_COUNT,
        exporter_module.ISCSI_INITIATOR_COUNT,
        exporter_module.NVMET_HOST_COUNT,
        exporter_module.NVMET_NAMESPACE_COUNT,
        exporter_module.DOCKER_IMAGE_COUNT,
        exporter_module.DNS_RESOLVER_COUNT,
        exporter_module.REPORTING_EXPORTER_COUNT,
        exporter_module.NETWORK_HTTPPROXY_CONFIGURED,
        exporter_module.REPLICATION_MAX_PARALLEL,
        exporter_module.APP_DOCKERHUB_PULL_LIMIT_TOTAL,
        exporter_module.APP_DOCKERHUB_PULL_LIMIT_REMAINING,
        exporter_module.APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS,
        exporter_module.APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT,
        exporter_module.VM_FLAG_INTEL_VMX,
        exporter_module.VM_FLAG_AMD_RVI,
        exporter_module.VM_FLAG_UNRESTRICTED_GUEST,
        exporter_module.VM_FLAG_AMD_ASIDS,
        exporter_module.VM_VIRTUALIZATION_DETAILS_SUPPORTED,
        exporter_module.VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT,
        exporter_module.DIRECTORYSERVICES_CONFIG_ENABLED,
        exporter_module.DIRECTORYSERVICES_ACCOUNT_CACHE_ENABLED,
        exporter_module.DIRECTORYSERVICES_DNS_UPDATES_ENABLED,
        exporter_module.DIRECTORYSERVICES_TIMEOUT_SECONDS,
        exporter_module.DIRECTORYSERVICES_SERVICE_TYPE,
        exporter_module.DIRECTORYSERVICES_KERBEROS_CONFIGURED,
        exporter_module.SYSTEM_SECURITY_FIPS_CONFIGURED,
        exporter_module.SYSTEM_SECURITY_GPOS_STIG,
        exporter_module.SYSTEM_SECURITY_PASSWORD_MIN_LENGTH,
        exporter_module.SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS,
        exporter_module.SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS,
        exporter_module.SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS,
        exporter_module.SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT,
        exporter_module.SUPPORT_AVAILABLE_AND_ENABLED,
        exporter_module.SUPPORT_CONFIG_ENABLED,
        exporter_module.UPDATE_AUTOCHECK_ENABLED,
        exporter_module.UPDATE_PROFILE_INFO,
        exporter_module.NTP_SERVER_COUNT,
        exporter_module.NTP_SERVER_ACTIVE_COUNT,
        exporter_module.NTP_SERVER_REACHABLE_COUNT,
        exporter_module.NTP_SERVER_PREFER_COUNT,
        exporter_module.NTP_SERVER_BURST_COUNT,
        exporter_module.NTP_SERVER_IBURST_COUNT,
        exporter_module.NTP_SERVER_MIN_POLL_MINUTES,
        exporter_module.NTP_SERVER_MAX_POLL_MINUTES,
        exporter_module.CATALOG_CONFIG_PRESENT,
        exporter_module.CATALOG_PREFERRED_TRAIN_COUNT,
        exporter_module.ISCSI_SESSION_COUNT,
        exporter_module.ISCSI_SESSION_ISER_COUNT,
        exporter_module.ISCSI_SESSION_OFFLOAD_COUNT,
        exporter_module.ISCSI_SESSION_IMMEDIATE_DATA_COUNT,
        exporter_module.REPORTING_TIER0_RETENTION_DAYS,
        exporter_module.REPORTING_TIER1_RETENTION_DAYS,
        exporter_module.REPORTING_TIER1_UPDATE_INTERVAL_SECONDS,
        exporter_module.TASK_COUNT,
        exporter_module.TASK_ENABLED,
        exporter_module.TASK_STATE,
        exporter_module.TASK_LAST_RUN_TS,
        exporter_module.POOL_VDEV_READ_ERRORS,
        exporter_module.POOL_VDEV_WRITE_ERRORS,
        exporter_module.POOL_VDEV_CHECKSUM_ERRORS,
        exporter_module.DISK_TEMP_ALERT_COUNT,
    ):
        reset_metric(metric)


def test_vdev_error_walker_fails_closed_on_malformed_topology():
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))

    exporter._extract_vdev_errors(
        "tank",
        {
            "data": [
                {"name": "missing-stats"},
                {"name": "missing-keys", "stats": {"alloc": 1}},
                {
                    "name": "non-list-children",
                    "children": {"bad": {"stats": {"read_errors": 1}}},
                },
                "not-a-vdev",
            ],
            "cache": None,
        },
    )

    assert list(exporter_module.POOL_VDEV_READ_ERRORS.collect())[0].samples == []
    assert list(exporter_module.POOL_VDEV_WRITE_ERRORS.collect())[0].samples == []
    assert list(exporter_module.POOL_VDEV_CHECKSUM_ERRORS.collect())[0].samples == []


def test_vdev_error_walker_stops_at_existing_depth_guard():
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    vdev = {"name": "leaf-too-deep", "stats": {"read_errors": 1}}
    for depth in range(8):
        vdev = {"name": f"level-{depth}", "children": [vdev]}

    exporter._extract_vdev_errors("tank", {"data": [vdev]})

    assert list(exporter_module.POOL_VDEV_READ_ERRORS.collect())[0].samples == []


def test_snapshot_count_uses_exact_count_query(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(exporter_mode="legacy", enable_task_metrics=True)
    )
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "pool.snapshot.query"
        options = params[1]
        if options.get("count"):
            return 321
        return []

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_snapshot_metrics(object(), {})

    assert gauge_value(exporter_module.SNAPSHOT_TOTAL_COUNT) == 321
    assert calls[0][1][1] == {"count": True}


def test_oldest_snapshot_timestamp_uses_ordered_exact_query(monkeypatch):
    exporter = exporter_module.TrueNASExporter(
        make_config(exporter_mode="legacy", enable_task_metrics=True)
    )
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        options = params[1]
        if options.get("count"):
            return 4
        # v26 returns the full object with properties.creation populated (via
        # extra.properties); the nested select alias is no longer used.
        return [{"properties": {"creation": {"parsed": 1700000000}}}]

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_snapshot_metrics(object(), {})

    assert gauge_value(exporter_module.SNAPSHOT_OLDEST_TS) == 1700000000
    oldest_options = calls[1][1][1]
    assert oldest_options["limit"] == 1
    assert oldest_options["order_by"] == ["properties.creation.parsed"]
    assert oldest_options["extra"] == {"properties": ["creation"]}
    assert "select" not in oldest_options


def test_dataset_metrics_request_parsed_properties_and_snapshot_fallback(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", dataset_snapshot_fallback_limit=50))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "pool.dataset.query":
            return [{
                "id": "tank/data",
                "used": 123.0,
                "available": 456.0,
                "quota": 1000.0,
                "refquota": 900.0,
                "compressratio": 1.5,
                "reservation": 50.0,
                "refreservation": 25.0,
                "usedbychildren": 11.0,
                "usedbydataset": 12.0,
                "usedbysnapshots": 13.0,
                "readonly": True,
                "atime": False,
                "exec": True,
                "key_loaded": True,
                "locked": False,
                "quota_warning": 80.0,
                "quota_critical": 95.0,
                "refquota_warning": 70.0,
                "refquota_critical": 90.0,
                "creation": 1700000000,
                "encrypted": True,
            }]
        if method == "pool.dataset.snapshot_count":
            assert params == ["tank/data"]
            return 9
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_dataset_metrics(object())

    dataset_options = calls[0][1][1]
    assert dataset_options["extra"]["properties"] == [
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
    ]
    assert dataset_options["select"] == [
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
    ]
    assert exporter_module.DATASET_USED_BYTES.labels(dataset="tank/data")._value.get() == 123.0
    assert exporter_module.DATASET_SNAPSHOT_COUNT.labels(dataset="tank/data")._value.get() == 9.0
    assert exporter_module.DATASET_RESERVATION_BYTES.labels(dataset="tank/data")._value.get() == 50.0
    assert exporter_module.DATASET_USED_BY_SNAPSHOTS_BYTES.labels(dataset="tank/data")._value.get() == 13.0
    assert exporter_module.DATASET_READONLY.labels(dataset="tank/data")._value.get() == 1.0
    assert exporter_module.DATASET_ATIME.labels(dataset="tank/data")._value.get() == 0.0
    assert exporter_module.DATASET_KEY_LOADED.labels(dataset="tank/data")._value.get() == 1.0
    assert exporter_module.DATASET_LOCKED.labels(dataset="tank/data")._value.get() == 0.0
    assert exporter_module.DATASET_QUOTA_WARNING_PERCENT.labels(dataset="tank/data")._value.get() == 80.0
    assert exporter_module.DATASET_REFQUOTA_CRITICAL_PERCENT.labels(dataset="tank/data")._value.get() == 90.0
    assert exporter_module.DATASET_CREATION_TS.labels(dataset="tank/data")._value.get() == 1700000000.0


def test_alert_metrics_export_enriched_rollups():
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))

    exporter._export_alert_metrics([
        {
            "level": "WARNING",
            "source": "SMART",
            "klass": "DiskTemp",
            "node": "A",
            "dismissed": False,
            "one_shot": False,
            "datetime": "2025-01-01T00:00:00+00:00",
            "last_occurrence": "2025-01-03T00:00:00+00:00",
        },
        {
            "level": "WARNING",
            "source": "SMART",
            "klass": "DiskTemp",
            "node": "B",
            "dismissed": True,
            "one_shot": True,
            "datetime": "2025-01-02T00:00:00+00:00",
            "last_occurrence": "2025-01-04T00:00:00+00:00",
        },
        {
            "level": "ERROR",
            "source": "POOL",
            "klass": "PoolHealth",
            "node": "A",
            "dismissed": False,
            "one_shot": False,
            "datetime": "2025-01-05T00:00:00+00:00",
            "last_occurrence": "2025-01-05T01:00:00+00:00",
        },
    ])

    assert gauge_value(exporter_module.ALERT_COUNT) == 3
    assert labeled_value(exporter_module.ALERT_COUNT_BY_LEVEL, "WARNING") == 2
    assert labeled_value(exporter_module.ALERT_COUNT_BY_SOURCE, "SMART") == 2
    assert labeled_value(exporter_module.ALERT_COUNT_BY_CLASS, "DiskTemp", "WARNING") == 2
    assert labeled_value(exporter_module.ALERT_COUNT_BY_NODE, "A") == 2
    assert gauge_value(exporter_module.ALERT_DISMISSED_COUNT) == 1
    assert gauge_value(exporter_module.ALERT_ONE_SHOT_COUNT) == 1
    assert gauge_value(exporter_module.ALERT_OLDEST_TS) == exporter_module._parse_ts("2025-01-01T00:00:00+00:00")
    assert labeled_value(exporter_module.ALERT_LAST_OCCURRENCE_TS, "WARNING") == exporter_module._parse_ts("2025-01-04T00:00:00+00:00")


def test_job_metrics_use_exact_active_counts_and_filtered_detail_query(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", query_limit=1))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "core.get_jobs"
        filters, options = params
        if options == {"count": True}:
            if filters == [["state", "=", "WAITING"]]:
                return 1
            if filters == [["state", "=", "RUNNING"]]:
                return 2
        assert filters == [["state", "in", ["WAITING", "RUNNING"]]]
        assert options["limit"] == 3
        assert options["select"] == [
            "method",
            "state",
            "abortable",
            "transient",
            "time_started",
            ["progress.percent", "progress_percent"],
        ]
        return [
            {
                "method": "replication.run",
                "state": "RUNNING",
                "abortable": False,
                "transient": False,
                "time_started": "2025-02-01T00:10:00+00:00",
                "progress_percent": 35,
            },
            {
                "method": "replication.run",
                "state": "RUNNING",
                "abortable": False,
                "transient": True,
                "time_started": "2025-02-01T00:05:00+00:00",
                "progress_percent": 55,
            },
            {
                "method": "pool.scrub.run",
                "state": "WAITING",
                "abortable": True,
                "transient": False,
                "time_started": "2025-02-01T00:01:00+00:00",
                "progress_percent": None,
            },
        ]

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_job_metrics(object())

    assert gauge_value(exporter_module.JOB_ACTIVE_COUNT) == 3
    assert labeled_value(exporter_module.JOB_ACTIVE_COUNT_BY_STATE, "WAITING") == 1
    assert labeled_value(exporter_module.JOB_ACTIVE_COUNT_BY_STATE, "RUNNING") == 2
    assert labeled_value(exporter_module.JOB_ACTIVE_COUNT_BY_METHOD, "replication.run", "RUNNING") == 2
    assert labeled_value(exporter_module.JOB_ACTIVE_COUNT_BY_METHOD, "pool.scrub.run", "WAITING") == 1
    assert gauge_value(exporter_module.JOB_ABORTABLE_ACTIVE_COUNT) == 1
    assert gauge_value(exporter_module.JOB_TRANSIENT_ACTIVE_COUNT) == 1
    assert labeled_value(exporter_module.JOB_PROGRESS_PERCENT, "replication.run") == 55
    assert labeled_value(exporter_module.JOB_OLDEST_ACTIVE_TS, "RUNNING") == exporter_module._parse_ts("2025-02-01T00:05:00+00:00")
    assert labeled_value(exporter_module.JOB_OLDEST_ACTIVE_TS, "WAITING") == exporter_module._parse_ts("2025-02-01T00:01:00+00:00")
    assert calls[:2] == [
        ("core.get_jobs", [[["state", "=", "WAITING"]], {"count": True}]),
        ("core.get_jobs", [[["state", "=", "RUNNING"]], {"count": True}]),
    ]


def test_job_flag_metrics_stay_nan_when_detail_query_fails(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", query_limit=1))
    exporter._reset_poll_metrics()

    def fake_call(client, method, params=None):
        assert method == "core.get_jobs"
        filters, options = params
        if options == {"count": True}:
            if filters == [["state", "=", "WAITING"]]:
                return 3
            if filters == [["state", "=", "RUNNING"]]:
                return 4
        raise RuntimeError("detail query failed")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_job_metrics(object())

    assert gauge_value(exporter_module.JOB_ACTIVE_COUNT) == 7
    assert labeled_value(exporter_module.JOB_ACTIVE_COUNT_BY_STATE, "WAITING") == 3
    assert labeled_value(exporter_module.JOB_ACTIVE_COUNT_BY_STATE, "RUNNING") == 4
    assert math.isnan(gauge_value(exporter_module.JOB_ABORTABLE_ACTIVE_COUNT))
    assert math.isnan(gauge_value(exporter_module.JOB_TRANSIENT_ACTIVE_COUNT))


def test_job_flag_metrics_publish_zero_when_no_active_jobs(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", query_limit=1))
    exporter._reset_poll_metrics()

    def fake_call(client, method, params=None):
        assert method == "core.get_jobs"
        filters, options = params
        assert options == {"count": True}
        if filters in (
            [["state", "=", "WAITING"]],
            [["state", "=", "RUNNING"]],
        ):
            return 0
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_job_metrics(object())

    assert gauge_value(exporter_module.JOB_ACTIVE_COUNT) == 0
    assert gauge_value(exporter_module.JOB_ABORTABLE_ACTIVE_COUNT) == 0
    assert gauge_value(exporter_module.JOB_TRANSIENT_ACTIVE_COUNT) == 0


def test_app_query_enrichment_metrics(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))

    def fake_call(client, method, params=None):
        if method in {"vm.query", "app.query"} and params[1].get("count"):
            return 0 if method == "vm.query" else 1
        if method == "app.outdated_docker_images":
            return []
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_entity_detail_metrics(
        object(),
        {
            "vm.query": [],
            "app.query": [
                {
                    "name": "plex",
                    "state": "RUNNING",
                    "upgrade_available": True,
                    "image_updates_available": False,
                    "custom_app": False,
                    "migrated": True,
                    "active_workloads": {
                        "containers": 2,
                        "used_ports": [{"container_port": 32400}, {"container_port": 1900}],
                        "used_host_ips": ["10.0.0.10", "10.0.0.11"],
                        "container_details": [
                            {"state": "running"},
                            {"state": "exited"},
                        ],
                    },
                }
            ],
        },
    )

    assert gauge_value(exporter_module.APP_COUNT) == 1
    assert labeled_value(exporter_module.APP_STATE, "plex", "RUNNING") == 1
    assert labeled_value(exporter_module.APP_UPGRADE_AVAILABLE, "plex") == 1
    assert labeled_value(exporter_module.APP_IMAGE_UPDATES_AVAILABLE, "plex") == 0
    assert labeled_value(exporter_module.APP_CUSTOM, "plex") == 0
    assert labeled_value(exporter_module.APP_MIGRATED, "plex") == 1
    assert labeled_value(exporter_module.APP_CONTAINER_COUNT, "plex") == 2
    assert labeled_value(exporter_module.APP_USED_PORT_COUNT, "plex") == 2
    assert labeled_value(exporter_module.APP_USED_HOST_IP_COUNT, "plex") == 2
    assert labeled_value(exporter_module.APP_CONTAINER_STATE_COUNT, "plex", "RUNNING") == 1
    assert labeled_value(exporter_module.APP_CONTAINER_STATE_COUNT, "plex", "EXITED") == 1


def test_boot_env_metrics_use_used_bytes_field(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    calls = []
    environments = json.loads(
        (FIXTURES / "boot_environment_query.json").read_text(encoding="utf-8")
    )

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "boot.environment.query"
        if params[1].get("count"):
            return len(environments)
        return environments

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_boot_env_metrics(object(), {})

    assert calls[0][1][1]["select"] == ["id", "active", "activated", "keep", "created", "used_bytes"]
    assert exporter_module.BOOT_ENV_SIZE_BYTES.labels(name="default")._value.get() == 2048.0
    assert exporter_module.BOOT_ENV_USED_BYTES.labels(name="next")._value.get() == 0.0
    assert exporter_module.BOOT_ENV_ACTIVATED.labels(name="default")._value.get() == 0.0
    assert exporter_module.BOOT_ENV_ACTIVATED.labels(name="next")._value.get() == 1.0
    assert exporter_module.BOOT_ENV_ACTIVATED_COUNT._value.get() == 1.0


def test_certificate_metrics_do_not_request_undocumented_issuer_field(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        assert method == "certificate.query"
        return [{"name": "ui_cert", "until": "2099-01-01T00:00:00+00:00", "CSR": None}]

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_certificate_metrics(object())

    assert calls[0][1][1]["select"] == ["name", "until", "CSR"]
    assert exporter_module.CERT_DAYS_TO_EXPIRY.labels(name="ui_cert", issuer="unknown")._value.get() > 0
    assert exporter_module.CERT_EXPIRY_TIMESTAMP_SECONDS.labels(name="ui_cert")._value.get() > 0


def test_inventory_collectors_accept_numeric_count_results(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))

    counts = {
        "user.query": 11,
        "group.query": 12,
        "staticroute.query": 13,
        "tunable.query": 14,
        "privilege.query": 15,
        "initshutdownscript.query": 16,
        "keychaincredential.query": 17,
        "iscsi.target.query": 21,
        "iscsi.portal.query": 22,
        "iscsi.extent.query": 23,
        "iscsi.initiator.query": 24,
        "nvmet.host.query": 31,
        "nvmet.namespace.query": 32,
        "app.image.query": 41,
        "dns.query": 42,
        "reporting.exporters.query": 43,
    }

    def fake_call(client, method, params=None):
        if method in counts:
            assert params[1] == {"count": True}
            return counts[method]
        if method == "network.configuration.config":
            return {"httpproxy": ""}
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 6}
        if method == "service.query":
            return [{"service": "netdata", "enable": False}]
        if method == "reporting.config":
            return {"tier0_days": 7, "tier1_days": 30, "tier1_update_interval_seconds": 300}
        if method == "system.ntpserver.query":
            return []
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_inventory_counts(object(), {})
    exporter._collect_iscsi_inventory(object(), {})
    exporter._collect_nvmet_extended(object(), {})
    exporter._collect_misc_configs(object(), {})

    assert gauge_value(exporter_module.LOCAL_USER_COUNT) == 11
    assert gauge_value(exporter_module.LOCAL_GROUP_COUNT) == 12
    assert gauge_value(exporter_module.STATIC_ROUTE_COUNT) == 13
    assert gauge_value(exporter_module.TUNABLE_COUNT) == 14
    assert gauge_value(exporter_module.PRIVILEGE_COUNT) == 15
    assert gauge_value(exporter_module.INITSHUTDOWNSCRIPT_COUNT) == 16
    assert gauge_value(exporter_module.KEYCHAIN_CREDENTIAL_COUNT) == 17
    assert gauge_value(exporter_module.ISCSI_TARGET_COUNT) == 21
    assert gauge_value(exporter_module.ISCSI_PORTAL_COUNT) == 22
    assert gauge_value(exporter_module.ISCSI_EXTENT_COUNT) == 23
    assert gauge_value(exporter_module.ISCSI_INITIATOR_COUNT) == 24
    assert gauge_value(exporter_module.NVMET_HOST_COUNT) == 31
    assert gauge_value(exporter_module.NVMET_NAMESPACE_COUNT) == 32
    assert gauge_value(exporter_module.DOCKER_IMAGE_COUNT) == 41
    assert gauge_value(exporter_module.DNS_RESOLVER_COUNT) == 42
    assert gauge_value(exporter_module.REPORTING_EXPORTER_COUNT) == 43


def test_enabled_gauges_follow_service_enable_state(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))

    def fake_call(client, method, params=None):
        if method == "service.query":
            requested = tuple(params[0][0][2])
            if requested == ("ssh", "ftp", "snmp"):
                return [
                    {"service": "ssh", "enable": False},
                    {"service": "ftp", "enable": True},
                    {"service": "snmp", "enable": False},
                ]
            if requested == ("netdata", "reporting"):
                return [{"service": "netdata", "enable": True}]
        if method == "smb.config":
            return {"multichannel": False}
        if method == "nfs.config":
            return {"protocols": ["NFSV4"], "servers": 8, "rdma": False}
        if method == "network.configuration.config":
            return {"httpproxy": ""}
        if method == "app.image.query":
            return 0
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 2}
        if method == "reporting.exporters.query":
            return 0
        if method == "dns.query":
            return 1
        if method == "reporting.config":
            return {"tier0_days": 7, "tier1_days": 30, "tier1_update_interval_seconds": 300}
        if method == "system.ntpserver.query":
            return []
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_protocol_configs(object(), {})
    exporter._collect_misc_configs(object(), {})

    assert gauge_value(exporter_module.SSH_ENABLED) == 0
    assert math.isnan(gauge_value(exporter_module.SSH_PASSWORD_AUTH))
    assert gauge_value(exporter_module.FTP_ENABLED) == 1
    assert gauge_value(exporter_module.SNMP_ENABLED) == 0
    assert gauge_value(exporter_module.REPORTING_ENABLED) == 1


@pytest.mark.parametrize(
    ("reporting_rows", "expected"),
    [
        ([], math.nan),
        ([{"service": "netdata", "enable": False}], 0),
        ([{"service": "netdata", "enable": True}], 1),
    ],
)
def test_reporting_enabled_requires_matching_service_row(monkeypatch, reporting_rows, expected):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    exporter._reset_poll_metrics()

    def fake_call(client, method, params=None):
        if method == "network.configuration.config":
            return {"httpproxy": ""}
        if method == "app.image.query":
            return 0
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 2}
        if method == "reporting.exporters.query":
            return 0
        if method == "service.query":
            requested = tuple(params[0][0][2])
            assert requested == ("netdata", "reporting")
            return reporting_rows
        if method == "dns.query":
            return 1
        if method == "reporting.config":
            return {"tier0_days": 7, "tier1_days": 30, "tier1_update_interval_seconds": 300}
        if method == "system.ntpserver.query":
            return []
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_misc_configs(object(), {})

    value = gauge_value(exporter_module.REPORTING_ENABLED)
    if math.isnan(expected):
        assert math.isnan(value)
    else:
        assert value == expected


def test_load_config_parses_defaults_and_lists(monkeypatch):
    for key in (
        "TRUENAS_WS_URL",
        "TRUENAS_API_KEY",
        "TRUENAS_VERIFY_TLS",
        "FILESYSTEM_PATHS",
        "EXTRA_METHODS",
        "EVENT_SUBSCRIPTIONS",
        "ENABLE_EVENT_STREAMS",
    ):
        monkeypatch.delenv(key, raising=False)

    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    monkeypatch.setenv("TRUENAS_VERIFY_TLS", "no")
    monkeypatch.setenv("FILESYSTEM_PATHS", "/mnt/data, /mnt/backups")
    monkeypatch.setenv("EXTRA_METHODS", "foo.query, bar.config")
    monkeypatch.setenv("EVENT_SUBSCRIPTIONS", "app.stats,reporting.realtime")
    monkeypatch.setenv("ENABLE_EVENT_STREAMS", "0")

    config = exporter_module._load_config()

    assert config.ws_url == "wss://nas.example/api/current"
    assert config.api_key == "secret"
    assert config.verify_tls is False
    assert config.filesystem_paths == ["/mnt/data", "/mnt/backups"]
    assert config.extra_methods == ["foo.query", "bar.config"]
    assert config.event_subscriptions == ["app.stats", "reporting.realtime"]
    assert config.enable_event_streams is False
    assert config.query_limit == 200
    assert config.exporter_port == 9108


@pytest.mark.parametrize(
    ("env", "message"),
    [
        ({}, "TRUENAS_WS_URL is required"),
        ({"TRUENAS_WS_URL": "wss://nas.example/api/current"}, "TRUENAS_API_KEY or TRUENAS_API_KEY_FILE is required"),
    ],
)
def test_load_config_requires_mandatory_env(monkeypatch, env, message):
    monkeypatch.delenv("TRUENAS_WS_URL", raising=False)
    monkeypatch.delenv("TRUENAS_API_KEY", raising=False)
    monkeypatch.delenv("TRUENAS_API_KEY_FILE", raising=False)
    for key, value in env.items():
        monkeypatch.setenv(key, value)

    with pytest.raises(ValueError, match=message):
        exporter_module._load_config()


# ---------------------------------------------------------------------------
# Phase 1 additions
# ---------------------------------------------------------------------------


def test_load_config_new_flags_defaults(monkeypatch):
    for key in ("TRUENAS_WS_URL", "TRUENAS_API_KEY"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    for key in ("ENABLE_GENERIC_METHOD_METRICS", "ENABLE_GENERIC_EVENT_METRICS", "DATASET_SNAPSHOT_FALLBACK_LIMIT"):
        monkeypatch.delenv(key, raising=False)

    config = exporter_module._load_config()

    assert config.enable_generic_method_metrics is False
    assert config.enable_generic_event_metrics is False
    assert config.dataset_snapshot_fallback_limit == 25


def test_load_config_new_flags_enabled(monkeypatch):
    for key in ("TRUENAS_WS_URL", "TRUENAS_API_KEY"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setenv("TRUENAS_WS_URL", "wss://nas.example/api/current")
    monkeypatch.setenv("TRUENAS_API_KEY", "secret")
    monkeypatch.setenv("ENABLE_GENERIC_METHOD_METRICS", "true")
    monkeypatch.setenv("ENABLE_GENERIC_EVENT_METRICS", "1")
    monkeypatch.setenv("DATASET_SNAPSHOT_FALLBACK_LIMIT", "25")

    config = exporter_module._load_config()

    assert config.enable_generic_method_metrics is True
    assert config.enable_generic_event_metrics is True
    assert config.dataset_snapshot_fallback_limit == 25


def test_dataset_snapshot_fallback_can_be_disabled(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", dataset_snapshot_fallback_limit=0))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "pool.dataset.query":
            return [{"name": "tank/data", "used": 1.0, "available": 2.0}]
        raise AssertionError(f"Unexpected fallback call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_dataset_metrics(object())

    methods_called = [c[0] for c in calls]
    assert "pool.dataset.snapshot_count" not in methods_called


def test_dataset_snapshot_fallback_failure_leaves_count_absent(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", dataset_snapshot_fallback_limit=25))

    def fake_call(client, method, params=None):
        if method == "pool.dataset.query":
            return [{"name": "tank/data", "used": 1.0, "available": 2.0}]
        if method == "pool.dataset.snapshot_count":
            raise RuntimeError("snapshot count unavailable")
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_dataset_metrics(object())

    assert exporter_module.DATASET_USED_BYTES.labels(dataset="tank/data")._value.get() == 1.0
    assert not list(exporter_module.DATASET_SNAPSHOT_COUNT.collect())[0].samples


def test_dataset_snapshot_fallback_calls_are_capped_by_limit(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", dataset_snapshot_fallback_limit=2))
    snapshot_calls = []

    def fake_call(client, method, params=None):
        if method == "pool.dataset.query":
            return [
                {"name": "tank/one", "used": 1.0},
                {"name": "tank/two", "used": 2.0},
                {"name": "tank/three", "used": 3.0},
            ]
        if method == "pool.dataset.snapshot_count":
            snapshot_calls.append(params[0])
            return len(snapshot_calls)
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_dataset_metrics(object())

    assert snapshot_calls == ["tank/one", "tank/two"]
    assert exporter_module.DATASET_SNAPSHOT_COUNT.labels(dataset="tank/one")._value.get() == 1.0
    assert exporter_module.DATASET_SNAPSHOT_COUNT.labels(dataset="tank/two")._value.get() == 2.0
    samples = {
        sample.labels["dataset"]: sample.value
        for sample in list(exporter_module.DATASET_SNAPSHOT_COUNT.collect())[0].samples
    }
    assert "tank/three" not in samples


def test_generic_event_metrics_gated_by_flag():
    """With enable_generic_event_metrics=False, _dispatch_event skips generic extraction."""
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_generic_event_metrics=False))
    called = []

    original = exporter._replace_generic_event_metrics

    def spy(*args, **kwargs):
        called.append(args)
        return original(*args, **kwargs)

    exporter._replace_generic_event_metrics = spy

    exporter._dispatch_event("pool.query", {"fields": {"status": "ONLINE"}})

    assert called == [], "Generic event extraction should be skipped when disabled"


def test_generic_event_metrics_enabled():
    """With enable_generic_event_metrics=True, _dispatch_event calls generic extraction."""
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_generic_event_metrics=True))
    called = []

    original = exporter._replace_generic_event_metrics

    def spy(*args, **kwargs):
        called.append(args)
        return original(*args, **kwargs)

    exporter._replace_generic_event_metrics = spy

    exporter._dispatch_event("pool.query", {"fields": {"status": "ONLINE"}})

    assert len(called) == 1


def test_landing_page():
    """The / endpoint returns an HTML landing page with links."""
    captured_status = []
    captured_headers = []

    def start_response(status, headers):
        captured_status.append(status)
        captured_headers.extend(headers)

    body = exporter_module._LANDING_PAGE

    assert b"/metrics" in body
    assert b"/healthz" in body
    assert b"/readyz" in body


def test_disable_created_metrics():
    """Verify that disable_created_metrics was called (Counter has no _created child)."""
    # After disable_created_metrics(), new Counters should not produce _created series.
    # We can verify by checking that the module-level counter doesn't have _created.
    from prometheus_client import generate_latest
    output = generate_latest().decode()
    assert "truenas_api_call_errors_created" not in output


# ---------------------------------------------------------------------------
# Phase 2 additions — performance and cardinality tuning
# ---------------------------------------------------------------------------


def test_scrub_task_collector_uses_exact_count_and_bounded_detail(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "pool.scrub.query":
            if params[1].get("count"):
                return 301
            return [{"id": 1, "pool_name": "tank", "enabled": True}]
        raise AssertionError(f"Unexpected call: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_scrub_task_metrics(object(), {})

    scrub_calls = [c for c in calls if c[0] == "pool.scrub.query"]
    assert len(scrub_calls) == 2
    assert scrub_calls[1][1] == [[], {"count": True}]
    assert gauge_value(exporter_module.POOL_SCRUB_TASK_COUNT) == 301


def test_cloud_backup_collector_uses_exact_count_and_safe_detail_select(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "cloud_backup.query":
            if params[1].get("count"):
                return 402
            return [
                {"id": 1, "enabled": True},
                {"id": 2, "enabled": False},
            ]
        raise AssertionError(f"Unexpected call: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_cloud_backup_metrics(object(), {})

    backup_calls = [c for c in calls if c[0] == "cloud_backup.query"]
    assert len(backup_calls) == 2
    assert backup_calls[0][1][1]["select"] == ["id", "enabled"]
    assert gauge_value(exporter_module.CLOUD_BACKUP_TASK_COUNT) == 402
    assert not list(exporter_module.CLOUD_BACKUP_TASK_STATE.collect())[0].samples


def test_cronjob_collector_uses_exact_count_and_excludes_command(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "cronjob.query":
            if params[1].get("count"):
                return 503
            return [{"id": 1, "description": "nightly", "enabled": True, "command": "echo hi"}]
        raise AssertionError(f"Unexpected call: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_cronjob_metrics(object(), {})

    cron_calls = [c for c in calls if c[0] == "cronjob.query"]
    assert len(cron_calls) == 2
    assert cron_calls[0][1][1]["select"] == ["id", "enabled"]
    assert gauge_value(exporter_module.CRONJOB_COUNT) == 503


def task_samples(metric, **labels):
    family = list(metric.collect())[0]
    return [
        sample
        for sample in family.samples
        if sample.name == family.name and all(sample.labels.get(key) == value for key, value in labels.items())
    ]


def task_sample_value(metric, **labels):
    samples = task_samples(metric, **labels)
    assert len(samples) == 1
    return samples[0].value


def test_task_collectors_emit_outcomes_and_use_safe_selects(monkeypatch):
    config = make_config(exporter_mode="legacy", enable_task_metrics=True)
    exporter = exporter_module.TrueNASExporter(config)
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        if method == "replication.query":
            options = params[1]
            if options.get("count"):
                return 1
            return [{
                "id": 1,
                "name": "replicate-nightly",
                "enabled": True,
                "state": {"state": "ERROR", "datetime": {"$date": 1750000000000}},
            }]
        if method == "cloudsync.query":
            options = params[1]
            if options.get("count"):
                return 1
            return [{
                "id": 2,
                "description": "cloud-nightly",
                "enabled": False,
                "job": {
                    "state": "SUCCESS",
                    "time_finished": {"$date": 1750000100000},
                    "progress": {"percent": 100},
                },
            }]
        if method == "rsynctask.query":
            options = params[1]
            if options.get("count"):
                return 1
            return [{"id": 3, "enabled": True, "job": None}]
        if method == "pool.snapshottask.query":
            options = params[1]
            if options.get("count"):
                return 1
            return [{
                "id": 4,
                "enabled": True,
                "state": {"state": "FINISHED", "datetime": {"$date": 1750000200000}},
            }]
        if method in ("pool.snapshottask.max_count", "pool.snapshottask.max_total_count"):
            return 0
        raise AssertionError(f"Unexpected call: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_task_metrics(object())

    expected_selects = {
        "replication.query": ["id", "name", "enabled", "state"],
        "cloudsync.query": ["id", "description", "enabled", "job"],
        "rsynctask.query": ["id", "enabled", "job"],
        "pool.snapshottask.query": ["id", "enabled", "state"],
    }
    for method, expected_select in expected_selects.items():
        method_calls = [call for call in calls if call[0] == method]
        assert len(method_calls) == 2
        assert method_calls[0][1][1]["select"] == expected_select
        assert method_calls[1][1] == [[], {"count": True}]

    assert task_sample_value(
        exporter_module.TASK_STATE,
        task_type="replication",
        name="replicate-nightly",
        state="ERROR",
    ) == 1
    assert task_sample_value(
        exporter_module.TASK_STATE,
        task_type="cloudsync",
        name="cloud-nightly",
        state="SUCCESS",
    ) == 1
    assert task_sample_value(
        exporter_module.TASK_STATE,
        task_type="snapshottask",
        name="4",
        state="FINISHED",
    ) == 1
    assert task_sample_value(
        exporter_module.TASK_LAST_RUN_TS,
        task_type="replication",
        name="replicate-nightly",
    ) == 1750000000.0
    assert task_sample_value(
        exporter_module.TASK_LAST_RUN_TS,
        task_type="cloudsync",
        name="cloud-nightly",
    ) == 1750000100.0
    assert task_sample_value(
        exporter_module.TASK_LAST_RUN_TS,
        task_type="snapshottask",
        name="4",
    ) == 1750000200.0
    assert task_sample_value(exporter_module.TASK_ENABLED, task_type="rsynctask", name="3") == 1
    assert not task_samples(exporter_module.TASK_STATE, task_type="rsynctask", name="3")
    assert not task_samples(exporter_module.TASK_LAST_RUN_TS, task_type="rsynctask", name="3")


def test_task_outcome_unknown_state_maps_to_unknown(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_task_metrics=True))

    def fake_call(client, method, params=None):
        if method == "replication.query":
            if params[1].get("count"):
                return 1
            return [{
                "id": 1,
                "name": "replicate-nightly",
                "enabled": True,
                "state": {"state": "WEIRD_NEW_STATE", "datetime": {"$date": 1750000000000}},
            }]
        if method in ("cloudsync.query", "rsynctask.query", "pool.snapshottask.query"):
            return 0 if params[1].get("count") else []
        if method in ("pool.snapshottask.max_count", "pool.snapshottask.max_total_count"):
            return 0
        raise AssertionError(f"Unexpected call: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_task_metrics(object())

    assert task_sample_value(
        exporter_module.TASK_STATE,
        task_type="replication",
        name="replicate-nightly",
        state="UNKNOWN",
    ) == 1


def test_task_query_failure_leaves_that_type_absent(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_task_metrics=True))

    def fake_call(client, method, params=None):
        if method == "replication.query":
            raise RuntimeError("replication unavailable")
        if method == "cloudsync.query":
            if params[1].get("count"):
                return 1
            return [{
                "id": 2,
                "description": "cloud-nightly",
                "enabled": True,
                "job": {"state": "SUCCESS", "time_finished": {"$date": 1750000100000}},
            }]
        if method in ("rsynctask.query", "pool.snapshottask.query"):
            return 0 if params[1].get("count") else []
        if method in ("pool.snapshottask.max_count", "pool.snapshottask.max_total_count"):
            return 0
        raise AssertionError(f"Unexpected call: {method}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_task_metrics(object())

    assert not task_samples(exporter_module.TASK_COUNT, task_type="replication")
    assert not task_samples(exporter_module.TASK_ENABLED, task_type="replication")
    assert not task_samples(exporter_module.TASK_STATE, task_type="replication")
    assert not task_samples(exporter_module.TASK_LAST_RUN_TS, task_type="replication")
    assert task_sample_value(
        exporter_module.TASK_STATE,
        task_type="cloudsync",
        name="cloud-nightly",
        state="SUCCESS",
    ) == 1


def test_reporting_graph_discovery_skipped_when_generic_disabled(monkeypatch):
    """Phase 2: graph discovery calls are skipped when enable_generic_method_metrics=False."""
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_generic_method_metrics=False))
    calls = []

    def fake_safe_call(client, method):
        calls.append(method)
        return None

    monkeypatch.setattr(exporter, "_safe_call_auto", fake_safe_call)

    cache = {}
    exporter._collect_reporting_timeseries(object(), cache)

    graph_calls = [c for c in calls if "graph" in c or "reporting" in c]
    assert graph_calls == [], f"No graph discovery calls expected, got {graph_calls}"
    assert cache == {}


def test_reporting_graph_discovery_runs_when_generic_enabled(monkeypatch):
    """Phase 2: graph discovery calls run when enable_generic_method_metrics=True."""
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", enable_generic_method_metrics=True))
    calls = []

    def fake_safe_call(client, method):
        calls.append(method)
        if method == "reporting.netdata_graphs":
            return [{"name": "cpu"}]
        return None

    monkeypatch.setattr(exporter, "_safe_call_auto", fake_safe_call)

    extracted = []
    original_extract = exporter._extract_generic_metrics

    def spy_extract(*args, **kwargs):
        extracted.append(args[0])
        return original_extract(*args, **kwargs)

    monkeypatch.setattr(exporter, "_extract_generic_metrics", spy_extract)

    cache = {}
    exporter._collect_reporting_timeseries(object(), cache)

    assert "reporting.netdata_graphs" in calls
    assert "reporting.graphs" in calls
    assert "reporting.netdata_graphs" in cache
    assert "reporting.netdata_graphs" in extracted


def test_undocumented_smart_results_method_is_never_called(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    monkeypatch.setattr(
        exporter,
        "_safe_call_auto",
        lambda *_args, **_kwargs: pytest.fail("undocumented SMART RPC must not be called"),
    )

    exporter._collect_smart_test_results(object())
    assert not list(exporter_module.SMART_TEST_LAST_RESULT.collect())[0].samples
    assert not list(exporter_module.SMART_TEST_LAST_TIMESTAMP.collect())[0].samples


def test_smart_results_unavailable_is_non_fatal(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    monkeypatch.setattr(exporter, "_safe_call_auto", lambda client, method: None)

    exporter._collect_smart_test_results(object())


def test_safe_call_auto_runtime_skips_missing_argument_methods(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))
    calls = []

    def fake_call(client, method, params=None):
        calls.append((method, params))
        raise exporter_module.JsonRpcError(
            "virt.global.get_network failed: {'error': '[EINVAL] missing required argument: id'}"
        )

    monkeypatch.setattr(exporter, "_call", fake_call)

    assert exporter._safe_call_auto(object(), "virt.global.get_network") is None
    assert exporter._safe_call_auto(object(), "virt.global.get_network") is None
    assert len(calls) == 1
    assert "virt.global.get_network" in exporter._auto_skipped_methods


def test_requires_entity_param_includes_virt_global_get_network():
    assert "virt.global.get_network" in exporter_module.REQUIRES_ENTITY_PARAM


def test_priority_gap_collectors_emit_dedicated_metrics(monkeypatch):
    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy", ))

    def fake_call(client, method, params=None):
        if method == "service.query":
            requested = tuple(params[0][0][2])
            if requested == ("netdata", "reporting"):
                return [{"service": "netdata", "enable": True}]
            if requested == ("ssh", "ftp", "snmp"):
                return []
        if method in {
            "reporting.exporters.query",
            "dns.query",
            "app.image.query",
            "alertservice.query",
        } and params[1].get("count"):
            return 0
        if method == "replication.config.config":
            return {"max_parallel_replication_tasks": 1}
        if method in {
            "vm.device.iommu_enabled",
            "vm.supports_virtualization",
            "iscsi.global.alua_enabled",
            "iscsi.global.iser_enabled",
        }:
            return False
        if method == "vm.maximum_supported_vcpus":
            return 16
        if method == "support.is_available":
            return True
        if method == "systemdataset.config":
            return {"pool": None}
        if method == "auth.twofactor.config":
            return {"enabled": False}
        if method == "alertservice.query":
            return []
        if method == "system.ntpserver.query":
            if params[1].get("count"):
                return 2
            return [
                {"prefer": True, "burst": False, "iburst": True, "minpoll": 6, "maxpoll": 10},
                {"prefer": False, "burst": True, "iburst": False, "minpoll": 8, "maxpoll": 12},
            ]
        if method == "iscsi.global.sessions":
            filters = params[0]
            if not filters:
                return 2
            return 1
        raise AssertionError(f"Unexpected call: {method} {params}")

    monkeypatch.setattr(exporter, "_call", fake_call)

    cache = {
        "app.image.dockerhub_rate_limit": {
            "total_pull_limit": 100,
            "remaining_pull_limit": 75,
            "total_time_limit_in_secs": 21600,
            "remaining_time_limit_in_secs": 3600,
            "error": "",
        },
        "update.config": {"autocheck": True, "profile": "STABLE"},
        "catalog.config": {"preferred_trains": ["stable", "enterprise"]},
        "hardware.virtualization.variant": "INTEL",
        "vm.flags": {"intel_vmx": True, "amd_rvi": False, "unrestricted_guest": True, "amd_asids": True},
        "vm.virtualization_details": {"supported": True, "error": ""},
        "directoryservices.status": {
            "type": "ACTIVEDIRECTORY",
            "status": "HEALTHY",
            "status_msg": None,
        },
        "system.security.config": {
            "enable_fips": True,
            "enable_gpos_stig": False,
            "min_password_length": 14,
            "min_password_age": 1,
            "max_password_age": 90,
            "password_history_length": 5,
        },
        "support.is_available_and_enabled": True,
        "reporting.config": {"tier0_days": 14, "tier1_days": 60, "tier1_update_interval": 300},
    }

    exporter._collect_app_extras(object(), cache)
    exporter._collect_update_extras(object(), cache)
    exporter._collect_catalog_metrics(object(), cache)
    exporter._collect_vm_extras(object(), cache)
    exporter._collect_directoryservices_metrics(object(), cache)
    exporter._collect_infrastructure_configs(object(), cache)
    exporter._collect_iscsi_extras(object(), cache)
    exporter._collect_misc_configs(object(), cache)
    exporter._collect_security_posture(object(), cache)

    assert gauge_value(exporter_module.APP_DOCKERHUB_PULL_LIMIT_TOTAL) == 100
    assert gauge_value(exporter_module.APP_DOCKERHUB_PULL_LIMIT_REMAINING) == 75
    assert gauge_value(exporter_module.APP_DOCKERHUB_PULL_LIMIT_WINDOW_SECONDS) == 21600
    assert gauge_value(exporter_module.APP_DOCKERHUB_PULL_LIMIT_REMAINING_WINDOW_SECONDS) == 3600
    assert gauge_value(exporter_module.APP_DOCKERHUB_RATE_LIMIT_ERROR_PRESENT) == 0
    assert gauge_value(exporter_module.UPDATE_AUTOCHECK_ENABLED) == 1
    assert labeled_value(exporter_module.UPDATE_PROFILE_INFO, "STABLE") == 1
    assert gauge_value(exporter_module.CATALOG_CONFIG_PRESENT) == 1
    assert gauge_value(exporter_module.CATALOG_PREFERRED_TRAIN_COUNT) == 2
    assert gauge_value(exporter_module.VM_FLAG_INTEL_VMX) == 1
    assert gauge_value(exporter_module.VM_FLAG_AMD_RVI) == 0
    assert gauge_value(exporter_module.VM_FLAG_UNRESTRICTED_GUEST) == 1
    assert gauge_value(exporter_module.VM_FLAG_AMD_ASIDS) == 1
    assert gauge_value(exporter_module.VM_FLAG_AMD_ASIDS_SUPPORTED) == 1
    assert gauge_value(exporter_module.VM_VIRTUALIZATION_DETAILS_SUPPORTED) == 1
    assert gauge_value(exporter_module.VM_VIRTUALIZATION_DETAILS_ERROR_PRESENT) == 0
    assert gauge_value(exporter_module.DIRECTORYSERVICES_CONFIG_ENABLED) == 1
    assert labeled_value(exporter_module.DIRECTORYSERVICES_SERVICE_TYPE, "ACTIVEDIRECTORY") == 1
    assert labeled_value(exporter_module.DIRECTORYSERVICES_HEALTHY, "activedirectory") == 1
    assert gauge_value(exporter_module.SYSTEM_SECURITY_FIPS_CONFIGURED) == 1
    assert gauge_value(exporter_module.SYSTEM_SECURITY_GPOS_STIG) == 0
    assert gauge_value(exporter_module.SYSTEM_SECURITY_PASSWORD_MIN_LENGTH) == 14
    assert gauge_value(exporter_module.SYSTEM_SECURITY_PASSWORD_MIN_AGE_DAYS) == 1
    assert gauge_value(exporter_module.SYSTEM_SECURITY_PASSWORD_MAX_AGE_DAYS) == 90
    assert math.isnan(gauge_value(exporter_module.SYSTEM_SECURITY_PASSWORD_WARN_AGE_DAYS))
    assert gauge_value(exporter_module.SYSTEM_SECURITY_PASSWORD_HISTORY_COUNT) == 5
    assert gauge_value(exporter_module.SUPPORT_AVAILABLE_AND_ENABLED) == 1
    assert math.isnan(gauge_value(exporter_module.SUPPORT_CONFIG_ENABLED))
    assert gauge_value(exporter_module.NTP_SERVER_COUNT) == 2
    assert math.isnan(gauge_value(exporter_module.NTP_SERVER_ACTIVE_COUNT))
    assert math.isnan(gauge_value(exporter_module.NTP_SERVER_REACHABLE_COUNT))
    assert gauge_value(exporter_module.NTP_SERVER_PREFER_COUNT) == 1
    assert gauge_value(exporter_module.NTP_SERVER_BURST_COUNT) == 1
    assert gauge_value(exporter_module.NTP_SERVER_IBURST_COUNT) == 1
    assert gauge_value(exporter_module.NTP_SERVER_MIN_POLL_MINUTES) == pytest.approx(2**6 / 60)
    assert gauge_value(exporter_module.NTP_SERVER_MAX_POLL_MINUTES) == pytest.approx(2**12 / 60)
    assert gauge_value(exporter_module.ISCSI_SESSION_COUNT) == 2
    assert gauge_value(exporter_module.ISCSI_SESSION_ISER_COUNT) == 1
    assert gauge_value(exporter_module.ISCSI_SESSION_OFFLOAD_COUNT) == 1
    assert gauge_value(exporter_module.ISCSI_SESSION_IMMEDIATE_DATA_COUNT) == 1
    assert gauge_value(exporter_module.REPORTING_TIER0_RETENTION_DAYS) == 14
    assert gauge_value(exporter_module.REPORTING_TIER1_RETENTION_DAYS) == 60
    assert gauge_value(exporter_module.REPORTING_TIER1_UPDATE_INTERVAL_SECONDS) == 300


def test_full_domain_scrape_accepts_empty_read_only_fixture(monkeypatch):
    """Walk every enabled domain collector without requiring a live TrueNAS."""

    class EmptyClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    config = make_config(
        exporter_mode="legacy",
        enable_dataset_metrics=True,
        enable_task_metrics=True,
        enable_ipmi_metrics=True,
        enable_generic_method_metrics=True,
        enable_filesystem_listdir=True,
        filesystem_paths=["/mnt"],
    )
    exporter = exporter_module.TrueNASExporter(config)
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: EmptyClient())

    def empty_call(_client, method, _params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info" or method.endswith(".config"):
            return {}
        return []

    monkeypatch.setattr(exporter, "_call", empty_call)
    exporter.scrape_once()

    assert exporter_module.SCRAPE_SUCCESS._value.get() == 1
    assert exporter.is_ready()


def test_full_domain_scrape_contains_optional_method_failures(monkeypatch):
    """Optional read failures must not escape or turn into mutating fallbacks."""

    class FailureClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    exporter = exporter_module.TrueNASExporter(
        make_config(
            exporter_mode="legacy",
            enable_dataset_metrics=True,
            enable_task_metrics=True,
            enable_ipmi_metrics=True,
            enable_filesystem_listdir=True,
        )
    )
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: FailureClient())

    def failing_call(_client, method, _params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {}
        raise exporter_module.JsonRpcError(f"{method} unavailable")

    monkeypatch.setattr(exporter, "_call", failing_call)
    exporter.scrape_once()

    assert exporter_module.SCRAPE_SUCCESS._value.get() in {0, 1}
    assert all(
        not exporter._is_safe_read_method(method)
        for method in ("system.reboot", "pool.delete", "app.update")
    )


def test_full_domain_scrape_accepts_sparse_entity_fixture(monkeypatch):
    """Exercise defensive entity parsing with minimally populated records."""

    class SparseClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    exporter = exporter_module.TrueNASExporter(
        make_config(
            exporter_mode="legacy",
            enable_dataset_metrics=True,
            enable_task_metrics=True,
            enable_ipmi_metrics=True,
            enable_filesystem_listdir=True,
        )
    )
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: SparseClient())

    def sparse_call(_client, method, _params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {"hostname": "nas", "version": "25.10.2", "product_type": "SCALE"}
        if method.endswith((".query", ".list", ".sessions")) or method == "core.get_jobs":
            return [{}]
        if method.endswith((".config", ".status", ".info", ".summary")):
            return {}
        return {}

    monkeypatch.setattr(exporter, "_call", sparse_call)
    exporter.scrape_once()

    assert exporter_module.LAST_SCRAPE_TS._value.get() > 0


def test_full_domain_scrape_accepts_rich_read_only_fixture(monkeypatch):
    """Exercise populated branches across the complete domain graph."""

    class RichClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    exporter = exporter_module.TrueNASExporter(
        make_config(
            exporter_mode="legacy",
            enable_dataset_metrics=True,
            enable_task_metrics=True,
            enable_ipmi_metrics=True,
            enable_filesystem_listdir=True,
            enable_generic_method_metrics=True,
        )
    )
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: RichClient())
    record = {
        "id": 1,
        "name": "demo",
        "description": "demo",
        "dataset": "tank/demo",
        "pool": "tank",
        "disk": "sda",
        "service": "ssh",
        "enabled": True,
        "enable": True,
        "running": True,
        "healthy": True,
        "warning": False,
        "active": True,
        "reachable": True,
        "state": "RUNNING",
        "status": "ONLINE",
        "size": 100,
        "used": 25,
        "available": 75,
        "allocated": 25,
        "free": 75,
        "referenced": 20,
        "quota": 0,
        "refquota": 0,
        "snapshot_count": 2,
        "fragmentation": 1,
        "temperature": 35,
        "progress": {"percent": 50},
        "job": {"state": "SUCCESS", "time_finished": "2026-01-01T00:00:00Z"},
        "scan": {"state": "SCANNING", "percentage": 10, "errors": 0},
        "topology": {"data": [{"name": "sda", "stats": {"read_errors": 0}}]},
        "properties": {},
    }

    def rich_call(_client, method, _params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {
                **record,
                "hostname": "nas",
                "version": "25.10.2",
                "product_type": "SCALE",
                "uptime_seconds": 100,
                "physmem": 1024,
                "cores": 4,
                "physical_cores": 2,
                "loadavg": [0.1, 0.2, 0.3],
            }
        if method.endswith((".query", ".list", ".sessions")) or method == "core.get_jobs":
            return [dict(record)]
        if method.endswith((".config", ".info", ".summary")):
            return dict(record)
        if method.endswith((".count", ".client_count", ".max_count", ".max_total_count")):
            return 1
        if method.endswith((".ready", ".enabled", ".available", ".supported")):
            return True
        return dict(record)

    monkeypatch.setattr(exporter, "_call", rich_call)
    exporter.scrape_once()

    assert exporter_module.SCRAPE_SUCCESS._value.get() == 1


def test_disk_temperature_alert_count_emits_zero_for_queried_disks_without_alerts(monkeypatch):
    class DiskClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: DiskClient())

    def disk_call(_client, method, _params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {}
        if method == "disk.query":
            return [
                {"name": "sda", "size": 100, "pool": "tank"},
                {"name": "sdb", "size": 200, "pool": None},
            ]
        if method == "disk.temperature_agg":
            return {}
        if method == "disk.temperature_alerts":
            assert _params == [["sda", "sdb"]]
            return [
                {"args": {"device": "sda"}, "id": "alert-1"},
                {"args": {"device": "sda"}, "id": "alert-2"},
            ]
        if method == "disk.temperatures":
            return {}
        if method.endswith((".query", ".list", ".sessions")) or method == "core.get_jobs":
            return []
        if method.endswith((".config", ".status", ".info", ".summary")):
            return {}
        return {}

    monkeypatch.setattr(exporter, "_call", disk_call)
    exporter.scrape_once()

    assert labeled_value(exporter_module.DISK_TEMP_ALERT_COUNT, "sda") == 2
    assert labeled_value(exporter_module.DISK_TEMP_ALERT_COUNT, "sdb") == 0


def test_disk_temperature_alert_failure_keeps_sibling_disk_metrics(monkeypatch):
    class DiskClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: DiskClient())

    def disk_call(_client, method, _params=None):
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {}
        if method == "disk.query":
            return [{"name": "sda", "size": 100, "pool": "tank"}]
        if method == "disk.temperature_agg":
            return {"sda": {"min": 31, "max": 35, "avg": 33}}
        if method == "disk.temperature_alerts":
            raise exporter_module.JsonRpcError("temperature alerts unavailable")
        if method == "disk.temperatures":
            return {"sda": 34}
        if method.endswith((".query", ".list", ".sessions")) or method == "core.get_jobs":
            return []
        if method.endswith((".config", ".status", ".info", ".summary")):
            return {}
        return {}

    monkeypatch.setattr(exporter, "_call", disk_call)
    exporter.scrape_once()

    assert list(exporter_module.DISK_TEMP_ALERT_COUNT.collect())[0].samples == []
    assert labeled_value(exporter_module.DISK_SIZE_BYTES, "sda") == 100
    assert labeled_value(exporter_module.DISK_TEMPERATURE_C, "sda") == 34
    assert labeled_value(exporter_module.DISK_TEMP_AGG_C, "sda", "min") == 31


def test_disk_temperature_alerts_not_called_without_disks(monkeypatch):
    class DiskClient:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return None

        def authenticate(self, _api_key, call=None):
            if call is not None:
                call("auth.login_with_api_key", [])

    exporter = exporter_module.TrueNASExporter(make_config(exporter_mode="legacy"))
    monkeypatch.setattr(exporter_module, "JsonRpcWsClient", lambda **_kwargs: DiskClient())
    calls = []

    def disk_call(_client, method, _params=None):
        calls.append(method)
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {}
        if method.endswith((".query", ".list", ".sessions")) or method == "core.get_jobs":
            return []
        if method.endswith((".config", ".status", ".info", ".summary")):
            return {}
        return {}

    monkeypatch.setattr(exporter, "_call", disk_call)
    exporter.scrape_once()

    assert "disk.temperature_alerts" not in calls
