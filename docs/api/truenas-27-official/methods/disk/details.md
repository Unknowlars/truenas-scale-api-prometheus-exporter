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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Disk query parameters specifying which disks to return and options.
- No Additional Properties
<a id="headingCall_parameters_items_i0_join_partitions"></a>
<a id="Call_parameters_items_i0_join_partitions"></a>
##### join_partitions

- Schema name: `Join Partitions`
- Type: boolean
- Default: false

Return all partitions currently written to disk. **NOTE: This is an expensive operation.**

<a id="headingCall_parameters_items_i0_type"></a>
<a id="Call_parameters_items_i0_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "BOTH"

`USED`: Only disks that are IN USE will be returned. `UNUSED`: Only disks that are NOT IN USE are returned. `BOTH`: Used and unused disks will be returned.
###### Must be one of:

- "USED"
- "UNUSED"
- "BOTH"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

Array of disk information or object with disk details depending on query options.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
