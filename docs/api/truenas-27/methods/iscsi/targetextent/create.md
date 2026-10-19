---
title: iscsi.targetextent.create
kind: method
source_rst: _sources/api_methods_iscsi.targetextent.create.rst.txt
source_html: api_methods_iscsi.targetextent.create.html
required_roles:
  - SHARING_ISCSI_TARGETEXTENT_WRITE
---

# iscsi.targetextent.create

## Summary

Create an Associated Target.

`lunid` will be automatically assigned if it is not provided based on the `target`.

## Required Roles

- `SHARING_ISCSI_TARGETEXTENT_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: iscsi_target_to_extent_create

<a id="Call_parameters_items_i0"></a>
#### iscsi_target_to_extent_create

- Schema name: `iscsi_target_to_extent_create`
- Type: object

Target-to-extent association configuration data for creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_target"></a>
<a id="Call_parameters_items_i0_target"></a>
##### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

<a id="headingCall_parameters_items_i0_lunid"></a>
<a id="Call_parameters_items_i0_lunid"></a>
##### lunid

- Schema name: `Lunid`
- Default: null

LUN ID to assign or `null` to auto-assign the next available LUN.
<a id="Call_parameters_items_i0_lunid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_lunid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_lunid_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_lunid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_lunid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_extent"></a>
<a id="Call_parameters_items_i0_extent"></a>
##### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetToExtentEntry`
- Type: object

The created target-to-extent association.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

<a id="headingReturn_value_target"></a>
<a id="Return_value_target"></a>
#### target (required)

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

<a id="headingReturn_value_lunid"></a>
<a id="Return_value_lunid"></a>
#### lunid (required)

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

<a id="headingReturn_value_extent"></a>
<a id="Return_value_extent"></a>
#### extent (required)

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
