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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the held snapshot to release.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for controlling snapshot release behavior.
- No Additional Properties
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively release holds on child snapshots. Only the tags that are present on the parent snapshot will be removed.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful snapshot release.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
