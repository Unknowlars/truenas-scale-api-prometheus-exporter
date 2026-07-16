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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

The cloud backup task ID.

#### Parameter 2: snapshot_id

#### snapshot_id

- Schema name: `snapshot_id`
- Type: string

ID of the snapshot whose contents to list.

#### Parameter 3: path

#### path

- Schema name: `path`
- Type: string

Path within the snapshot to list the contents of.

### Return value

- Schema name: `Result`
- Type: array of object

All files and directories at the given snapshot path.
- No Additional Items

#### Each item of this array must be:

#### CloudBackupSnapshotItem

- Schema name: `CloudBackupSnapshotItem`
- Type: object
##### name (required)

- Schema name: `Name`
- Type: string

Name of the item.

##### path (required)

- Schema name: `Path`
- Type: string

Item's path in the snapshot.

##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Directory or file.

##### size (required)

- Schema name: `Size`

Size of the file in bytes.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### mtime (required)

- Schema name: `Mtime`
- Type: string
- Type: Format: date-time

Last modified time.

##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
