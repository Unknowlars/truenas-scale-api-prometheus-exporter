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

    def __init__(self, message: str, *, code: int | None = None) -> None:
        super().__init__(message)
        self.code = code


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
            timeout=self._remaining_timeout("connect"),
            sslopt=sslopt,
        )
        return self

    def _remaining_timeout(self, operation: str) -> float:
        if self._deadline_monotonic is None:
            return float(self._timeout_seconds)
        remaining = self._deadline_monotonic - time.monotonic()
        if remaining <= 0:
            raise TimeoutError(f"{operation}: total scrape budget exhausted")
        return min(float(self._timeout_seconds), remaining)

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
        timeout = self._remaining_timeout(method)
        if hasattr(self._ws, "settimeout"):
            self._ws.settimeout(timeout)
        self._id += 1
        req_id = self._id
        self._ws.send(json.dumps({
            "jsonrpc": "2.0",
            "id": req_id,
            "method": method,
            "params": params if params is not None else [],
        }))

        for _ in range(MAX_STRAY_MESSAGES):
            timeout = self._remaining_timeout(method)
            if hasattr(self._ws, "settimeout"):
                self._ws.settimeout(timeout)
            raw = self._ws.recv()
            msg = json.loads(raw)
            if not isinstance(msg, dict):
                raise JsonRpcError(f"{method}: expected a JSON-RPC object")
            if msg.get("id") != req_id:
                LOG.debug(
                    "call(%s): discarding stray WS message id=%s (waiting for id=%s)",
                    method,
                    msg.get("id"),
                    req_id,
                )
                continue
            if "error" in msg:
                error = msg["error"]
                code = error.get("code") if isinstance(error, dict) else None
                # Never interpolate server error data: authentication and validation
                # errors can echo credentials, parameters, or private paths.
                suffix = " method does not exist" if code == -32601 else ""
                raise JsonRpcError(f"{method} failed (code={code}){suffix}", code=code if isinstance(code, int) else None)
            if "result" not in msg:
                raise JsonRpcError(f"{method}: missing JSON-RPC result")
            return msg.get("result")
        raise JsonRpcError(
            f"{method}: response not received after {MAX_STRAY_MESSAGES} stray messages"
        )

    def recv_json(self) -> dict[str, Any]:
        if self._ws is None:
            raise RuntimeError("WebSocket is not connected")
        result = json.loads(self._ws.recv())
        if not isinstance(result, dict):
            raise JsonRpcError("Expected a JSON-RPC notification object")
        return result

    def authenticate(
        self,
        api_key: str,
        call: Callable[[str, list[Any]], Any] | None = None,
        *,
        username: str | None = None,
    ) -> None:
        """Authenticate with a read-only API key, accepting v25 session objects."""
        request = self.call if call is None else call
        if username:
            result = request("auth.login_ex", [{
                "mechanism": "API_KEY_PLAIN",
                "username": username,
                "api_key": api_key,
                "login_options": {"user_info": False, "reconnect_token": False},
            }])
            if not isinstance(result, dict) or result.get("response_type") != "SUCCESS":
                raise JsonRpcError("auth.login_ex did not return SUCCESS")
            return
        result = request("auth.login_with_api_key", [api_key])
        if isinstance(result, dict) and "response_type" in result:
            if result.get("response_type") != "SUCCESS":
                raise JsonRpcError("auth.login_with_api_key did not return SUCCESS")
            return
        if isinstance(result, str):
            accepted = result.strip().lower() in {"1", "true", "yes", "on", "up", "running"}
        elif isinstance(result, (dict, list)):
            accepted = bool(result)
        else:
            accepted = bool(result)
        if not accepted:
            raise JsonRpcError("auth.login_with_api_key returned falsy")
