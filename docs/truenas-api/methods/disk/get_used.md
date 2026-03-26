---
title: disk.get_used
kind: method
source_rst: _sources/api_methods_disk.get_used.rst.txt
source_html: api_methods_disk.get_used.html
required_roles:
  - REPORTING_READ
---

# disk.get_used

## Summary

Return disks that are in use by any zpool that is currently imported. It will also return disks that are in use by any zpool that is exported.

`join_partitions`: Bool, when True will return all partitions currently written to disk NOTE: this is an expensive operation

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: join_partitions

#### join_partitions

- Schema name: `join_partitions`
- Type: boolean
- Default: false

Return all partitions currently written to disk. **NOTE: this is an expensive operation.**

### Return value

- Schema name: `Result`
- Type: array

Array of disks that are currently in use by the system.
- No Additional Items

#### Each item of this array must be:

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
