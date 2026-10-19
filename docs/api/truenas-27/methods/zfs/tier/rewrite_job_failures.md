---
title: zfs.tier.rewrite_job_failures
kind: method
source_rst: _sources/api_methods_zfs.tier.rewrite_job_failures.rst.txt
source_html: api_methods_zfs.tier.rewrite_job_failures.html
required_roles:
  - DATASET_READ
---

# zfs.tier.rewrite_job_failures

## Summary

List files that failed to be rewritten during a rewrite job.

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

#### Parameter 1: zfs_tier_rewrite_job_failures

<a id="Call_parameters_items_i0"></a>
#### zfs_tier_rewrite_job_failures

- Schema name: `zfs_tier_rewrite_job_failures`
- Type: object

ZfsTierRewriteJobFailuresArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_tier_job_id"></a>
<a id="Call_parameters_items_i0_tier_job_id"></a>
##### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job to query, in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

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
###### ZfsTierRewriteJobFailureQueryResultItem

- Schema name: `ZfsTierRewriteJobFailureQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_filename"></a>
<a id="Return_value_anyOf_i0_items_filename"></a>
###### filename

- Schema name: `Filename`
- Type: string

Name of the file that failed to migrate storage tier.

<a id="headingReturn_value_anyOf_i0_items_error"></a>
<a id="Return_value_anyOf_i0_items_error"></a>
###### error

- Schema name: `ZfsTierRewriteJobFailureError`
- Type: object

Error details for the failed storage tier migration.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_error_errno"></a>
<a id="Return_value_anyOf_i0_items_error_errno"></a>
###### errno (required)

- Schema name: `Errno`
- Type: integer

Error number from the failed storage tier migration.

<a id="headingReturn_value_anyOf_i0_items_error_strerror"></a>
<a id="Return_value_anyOf_i0_items_error_strerror"></a>
###### strerror (required)

- Schema name: `Strerror`
- Type: string

Human-readable description of the error.

<a id="headingReturn_value_anyOf_i0_items_path"></a>
<a id="Return_value_anyOf_i0_items_path"></a>
###### path

- Schema name: `Path`

Absolute path of the file resolved via its file handle, or `null` if the file no longer exists on the filesystem.
<a id="Return_value_anyOf_i0_items_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_path_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ZfsTierRewriteJobFailureQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ZfsTierRewriteJobFailureQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_filename"></a>
<a id="Return_value_anyOf_i1_filename"></a>
###### filename

- Schema name: `Filename`
- Type: string

Name of the file that failed to migrate storage tier.

<a id="headingReturn_value_anyOf_i1_error"></a>
<a id="Return_value_anyOf_i1_error"></a>
###### error

- Type: object

Error details for the failed storage tier migration.

<a id="headingReturn_value_anyOf_i1_path"></a>
<a id="Return_value_anyOf_i1_path"></a>
###### path

- Schema name: `Path`

Absolute path of the file resolved via its file handle, or `null` if the file no longer exists on the filesystem.
<a id="Return_value_anyOf_i1_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_path_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
