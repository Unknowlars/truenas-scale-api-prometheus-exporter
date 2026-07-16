---
title: pool.snapshot.query
kind: event
source_rst: _sources/api_events_pool.snapshot.query.rst.txt
source_html: api_events_pool.snapshot.query.html
required_roles:
  - SNAPSHOT_READ
---

# pool.snapshot.query

## Summary

Sent on pool.snapshot changes.

## Required Roles

- `SNAPSHOT_READ`

## Schema

- Type: object

### ADDED

- Schema name: `PoolSnapshotAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `PoolSnapshotEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

##### properties (required)

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
####### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

####### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

####### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation

####### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

##### pool (required)

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

##### name (required)

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

##### type (required)

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.

##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

##### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

##### createtxg (required)

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

##### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.
- No Additional Properties
###### truenas

- Schema name: `Truenas`
- Type: integer

Present if a hold has been placed on the snapshot.

##### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
###### Any of

####### Option 1

####### Option 2

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
######## datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

######## source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.

######## periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

####### PoolSnapshotRetentionPST

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
######## datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

######## source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.

####### PoolSnapshotRetentionProperty

- Type: null

### CHANGED

- Schema name: `PoolSnapshotChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `PoolSnapshotEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

##### properties (required)

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
####### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

####### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

####### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation

####### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

##### pool (required)

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

##### name (required)

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

##### type (required)

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.

##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

##### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

##### createtxg (required)

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

##### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.
- No Additional Properties
###### truenas

- Schema name: `Truenas`
- Type: integer

Present if a hold has been placed on the snapshot.

##### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
###### Any of

####### Option 1

####### Option 2

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
######## datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

######## source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.

######## periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

####### PoolSnapshotRetentionPST

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
######## datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

######## source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.

####### PoolSnapshotRetentionProperty

- Type: null

### REMOVED

- Schema name: `PoolSnapshotRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
