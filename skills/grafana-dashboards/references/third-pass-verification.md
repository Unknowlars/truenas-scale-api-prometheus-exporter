# Third-pass Verification Notes

Date: 2026-07-12

This pass verified the skill against Grafana 13.1 (released 2026-06-23, the
current stable release) and added a visual design / wow-factor layer.

## Verified against official Grafana sources (July 2026)

- Current stable release is Grafana 13.1.0 (2026-06-23); 13.0.3, 12.4.5,
  12.3.8, and 11.6.16 are the latest maintained patch lines.
- Grafana 13.0 (GrafanaCON 2026, Barcelona): dynamic dashboards GA and on by
  default; v1 dashboards auto-migrate to the v2 schema when opened; provisioned
  dashboards (API/Terraform/Git Sync) continue to work; nesting up to three
  levels; Git Sync GA in all editions (GitHub App auth, GitLab, Bitbucket, pure
  Git); `/api` deprecated in favor of `/apis`; Scenes can no longer be
  disabled; the Image Renderer plugin is fully removed; new Gauge
  visualization; Advisor GA; suggested dashboards in public preview.
- Grafana 13.0.0 Git Sync migration bug confirmed: upgrading 12.x → 13.0.0 with
  Git Sync enabled could lose/revert dashboards; recovery requires database
  restore before upgrading to 13.0.1+.
- Grafana 13.1: Filter and Group by control GA; section-level variables for
  rows/tabs GA; panel style presets GA (timeseries, stat, gauge, bar gauge,
  bar chart); copy/paste panel styles; series visibility filter in timeseries
  legends; nested table cell styling/aggregation improvements; revamped query
  editor in public preview (multi-select bulk actions, stacked view); Git Sync
  import of dashboard JSON into a provisioned folder with path/branch/commit
  selection; Grafana Assistant pre-installed in Enterprise.
- `config.apps` / `config.panels` (`@grafana/runtime`) deprecated, removal
  scheduled for Grafana 13.2 (H2 2026).
- Grafana docs publish machine-readable indexes at grafana.com/llms.txt and
  llms-full.txt; individual doc pages are available as Markdown via `.md`
  suffix — added as verification anchors.
- Release cadence: minors on even-numbered months, patches on odd-numbered
  months; each minor supported ~9 months, last minor of a major ~15 months.

## Changes made in this pass

1. Renamed/expanded the "Grafana 13 update notes" section to "Grafana 13.x"
   with the 13.0 breaking-change details (Scenes, Image Renderer, Git Sync
   bug specifics) and a full "New in Grafana 13.1" subsection.
2. Added 13.1 what's-new URL and the llms.txt/Markdown docs indexes to the
   verification anchors.
3. Added `references/visual-design-wow.md` — hero KPI bands, gradient/opacity
   fill recipes, semantic color identity, value mappings, state timelines,
   heatmaps, geomap/canvas guidance, demo/kiosk mode, anti-patterns, and a
   pre-flight visual checklist.
4. Added a "Make it pop" section to the Dashboard design principles in
   SKILL.md making visual impact a default requirement, with the explicit
   constraint that polish must never distort meaning.
5. Updated the frontmatter description so the skill triggers on requests to
   make dashboards "pop", "wow", look impressive, or be demo/executive ready.
6. Added pointers in the reference list and in `design-patterns.md` to the new
   visual design reference.

## Intentionally NOT changed

- The classic-JSON boilerplate, grid rules, PromQL/LogQL/Lucene/TraceQL
  guidance, alerting, provisioning, and LGTM sections were re-checked and
  remain accurate for 13.1; no corrections were needed.
- Panel style presets are a UI feature; the skill emulates their discipline in
  generated JSON rather than trying to reference a preset by name (no public
  JSON preset identifier is documented).
