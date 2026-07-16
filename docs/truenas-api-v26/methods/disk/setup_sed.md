---
title: disk.setup_sed
kind: method
source_rst: _sources/api_methods_disk.setup_sed.rst.txt
source_html: api_methods_disk.setup_sed.html
required_roles:
  - DISK_WRITE
---

# disk.setup_sed

## Summary

Setup specified `options.name` SED disk.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: disk_sed_setup

#### disk_sed_setup

- Schema name: `disk_sed_setup`
- Type: object

DiskSetupSedArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name of disk to setup.
- Must be at least `1` characters long

##### password

- Schema name: `Password`
- Default: null

Password to use to setup the disk. If this is not set, first if a password on disk is set, it will be used else global configured SED password will be used.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: const

Returns true if the disk setup was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
