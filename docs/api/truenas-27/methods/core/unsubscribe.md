---
title: core.unsubscribe
kind: method
source_rst: _sources/api_methods_core.unsubscribe.rst.txt
source_html: api_methods_core.unsubscribe.html
required_roles:
  []
---

# core.unsubscribe

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

#### Parameter 1: id_

<a id="Call_parameters_items_i0"></a>
#### id_

- Schema name: `id_`
- Type: string

Subscription ID to cancel.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

CoreUnsubscribeResult return fields.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
