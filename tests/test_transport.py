import json
import ssl

import pytest

from truenas_exporter import transport


class FakeWebSocket:
    def __init__(self, responses):
        self.responses = list(responses)
        self.sent = []
        self.timeouts = []
        self.closed = False

    def send(self, payload):
        self.sent.append(json.loads(payload))

    def recv(self):
        return self.responses.pop(0)

    def settimeout(self, value):
        self.timeouts.append(value)

    def close(self):
        self.closed = True


def test_transport_skips_stray_messages_and_returns_matching_response(monkeypatch):
    socket = FakeWebSocket([
        json.dumps({"jsonrpc": "2.0", "id": 99, "result": "stray"}),
        json.dumps({"jsonrpc": "2.0", "id": 1, "result": {"state": "READY"}}),
    ])
    captured = {}

    def fake_create_connection(url, **kwargs):
        captured.update(url=url, **kwargs)
        return socket

    monkeypatch.setattr(transport, "create_connection", fake_create_connection)
    client = transport.JsonRpcWsClient(
        "wss://nas.example/api/current",
        timeout_seconds=20,
        verify_tls=True,
        ca_file="/tmp/test-ca.pem",
        deadline_monotonic=100.0,
    )
    monkeypatch.setattr(transport.time, "monotonic", lambda: 90.0)

    with client:
        result = client.call("system.state")

    assert result == {"state": "READY"}
    assert socket.sent == [{"jsonrpc": "2.0", "id": 1, "method": "system.state", "params": []}]
    assert socket.timeouts == [10.0, 10.0]
    assert socket.closed is True
    assert captured["sslopt"] == {"cert_reqs": ssl.CERT_REQUIRED, "ca_certs": "/tmp/test-ca.pem"}


def test_transport_raises_jsonrpc_error(monkeypatch):
    socket = FakeWebSocket([
        json.dumps({"jsonrpc": "2.0", "id": 1, "error": {"message": "denied"}}),
    ])
    monkeypatch.setattr(transport, "create_connection", lambda *_args, **_kwargs: socket)

    with (
        transport.JsonRpcWsClient("ws://nas.example/api/current", 5, True) as client,
        pytest.raises(transport.JsonRpcError, match="system.info failed"),
    ):
        client.call("system.info")


def test_transport_tls_verification_can_be_explicitly_disabled(monkeypatch):
    socket = FakeWebSocket([])
    captured = {}

    def fake_create_connection(_url, **kwargs):
        captured.update(kwargs)
        return socket

    monkeypatch.setattr(transport, "create_connection", fake_create_connection)

    with transport.JsonRpcWsClient("wss://nas.example/api/current", 5, False):
        pass

    assert captured["sslopt"] == {
        "cert_reqs": ssl.CERT_NONE,
        "check_hostname": False,
    }


def test_transport_recv_json_and_disconnected_errors():
    socket = FakeWebSocket([json.dumps({"method": "collection_update"})])
    client = transport.JsonRpcWsClient("ws://nas.example/api/current", 5, True)

    with pytest.raises(RuntimeError, match="not connected"):
        client.call("system.info")
    with pytest.raises(RuntimeError, match="not connected"):
        client.recv_json()

    client._ws = socket
    assert client.recv_json() == {"method": "collection_update"}


def test_transport_tolerates_close_failure():
    class CloseFailureSocket(FakeWebSocket):
        def close(self):
            raise OSError("close failed")

    client = transport.JsonRpcWsClient("ws://nas.example/api/current", 5, True)
    client._ws = CloseFailureSocket([])

    client.__exit__(None, None, None)

    assert client._ws is None


def test_transport_bounds_stray_messages(monkeypatch):
    responses = [
        json.dumps({"jsonrpc": "2.0", "id": 99, "result": "stray"})
        for _ in range(transport.MAX_STRAY_MESSAGES)
    ]
    socket = FakeWebSocket(responses)
    monkeypatch.setattr(transport, "create_connection", lambda *_args, **_kwargs: socket)

    with (
        transport.JsonRpcWsClient("ws://nas.example/api/current", 5, True) as client,
        pytest.raises(transport.JsonRpcError, match="response not received"),
    ):
        client.call("system.info")


def test_transport_authenticate_accepts_session_and_rejects_falsy():
    client = transport.JsonRpcWsClient("ws://nas.example/api/current", 5, True)
    calls = []
    client.authenticate("secret", call=lambda method, params: calls.append((method, params)) or {"id": "session"})
    assert calls == [("auth.login_with_api_key", ["secret"])]
    with pytest.raises(transport.JsonRpcError, match="returned falsy"):
        client.authenticate("secret", call=lambda _method, _params: False)
