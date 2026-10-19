---
title: fcport.create
kind: method
source_rst: _sources/api_methods_fcport.create.rst.txt
source_html: api_methods_fcport.create.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fcport.create

## Summary

Creates mapping between a FC port and a target.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: fc_Port_create

<a id="Call_parameters_items_i0"></a>
#### fc_Port_create

- Schema name: `fc_Port_create`
- Type: object

Fibre Channel port configuration data for the new port.
- No Additional Properties
<a id="headingCall_parameters_items_i0_port"></a>
<a id="Call_parameters_items_i0_port"></a>
##### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+(/[1-9][0-9]*)?$`
- Must be at least `1` characters long
- Must be at most `40` characters long

<a id="headingCall_parameters_items_i0_target_id"></a>
<a id="Call_parameters_items_i0_target_id"></a>
##### target_id (required)

- Schema name: `Target Id`
- Type: integer

ID of the target to associate with this FC port.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FCPortEntry`
- Type: object

The created Fibre Channel port configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel port configuration.

<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+(/[1-9][0-9]*)?$`
- Must be at least `1` characters long
- Must be at most `40` characters long

<a id="headingReturn_value_wwpn"></a>
<a id="Return_value_wwpn"></a>
#### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
<a id="Return_value_wwpn_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_wwpn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_wwpn_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_Return_value_wwpn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_wwpn_anyOf_i1)

- Type: null

<a id="headingReturn_value_wwpn_b"></a>
<a id="Return_value_wwpn_b"></a>
#### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
<a id="Return_value_wwpn_b_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_wwpn_b_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_wwpn_b_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_Return_value_wwpn_b_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_wwpn_b_anyOf_i1)

- Type: null

<a id="headingReturn_value_target"></a>
<a id="Return_value_target"></a>
#### target (required)

- Schema name: `Target`

Target configuration object or `null` if not configured.
<a id="Return_value_target_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_target_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_target_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_target_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_target_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
