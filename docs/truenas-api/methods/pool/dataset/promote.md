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

Promote the cloned dataset `id`.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The clone dataset ID (full path) to promote to become the parent.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful clone promotion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
