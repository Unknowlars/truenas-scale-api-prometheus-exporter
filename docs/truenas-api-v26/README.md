# TrueNAS API Markdown Export

This directory contains an AI-friendly Markdown conversion of the offline TrueNAS API docs.

## Layout

- `methods/`: converted API method namespaces and leaf pages
- `events/`: converted API event namespaces and leaf pages
- `shared/`: JSON-RPC, query behavior, and job guides

## Regenerate

```bash
python scripts/convert_truenas_api_docs_to_markdown.py --clean
```

The converter reads from `_sources/*.rst.txt` for page metadata and parses each embedded `#json-schema` block into Markdown headings, bullets, and examples.

## Entry Points

- [Methods](methods/index.md)
- [Events](events/index.md)
- [Shared Guides](shared/index.md)
