---
title: support.fields
kind: method
source_rst: _sources/api_methods_support.fields.rst.txt
source_html: api_methods_support.fields.html
required_roles:
  - SUPPORT_READ
---

# support.fields

## Summary

Returns list of pairs of field names and field titles for Proactive Support.

## Required Roles

- `SUPPORT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of array

Pairs of field names and their titles for Proactive Support.
- No Additional Items

#### Each item of this array must be:

- Type: array of string
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
