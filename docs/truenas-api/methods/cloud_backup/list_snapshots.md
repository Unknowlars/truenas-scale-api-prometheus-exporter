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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

The cloud backup task ID.

### Return value

- Schema name: `Result`
- Type: array of object

All retained backup snapshots.
- No Additional Items

#### Each item of this array must be:

#### CloudBackupSnapshot

- Schema name: `CloudBackupSnapshot`
- Type: object
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for this cloud backup snapshot.

##### hostname (required)

- Schema name: `Hostname`
- Type: string

Host that created the snapshot.

##### time (required)

- Schema name: `Time`
- Type: string
- Type: Format: date-time

Time at which the snapshot was created.

##### paths (required)

- Schema name: `Paths`
- Type: array of string

Paths that the snapshot includes.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
