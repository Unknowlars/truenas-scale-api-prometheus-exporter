---
title: interface.vlan_parent_interface_choices
kind: method
source_rst: _sources/api_methods_interface.vlan_parent_interface_choices.rst.txt
source_html: api_methods_interface.vlan_parent_interface_choices.html
required_roles:
  - NETWORK_INTERFACE_READ
  - READONLY_ADMIN
---

# interface.vlan_parent_interface_choices

## Summary

Return available interface choices for `vlan_parent_interface` attribute.

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

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Names and descriptions of available interfaces for `vlan_parent_interface` attribute.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
