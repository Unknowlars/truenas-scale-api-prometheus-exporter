# Contributing

Thanks for helping improve the exporter.

## Local setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
```

Set `TRUENAS_WS_URL` and `TRUENAS_API_KEY` in `.env` before manual testing.
Use a read-only API key when talking to a real system.

## Tests

```bash
./scripts/validate.sh
```

Set `RUN_PYTHON_MATRIX=1` to run the local Python 3.12/3.13/3.14 container matrix.
Set `RUN_SECURITY_AUDIT=1` to query the vulnerability database with `pip-audit`.
The project intentionally has no GitHub Actions or other hosted CI; do not add
hosted workflow files without explicit owner approval.

## Pull requests

- keep changes focused and easy to review
- add or update tests when behavior changes
- update `README.md`, `.env.example`, or `CHANGELOG.md` when user-facing behavior changes
- avoid committing secrets, local `.env` files, or large local artifacts
- preserve existing Prometheus metric names, types, help text, and labels

If you are adding new metrics, prefer stable names, bounded labels, and clear
documentation for any cardinality trade-offs.
