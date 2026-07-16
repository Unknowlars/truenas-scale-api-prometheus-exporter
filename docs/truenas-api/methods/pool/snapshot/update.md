---
title: pool.snapshot.update
kind: method
source_rst: _sources/api_methods_pool.snapshot.update.rst.txt
source_html: api_methods_pool.snapshot.update.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.update

## Required Roles

- `SNAPSHOT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the snapshot to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

The property updates to apply to the snapshot.
- No Additional Properties
##### user_properties_update

- Schema name: `User Properties Update`
- Type: array of object
- Default: []

Properties to update.
- No Additional Items

###### Each item of this array must be:

###### PoolSnapshotUserPropertyUpdate

- Schema name: `PoolSnapshotUserPropertyUpdate`
- Type: object
- No Additional Properties
####### key (required)

- Schema name: `Key`
- Type: string

ZFS user property key in namespace:property format (e.g., 'custom:backup*policy', 'org:created*by').

####### value (required)

- Schema name: `Value`
- Type: string

The new value to assign to the user property.

##### user_properties_remove

- Schema name: `User Properties Remove`
- Type: array of string
- Default: []

Properties to remove.
- No Additional Items

###### Each item of this array must be:

- Type: string

ZFS user property key in namespace:property format (e.g., 'custom:backup*policy', 'org:created*by').

### Return value

- Schema name: `PoolSnapshotCreateUpdateEntry`
- Type: object

Information about the updated snapshot.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

#### properties (required)

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
###### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

###### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

###### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation

###### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

#### pool (required)

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

#### name (required)

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

#### type (required)

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.

#### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

#### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

#### createtxg (required)

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
