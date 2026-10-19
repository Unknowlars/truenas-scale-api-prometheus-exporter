# Domain documentation

Use one repository context. Read `GLOSSARY.md`, when present, and relevant
decisions in `docs/adr/` before changing behavior. Missing domain documents do
not block work. Add definitions or decisions only when useful, without inventing
an empty documentation framework.

The exporter has polling and event producers, documentation-reviewed version
profiles, owned metric specifications, and atomic exposition snapshots. Keep
those concepts distinct. Source evidence and live observations are separate.
