---
title: pool.replace
kind: method
source_rst: _sources/api_methods_pool.replace.rst.txt
source_html: api_methods_pool.replace.html
required_roles:
  - POOL_WRITE
---

# pool.replace

## Summary

Replace a disk on a pool.

`label` is the ZFS guid or a device name `disk` is the identifier of a disk If `preserve_settings` is true, then settings (power management, S.M.A.R.T., etc.) of a disk being replaced will be applied to a new disk.

.. examples(websocket)::

Replace missing ZFS device with disk {serial}FOO.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.replace", "params": [1, { "label": "80802394992848654", "disk": "{serial}FOO" }] }

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

ID of the pool to replace a disk in.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Configuration for the disk replacement operation.
- No Additional Properties
##### label (required)

- Schema name: `Label`
- Type: string

GUID or device name of the disk to replace.

##### disk (required)

- Schema name: `Disk`
- Type: string

Name of the new disk to use as replacement.

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force the replacement even if the new disk appears to be in use.

##### preserve_settings

- Schema name: `Preserve Settings`
- Type: boolean
- Default: true

Whether to preserve disk settings from the replaced disk.

##### preserve_description

- Schema name: `Preserve Description`
- Type: boolean
- Default: true

Whether to preserve the description from the replaced disk.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful disk replacement initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
