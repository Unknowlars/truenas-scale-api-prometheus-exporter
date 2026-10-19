---
title: system.product_type
kind: method
source_rst: _sources/api_methods_system.product_type.rst.txt
source_html: api_methods_system.product_type.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# system.product_type

## Summary

Returns the type of the product.

*DEPRECATED: this method is scheduled to be removed in v27.*

## Required Roles

- `SYSTEM_PRODUCT_READ`

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
- Type: enum (of string)

Product type of this TrueNAS system.
#### Must be one of:

- "COMMUNITY_EDITION"
- "ENTERPRISE"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
