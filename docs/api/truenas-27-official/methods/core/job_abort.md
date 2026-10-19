---
title: core.job_abort
kind: method
source_rst: _sources/api_methods_core.job_abort.rst.txt
source_html: api_methods_core.job_abort.html
required_roles:
  []
---

# core.job_abort

## Summary

Abort the running job identified by `id`.

Only jobs the caller is authorized to abort may be aborted.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the job to abort.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the job is successfully aborted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
