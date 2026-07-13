"""Transport-trace tests for v26 removed-source suppression."""

from __future__ import annotations

from typing import Any

import pytest
from conftest import make_config

import truenas_exporter as runtime
from truenas_exporter.compat_profiles import PROFILE_25_10, PROFILE_26_0, PROFILE_UNKNOWN

REMOVED_METHODS = {
    "virt.instance.query",
    "virt.volume.query",
    "nvmet.global.sessions",
    "reporting.graphs",
    "reporting.netdata_graphs",
}


class RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, Any]] = []

    def call(self, method: str, params: Any = None) -> Any:
        self.calls.append((method, params))
        if method == "core.get_methods":
            return {
                "app.image.query": {},
                "virt.instance.query": {},
                "virt.volume.query": {},
                "nvmet.global.sessions": {},
                "reporting.graphs": {},
                "reporting.netdata_graphs": {},
                "pool.is_upgraded": {},
                "pool.ddt_prefetch": {},
            }
        if (
            isinstance(params, list)
            and len(params) > 1
            and isinstance(params[1], dict)
            and params[1].get("count")
        ):
            return 0
        if method == "virt.instance.query":
            return [{"name": "incus-demo", "type": "CONTAINER", "status": "RUNNING"}]
        if method in {"reporting.graphs", "reporting.netdata_graphs"}:
            return [{"name": "cpu"}]
        return 0


@pytest.mark.parametrize("profile", [PROFILE_26_0, PROFILE_UNKNOWN])
def test_removed_methods_do_not_reach_collector_reporting_or_count_transports(
    profile: Any,
) -> None:
    exporter = runtime.TrueNASExporter(
        make_config(enable_generic_method_metrics=True),
        compatibility_profile=profile,
    )
    client = RecordingClient()

    exporter._collect_virt_metrics(client, {})
    exporter._collect_nvmet_metrics(client, {})
    exporter._collect_reporting_timeseries(client, {})

    for method in REMOVED_METHODS:
        with pytest.raises(RuntimeError, match="removed"):
            exporter._query_count(client, method)

    assert REMOVED_METHODS.isdisjoint(method for method, _params in client.calls)
    assert exporter._collector_errors["profile_removed_method_suppressed"] >= 8
    assert "profile_method_blocked" not in exporter._collector_errors


@pytest.mark.parametrize("profile", [PROFILE_26_0, PROFILE_UNKNOWN])
def test_removed_methods_cannot_bypass_via_extra_or_generic_discovery(profile: Any) -> None:
    exporter = runtime.TrueNASExporter(
        make_config(
            auto_discover_methods=True,
            scrape_all_metrics=True,
            enable_generic_method_metrics=True,
            extra_methods=[
                "app.image.query",
                "virt.instance.query",
                "virt.volume.query",
                "nvmet.global.sessions",
                "reporting.graphs",
                "reporting.netdata_graphs",
                "pool.is_upgraded",
                "pool.ddt_prefetch",
            ],
        ),
        compatibility_profile=profile,
    )
    client = RecordingClient()

    exporter._discover_all_methods(client)
    methods_to_call = exporter._discover_methods(client)
    for method in methods_to_call:
        exporter._safe_call_auto(client, method)

    assert REMOVED_METHODS.isdisjoint(methods_to_call)
    assert "pool.is_upgraded" not in methods_to_call
    assert "pool.ddt_prefetch" not in methods_to_call
    assert REMOVED_METHODS.isdisjoint(method for method, _params in client.calls)
    assert "core.get_methods" in [method for method, _params in client.calls]


@pytest.mark.parametrize("profile", [PROFILE_26_0, PROFILE_UNKNOWN])
def test_app_image_query_remains_eligible_for_reviewed_count_use(profile: Any) -> None:
    exporter = runtime.TrueNASExporter(make_config(), compatibility_profile=profile)
    client = RecordingClient()

    assert exporter._query_count(client, "app.image.query") == 0

    assert client.calls == [("app.image.query", [[], {"count": True}])]


def test_v25_still_transports_removed_in_v26_sources() -> None:
    exporter = runtime.TrueNASExporter(
        make_config(enable_generic_method_metrics=True),
        compatibility_profile=PROFILE_25_10,
    )
    client = RecordingClient()

    exporter._collect_virt_metrics(client, {})
    exporter._collect_nvmet_metrics(client, {})
    exporter._collect_reporting_timeseries(client, {})

    transported = [method for method, _params in client.calls]
    for method in REMOVED_METHODS:
        assert method in transported


@pytest.mark.parametrize("profile", [PROFILE_26_0, PROFILE_UNKNOWN])
def test_removed_virt_event_is_not_subscribed_under_suppressed_profiles(
    monkeypatch: pytest.MonkeyPatch,
    profile: Any,
) -> None:
    attempts: list[tuple[str, Any]] = []
    version = "26.0.0" if profile is PROFILE_26_0 else "27.0.0"

    class EventClient:
        def __enter__(self) -> EventClient:
            return self

        def __exit__(self, *_args: Any) -> None:
            return None

        def authenticate(self, _api_key: str, call: Any = None) -> None:
            if call is not None:
                call("auth.login_with_api_key", ["redacted-test-key"])

        def call(self, method: str, params: Any = None) -> Any:
            attempts.append((method, params))
            if method == "auth.login_with_api_key":
                return True
            if method == "system.version_short":
                return version
            if method == "core.subscribe" and params == ["app.stats"]:
                raise KeyboardInterrupt
            return True

    exporter = runtime.TrueNASExporter(
        make_config(
            event_subscriptions=["virt.instance.metrics", "app.stats"],
            event_read_timeout_seconds=1,
        ),
        compatibility_profile=profile,
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
    assert exporter._collector_errors["profile_removed_event_suppressed"] == 1


def test_v25_still_subscribes_virt_event(monkeypatch: pytest.MonkeyPatch) -> None:
    attempts: list[tuple[str, Any]] = []

    class EventClient:
        def __enter__(self) -> EventClient:
            return self

        def __exit__(self, *_args: Any) -> None:
            return None

        def authenticate(self, _api_key: str, call: Any = None) -> None:
            if call is not None:
                call("auth.login_with_api_key", ["redacted-test-key"])

        def call(self, method: str, params: Any = None) -> Any:
            attempts.append((method, params))
            if method == "auth.login_with_api_key":
                return True
            if method == "system.version_short":
                return "25.10.2"
            if method == "core.subscribe" and params == ["virt.instance.metrics"]:
                raise KeyboardInterrupt
            return True

    exporter = runtime.TrueNASExporter(
        make_config(
            event_subscriptions=["virt.instance.metrics"],
            event_read_timeout_seconds=1,
        ),
        compatibility_profile=PROFILE_25_10,
    )
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: EventClient())

    with pytest.raises(KeyboardInterrupt):
        exporter._event_stream_loop()

    assert attempts == [
        ("auth.login_with_api_key", ["redacted-test-key"]),
        ("system.version_short", []),
        ("core.subscribe", ["virt.instance.metrics"]),
    ]
