---
title: iscsi.extent.disk_choices
kind: method
source_rst: _sources/api_methods_iscsi.extent.disk_choices.rst.txt
source_html: api_methods_iscsi.extent.disk_choices.html
required_roles:
  - READONLY_ADMIN | SHARING_ISCSI_EXTENT_READ
---

# iscsi.extent.disk_choices

## Summary

Return a dict of available zvols that can be used when creating an extent.

## Required Roles

- `READONLY_ADMIN | SHARING_ISCSI_EXTENT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Object mapping disk identifiers to their display names.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
