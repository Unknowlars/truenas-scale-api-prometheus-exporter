---
title: disk.temperatures
kind: method
source_rst: _sources/api_methods_disk.temperatures.rst.txt
source_html: api_methods_disk.temperatures.html
required_roles:
  - REPORTING_READ
---

# disk.temperatures

## Summary

Returns disk temperatures for disks in degrees celsius.

NOTE: Disk temperatures are not retrieved more than once every 5 minutes.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: array of string

List of names of disks to retrieve temperature information. Name should be in the form of "sda", "nvme0n1", etc.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### Parameter 2: include_thresholds

#### include_thresholds

- Schema name: `include_thresholds`
- Type: boolean
- Default: false

Include the temperature thresholds as reported by the disk (i.e. the critical temp).

### Return value

- Schema name: `Result`
- Type: object

Object mapping disk names to their current temperature information.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
