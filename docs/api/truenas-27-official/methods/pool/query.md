---
title: pool.query
kind: method
source_rst: _sources/api_methods_pool.query.rst.txt
source_html: api_methods_pool.query.html
required_roles:
  - POOL_READ
---

# pool.query

## Required Roles

- `POOL_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
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

Query options including pagination, ordering, and additional parameters.
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

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### PoolEntry

- Schema name: `PoolEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

<a id="headingReturn_value_anyOf_i0_items_guid"></a>
<a id="Return_value_anyOf_i0_items_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

<a id="headingReturn_value_anyOf_i0_items_all_sed"></a>
<a id="Return_value_anyOf_i0_items_all_sed"></a>
###### all_sed (required)

- Schema name: `All Sed`

Set when pool is made up of SED disks.
<a id="Return_value_anyOf_i0_items_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_all_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_status"></a>
<a id="Return_value_anyOf_i0_items_status"></a>
###### status (required)

- Schema name: `Status`
- Type: string

Current status of the pool.
Examples:

```json
"ONLINE"
```
Examples:

```json
"DEGRADED"
```
Examples:

```json
"FAULTED"
```

<a id="headingReturn_value_anyOf_i0_items_path"></a>
<a id="Return_value_anyOf_i0_items_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

<a id="headingReturn_value_anyOf_i0_items_scan"></a>
<a id="Return_value_anyOf_i0_items_scan"></a>
###### scan (required)

Information about the most recent scrub or resilver operation. `null` if no scan data is available.
<a id="Return_value_anyOf_i0_items_scan_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0"></a>
###### [PoolScan](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0)

- Schema name: `PoolScan`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_function"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_state"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_start_time"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: string
- Type: Format: date-time

Scan start time.

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_end_time"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time (`null` while the scan is still running).
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_end_time_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_percentage"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_bytes_to_process"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_bytes_processed"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_bytes_issued"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_pause"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time of a scrub pass (`null` if the scan is not paused).
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_pause_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_errors"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingReturn_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left"></a>
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="Return_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_scan_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_expand"></a>
<a id="Return_value_anyOf_i0_items_expand"></a>
###### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
<a id="Return_value_anyOf_i0_items_expand_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_expand_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_expand_anyOf_i0)

- Type: object
Examples:

```json
{
    "bytes_reflowed": 978944,
    "bytes_to_reflow": 835584,
    "end_time": null,
    "expanding_vdev": 0,
    "percentage": 85.35564853556485,
    "start_time": null,
    "state": "FINISHED",
    "total_secs_left": null,
    "waiting_for_resilver": 0
}
```

<a id="tab-pane_Return_value_anyOf_i0_items_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_expand_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_is_upgraded"></a>
<a id="Return_value_anyOf_i0_items_is_upgraded"></a>
###### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

<a id="headingReturn_value_anyOf_i0_items_healthy"></a>
<a id="Return_value_anyOf_i0_items_healthy"></a>
###### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

<a id="headingReturn_value_anyOf_i0_items_warning"></a>
<a id="Return_value_anyOf_i0_items_warning"></a>
###### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

<a id="headingReturn_value_anyOf_i0_items_status_code"></a>
<a id="Return_value_anyOf_i0_items_status_code"></a>
###### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
<a id="Return_value_anyOf_i0_items_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_status_code_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_status_detail"></a>
<a id="Return_value_anyOf_i0_items_status_detail"></a>
###### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
<a id="Return_value_anyOf_i0_items_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_status_detail_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_size"></a>
<a id="Return_value_anyOf_i0_items_size"></a>
###### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i0_items_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_allocated"></a>
<a id="Return_value_anyOf_i0_items_allocated"></a>
###### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i0_items_allocated_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_allocated_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_allocated_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_allocated_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_allocated_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_free"></a>
<a id="Return_value_anyOf_i0_items_free"></a>
###### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i0_items_free_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_free_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_free_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_free_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_free_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_freeing"></a>
<a id="Return_value_anyOf_i0_items_freeing"></a>
###### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
<a id="Return_value_anyOf_i0_items_freeing_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_freeing_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_freeing_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_freeing_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_freeing_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_dedup_table_size"></a>
<a id="Return_value_anyOf_i0_items_dedup_table_size"></a>
###### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
<a id="Return_value_anyOf_i0_items_dedup_table_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_dedup_table_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_dedup_table_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_dedup_table_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_dedup_table_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_dedup_table_quota"></a>
<a id="Return_value_anyOf_i0_items_dedup_table_quota"></a>
###### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
<a id="Return_value_anyOf_i0_items_dedup_table_quota_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_dedup_table_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_dedup_table_quota_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_dedup_table_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_dedup_table_quota_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_fragmentation"></a>
<a id="Return_value_anyOf_i0_items_fragmentation"></a>
###### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
<a id="Return_value_anyOf_i0_items_fragmentation_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_fragmentation_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_fragmentation_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_fragmentation_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_fragmentation_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_size_str"></a>
<a id="Return_value_anyOf_i0_items_size_str"></a>
###### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
<a id="Return_value_anyOf_i0_items_size_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_size_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_size_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_size_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_size_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_allocated_str"></a>
<a id="Return_value_anyOf_i0_items_allocated_str"></a>
###### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
<a id="Return_value_anyOf_i0_items_allocated_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_allocated_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_allocated_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_allocated_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_allocated_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_free_str"></a>
<a id="Return_value_anyOf_i0_items_free_str"></a>
###### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
<a id="Return_value_anyOf_i0_items_free_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_free_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_free_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_free_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_free_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_freeing_str"></a>
<a id="Return_value_anyOf_i0_items_freeing_str"></a>
###### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
<a id="Return_value_anyOf_i0_items_freeing_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_freeing_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_freeing_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_freeing_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_freeing_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_autotrim"></a>
<a id="Return_value_anyOf_i0_items_autotrim"></a>
###### autotrim (required)

- Schema name: `Autotrim`
- Type: object

Auto-trim configuration for the pool indicating whether automatic TRIM operations are enabled.
Examples:

```json
{
    "parsed": "off",
    "rawvalue": "off",
    "source": "DEFAULT",
    "value": "off"
}
```

<a id="headingReturn_value_anyOf_i0_items_topology"></a>
<a id="Return_value_anyOf_i0_items_topology"></a>
###### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
<a id="Return_value_anyOf_i0_items_topology_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_topology_anyOf_i0"></a>
###### [PoolTopology](#tab-pane_Return_value_anyOf_i0_items_topology_anyOf_i0)

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_topology_anyOf_i0_data"></a>
<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_data_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_topology_anyOf_i0_log"></a>
<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_log_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_topology_anyOf_i0_cache"></a>
<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_cache_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_topology_anyOf_i0_spare"></a>
<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_spare"></a>
###### spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_spare_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_topology_anyOf_i0_special"></a>
<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_special_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_topology_anyOf_i0_dedup"></a>
<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_topology_anyOf_i0_dedup_items"></a>
- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_topology_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [PoolEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `PoolEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

<a id="headingReturn_value_anyOf_i1_guid"></a>
<a id="Return_value_anyOf_i1_guid"></a>
###### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

<a id="headingReturn_value_anyOf_i1_all_sed"></a>
<a id="Return_value_anyOf_i1_all_sed"></a>
###### all_sed (required)

- Schema name: `All Sed`

Set when pool is made up of SED disks.
<a id="Return_value_anyOf_i1_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i1_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_all_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_status"></a>
<a id="Return_value_anyOf_i1_status"></a>
###### status (required)

- Schema name: `Status`
- Type: string

Current status of the pool.
Examples:

```json
"ONLINE"
```
Examples:

```json
"DEGRADED"
```
Examples:

```json
"FAULTED"
```

<a id="headingReturn_value_anyOf_i1_path"></a>
<a id="Return_value_anyOf_i1_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

<a id="headingReturn_value_anyOf_i1_scan"></a>
<a id="Return_value_anyOf_i1_scan"></a>
###### scan (required)

Information about the most recent scrub or resilver operation. `null` if no scan data is available.
<a id="Return_value_anyOf_i1_scan_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_scan_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_scan_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_scan_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_expand"></a>
<a id="Return_value_anyOf_i1_expand"></a>
###### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
<a id="Return_value_anyOf_i1_expand_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_expand_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_expand_anyOf_i0)

- Type: object
Examples:

```json
{
    "bytes_reflowed": 978944,
    "bytes_to_reflow": 835584,
    "end_time": null,
    "expanding_vdev": 0,
    "percentage": 85.35564853556485,
    "start_time": null,
    "state": "FINISHED",
    "total_secs_left": null,
    "waiting_for_resilver": 0
}
```

<a id="tab-pane_Return_value_anyOf_i1_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_expand_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_is_upgraded"></a>
<a id="Return_value_anyOf_i1_is_upgraded"></a>
###### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

<a id="headingReturn_value_anyOf_i1_healthy"></a>
<a id="Return_value_anyOf_i1_healthy"></a>
###### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

<a id="headingReturn_value_anyOf_i1_warning"></a>
<a id="Return_value_anyOf_i1_warning"></a>
###### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

<a id="headingReturn_value_anyOf_i1_status_code"></a>
<a id="Return_value_anyOf_i1_status_code"></a>
###### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
<a id="Return_value_anyOf_i1_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_status_code_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_status_detail"></a>
<a id="Return_value_anyOf_i1_status_detail"></a>
###### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
<a id="Return_value_anyOf_i1_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_status_detail_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_size"></a>
<a id="Return_value_anyOf_i1_size"></a>
###### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i1_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_allocated"></a>
<a id="Return_value_anyOf_i1_allocated"></a>
###### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i1_allocated_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_allocated_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_allocated_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_allocated_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_allocated_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_free"></a>
<a id="Return_value_anyOf_i1_free"></a>
###### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i1_free_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_free_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_free_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_free_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_free_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_freeing"></a>
<a id="Return_value_anyOf_i1_freeing"></a>
###### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
<a id="Return_value_anyOf_i1_freeing_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_freeing_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_freeing_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_freeing_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_freeing_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_dedup_table_size"></a>
<a id="Return_value_anyOf_i1_dedup_table_size"></a>
###### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
<a id="Return_value_anyOf_i1_dedup_table_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_dedup_table_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_dedup_table_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_dedup_table_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_dedup_table_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_dedup_table_quota"></a>
<a id="Return_value_anyOf_i1_dedup_table_quota"></a>
###### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
<a id="Return_value_anyOf_i1_dedup_table_quota_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_dedup_table_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_dedup_table_quota_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_dedup_table_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_dedup_table_quota_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_fragmentation"></a>
<a id="Return_value_anyOf_i1_fragmentation"></a>
###### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
<a id="Return_value_anyOf_i1_fragmentation_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_fragmentation_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_fragmentation_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_fragmentation_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_fragmentation_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_size_str"></a>
<a id="Return_value_anyOf_i1_size_str"></a>
###### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
<a id="Return_value_anyOf_i1_size_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_size_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_size_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_size_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_size_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_allocated_str"></a>
<a id="Return_value_anyOf_i1_allocated_str"></a>
###### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
<a id="Return_value_anyOf_i1_allocated_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_allocated_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_allocated_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_allocated_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_allocated_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_free_str"></a>
<a id="Return_value_anyOf_i1_free_str"></a>
###### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
<a id="Return_value_anyOf_i1_free_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_free_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_free_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_free_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_free_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_freeing_str"></a>
<a id="Return_value_anyOf_i1_freeing_str"></a>
###### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
<a id="Return_value_anyOf_i1_freeing_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_freeing_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_freeing_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_freeing_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_freeing_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_autotrim"></a>
<a id="Return_value_anyOf_i1_autotrim"></a>
###### autotrim (required)

- Schema name: `Autotrim`
- Type: object

Auto-trim configuration for the pool indicating whether automatic TRIM operations are enabled.
Examples:

```json
{
    "parsed": "off",
    "rawvalue": "off",
    "source": "DEFAULT",
    "value": "off"
}
```

<a id="headingReturn_value_anyOf_i1_topology"></a>
<a id="Return_value_anyOf_i1_topology"></a>
###### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
<a id="Return_value_anyOf_i1_topology_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_topology_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_topology_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_topology_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### PoolQueryResultItem

- Schema name: `PoolQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the storage pool.

<a id="headingReturn_value_anyOf_i2_items_guid"></a>
<a id="Return_value_anyOf_i2_items_guid"></a>
###### guid

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

<a id="headingReturn_value_anyOf_i2_items_all_sed"></a>
<a id="Return_value_anyOf_i2_items_all_sed"></a>
###### all_sed

- Schema name: `All Sed`

Set when pool is made up of SED disks.
<a id="Return_value_anyOf_i2_items_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i2_items_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_all_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_status"></a>
<a id="Return_value_anyOf_i2_items_status"></a>
###### status

- Schema name: `Status`
- Type: string

Current status of the pool.
Examples:

```json
"ONLINE"
```
Examples:

```json
"DEGRADED"
```
Examples:

```json
"FAULTED"
```

<a id="headingReturn_value_anyOf_i2_items_path"></a>
<a id="Return_value_anyOf_i2_items_path"></a>
###### path

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

<a id="headingReturn_value_anyOf_i2_items_scan"></a>
<a id="Return_value_anyOf_i2_items_scan"></a>
###### scan

Information about the most recent scrub or resilver operation. `null` if no scan data is available.
<a id="Return_value_anyOf_i2_items_scan_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0"></a>
###### [PoolScan](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0)

- Schema name: `PoolScan`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_function"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_state"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_start_time"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: string
- Type: Format: date-time

Scan start time.

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_end_time"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time (`null` while the scan is still running).
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_end_time_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_percentage"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_bytes_to_process"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_bytes_processed"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_bytes_issued"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_pause"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time of a scrub pass (`null` if the scan is not paused).
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_pause_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_errors"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingReturn_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left"></a>
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="Return_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_scan_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_expand"></a>
<a id="Return_value_anyOf_i2_items_expand"></a>
###### expand

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
<a id="Return_value_anyOf_i2_items_expand_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_expand_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_expand_anyOf_i0)

- Type: object
Examples:

```json
{
    "bytes_reflowed": 978944,
    "bytes_to_reflow": 835584,
    "end_time": null,
    "expanding_vdev": 0,
    "percentage": 85.35564853556485,
    "start_time": null,
    "state": "FINISHED",
    "total_secs_left": null,
    "waiting_for_resilver": 0
}
```

<a id="tab-pane_Return_value_anyOf_i2_items_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_expand_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_is_upgraded"></a>
<a id="Return_value_anyOf_i2_items_is_upgraded"></a>
###### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean

Whether this pool has been upgraded to the latest feature flags.

<a id="headingReturn_value_anyOf_i2_items_healthy"></a>
<a id="Return_value_anyOf_i2_items_healthy"></a>
###### healthy

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

<a id="headingReturn_value_anyOf_i2_items_warning"></a>
<a id="Return_value_anyOf_i2_items_warning"></a>
###### warning

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

<a id="headingReturn_value_anyOf_i2_items_status_code"></a>
<a id="Return_value_anyOf_i2_items_status_code"></a>
###### status_code

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
<a id="Return_value_anyOf_i2_items_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_status_code_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_status_detail"></a>
<a id="Return_value_anyOf_i2_items_status_detail"></a>
###### status_detail

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
<a id="Return_value_anyOf_i2_items_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_status_detail_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_size"></a>
<a id="Return_value_anyOf_i2_items_size"></a>
###### size

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i2_items_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_allocated"></a>
<a id="Return_value_anyOf_i2_items_allocated"></a>
###### allocated

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i2_items_allocated_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_allocated_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_allocated_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_allocated_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_allocated_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_free"></a>
<a id="Return_value_anyOf_i2_items_free"></a>
###### free

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i2_items_free_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_free_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_free_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_free_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_free_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_freeing"></a>
<a id="Return_value_anyOf_i2_items_freeing"></a>
###### freeing

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
<a id="Return_value_anyOf_i2_items_freeing_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_freeing_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_freeing_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_freeing_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_freeing_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_dedup_table_size"></a>
<a id="Return_value_anyOf_i2_items_dedup_table_size"></a>
###### dedup_table_size

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
<a id="Return_value_anyOf_i2_items_dedup_table_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_dedup_table_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_dedup_table_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_dedup_table_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_dedup_table_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_dedup_table_quota"></a>
<a id="Return_value_anyOf_i2_items_dedup_table_quota"></a>
###### dedup_table_quota

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
<a id="Return_value_anyOf_i2_items_dedup_table_quota_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_dedup_table_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_dedup_table_quota_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_dedup_table_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_dedup_table_quota_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_fragmentation"></a>
<a id="Return_value_anyOf_i2_items_fragmentation"></a>
###### fragmentation

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
<a id="Return_value_anyOf_i2_items_fragmentation_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_fragmentation_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_fragmentation_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_fragmentation_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_fragmentation_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_size_str"></a>
<a id="Return_value_anyOf_i2_items_size_str"></a>
###### size_str

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
<a id="Return_value_anyOf_i2_items_size_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_size_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_size_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_size_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_size_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_allocated_str"></a>
<a id="Return_value_anyOf_i2_items_allocated_str"></a>
###### allocated_str

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
<a id="Return_value_anyOf_i2_items_allocated_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_allocated_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_allocated_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_allocated_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_allocated_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_free_str"></a>
<a id="Return_value_anyOf_i2_items_free_str"></a>
###### free_str

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
<a id="Return_value_anyOf_i2_items_free_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_free_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_free_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_free_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_free_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_freeing_str"></a>
<a id="Return_value_anyOf_i2_items_freeing_str"></a>
###### freeing_str

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
<a id="Return_value_anyOf_i2_items_freeing_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_freeing_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_freeing_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_freeing_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_freeing_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_autotrim"></a>
<a id="Return_value_anyOf_i2_items_autotrim"></a>
###### autotrim

- Schema name: `Autotrim`
- Type: object

Auto-trim configuration for the pool indicating whether automatic TRIM operations are enabled.
Examples:

```json
{
    "parsed": "off",
    "rawvalue": "off",
    "source": "DEFAULT",
    "value": "off"
}
```

<a id="headingReturn_value_anyOf_i2_items_topology"></a>
<a id="Return_value_anyOf_i2_items_topology"></a>
###### topology

Physical topology and structure of the pool including vdevs. `null` if not available.
<a id="Return_value_anyOf_i2_items_topology_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_topology_anyOf_i0"></a>
###### [PoolTopology](#tab-pane_Return_value_anyOf_i2_items_topology_anyOf_i0)

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_topology_anyOf_i0_data"></a>
<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_data_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i2_items_topology_anyOf_i0_log"></a>
<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_log_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i2_items_topology_anyOf_i0_cache"></a>
<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_cache_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i2_items_topology_anyOf_i0_spare"></a>
<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_spare"></a>
###### spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_spare_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i2_items_topology_anyOf_i0_special"></a>
<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_special_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i2_items_topology_anyOf_i0_dedup"></a>
<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_topology_anyOf_i0_dedup_items"></a>
- Type: object

<a id="tab-pane_Return_value_anyOf_i2_items_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_topology_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [PoolQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `PoolQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

<a id="headingReturn_value_anyOf_i3_name"></a>
<a id="Return_value_anyOf_i3_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the storage pool.

<a id="headingReturn_value_anyOf_i3_guid"></a>
<a id="Return_value_anyOf_i3_guid"></a>
###### guid

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

<a id="headingReturn_value_anyOf_i3_all_sed"></a>
<a id="Return_value_anyOf_i3_all_sed"></a>
###### all_sed

- Schema name: `All Sed`

Set when pool is made up of SED disks.
<a id="Return_value_anyOf_i3_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i3_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_all_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_status"></a>
<a id="Return_value_anyOf_i3_status"></a>
###### status

- Schema name: `Status`
- Type: string

Current status of the pool.
Examples:

```json
"ONLINE"
```
Examples:

```json
"DEGRADED"
```
Examples:

```json
"FAULTED"
```

<a id="headingReturn_value_anyOf_i3_path"></a>
<a id="Return_value_anyOf_i3_path"></a>
###### path

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

<a id="headingReturn_value_anyOf_i3_scan"></a>
<a id="Return_value_anyOf_i3_scan"></a>
###### scan

Information about the most recent scrub or resilver operation. `null` if no scan data is available.
<a id="Return_value_anyOf_i3_scan_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_scan_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_scan_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_scan_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_expand"></a>
<a id="Return_value_anyOf_i3_expand"></a>
###### expand

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
<a id="Return_value_anyOf_i3_expand_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_expand_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_expand_anyOf_i0)

- Type: object
Examples:

```json
{
    "bytes_reflowed": 978944,
    "bytes_to_reflow": 835584,
    "end_time": null,
    "expanding_vdev": 0,
    "percentage": 85.35564853556485,
    "start_time": null,
    "state": "FINISHED",
    "total_secs_left": null,
    "waiting_for_resilver": 0
}
```

<a id="tab-pane_Return_value_anyOf_i3_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_expand_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_is_upgraded"></a>
<a id="Return_value_anyOf_i3_is_upgraded"></a>
###### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean

Whether this pool has been upgraded to the latest feature flags.

<a id="headingReturn_value_anyOf_i3_healthy"></a>
<a id="Return_value_anyOf_i3_healthy"></a>
###### healthy

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

<a id="headingReturn_value_anyOf_i3_warning"></a>
<a id="Return_value_anyOf_i3_warning"></a>
###### warning

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

<a id="headingReturn_value_anyOf_i3_status_code"></a>
<a id="Return_value_anyOf_i3_status_code"></a>
###### status_code

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
<a id="Return_value_anyOf_i3_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_status_code_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_status_detail"></a>
<a id="Return_value_anyOf_i3_status_detail"></a>
###### status_detail

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
<a id="Return_value_anyOf_i3_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_status_detail_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_size"></a>
<a id="Return_value_anyOf_i3_size"></a>
###### size

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i3_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_allocated"></a>
<a id="Return_value_anyOf_i3_allocated"></a>
###### allocated

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i3_allocated_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_allocated_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_allocated_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_allocated_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_allocated_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_free"></a>
<a id="Return_value_anyOf_i3_free"></a>
###### free

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
<a id="Return_value_anyOf_i3_free_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_free_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_free_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_free_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_free_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_freeing"></a>
<a id="Return_value_anyOf_i3_freeing"></a>
###### freeing

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
<a id="Return_value_anyOf_i3_freeing_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_freeing_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_freeing_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_freeing_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_freeing_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_dedup_table_size"></a>
<a id="Return_value_anyOf_i3_dedup_table_size"></a>
###### dedup_table_size

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
<a id="Return_value_anyOf_i3_dedup_table_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_dedup_table_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_dedup_table_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_dedup_table_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_dedup_table_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_dedup_table_quota"></a>
<a id="Return_value_anyOf_i3_dedup_table_quota"></a>
###### dedup_table_quota

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
<a id="Return_value_anyOf_i3_dedup_table_quota_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_dedup_table_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_dedup_table_quota_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_dedup_table_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_dedup_table_quota_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_fragmentation"></a>
<a id="Return_value_anyOf_i3_fragmentation"></a>
###### fragmentation

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
<a id="Return_value_anyOf_i3_fragmentation_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_fragmentation_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_fragmentation_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_fragmentation_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_fragmentation_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_size_str"></a>
<a id="Return_value_anyOf_i3_size_str"></a>
###### size_str

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
<a id="Return_value_anyOf_i3_size_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_size_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_size_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_size_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_size_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_allocated_str"></a>
<a id="Return_value_anyOf_i3_allocated_str"></a>
###### allocated_str

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
<a id="Return_value_anyOf_i3_allocated_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_allocated_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_allocated_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_allocated_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_allocated_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_free_str"></a>
<a id="Return_value_anyOf_i3_free_str"></a>
###### free_str

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
<a id="Return_value_anyOf_i3_free_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_free_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_free_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_free_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_free_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_freeing_str"></a>
<a id="Return_value_anyOf_i3_freeing_str"></a>
###### freeing_str

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
<a id="Return_value_anyOf_i3_freeing_str_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_freeing_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_freeing_str_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_freeing_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_freeing_str_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_autotrim"></a>
<a id="Return_value_anyOf_i3_autotrim"></a>
###### autotrim

- Schema name: `Autotrim`
- Type: object

Auto-trim configuration for the pool indicating whether automatic TRIM operations are enabled.
Examples:

```json
{
    "parsed": "off",
    "rawvalue": "off",
    "source": "DEFAULT",
    "value": "off"
}
```

<a id="headingReturn_value_anyOf_i3_topology"></a>
<a id="Return_value_anyOf_i3_topology"></a>
###### topology

Physical topology and structure of the pool including vdevs. `null` if not available.
<a id="Return_value_anyOf_i3_topology_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_topology_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_topology_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_topology_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
