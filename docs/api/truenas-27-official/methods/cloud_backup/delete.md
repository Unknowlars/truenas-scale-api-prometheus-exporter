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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the cloud backup task to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Task successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
