---
title: staticroute.delete
kind: method
source_rst: _sources/api_methods_staticroute.delete.rst.txt
source_html: api_methods_staticroute.delete.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# staticroute.delete

## Summary

Delete Static Route of `id`.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the static route to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the static route was successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
