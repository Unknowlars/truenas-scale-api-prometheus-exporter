from datetime import UTC, datetime, timedelta

from truenas_exporter.collection import (
    _as_bool,
    _as_float,
    _cert_days_to_expiry,
    _extract_labeled_numeric_series,
    _first_not_none,
    _link_is_up,
    _normalize_core_label,
    _parse_ts,
    _str_label,
)


def test_scalar_coercion_edge_cases():
    assert _as_float(None) is None
    assert _as_float(True) == 1
    assert _as_float("bad") is None
    assert _as_float({"parsed": "2.5"}) == 2.5
    assert _as_float({"value": "bad"}) is None
    assert _first_not_none(None, False, 3) is False
    assert _first_not_none(None, None) is None
    assert _as_bool(1) and not _as_bool(0)
    assert _as_bool("running") and not _as_bool("stopped")
    assert _as_bool({"session": 1}) and not _as_bool([])
    assert not _as_bool(object())
    assert _link_is_up(" link_state_up ")
    assert not _link_is_up("LINK_STATE_DOWN")
    assert _link_is_up("up")
    assert _str_label(None) == "unknown"
    assert _str_label("  ", "fallback") == "fallback"
    assert _normalize_core_label("cpu12") == "12"
    assert _normalize_core_label("total") == "total"


def test_labeled_series_accepts_list_and_mapping_shapes():
    assert _extract_labeled_numeric_series(
        [{"core": "cpu0", "percent": 1}, {"percent": "bad"}, 3],
        value_keys=("percent",),
        normalize_label=True,
    ) == {("0",): 1.0, ("2",): 3.0}
    assert _extract_labeled_numeric_series(
        {"cpu1": {"usage": 4}, "cpu2": "5", "bad": None},
        value_keys=("usage",),
        normalize_label=True,
    ) == {("1",): 4.0, ("2",): 5.0}
    assert _extract_labeled_numeric_series("unsupported") == {}


def test_timestamp_and_certificate_edge_cases():
    assert _parse_ts(None) is None
    assert _parse_ts(10) == 10
    assert _parse_ts({"$date": 2500}) == 2.5
    assert _parse_ts({"$date": "bad"}) is None
    assert _parse_ts("Never") is None
    assert _parse_ts("2026-01-01T00:00:00Z") is not None
    assert _parse_ts("2026-01-01T00:00:00") is not None
    assert _parse_ts("not-a-date") is None
    assert _cert_days_to_expiry(None) is None
    future = datetime.now(tz=UTC) + timedelta(days=10)
    assert 8 <= _cert_days_to_expiry(future.isoformat()) <= 10
