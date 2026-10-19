---
title: pool.dataset.promote
kind: method
source_rst: _sources/api_methods_pool.dataset.promote.rst.txt
source_html: api_methods_pool.dataset.promote.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.promote

## Summary

Promote a cloned dataset.

## Required Roles

- `DATASET_WRITE`

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
- Type: string

The clone dataset ID (full path) to promote to become the parent.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful clone promotion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
