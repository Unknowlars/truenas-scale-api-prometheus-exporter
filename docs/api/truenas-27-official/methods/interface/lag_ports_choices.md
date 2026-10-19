---
title: interface.lag_ports_choices
kind: method
source_rst: _sources/api_methods_interface.lag_ports_choices.rst.txt
source_html: api_methods_interface.lag_ports_choices.html
required_roles:
  - NETWORK_INTERFACE_READ
  - READONLY_ADMIN
---

# interface.lag_ports_choices

## Summary

Return available interface choices that can be added to a `bond` (lag) interface.

## Required Roles

- `NETWORK_INTERFACE_READ`
- `READONLY_ADMIN`

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
- Default: null

Name of existing bond interface whose member interfaces should be included in the result.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

IDs of available interfaces that can be added to a bond interface.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
