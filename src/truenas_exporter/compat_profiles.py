"""TrueNAS API compatibility profiles and pre-call safety data."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType
from typing import Literal

from .api_catalog import (
    DEFAULT_SAFE_EVENT_SUBSCRIPTIONS,
    DOCUMENTED_EVENT_NAMES,
    READ_ONLY_METHOD_ALLOWLIST,
    TELEMETRY_CANDIDATE_METHOD_ALLOWLIST,
)

ProfileName = Literal["25.10", "26.0", "unknown"]

V26_REMOVED_METHODS: frozenset[str] = frozenset(
    {
        "nvmet.global.sessions",
        "reporting.graphs",
        "reporting.netdata_graphs",
        "virt.global.config",
        "virt.global.get_network",
        "virt.instance.query",
        "virt.volume.query",
    }
)
V26_REMOVED_EVENTS: frozenset[str] = frozenset({"virt.instance.metrics"})

PROFILE_PROHIBITED_METHODS: frozenset[str] = frozenset(
    {
        "pool.ddt_prefetch",
        "pool.is_upgraded",
    }
)

TRANSPORT_METHOD_ALLOWLIST: frozenset[str] = frozenset(
    {
        "auth.login_with_api_key",
        "core.subscribe",
        "core.unsubscribe",
        "system.version_short",
    }
)

QUERY_LIMIT_METHODS: frozenset[str] = frozenset(
    method
    for method in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST
    if method.endswith(".query") or method in {"core.get_jobs", "iscsi.global.sessions", "route.system_routes"}
)


@dataclass(frozen=True)
class UnitConversion:
    source_unit: str
    metric_unit: str
    multiplier: float = 1.0


@dataclass(frozen=True)
class CompatibilityProfile:
    name: ProfileName
    target_version: str
    reviewed_methods: frozenset[str]
    telemetry_methods: frozenset[str]
    reviewed_events: frozenset[str]
    default_event_subscriptions: tuple[str, ...]
    removed_methods: frozenset[str]
    removed_events: frozenset[str]
    query_limit_methods: frozenset[str]
    unit_conversions: MappingProxyType[str, UnitConversion]

    def allows_method(self, method: str) -> bool:
        return method in self.reviewed_methods or method in TRANSPORT_METHOD_ALLOWLIST

    def allows_telemetry_method(self, method: str) -> bool:
        return method in self.telemetry_methods

    def allows_event(self, event: str) -> bool:
        return event in self.reviewed_events

    def query_limit_for(self, method: str, configured_limit: int) -> int:
        if method not in self.query_limit_methods:
            return configured_limit
        return max(1, configured_limit)


_V25_METHODS = READ_ONLY_METHOD_ALLOWLIST - PROFILE_PROHIBITED_METHODS
_V25_TELEMETRY_METHODS = TELEMETRY_CANDIDATE_METHOD_ALLOWLIST - PROFILE_PROHIBITED_METHODS
_V26_METHODS = _V25_METHODS - V26_REMOVED_METHODS
_V26_TELEMETRY_METHODS = _V25_TELEMETRY_METHODS - V26_REMOVED_METHODS
_V25_EVENTS = frozenset(DEFAULT_SAFE_EVENT_SUBSCRIPTIONS)
_V26_EVENTS = _V25_EVENTS - V26_REMOVED_EVENTS

_V25_UNIT_CONVERSIONS = MappingProxyType(
    {
        "vm.get_available_memory": UnitConversion("MiB", "bytes", 1024.0 * 1024.0),
        "vm.get_vmemory_in_use": UnitConversion("MiB", "bytes", 1024.0 * 1024.0),
    }
)
_V26_UNIT_CONVERSIONS = MappingProxyType(
    {
        "vm.get_available_memory": UnitConversion("bytes", "bytes"),
        "vm.get_vmemory_in_use": UnitConversion("bytes", "bytes"),
    }
)

PROFILE_25_10 = CompatibilityProfile(
    name="25.10",
    target_version="25.10.2",
    reviewed_methods=_V25_METHODS,
    telemetry_methods=_V25_TELEMETRY_METHODS,
    reviewed_events=_V25_EVENTS,
    default_event_subscriptions=DEFAULT_SAFE_EVENT_SUBSCRIPTIONS,
    removed_methods=frozenset(),
    removed_events=frozenset(),
    query_limit_methods=QUERY_LIMIT_METHODS,
    unit_conversions=_V25_UNIT_CONVERSIONS,
)
PROFILE_26_0 = CompatibilityProfile(
    name="26.0",
    target_version="26.0.0",
    reviewed_methods=_V26_METHODS,
    telemetry_methods=_V26_TELEMETRY_METHODS,
    reviewed_events=_V26_EVENTS,
    default_event_subscriptions=tuple(event for event in DEFAULT_SAFE_EVENT_SUBSCRIPTIONS if event in _V26_EVENTS),
    removed_methods=V26_REMOVED_METHODS,
    removed_events=V26_REMOVED_EVENTS,
    query_limit_methods=QUERY_LIMIT_METHODS - V26_REMOVED_METHODS,
    unit_conversions=_V26_UNIT_CONVERSIONS,
)
PROFILE_UNKNOWN = CompatibilityProfile(
    name="unknown",
    target_version="common-intersection",
    reviewed_methods=_V26_METHODS,
    telemetry_methods=_V26_TELEMETRY_METHODS,
    reviewed_events=_V26_EVENTS,
    default_event_subscriptions=PROFILE_26_0.default_event_subscriptions,
    removed_methods=V26_REMOVED_METHODS,
    removed_events=V26_REMOVED_EVENTS,
    query_limit_methods=QUERY_LIMIT_METHODS - V26_REMOVED_METHODS,
    unit_conversions=_V26_UNIT_CONVERSIONS,
)

PROFILES: MappingProxyType[ProfileName, CompatibilityProfile] = MappingProxyType(
    {
        "25.10": PROFILE_25_10,
        "26.0": PROFILE_26_0,
        "unknown": PROFILE_UNKNOWN,
    }
)


def get_profile(name: ProfileName | str) -> CompatibilityProfile:
    """Return a compatibility profile, falling back to the common intersection."""

    return PROFILES.get(name, PROFILE_UNKNOWN)  # type: ignore[arg-type]


assert _V25_EVENTS <= DOCUMENTED_EVENT_NAMES
assert _V26_EVENTS <= DOCUMENTED_EVENT_NAMES
