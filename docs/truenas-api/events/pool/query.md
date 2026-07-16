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

### ADDED

- Schema name: `PoolAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `PoolEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

##### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

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

##### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

##### scan (required)

- Schema name: `Scan`

Information about any active scrub or resilver operation. `null` if no operation is running.
###### Any of

####### Option 1

- Type: object
Examples:

```json
{
    "bytes_issued": null,
    "bytes_processed": null,
    "bytes_to_process": null,
    "end_time": null,
    "errors": null,
    "function": null,
    "pause": null,
    "percentage": null,
    "start_time": null,
    "state": null,
    "total_secs_left": null
}
```

####### Option 2

- Type: null

##### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
###### Any of

####### Option 1

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

####### Option 2

- Type: null

##### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

##### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

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

##### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
###### Any of

####### PoolTopology

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
######## data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

####### Option 2

- Type: null

### CHANGED

- Schema name: `PoolChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `PoolEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the storage pool.

##### guid (required)

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

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

##### path (required)

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

##### scan (required)

- Schema name: `Scan`

Information about any active scrub or resilver operation. `null` if no operation is running.
###### Any of

####### Option 1

- Type: object
Examples:

```json
{
    "bytes_issued": null,
    "bytes_processed": null,
    "bytes_to_process": null,
    "end_time": null,
    "errors": null,
    "function": null,
    "pause": null,
    "percentage": null,
    "start_time": null,
    "state": null,
    "total_secs_left": null
}
```

####### Option 2

- Type: null

##### expand (required)

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
###### Any of

####### Option 1

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

####### Option 2

- Type: null

##### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean
- Default: false

Whether this pool has been upgraded to the latest feature flags.

##### healthy (required)

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

##### warning (required)

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

##### status_code (required)

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### status_detail (required)

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### size (required)

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### allocated (required)

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### free (required)

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### freeing (required)

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### dedup_table_size (required)

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### dedup_table_quota (required)

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### fragmentation (required)

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### size_str (required)

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### allocated_str (required)

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### free_str (required)

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### freeing_str (required)

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

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

##### topology (required)

Physical topology and structure of the pool including vdevs. `null` if not available.
###### Any of

####### PoolTopology

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
######## data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

######### Each item of this array must be:

- Type: object

######## dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

######### Each item of this array must be:

- Type: object

####### Option 2

- Type: null

### REMOVED

- Schema name: `PoolRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
