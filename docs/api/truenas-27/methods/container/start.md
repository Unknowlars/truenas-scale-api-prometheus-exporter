---
title: container.start
kind: method
source_rst: _sources/api_methods_container.start.rst.txt
source_html: api_methods_container.start.html
required_roles:
  - CONTAINER_WRITE
---

# container.start

## Summary

Start container.

## Required Roles

- `CONTAINER_WRITE`

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
- Type: integer

Container ID.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
