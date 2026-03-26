---
title: pool.detach
kind: method
source_rst: _sources/api_methods_pool.detach.rst.txt
source_html: api_methods_pool.detach.html
required_roles:
  - POOL_WRITE
---

# pool.detach

## Summary

Detach a disk from pool of id `id`.

.. examples(websocket)::

Detach ZFS device.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.detach, "params": [1, { "label": "80802394992848654" }] }

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

ID of the pool to detach a disk from.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Configuration for the disk detachment operation.
- No Additional Properties
##### label (required)

- Schema name: `Label`
- Type: string

GUID or device name of the vdev to detach.

##### wipe

- Schema name: `Wipe`
- Type: boolean
- Default: false

Whether to wipe the detached disk after removal.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful disk detachment.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
