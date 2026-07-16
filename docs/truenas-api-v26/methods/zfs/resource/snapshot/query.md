---
title: zfs.resource.snapshot.query
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.query.rst.txt
source_html: api_methods_zfs.resource.snapshot.query.html
required_roles:
  - SNAPSHOT_READ
---

# zfs.resource.snapshot.query

## Summary

Retrieve information about ZFS snapshots, including their properties and user properties.

Examples:

Query all snapshots:

.. code:: json

{}

Query snapshots for a specific dataset:

.. code:: json

{"paths": ["tank/data"]}

Query a specific snapshot:

.. code:: json

{"paths": ["tank/data@backup"]}

Query with recursion and specific properties:

.. code:: json

{"paths": ["tank"], "recursive": true, "properties": ["used", "referenced", "creation"]}

## Required Roles

- `SNAPSHOT_READ`

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
- Default:
```json
{
  "paths": [],
  "recursive": false,
  "properties": [],
  "get_user_properties": false,
  "get_source": false,
  "get_holds": false,
  "min_txg": 0,
  "max_txg": 0
}
```

Query parameters for retrieving ZFS snapshot information.
- No Additional Properties
##### paths

- Schema name: `Paths`
- Type: array of string
- Default: []

Dataset paths to count snapshots for. If empty, counts all snapshots.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

- Type: string

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Include snapshots from child datasets when counting.

##### properties

- Schema name: `Properties`
- Default: []

List of ZFS properties to retrieve. Empty list returns default properties. None returns no properties.
###### Any of

####### Option 1

- Type: array of string
- No Additional Items

######## Each item of this array must be:

- Type: string

####### Option 2

- Type: null

##### get_user_properties

- Schema name: `Get User Properties`
- Type: boolean
- Default: false

Retrieve user-defined properties for snapshots.

##### get_source

- Schema name: `Get Source`
- Type: boolean
- Default: false

Include source information for each property value.

##### get_holds

- Schema name: `Get Holds`
- Type: boolean
- Default: false

Include holds information (if any) for the snapshot.

##### min_txg

- Schema name: `Min Txg`
- Type: integer
- Default: 0

Minimum transaction group for filtering snapshots. 0 means no minimum.

##### max_txg

- Schema name: `Max Txg`
- Type: integer
- Default: 0

Maximum transaction group for filtering snapshots. 0 means no maximum.

### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

#### ZFSResourceSnapshotEntry

- Schema name: `ZFSResourceSnapshotEntry`
- Type: object
- No Additional Properties
##### createtxg (required)

- Schema name: `Createtxg`
- Type: integer

The TXG in which the snapshot was created.

##### guid (required)

- Schema name: `Guid`
- Type: integer

A GUID for the snapshot.

##### name (required)

- Schema name: `Name`
- Type: string

The zfs resource for the given snapshot.

##### pool (required)

- Schema name: `Pool`
- Type: string

The zpool of the snapshot.

##### dataset (required)

- Schema name: `Dataset`
- Type: string

The zfs resource for the given snapshot.

##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

The name of the snapshot.

##### type

- Schema name: `Type`
- Type: const
- Default: "SNAPSHOT"

The type of zfs resource.

##### holds (required)

- Schema name: `Holds`

A list of tags that hold the snapshot.
###### Any of

####### Option 1

- Type: array
- No Additional Items

######## Each item of this array must be:

- Type: object

####### Option 2

- Type: null

##### properties (required)

Requested properties for the snapshot.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### user_properties (required)

- Schema name: `User Properties`

User-defined properties for snapshots.
###### Any of

####### Option 1

- Type: object
######## Additional Properties

Each additional property must conform to the following schema
- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../../shared/query_methods.md)
