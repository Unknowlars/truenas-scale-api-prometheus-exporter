---
title: cloudsync.delete
kind: method
source_rst: _sources/api_methods_cloudsync.delete.rst.txt
source_html: api_methods_cloudsync.delete.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.delete

## Summary

Deletes cloud_sync entry `id`.

## Required Roles

- `CLOUD_SYNC_WRITE`

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

ID of the cloud sync task to delete.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the cloud sync task is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
