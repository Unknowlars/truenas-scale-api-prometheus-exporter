from __future__ import annotations

from typing import Any

from conftest import make_config

import truenas_exporter as runtime


class RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, Any]] = []

    def __enter__(self) -> RecordingClient:
        return self

    def __exit__(self, *_args: Any) -> None:
        return None

    def authenticate(self, _api_key: str, call: Any = None) -> None:
        if call is not None:
            call("auth.login_with_api_key", ["redacted-test-key"])

    def call(self, method: str, params: Any = None) -> Any:
        self.calls.append((method, params))
        if method == "auth.login_with_api_key":
            return True
        if method == "system.version_short":
            return "25.10.2"
        if method == "system.state":
            return "READY"
        if method == "system.info":
            return {
                "hostname": "synthetic-nas",
                "version": "TrueNAS-SCALE-25.10.2",
                "system_product": "SCALE",
            }
        if method.endswith(".config"):
            return {}
        if (
            isinstance(params, list)
            and len(params) > 1
            and isinstance(params[1], dict)
            and params[1].get("count") is True
        ):
            return 0
        return []


def test_default_scrape_deduplicates_disk_service_and_vm_list(
    monkeypatch,
) -> None:
    client = RecordingClient()
    exporter = runtime.TrueNASExporter(make_config())
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)

    exporter.scrape_once()

    calls_by_method: dict[str, list[Any]] = {}
    for method, params in client.calls:
        calls_by_method.setdefault(method, []).append(params)

    assert len(calls_by_method["disk.query"]) == 1
    assert calls_by_method["disk.query"][0] == [
        [],
        {
            "extra": {"pools": True},
            "select": [
                "name",
                "identifier",
                "size",
                "pool",
                "type",
                "rotationrate",
                "model",
                "bus",
            ],
        },
    ]
    assert len(calls_by_method["service.query"]) == 1
    assert calls_by_method["service.query"][0] == [
        [],
        {"extra": {"include_state": True}, "select": ["service", "enable", "state"]},
    ]
    assert calls_by_method["vm.query"] == [[[], {"count": True}]]


def test_count_or_len_skips_count_when_list_is_shorter_than_limit() -> None:
    exporter = runtime.TrueNASExporter(make_config())
    client = RecordingClient()

    total = exporter._count_or_len(client, "cronjob.query", [{"id": 1}], 2)

    assert total == 1
    assert client.calls == []


def test_count_or_len_counts_when_list_reaches_limit() -> None:
    exporter = runtime.TrueNASExporter(make_config())
    client = RecordingClient()

    total = exporter._count_or_len(client, "cronjob.query", [{"id": 1}], 1)

    assert total == 0
    assert client.calls == [("cronjob.query", [[], {"count": True}])]


def test_cronjob_metric_output_with_short_list(monkeypatch) -> None:
    exporter = runtime.TrueNASExporter(make_config(exporter_mode="legacy"))
    calls: list[tuple[str, Any]] = []

    def fake_call(_client: Any, method: str, params: Any = None) -> Any:
        calls.append((method, params))
        if method == "cronjob.query":
            return [{"id": 7, "enabled": True, "command": "not exported"}]
        raise AssertionError(f"Unexpected call: {method}")

    runtime.CRONJOB_COUNT.set(0)
    runtime.CRONJOB_ENABLED.clear()
    monkeypatch.setattr(exporter, "_call", fake_call)

    exporter._collect_cronjob_metrics(object(), {})

    assert runtime.CRONJOB_COUNT._value.get() == 1
    samples = list(runtime.CRONJOB_ENABLED.collect())[0].samples
    assert [
        (sample.name, sample.labels, sample.value)
        for sample in samples
        if sample.name == "truenas_cronjob_enabled"
    ] == [("truenas_cronjob_enabled", {"name": "7"}, 1.0)]
    assert calls == [
        ("cronjob.query", [[], {"limit": 200, "select": ["id", "enabled"]}])
    ]
