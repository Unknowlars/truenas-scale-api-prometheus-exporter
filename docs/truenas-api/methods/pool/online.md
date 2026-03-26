---
title: pool.online
kind: method
source_rst: _sources/api_methods_pool.online.rst.txt
source_html: api_methods_pool.online.html
required_roles:
  - POOL_WRITE
---

# pool.online

## Summary

Online a disk from pool of id `id`.

.. examples(websocket)::

Online ZFS device.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.online, "params": [1, { "label": "80802394992848654" }] }

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

ID of the pool to bring a disk online in.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Disk identifier to bring online.
- No Additional Properties
##### label (required)

- Schema name: `Label`
- Type: string

The vdev guid or device name.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful disk online operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
