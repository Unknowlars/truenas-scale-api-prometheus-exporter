---
title: pool.dataset.export_keys_for_replication
kind: method
source_rst: _sources/api_methods_pool.dataset.export_keys_for_replication.rst.txt
source_html: api_methods_pool.dataset.export_keys_for_replication.html
required_roles:
  - DATASET_WRITE | REPLICATION_TASK_WRITE
---

# pool.dataset.export_keys_for_replication

## Summary

Export keys for replication task `id` for source dataset(s) which are stored in the system. The exported file is a JSON file which has a dictionary containing dataset names as keys and their keys as the value.

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
- Type: integer

The pool ID to export dataset keys for replication purposes.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
