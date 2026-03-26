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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

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
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

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
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### PoolQueryResultItem

- Schema name: `PoolQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

####### name

- Schema name: `Name`
- Type: string

Name of the storage pool.

####### guid

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

####### status

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

####### path

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

####### scan

- Schema name: `Scan`

Information about any active scrub or resilver operation. `null` if no operation is running.
######## Any of

######### Option 1

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

######### Option 2

- Type: null

####### expand

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
######## Any of

######### Option 1

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

######### Option 2

- Type: null

####### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean

Whether this pool has been upgraded to the latest feature flags.

####### healthy

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

####### warning

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

####### status_code

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### status_detail

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### size

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### allocated

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### free

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### freeing

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### dedup_table_size

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### dedup_table_quota

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### fragmentation

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### size_str

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### allocated_str

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### free_str

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### freeing_str

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### autotrim

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

####### topology

Physical topology and structure of the pool including vdevs. `null` if not available.
######## Any of

######### PoolTopology

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
########## data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

########### Each item of this array must be:

- Type: object

########## dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

########### Each item of this array must be:

- Type: object

######### Option 2

- Type: null

##### PoolQueryResultItem

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

##### Option 3

- Type: null

##### Option 1

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

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `PoolTopology`
- Type: object
- No Additional Properties
###### data (required)

- Schema name: `Data`
- Type: array

Array of data vdev configurations in the pool.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### log (required)

- Schema name: `Log`
- Type: array

Array of ZFS Intent Log (ZIL) vdev configurations.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### cache (required)

- Schema name: `Cache`
- Type: array

Array of L2ARC cache vdev configurations.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### spare (required)

- Schema name: `Spare`
- Type: array

Array of spare disk configurations.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### special (required)

- Schema name: `Special`
- Type: array

Array of special vdev configurations for metadata.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### dedup (required)

- Schema name: `Dedup`
- Type: array

Array of deduplication table vdev configurations.
- No Additional Items

####### Each item of this array must be:

- Type: object

##### Option 2

- Type: null

##### PoolTopology

- Schema name: `PoolQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this storage pool.

###### name

- Schema name: `Name`
- Type: string

Name of the storage pool.

###### guid

- Schema name: `Guid`
- Type: string

Globally unique identifier (GUID) for this pool.

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

###### path

- Schema name: `Path`
- Type: string

Filesystem path where the pool is mounted.

###### scan

- Schema name: `Scan`

Information about any active scrub or resilver operation. `null` if no operation is running.
####### Any of

######## Option 1

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

######## Option 2

- Type: null

###### expand

- Schema name: `Expand`

Information about any active pool expansion operation. `null` if no expansion is running.
####### Any of

######## Option 1

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

######## Option 2

- Type: null

###### is_upgraded

- Schema name: `Is Upgraded`
- Type: boolean

Whether this pool has been upgraded to the latest feature flags.

###### healthy

- Schema name: `Healthy`
- Type: boolean

Whether the pool is in a healthy state with no errors or warnings.

###### warning

- Schema name: `Warning`
- Type: boolean

Whether the pool has warning conditions that require attention.

###### status_code

- Schema name: `Status Code`

Detailed status code for the pool condition. `null` if not applicable.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### status_detail

- Schema name: `Status Detail`

Human-readable description of the pool status. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### size

- Schema name: `Size`

Total size of the pool in bytes. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### allocated

- Schema name: `Allocated`

Amount of space currently allocated in the pool in bytes. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### free

- Schema name: `Free`

Amount of free space available in the pool in bytes. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### freeing

- Schema name: `Freeing`

Amount of space being freed (in bytes) by ongoing operations. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### dedup_table_size

- Schema name: `Dedup Table Size`

Size of the deduplication table in bytes. `null` if deduplication is not enabled.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### dedup_table_quota

- Schema name: `Dedup Table Quota`

Quota limit for the deduplication table. `null` if no quota is set.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### fragmentation

- Schema name: `Fragmentation`

Percentage of pool fragmentation as a string. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### size_str

- Schema name: `Size Str`

Human-readable string representation of the pool size. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### allocated_str

- Schema name: `Allocated Str`

Human-readable string representation of allocated space. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### free_str

- Schema name: `Free Str`

Human-readable string representation of free space. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### freeing_str

- Schema name: `Freeing Str`

Human-readable string representation of space being freed. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

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

###### topology

Physical topology and structure of the pool including vdevs. `null` if not available.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

##### Option 2

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

##### Option 1

- Type: null

##### Option 2

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

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
