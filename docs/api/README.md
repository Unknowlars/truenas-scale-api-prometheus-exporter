# Versioned TrueNAS API documentation

The appliance documentation archive is the primary 27.0.0 reference for this modernization. The official archive is retained separately because their contents differ despite reporting the same API version. Neither documentation title establishes the exact appliance release, account permissions, or successful live exporter behavior.

| Snapshot | API version | Methods | Events | Archive SHA256 |
| --- | --- | ---: | ---: | --- |
| [Appliance](truenas-27/README.md) | 27.0.0 | 835 | 84 | `cc3e9625d4847ed18d296bd7c006490196e9df8b1451082eaa43677d8952d3b4` |
| [Official](truenas-27-official/README.md) | 27.0.0 | 834 | 84 | `3649a158eb238fcfe92876bff9bd3fb5826411b56ce2c0471ffe1921ef7ee000` |

Retrieved on 2026-10-19 from the [appliance archive](http://192.168.0.238:8070/api/docs/current/truenas-v27.0.0-docs.zip) and [official archive](https://api.truenas.com/v27.0/truenas-v27.0.0-docs.zip). Raw ZIPs stay outside Git in `/tmp/truenas27-docs/`. Each snapshot's `MANIFEST.json` contains the archive checksum, source HTML/RST checksums, generated Markdown checksums, method/event inventory, roles, parameter positions and documented schema fields.

Both archives contain generated Sphinx HTML and reStructuredText sources with embedded schema HTML; neither archive contains JSON files exposing canonical JSON schemas. Authentication, RBAC, JSON-RPC transport, query semantics, jobs and changelog guides are converted along with every available method/event page. The schema index links to owning pages rather than inventing standalone schema definitions.

## Source disagreements

Among source RST files, 465 shared pages are identical and 662 shared pages differ. There are eight appliance-only and seven official-only source pages, including namespace indexes:

- Appliance-only methods: `core.debug`, `disk.get_instance`, `tn_connect.ip_choices`, `zfs.resource.create`.
- Official-only methods: `boot.environment.get_instance`, `sharing.s3.recover`, `sharing.s3.recoverable_buckets`.
- Appliance-only event families: `app.image`, `app.registry` (including their `.query` events).
- Official-only event families: `boot.environment`, `zfs.resource` (including `.query` and `.list` events respectively).

These are documentation differences. They do not establish runtime availability and do not authorize invoking any method, particularly mutating or debugging methods. The compatibility review must resolve exporter-used differences against documented signatures, pinned source where necessary, and explicitly identified read-only live checks.

The converter fixes previously omitted `oneOf` alternatives, enum/constant/pattern constraints and captioned shared-guide examples. It caps Markdown headings at six levels while retaining exact schema identifiers as anchors, and checks that every documented property identifier survives conversion. Individual property paths preserve nested/alternative context in the schema inventory; the inventory does not replace the owning response schema.

## Reproduction and checks

Each snapshot README provides its complete regeneration command and explicit download command. Regeneration uses the recorded retrieval date, never the current clock. Add `--check` to the same conversion command for a non-mutating byte comparison. Downloads require an explicit `--download-url`; offline regeneration never fetches a new source.

```bash
python3 scripts/generate_api_docs_manifest.py --target 27 --check
python3 scripts/generate_api_docs_manifest.py --target 27-official --check
```

The manifest checker verifies generated file checksums against the pinned manifest. Full converter `--check` also regenerates metadata, inventory and files from the original source archive. No acquisition or conversion invokes a TrueNAS API method or uses credentials.

Previous [25.10.2](../truenas-api/README.md) and [26.0.0](../truenas-api-v26/README.md) corpora remain available. The manifest tool defaults to 25.10.2 for compatibility; select 27 or 27-official explicitly.

## Copyright and license

The snapshots under `docs/api/`, `docs/truenas-api/` and `docs/truenas-api-v26/` are converted from documentation (c) iXsystems, Inc. dba TrueNAS. They are not covered by the repository MIT license; see the root [NOTICE](../../NOTICE). Snapshot READMEs are hash-pinned by their manifests and are intentionally left unchanged.
