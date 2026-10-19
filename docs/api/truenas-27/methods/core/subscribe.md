---
title: core.subscribe
kind: method
source_rst: _sources/api_methods_core.subscribe.rst.txt
source_html: api_methods_core.subscribe.html
required_roles:
  []
---

# core.subscribe

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: event

<a id="Call_parameters_items_i0"></a>
#### event

- Schema name: `event`
- Type: string

Event name to subscribe to for real-time updates.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

CoreSubscribeResult return fields.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
