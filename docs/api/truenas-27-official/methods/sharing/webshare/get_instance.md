---
title: sharing.webshare.get_instance
kind: method
source_rst: _sources/api_methods_sharing.webshare.get_instance.rst.txt
source_html: api_methods_sharing.webshare.get_instance.html
required_roles:
  - SHARING_WEBSHARE_READ
---

# sharing.webshare.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_WEBSHARE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SharingWebshareEntry`
- Type: object

Webshare share entry on the TrueNAS server.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this Webshare share.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Webshare share name.
- Must be at least `1` characters long

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`
- Type: string

Local server path to share by using the Webshare protocol. The path must start with `/mnt/` and must be in a ZFS pool.
- Must be at least `1` characters long

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

Dataset name component of the path (e.g., 'tank/webshare'). Null if path cannot be resolved.
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_relative_path"></a>
<a id="Return_value_relative_path"></a>
#### relative_path (required)

- Schema name: `Relative Path`

Relative path component within the dataset (e.g., 'subdir/data'). Null if path cannot be resolved.
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the Webshare share is not available.

<a id="headingReturn_value_is_home_base"></a>
<a id="Return_value_is_home_base"></a>
#### is_home_base

- Schema name: `Is Home Base`
- Type: boolean
- Default: false

If set, this share is used as the base path for user home directories. Only one share can have this enabled.

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="Return_value_locked_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_locked_anyOf_i1)

- Type: null

<a id="headingReturn_value_tier"></a>
<a id="Return_value_tier"></a>
#### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="Return_value_tier_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_Return_value_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_type"></a>
<a id="Return_value_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_tier_anyOf_i0_tier_job"></a>
<a id="Return_value_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
###### status (required)

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

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
