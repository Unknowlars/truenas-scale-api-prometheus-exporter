---
title: filesystem.put
kind: method
source_rst: _sources/api_methods_filesystem.put.rst.txt
source_html: api_methods_filesystem.put.html
required_roles:
  - FULL_ADMIN
---

# filesystem.put

## Summary

Job to put contents to `path`.

This method is a job.

*This job MUST be used with file upload.* See [uploading-files](../../shared/jobs.md#uploading-files).

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

<a id="Call_parameters_items_i0"></a>
#### path

- Schema name: `path`
- Type: string

Path where the file should be written.
- Must be at least `1` characters long

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"append": false, "mode": null}

Options controlling file writing behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_append"></a>
<a id="Call_parameters_items_i1_append"></a>
##### append

- Schema name: `Append`
- Type: boolean
- Default: false

Whether to append to the file instead of overwriting.

<a id="headingCall_parameters_items_i1_mode"></a>
<a id="Call_parameters_items_i1_mode"></a>
##### mode

- Schema name: `Mode`
- Default: null

Unix permissions to set on the file or `null` to use default.
<a id="Call_parameters_items_i1_mode_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_mode_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_mode_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_mode_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_mode_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the file is successfully written.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
