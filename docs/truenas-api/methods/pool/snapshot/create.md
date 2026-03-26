---
title: pool.snapshot.create
kind: method
source_rst: _sources/api_methods_pool.snapshot.create.rst.txt
source_html: api_methods_pool.snapshot.create.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.create

## Summary

Take a snapshot from a given dataset.

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

Configuration for creating a snapshot with either an explicit name or naming schema.
##### Any of

###### PoolSnapshotCreateWithName

- Schema name: `PoolSnapshotCreateWithName`
- Type: object
- No Additional Properties
####### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset to create a snapshot of.
- Must be at least `1` characters long

####### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

####### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean
- Default: false

Whether to sync VMware VMs before taking the snapshot.

####### properties

- Schema name: `Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the snapshot.

####### name (required)

- Schema name: `Name`
- Type: string

Explicit name for the snapshot.
- Must be at least `1` characters long

###### PoolSnapshotCreateWithSchema

- Schema name: `PoolSnapshotCreateWithSchema`
- Type: object
- No Additional Properties
####### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset to create a snapshot of.
- Must be at least `1` characters long

####### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

####### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean
- Default: false

Whether to sync VMware VMs before taking the snapshot.

####### properties

- Schema name: `Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the snapshot.

####### naming_schema (required)

- Schema name: `Naming Schema`
- Type: string

Naming schema pattern to generate the snapshot name automatically.
- Must be at least `1` characters long

### Return value

- Schema name: `PoolSnapshotCreateUpdateEntry`
- Type: object

Information about the newly created snapshot.
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
