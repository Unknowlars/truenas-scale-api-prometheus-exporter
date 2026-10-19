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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`

Configuration for creating a snapshot with either an explicit name or naming schema.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [PoolSnapshotCreateWithName](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Schema name: `PoolSnapshotCreateWithName`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i0_dataset"></a>
<a id="Call_parameters_items_i0_anyOf_i0_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset to create a snapshot of.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_anyOf_i0_recursive"></a>
<a id="Call_parameters_items_i0_anyOf_i0_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingCall_parameters_items_i0_anyOf_i0_exclude"></a>
<a id="Call_parameters_items_i0_anyOf_i0_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_anyOf_i0_exclude_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_anyOf_i0_vmware_sync"></a>
<a id="Call_parameters_items_i0_anyOf_i0_vmware_sync"></a>
###### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean
- Default: false

Whether to sync VMware VMs before taking the snapshot.

<a id="headingCall_parameters_items_i0_anyOf_i0_suspend_vms"></a>
<a id="Call_parameters_items_i0_anyOf_i0_suspend_vms"></a>
###### suspend_vms

- Schema name: `Suspend Vms`
- Type: boolean
- Default: false

Temporarily suspend VMs before taking snapshot.

<a id="headingCall_parameters_items_i0_anyOf_i0_properties"></a>
<a id="Call_parameters_items_i0_anyOf_i0_properties"></a>
###### properties

- Schema name: `Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the snapshot.

<a id="headingCall_parameters_items_i0_anyOf_i0_name"></a>
<a id="Call_parameters_items_i0_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Explicit name for the snapshot.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [PoolSnapshotCreateWithSchema](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Schema name: `PoolSnapshotCreateWithSchema`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i1_dataset"></a>
<a id="Call_parameters_items_i0_anyOf_i1_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset to create a snapshot of.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_anyOf_i1_recursive"></a>
<a id="Call_parameters_items_i0_anyOf_i1_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingCall_parameters_items_i0_anyOf_i1_exclude"></a>
<a id="Call_parameters_items_i0_anyOf_i1_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_anyOf_i1_exclude_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_anyOf_i1_vmware_sync"></a>
<a id="Call_parameters_items_i0_anyOf_i1_vmware_sync"></a>
###### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean
- Default: false

Whether to sync VMware VMs before taking the snapshot.

<a id="headingCall_parameters_items_i0_anyOf_i1_suspend_vms"></a>
<a id="Call_parameters_items_i0_anyOf_i1_suspend_vms"></a>
###### suspend_vms

- Schema name: `Suspend Vms`
- Type: boolean
- Default: false

Temporarily suspend VMs before taking snapshot.

<a id="headingCall_parameters_items_i0_anyOf_i1_properties"></a>
<a id="Call_parameters_items_i0_anyOf_i1_properties"></a>
###### properties

- Schema name: `Properties`
- Type: object
- Default: {}

Object mapping ZFS property names to values to set on the snapshot.

<a id="headingCall_parameters_items_i0_anyOf_i1_naming_schema"></a>
<a id="Call_parameters_items_i0_anyOf_i1_naming_schema"></a>
###### naming_schema (required)

- Schema name: `Naming Schema`
- Type: string

Naming schema pattern to generate the snapshot name automatically.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolSnapshotCreateUpdateEntry`
- Type: object

Information about the newly created snapshot.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

<a id="headingReturn_value_properties"></a>
<a id="Return_value_properties"></a>
#### properties (required)

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
<a id="headingReturn_value_properties_additionalProperties"></a>
<a id="Return_value_properties_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
<a id="headingReturn_value_properties_additionalProperties_value"></a>
<a id="Return_value_properties_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_properties_additionalProperties_rawvalue"></a>
<a id="Return_value_properties_additionalProperties_rawvalue"></a>
###### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_properties_additionalProperties_source"></a>
<a id="Return_value_properties_additionalProperties_source"></a>
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

<a id="headingReturn_value_properties_additionalProperties_parsed"></a>
<a id="Return_value_properties_additionalProperties_parsed"></a>
###### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool (required)

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.
- Specific value: `"SNAPSHOT"`

<a id="headingReturn_value_snapshot_name"></a>
<a id="Return_value_snapshot_name"></a>
#### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

<a id="headingReturn_value_createtxg"></a>
<a id="Return_value_createtxg"></a>
#### createtxg (required)

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
