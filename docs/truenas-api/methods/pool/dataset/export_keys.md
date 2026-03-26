---
title: pool.dataset.export_keys
kind: method
source_rst: _sources/api_methods_pool.dataset.export_keys.rst.txt
source_html: api_methods_pool.dataset.export_keys.html
required_roles:
  - DATASET_WRITE | REPLICATION_TASK_WRITE
---

# pool.dataset.export_keys

## Summary

Export keys for `id` and its children which are stored in the system. The exported file is a JSON file which has a dictionary containing dataset names as keys and their keys as the value.

Please refer to websocket documentation for downloading the file.

This method is a job.

*This job MUST be used with* :doc:`core.download <api_methods_core.download>`.

## Required Roles

- `DATASET_WRITE | REPLICATION_TASK_WRITE`

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

The dataset ID (full path) to export keys from recursively.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful key export.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
