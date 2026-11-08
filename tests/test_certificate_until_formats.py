"""Live 27.0.0-RC.1 returns certificate ``until`` as ctime text, not ISO 8601."""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from truenas_exporter.collection import _cert_days_to_expiry, _parse_ts

EXPECTED = datetime(2026, 3, 8, 12, 0, 0, tzinfo=UTC).timestamp()


@pytest.mark.parametrize(
    "value",
    ["Sun Mar  8 12:00:00 2026", "Sun Mar 8 12:00:00 2026", "2026-03-08T12:00:00Z", "2026-03-08T12:00:00+00:00"],
)
def test_until_formats_parse_to_same_utc_timestamp(value):
    assert _parse_ts(value) == EXPECTED


@pytest.mark.parametrize("value", [None, "", "Never", "Mon Foo 99 xx 2026", "garbage", True])
def test_unparseable_until_stays_absent(value):
    assert _parse_ts(value) is None
    assert _cert_days_to_expiry(value) is None


def test_expired_ctime_certificate_is_negative_days():
    assert _cert_days_to_expiry("Thu Jan  1 00:00:00 2015") < 0
