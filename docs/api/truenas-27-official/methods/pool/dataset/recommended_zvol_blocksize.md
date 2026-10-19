---
title: pool.dataset.recommended_zvol_blocksize
kind: method
source_rst: _sources/api_methods_pool.dataset.recommended_zvol_blocksize.rst.txt
source_html: api_methods_pool.dataset.recommended_zvol_blocksize.html
required_roles:
  - DATASET_READ
---

# pool.dataset.recommended_zvol_blocksize

## Summary

Helper method to get recommended size for a new zvol (dataset of type VOLUME).

Get blocksize for pool "tank"::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.dataset.recommended_zvol_blocksize", "params": ["tank"] }

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool

<a id="Call_parameters_items_i0"></a>
#### pool

- Schema name: `pool`
- Type: string

The pool name to get the recommended volume block size for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

The recommended block size for volumes on this pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
