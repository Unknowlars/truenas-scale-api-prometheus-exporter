---
title: pool.reimport
kind: method
source_rst: _sources/api_methods_pool.reimport.rst.txt
source_html: api_methods_pool.reimport.html
required_roles:
  - POOL_WRITE
---

# pool.reimport

## Summary

Attempt to import a pool that exists in database but is currently OFFLINE.

This is useful after SED disks have been unlocked and the pool can now be imported.

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

ID of the pool to reimport.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful pool reimport.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
