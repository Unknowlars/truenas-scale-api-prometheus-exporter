---
title: zfs.resource.snapshot.create
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.create.rst.txt
source_html: api_methods_zfs.resource.snapshot.create.html
required_roles:
  - SNAPSHOT_WRITE
---

# zfs.resource.snapshot.create

## Summary

Create a ZFS snapshot.

Invalid input is returned to the client as a JSON-RPC `error` response (code `-32602`, *Invalid params*); each failing condition appears in the error's `data.extra` array with its own `errno`. A validation error is raised when:

- the dataset does not exist

- the snapshot already exists

Examples:

Create a single snapshot:

.. code:: json

{"dataset": "tank/data", "name": "backup"}

Create snapshots recursively:

.. code:: json

{"dataset": "tank", "name": "backup", "recursive": true}

Create with user properties:

.. code:: json

{"dataset": "tank/data", "name": "backup", "user_properties": {"com.company:backup_type": "daily"}}

## Required Roles

- `SNAPSHOT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Create parameters for creating ZFS snapshots.
- No Additional Properties
##### dataset (required)

- Schema name: `Dataset`
- Type: string

Dataset path to snapshot (e.g., 'pool/dataset').
- Must be at least `1` characters long

##### name (required)

- Schema name: `Name`
- Type: string

Snapshot name (the part after @).
- Must be at least `1` characters long

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Create snapshots recursively for child datasets.

##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Datasets to exclude when creating recursive snapshots.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### user_properties

- Schema name: `User Properties`
- Type: object
- Default: {}

User properties to set on the snapshot. Only user-defined properties are supported (e.g., 'com.company:backup_type'). Regular ZFS properties cannot be set on snapshots at creation time.
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

### Return value

- Schema name: `ZFSResourceSnapshotEntry`
- Type: object
- No Additional Properties
#### createtxg (required)

- Schema name: `Createtxg`
- Type: integer

The TXG in which the snapshot was created.

#### guid (required)

- Schema name: `Guid`
- Type: integer

A GUID for the snapshot.

#### name (required)

- Schema name: `Name`
- Type: string

The zfs resource for the given snapshot.

#### pool (required)

- Schema name: `Pool`
- Type: string

The zpool of the snapshot.

#### dataset (required)

- Schema name: `Dataset`
- Type: string

The zfs resource for the given snapshot.

#### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

The name of the snapshot.

#### type

- Schema name: `Type`
- Type: const
- Default: "SNAPSHOT"

The type of zfs resource.

#### holds (required)

- Schema name: `Holds`

A list of tags that hold the snapshot.
##### Any of

###### Option 1

- Type: array
- No Additional Items

####### Each item of this array must be:

- Type: object

###### Option 2

- Type: null

#### properties (required)

Requested properties for the snapshot.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### user_properties (required)

- Schema name: `User Properties`

User-defined properties for snapshots.
##### Any of

###### Option 1

- Type: object
####### Additional Properties

Each additional property must conform to the following schema
- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
