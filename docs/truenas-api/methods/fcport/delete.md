---
title: fcport.delete
kind: method
source_rst: _sources/api_methods_fcport.delete.rst.txt
source_html: api_methods_fcport.delete.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fcport.delete

## Summary

Delete FC port mapping `id`.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

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

ID of the Fibre Channel port to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the Fibre Channel port is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
