---
title: cloud_backup.list_snapshots
kind: method
source_rst: _sources/api_methods_cloud_backup.list_snapshots.rst.txt
source_html: api_methods_cloud_backup.list_snapshots.html
required_roles:
  - CLOUD_BACKUP_READ
---

# cloud_backup.list_snapshots

## Summary

List existing snapshots for the cloud backup job `id`.

## Required Roles

- `CLOUD_BACKUP_READ`

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

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

All retained backup snapshots.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### CloudBackupSnapshot

- Schema name: `CloudBackupSnapshot`
- Type: object
<a id="headingReturn_value_items_id"></a>
<a id="Return_value_items_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for this cloud backup snapshot.

<a id="headingReturn_value_items_hostname"></a>
<a id="Return_value_items_hostname"></a>
##### hostname (required)

- Schema name: `Hostname`
- Type: string

Host that created the snapshot.

<a id="headingReturn_value_items_time"></a>
<a id="Return_value_items_time"></a>
##### time (required)

- Schema name: `Time`
- Type: string
- Type: Format: date-time

Time at which the snapshot was created.

<a id="headingReturn_value_items_paths"></a>
<a id="Return_value_items_paths"></a>
##### paths (required)

- Schema name: `Paths`
- Type: array of string

Paths that the snapshot includes.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_paths_items"></a>
- Type: string

<a id="headingReturn_value_items_additionalProperties"></a>
<a id="Return_value_items_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
