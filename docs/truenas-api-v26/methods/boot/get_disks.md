---
title: boot.get_disks
kind: method
source_rst: _sources/api_methods_boot.get_disks.rst.txt
source_html: api_methods_boot.get_disks.html
required_roles:
  - DISK_READ
---

# boot.get_disks

## Summary

Returns disks of the boot pool.

## Required Roles

- `DISK_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of string

Array of disk device names that are part of the boot pool.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
