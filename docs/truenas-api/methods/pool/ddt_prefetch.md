---
title: pool.ddt_prefetch
kind: method
source_rst: _sources/api_methods_pool.ddt_prefetch.rst.txt
source_html: api_methods_pool.ddt_prefetch.html
required_roles:
  - POOL_WRITE
---

# pool.ddt_prefetch

## Summary

Prefetch DDT entries in pool `pool_name`.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_name

#### pool_name

- Schema name: `pool_name`
- Type: string

Name of the pool to prefetch deduplication table entries for.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful deduplication table prefetch.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
