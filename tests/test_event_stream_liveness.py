import sys

from conftest import make_config
from websocket import WebSocketTimeoutException

import truenas_exporter as exporter_module

runtime = sys.modules[exporter_module.TrueNASExporter.__module__]


class _LivenessClient:
    """Fake JsonRpcWsClient whose recv_json() raises WebSocketTimeoutException or
    returns queued messages, advancing a shared monotonic clock on every attempt."""

    def __init__(self, now, tick_seconds, outcomes, subscribe_result="sub-1"):
        self._now = now
        self._tick_seconds = tick_seconds
        self._outcomes = iter(outcomes)
        self.subscribe_result = subscribe_result
        self.calls = []
        self.recv_count = 0

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return None

    def authenticate(self, _key, call=None):
        if call is not None:
            call("auth.login_with_api_key", ["redacted-test-key"])

    def call(self, method, params=None):
        self.calls.append((method, params))
        if method == "system.version_short":
            return "25.10.2"
        if method == "core.subscribe":
            return self.subscribe_result
        return True

    def recv_json(self):
        self.recv_count += 1
        self._now["value"] += self._tick_seconds
        outcome = next(self._outcomes, WebSocketTimeoutException())
        if isinstance(outcome, Exception):
            raise outcome
        return outcome


def test_dead_connection_detected_after_read_timeout(monkeypatch):
    now = {"value": 0.0}
    monkeypatch.setattr(runtime.time, "monotonic", lambda: now["value"])
    exporter = exporter_module.TrueNASExporter(
        make_config(
            enable_event_streams=True,
            event_subscriptions=["reporting.realtime"],
            event_read_timeout_seconds=60,
            event_stale_after_seconds=30,
        )
    )
    # Repeated timeouts, spaced 25s apart: idle time crosses the 60s deadline on
    # the 3rd read attempt (75s of silence) without any real sleep().
    client = _LivenessClient(now, tick_seconds=25, outcomes=[])
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)

    exporter._event_stream_loop()

    assert client.recv_count == 3
    assert exporter._collector_event_stream_up["reporting.realtime"] == 0.0


def test_message_arrival_resets_idle_deadline(monkeypatch):
    now = {"value": 0.0}
    monkeypatch.setattr(runtime.time, "monotonic", lambda: now["value"])
    exporter = exporter_module.TrueNASExporter(
        make_config(
            enable_event_streams=True,
            event_subscriptions=["reporting.realtime"],
            event_read_timeout_seconds=60,
            event_stale_after_seconds=30,
        )
    )
    message = {
        "method": "collection_update",
        "params": {"collection": "reporting.realtime", "fields": {"cpu": {"percent": 1}}},
    }
    outcomes = [
        WebSocketTimeoutException(),
        WebSocketTimeoutException(),
        message,  # arrives at t=75s; must reset the idle deadline
        WebSocketTimeoutException(),
        WebSocketTimeoutException(),
        WebSocketTimeoutException(),  # only trips the deadline if the reset worked
    ]
    client = _LivenessClient(now, tick_seconds=25, outcomes=outcomes)
    monkeypatch.setattr(runtime, "JsonRpcWsClient", lambda **_kwargs: client)
    monkeypatch.setattr(exporter._stop_event, "wait", lambda _seconds: True)

    exporter._event_stream_loop()

    # If the deadline were not reset by the message, the 4th read (t=100s, 100s
    # since connection start) would already exceed the 60s deadline.
    assert client.recv_count == 6
    assert exporter._event_message_counts["reporting.realtime"] == 1
    assert exporter._collector_event_stream_up["reporting.realtime"] == 0.0
