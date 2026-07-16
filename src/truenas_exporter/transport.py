"""Bounded JSON-RPC 2.0 transport over WebSocket."""

from __future__ import annotations

import json
import logging
import ssl
import time
from collections.abc import Callable
from typing import Any

from websocket import WebSocket, create_connection

LOG = logging.getLogger("truenas_exporter")
MAX_STRAY_MESSAGES = 100


class JsonRpcError(RuntimeError):
    """Raised when TrueNAS JSON-RPC responds with an error object."""


class JsonRpcWsClient:
    def __init__(
        self,
        ws_url: str,
        timeout_seconds: int,
        verify_tls: bool,
        ca_file: str | None = None,
        deadline_monotonic: float | None = None,
    ) -> None:
        self._ws_url = ws_url
        self._timeout_seconds = timeout_seconds
        self._verify_tls = verify_tls
        self._ca_file = ca_file
        self._deadline_monotonic = deadline_monotonic
        self._id = 0
        self._ws: WebSocket | None = None

    def __enter__(self) -> JsonRpcWsClient:
        sslopt: dict[str, Any] | None = None
        if self._ws_url.startswith("wss://"):
            if self._verify_tls:
                sslopt = {"cert_reqs": ssl.CERT_REQUIRED}
                if self._ca_file:
                    sslopt["ca_certs"] = self._ca_file
            else:
                sslopt = {
                    "cert_reqs": ssl.CERT_NONE,
                    "check_hostname": False,
                }
        self._ws = create_connection(
            self._ws_url,
            timeout=self._timeout_seconds,
            sslopt=sslopt,
        )
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        if self._ws is not None:
            try:
                self._ws.close()
            except Exception:
                LOG.debug("Failed to close websocket cleanly", exc_info=True)
        self._ws = None

    def call(self, method: str, params: list[Any] | None = None) -> Any:
        if self._ws is None:
            raise RuntimeError("WebSocket is not connected")
        self._id += 1
        req_id = self._id
        self._ws.send(json.dumps({
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params if params is not None else [],
        }))

        for _ in range(MAX_STRAY_MESSAGES):
            if self._deadline_monotonic is not None:
                remaining = self._deadline_monotonic - time.monotonic()
                if remaining <= 0:
                    raise TimeoutError(f"{method}: total scrape budget exhausted")
                if hasattr(self._ws, "settimeout"):
                    self._ws.settimeout(min(float(self._timeout_seconds), remaining))
            raw = self._ws.recv()
            msg = json.loads(raw)
            if msg.get("id") != req_id:
                LOG.debug(
                    "call(%s): discarding stray WS message id=%s (waiting for id=%s)",
                    method,
                    msg.get("id"),
                    req_id,
                )
                continue
            if "error" in msg:
                raise JsonRpcError(f"{method} failed: {msg['error']}")
            return msg.get("result")
        raise JsonRpcError(
            f"{method}: response not received after {MAX_STRAY_MESSAGES} stray messages"
        )

    def recv_json(self) -> dict[str, Any]:
        if self._ws is None:
            raise RuntimeError("WebSocket is not connected")
        return json.loads(self._ws.recv())

    def authenticate(
        self,
        api_key: str,
        call: Callable[[str, list[Any]], Any] | None = None,
    ) -> None:
        """Authenticate with a read-only API key, accepting v25 session objects."""
        request = self.call if call is None else call
        result = request("auth.login_with_api_key", [api_key])
        if isinstance(result, str):
            accepted = result.strip().lower() in {"1", "true", "yes", "on", "up", "running"}
        elif isinstance(result, (dict, list)):
            accepted = bool(result)
        else:
            accepted = bool(result)
        if not accepted:
            raise JsonRpcError("auth.login_with_api_key returned falsy")
