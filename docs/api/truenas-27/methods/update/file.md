---
title: update.file
kind: method
source_rst: _sources/api_methods_update.file.rst.txt
source_html: api_methods_update.file.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.file

## Summary

Updates the system using the uploaded .tar file.

This method is a job.

## Required Roles

- `SYSTEM_UPDATE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"resume": false, "destination": null}

Options for controlling the manual update file upload process.
- No Additional Properties
<a id="headingCall_parameters_items_i0_resume"></a>
<a id="Call_parameters_items_i0_resume"></a>
##### resume

- Schema name: `Resume`
- Type: boolean
- Default: false

Should be set to `true` if a previous call to this method returned a `CallError` with `errno=EAGAIN` meaning that an upgrade can be performed with a warning and that warning is accepted. In that case, re-uploading the file is not necessary.

<a id="headingCall_parameters_items_i0_destination"></a>
<a id="Call_parameters_items_i0_destination"></a>
##### destination

- Schema name: `Destination`
- Default: null

Create a temporary location by default.
<a id="Call_parameters_items_i0_destination_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_destination_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_destination_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_destination_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_destination_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful update file upload and validation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
