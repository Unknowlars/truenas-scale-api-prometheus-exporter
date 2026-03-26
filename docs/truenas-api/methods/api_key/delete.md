---
title: api_key.delete
kind: method
source_rst: _sources/api_methods_api_key.delete.rst.txt
source_html: api_methods_api_key.delete.html
required_roles:
  - API_KEY_WRITE | READONLY_ADMIN
---

# api_key.delete

## Summary

Delete API Key `id`.

## Required Roles

- `API_KEY_WRITE | READONLY_ADMIN`

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

ID of the API key to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the API key is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
