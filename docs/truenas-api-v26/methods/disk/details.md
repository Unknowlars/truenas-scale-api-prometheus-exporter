---
title: disk.details
kind: method
source_rst: _sources/api_methods_disk.details.rst.txt
source_html: api_methods_disk.details.html
required_roles:
  - REPORTING_READ
---

# disk.details

## Summary

Return detailed information for all disks on the system.

## Required Roles

- `REPORTING_READ`

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

Disk query parameters specifying which disks to return and options.
- No Additional Properties
##### join_partitions

- Schema name: `Join Partitions`
- Type: boolean
- Default: false

Return all partitions currently written to disk. **NOTE: This is an expensive operation.**

##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "BOTH"

`USED`: Only disks that are IN USE will be returned. `UNUSED`: Only disks that are NOT IN USE are returned. `BOTH`: Used and unused disks will be returned.

### Return value

- Schema name: `Result`

Array of disk information or object with disk details depending on query options.
#### Any of

##### Option 1

- Type: array
- No Additional Items

###### Each item of this array must be:

- Type: object

##### Option 2

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
