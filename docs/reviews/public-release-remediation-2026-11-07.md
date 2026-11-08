# Public release remediation closeout — 2026-11-07

Original review (historical findings preserved unchanged):
[public-release-readiness-review.md](public-release-readiness-review.md).
Tracker: `.scratch/public-release-review/`.

## Candidate

Branch `feat/truenas-27-support`, HEAD `04ca8b1` (unchanged since the review)
plus **uncommitted** working-tree changes. No commit, push, publication,
deployment, branch switch, reset or stash was performed. Because the candidate
is not committed, it has no exact SHA; the clean-checkout and exact-tag gates
below therefore remain open.

## Verdict: NOT READY for public release (all confirmed defects resolved)

PRR-01 through PRR-05 are fixed and regression-tested, and the full local
gate passes. Release remains blocked by external/owner gates: upstream
documentation redistribution permission (PRR-U1), authenticated live
acceptance (PRR-U2), arm64/browser/PromQL acceptance and 51 HIGH base-image
OS findings (PRR-U3), and an exact committed/tagged candidate.

## Finding resolution

| ID | Reproduced | Resolution | Regression evidence (type) |
|---|---|---|---|
| PRR-01 | Yes — synthetic `.env.production`, `secrets/api_key`, `*.pem` all entered the context (BuildKit `COPY . /ctx` listing). Nested files also re-entered through `!tests/**`. | `.dockerignore` excludes `**/.env`, `**/.env.*`, `**/*.env`, `**/secrets/`, `**/*.pem/.key/.p12/.pfx`, root `*api_key*`/`*apikey*`, and caches/build outputs; secret block placed last so earlier re-includes cannot override it. `!.env.example` retained for `Dockerfile.test`. | Synthetic re-export shows only `.env.example` (local/container). `tests/test_build_context.py` (static). Production and test images build. |
| PRR-02 | Yes — `{}` produced `config_enabled=0`, `status{none,DISABLED}=1`, `healthy{none}=0`. | `_parse_directoryservices_status` validates required `type` presence, documented enums (`ACTIVEDIRECTORY/IPA/LDAP`; `DISABLED/FAULTED/LEAVING/JOINING/HEALTHY`, case-insensitive as before) and null combinations before allocation. All owned series cleared and `config_enabled` set NaN first. Explicit `type: null` with null/absent `status` still yields the disabled state with valid zeros. No name/type/HELP/label change. | `tests/test_directoryservices_status.py`: 16 cases via stubbed RPC → collector → published snapshot → `/metrics` collector, including healthy→malformed clearing, faulted→empty→recovered. 14 fail against the pre-fix code; the 2 disabled-state cases pass both before and after (mocked). |
| PRR-03 | Yes (reviewer reproduction: `ValueError: TRUENAS_WS_URL is required`; `config.py` reads the process environment only). | README local-Python steps now export `TRUENAS_WS_URL` and `TRUENAS_API_KEY_FILE` (mode-600 key file) and state that `.env` is not loaded. CONTRIBUTING clarified. Environment precedence and key-file support unchanged. | Copied steps run with `env -i` in a fresh venv against a local listener: listener received `GET /api/current HTTP/1.1` upgrade; key file mode 600 (local, synthetic key). |
| PRR-04 | Yes — README badge/quick start and SECURITY.md named only 25.10/26.0; migration doc stated live auth failed. | Badge, quick start and SECURITY.md name 27.0 as primary with 25.10/26.0 retained; README adds a per-version evidence table (documented/mocked/historical-live). Migration doc gets a dated update citing the 2026-10-21 `27.0.0-RC.1` read-only run as historical RC evidence only. | Documentation (static). |
| PRR-05 | Yes — readiness/TTL behavior matches the review; existing late-deadline test is cold-start only. | Dated corrections appended (not rewritten) to `docs/modernization/01-reliability.md` and `.scratch/truenas27-live-validation/report.md`; README `/readyz` and `truenas_event_stream_up` descriptions clarified. Semantics unchanged. | `tests/test_readiness_lifetimes.py`: success → failed poll (`truenas_up=0`, still ready) → expiry at max_age boundary → recovery; active subscription with CPU NaN after 16 s TTL (mocked). |
| PRR-U1 | n/a | See below. Root `NOTICE` added; owner decision required. | Primary-source check (official). |

## PRR-U1 — upstream documentation notice

Accessed 2026-11-07:

- https://api.truenas.com/v27.0/ — footer "© Copyright 2026, iXsystems, Inc. dba TrueNAS."; no license or terms stated.
- https://api.truenas.com/v25.10/ (now 25.10.5) — same copyright footer; no license stated.
- https://api.truenas.com/v26.0/ — empty object listing; no terms retrievable.
- https://github.com/truenas/middleware — LGPL-3.0. Not established that the published HTML documentation is distributed under it.

No legal conclusion is drawn. Action taken: root `NOTICE` attributes the
snapshots to iXsystems, states the MIT license does not cover them, records the
above, and `docs/api/README.md` links it. Snapshot READMEs were **not** changed
because their content hashes are pinned by `MANIFEST.json`/parity checks
(an initial attempt failed validation and was reverted); regeneration is
therefore unaffected. **Owner decision required:** obtain permission/terms
from iXsystems, or remove the ~49 MB snapshots from the public release and
retain them privately (removal requires reworking manifest/parity generators).

## Checks (final candidate)

| Check | Result | Evidence type |
|---|---|---|
| `./scripts/validate.sh` | exit 0, `validation_ok`; 377 passed, coverage 91.88%; Ruff/mypy; Promtool 98-warning baseline; generators/manifests/parity; public audit; Compose; image build; version 5.2.0rc1 | local/container |
| Regenerated `docs/api-exporter-parity.{json,md}`, `docs/reviews/truenas27-inventory.json` | Only shifted `runtime.py` line citations, file hashes and fixture-test citations changed; decision counts identical | local |
| `./scripts/test_python_matrix.sh` | 3.12, 3.13, 3.14: 375 passed, 2 skipped each (static `.dockerignore` checks skip in-image) | container, amd64 |
| `Dockerfile.test` / production build | pass | container |
| `bash scripts/release.sh` | dry run only; no build/push | local |
| `git diff --check` | pass | static |
| Trivy 0.72.0 on `:validate` (HIGH/CRITICAL) | 51 HIGH, 0 CRITICAL, all Debian 13.7 base packages; 2 fixable (`apt`, `libapt-pkg` → 3.0.4); 0 in Python packages | container |
| Live smoke / authenticated appliance | pass on 27.0.0-RC.1 with an owner-authorized FULL_ADMIN key (see below); least privilege UNCONFIRMED | live |
| arm64 build | **BLOCKED** — no arm64 buildx builder on host | — |
| Live PromQL | 0 errors; empty panels classified below | live |
| Grafana browser visual | **UNCONFIRMED** | — |
| Clean isolated checkout, exact-tag gate | **UNCONFIRMED** — candidate uncommitted | — |

## Authenticated live acceptance (2026-11-07, owner-authorized)

Target: owner's appliance, `27.0.0-RC.1` (not GA), `wss://` with
`TRUENAS_VERIFY_TLS=false`, an administrator key. The owner
explicitly authorized this **FULL_ADMIN** key after being told it is not
read-only, so **least privilege remains UNCONFIRMED**. The key was kept only in
a mode-600 scratch file, mounted read-only, and deleted afterwards; it never
appeared in logs. The owner will rotate it. Only the exporter's read-only
methods plus `auth.me` and field-type checks were called. No raw responses
were kept; pool and certificate names were masked.

| Check | Result |
|---|---|
| `scripts/live_smoke.py` | pass: 5 read-only methods; 2 pools, 5 services |
| Hardened container (`--read-only`, `cap_drop ALL`, `no-new-privileges`, key file `:ro`) | `/readyz` 200 after ~20 s, `/healthz` 200, profile 25.10→27.0 selected, 0 errors/tracebacks |
| Exposition | `truenas_up=1`, ~2,350 samples, scrape 10–12 s; Promtool 97 lint lines (same as the inherited live baseline) |
| Value cross-check against API | memory 33,560,350,720 B matches `system.info.physmem`; both pools `ONLINE`/healthy match `pool.query`; directory services `type=null,status=null` → disabled state (PRR-02 valid path holds on real data) |
| Outage via local TCP proxy (NAS untouched) | `truenas_up` 0 within 5 s while `/readyz` stays 200; `/readyz` 503 ~50 s after the last success; event stream 0, CPU NaN; scrape errors logged with 2/4/8 s event backoff and no crash |
| Recovery | events back within 5 s, `truenas_up`/`/readyz` within 15 s |
| Dashboard PromQL (Prometheus v3.5.0, ~5 min of data; variables → `.*`) | 0 query errors. Operations Center 370 with data / 48 empty; Mission Control 389 / 52. Every referenced metric is exposed. |

Empty panels classified: on this appliance they are legitimately absent (no
VMs, encryption, pool expansion, pending reboot, key expiry, generic modes
disabled); CPU split is deliberately NaN because 27 realtime sends usage only;
per-disk busy/IO is empty because 27 sends only the aggregate `disk="total"`
(documented in HELP; the panels filter `disk!="total"`, so they show no data on
27 — a dashboard follow-up, not changed here).

**New defect found and fixed (LIVE-01):** `certificate.query.until` is
documented as ISO 8601 but this appliance returns ctime text, so
`truenas_certificate_days_to_expiry` and
`truenas_certificate_expiry_timestamp_seconds` were always absent. `_parse_ts`
in `collection.py` now also accepts ctime, read as UTC. Contract unchanged.
Tests: `tests/test_certificate_until_formats.py` (11). Live re-check: both
series present, 127 days to expiry.

Still not done: GA 27.0, 25.10/26.0 appliances, least-privilege key, TLS
verification with a CA, long soak, browser visual check, arm64.

## Remaining external and owner gates

1. PRR-U1 redistribution decision (above); the owner has deferred it.
2. Commit the candidate, re-run `./scripts/validate.sh` from a clean checkout of the exact SHA.
3. Live run on 27.0 GA (and 25.10/26.0 if those claims are kept) with a `READONLY_ADMIN` key and TLS verification on; long soak.
4. arm64 build and Grafana visual acceptance; decide how per-disk panels should handle the `disk="total"` aggregate on 27.
5. Rebuild on a refreshed base image and decide on remaining unfixed OS findings.
6. Owner acceptance of the supported-version claims in the README table.
