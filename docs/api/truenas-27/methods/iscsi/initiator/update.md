---
title: iscsi.initiator.update
kind: method
source_rst: _sources/api_methods_iscsi.initiator.update.rst.txt
source_html: api_methods_iscsi.initiator.update.html
required_roles:
  - SHARING_ISCSI_INITIATOR_WRITE
---

# iscsi.initiator.update

## Summary

Update iSCSI initiator of `id`.

## Required Roles

- `SHARING_ISCSI_INITIATOR_WRITE`

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

ID of the authorized initiator group to update.

#### Parameter 2: iscsi_initiator_update

<a id="Call_parameters_items_i1"></a>
#### iscsi_initiator_update

- Schema name: `iscsi_initiator_update`
- Type: object

Updated authorized initiator group configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_id"></a>
<a id="Call_parameters_items_i1_id"></a>
##### id

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

<a id="headingCall_parameters_items_i1_initiators"></a>
<a id="Call_parameters_items_i1_initiators"></a>
##### initiators

- Schema name: `Initiators`
- Type: array of string

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_initiators_items"></a>
- Type: string

<a id="headingCall_parameters_items_i1_comment"></a>
<a id="Call_parameters_items_i1_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string

Optional comment describing the authorized initiator group.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetAuthorizedInitiatorEntry`
- Type: object

The updated authorized initiator group configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the authorized initiator group.

<a id="headingReturn_value_initiators"></a>
<a id="Return_value_initiators"></a>
#### initiators

- Schema name: `Initiators`
- Type: array of string
- Default: []

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_initiators_items"></a>
- Type: string

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the authorized initiator group.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
