---
title: pool.get_disks
kind: method
source_rst: _sources/api_methods_pool.get_disks.rst.txt
source_html: api_methods_pool.get_disks.html
required_roles:
  - POOL_READ
---

# pool.get_disks

## Summary

Return the device names of all disks belonging to a pool.

Queries the database for the pool matching the given `id` and resolves each vdev, cache, log, special, dedup, and spare device to its whole-disk device name (e.g. sda, nvme0n1). If `id` is not provided, disks for all imported pools in the database are returned. Pools that are not currently imported are skipped.

Raises a `ValidationError` if `id` is provided but does not match any pool in the database.

## Required Roles

- `POOL_READ`

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
- Default: null

ID of the pool to get disks for. If `null`, returns disks from all pools.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of string

Array of disk device names used in the specified pool(s).
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
