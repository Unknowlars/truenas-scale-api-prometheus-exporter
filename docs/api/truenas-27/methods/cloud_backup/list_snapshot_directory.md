---
title: cloud_backup.list_snapshot_directory
kind: method
source_rst: _sources/api_methods_cloud_backup.list_snapshot_directory.rst.txt
source_html: api_methods_cloud_backup.list_snapshot_directory.html
required_roles:
  - CLOUD_BACKUP_READ
---

# cloud_backup.list_snapshot_directory

## Summary

List files in the directory `path` of the `snapshot_id` created by the cloud backup job `id`.

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

#### Parameter 2: snapshot_id

<a id="Call_parameters_items_i1"></a>
#### snapshot_id

- Schema name: `snapshot_id`
- Type: string

ID of the snapshot whose contents to list.
- Must match regular expression: `^[^-]`

#### Parameter 3: path

<a id="Call_parameters_items_i2"></a>
#### path

- Schema name: `path`
- Type: string

Path within the snapshot to list the contents of.
- Must match regular expression: `^[^-]`

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

All files and directories at the given snapshot path.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### CloudBackupSnapshotItem

- Schema name: `CloudBackupSnapshotItem`
- Type: object
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the item.

<a id="headingReturn_value_items_path"></a>
<a id="Return_value_items_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Item's path in the snapshot.

<a id="headingReturn_value_items_type"></a>
<a id="Return_value_items_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Directory or file.
###### Must be one of:

- "dir"
- "file"

<a id="headingReturn_value_items_size"></a>
<a id="Return_value_items_size"></a>
##### size (required)

- Schema name: `Size`

Size of the file in bytes.
<a id="Return_value_items_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_mtime"></a>
<a id="Return_value_items_mtime"></a>
##### mtime (required)

- Schema name: `Mtime`
- Type: string
- Type: Format: date-time

Last modified time.

<a id="headingReturn_value_items_additionalProperties"></a>
<a id="Return_value_items_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
