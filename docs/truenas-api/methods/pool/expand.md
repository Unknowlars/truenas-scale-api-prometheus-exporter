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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the pool to expand.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful pool expansion initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
