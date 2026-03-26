---
title: cloud_backup.delete
kind: method
source_rst: _sources/api_methods_cloud_backup.delete.rst.txt
source_html: api_methods_cloud_backup.delete.html
required_roles:
  - CLOUD_BACKUP_WRITE
---

# cloud_backup.delete

## Summary

Delete cloud backup entry `id`.

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

ID of the cloud backup task to delete.

### Return value

- Schema name: `Result`
- Type: const

Task successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
