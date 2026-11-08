# 02-directoryservices
Status: resolved
Finding IDs: PRR-02
Affected files/symbols: src/truenas_exporter/runtime.py:3109-3127 _collect_directoryservices_metrics; tests/test_runtime_api_parity.py; tests/test_documented_api_shapes.py
Blocked by: none
Blocks: final public release acceptance

## Implementation and acceptance
Validate required field presence and enum/null combinations before metric allocation. Preserve explicit disabled null behavior. Test empty/missing/malformed/healthy/faulted states and recovery through RPC-to-snapshot, clearing previous labels. Assert unknown absent/NaN, valid zero preserved; no metric contract changes.

## Validation
`python3 -m pytest -q tests/test_runtime_api_parity.py tests/test_documented_api_shapes.py; ./scripts/validate.sh`

Record exact candidate SHA, commands, results and sanitized evidence. Preserve existing contracts and user changes; do not weaken checks. Full validate required before closure.

## Answer
Reproduced: `{}` -> config_enabled 0, status{none,DISABLED} 1, healthy{none} 0.
Fix: `_parse_directoryservices_status` in runtime.py validates required `type`, enums and null combinations before allocation; all owned series cleared and config_enabled NaN first. Explicit null type with null/absent status unchanged (disabled, valid zeros). No metric contract change.
Regression: tests/test_directoryservices_status.py, 16 RPC->collector->snapshot cases (empty, missing type, bad enums, inconsistent nulls, non-dict, RPC failure, disabled, faulted/redacted, recovery). 14 fail on pre-fix code. Mocked evidence only.
Generated parity/inventory artifacts regenerated (line citations/hashes only).
Closeout: docs/reviews/public-release-remediation-2026-11-07.md. Candidate: HEAD 04ca8b1 + uncommitted working tree (no exact SHA). Final ./scripts/validate.sh exit 0, validation_ok, 377 passed, 91.88% coverage.
