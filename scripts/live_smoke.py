#!/usr/bin/env python3
"""Optional, explicitly read-only smoke test against a live TrueNAS system."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from truenas_exporter.config import load_config  # noqa: E402
from truenas_exporter.transport import JsonRpcWsClient  # noqa: E402

READ_ONLY_METHODS = (
    "system.state",
    "system.info",
    "system.version_short",
    "pool.query",
    "service.query",
)


def summarize(method: str, value: object) -> dict[str, object]:
    if isinstance(value, list):
        return {"method": method, "result_type": "list", "item_count": len(value)}
    if isinstance(value, dict):
        allowed_keys = {"hostname", "version", "product_type", "state"}
        return {
            "method": method,
            "result_type": "object",
            "keys": sorted(key for key in value if key in allowed_keys),
        }
    return {"method": method, "result_type": type(value).__name__}


def main() -> None:
    config = load_config()
    print("Read-only methods:")
    for method in READ_ONLY_METHODS:
        print(f"  - {method}")

    with JsonRpcWsClient(
        config.ws_url,
        config.timeout_seconds,
        config.verify_tls,
        ca_file=config.ca_file,
    ) as client:
        client.authenticate(config.api_key)
        for method in READ_ONLY_METHODS:
            params = [[], {"limit": 5}] if method.endswith(".query") else []
            print(json.dumps(summarize(method, client.call(method, params)), sort_keys=True))


if __name__ == "__main__":
    main()
