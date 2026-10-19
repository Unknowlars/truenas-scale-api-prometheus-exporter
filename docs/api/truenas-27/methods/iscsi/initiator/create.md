---
title: iscsi.initiator.create
kind: method
source_rst: _sources/api_methods_iscsi.initiator.create.rst.txt
source_html: api_methods_iscsi.initiator.create.html
required_roles:
  - SHARING_ISCSI_INITIATOR_WRITE
---

# iscsi.initiator.create

## Summary

Create an iSCSI Initiator.

`initiators` is a list of initiator hostnames which are authorized to access an iSCSI Target. To allow all possible initiators, `initiators` can be left empty.

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

#### Parameter 1: iscsi_initiator_create

<a id="Call_parameters_items_i0"></a>
#### iscsi_initiator_create

- Schema name: `iscsi_initiator_create`
- Type: object

Authorized initiator group configuration data for creation.
- No Additional Properties
<a id="headingCall_parameters_items_i0_initiators"></a>
<a id="Call_parameters_items_i0_initiators"></a>
##### initiators

- Schema name: `Initiators`
- Type: array of string
- Default: []

Array of iSCSI Qualified Names (IQNs) or IP addresses of authorized initiators.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_initiators_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_comment"></a>
<a id="Call_parameters_items_i0_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the authorized initiator group.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetAuthorizedInitiatorEntry`
- Type: object

The created authorized initiator group configuration.
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
