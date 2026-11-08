# Public release follow-up — 2026-11-08

This is a focused follow-up, not an independent complete security audit.
The prior [remediation review](public-release-remediation-2026-11-07.md)
records the detailed candidate checks and outstanding owner decisions.

## Findings

1. **Release blocker: upstream documentation redistribution.** The bundled
   API documentation has no verified redistribution permission. Attribution in
   `NOTICE` does not establish permission. Obtain terms or remove the snapshots
   and adapt the dependent generators before public release.
2. **Release gate: candidate and image.** This checkout has no local tags;
   the release script requires an exact version tag and a clean worktree for
   publication. Registry image availability has not been verified. The README
   now builds locally instead of promising a published `latest` image.
3. **Compatibility evidence.** The README's version table records a live
   27.0.0-RC.1 check; least-privilege authentication and 27.0 GA remain
   unverified. Support and changelog wording now agrees with that distinction.
4. **Credential security.** The README no longer implies a full-access key is
   safe if exposed. Prefer least privilege and rotate a disclosed key.

## Limits

The local public-release audit scans tracked working-tree text for selected
secret patterns; it does not inspect Git history, all secret formats, binary
images, or prove the absence of private data. A history and screenshot privacy
review remains necessary before making the repository public. Historical image
vulnerability results, arm64, TLS and live compatibility gaps in the prior
review should be refreshed for the exact release candidate. No publication or
live appliance operation was performed in this follow-up.
