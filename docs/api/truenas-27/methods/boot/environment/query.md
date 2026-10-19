---
title: boot.environment.query
kind: method
source_rst: _sources/api_methods_boot.environment.query.rst.txt
source_html: api_methods_boot.environment.query.html
required_roles:
  - BOOT_ENV_READ
---

# boot.environment.query

## Required Roles

- `BOOT_ENV_READ`

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
###### BootEnvironmentQueryResultItem

- Schema name: `BootEnvironmentQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: string

The name of the boot environment referenced by the boot environment tool.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

The name of the zfs dataset that represents the boot environment.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_active"></a>
<a id="Return_value_anyOf_i0_items_active"></a>
###### active

- Schema name: `Active`
- Type: boolean

This is the currently running boot environment.

<a id="headingReturn_value_anyOf_i0_items_activated"></a>
<a id="Return_value_anyOf_i0_items_activated"></a>
###### activated

- Schema name: `Activated`
- Type: boolean

Use this boot environment on next boot.

<a id="headingReturn_value_anyOf_i0_items_created"></a>
<a id="Return_value_anyOf_i0_items_created"></a>
###### created

- Schema name: `Created`
- Type: string
- Type: Format: date-time

The date when the boot environment was created.

<a id="headingReturn_value_anyOf_i0_items_used_bytes"></a>
<a id="Return_value_anyOf_i0_items_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The total amount of bytes used by the boot environment.

<a id="headingReturn_value_anyOf_i0_items_used"></a>
<a id="Return_value_anyOf_i0_items_used"></a>
###### used

- Schema name: `Used`
- Type: string

The boot environment's used space in human readable format.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_keep"></a>
<a id="Return_value_anyOf_i0_items_keep"></a>
###### keep

- Schema name: `Keep`
- Type: boolean

When set to false, this makes the boot environment subject to automatic deletion if the TrueNAS updater needs space for an update. Otherwise, the updater will not delete this boot environment if it is set to true.

<a id="headingReturn_value_anyOf_i0_items_can_activate"></a>
<a id="Return_value_anyOf_i0_items_can_activate"></a>
###### can_activate

- Schema name: `Can Activate`
- Type: boolean

The given boot environment may be activated.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [BootEnvironmentQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `BootEnvironmentQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: string

The name of the boot environment referenced by the boot environment tool.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

The name of the zfs dataset that represents the boot environment.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_active"></a>
<a id="Return_value_anyOf_i1_active"></a>
###### active

- Schema name: `Active`
- Type: boolean

This is the currently running boot environment.

<a id="headingReturn_value_anyOf_i1_activated"></a>
<a id="Return_value_anyOf_i1_activated"></a>
###### activated

- Schema name: `Activated`
- Type: boolean

Use this boot environment on next boot.

<a id="headingReturn_value_anyOf_i1_created"></a>
<a id="Return_value_anyOf_i1_created"></a>
###### created

- Schema name: `Created`
- Type: string
- Type: Format: date-time

The date when the boot environment was created.

<a id="headingReturn_value_anyOf_i1_used_bytes"></a>
<a id="Return_value_anyOf_i1_used_bytes"></a>
###### used_bytes

- Schema name: `Used Bytes`
- Type: integer

The total amount of bytes used by the boot environment.

<a id="headingReturn_value_anyOf_i1_used"></a>
<a id="Return_value_anyOf_i1_used"></a>
###### used

- Schema name: `Used`
- Type: string

The boot environment's used space in human readable format.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_keep"></a>
<a id="Return_value_anyOf_i1_keep"></a>
###### keep

- Schema name: `Keep`
- Type: boolean

When set to false, this makes the boot environment subject to automatic deletion if the TrueNAS updater needs space for an update. Otherwise, the updater will not delete this boot environment if it is set to true.

<a id="headingReturn_value_anyOf_i1_can_activate"></a>
<a id="Return_value_anyOf_i1_can_activate"></a>
###### can_activate

- Schema name: `Can Activate`
- Type: boolean

The given boot environment may be activated.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
