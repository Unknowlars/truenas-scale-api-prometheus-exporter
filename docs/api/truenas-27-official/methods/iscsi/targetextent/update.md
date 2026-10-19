---
title: iscsi.targetextent.update
kind: method
source_rst: _sources/api_methods_iscsi.targetextent.update.rst.txt
source_html: api_methods_iscsi.targetextent.update.html
required_roles:
  - SHARING_ISCSI_TARGETEXTENT_WRITE
---

# iscsi.targetextent.update

## Summary

Update Associated Target of `id`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the target-to-extent association to update.

#### Parameter 2: iscsi_target_to_extent_update

<a id="Call_parameters_items_i1"></a>
#### iscsi_target_to_extent_update

- Schema name: `iscsi_target_to_extent_update`
- Type: object

Updated target-to-extent association configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_id"></a>
<a id="Call_parameters_items_i1_id"></a>
##### id

- Schema name: `Id`
- Type: integer

Unique identifier for the target-to-extent association.

<a id="headingCall_parameters_items_i1_target"></a>
<a id="Call_parameters_items_i1_target"></a>
##### target

- Schema name: `Target`
- Type: integer

ID of the iSCSI target to associate with the extent.

<a id="headingCall_parameters_items_i1_lunid"></a>
<a id="Call_parameters_items_i1_lunid"></a>
##### lunid

- Schema name: `Lunid`
- Type: integer

Logical Unit Number (LUN) ID for presenting the extent to the target.

<a id="headingCall_parameters_items_i1_extent"></a>
<a id="Call_parameters_items_i1_extent"></a>
##### extent

- Schema name: `Extent`
- Type: integer

ID of the iSCSI extent to associate with the target.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetToExtentEntry`
- Type: object

The updated target-to-extent association.
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
