#!/usr/bin/env python3
"""Compatibility launcher for source checkouts.

The implementation lives in ``src/truenas_exporter``. Importing this module
aliases the packaged runtime so existing tests and integrations that monkeypatch
module globals continue to behave as before.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path


_PACKAGE_PATH = Path(__file__).resolve().parent / "src" / "truenas_exporter"

if __name__ == "__main__":
    sys.path.insert(0, str(_PACKAGE_PATH.parent))
    from truenas_exporter.cli import main

    main()
else:
    __path__ = [str(_PACKAGE_PATH)]
    _runtime = importlib.import_module("truenas_exporter.runtime")
    _runtime.__path__ = [str(_PACKAGE_PATH)]
    sys.modules[__name__] = _runtime
