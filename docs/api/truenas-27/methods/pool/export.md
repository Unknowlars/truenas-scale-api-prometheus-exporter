---
title: pool.export
kind: method
source_rst: _sources/api_methods_pool.export.rst.txt
source_html: api_methods_pool.export.html
required_roles:
  - POOL_WRITE
---

# pool.export

## Summary

Export pool of `id`.

`cascade` will delete all attachments of the given pool (`pool.attachments`). `restart_services` will restart services that have open files on given pool. `destroy` will also PERMANENTLY destroy the pool/data.

.. examples(websocket)::

Export pool of id 1.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.export, "params": [1, { "cascade": true, "destroy": false }] }

If this is an HA system and failover is enabled and the last zpool is exported/disconnected, then this will raise EOPNOTSUPP. Failover must be disabled before exporting the last zpool on the system.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the pool to export.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling the pool export process.
- No Additional Properties
<a id="headingCall_parameters_items_i1_cascade"></a>
<a id="Call_parameters_items_i1_cascade"></a>
##### cascade

- Schema name: `Cascade`
- Type: boolean
- Default: false

Delete all attachments of the given pool (`pool.attachments`).

<a id="headingCall_parameters_items_i1_restart_services"></a>
<a id="Call_parameters_items_i1_restart_services"></a>
##### restart_services

- Schema name: `Restart Services`
- Type: boolean
- Default: false

Restart services that have open files on given pool.

<a id="headingCall_parameters_items_i1_destroy"></a>
<a id="Call_parameters_items_i1_destroy"></a>
##### destroy

- Schema name: `Destroy`
- Type: boolean
- Default: false

PERMANENTLY destroy the pool/data.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful pool export.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
