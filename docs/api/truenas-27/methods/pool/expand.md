---
title: pool.expand
kind: method
source_rst: _sources/api_methods_pool.expand.rst.txt
source_html: api_methods_pool.expand.html
required_roles:
  - POOL_WRITE
---

# pool.expand

## Summary

Expand pool to fit all available disk space.

This method is a job.

## Required Roles

- `POOL_WRITE`

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

ID of the pool to expand.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful pool expansion initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
