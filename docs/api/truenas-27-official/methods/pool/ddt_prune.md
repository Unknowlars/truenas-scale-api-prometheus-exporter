---
title: pool.ddt_prune
kind: method
source_rst: _sources/api_methods_pool.ddt_prune.rst.txt
source_html: api_methods_pool.ddt_prune.html
required_roles:
  - POOL_WRITE
---

# pool.ddt_prune

## Summary

Prune DDT entries in pool `pool_name` based on the specified options.

This method is a job.

## Required Roles

- `POOL_WRITE`

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

PoolDdtPruneArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_pool_name"></a>
<a id="Call_parameters_items_i0_pool_name"></a>
##### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool to prune deduplication table entries from.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_percentage"></a>
<a id="Call_parameters_items_i0_percentage"></a>
##### percentage

- Schema name: `Percentage`
- Default: null

Percentage of deduplication table entries to prune.
<a id="Call_parameters_items_i0_percentage_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_percentage_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_percentage_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `100`

<a id="tab-pane_Call_parameters_items_i0_percentage_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_percentage_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_days"></a>
<a id="Call_parameters_items_i0_days"></a>
##### days

- Schema name: `Days`
- Default: null

Remove entries older than this many days.
<a id="Call_parameters_items_i0_days_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_days_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_days_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1`

<a id="tab-pane_Call_parameters_items_i0_days_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_days_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful deduplication table pruning.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
