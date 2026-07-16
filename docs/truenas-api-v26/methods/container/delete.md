---
title: container.delete
kind: method
source_rst: _sources/api_methods_container.delete.rst.txt
source_html: api_methods_container.delete.html
required_roles:
  - CONTAINER_WRITE
---

# container.delete

## Summary

Delete a Container.

## Required Roles

- `CONTAINER_WRITE`

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

Container ID.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
