---
title: systemdataset.update
kind: method
source_rst: _sources/api_methods_systemdataset.update.rst.txt
source_html: api_methods_systemdataset.update.html
required_roles:
  - DATASET_WRITE
---

# systemdataset.update

## Summary

Update System Dataset Service Configuration.

This method is a job.

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

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Updated configuration for the system dataset.
- No Additional Properties
<a id="headingCall_parameters_items_i0_pool"></a>
<a id="Call_parameters_items_i0_pool"></a>
##### pool

- Schema name: `Pool`

The name of a valid pool configured in the system to host the system dataset.
<a id="Call_parameters_items_i0_pool_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_pool_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_pool_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_pool_exclude"></a>
<a id="Call_parameters_items_i0_pool_exclude"></a>
##### pool_exclude

- Schema name: `Pool Exclude`

The name of a pool to not place the system dataset on if `pool` is not provided.
<a id="Call_parameters_items_i0_pool_exclude_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_pool_exclude_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_pool_exclude_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_pool_exclude_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_pool_exclude_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SystemDatasetEntry`
- Type: object

The updated system dataset configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the system dataset configuration.

<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool (required)

- Schema name: `Pool`
- Type: string

Name of the pool hosting the system dataset.

<a id="headingReturn_value_pool_set"></a>
<a id="Return_value_pool_set"></a>
#### pool_set (required)

- Schema name: `Pool Set`
- Type: boolean

Whether a pool has been explicitly set for the system dataset.

<a id="headingReturn_value_uuid"></a>
<a id="Return_value_uuid"></a>
#### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the system dataset.

<a id="headingReturn_value_basename"></a>
<a id="Return_value_basename"></a>
#### basename (required)

- Schema name: `Basename`
- Type: string

Base name of the system dataset.

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`

Filesystem path to the system dataset. `null` if not mounted.
<a id="Return_value_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_path_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
