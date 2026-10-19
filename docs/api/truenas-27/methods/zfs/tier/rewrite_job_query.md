---
title: zfs.tier.rewrite_job_query
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_query.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_query.html
required_roles:
  - DATASET_READ
---

# zfs.tier.rewrite_job_query

## Summary

Query rewrite jobs, optionally filtered by status.

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

#### Parameter 1: zfs_tier_rewrite_job_query

<a id="Call_parameters_items_i0"></a>
#### zfs_tier_rewrite_job_query

- Schema name: `zfs_tier_rewrite_job_query`
- Type: object

ZfsTierRewriteJobQueryArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_status"></a>
<a id="Call_parameters_items_i0_status"></a>
##### status

- Schema name: `Status`
- Default: null

Limit results to jobs in the specified states. Pass `null` or omit to return all jobs.
<a id="Call_parameters_items_i0_status_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_status_anyOf_i0)

- Type: array of enum (of string)
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_status_anyOf_i0_items"></a>
- Type: enum (of string)
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Call_parameters_items_i0_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_status_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_query-filters"></a>
<a id="Call_parameters_items_i0_query-filters"></a>
##### query-filters

- Schema name: `Query-Filters`
- Type: array
- Default: []

Additional filters to apply to the results.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-filters_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

<a id="headingCall_parameters_items_i0_query-options"></a>
<a id="Call_parameters_items_i0_query-options"></a>
##### query-options

- Schema name: `QueryOptions`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Options controlling sort order, pagination, and result format.
- No Additional Properties
<a id="headingCall_parameters_items_i0_query-options_extra"></a>
<a id="Call_parameters_items_i0_query-options_extra"></a>
###### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i0_query-options_order_by"></a>
<a id="Call_parameters_items_i0_query-options_order_by"></a>
###### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i0_query-options_select"></a>
<a id="Call_parameters_items_i0_query-options_select"></a>
###### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_select_items"></a>
<a id="Call_parameters_items_i0_query-options_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i0_query-options_count"></a>
<a id="Call_parameters_items_i0_query-options_count"></a>
###### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i0_query-options_get"></a>
<a id="Call_parameters_items_i0_query-options_get"></a>
###### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i0_query-options_offset"></a>
<a id="Call_parameters_items_i0_query-options_offset"></a>
###### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i0_query-options_limit"></a>
<a id="Call_parameters_items_i0_query-options_limit"></a>
###### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i0_query-options_force_sql_filters"></a>
<a id="Call_parameters_items_i0_query-options_force_sql_filters"></a>
###### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### ZfsTierRewriteJobQueryResultItem

- Schema name: `ZfsTierRewriteJobQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_tier_job_id"></a>
<a id="Return_value_anyOf_i0_items_tier_job_id"></a>
###### tier_job_id

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_dataset_name"></a>
<a id="Return_value_anyOf_i0_items_dataset_name"></a>
###### dataset_name

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_job_uuid"></a>
<a id="Return_value_anyOf_i0_items_job_uuid"></a>
###### job_uuid

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_status"></a>
<a id="Return_value_anyOf_i0_items_status"></a>
###### status

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ZfsTierRewriteJobQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ZfsTierRewriteJobQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_tier_job_id"></a>
<a id="Return_value_anyOf_i1_tier_job_id"></a>
###### tier_job_id

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_dataset_name"></a>
<a id="Return_value_anyOf_i1_dataset_name"></a>
###### dataset_name

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_job_uuid"></a>
<a id="Return_value_anyOf_i1_job_uuid"></a>
###### job_uuid

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_status"></a>
<a id="Return_value_anyOf_i1_status"></a>
###### status

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
