---
title: pool.dataset.recordsize_choices
kind: method
source_rst: _sources/api_methods_pool.dataset.recordsize_choices.rst.txt
source_html: api_methods_pool.dataset.recordsize_choices.html
required_roles:
  - DATASET_READ
  - READONLY_ADMIN
---

# pool.dataset.recordsize_choices

## Summary

Retrieve recordsize choices for datasets.

## Required Roles

- `DATASET_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_name

<a id="Call_parameters_items_i0"></a>
#### pool_name

- Schema name: `pool_name`
- Default: null

Optional pool name to get record size choices for. If not provided, returns general choices.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of string

Array of available record size options for filesystem datasets.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
