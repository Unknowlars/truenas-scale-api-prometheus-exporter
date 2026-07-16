---
title: pool.remove
kind: method
source_rst: _sources/api_methods_pool.remove.rst.txt
source_html: api_methods_pool.remove.html
required_roles:
  - POOL_WRITE
---

# pool.remove

## Summary

Remove a disk from pool of id `id`.

`label` is the vdev guid or device name.

Error codes:

EZFS_NOSPC(2032): out of space to remove a device EZFS_NODEVICE(2017): no such device in pool EZFS_NOREPLICAS(2019): no valid replicas

.. examples(websocket)::

Remove ZFS device.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.remove, "params": [1, { "label": "80802394992848654" }] }

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

ID of the pool to remove a disk from.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Disk identifier to remove from the pool.
- No Additional Properties
##### label (required)

- Schema name: `Label`
- Type: string

The vdev guid or device name.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful disk removal.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
