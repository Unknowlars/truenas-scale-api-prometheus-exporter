---
title: disk.unlock_sed
kind: method
source_rst: _sources/api_methods_disk.unlock_sed.rst.txt
source_html: api_methods_disk.unlock_sed.html
required_roles:
  - DISK_WRITE
---

# disk.unlock_sed

## Summary

Unlock specified `options.name` SED disk.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: disk_sed_unlock

#### disk_sed_unlock

- Schema name: `disk_sed_unlock`
- Type: object

DiskUnlockSedArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name of disk to unlock.
- Must be at least `1` characters long

##### password

- Schema name: `Password`
- Default: null

Password for disk to unlock.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: const

Returns true if the disk unlock was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
