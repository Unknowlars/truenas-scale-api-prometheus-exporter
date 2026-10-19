---
title: fc.fc_host.create
kind: method
source_rst: _sources/api_methods_fc.fc_host.create.rst.txt
source_html: api_methods_fc.fc_host.create.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# fc.fc_host.create

## Summary

Create an FC host (pairing).

This associates an `alias` with a corresponding Fibre Channel WWPN. For HA systems, the alias is associated with a pair of WWPNs, one per node.

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

#### Parameter 1: fc_host_create

<a id="Call_parameters_items_i0"></a>
#### fc_host_create

- Schema name: `fc_host_create`
- Type: object

Fibre Channel host configuration data for the new host.
- No Additional Properties
<a id="headingCall_parameters_items_i0_alias"></a>
<a id="Call_parameters_items_i0_alias"></a>
##### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+$`
- Must be at least `1` characters long
- Must be at most `32` characters long

<a id="headingCall_parameters_items_i0_wwpn"></a>
<a id="Call_parameters_items_i0_wwpn"></a>
##### wwpn

- Schema name: `Wwpn`
- Default: null

World Wide Port Name for port A or `null` if not configured.
<a id="Call_parameters_items_i0_wwpn_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_wwpn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_wwpn_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_Call_parameters_items_i0_wwpn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_wwpn_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_wwpn_b"></a>
<a id="Call_parameters_items_i0_wwpn_b"></a>
##### wwpn_b

- Schema name: `Wwpn B`
- Default: null

World Wide Port Name for port B or `null` if not configured.
<a id="Call_parameters_items_i0_wwpn_b_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_wwpn_b_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_wwpn_b_anyOf_i0)

- Type: string
- Must match regular expression: `^naa.[0-9a-fA-F]{16}$`

<a id="tab-pane_Call_parameters_items_i0_wwpn_b_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_wwpn_b_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_npiv"></a>
<a id="Call_parameters_items_i0_npiv"></a>
##### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FCHostEntry`
- Type: object

The created Fibre Channel host configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel host configuration.

<a id="headingReturn_value_alias"></a>
<a id="Return_value_alias"></a>
#### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must match regular expression: `^[a-zA-Z0-9,\-_:]+$`
- Must be at least `1` characters long
- Must be at most `32` characters long

<a id="headingReturn_value_wwpn"></a>
<a id="Return_value_wwpn"></a>
#### wwpn

- Schema name: `Wwpn`
- Default: null

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
#### wwpn_b

- Schema name: `Wwpn B`
- Default: null

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

<a id="headingReturn_value_npiv"></a>
<a id="Return_value_npiv"></a>
#### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
