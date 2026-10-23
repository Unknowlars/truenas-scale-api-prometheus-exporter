# Local validation

Status: resolved

Run the required validation gate, Python 3.12–3.14 matrix and runtime dependency
audit. Verify historical metric metadata against the baseline.

## Answer

The required gate passed with 306 tests and 91.40% branch coverage. All 306
tests passed on each of Python 3.12.15, 3.13.16 and 3.14.8. The release image
runs Python 3.14.6 as UID/GID 10001:10001. All 417 historical metric contracts
are unchanged; three were added. Dependency audit found no known application
dependency vulnerabilities. Release script remained dry-run.

Additional checks found 97 inherited promtool naming/unit warnings and 330
image package/advisory findings (3 critical, 97 high). These are reported in
`../report.md`, not fixed or suppressed. The synthetic reproduction confirms
late-budget false health and missing SMB1 status. No exporter behavior changed.
