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

.. examples(websocket)::

Get blocksize for pool "tank".

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.dataset.recommended_zvol_blocksize", "params": ["tank"] }

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool

#### pool

- Schema name: `pool`
- Type: string

The pool name to get the recommended volume block size for.

### Return value

- Schema name: `Result`
- Type: string

The recommended block size for volumes on this pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
