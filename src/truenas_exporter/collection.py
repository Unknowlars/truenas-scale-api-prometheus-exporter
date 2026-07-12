"""Pure fixture-friendly domain value parsers."""

import re
from datetime import UTC, datetime
from typing import Any


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
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
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on", "running", "up"}
    # A non-empty dict or list is truthy — handles session objects returned by
    # auth.login_with_api_key in TrueNAS 25.x
    if isinstance(value, (dict, list)):
        return bool(value)
    return False


def _link_is_up(value: Any) -> bool:
    if isinstance(value, str):
        normalized = value.strip().upper()
        if normalized == "LINK_STATE_UP":
            return True
        if normalized == "LINK_STATE_DOWN":
            return False
    return _as_bool(value)


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
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, dict):
        # {"$date": milliseconds_since_epoch}
        ms = value.get("$date")
        if ms is not None:
            try:
                return float(ms) / 1000.0
            except (TypeError, ValueError):
                pass
    if isinstance(value, str):
        if value in {"Never", "N/A", "None", ""}:
            return None
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
