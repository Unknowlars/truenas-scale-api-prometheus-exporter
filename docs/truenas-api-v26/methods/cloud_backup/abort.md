---
title: cloud_backup.abort
kind: method
source_rst: _sources/api_methods_cloud_backup.abort.rst.txt
source_html: api_methods_cloud_backup.abort.html
required_roles:
  - CLOUD_BACKUP_WRITE
---

# cloud_backup.abort

## Summary

Abort a running cloud backup task.

## Required Roles

- `CLOUD_BACKUP_WRITE`

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

ID of the cloud backup task whose backup job to abort.

### Return value

- Schema name: `Result`
- Type: boolean

The backup was successfully aborted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
