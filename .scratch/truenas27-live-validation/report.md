# SCALE 27 validation report — 2026-10-21

Status: remediated and revalidated. The original 2026-10-21 findings and
evidence are retained below as historical pre-remediation evidence.

Source: `a1a5526`, exporter `5.2.0rc1`; modernization baseline `de0e18b`.
The pre-existing untracked `docs/reviews/truenas27-gap-analysis.md` is preserved.
The remediation is an uncommitted working-tree change on `a1a5526`; no commit,
push, publication, deployment, or NAS configuration/storage change occurred.

## Remediation verification — 2026-10-21

### Fixed behavior

- **Collector publication:** every valid, invalid, expired, subscription, and
  teardown transition now bridges event caches and requests a throttled atomic
  snapshot publication. Publication remains bounded to once per second; timer
  callbacks take the polling lock, `/metrics` reads only the last complete
  snapshot, and shutdown cancels a pending timer. The original
  `--assert-event-freshness` reproduction now passes with the expected CPU value
  and snapshot event age 0 after 16 seconds of continuous updates. Regression
  tests cover continuous updates, real silence/expiry, recovery, a blocked poll
  lock, reconnect/teardown paths, bounded frequency, and shutdown.
- **Deadline/transport health:** the transport exposes a pre-send deadline
  check, and scrape-local state records deadline/transport failures even when an
  independent helper catches the exception. Late exhaustion now produces
  `truenas_up=0` and readiness false while retaining earlier partial metrics.
  The synthetic late-deadline case records 73 pre-send rejections and **zero**
  late transport calls. Existing early-deadline coverage confirms no connect or
  send occurs after expiry.
- **SMB1:** 26.0/27.0 derive the existing `truenas_smb1_enabled` gauge from the
  recognized `minimum_protocol` enum; 25.10 continues using `enable_smb1`.
  `SMB1`, `SMB2`, `SMB3`, missing, null, malformed, unknown, and failed-source
  cases are covered. Unknown data remains non-finite, never reassuring zero.
- **Heavy-query freshness:** disk-temperature aggregates and the oldest-snapshot
  cache now use monotonic wall time for refresh and maximum staleness. A long
  polling outage forces an immediate refresh on recovery; a failed refresh drops
  data once the wall-clock staleness bound is exceeded.
- **Authentication safety:** modern login failures report only a validated,
  bounded uppercase `response_type` enum (otherwise `UNKNOWN`); arbitrary server
  content remains excluded. `Config.api_key` is excluded from `repr`.

### Local, packaging, scanner, and lint evidence

- `./scripts/validate.sh`: PASS, `validation_ok`; 324 tests, 91.75% branch
  coverage, Ruff, mypy, deterministic generated artefacts, dashboard validators,
  Compose checks, public-release audit, image build, and container version smoke.
- `./scripts/test_python_matrix.sh`: PASS, 324 tests each on Python 3.12.15,
  3.13.16, and 3.14.8. `pip-audit 2.10.1` reports no known vulnerabilities in
  the two pinned application dependencies. `./scripts/release.sh` was exercised
  in dry-run mode only and selects Python 3.14.8 without `latest` for the RC.
- All 420 metric name/type/HELP/label contracts are unchanged. Promtool 3.5.0
  still reports the expected 97 warnings on the live exposition. A synthetic
  all-family exposition reports 98 because it also includes the live-absent
  `truenas_certificate_days_to_expiry`. The exact warning-name inventory is now
  fingerprinted by `scripts/check_prometheus_lint_baseline.py`; any new, removed,
  or renamed warning fails validation. No warning was suppressed.
- The final validation image is
  `sha256:dc30f711dd2c3b9447aa66dbb15b9660ce87964c59aba71479b9f874ccfe7996`,
  Python 3.14.8 on Debian 13.7, UID/GID 10001:10001, with `pip` absent from the
  runtime stage. Trivy 0.72.0 reports 164 OS package/advisory findings: 44 high,
  58 medium, 61 low, 1 unknown, 0 critical, and none with a listed fixed version;
  Python package findings are zero. Compared with the historical image, 166
  findings were removed, including all 3 critical and 53 high findings. These
  are scanner classifications, not confirmed exploitability assessments.

### Live and packaged evidence

- **LIVE/source runtime:** the server still reports `27.0.0-RC.1` and selects
  profile `27.0`. The current-default session completed a healthy 9.682-second
  poll, SMB source/metric comparison, nine event observations over 18 seconds
  with finite CPU and snapshot ages 1.467–1.913 seconds, ten HTTP scrapes with
  zero NAS RPCs, and local event-socket reconnection. The historical-settings
  repeat completed a healthy 9.651-second poll, matching SMB, nine finite event
  observations aged 1.446–1.986 seconds, and ten HTTP scrapes with zero NAS
  RPCs. One immediately preceding historical attempt failed the bounded event
  freshness assertion; no raw values were retained and a same-settings repeat
  passed, so this remains a transient live limitation requiring soak coverage.
- **PACKAGED:** the hardened image content (runtime config digest
  `sha256:0ddd7f9f386e1a56346e8d6be6d9378ce042975cd023ddb6127f0cf996516f8e`)
  ran read-only with all capabilities dropped and no-new-privileges. It became
  healthy, exposed 1,778 samples, and kept CPU finite with event ages 0.107,
  1.850, and 1.748 seconds across the old TTL boundary; ten additional metrics
  reads succeeded. The subsequently rebuilt validation manifest differs only in
  BuildKit attestation identity and has the same runtime config/layers; it was
  scanned exactly but not given another live credential.

### Remaining limits and security incident

No real 25.10/26.0 appliance, least-privilege key, certificate verification,
long soak, NAS restart, live PromQL, or Grafana browser acceptance was tested.
The 164 remaining image advisories have no scanner-listed fix and were not
individually assessed for exploitability. The historical event-session failure
above remains unresolved as a transient observation, so release readiness is
improved but not unconditional.

During the packaged check, Docker's pseudo-TTY echoed the stdin-supplied key once
into the execution transcript. It was not placed in a command argument, file,
image, container configuration, retained report/evidence value, or commit, and
the container was stopped. The key must be rotated; it was not reused afterward.

## Evidence boundaries

- **LIVE:** modern authentication succeeded; server reports `27.0.0-RC.1` and
  the actual runtime selects profile `27.0`. Only reviewed read-only methods
  and authentication/subscription transport operations were permitted.
- The authenticated session exposed a wildcard method/resource allowlist.
  After this was disclosed, the owner explicitly authorized continuing with
  the supplied key. This verifies compatibility with that key, not operation
  under `READONLY_ADMIN` or least-privilege permissions.
- Existing TLS verification was disabled for these tests. Certificate trust
  verification was not established. No NAS configuration or storage changes.
- Credentials were entered through hidden stdin and kept in process memory.
  Operational responses and metric labels were inspected only in memory;
  retained evidence contains method/metric identifiers, aggregate results and
  sanitized diagnostics. No production payloads or keys were saved.
- **MOCKED:** deterministic reproductions below are synthetic and issue no RPCs.
- **LOCAL:** tests, generated artifacts, image, dependency and exposition checks
  are distinct from live appliance and Grafana browser acceptance.

## Local results

| Check | Result |
| --- | --- |
| `./scripts/validate.sh` | PASS; `validation_ok`, 306 tests, 91.40% branch coverage, Ruff/mypy, generated checks, both dashboards, Compose checks, image build, container version `5.2.0rc1` |
| `./scripts/test_python_matrix.sh` | PASS; 306 tests each on Python 3.12.15, 3.13.16, 3.14.8 |
| Runtime dependency audit | `python3 -m pip_audit --cache-dir /tmp/truenas-exporter-pip-audit --no-deps --disable-pip -r requirements.txt`: no known vulnerabilities in the two pinned application dependencies |
| Historical metric contracts | PASS; all 417 baseline contracts preserved, including type, HELP and labels; three additions, 420 current contracts |
| Release script | Dry run only; prerelease tag `5.2.0rc1`, no `latest`, no publication |
| Runtime image | Python 3.14.6, UID/GID `10001:10001`; image `sha256:ec5e80fbc6db2ef34d655c43b6c779531dfd13a9d509a5fd95f3d2c74f2a2ba9` |

Tool versions: host Python 3.12.3, pytest 8.4.2, pytest-cov 7.1.0, Ruff 0.15.21,
mypy 1.20.2, pip-audit 2.10.1, Docker client/server 29.9.1, promtool 3.5.0,
Trivy 0.72.0. Docker/network access initially needed elevated execution;
authorized reruns succeeded. No Git configuration was changed.

## Live method and exporter checks

The five-method smoke passed `system.state`, `system.info`,
`system.version_short`, `pool.query` and `service.query`; the two queries used
`limit=5`. Authentication used `auth.login_ex(API_KEY_PLAIN)` with the
owner-confirmed username. Authentication did not silently fall back.

Both sustained sessions use the source runtime on host Python 3.12.3, collector
mode, an ephemeral loopback HTTP listener, 30-second polling, a 20-second call
timeout, 25-second polling budget, and the supplied query/entity/dataset limits.
Generic method/event extraction stays disabled. Sessions are sequential and
last five minutes each, followed by bounded worker shutdown.

Current defaults select discovery/listdir off and dataset snapshot fallback 25.
The historical-settings session selects discovery/all-metrics/listdir on and
dataset snapshot fallback 0. Both use modern authentication and profile-aware
default event subscriptions; this intentionally adds the required username to
the old settings rather than assuming old authentication works.

### Current defaults — complete

- Eight polling cycles; every completed cycle has `truenas_up=1`, readiness
  true and profile `27.0`; observed polling durations 9.004–9.738 seconds.
- 1,290 RPC attempts covering 127 distinct reviewed methods; no safety-denied
  methods. The only RPC exceptions were three unsubscribe attempts on the
  locally closed event connection during the deliberate reconnect test.
- 148 liveness probes returned 200. Readiness returned 503 for five startup
  probes, then 200 for 143 probes; no HTTP failures. Maximum combined HTTP
  liveness/readiness/metrics probe time was 0.060 seconds.
- Peak exposition: 1,776 samples / 166,338 bytes; 323 distinct metric sample
  names had a finite value during the session.
- `reporting.realtime` and `app.stats` delivered messages. Both event connection
  setup sequences acquired three subscriptions. `container.metrics` payload
  correctness remains unverified because no such updates were observed.
- Withholding event frames locally for 22 seconds caused the CPU metric to
  become NaN after its configured TTL; it became finite again after resuming
  events and subsequent polling. The independently confirmed publication
  defect below means this alone does not establish complete event correctness.
  Closing only the client's event socket caused successful reconnection.
- Ten `/metrics` requests after polling stopped caused **zero** additional
  NAS RPCs. Both workers stopped cleanly.
- 112 field/count comparisons matched across the eight cycles: host physical
  memory, VM available memory, disk/interface/service/pool counts, and pool
  size/allocated/free/freeing bytes. The SMB1 comparison failed in every cycle;
  see finding 3. Real entity identities and values are not retained.
- Dataset, application and task metric families contained finite values.

### Historical settings — complete

- Eight polling cycles, all up/ready on profile `27.0`, taking 9.055–9.436
  seconds. 1,082 RPC attempts across 126 methods; no RPC errors or denied
  methods. No fault injection was applied in this session.
- 148 liveness probes returned 200; readiness was 503 for five startup probes
  and 200 for 143 later probes. No HTTP failures; maximum combined HTTP probe
  time 0.045 seconds. Ten final metrics requests caused zero extra RPCs.
- Peak exposition 1,747 samples / 164,357 bytes; 322 finite sample names.
  Both workers stopped cleanly after 301.37 seconds including teardown.
- 112 successful comparisons and eight SMB1 mismatches, matching the first
  session. `reporting.realtime` and `app.stats` delivered updates; three
  subscriptions were acquired, with no `container.metrics` payload observed.
- The only finite metric family present with current defaults but missing with
  the old settings was `truenas_dataset_snapshot_count`. Current defaults made
  200 `pool.dataset.snapshot_count` calls across eight cycles (25 per cycle),
  versus zero with the old fallback limit of 0. Other call-count differences
  came from the intentional reconnect in the first session.
- Neither configuration invoked discovery or filesystem listing: those paths
  are gated by `ENABLE_GENERIC_METHOD_METRICS`, which was false in both.

### Packaged runtime — complete

The validated image also completed a bounded live scrape with a read-only
container filesystem, dropped capabilities and `no-new-privileges`: Python
3.14.6, exporter `5.2.0rc1`, profile `27.0`, up/ready, 9.554 seconds, 161 calls
across 125 methods, no RPC errors. There were 144 additional successful
comparisons: app count, dataset count, 69 dataset-used byte values, 69
dataset-available byte values and four task-type counts. No dataset identities
or operational values were retained. Live legacy key-only authentication also
succeeded with the new key. The earlier migration note about an older key's
failure must not be applied to this key. Explicit `TRUENAS_USERNAME` still
selects and tests modern authentication.

The subsequent focused event-publication check repeated the packaged scrape
with `reporting.realtime` enabled: 165 calls across 127 methods, zero errors,
144 additional matching comparisons, up/ready true. It ran 35.133 seconds
including the scrape and 24-second observation window. The actual HTTP
observations establish the publication defect:

| Seconds after polling completed | Newest event age | Published snapshot event age | HTTP CPU metric |
| --- | --- | --- | --- |
| 0 | 0.047 s | 0.057 s | finite |
| 12 | 1.193 s | 12.120 s | finite |
| 18 | 1.051 s | 18.150 s | NaN |
| 24 | 0.935 s | 24.179 s | NaN |

There were **512 matching comparisons** across the two sustained sessions and
two packaged scrapes, plus the 16 sustained SMB1 mismatches. These are field
observations, not 512 distinct metric families or independent test cases.

## Historical confirmed findings (pre-remediation)

1. **High — collector event snapshots stop refreshing between polls.** The
   undisturbed live session exposed a non-finite CPU metric despite continuing
   event messages. A deterministic synthetic reproduction delivers a new CPU
   event every two seconds: at 16 seconds the newest event is age 0 but the
   published snapshot is age 16, so `TrueNASCollector.collect()` returns NaN.
   The collector branch of `_dispatch_event` updates event caches without
   publishing a new HTTP snapshot; legacy mode does publish. Switching only
   the mode to legacy, or explicitly publishing the collector bridge, exposes
   the latest synthetic value. Raising TTL to 60 keeps the old value visible
   rather than refreshing it. This is a publication defect, not a payload or
   clock problem. Polling health can remain true while realtime charts have
   regular gaps. The packaged live HTTP check above confirms the same failure:
   events remain fresh while snapshot age exceeds TTL and CPU exposition is NaN.
2. **High — late deadline failures can report healthy.** The synthetic transport
   advances beyond the total deadline immediately after `update.status` and
   rejects every later call. Public `scrape_once()` still exposes `truenas_up=1`
   and `is_ready()=True`, despite 73 late `TimeoutError`s. The late helper
   collectors catch failures without setting the required-source failure flag
   before `success = not self._required_source_failed` in `runtime.py:4141`.
   This independently confirms the earlier review finding; it was not observed
   during the healthy live polling windows and was not induced on the NAS.
3. **Medium — SMB1 status is missing on 26/27.** `runtime.py:5056` still reads
   `enable_smb1`; the 27 schema and live response use `minimum_protocol`.
   Live metric/API comparisons fail for every current-defaults cycle. Synthetic
   `SMB1` and `SMB2` cases both yield a non-finite metric on 27, and `SMB1` also
   fails on 26. A missing metric must not be interpreted as SMB1 disabled.
4. **Image scan — unresolved package findings.**
   `trivy image --image-src docker --scanners vuln --timeout 5m --cache-dir
   /tmp/truenas27-trivy-cache --format json --output
   /tmp/truenas27-image-audit.json truenas-scale-api-prometheus-exporter:validate`
   reports 330 package/advisory findings: 3 critical, 97 high, 131 medium, 95 low,
   4 unknown. There are 329 Debian package findings and one pip finding; 166
   findings have a listed fixed version. The critical findings concern
   `perl-base`. These are scanner classifications, not confirmed exploitable
   paths through the exporter. The clean application dependency audit does not
   cover the base operating system or bundled packaging tools.
5. **Prometheus lint — inherited contract warnings.** Live exposition parses,
   but `promtool check metrics` exits 3 with 97 lint diagnostics: 87 `_count`
   suffix warnings, two non-counter `_total` warnings, six day-unit warnings
   and two minute-unit warnings. Every affected metric exists in the baseline
   contract. Renaming them silently would violate compatibility; no changes
   were made. Parsing and metric correctness are separate from lint conventions.

Synthetic reproductions are retained in `reproduce_findings.py` in this folder:

```sh
python3 .scratch/truenas27-live-validation/reproduce_findings.py
```

At the time of the historical run, the explicit event freshness assertion
intentionally exited 1. It now exits 0 and is covered by repository regression
tests:

```sh
python3 .scratch/truenas27-live-validation/reproduce_findings.py --assert-event-freshness
```

## Historical remaining limits

No real 25.10/26.0 appliance was tested; those compatibility results are mocked.
No general generic-extraction load test or API-wide method sweep was performed.
No long-duration soak, NAS restart, disruptive fault injection, deployment,
PromQL evaluation against a live Prometheus, or Grafana browser acceptance.
Other historical review hypotheses remain unconfirmed unless explicitly
reproduced here. Functional local checks pass, but the findings above prevent
an unconditional release-readiness claim.

Sanitized machine-readable results are retained in `evidence.json` in this
folder. The only intentionally failing assertion is the new event-freshness
reproduction; the existing complete validation suite remains green. No test
expectations were weakened and no findings were fixed or suppressed.
