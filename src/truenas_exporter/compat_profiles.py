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
        "reporting.graphs",
        "reporting.netdata_graphs",
        "virt.global.config",
        "virt.global.get_network",
        "virt.instance.query",
        "virt.volume.query",
    }
)
# nvmet.global.sessions is absent from the pinned v26 doc corpus but is still
# served by live 26.0.0-BETA.2 (returns []), so it is intentionally NOT treated
# as removed — the exporter keeps populating truenas_nvmet_session_count on v26.
V26_REMOVED_EVENTS: frozenset[str] = frozenset({"virt.instance.metrics"})

# v26 replaced the virt.* Incus/LXD API with container.*/lxc.* and adds small
# read-only surfaces such as webshare/smb status and zpool status detail. These
# methods and the container.metrics event do not exist on 25.10, so they are
# added to the 26.0 profile only (never the 25.10 profile).
V26_ADDED_METHODS: frozenset[str] = frozenset(
    {
        "container.query",
        "sharing.webshare.query",
        "smb.status",
        "webshare.config",
        "zpool.query",
    }
)
V26_ADDED_EVENTS: frozenset[str] = frozenset({"container.metrics"})

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
_V26_METHODS = (_V25_METHODS - V26_REMOVED_METHODS) | V26_ADDED_METHODS
_V26_TELEMETRY_METHODS = _V25_TELEMETRY_METHODS - V26_REMOVED_METHODS
# DEFAULT_SAFE_EVENT_SUBSCRIPTIONS carries both virt.instance.metrics (v25) and
# container.metrics (v26); each profile keeps only the name its version exposes.
_V25_EVENTS = frozenset(DEFAULT_SAFE_EVENT_SUBSCRIPTIONS) - V26_ADDED_EVENTS
_V26_EVENTS = frozenset(DEFAULT_SAFE_EVENT_SUBSCRIPTIONS) - V26_REMOVED_EVENTS
_UNKNOWN_METHODS = _V25_METHODS & _V26_METHODS
_UNKNOWN_TELEMETRY_METHODS = _V25_TELEMETRY_METHODS & _V26_TELEMETRY_METHODS
_UNKNOWN_EVENTS = _V25_EVENTS & _V26_EVENTS

# The pinned 25.10.2 documentation says these VM memory methods return
# "megabytes", but a live TrueNAS SCALE 25.10.3 system returns raw *bytes*
# (observed 17,390,127,315 = 16.2 GiB on a 31.3 GiB host, 2026-07-13). The
# documentation contradicts reality; a MiB multiplier inflated
# ``truenas_vm_available_memory_bytes`` by 1024**2. Treat 25.10 as bytes to
# match the live API and the 26.0 profile.
_V25_UNIT_CONVERSIONS = MappingProxyType(
    {
        "vm.get_available_memory": UnitConversion("bytes", "bytes"),
        "vm.get_vmemory_in_use": UnitConversion("bytes", "bytes"),
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
    default_event_subscriptions=tuple(
        event for event in DEFAULT_SAFE_EVENT_SUBSCRIPTIONS if event in _V25_EVENTS
    ),
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
    reviewed_methods=_UNKNOWN_METHODS,
    telemetry_methods=_UNKNOWN_TELEMETRY_METHODS,
    reviewed_events=_UNKNOWN_EVENTS,
    default_event_subscriptions=tuple(
        event for event in DEFAULT_SAFE_EVENT_SUBSCRIPTIONS if event in _UNKNOWN_EVENTS
    ),
    removed_methods=V26_REMOVED_METHODS,
    removed_events=V26_REMOVED_EVENTS,
    query_limit_methods=QUERY_LIMIT_METHODS & _UNKNOWN_METHODS,
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
assert _UNKNOWN_EVENTS <= DOCUMENTED_EVENT_NAMES
