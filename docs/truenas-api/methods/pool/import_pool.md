---
title: pool.import_pool
kind: method
source_rst: _sources/api_methods_pool.import_pool.rst.txt
source_html: api_methods_pool.import_pool.html
required_roles:
  - POOL_WRITE
---

# pool.import_pool

## Summary

Import a pool found with `pool.import_find`.

Errors: ENOENT - Pool not found

.. examples(websocket)::

Import pool of guid 5571830764813710860.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.import_pool, "params": [{ "guid": "5571830764813710860" }] }

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_import

#### pool_import

- Schema name: `pool_import`
- Type: object

PoolImportPoolArgs parameters.
- No Additional Properties
##### guid (required)

- Schema name: `Guid`
- Type: string

GUID of the pool to import.

##### name

- Schema name: `Name`
- Default: null

If specified, import the pool using this name.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long
- Must be at most `50` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: const

Indicates successful pool import.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
