---
title: zfs.resource.snapshot.holds
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.holds.rst.txt
source_html: api_methods_zfs.resource.snapshot.holds.html
required_roles:
  - SNAPSHOT_READ
---

# zfs.resource.snapshot.holds

## Summary

Get holds on a ZFS snapshot.

Examples:

Get the holds on a snapshot:

.. code:: json

{"path": "tank/data@backup"}

## Required Roles

- `SNAPSHOT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Query parameters for getting holds on a ZFS snapshot.
- No Additional Properties
##### path (required)

- Schema name: `Path`
- Type: string

Snapshot path to query holds for (e.g., 'pool/dataset@snapshot').
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: array of string

List of hold tag names on the snapshot.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
