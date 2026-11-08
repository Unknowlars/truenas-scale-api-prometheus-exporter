# Security Policy

## Supported versions

Security fixes are applied to the latest released version. TrueNAS SCALE 27.0
is the primary API target; the 25.10 and 26.0 compatibility profiles are
retained. See the README "TrueNAS 27 release candidate" section for which
versions have documented, mocked, and historical live evidence.

## Reporting a vulnerability

Do not open a public issue containing credentials, private hostnames, API
responses, or exploit details. Contact the repository owner privately through
the contact method on their GitHub profile and include:

- affected exporter version or commit
- impact and reproduction steps
- whether credentials or a TrueNAS mutation are involved
- a redacted proof of concept

Use a read-only TrueNAS API key for normal operation. Rotate any key that may
have been disclosed and do not attach `.env` files to reports.

