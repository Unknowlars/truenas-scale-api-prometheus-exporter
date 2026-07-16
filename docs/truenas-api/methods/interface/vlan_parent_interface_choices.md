---
title: interface.vlan_parent_interface_choices
kind: method
source_rst: _sources/api_methods_interface.vlan_parent_interface_choices.rst.txt
source_html: api_methods_interface.vlan_parent_interface_choices.html
required_roles:
  - NETWORK_INTERFACE_READ | READONLY_ADMIN
---

# interface.vlan_parent_interface_choices

## Summary

Return available interface choices for `vlan_parent_interface` attribute.

## Required Roles

- `NETWORK_INTERFACE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: object

Names and descriptions of available interfaces for `vlan_parent_interface` attribute.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
