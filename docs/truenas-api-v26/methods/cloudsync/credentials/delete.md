---
title: cloudsync.credentials.delete
kind: method
source_rst: _sources/api_methods_cloudsync.credentials.delete.rst.txt
source_html: api_methods_cloudsync.credentials.delete.html
required_roles:
  - CLOUD_SYNC_WRITE
---

# cloudsync.credentials.delete

## Summary

Delete Cloud Sync Credentials of `id`.

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

ID of the cloud credential to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the cloud credential is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
