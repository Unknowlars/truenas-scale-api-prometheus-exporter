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

`query-options.extra.holds` *(bool)* Include hold tags for snapshots in the query result (false by default). `query-options.extra.min_txg` *(int)* Limit snapshot retrieval based on minimum transaction group. `query-options.extra.max_txg` *(int)* Limit snapshot retrieval based on maximum transaction group. `query-options.extra.retention` *(bool)* Include retention information in the query result (false by default). `query-options.extra.properties` *(list)* List of ZFS property names to retrieve.

## Required Roles

- `SNAPSHOT_READ`

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

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

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
###### PoolSnapshotQueryResultItem

- Schema name: `PoolSnapshotQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

<a id="headingReturn_value_anyOf_i0_items_properties"></a>
<a id="Return_value_anyOf_i0_items_properties"></a>
###### properties

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
<a id="headingReturn_value_anyOf_i0_items_properties_additionalProperties"></a>
<a id="Return_value_anyOf_i0_items_properties_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Schema name: `PoolSnapshotEntryPropertyFields`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_properties_additionalProperties_value"></a>
<a id="Return_value_anyOf_i0_items_properties_additionalProperties_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

Current effective value of the ZFS property as a string.

<a id="headingReturn_value_anyOf_i0_items_properties_additionalProperties_rawvalue"></a>
<a id="Return_value_anyOf_i0_items_properties_additionalProperties_rawvalue"></a>
###### rawvalue (required)

- Schema name: `Rawvalue`
- Type: string

Raw string value of the ZFS property as stored.

<a id="headingReturn_value_anyOf_i0_items_properties_additionalProperties_source"></a>
<a id="Return_value_anyOf_i0_items_properties_additionalProperties_source"></a>
###### source (required)

- Schema name: `Source`
- Type: enum (of string)

Source of the property value. `NONE`: Property is not set `DEFAULT`: Using ZFS default value `LOCAL`: Set locally on this snapshot `TEMPORARY`: Temporary override value `INHERITED`: Inherited from parent dataset `RECEIVED`: Set by ZFS receive operation
###### Must be one of:

- "NONE"
- "DEFAULT"
- "LOCAL"
- "TEMPORARY"
- "INHERITED"
- "RECEIVED"

<a id="headingReturn_value_anyOf_i0_items_properties_additionalProperties_parsed"></a>
<a id="Return_value_anyOf_i0_items_properties_additionalProperties_parsed"></a>
###### parsed (required)

- Schema name: `Parsed`
- Type: object

Property value parsed into the appropriate type (string, boolean, integer, etc.).

<a id="headingReturn_value_anyOf_i0_items_pool"></a>
<a id="Return_value_anyOf_i0_items_pool"></a>
###### pool

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

<a id="headingReturn_value_anyOf_i0_items_type"></a>
<a id="Return_value_anyOf_i0_items_type"></a>
###### type

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.
- Specific value: `"SNAPSHOT"`

<a id="headingReturn_value_anyOf_i0_items_snapshot_name"></a>
<a id="Return_value_anyOf_i0_items_snapshot_name"></a>
###### snapshot_name

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

<a id="headingReturn_value_anyOf_i0_items_createtxg"></a>
<a id="Return_value_anyOf_i0_items_createtxg"></a>
###### createtxg

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

<a id="headingReturn_value_anyOf_i0_items_holds"></a>
<a id="Return_value_anyOf_i0_items_holds"></a>
###### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_holds_truenas"></a>
<a id="Return_value_anyOf_i0_items_holds_truenas"></a>
###### truenas

- Schema name: `Truenas`
- Type: integer

Present if a hold has been placed on the snapshot.

<a id="headingReturn_value_anyOf_i0_items_retention"></a>
<a id="Return_value_anyOf_i0_items_retention"></a>
###### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
<a id="Return_value_anyOf_i0_items_retention_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i0)

<a id="Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0"></a>
###### [PoolSnapshotRetentionPST](#tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0)

- Schema name: `PoolSnapshotRetentionPST`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0_datetime"></a>
<a id="Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

<a id="headingReturn_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0_source"></a>
<a id="Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0_source"></a>
###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by a periodic snapshot task.
- Specific value: `"periodic_snapshot_task"`

<a id="headingReturn_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0_periodic_snapshot_task_id"></a>
<a id="Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i0_periodic_snapshot_task_id"></a>
###### periodic_snapshot_task_id (required)

- Schema name: `Periodic Snapshot Task Id`
- Type: integer

ID of the periodic snapshot task managing this retention.

<a id="tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i1"></a>
###### [PoolSnapshotRetentionProperty](#tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i1)

- Schema name: `PoolSnapshotRetentionProperty`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i1_datetime"></a>
<a id="Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i1_datetime"></a>
###### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the snapshot will be eligible for removal.

<a id="headingReturn_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i1_source"></a>
<a id="Return_value_anyOf_i0_items_retention_anyOf_i0_oneOf_i1_source"></a>
###### source (required)

- Schema name: `Source`
- Type: const

Indicates retention is managed by ZFS properties.
- Specific value: `"property"`

<a id="tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_retention_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [PoolSnapshotQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `PoolSnapshotQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: string

Full snapshot identifier including dataset and snapshot name.

<a id="headingReturn_value_anyOf_i1_properties"></a>
<a id="Return_value_anyOf_i1_properties"></a>
###### properties

- Schema name: `Properties`
- Type: object

Object mapping ZFS property names to their values and metadata.
<a id="headingReturn_value_anyOf_i1_properties_additionalProperties"></a>
<a id="Return_value_anyOf_i1_properties_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: object

<a id="headingReturn_value_anyOf_i1_pool"></a>
<a id="Return_value_anyOf_i1_pool"></a>
###### pool

- Schema name: `Pool`
- Type: string

Name of the ZFS pool containing this snapshot.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name

- Schema name: `Name`
- Type: string

Full name of the snapshot including dataset path.

<a id="headingReturn_value_anyOf_i1_type"></a>
<a id="Return_value_anyOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: const

Type identifier indicating this is a ZFS snapshot.
- Specific value: `"SNAPSHOT"`

<a id="headingReturn_value_anyOf_i1_snapshot_name"></a>
<a id="Return_value_anyOf_i1_snapshot_name"></a>
###### snapshot_name

- Schema name: `Snapshot Name`
- Type: string

Just the snapshot name portion without the dataset path.

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

Name of the dataset this snapshot was taken from.

<a id="headingReturn_value_anyOf_i1_createtxg"></a>
<a id="Return_value_anyOf_i1_createtxg"></a>
###### createtxg

- Schema name: `Createtxg`
- Type: string

Transaction group ID when the snapshot was created.

<a id="headingReturn_value_anyOf_i1_holds"></a>
<a id="Return_value_anyOf_i1_holds"></a>
###### holds

- Schema name: `Holds`
- Type: object

Returned when options.extra.holds is set.

<a id="headingReturn_value_anyOf_i1_retention"></a>
<a id="Return_value_anyOf_i1_retention"></a>
###### retention

- Schema name: `Retention`

Returned when options.extra.retention is set.
<a id="Return_value_anyOf_i1_retention_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_retention_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_retention_anyOf_i0)

<a id="Return_value_anyOf_i1_retention_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_anyOf_i1_retention_anyOf_i0_oneOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_retention_anyOf_i0_oneOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_retention_anyOf_i0_oneOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_retention_anyOf_i0_oneOf_i1)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_retention_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_retention_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
