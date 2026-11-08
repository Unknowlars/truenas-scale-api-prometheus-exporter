# 06-acceptance
Status: done
Blocked by: 01 02 03 04 05

Generators `--check`, validate_dashboard counts, 0 PromQL errors with empty
queries classified, empty-Prometheus render, dark + light screenshots
(sanitized), README/screenshots, modernization ledger entry, closeout doc.
Live render only if the owner supplies a session key; otherwise UNCONFIRMED.

## Answer
Done 2026-11-07.
- **Generators and validation.** `--check` is clean for both. `validate_dashboard.py` reports classic 367 panels / 356 references (was 370/364) and MC 379 elements (was 369); the changes are deliberate (D2 removed 8 metric refs, MC gained hero and Incident).
- **PromQL.** 0 errors on mock 27 (classic 359/58, MC 394/63 data/empty), mock 25.10 (371/46, 405/50) and live (372/45, 408/47). Empties are classified in the closeout.
- **Empty Prometheus.** No green or red tiles.
- **Screenshots.** Dark (13 tabs + 19 classic rows), light (3 tabs) and empty (2), all on mock data, in `grafana-dashboard/screenshots/`. The old screenshots were replaced.
- **Docs.** README dashboard section, ledger entry and closeout `docs/reviews/dashboard-overhaul-2026-11-07.md`.
- **Validation.** `./scripts/validate.sh` passes with `validation_ok`.
- **Live (owner key).** Kept in a mode-600 scratch file, mounted read-only, deleted at the end; no live images committed.

Limits: see the closeout ("Remaining limits").
