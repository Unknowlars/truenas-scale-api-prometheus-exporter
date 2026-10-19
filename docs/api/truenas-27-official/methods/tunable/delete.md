---
title: tunable.delete
kind: method
source_rst: _sources/api_methods_tunable.delete.rst.txt
source_html: api_methods_tunable.delete.html
required_roles:
  - SYSTEM_TUNABLE_WRITE
---

# tunable.delete

## Summary

Delete Tunable of `id`.

This method is a job.

## Required Roles

- `SYSTEM_TUNABLE_WRITE`

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

ID of the tunable to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful tunable deletion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
