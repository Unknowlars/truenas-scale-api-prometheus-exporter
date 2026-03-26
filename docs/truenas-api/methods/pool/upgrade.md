---
title: pool.upgrade
kind: method
source_rst: _sources/api_methods_pool.upgrade.rst.txt
source_html: api_methods_pool.upgrade.html
required_roles:
  - POOL_WRITE
---

# pool.upgrade

## Summary

Upgrade pool of `id` to latest version with all feature flags.

.. examples(websocket)::

Upgrade pool of id 1.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.upgrade", "params": [1] }

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

ID of the pool to upgrade to the latest feature flags.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful pool upgrade.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
