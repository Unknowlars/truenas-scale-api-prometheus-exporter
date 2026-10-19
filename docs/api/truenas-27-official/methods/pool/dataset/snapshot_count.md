---
title: pool.dataset.snapshot_count
kind: method
source_rst: _sources/api_methods_pool.dataset.snapshot_count.rst.txt
source_html: api_methods_pool.dataset.snapshot_count.html
required_roles:
  - DATASET_READ
---

# pool.dataset.snapshot_count

## Summary

Returns snapshot count for specified `dataset`.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dataset

<a id="Call_parameters_items_i0"></a>
#### dataset

- Schema name: `dataset`
- Type: string

The dataset path to count snapshots for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

The number of snapshots for the specified dataset.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
