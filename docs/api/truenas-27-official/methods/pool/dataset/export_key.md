---
title: pool.dataset.export_key
kind: method
source_rst: _sources/api_methods_pool.dataset.export_key.rst.txt
source_html: api_methods_pool.dataset.export_key.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.export_key

## Summary

Export own encryption key for dataset `id`. If `download` is `true`, key will be downloaded in a json file where the same file can be used to unlock the dataset, otherwise it will be returned as string.

Please refer to websocket documentation for downloading the file.

This method is a job.

*This job CAN produce a file for download.* See [downloading-files](https://api.truenas.com/v27.0/jsonrpc.html#downloading-files).

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to export the encryption key from.

#### Parameter 2: download

<a id="Call_parameters_items_i1"></a>
#### download

- Schema name: `download`
- Type: boolean
- Default: false

Whether to prepare the key for download as a file.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

The exported encryption key as a hex string, or `null` if no key is available.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
