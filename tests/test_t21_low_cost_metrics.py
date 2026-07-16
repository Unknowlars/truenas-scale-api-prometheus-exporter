import math
from typing import Any

import pytest
from conftest import make_config

import truenas_exporter as runtime
from truenas_exporter.compat_profiles import PROFILE_25_10, PROFILE_26_0, PROFILE_UNKNOWN


def reset_metric(metric: Any) -> None:
    if getattr(metric, "_labelnames", ()):  # pragma: no branch
        metric.clear()
    else:
        metric.set(float("nan"))


def labeled(metric: Any, *labels: str) -> float:
    return metric.labels(*labels)._value.get()


@pytest.fixture(autouse=True)
def reset_t21_metrics() -> None:
    for metric in (
        runtime.API_KEY_COUNT,
        runtime.API_KEY_EXPIRY_TS,
        runtime.API_KEY_REVOKED_COUNT,
        runtime.FAILOVER_NODE_REBOOT_REQUIRED,
        runtime.KMIP_SYNC_PENDING,
        runtime.POOL_STATUS_CODE,
    ):
        reset_metric(metric)


class ApiKeyClient:
    def __init__(self, result: Any) -> None:
        self.result = result
        self.calls: list[tuple[str, Any]] = []

    def call(self, method: str, params: Any = None) -> Any:
        self.calls.append((method, params))
        if method != "api_key.query":
            raise AssertionError(f"unexpected method: {method}")
        if (
            isinstance(params, list)
            and len(params) > 1
            and isinstance(params[1], dict)
            and params[1].get("count")
        ):
            return 1
        return self.result


def test_api_key_metrics_use_safe_select_and_export_expiry() -> None:
    exporter = runtime.TrueNASExporter(make_config())
    client = ApiKeyClient(
        [
            {
                "id": 1,
                "name": "backup",
                "expires_at": "2026-08-01T00:00:00Z",
                "revoked": False,
            },
            {"id": 2, "name": "permanent", "expires_at": None, "revoked": False},
            {"id": 3, "name": "old", "expires_at": "2026-07-01T00:00:00Z", "revoked": True},
        ]
    )

    exporter._collect_api_key_metrics(client)

    assert runtime.API_KEY_COUNT._value.get() == 3
    assert runtime.API_KEY_REVOKED_COUNT._value.get() == 1
    assert labeled(runtime.API_KEY_EXPIRY_TS, "backup") == 1785542400.0
    assert labeled(runtime.API_KEY_EXPIRY_TS, "old") == 1782864000.0
    assert ("permanent",) not in runtime.API_KEY_EXPIRY_TS._metrics
    assert client.calls == [
        (
            "api_key.query",
            [
                [],
                {
                    "limit": exporter.config.query_limit,
                    "select": ["id", "name", "expires_at", "revoked"],
                },
            ],
        ),
        ("api_key.query", [[["revoked", "=", True]], {"count": True}]),
    ]


def test_api_key_query_failure_leaves_metrics_absent() -> None:
    exporter = runtime.TrueNASExporter(make_config())

    class FailingClient:
        def call(self, method: str, params: Any = None) -> Any:
            raise RuntimeError("api key query failed")

    exporter._collect_api_key_metrics(FailingClient())

    assert math.isnan(runtime.API_KEY_COUNT._value.get())
    assert math.isnan(runtime.API_KEY_REVOKED_COUNT._value.get())
    assert not runtime.API_KEY_EXPIRY_TS._metrics


class FailoverClient:
    def __init__(self, result: Any) -> None:
        self.result = result
        self.calls: list[tuple[str, Any]] = []

    def call(self, method: str, params: Any = None) -> Any:
        self.calls.append((method, params))
        if method != "failover.reboot.info":
            raise AssertionError(f"unexpected method: {method}")
        return self.result


def test_failover_reboot_info_exports_per_node_required_flags() -> None:
    exporter = runtime.TrueNASExporter(make_config())
    client = FailoverClient(
        {
            "this_node": {"boot_id": "a", "reboot_required_reasons": []},
            "other_node": {
                "boot_id": "b",
                "reboot_required_reasons": [{"code": "UPDATE", "reason": "updated"}],
            },
        }
    )

    exporter._collect_failover_reboot_info(client)

    assert labeled(runtime.FAILOVER_NODE_REBOOT_REQUIRED, "this_node") == 0
    assert labeled(runtime.FAILOVER_NODE_REBOOT_REQUIRED, "other_node") == 1
    assert client.calls == [("failover.reboot.info", [])]


def test_failover_reboot_info_null_or_failure_leaves_node_absent() -> None:
    exporter = runtime.TrueNASExporter(make_config())
    exporter._collect_failover_reboot_info(
        FailoverClient({"this_node": {"reboot_required_reasons": []}, "other_node": None})
    )

    assert labeled(runtime.FAILOVER_NODE_REBOOT_REQUIRED, "this_node") == 0
    assert ("other_node",) not in runtime.FAILOVER_NODE_REBOOT_REQUIRED._metrics

    reset_metric(runtime.FAILOVER_NODE_REBOOT_REQUIRED)

    class FailingClient:
        def call(self, method: str, params: Any = None) -> Any:
            raise RuntimeError("not HA")

    exporter._collect_failover_reboot_info(FailingClient())
    assert not runtime.FAILOVER_NODE_REBOOT_REQUIRED._metrics


def test_kmip_sync_pending_exports_boolean_and_omits_null() -> None:
    exporter = runtime.TrueNASExporter(make_config())

    class KmipClient:
        def __init__(self, result: Any) -> None:
            self.result = result
            self.calls: list[tuple[str, Any]] = []

        def call(self, method: str, params: Any = None) -> Any:
            self.calls.append((method, params))
            if method != "kmip.kmip_sync_pending":
                raise AssertionError(f"unexpected method: {method}")
            return self.result

    true_client = KmipClient(True)
    exporter._collect_kmip_sync_pending(true_client, {})
    assert runtime.KMIP_SYNC_PENDING._value.get() == 1
    assert true_client.calls == [("kmip.kmip_sync_pending", [])]

    reset_metric(runtime.KMIP_SYNC_PENDING)
    exporter._collect_kmip_sync_pending(KmipClient(None), {})
    assert math.isnan(runtime.KMIP_SYNC_PENDING._value.get())


class ZpoolClient:
    def __init__(self, result: Any) -> None:
        self.result = result
        self.calls: list[tuple[str, Any]] = []

    def call(self, method: str, params: Any = None) -> Any:
        self.calls.append((method, params))
        if method != "zpool.query":
            raise AssertionError(f"unexpected method: {method}")
        return self.result


def test_v26_zpool_status_code_exports_profile_gated_metric() -> None:
    exporter = runtime.TrueNASExporter(make_config(), compatibility_profile=PROFILE_26_0)
    client = ZpoolClient(
        [
            {"name": "tank", "status_code": "OK"},
            {"name": "archive", "status_code": None},
        ]
    )

    exporter._collect_zpool_status_metrics(client)

    assert labeled(runtime.POOL_STATUS_CODE, "tank", "OK") == 1
    assert ("archive", "OK") not in runtime.POOL_STATUS_CODE._metrics
    assert client.calls == [("zpool.query", [{}])]


@pytest.mark.parametrize("profile", [PROFILE_25_10, PROFILE_UNKNOWN])
def test_non_v26_profiles_do_not_call_zpool_query(profile: Any) -> None:
    exporter = runtime.TrueNASExporter(make_config(), compatibility_profile=profile)
    client = ZpoolClient([{"name": "tank", "status_code": "OK"}])

    exporter._collect_zpool_status_metrics(client)

    assert client.calls == []
    assert not runtime.POOL_STATUS_CODE._metrics
