---
title: pool.query
kind: event
source_rst: _sources/api_events_pool.query.rst.txt
source_html: api_events_pool.query.html
required_roles:
  - POOL_READ
---

# pool.query

## Summary

Sent on pool changes.

## Required Roles

- `POOL_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `PoolAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `PoolEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

<a id="headingADDED_fields_guid"></a>
<a id="ADDED_fields_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

<a id="headingADDED_fields_all_sed"></a>
<a id="ADDED_fields_all_sed"></a>
##### all_sed (required)

- Schema name: `All Sed`

Set when pool is made up of SED disks.
<a id="ADDED_fields_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_all_sed_anyOf_i1)

- Type: null

<a id="headingADDED_fields_status"></a>
<a id="ADDED_fields_status"></a>
##### status (required)

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

<a id="headingADDED_fields_path"></a>
<a id="ADDED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

<a id="headingADDED_fields_scan"></a>
<a id="ADDED_fields_scan"></a>
##### scan (required)

Information about the most recent scrub or resilver operation. `null` if no scan data is available.
<a id="ADDED_fields_scan_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0"></a>
###### [PoolScan](#tab-pane_ADDED_fields_scan_anyOf_i0)

- Schema name: `PoolScan`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_scan_anyOf_i0_function"></a>
<a id="ADDED_fields_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingADDED_fields_scan_anyOf_i0_state"></a>
<a id="ADDED_fields_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingADDED_fields_scan_anyOf_i0_start_time"></a>
<a id="ADDED_fields_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: string
- Type: Format: date-time

Scan start time.

<a id="headingADDED_fields_scan_anyOf_i0_end_time"></a>
<a id="ADDED_fields_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time (`null` while the scan is still running).
<a id="ADDED_fields_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingADDED_fields_scan_anyOf_i0_percentage"></a>
<a id="ADDED_fields_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingADDED_fields_scan_anyOf_i0_bytes_to_process"></a>
<a id="ADDED_fields_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingADDED_fields_scan_anyOf_i0_bytes_processed"></a>
<a id="ADDED_fields_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingADDED_fields_scan_anyOf_i0_bytes_issued"></a>
<a id="ADDED_fields_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingADDED_fields_scan_anyOf_i0_pause"></a>
<a id="ADDED_fields_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time of a scrub pass (`null` if the scan is not paused).
<a id="ADDED_fields_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingADDED_fields_scan_anyOf_i0_errors"></a>
<a id="ADDED_fields_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingADDED_fields_scan_anyOf_i0_total_secs_left"></a>
<a id="ADDED_fields_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_scan_anyOf_i1)

- Type: null

<a id="headingADDED_fields_expand"></a>
<a id="ADDED_fields_expand"></a>
##### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
<a id="ADDED_fields_expand_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expand_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expand_anyOf_i0)

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

<a id="tab-pane_ADDED_fields_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expand_anyOf_i1)

- Type: null

<a id="headingADDED_fields_is_upgraded"></a>
<a id="ADDED_fields_is_upgraded"></a>
##### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

<a id="headingADDED_fields_healthy"></a>
<a id="ADDED_fields_healthy"></a>
##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

<a id="headingADDED_fields_warning"></a>
<a id="ADDED_fields_warning"></a>
##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

<a id="headingADDED_fields_status_code"></a>
<a id="ADDED_fields_status_code"></a>
##### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
<a id="ADDED_fields_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_code_anyOf_i1)

- Type: null

<a id="headingADDED_fields_status_detail"></a>
<a id="ADDED_fields_status_detail"></a>
##### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
<a id="ADDED_fields_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_detail_anyOf_i1)

- Type: null

<a id="headingADDED_fields_size"></a>
<a id="ADDED_fields_size"></a>
##### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
<a id="ADDED_fields_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_allocated"></a>
<a id="ADDED_fields_allocated"></a>
##### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
<a id="ADDED_fields_allocated_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_allocated_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_allocated_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_allocated_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_allocated_anyOf_i1)

- Type: null

<a id="headingADDED_fields_free"></a>
<a id="ADDED_fields_free"></a>
##### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
<a id="ADDED_fields_free_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_free_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_free_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_free_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_free_anyOf_i1)

- Type: null

<a id="headingADDED_fields_freeing"></a>
<a id="ADDED_fields_freeing"></a>
##### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
<a id="ADDED_fields_freeing_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_freeing_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_freeing_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_freeing_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_freeing_anyOf_i1)

- Type: null

<a id="headingADDED_fields_dedup_table_size"></a>
<a id="ADDED_fields_dedup_table_size"></a>
##### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
<a id="ADDED_fields_dedup_table_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dedup_table_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dedup_table_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_dedup_table_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dedup_table_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_dedup_table_quota"></a>
<a id="ADDED_fields_dedup_table_quota"></a>
##### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
<a id="ADDED_fields_dedup_table_quota_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dedup_table_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dedup_table_quota_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_dedup_table_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dedup_table_quota_anyOf_i1)

- Type: null

<a id="headingADDED_fields_fragmentation"></a>
<a id="ADDED_fields_fragmentation"></a>
##### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
<a id="ADDED_fields_fragmentation_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_fragmentation_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_fragmentation_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_fragmentation_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_fragmentation_anyOf_i1)

- Type: null

<a id="headingADDED_fields_size_str"></a>
<a id="ADDED_fields_size_str"></a>
##### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
<a id="ADDED_fields_size_str_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_size_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_size_str_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_size_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_size_str_anyOf_i1)

- Type: null

<a id="headingADDED_fields_allocated_str"></a>
<a id="ADDED_fields_allocated_str"></a>
##### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
<a id="ADDED_fields_allocated_str_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_allocated_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_allocated_str_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_allocated_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_allocated_str_anyOf_i1)

- Type: null

<a id="headingADDED_fields_free_str"></a>
<a id="ADDED_fields_free_str"></a>
##### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
<a id="ADDED_fields_free_str_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_free_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_free_str_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_free_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_free_str_anyOf_i1)

- Type: null

<a id="headingADDED_fields_freeing_str"></a>
<a id="ADDED_fields_freeing_str"></a>
##### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
<a id="ADDED_fields_freeing_str_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_freeing_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_freeing_str_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_freeing_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_freeing_str_anyOf_i1)

- Type: null

<a id="headingADDED_fields_autotrim"></a>
<a id="ADDED_fields_autotrim"></a>
##### autotrim (required)

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

<a id="headingADDED_fields_topology"></a>
<a id="ADDED_fields_topology"></a>
##### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
<a id="ADDED_fields_topology_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_topology_anyOf_i0"></a>
###### [PoolTopology](#tab-pane_ADDED_fields_topology_anyOf_i0)

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_topology_anyOf_i0_data"></a>
<a id="ADDED_fields_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_data_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_log"></a>
<a id="ADDED_fields_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_log_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_cache"></a>
<a id="ADDED_fields_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_cache_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_spare"></a>
<a id="ADDED_fields_topology_anyOf_i0_spare"></a>
###### spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_spare_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_special"></a>
<a id="ADDED_fields_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_special_items"></a>
- Type: object

<a id="headingADDED_fields_topology_anyOf_i0_dedup"></a>
<a id="ADDED_fields_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_topology_anyOf_i0_dedup_items"></a>
- Type: object

<a id="tab-pane_ADDED_fields_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_topology_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `PoolChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `PoolEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

<a id="headingCHANGED_fields_guid"></a>
<a id="CHANGED_fields_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

<a id="headingCHANGED_fields_all_sed"></a>
<a id="CHANGED_fields_all_sed"></a>
##### all_sed (required)

- Schema name: `All Sed`

Set when pool is made up of SED disks.
<a id="CHANGED_fields_all_sed_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_all_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_all_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_all_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_all_sed_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

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

<a id="headingCHANGED_fields_path"></a>
<a id="CHANGED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

<a id="headingCHANGED_fields_scan"></a>
<a id="CHANGED_fields_scan"></a>
##### scan (required)

Information about the most recent scrub or resilver operation. `null` if no scan data is available.
<a id="CHANGED_fields_scan_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0"></a>
###### [PoolScan](#tab-pane_CHANGED_fields_scan_anyOf_i0)

- Schema name: `PoolScan`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_scan_anyOf_i0_function"></a>
<a id="CHANGED_fields_scan_anyOf_i0_function"></a>
###### function (required)

- Schema name: `Function`
- Type: enum (of string)

Type of ZFS pool scan.
###### Must be one of:

- "RESILVER"
- "SCRUB"

<a id="headingCHANGED_fields_scan_anyOf_i0_state"></a>
<a id="CHANGED_fields_scan_anyOf_i0_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current lifecycle state of the scan.
###### Must be one of:

- "SCANNING"
- "FINISHED"
- "CANCELED"

<a id="headingCHANGED_fields_scan_anyOf_i0_start_time"></a>
<a id="CHANGED_fields_scan_anyOf_i0_start_time"></a>
###### start_time (required)

- Schema name: `Start Time`
- Type: string
- Type: Format: date-time

Scan start time.

<a id="headingCHANGED_fields_scan_anyOf_i0_end_time"></a>
<a id="CHANGED_fields_scan_anyOf_i0_end_time"></a>
###### end_time (required)

- Schema name: `End Time`

Scan end time (`null` while the scan is still running).
<a id="CHANGED_fields_scan_anyOf_i0_end_time_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i0_end_time_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_scan_anyOf_i0_percentage"></a>
<a id="CHANGED_fields_scan_anyOf_i0_percentage"></a>
###### percentage (required)

- Schema name: `Percentage`
- Type: number

Scan progress (between 0 and 100%).

<a id="headingCHANGED_fields_scan_anyOf_i0_bytes_to_process"></a>
<a id="CHANGED_fields_scan_anyOf_i0_bytes_to_process"></a>
###### bytes_to_process (required)

- Schema name: `Bytes To Process`
- Type: integer

Total bytes located by scanner.

<a id="headingCHANGED_fields_scan_anyOf_i0_bytes_processed"></a>
<a id="CHANGED_fields_scan_anyOf_i0_bytes_processed"></a>
###### bytes_processed (required)

- Schema name: `Bytes Processed`
- Type: integer

Total bytes to scan.

<a id="headingCHANGED_fields_scan_anyOf_i0_bytes_issued"></a>
<a id="CHANGED_fields_scan_anyOf_i0_bytes_issued"></a>
###### bytes_issued (required)

- Schema name: `Bytes Issued`
- Type: integer

Issued bytes per scan pass.

<a id="headingCHANGED_fields_scan_anyOf_i0_pause"></a>
<a id="CHANGED_fields_scan_anyOf_i0_pause"></a>
###### pause (required)

- Schema name: `Pause`

Pause time of a scrub pass (`null` if the scan is not paused).
<a id="CHANGED_fields_scan_anyOf_i0_pause_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i0_pause_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_scan_anyOf_i0_errors"></a>
<a id="CHANGED_fields_scan_anyOf_i0_errors"></a>
###### errors (required)

- Schema name: `Errors`
- Type: integer

Number of scan errors.

<a id="headingCHANGED_fields_scan_anyOf_i0_total_secs_left"></a>
<a id="CHANGED_fields_scan_anyOf_i0_total_secs_left"></a>
###### total_secs_left (required)

- Schema name: `Total Secs Left`

Number of seconds left (`null` if the scan is not running).
<a id="CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i0_total_secs_left_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_scan_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_scan_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_expand"></a>
<a id="CHANGED_fields_expand"></a>
##### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
<a id="CHANGED_fields_expand_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expand_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expand_anyOf_i0)

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

<a id="tab-pane_CHANGED_fields_expand_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expand_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_is_upgraded"></a>
<a id="CHANGED_fields_is_upgraded"></a>
##### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

<a id="headingCHANGED_fields_healthy"></a>
<a id="CHANGED_fields_healthy"></a>
##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

<a id="headingCHANGED_fields_warning"></a>
<a id="CHANGED_fields_warning"></a>
##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

<a id="headingCHANGED_fields_status_code"></a>
<a id="CHANGED_fields_status_code"></a>
##### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
<a id="CHANGED_fields_status_code_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_code_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_code_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_status_code_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_code_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status_detail"></a>
<a id="CHANGED_fields_status_detail"></a>
##### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
<a id="CHANGED_fields_status_detail_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_detail_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_detail_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_status_detail_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_detail_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_size"></a>
<a id="CHANGED_fields_size"></a>
##### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
<a id="CHANGED_fields_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_allocated"></a>
<a id="CHANGED_fields_allocated"></a>
##### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
<a id="CHANGED_fields_allocated_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_allocated_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_allocated_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_allocated_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_allocated_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_free"></a>
<a id="CHANGED_fields_free"></a>
##### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
<a id="CHANGED_fields_free_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_free_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_free_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_free_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_free_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_freeing"></a>
<a id="CHANGED_fields_freeing"></a>
##### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
<a id="CHANGED_fields_freeing_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_freeing_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_freeing_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_freeing_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_freeing_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_dedup_table_size"></a>
<a id="CHANGED_fields_dedup_table_size"></a>
##### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
<a id="CHANGED_fields_dedup_table_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dedup_table_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dedup_table_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_dedup_table_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dedup_table_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_dedup_table_quota"></a>
<a id="CHANGED_fields_dedup_table_quota"></a>
##### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
<a id="CHANGED_fields_dedup_table_quota_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dedup_table_quota_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dedup_table_quota_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_dedup_table_quota_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dedup_table_quota_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_fragmentation"></a>
<a id="CHANGED_fields_fragmentation"></a>
##### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
<a id="CHANGED_fields_fragmentation_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_fragmentation_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_fragmentation_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_fragmentation_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_fragmentation_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_size_str"></a>
<a id="CHANGED_fields_size_str"></a>
##### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
<a id="CHANGED_fields_size_str_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_size_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_size_str_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_size_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_size_str_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_allocated_str"></a>
<a id="CHANGED_fields_allocated_str"></a>
##### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
<a id="CHANGED_fields_allocated_str_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_allocated_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_allocated_str_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_allocated_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_allocated_str_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_free_str"></a>
<a id="CHANGED_fields_free_str"></a>
##### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
<a id="CHANGED_fields_free_str_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_free_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_free_str_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_free_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_free_str_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_freeing_str"></a>
<a id="CHANGED_fields_freeing_str"></a>
##### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
<a id="CHANGED_fields_freeing_str_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_freeing_str_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_freeing_str_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_freeing_str_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_freeing_str_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_autotrim"></a>
<a id="CHANGED_fields_autotrim"></a>
##### autotrim (required)

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

<a id="headingCHANGED_fields_topology"></a>
<a id="CHANGED_fields_topology"></a>
##### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
<a id="CHANGED_fields_topology_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_topology_anyOf_i0"></a>
###### [PoolTopology](#tab-pane_CHANGED_fields_topology_anyOf_i0)

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_topology_anyOf_i0_data"></a>
<a id="CHANGED_fields_topology_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_data_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_log"></a>
<a id="CHANGED_fields_topology_anyOf_i0_log"></a>
###### log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_log_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_cache"></a>
<a id="CHANGED_fields_topology_anyOf_i0_cache"></a>
###### cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_cache_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_spare"></a>
<a id="CHANGED_fields_topology_anyOf_i0_spare"></a>
###### spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_spare_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_special"></a>
<a id="CHANGED_fields_topology_anyOf_i0_special"></a>
###### special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_special_items"></a>
- Type: object

<a id="headingCHANGED_fields_topology_anyOf_i0_dedup"></a>
<a id="CHANGED_fields_topology_anyOf_i0_dedup"></a>
###### dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_topology_anyOf_i0_dedup_items"></a>
- Type: object

<a id="tab-pane_CHANGED_fields_topology_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_topology_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `PoolRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
