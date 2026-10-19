---
title: cloud_backup.delete_snapshot
kind: method
source_rst: _sources/api_methods_cloud_backup.delete_snapshot.rst.txt
source_html: api_methods_cloud_backup.delete_snapshot.html
required_roles:
  - CLOUD_BACKUP_WRITE
---

# cloud_backup.delete_snapshot

## Summary

Delete snapshot `snapshot_id` created by the cloud backup job `id`.

This method is a job.

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

The cloud backup task ID.

#### Parameter 2: snapshot_id

<a id="Call_parameters_items_i1"></a>
#### snapshot_id

- Schema name: `snapshot_id`
- Type: string

ID of the snapshot to delete.
- Must match regular expression: `^[^-]`

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
