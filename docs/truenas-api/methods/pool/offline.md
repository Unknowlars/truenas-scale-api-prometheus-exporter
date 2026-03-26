---
title: pool.offline
kind: method
source_rst: _sources/api_methods_pool.offline.rst.txt
source_html: api_methods_pool.offline.html
required_roles:
  - POOL_WRITE
---

# pool.offline

## Summary

Offline a disk from pool of id `id`.

.. examples(websocket)::

Offline ZFS device.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.offline, "params": [1, { "label": "80802394992848654" }] }

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

ID of the pool to modify.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Disk identifier to take offline.
- No Additional Properties
##### label (required)

- Schema name: `Label`
- Type: string

The vdev guid or device name.

### Return value

- Schema name: `Result`
- Type: const

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
