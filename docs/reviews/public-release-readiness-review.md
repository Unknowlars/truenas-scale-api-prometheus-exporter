# Public release readiness review — 2026-11-07

## Verdict: NOT READY

Three medium confirmed defects should be corrected before public release: build-context secret exclusions, missing-data semantics, and broken local installation instructions. Two low documentation findings also need reconciliation. No critical/high defect was established. Current appliance, browser, image-security and platform acceptance remain external gates, not confirmed product defects. This is a broad source and behavioral review, not exhaustive verification of every API schema, screenshot or historical Git object.

## Scope and provenance

Branch `feat/truenas-27-support`; HEAD `04ca8b1e38e64eaee67fa91c8561d406646895ad`. Baseline `main` and merge-base both `de0e18b9fd9f92427b25783522cff91e20232169`. Chosen because this is the local main/origin-main release line and the documented modernization starting point. No remote fetch was performed; remote freshness is unconfirmed. Comparison `git diff main...HEAD`; commits 523686d, 288ac02, f1567a4, e605195, a1a5526, 04ca8b1. Initial staged, unstaged and untracked status was empty. All six commits and current release-relevant unchanged assets were in scope. No branch switch, reset, commit, push, publication or deployment occurred.

AGENTS.md, both required skills, tracker/domain conventions and prior modernization/review evidence informed inspection. GLOSSARY.md and docs/adr are absent, explicitly permitted by domain rules. Independent Standards and Spec axes follow below; supplementary findings are consolidated without replacing either axis.

## Consolidated finding ledger

| ID | Severity / confidence | Blocker | Trigger, impact, reference and correction |
|---|---|---|---|
| PRR-01 | Medium / confirmed | Yes | Ignored `.env.production` can enter Docker context: `.dockerignore:10`, `scripts/release.sh:43-53`. Clean Git status does not exclude ignored secrets. Exclude environment variants and verify with synthetic context export. No actual secret disclosure or final-image inclusion established. |
| PRR-02 | Medium / confirmed | Yes | Empty directoryservices response emits disabled rather than unknown: `runtime.py:3109-3127`, `_collect_directoryservices_metrics`. Validate required presence/null/enums; preserve names/HELP/labels. Detailed reproduction in Spec section. |
| PRR-03 | Medium / confirmed | Yes | README.md:101-106 creates `.env` but local launcher only reads process environment (`config.py:98-105`). Fresh instructions fail before startup. Document explicit safe environment configuration and test copied instructions. |
| PRR-04 | Low / confirmed | No | README support list, SECURITY.md:6 and migration evidence disagree with primary27 and later historical evidence. Reconcile supported/documented/mocked/live claims. |
| PRR-05 | Low / confirmed | No | Phase1 acceptance and historical deadline report overstate readiness/freshness behavior. Document recent-success readiness versus active subscription; add warm-success/failure/expiry regression without changing contracts. See Spec evidence. |

UNCONFIRMED risks: PRR-U1 upstream API documentation redistribution license/notices (owner verification gate, no legal violation asserted); PRR-U2 current live27, older appliances, least privilege/TLS, real job/UPS accuracy and long soak; PRR-U3 live PromQL/browser no-data behavior, ARM64/Python matrix and current image vulnerabilities. These are not included in confirmed severity counts.

Optional improvements: PRR-O1 possible Divergent Change in large runtime module; PRR-O2 hash/digest pinning of build dependencies/base images for stronger reproducibility. Neither warrants broad release refactoring.

## Coverage and evidence matrix

| Area | Inspected / tested | Remaining uncertainty |
|---|---|---|
| API/auth/collectors | Transport, profiles, safety catalogs, parsers, source isolation; focused synthetic regressions | Every schema/permission not independently exercised; current authenticated compatibility absent |
| Runtime | Poll/event snapshots, TTL, deadlines, reconnect/shutdown, readiness; 124 focused tests pass | Long soak, real reconnect and resource behavior |
| Prometheus | Contract generation and pinned Promtool inventory; 98 compatibility warnings preserved | Real cardinality and live metric accuracy |
| Security | TLS defaults, UID10001, Compose hardening, tracked-file pattern audit; dependency audit | Ignored context gap; arbitrary secret formats/history/binaries and screenshot privacy not exhaustive; image scan absent |
| Packaging | Release dry-run/guards, pins, Docker inputs and validation build | Clean isolated checkout install, ARM64 and full Python matrix not repeated |
| Grafana | Both generators and structural/reference checks pass | Live PromQL semantics, rendering, units/no-data visual acceptance |
| Public docs | README, security/contribution/license, migration and historical reviews | Upstream redistribution terms |
| Maintainability/performance | Snapshot boundaries, bounds, API cadence and large runtime inspected | Production load/memory soak |

## Official-source verification

Accessed 2026-11-07: https://api.truenas.com/v27.0/ identifies27.0.0; https://api.truenas.com/v25.10/ identifies25.10.5 (not the pinned25.10.2 snapshot). https://api.truenas.com/v26.0/ returned an empty Storj listing; fresh26 verification blocked. Exact directoryservices evidence: https://api.truenas.com/v27.0/api_methods_directoryservices.status.html requires nullable type. Pinned version-specific corpora and manifests supply documentation evidence only. No new authenticated NAS calls were made; verified read-only key availability was not established. Historical credentials were not reused or printed.

## Prior findings

Current focused regressions support repairs to event snapshot bridging, pre-send deadlines and SMB1 profile handling. These are mocked confirmations. Missing-data handling still has PRR-02. Historical broad readiness claims need PRR-05 qualification. Older live records remain historical; they do not close current acceptance gates.

## Verification ledger

`./scripts/validate.sh` inspected: compile, Ruff, mypy, pytest branch coverage floor85%, contract/Promtool, generators/manifests/parity, public audit, Compose, image build/version; matrix/security are opt-in. Initial run passed357 tests/91.80% then stopped at Promtool with34 unparsable lines. Docker-enabled rerun resolves that environmental failure; final outcome appended below. Standalone pip-audit initially failed DNS; network-enabled retry with `--no-deps --disable-pip -r requirements.txt` passed, no known runtime vulnerabilities. This excludes development/build/image vulnerabilities.

Focused runtime suite:124 passed. Generator checks and dashboard validator passed (classic370 panels/364 references; Mission Control369 elements). Public tracked-file audit passed. Release script dry-run passed, no push. Commands and limitations are preserved in axis appendices. Validation may update ignored bytecode, coverage and tool caches; no generated tracked implementation changes were observed. Docker validation creates/replaces a local `:validate` image.

## Implementation sequence and owner gates

1. Independently fix PRR-01 build context and PRR-02 collector validation with synthetic regressions (issues01/02).
2. Correct installation/support/evidence documentation and readiness tests (issue03); preserve historical provenance.
3. Resolve upstream notice/redistribution evidence (issue04) independently of code.
4. Run complete local gate on final candidate, Python/platform matrix, image audit, clean-checkout install; then bounded read-only appliance/Prometheus/Grafana acceptance (issue05). Never infer these from unit coverage.
5. Owner chooses supported release claims and accepts remaining nonblocking debt. Publish only under a separate explicit instruction, after clean exact-tag verification. No hosted CI.

Copy-ready remediation prompt:

> Read AGENTS.md, exporter skill, docs/reviews/public-release-readiness-review.md and .scratch/public-release-review/spec.md. Implement open issues01–03 in focused changes; preserve metric contracts, read-only calls and user work. Resolve issue04 with primary-source notice evidence. Complete issue05 with clearly separated mocked/local/official/live evidence. Do not publish, deploy, push, create hosted CI or silently change readiness semantics. Run ./scripts/validate.sh and record results in modernization evidence; never mark unavailable external gates passed.


## Standards — independent review

# Independent Standards axis

Baseline: `git diff main...HEAD`; six commits 523686d, 288ac02, f1567a4, e605195, a1a5526, 04ca8b1. Standards read: AGENTS.md, CONTRIBUTING.md, SECURITY.md, domain/tracker conventions and exporter validation skill. GLOSSARY.md and docs/adr are absent (per domain convention this is permitted). No pending changes were present at initial inspection.

## Axis summary (under 400 words)

One confirmed low-severity documentation violation: SECURITY.md:5-6 still says the project is maintained against SCALE 25.10.2, inconsistent with AGENTS.md's primary SCALE 27 target and the added 27 release-candidate support. CONTRIBUTING.md requires user-facing documentation updates. README.md:34 likewise excludes 27 from quickstart prerequisites despite its later candidate section. Align supported-version and evidence wording without claiming current authenticated live compatibility.

One optional heuristic: possible Divergent Change in src/truenas_exporter/runtime.py (5,872 lines), which combines lifecycle, collection, conversion and exposition coordination. This is not a documented-standard violation and not a release blocker; do not require broad refactoring before release. Preserve existing snapshot/event boundaries if extracting independently testable parsers later.

Release script respects explicit publish, dry-run default, exact version tag, clean worktree and prerelease exclusion from latest. Docker runtime uses UID/GID 10001 and removes pip. No confirmed violation of those requirements.

Standards totals: one hard documentation finding (low); one optional heuristic. Worst axis issue: stale support policy.

## Supplementary release-security finding

STD-SEC-01, medium, confirmed configuration gap; release blocker recommended before local publication: `.dockerignore:10` excludes only `.env`, whereas `.gitignore` excludes `.env.*`. `scripts/release.sh:43-53` checks git status then builds from `.`; ignored `.env.production` is invisible to that check and is not excluded from build context. Dockerfile currently uses explicit COPY and therefore this is NOT evidence that a secret appears in the final image. It exposes avoidable secret-bearing files to the configured builder, including remote builders. Reproduction is static rule comparison; no real secret was read or transmitted. Correct by excluding `.env.*` (optionally allow synthetic .env.example), private key/secret directories and generated artifacts, or use an explicit context allowlist compatible with Dockerfile.test. Regression: synthetic ignored .env.production must be absent from an exported build context; production and test images still build. Do not claim an actual credential leak.

## Additional observations / limits

requirements.txt pins runtime packages, but build-system setuptools>=75 and base python:3.14.8-slim are mutable; bit-for-bit reproducibility is not established. Treat digest/hash locking as optional unless reproducible artifacts are a release promise. Dev dependencies are bounded ranges. Public release audit scans tracked current content using a finite token-pattern list: it does not scan ignored build-context inputs, arbitrary TrueNAS key formats or Git history. Its pass is limited evidence, not a complete secret audit. No external vulnerabilities asserted; dependency database/container scans delegated to root review. No implementation files modified and no builds or publication performed by this reviewer.

## Spec — independent review

# Independent Spec review — 2026-11-07

## Axis summary (under 400 words)

The specification is the accepted modernization request as recorded in `docs/modernization/README.md`, phase documents, `.scratch/truenas27-release-remediation/spec.md`, `.scratch/telemetry-expansion/spec.md`, and `docs/telemetry-expansion.md`. Comparison: `git diff main...HEAD`, supplemented with current source, tests and prior evidence. No implementation edits were made.

One confirmed medium defect remains: `directoryservices.status={}` becomes a concrete disabled state rather than unknown (SPEC-01). This conflicts with the documented missing/malformed-data rule. No release-wide scope creep was identified. Typed expansion is profile-gated, bounded and uses selected responses. Existing deadline/event/telemetry regressions passed, but these are mocked evidence, not authenticated compatibility.

Two documentation qualifications need attention (SPEC-02): historical remediation text claims deadline failures make readiness false without qualifying that readiness deliberately uses the last successful scrape; its regression only exercises a cold start. Phase-1 acceptance also says stale events cause stream health down, whereas the preserved stream metric means an active subscription. These are specification/evidence inconsistencies, not grounds to silently change established metric semantics.

Total: one medium confirmed behavior defect, one low documentation/evidence finding containing two related corrections. No high/critical defect established in this axis. Current live, least-privilege, older-appliance, real UPS/job execution, long-soak and browser acceptance remain unverified.

## SPEC-01 — missing directory-service type fabricates disabled state

- Severity: medium; confidence: confirmed/high; suggested release blocker: yes under the explicit unknown-data contract (owner can separately assess malformed-source likelihood).
- Files/symbols: `src/truenas_exporter/runtime.py:3109-3127`, `TrueNASExporter._collect_directoryservices_metrics`; regression areas `tests/test_runtime_api_parity.py`, `tests/test_documented_api_shapes.py`.
- Trigger: `directoryservices.status` returns `{}` or a payload missing `type` with absent/null `status`.
- Impact: emits `truenas_directoryservices_config_enabled=0` and `truenas_directoryservices_status{service="none",status="DISABLED"}=1`; missing data is presented as an actual disabled configuration.
- Requirement: `docs/telemetry-expansion.md` Bounds and missing data: unknown/malformed values remain absent or NaN. Domain skill repeats the same compatibility requirement.
- Evidence: current official v27.0.0 `directoryservices.status` documentation requires `type`, permitting explicit null; missing required type is not a valid disabled state. Refreshed 2026-11-07: https://api.truenas.com/v27.0/api_methods_directoryservices.status.html . Local pinned older schema `docs/truenas-api/methods/directoryservices/status.md` likewise declares required nullable type.
- Local reproduction (executed successfully, no network):

```sh
PYTHONPATH=tests:. python3 - <<'PY'
from conftest import make_config
import truenas_exporter as m
x=m.TrueNASExporter(make_config())
x._call=lambda *a,**k: {}
x._collect_directoryservices_metrics(object(),{})
for metric in (m.DIRECTORYSERVICES_CONFIG_ENABLED,m.DIRECTORYSERVICES_STATUS,m.DIRECTORYSERVICES_HEALTHY):
 print([(s.name,s.labels,s.value) for f in metric.collect() for s in f.samples])
PY
```

- Output: config_enabled 0.0, status DISABLED 1.0, healthy{service=none} 0.0.
- Correction: validate required field presence and documented enum/null combinations before allocating metrics. Preserve explicitly disabled null type behavior; never alter metric contracts. Add empty object, missing type, malformed enum, explicit null disabled, healthy/faulted, failure/recovery RPC-to-snapshot tests. Ensure prior labels disappear after a malformed new cycle. Run focused tests then full validate.

## SPEC-02 — readiness/event acceptance overstates what existing regressions prove

- Severity: low; confidence: confirmed/high; release blocker: no if documentation is corrected before interpreting evidence.
- Affected: `.scratch/truenas27-live-validation/report.md` remediation Deadline/transport health paragraph; `docs/modernization/01-reliability.md` Acceptance; `tests/test_truenas27.py:279-335`; runtime `is_ready` at 908-917 and scrape tail 4415-4424; event HELP at `src/truenas_exporter/metrics.py:598`.
- Readiness: `is_ready` means a success within max(2*budget,2*interval,30). A subsequent failed poll does not clear last success. Existing late-deadline regression constructs a new exporter, so false readiness proves only cold-start failure. README accurately promises recent-success readiness. Correct historical claim and add successful-then-failed-then-expired behavior coverage; do not silently redefine readiness.
- Events: Phase 1 says events expire while stream health reports down; current HELP explicitly says active subscription. At TTL+1 with subscription active, CPU becomes NaN but event_stream_up remains 1. This is consistent with HELP and should be documented as subscription availability distinct from data freshness. A future freshness metric is optional and additive, not a contract-breaking reinterpretation.
- Local synthetic reproduction of TTL: set `_collector_event_stream_up['reporting.realtime']=1`, dispatch CPU=25, publish snapshot, advance monotonic by 16 seconds (15-second TTL). Snapshot emits CPU NaN and stream_up=1. No NAS accessed.
- Acceptance: documentation and tests explain both lifetimes; historical evidence is retained with correction rather than rewritten as new live validation.

## Verification and inspection

- Executed `python3 -m pytest -q tests/test_telemetry_expansion.py tests/test_truenas27.py tests/test_reliability.py tests/test_event_stream_liveness.py`: **124 passed in 1.50s**. Pytest emitted cleanup warnings for pre-existing unrelated `/tmp/pytest-of-root/garbage-*` trees after completion; no test failed. No intentional tracked modifications; pytest caches may be updated.
- Inspected transport connect/send/receive deadlines, authentication sanitation, exact read-only profile policy, source failure isolation, snapshot publication/readiness ordering, event reconnect/expiry and shutdown paths, task/directoryservice/IPMI/UPS/tier/cloud-backup/dataset collection, bounds and parser behavior, and corresponding synthetic tests.
- Prior event snapshot bridging, deadline pre-send guard, SMB1 profile behavior and telemetry expansion have current passing focused regressions. This does not repeat historical authenticated live checks.
- Official targeted directoryservices schema was fetched successfully; initial wrong-shaped URLs (`/directoryservices.status.html`, `/zfs.tier.rewrite_job_query.html`) failed. Correct official pages use `api_methods_` prefix. Pinned tier schema inspected locally, not independently live-refreshed here.
- Did not establish current live appliance behavior, 25.10/26 appliances, least privilege/TLS, physical UPS accuracy, actual tier/backup execution, long soak, or PromQL/browser behavior. Do not upgrade historical evidence to current acceptance.

## Supplemental release inspection

# Supplemental release audit

## Confirmed defect R-DOC-1 (Medium, high confidence, nonblocking if local Python support withdrawn)
README.md:101-106 instructs creating/editing `.env` then `python3 truenas_exporter.py`. Neither launcher nor CLI loads dotenv; src/truenas_exporter/config.py:98-105 reads process environment only. Fresh local Python installation following these instructions terminates with `ValueError: TRUENAS_WS_URL is required`. Independently reproduced with `env -u TRUENAS_WS_URL -u TRUENAS_API_KEY -u TRUENAS_API_KEY_FILE python3 truenas_exporter.py`. This reads no secret and makes no NAS calls. Correct instructions to explicitly export configuration safely (or add deliberately specified dotenv behavior, unnecessary for documentation fix). Test instructions from clean environment with synthetic values and mocked/local endpoint; preserve existing environment precedence and secret-file support. CONTRIBUTING.md local setup has the same misleading `.env` manual-testing implication.

## Confirmed documentation drift R-DOC-2 (Low, high confidence, nonblocking)
README.md badge and quick-start supported version list omit primary 27 despite later candidate section describing it. SECURITY.md:6 says maintained against 25.10.2. docs/truenas27-migration.md verification section still states supplied key failed and exact live appliance remains unknown, whereas modernization records later live evidence. Reconcile current supported/documented/tested/live statuses without claiming current live acceptance from historical evidence. Bundle these with R-DOC-1.

## UNCONFIRMED release risk R-LICENSE
Approximately 49 MB of vendored API documentation across docs/api, docs/truenas-api, docs/truenas-api-v26 is distributed alongside root MIT LICENSE; tracked inventory exposes no separate third-party LICENSE/NOTICE. docs/api/truenas-27-official/README.md attributes official source and retrieval but does not specify redistribution license. This does not establish a legal violation: upstream terms and required notices were not independently verified. Owner should resolve source redistribution permissions and preserve applicable upstream notices before public redistribution; do not label all upstream docs project-authored MIT. Primary-source legal review remains needed.

## Verified local checks
- `python3 scripts/public_release_audit.py`: public_release_audit_ok. Tracked current files only; regex-based patterns, no historical/binary/full arbitrary API-key assurance. No secret values printed.
- `python3 scripts/validate_dashboard.py`: dashboard_ok panels=370 metric_references=364; mission_control_dashboard_ok elements=369. Structural/reference validation, not browser/live PromQL acceptance.
- `bash scripts/release.sh`: dry-run prints linux/amd64,linux/arm64, Python3.14.8, 5.2.0rc1 tag, SBOM/provenance. No latest prerelease tag, no build/push performed.
- Static scripts/release.sh: --publish explicit, clean-tree and exact-version tag gates, validate.sh before --push.
- Static Dockerfile/compose: two-stage wheel install, UID/GID10001, Compose read-only filesystem/cap_drop/no-new-privileges, TLS true by default. Compose publishes port to all host interfaces by default: documented operational exposure, not newly identified defect. Key and CA file paths need operator mounts, migration guide explicitly says so.
- requirements.txt and pyproject runtime pins match prometheus-client0.22.1/websocket-client1.9.0. Build backend setuptools>=75 is unpinned; reproducibility across future build resolutions is not proven. Optional improvement: lock/hash build tooling or document non-bit-reproducibility, avoid making unsupported vulnerability claims.
- No implementation files changed by these commands. Public audit and dashboard checks read-only; Python launcher may produce ignored bytecode.

## Limitations
No fresh vulnerability database/image scan, arm64 build, wheel clean-environment installation, Grafana browser interaction, live datasource PromQL evaluation or third-party redistribution license confirmation performed by this supplemental reviewer. Root reviewer runs required complete validate.sh. Existing screenshots were not visually screened for private labels. Build context .dockerignore excludes .env but not all possible .env.* or arbitrary secret-file locations; runtime Dockerfile copies explicit package inputs so no evidence these enter image, but remote build context minimization is advisable as optional hardening.
- `python3 scripts/generate_truenas_dashboard.py --check` and `python3 grafana-dashboard/build_mission_control.py --check`: exit0; Mission Control validated369 panels/12tabs/365 distinct metric names, mission_control_ok. No generated files written.

## Final validation outcome

Docker/network-enabled `./scripts/validate.sh` completed exit0, `validation_ok`, container version5.2.0rc1. All357 tests passed (26.96s), coverage91.80%; all mandatory checks including public audit, Compose, image build/version passed. The initial Promtool failure did not recur with Docker access. No tests or implementation were changed to obtain this result. `git diff --check` passed. Final changes are this report, the five tracker issues/spec, and the modernization evidence append only. Ignored caches/coverage and local Docker image are verification side effects. The passing local gate does not change the NOT READY verdict or close external acceptance gates.
