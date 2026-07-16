---
title: interface.delete
kind: method
source_rst: _sources/api_methods_interface.delete.rst.txt
source_html: api_methods_interface.delete.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.delete

## Summary

Delete Interface of `id`.

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
- Type: string

ID of the interface to delete.

### Return value

- Schema name: `Result`
- Type: string

ID of the interface that was deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
