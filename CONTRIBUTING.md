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
.venv/bin/pytest
.venv/bin/python -m compileall truenas_exporter.py tests
```

## Pull requests

- keep changes focused and easy to review
- add or update tests when behavior changes
- update `README.md`, `.env.example`, or `CHANGELOG.md` when user-facing behavior changes
- avoid committing secrets, local `.env` files, or large local artifacts

If you are adding new metrics, prefer stable names, bounded labels, and clear
documentation for any cardinality trade-offs.
