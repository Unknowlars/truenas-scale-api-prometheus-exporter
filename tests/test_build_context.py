"""PRR-01: secret-bearing files must never enter a Docker build context."""

from __future__ import annotations

from pathlib import Path

import pytest

DOCKERIGNORE = Path(__file__).resolve().parents[1] / ".dockerignore"

# .dockerignore is a checkout-level build input that is (correctly) not copied
# into the Dockerfile.test workspace; ./scripts/validate.sh runs these checks.
pytestmark = pytest.mark.skipif(not DOCKERIGNORE.exists(), reason="no .dockerignore outside a checkout")

REQUIRED_EXCLUSIONS = (
    "**/.env",
    "**/.env.*",
    "**/*.env",
    "**/secrets/",
    "**/*.pem",
    "**/*.key",
    "**/*.p12",
    "**/*.pfx",
)


def _rules() -> list[str]:
    lines = DOCKERIGNORE.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def test_secret_exclusions_present() -> None:
    rules = _rules()
    for pattern in REQUIRED_EXCLUSIONS:
        assert pattern in rules, pattern


def test_no_later_reinclude_overrides_secret_exclusions() -> None:
    # Docker applies the last matching rule; a re-include after the secret
    # block (other than the synthetic template) could re-admit secrets.
    rules = _rules()
    first_secret = min(rules.index(p) for p in REQUIRED_EXCLUSIONS)
    later_negations = [r for r in rules[first_secret:] if r.startswith("!")]
    assert later_negations == ["!.env.example"]
