---
title: pool.snapshot.update
kind: method
source_rst: _sources/api_methods_pool.snapshot.update.rst.txt
source_html: api_methods_pool.snapshot.update.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.update

## Summary

Update the user properties of the snapshot identified by `snap_id`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

ID of the snapshot to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

The property updates to apply to the snapshot.
- No Additional Properties
<a id="headingCall_parameters_items_i1_user_properties_update"></a>
<a id="Call_parameters_items_i1_user_properties_update"></a>
##### user_properties_update

- Schema name: `User Properties Update`
- Type: array of object
- Default: []

Properties to update.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_user_properties_update_items"></a>
###### PoolSnapshotUserPropertyUpdate

- Schema name: `PoolSnapshotUserPropertyUpdate`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_user_properties_update_items_key"></a>
<a id="Call_parameters_items_i1_user_properties_update_items_key"></a>
###### key (required)

- Schema name: `Key`
- Type: string

The property name in namespace:property format.
- Must match regular expression: `.*:.*`

<a id="headingCall_parameters_items_i1_user_properties_update_items_value"></a>
<a id="Call_parameters_items_i1_user_properties_update_items_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

The new value to assign to the user property.
- Must be at most `2147483647` characters long

<a id="headingCall_parameters_items_i1_user_properties_remove"></a>
<a id="Call_parameters_items_i1_user_properties_remove"></a>
##### user_properties_remove

- Schema name: `User Properties Remove`
- Type: array of string
- Default: []

Properties to remove.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_user_properties_remove_items"></a>
- Type: string

ZFS user property key in namespace:property format (e.g., 'custom:backup*policy', 'org:created*by').
- Must match regular expression: `.*:.*`

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolSnapshotCreateUpdateEntry`
- Type: object

Information about the updated snapshot.
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
