---
title: pool.snapshot.release
kind: method
source_rst: _sources/api_methods_pool.snapshot.release.rst.txt
source_html: api_methods_pool.snapshot.release.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.release

## Summary

Release hold on snapshot `id`.

Remove all hold tags from the specified snapshot.

## Required Roles

- `SNAPSHOT_WRITE`

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
- Type: string

ID of the held snapshot to release.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot release behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively release holds on child snapshots. Only the tags that are present on the parent snapshot will be removed.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful snapshot release.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
