---
title: system.release_notes_url
kind: method
source_rst: _sources/api_methods_system.release_notes_url.rst.txt
source_html: api_methods_system.release_notes_url.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# system.release_notes_url

## Summary

Returns the release notes URL for a version of SCALE.

If a version is not provided, the URL for the currently installed version is returned.

## Required Roles

- `SYSTEM_PRODUCT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: version_str

<a id="Call_parameters_items_i0"></a>
#### version_str

- Schema name: `version_str`
- Default: null

Version string to get release notes for. `null` for current version.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

URL to the release notes for the specified version.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
