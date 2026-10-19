---
title: update.download
kind: method
source_rst: _sources/api_methods_update.download.rst.txt
source_html: api_methods_update.download.html
required_roles:
  - SYSTEM_UPDATE_WRITE
---

# update.download

## Summary

Download updates.

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

#### Parameter 1: train

<a id="Call_parameters_items_i0"></a>
#### train

- Schema name: `train`
- Default: null

Specifies the train from which to download the update. If both `train` and `version` are `null``, the most recent version that matches the currently selected update profile is used.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

#### Parameter 2: version

<a id="Call_parameters_items_i1"></a>
#### version

- Schema name: `version`
- Default: null

Specific version to download. `null` to download the latest version from the specified train.
<a id="Call_parameters_items_i1_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i1_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Whether the update download was successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
