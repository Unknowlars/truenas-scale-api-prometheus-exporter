"""Pure fixture-friendly domain value parsers."""

import math
import re
from datetime import UTC, datetime
from typing import Any


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        numeric = float(value)
        return numeric if math.isfinite(numeric) else None
    if isinstance(value, str):
        try:
            numeric = float(value)
            return numeric if math.isfinite(numeric) else None
        except ValueError:
            return None
    if isinstance(value, dict):
        for key in ("value", "parsed", "rawvalue"):
            nested = _as_float(value.get(key))
            if nested is not None:
                return nested
    return None


def _first_not_none(*values: Any) -> Any:
    """Return the first present value without discarding valid zero/false values."""
    for value in values:
        if value is not None:
            return value
    return None


def _as_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        numeric = float(value)
        return math.isfinite(numeric) and numeric != 0
    if isinstance(value, str):
        return value.strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
            "running",
            "up",
            "active",
            "enabled",
            "online",
            "healthy",
            "success",
            "present",
            "detected",
        }
    # A non-empty dict or list is truthy — handles session objects returned by
    # auth.login_with_api_key in TrueNAS 25.x
    if isinstance(value, (dict, list)):
        return bool(value)
    return False


def _as_optional_bool(value: Any) -> bool | None:
    """Parse a documented boolean while distinguishing missing/malformed data."""
    if value is None:
        return None
    if isinstance(value, dict):
        for key in ("value", "parsed", "rawvalue"):
            nested = _as_optional_bool(value.get(key))
            if nested is not None:
                return nested
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        numeric = float(value)
        if not math.isfinite(numeric) or numeric not in {0.0, 1.0}:
            return None
        return numeric == 1.0
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {
            "1",
            "true",
            "yes",
            "on",
            "running",
            "up",
            "active",
            "enabled",
            "online",
            "healthy",
            "success",
            "present",
            "detected",
        }:
            return True
        if normalized in {
            "0",
            "false",
            "no",
            "off",
            "stopped",
            "down",
            "inactive",
            "disabled",
            "offline",
            "unhealthy",
            "failed",
            "absent",
            "not detected",
        }:
            return False
    return None


def _as_percent(value: Any) -> float | None:
    """Parse a documented percentage number or a string such as ``"12%"``."""
    if isinstance(value, str):
        value = value.strip()
        if value.endswith("%"):
            value = value[:-1].strip()
    numeric = _as_float(value)
    if numeric is None or not 0 <= numeric <= 100:
        return None
    return numeric


def _as_ratio(value: Any) -> float | None:
    """Parse a decimal ratio, including ZFS strings such as ``"2.50x"``."""
    if isinstance(value, dict):
        for key in ("value", "parsed", "rawvalue"):
            nested = _as_ratio(value.get(key))
            if nested is not None:
                return nested
    if isinstance(value, str):
        value = value.strip()
        if value.lower().endswith("x"):
            value = value[:-1].strip()
    numeric = _as_float(value)
    if numeric is None or numeric < 0:
        return None
    return numeric


def _as_size_bytes(value: Any) -> float | None:
    """Parse byte counts and the unit-bearing strings returned by IPMI tools."""
    numeric = _as_float(value)
    if numeric is not None:
        return numeric if numeric >= 0 else None
    if not isinstance(value, str):
        return None

    match = re.fullmatch(
        r"\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*([kmgtpe]?i?b|bytes?)?\s*",
        value,
        flags=re.IGNORECASE,
    )
    if match is None:
        return None
    number = float(match.group(1))
    if number < 0 or not math.isfinite(number):
        return None
    unit = (match.group(2) or "b").lower()
    powers = {
        "b": 0,
        "byte": 0,
        "bytes": 0,
        "kb": 1,
        "kib": 1,
        "mb": 2,
        "mib": 2,
        "gb": 3,
        "gib": 3,
        "tb": 4,
        "tib": 4,
        "pb": 5,
        "pib": 5,
        "eb": 6,
        "eib": 6,
    }
    power = powers.get(unit)
    if power is None:
        return None
    return number * (1024**power)


def _link_is_up(value: Any) -> bool | None:
    if isinstance(value, str):
        normalized = value.strip().upper()
        if normalized == "LINK_STATE_UP":
            return True
        if normalized == "LINK_STATE_DOWN":
            return False
    return _as_optional_bool(value)


def _str_label(value: Any, fallback: str = "unknown") -> str:
    if value is None:
        return fallback
    text = str(value).strip()
    return text or fallback


def _normalize_core_label(value: Any) -> str:
    text = _str_label(value)
    match = re.search(r"(\d+)$", text)
    return match.group(1) if match else text


def _extract_labeled_numeric_series(
    payload: Any,
    *,
    label_keys: tuple[str, ...] = ("core", "cpu", "id", "name"),
    value_keys: tuple[str, ...] = ("value",),
    normalize_label: bool = False,
) -> dict[tuple[str, ...], float]:
    series: dict[tuple[str, ...], float] = {}

    if isinstance(payload, list):
        for idx, item in enumerate(payload):
            if isinstance(item, dict):
                label = None
                for label_key in label_keys:
                    candidate = item.get(label_key)
                    if candidate is not None:
                        label = candidate
                        break
                if label is None:
                    label = idx

                value = None
                for value_key in value_keys:
                    value = _as_float(item.get(value_key))
                    if value is not None:
                        break
            else:
                label = idx
                value = _as_float(item)

            if value is None:
                continue

            label_text = _normalize_core_label(label) if normalize_label else _str_label(label)
            series[(label_text,)] = value
        return series

    if isinstance(payload, dict):
        for raw_label, raw_value in payload.items():
            value = None
            if isinstance(raw_value, dict):
                for value_key in value_keys:
                    value = _as_float(raw_value.get(value_key))
                    if value is not None:
                        break
            if value is None:
                value = _as_float(raw_value)
            if value is None:
                continue

            label_text = _normalize_core_label(raw_label) if normalize_label else _str_label(raw_label)
            series[(label_text,)] = value

    return series


def _parse_ts(value: Any) -> float | None:
    """Convert various TrueNAS datetime representations to a Unix timestamp."""
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        numeric = float(value)
        return numeric if math.isfinite(numeric) else None
    if isinstance(value, dict):
        # {"$date": milliseconds_since_epoch}
        ms = value.get("$date")
        if ms is not None:
            if isinstance(ms, bool):
                return None
            try:
                numeric = float(ms)
                return numeric / 1000.0 if math.isfinite(numeric) else None
            except (TypeError, ValueError):
                pass
        for key in ("parsed", "value", "rawvalue", "time", "timestamp", "datetime"):
            nested = _parse_ts(value.get(key))
            if nested is not None:
                return nested
    if isinstance(value, str):
        if value in {"Never", "N/A", "None", ""}:
            return None
        try:
            numeric = float(value)
            return numeric if math.isfinite(numeric) else None
        except ValueError:
            pass
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=UTC)
            return dt.timestamp()
        except ValueError:
            pass
    return None


def _cert_days_to_expiry(until: Any) -> int | None:
    """Return days until certificate expiry; negative means already expired."""
    ts = _parse_ts(until)
    if ts is None:
        return None
    try:
        expiry_dt = datetime.fromtimestamp(ts, tz=UTC)
        delta = expiry_dt - datetime.now(tz=UTC)
        return delta.days
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Method safety filters
# ---------------------------------------------------------------------------
