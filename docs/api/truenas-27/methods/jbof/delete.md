---
title: jbof.delete
kind: method
source_rst: _sources/api_methods_jbof.delete.rst.txt
source_html: api_methods_jbof.delete.html
required_roles:
  - JBOF_WRITE
---

# jbof.delete

## Summary

Delete a JBOF by ID.

## Required Roles

- `JBOF_WRITE`

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

ID of the JBOF to delete.

#### Parameter 2: force

<a id="Call_parameters_items_i1"></a>
#### force

- Schema name: `force`
- Type: boolean
- Default: false

Whether to force deletion even if the JBOF is in use.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the JBOF is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
