"""Regression tests for documentation-derived API method and event safety."""

from truenas_exporter.api_catalog import (
    API_DOCS_TARGET_VERSION,
    DOCUMENTED_EVENT_NAMES,
    READ_ONLY_METHOD_ALLOWLIST,
    SAFE_EVENT_SUBSCRIPTIONS,
    SENSITIVE_READ_METHODS,
    TELEMETRY_CANDIDATE_METHOD_ALLOWLIST,
    UNSAFE_EVENT_SUBSCRIPTIONS,
    UNSAFE_GENERIC_READ_METHODS,
)
from truenas_exporter.compat_profiles import (
    PROFILE_25_10,
    PROFILE_26_0,
    PROFILE_UNKNOWN,
    V26_ADDED_METHODS,
    V26_REMOVED_EVENTS,
    V26_REMOVED_METHODS,
)
from truenas_exporter.config import DEFAULT_EVENT_SUBSCRIPTIONS
from truenas_exporter.method_safety import (
    SAFE_ALLOW_RE,
    is_documented_read_only_method,
    is_sensitive_read_method,
)


def test_read_only_catalog_is_pinned_and_contains_documented_reads() -> None:
    assert API_DOCS_TARGET_VERSION == "25.10.2"
    assert len(READ_ONLY_METHOD_ALLOWLIST) == 398

    for method in (
        "system.info",
        "system.security.config",
        "pool.query",
        "filesystem.stat",
        "ssh.config",
        "snmp.config",
        "vm.query",
        "app.registry.query",
    ):
        assert is_documented_read_only_method(method)
        assert SAFE_ALLOW_RE.fullmatch(method)


def test_documented_mutators_and_workflows_are_not_read_only() -> None:
    for method in (
        "app.convert_to_custom",
        "auth.login",
        "boot.scrub",
        "cloudsync.create_bucket",
        "nvmet.host.generate_key",
        "pool.dataset.rename",
        "pool.scrub.scrub",
        "system.reboot",
        "tn_connect.generate_claim_token",
        "virt.instance.device_delete",
        "virt.instance.set_bootable_disk",
    ):
        assert not is_documented_read_only_method(method)
        assert SAFE_ALLOW_RE.fullmatch(method) is None


def test_generic_telemetry_candidates_are_a_conservative_read_subset() -> None:
    assert len(TELEMETRY_CANDIDATE_METHOD_ALLOWLIST) == 112
    assert TELEMETRY_CANDIDATE_METHOD_ALLOWLIST < READ_ONLY_METHOD_ALLOWLIST
    assert "pool.query" in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST
    assert "user.has_local_administrator_set_up" in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST
    assert "core.ping" not in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST
    assert "app.upgrade_summary" in TELEMETRY_CANDIDATE_METHOD_ALLOWLIST


def test_sensitive_read_catalog_covers_credential_bearing_schemas() -> None:
    for method in (
        "alertservice.query",
        "api_key.my_keys",
        "app.config",
        "app.registry.query",
        "certificate.query",
        "cloud_backup.query",
        "cloudsync.credentials.query",
        "core.get_jobs",
        "docker.config",
        "iscsi.auth.query",
        "iscsi.global.sessions",
        "jbof.query",
        "kmip.config",
        "network.configuration.config",
        "nfs.get_nfs3_clients",
        "nvmet.host.query",
        "snmp.config",
        "ssh.config",
        "system.advanced.config",
        "system.advanced.sed_global_password",
        "user.query",
        "virt.instance.query",
        "vm.device.query",
        "vm.query",
        "vmware.query",
        "zfs.resource.query",
    ):
        assert is_sensitive_read_method(method)

    # Prefix checks protect newly documented entity reads until regeneration.
    assert is_sensitive_read_method("app.registry.future_read")
    assert is_sensitive_read_method("cloudsync.credentials.future_read")
    assert not is_sensitive_read_method("pool.query")

    assert len(UNSAFE_GENERIC_READ_METHODS) == 43
    assert SENSITIVE_READ_METHODS.isdisjoint(UNSAFE_GENERIC_READ_METHODS)
    assert {
        "alert.list",
        "disk.details",
        "fcport.status",
        "pool.dataset.details",
        "pool.query",
        "tunable.query",
    } <= UNSAFE_GENERIC_READ_METHODS


def test_default_event_subscriptions_are_documented() -> None:
    assert DEFAULT_EVENT_SUBSCRIPTIONS == (
        "reporting.realtime",
        "app.stats",
        "virt.instance.metrics",
        "container.metrics",
    )
    assert set(DEFAULT_EVENT_SUBSCRIPTIONS) <= SAFE_EVENT_SUBSCRIPTIONS
    assert SAFE_EVENT_SUBSCRIPTIONS | UNSAFE_EVENT_SUBSCRIPTIONS == DOCUMENTED_EVENT_NAMES
    assert SAFE_EVENT_SUBSCRIPTIONS.isdisjoint(UNSAFE_EVENT_SUBSCRIPTIONS)
    assert set(DEFAULT_EVENT_SUBSCRIPTIONS) == SAFE_EVENT_SUBSCRIPTIONS
    assert {
        "core.get_jobs",
        "jbof.query",
        "nvmet.host.query",
        "replication.query",
        "rsynctask.query",
        "virt.instance.query",
        "vm.query",
    } <= UNSAFE_EVENT_SUBSCRIPTIONS

    removed_undocumented_defaults = {
        "container.query",
        "directoryservices.status",
        "disk.query",
        "docker.state",
        "failover.status",
        "pool.scan",
        "system.reboot.info",
        "system.shutdown",
    }
    assert removed_undocumented_defaults.isdisjoint(DEFAULT_EVENT_SUBSCRIPTIONS)


def test_compatibility_profiles_encode_reviewed_intersections() -> None:
    assert PROFILE_25_10.target_version == "25.10.2"
    assert PROFILE_26_0.target_version == "26.0.0"
    assert PROFILE_UNKNOWN.target_version == "common-intersection"

    # v26 = (v25 minus removed methods) plus v26-only additions (container.*, webshare).
    assert PROFILE_26_0.reviewed_methods >= V26_ADDED_METHODS
    assert V26_ADDED_METHODS.isdisjoint(PROFILE_25_10.reviewed_methods)
    assert PROFILE_26_0.reviewed_methods - V26_ADDED_METHODS < PROFILE_25_10.reviewed_methods
    assert PROFILE_UNKNOWN.reviewed_methods == PROFILE_26_0.reviewed_methods
    assert PROFILE_UNKNOWN.reviewed_events == PROFILE_26_0.reviewed_events

    removed_methods = {
        "virt.instance.query",
        "virt.volume.query",
        "reporting.graphs",
        "reporting.netdata_graphs",
    }
    assert removed_methods <= V26_REMOVED_METHODS
    assert removed_methods <= PROFILE_25_10.reviewed_methods
    assert removed_methods.isdisjoint(PROFILE_26_0.reviewed_methods)
    assert removed_methods.isdisjoint(PROFILE_UNKNOWN.reviewed_methods)

    assert {"virt.instance.metrics"} == V26_REMOVED_EVENTS
    assert "virt.instance.metrics" in PROFILE_25_10.reviewed_events
    assert "virt.instance.metrics" not in PROFILE_26_0.reviewed_events
    assert "virt.instance.metrics" not in PROFILE_UNKNOWN.reviewed_events

    # container.metrics is the v26 rename of virt.instance.metrics.
    assert "container.metrics" not in PROFILE_25_10.reviewed_events
    assert "container.metrics" in PROFILE_26_0.reviewed_events
    assert "container.metrics" in PROFILE_UNKNOWN.reviewed_events

    assert "app.image.query" in PROFILE_25_10.reviewed_methods
    assert "app.image.query" in PROFILE_26_0.reviewed_methods
    assert "pool.is_upgraded" not in PROFILE_25_10.reviewed_methods
    assert "pool.is_upgraded" not in PROFILE_26_0.reviewed_methods
    assert "pool.ddt_prefetch" not in PROFILE_25_10.reviewed_methods
    assert "pool.ddt_prefetch" not in PROFILE_26_0.reviewed_methods

    assert PROFILE_25_10.unit_conversions["vm.get_available_memory"].source_unit == "bytes"
    assert PROFILE_25_10.unit_conversions["vm.get_available_memory"].multiplier == 1.0
    assert PROFILE_26_0.unit_conversions["vm.get_available_memory"].source_unit == "bytes"
