---
title: pool.snapshot.delete
kind: method
source_rst: _sources/api_methods_pool.snapshot.delete.rst.txt
source_html: api_methods_pool.snapshot.delete.html
required_roles:
  - SNAPSHOT_DELETE
---

# pool.snapshot.delete

## Summary

Delete the snapshot identified by `id`.

Set `recursive` to also delete identically named snapshots of child datasets. Set `defer` to request a deferred (asynchronous) destroy, which lets the snapshot be removed even while it still has holds or clones.

## Required Roles

- `SNAPSHOT_DELETE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the snapshot to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot deletion behavior.
- No Additional Properties
##### defer

- Schema name: `Defer`
- Type: boolean
- Default: false

Defer deletion of the snapshot.

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively delete child snapshots.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful snapshot deletion.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
