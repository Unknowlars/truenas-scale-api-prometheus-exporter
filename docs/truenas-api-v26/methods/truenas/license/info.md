---
title: truenas.license.info
kind: method
source_rst: _sources/api_methods_truenas.license.info.rst.txt
source_html: api_methods_truenas.license.info.html
required_roles:
  - READONLY_ADMIN
---

# truenas.license.info

## Summary

Returns the parsed license object, or null if no license exists.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`

Parsed license JSON object, or `null` if no license file exists.
#### Any of

##### Option 1

- Type: object

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
