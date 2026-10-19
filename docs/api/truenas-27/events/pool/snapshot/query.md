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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `PoolSnapshotAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `PoolSnapshotEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

<a id="headingADDED_fields_properties"></a>
<a id="ADDED_fields_properties"></a>
##### properties (required)

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
<a id="headingADDED_fields_properties_additionalProperties"></a>
<a id="ADDED_fields_properties_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_properties_additionalProperties_value"></a>
<a id="ADDED_fields_properties_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

<a id="headingADDED_fields_properties_additionalProperties_rawvalue"></a>
<a id="ADDED_fields_properties_additionalProperties_rawvalue"></a>
###### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

<a id="headingADDED_fields_properties_additionalProperties_source"></a>
<a id="ADDED_fields_properties_additionalProperties_source"></a>
###### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation
###### Must be one of:

- "NONE"
- "DEFAULT"
- "LOCAL"
- "TEMPORARY"
- "INHERITED"
- "RECEIVED"

<a id="headingADDED_fields_properties_additionalProperties_parsed"></a>
<a id="ADDED_fields_properties_additionalProperties_parsed"></a>
###### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingADDED_fields_pool"></a>
<a id="ADDED_fields_pool"></a>
##### pool (required)

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.
- Specific value: `"SNAPSHOT"`

<a id="headingADDED_fields_snapshot_name"></a>
<a id="ADDED_fields_snapshot_name"></a>
##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

<a id="headingADDED_fields_createtxg"></a>
<a id="ADDED_fields_createtxg"></a>
##### createtxg (required)

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

<a id="headingADDED_fields_holds"></a>
<a id="ADDED_fields_holds"></a>
##### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.
- No Additional Properties
<a id="headingADDED_fields_holds_truenas"></a>
<a id="ADDED_fields_holds_truenas"></a>
###### truenas

- Schema name: `Truenas`
- Type: integer

Present if a hold has been placed on the snapshot.

<a id="headingADDED_fields_retention"></a>
<a id="ADDED_fields_retention"></a>
##### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
<a id="ADDED_fields_retention_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_retention_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_retention_anyOf_i0)

<a id="ADDED_fields_retention_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_ADDED_fields_retention_anyOf_i0_oneOf_i0"></a>
###### [PoolSnapshotRetentionPST](#tab-pane_ADDED_fields_retention_anyOf_i0_oneOf_i0)

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_retention_anyOf_i0_oneOf_i0_datetime"></a>
<a id="ADDED_fields_retention_anyOf_i0_oneOf_i0_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

<a id="headingADDED_fields_retention_anyOf_i0_oneOf_i0_source"></a>
<a id="ADDED_fields_retention_anyOf_i0_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.
- Specific value: `"periodic_snapshot_task"`

<a id="headingADDED_fields_retention_anyOf_i0_oneOf_i0_periodic_snapshot_task_id"></a>
<a id="ADDED_fields_retention_anyOf_i0_oneOf_i0_periodic_snapshot_task_id"></a>
###### periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

<a id="tab-pane_ADDED_fields_retention_anyOf_i0_oneOf_i1"></a>
###### [PoolSnapshotRetentionProperty](#tab-pane_ADDED_fields_retention_anyOf_i0_oneOf_i1)

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_retention_anyOf_i0_oneOf_i1_datetime"></a>
<a id="ADDED_fields_retention_anyOf_i0_oneOf_i1_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

<a id="headingADDED_fields_retention_anyOf_i0_oneOf_i1_source"></a>
<a id="ADDED_fields_retention_anyOf_i0_oneOf_i1_source"></a>
###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.
- Specific value: `"property"`

<a id="tab-pane_ADDED_fields_retention_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_retention_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `PoolSnapshotChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `PoolSnapshotEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

<a id="headingCHANGED_fields_properties"></a>
<a id="CHANGED_fields_properties"></a>
##### properties (required)

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
<a id="headingCHANGED_fields_properties_additionalProperties"></a>
<a id="CHANGED_fields_properties_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_properties_additionalProperties_value"></a>
<a id="CHANGED_fields_properties_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

<a id="headingCHANGED_fields_properties_additionalProperties_rawvalue"></a>
<a id="CHANGED_fields_properties_additionalProperties_rawvalue"></a>
###### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

<a id="headingCHANGED_fields_properties_additionalProperties_source"></a>
<a id="CHANGED_fields_properties_additionalProperties_source"></a>
###### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation
###### Must be one of:

- "NONE"
- "DEFAULT"
- "LOCAL"
- "TEMPORARY"
- "INHERITED"
- "RECEIVED"

<a id="headingCHANGED_fields_properties_additionalProperties_parsed"></a>
<a id="CHANGED_fields_properties_additionalProperties_parsed"></a>
###### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingCHANGED_fields_pool"></a>
<a id="CHANGED_fields_pool"></a>
##### pool (required)

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.
- Specific value: `"SNAPSHOT"`

<a id="headingCHANGED_fields_snapshot_name"></a>
<a id="CHANGED_fields_snapshot_name"></a>
##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

<a id="headingCHANGED_fields_createtxg"></a>
<a id="CHANGED_fields_createtxg"></a>
##### createtxg (required)

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

<a id="headingCHANGED_fields_holds"></a>
<a id="CHANGED_fields_holds"></a>
##### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.
- No Additional Properties
<a id="headingCHANGED_fields_holds_truenas"></a>
<a id="CHANGED_fields_holds_truenas"></a>
###### truenas

- Schema name: `Truenas`
- Type: integer

Present if a hold has been placed on the snapshot.

<a id="headingCHANGED_fields_retention"></a>
<a id="CHANGED_fields_retention"></a>
##### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
<a id="CHANGED_fields_retention_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_retention_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_retention_anyOf_i0)

<a id="CHANGED_fields_retention_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_CHANGED_fields_retention_anyOf_i0_oneOf_i0"></a>
###### [PoolSnapshotRetentionPST](#tab-pane_CHANGED_fields_retention_anyOf_i0_oneOf_i0)

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_retention_anyOf_i0_oneOf_i0_datetime"></a>
<a id="CHANGED_fields_retention_anyOf_i0_oneOf_i0_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

<a id="headingCHANGED_fields_retention_anyOf_i0_oneOf_i0_source"></a>
<a id="CHANGED_fields_retention_anyOf_i0_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.
- Specific value: `"periodic_snapshot_task"`

<a id="headingCHANGED_fields_retention_anyOf_i0_oneOf_i0_periodic_snapshot_task_id"></a>
<a id="CHANGED_fields_retention_anyOf_i0_oneOf_i0_periodic_snapshot_task_id"></a>
###### periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

<a id="tab-pane_CHANGED_fields_retention_anyOf_i0_oneOf_i1"></a>
###### [PoolSnapshotRetentionProperty](#tab-pane_CHANGED_fields_retention_anyOf_i0_oneOf_i1)

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_retention_anyOf_i0_oneOf_i1_datetime"></a>
<a id="CHANGED_fields_retention_anyOf_i0_oneOf_i1_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

<a id="headingCHANGED_fields_retention_anyOf_i0_oneOf_i1_source"></a>
<a id="CHANGED_fields_retention_anyOf_i0_oneOf_i1_source"></a>
###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.
- Specific value: `"property"`

<a id="tab-pane_CHANGED_fields_retention_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_retention_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `PoolSnapshotRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
