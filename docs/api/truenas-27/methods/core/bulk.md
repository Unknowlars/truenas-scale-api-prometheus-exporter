---
title: core.bulk
kind: method
source_rst: _sources/api_methods_core.bulk.rst.txt
source_html: api_methods_core.bulk.html
required_roles:
  []
---

# core.bulk

## Summary

Will sequentially call `method` with arguments from the `params` list. For example, running

call( "core.bulk", "zfs.resource.destroy", [ {"path": "tank@snap-1", "recursive": True}, {"path": "tank@snap-2", "recursive": False} ] )

will call

call("zfs.resource.destroy", {"path": tank@snap-1", recursive=True}) call("zfs.resource.destroy", {"path": "tank@snap-2", recursive=False)

If the first call fails and the seconds succeeds (returning `true`), the result of the overall call will be:

[ {"result": null, "error": "Error deleting snapshot"}, {"result": true, "error": null} ]

Important note: the execution status of `core.bulk` will always be a `SUCCESS` (unless an unlikely internal error occurs). Caller must check for individual call results to ensure the absence of any call errors.

This method is a job.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: method

<a id="Call_parameters_items_i0"></a>
#### method

- Schema name: `method`
- Type: string

Method name to execute for each parameter set.

#### Parameter 2: params

<a id="Call_parameters_items_i1"></a>
#### params

- Schema name: `params`
- Type: array of array

Array of parameter arrays, each representing one method call.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i1_items"></a>
- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_items_items"></a>
- Type: object

#### Parameter 3: description

<a id="Call_parameters_items_i2"></a>
#### description

- Schema name: `description`
- Default: null

Format string for job progress (e.g. "Deleting snapshot {0[dataset]}@{0[name]}").
<a id="Call_parameters_items_i2_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i2_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i2_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i2_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i2_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of results for each bulk operation item.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### CoreBulkResultItem

- Schema name: `CoreBulkResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_job_id"></a>
<a id="Return_value_items_job_id"></a>
##### job_id (required)

- Schema name: `Job Id`

Job ID for this bulk operation item or `null` if it failed to start.
<a id="Return_value_items_job_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_job_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_job_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_job_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_job_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_error"></a>
<a id="Return_value_items_error"></a>
##### error (required)

- Schema name: `Error`

Error message if this item failed or `null` on success.
<a id="Return_value_items_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_result"></a>
<a id="Return_value_items_result"></a>
##### result (required)

- Schema name: `Result`
- Type: object

Result data returned by this bulk operation item.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
