---
title: interface.choices
kind: method
source_rst: _sources/api_methods_interface.choices.rst.txt
source_html: api_methods_interface.choices.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.choices

## Summary

Choices of available network interfaces.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object

Options for filtering interface choices.
- No Additional Properties
<a id="headingCall_parameters_items_i0_bridge_members"></a>
<a id="Call_parameters_items_i0_bridge_members"></a>
##### bridge_members

- Schema name: `Bridge Members`
- Type: boolean
- Default: false

Include BRIDGE members.

<a id="headingCall_parameters_items_i0_lag_ports"></a>
<a id="Call_parameters_items_i0_lag_ports"></a>
##### lag_ports

- Schema name: `Lag Ports`
- Type: boolean
- Default: false

Include LINK_AGGREGATION ports.

<a id="headingCall_parameters_items_i0_vlan_parent"></a>
<a id="Call_parameters_items_i0_vlan_parent"></a>
##### vlan_parent

- Schema name: `Vlan Parent`
- Type: boolean
- Default: true

Include VLAN parent interface.

<a id="headingCall_parameters_items_i0_exclude"></a>
<a id="Call_parameters_items_i0_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array
- Default: ["epair", "tap", "vnet"]

Prefixes of interfaces to exclude from the result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_exclude_items"></a>
- Type: object

<a id="headingCall_parameters_items_i0_exclude_types"></a>
<a id="Call_parameters_items_i0_exclude_types"></a>
##### exclude_types

- Schema name: `Exclude Types`
- Type: array of enum (of string)
- Default: []

Types of interfaces to exclude from the result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_exclude_types_items"></a>
- Type: enum (of string)
###### Must be one of:

- "BRIDGE"
- "LINK_AGGREGATION"
- "PHYSICAL"
- "UNKNOWN"
- "VLAN"

<a id="headingCall_parameters_items_i0_include"></a>
<a id="Call_parameters_items_i0_include"></a>
##### include

- Schema name: `Include`
- Type: array of string
- Default: []

Specific interfaces to include even if they would normally be excluded.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_include_items"></a>
- Type: string

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Names and descriptions of available network interfaces.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
