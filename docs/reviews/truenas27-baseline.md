# TrueNAS 27 modernization baseline

Inspection date: 2026-10-19. Baseline: `de0e18b`, branch
`feat/truenas-27-support`. Preserve pre-existing untracked `.agents/` and
`skills-lock.json`. The owner supplied an untracked credential file; its contents
are never evidence and must never be staged.

## Implementation inventory

- Installable Python >=3.12 package; version 5.2.0 is unreleased. No public
  GitHub release or tag was returned by the public metadata endpoints.
- `runtime.py` coordinates synchronous polling and a separate event thread in
  collector/default and legacy modes. Both expose immutable background metric
  snapshots through threaded HTTP; requests do not issue NAS RPCs.
- Dedicated modules own transport, configuration, metric declarations, event
  ownership, safety catalogs, compatibility profiles, parsers, HTTP, and CLI.
- Reviewed 25.10 and 26.0 profiles and a conservative unknown profile exist.
  Version 27 currently selects unknown. Legacy API-key login is the only
  implemented authentication mechanism.
- Collectors cover host, pools/datasets, disks, interfaces, apps/VMs, protocols,
  jobs/alerts, inventory, security/configuration, and optional generic discovery.
  Unsupported historical metrics remain absent/NaN rather than fabricated.
- Event subscriptions supply realtime system/ZFS/network/disk/app telemetry.
  Existing recovery, staleness, skip-cache expiry, duplicate-call suppression,
  and heavy-query cadence tests must be retained.
- Docker uses a Python 3.14.6 multi-stage image and unprivileged UID 10001.
  Compose drops capabilities, uses read-only rootfs, and requires local config.
- Classic Operations Center (367 panels checked by validation) feeds generated
  Grafana v2 Mission Control (366 elements). The latter currently probes a
  hard-coded private exporter and caches names during generation; the baseline
  validation gate does not check its regeneration.
- Existing converter consumes Sphinx RST and embedded schema HTML. Historical
  25.10.2 and 26.0 Markdown corpora, manifests, API parity reports, remediation
  ledger, and modernization records already exist.

## Verification before application changes

`./scripts/validate.sh`: PASS; ruff, mypy (13 files), **257 pytest tests**, branch
coverage **91.34%** (required85%), metric/dashboard/docs/parity generation checks,
public-release audit, both Compose configurations, image build, version smoke
`5.2.0`, and final `validation_ok`.

`pip-audit --no-deps --disable-pip -r requirements.txt`: PASS, no known runtime
vulnerabilities. Runtime pins: prometheus-client0.22.1 and websocket-client1.9.0.
Development tools use bounded ranges rather than a complete lock. The first
audit attempt failed due to sandbox DNS; the network-enabled retry passed.
Image vulnerability scanning and the optional three-version Python matrix
were not part of this initial baseline pass.

Git requires a per-command `safe.directory` exception in this checkout. No
global Git configuration was changed. No hosted workflows are present.

## Evidence and gaps

Local docs identify API27.0.0. Both local and official complete archives were
inspected in memory: 662 common RST source pages differ. Source labels alone
cannot establish the appliance release or general27 compatibility. A bounded
legacy login returned false; no telemetry followed and key privileges remain
unverified. No authenticated live acceptance is claimed.

Read-only reproductions identified deadline checking after send, expired event
values surviving through the public collector without a republish, and polling
source errors aborting later collectors. Generic extraction is opt-in but dictionary
breadth and total series remain unbounded. These are focused reliability debt;
the existing package and snapshot architecture do not justify a rewrite.

The public open issue #1 describes permission failures and removed calls on an
older5.1 legacy deployment. Several named failures are already repaired here;
verify source/behavior rather than copying its historical recommendations or
granting write permissions. Public issues/PRs were read only; none were posted.

## Review coverage

Reviewed entrypoints, transport/authentication, configuration, event ownership,
poll/snapshot lifecycle, metric definitions, safety/profiles, all test modules
and fixture inventory, Docker/Compose, dashboard generation/validation, converter,
manifest/parity/contract tooling, release/security policy, and existing review
and modernization documentation. Application changes begin only after this
baseline and source acquisition work have been established.
