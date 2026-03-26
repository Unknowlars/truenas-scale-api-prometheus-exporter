---
title: pool.snapshot.hold
kind: method
source_rst: _sources/api_methods_pool.snapshot.hold.rst.txt
source_html: api_methods_pool.snapshot.hold.html
required_roles:
  - SNAPSHOT_WRITE
---

# pool.snapshot.hold

## Summary

Hold snapshot `id`.

Add `truenas` tag to the snapshot's tag namespace.

## Required Roles

- `SNAPSHOT_WRITE`

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

ID of the snapshot to hold.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot hold behavior.
- No Additional Properties
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Hold snapshots recursively.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful snapshot hold.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
