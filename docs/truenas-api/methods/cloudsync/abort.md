---
title: cloudsync.abort
kind: method
source_rst: _sources/api_methods_cloudsync.abort.rst.txt
source_html: api_methods_cloudsync.abort.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.abort

## Summary

Aborts cloud sync task.

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

ID of the cloud sync task to abort.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the sync operation was successfully aborted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
