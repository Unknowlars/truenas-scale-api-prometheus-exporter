---
title: pool.filesystem_choices
kind: method
source_rst: _sources/api_methods_pool.filesystem_choices.rst.txt
source_html: api_methods_pool.filesystem_choices.html
required_roles:
  - DATASET_READ
  - POOL_READ
  - READONLY_ADMIN
---

# pool.filesystem_choices

## Summary

Returns all available zfs resources based on `types`.

## Required Roles

- `DATASET_READ`
- `POOL_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: types

<a id="Call_parameters_items_i0"></a>
#### types

- Schema name: `types`
- Type: array of enum (of string)
- Default: ["FILESYSTEM", "VOLUME"]

Dataset types to include in the results.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "FILESYSTEM"
- "VOLUME"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of string

Array of available filesystem/dataset paths.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
