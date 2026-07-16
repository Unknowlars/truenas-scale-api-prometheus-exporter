---
title: interface.lag_ports_choices
kind: method
source_rst: _sources/api_methods_interface.lag_ports_choices.rst.txt
source_html: api_methods_interface.lag_ports_choices.html
required_roles:
  - NETWORK_INTERFACE_READ | READONLY_ADMIN
---

# interface.lag_ports_choices

## Summary

Return available interface choices that can be added to a `bond` (lag) interface.

## Required Roles

- `NETWORK_INTERFACE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Default: null

Name of existing bond interface whose member interfaces should be included in the result.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: object

IDs of available interfaces that can be added to a bond interface.
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
