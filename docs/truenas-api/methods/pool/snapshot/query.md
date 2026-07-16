---
title: pool.snapshot.query
kind: method
source_rst: _sources/api_methods_pool.snapshot.query.rst.txt
source_html: api_methods_pool.snapshot.query.html
required_roles:
  - SNAPSHOT_READ
---

# pool.snapshot.query

## Summary

Query all ZFS Snapshots with `query-filters` and `query-options`.

`query-options.extra.holds` *(bool)* Include hold tags for snapshots in the query result (false by default). `query-options.extra.min_txg` *(int)* Limit snapshot retrieval based on minimum transaction group. `query-options.extra.max_txg` *(int)* Limit snapshot retrieval based on maximum transaction group. `query-options.extra.retention` *(bool)* Include retention information in the query result (false by default). `query-options.extra.properties` *(dict)* Passed to `zfs.snapshots_serialized.props`.

## Required Roles

- `SNAPSHOT_READ`

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

###### PoolSnapshotQueryResultItem

- Schema name: `PoolSnapshotQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

####### properties

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
######## Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
######### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

######### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

######### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation

######### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

####### pool

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

####### name

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

####### type

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.

####### snapshot_name

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

####### dataset

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

####### createtxg

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

####### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.
- No Additional Properties
######## truenas

- Schema name: `Truenas`
- Type: integer

Present if a hold has been placed on the snapshot.

####### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
######## Any of

######### Option 1

######### Option 2

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
########## datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

########## source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.

########## periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

######### PoolSnapshotRetentionPST

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
########## datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

########## source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.

######### PoolSnapshotRetentionProperty

- Type: null

##### PoolSnapshotQueryResultItem

##### Option 3

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.

###### periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

##### Option 1

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.

##### Option 2

- Type: null

##### PoolSnapshotRetentionPST

- Schema name: `PoolSnapshotQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

###### properties

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
####### Additional Properties

Each additional property must conform to the following schema
- Type: object

###### pool

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

###### name

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

###### type

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.

###### snapshot_name

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

###### dataset

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

###### createtxg

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

###### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.

###### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
####### Any of

######## Option 1

######## Option 2

- Type: object

######## Option 1

- Type: object

######## Option 2

- Type: null

##### PoolSnapshotRetentionProperty

##### Option 1

- Type: object

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
