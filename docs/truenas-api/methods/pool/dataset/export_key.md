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

*This job CAN be used with* :doc:`core.download <api_methods_core.download>`.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to export the encryption key from.

#### Parameter 2: download

#### download

- Schema name: `download`
- Type: boolean
- Default: false

Whether to prepare the key for download as a file.

### Return value

- Schema name: `Result`

The exported encryption key as a hex string, or `null` if no key is available.
#### Any of

##### Option 1

- Type: string

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
