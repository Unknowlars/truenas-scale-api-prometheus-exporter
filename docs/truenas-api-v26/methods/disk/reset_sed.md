---
title: disk.reset_sed
kind: method
source_rst: _sources/api_methods_disk.reset_sed.rst.txt
source_html: api_methods_disk.reset_sed.html
required_roles:
  - DISK_WRITE
---

# disk.reset_sed

## Summary

Reset SED disk.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: disk_sed_reset

#### disk_sed_reset

- Schema name: `disk_sed_reset`
- Type: object

DiskResetSedArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name of disk to reset.
- Must be at least `1` characters long

##### psid (required)

- Schema name: `Psid`
- Type: string

PID of disk to reset.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: const

Returns true if the disk reset was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
