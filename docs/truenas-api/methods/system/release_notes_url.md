---
title: system.release_notes_url
kind: method
source_rst: _sources/api_methods_system.release_notes_url.rst.txt
source_html: api_methods_system.release_notes_url.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# system.release_notes_url

## Summary

Returns the release notes URL for a version of SCALE.

`version_str` str: represents a version to check against

If `version` is not provided, then the release notes URL will return a link for the currently installed version of SCALE.

## Required Roles

- `SYSTEM_PRODUCT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: version_str

#### version_str

- Schema name: `version_str`
- Default: null

Version string to get release notes for. `null` for current version.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: string

URL to the release notes for the specified version.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
