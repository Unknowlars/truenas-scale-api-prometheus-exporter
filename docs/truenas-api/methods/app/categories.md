---
title: app.categories
kind: method
source_rst: _sources/api_methods_app.categories.rst.txt
source_html: api_methods_app.categories.html
required_roles:
  - CATALOG_READ
---

# app.categories

## Summary

Retrieve list of valid categories which have associated applications.

## Required Roles

- `CATALOG_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of string

Array of available application category names.
- No Additional Items

#### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
