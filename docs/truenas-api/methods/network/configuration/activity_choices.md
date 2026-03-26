---
title: network.configuration.activity_choices
kind: method
source_rst: _sources/api_methods_network.configuration.activity_choices.rst.txt
source_html: api_methods_network.configuration.activity_choices.html
required_roles:
  - NETWORK_GENERAL_READ | READONLY_ADMIN
---

# network.configuration.activity_choices

## Summary

Returns allowed/forbidden network activity choices.

## Required Roles

- `NETWORK_GENERAL_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of array

Array of available network activity choices for filtering.
- No Additional Items

#### Each item of this array must be:

- Type: array of string
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
