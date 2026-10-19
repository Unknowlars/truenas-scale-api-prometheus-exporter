---
title: system.feature_enabled
kind: method
source_rst: _sources/api_methods_system.feature_enabled.rst.txt
source_html: api_methods_system.feature_enabled.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# system.feature_enabled

## Summary

Returns whether the `feature` is enabled or not

*DEPRECATED: this method is scheduled to be removed in v26.*

## Required Roles

- `SYSTEM_PRODUCT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: feature

<a id="Call_parameters_items_i0"></a>
#### feature

- Schema name: `feature`
- Type: string

Feature to check for availability on this system. A feature this system does not recognize or does not gate is reported as available.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Whether the specified feature is enabled on this system.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
