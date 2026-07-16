---
title: pool.is_upgraded
kind: method
source_rst: _sources/api_methods_pool.is_upgraded.rst.txt
source_html: api_methods_pool.is_upgraded.html
required_roles:
  - POOL_READ
---

# pool.is_upgraded

## Summary

Returns whether or not the pool of `id` is on the latest version and with all feature flags enabled.

.. examples(websocket)::

Check if pool of id 1 is upgraded.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.is_upgraded", "params": [1] }

## Required Roles

- `POOL_READ`

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

ID of the pool to check upgrade status for.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the pool has been upgraded to the latest feature flags.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
