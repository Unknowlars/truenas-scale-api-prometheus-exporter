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

call("core.bulk", "zfs.snapshot.delete", [["tank@snap-1", true], ["tank@snap-2", false]])

will call

call("zfs.snapshot.delete", "tank@snap-1", true) call("zfs.snapshot.delete", "tank@snap-2", false)

If the first call fails and the seconds succeeds (returning `true`), the result of the overall call will be:

[ {"result": null, "error": "Error deleting snapshot"}, {"result": true, "error": null} ]

Important note: the execution status of `core.bulk` will always be a `SUCCESS` (unless an unlikely internal error occurs). Caller must check for individual call results to ensure the absence of any call errors.

This method is a job.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: method

#### method

- Schema name: `method`
- Type: string

Method name to execute for each parameter set.

#### Parameter 2: params

#### params

- Schema name: `params`
- Type: array of array

Array of parameter arrays, each representing one method call.
- No Additional Items

##### Each item of this array must be:

- Type: array
- No Additional Items

###### Each item of this array must be:

- Type: object

#### Parameter 3: description

#### description

- Schema name: `description`
- Default: null

Format string for job progress (e.g. "Deleting snapshot {0[dataset]}@{0[name]}").
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: array of object

Array of results for each bulk operation item.
- No Additional Items

#### Each item of this array must be:

#### CoreBulkResultItem

- Schema name: `CoreBulkResultItem`
- Type: object
- No Additional Properties
##### job_id (required)

- Schema name: `Job Id`

Job ID for this bulk operation item or `null` if it failed to start.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### error (required)

- Schema name: `Error`

Error message if this item failed or `null` on success.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### result (required)

- Schema name: `Result`
- Type: object

Result data returned by this bulk operation item.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
