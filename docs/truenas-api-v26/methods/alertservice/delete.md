---
title: alertservice.delete
kind: method
source_rst: _sources/api_methods_alertservice.delete.rst.txt
source_html: api_methods_alertservice.delete.html
required_roles:
  - ALERT_WRITE
---

# alertservice.delete

## Summary

Delete Alert Service of `id`.

## Required Roles

- `ALERT_WRITE`

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

ID of the alert service to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the alert service is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
