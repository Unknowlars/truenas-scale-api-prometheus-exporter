# TrueNAS API 27.0.0 Markdown snapshot

Source: [http://192.168.0.238:8070/api/docs/current/](http://192.168.0.238:8070/api/docs/current/). Retrieved: 2026-10-19. This snapshot describes the API documentation; it does not establish the appliance release or live compatibility.

`MANIFEST.json` records the source archive SHA256, individual source/content checksums, required roles, parameter positions, schema field identifiers/types/required markers and method/event inventories.

- [Methods](methods/index.md)
- [Events](events/index.md)
- [Authentication](authentication.md)
- [Schemas](schemas/index.md)
- [Shared guides](shared/index.md)
- [RBAC](shared/rbac.md)
- [Changelog](shared/changelog.md)
- [Compatibility](compatibility.md)

## Regeneration

Run from the repository root using the retained archive or extracted source tree:

```bash
python3 scripts/convert_truenas_api_docs_to_markdown.py --archive /tmp/truenas27-docs/local.zip --output docs/api/truenas-27 --api-version 27.0.0 --source-url http://192.168.0.238:8070/api/docs/current/ --retrieved-at 2026-10-19 --clean
```

Append `--check` to compare byte-identical output without changing files. The retrieval date is a fixed input. Raw source archives are deliberately outside Git.

Acquire a fresh archive deliberately (this changes the pinned source checksum):

```bash
python3 scripts/convert_truenas_api_docs_to_markdown.py --archive /tmp/truenas27-docs/local.zip --output docs/api/truenas-27 --api-version 27.0.0 --source-url http://192.168.0.238:8070/api/docs/current/ --retrieved-at 2026-10-19 --download-url http://192.168.0.238:8070/api/docs/current/truenas-v27.0.0-docs.zip
```

The existing converter reads `_sources/*.rst.txt` and embedded schema HTML. Original fields, alternatives, constants, constraints, examples and roles are retained in owning pages; the inventory is an index, not a substitute for those schemas.
