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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object

Options for filtering interface choices.
- No Additional Properties
##### bridge_members

- Schema name: `Bridge Members`
- Type: boolean
- Default: false

Include BRIDGE members.

##### lag_ports

- Schema name: `Lag Ports`
- Type: boolean
- Default: false

Include LINK_AGGREGATION ports.

##### vlan_parent

- Schema name: `Vlan Parent`
- Type: boolean
- Default: true

Include VLAN parent interface.

##### exclude

- Schema name: `Exclude`
- Type: array
- Default: ["epair", "tap", "vnet"]

Prefixes of interfaces to exclude from the result.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### exclude_types

- Schema name: `Exclude Types`
- Type: array of enum (of string)
- Default: []

Types of interfaces to exclude from the result.
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### include

- Schema name: `Include`
- Type: array of string
- Default: []

Specific interfaces to include even if they would normally be excluded.
- No Additional Items

###### Each item of this array must be:

- Type: string

### Return value

- Schema name: `Result`
- Type: object

Names and descriptions of available network interfaces.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
