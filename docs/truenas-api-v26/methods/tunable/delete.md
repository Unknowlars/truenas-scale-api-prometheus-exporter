---
title: tunable.delete
kind: method
source_rst: _sources/api_methods_tunable.delete.rst.txt
source_html: api_methods_tunable.delete.html
required_roles:
  - SYSTEM_TUNABLE_WRITE
---

# tunable.delete

## Summary

Delete Tunable of `id`.

This method is a job.

## Required Roles

- `SYSTEM_TUNABLE_WRITE`

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

ID of the tunable to delete.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful tunable deletion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
