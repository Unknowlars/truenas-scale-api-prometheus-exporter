---
title: tunable.query
kind: method
source_rst: _sources/api_methods_tunable.query.rst.txt
source_html: api_methods_tunable.query.html
required_roles:
  - SYSTEM_TUNABLE_READ
---

# tunable.query

## Required Roles

- `SYSTEM_TUNABLE_READ`

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
###### TunableEntry

- Schema name: `TunableEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_type"></a>
<a id="Return_value_anyOf_i0_items_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SYSCTL"

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
###### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingReturn_value_anyOf_i0_items_var"></a>
<a id="Return_value_anyOf_i0_items_var"></a>
###### var (required)

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingReturn_value_anyOf_i0_items_value"></a>
<a id="Return_value_anyOf_i0_items_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingReturn_value_anyOf_i0_items_comment"></a>
<a id="Return_value_anyOf_i0_items_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingReturn_value_anyOf_i0_items_enabled"></a>
<a id="Return_value_anyOf_i0_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this tunable is active and should be applied.

<a id="headingReturn_value_anyOf_i0_items_update_initramfs"></a>
<a id="Return_value_anyOf_i0_items_update_initramfs"></a>
###### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean
- Default: true

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingReturn_value_anyOf_i0_items_orig_value"></a>
<a id="Return_value_anyOf_i0_items_orig_value"></a>
###### orig_value (required)

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [TunableEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `TunableEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_type"></a>
<a id="Return_value_anyOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SYSCTL"

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
###### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingReturn_value_anyOf_i1_var"></a>
<a id="Return_value_anyOf_i1_var"></a>
###### var (required)

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingReturn_value_anyOf_i1_value"></a>
<a id="Return_value_anyOf_i1_value"></a>
###### value (required)

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingReturn_value_anyOf_i1_comment"></a>
<a id="Return_value_anyOf_i1_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingReturn_value_anyOf_i1_enabled"></a>
<a id="Return_value_anyOf_i1_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this tunable is active and should be applied.

<a id="headingReturn_value_anyOf_i1_update_initramfs"></a>
<a id="Return_value_anyOf_i1_update_initramfs"></a>
###### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean
- Default: true

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingReturn_value_anyOf_i1_orig_value"></a>
<a id="Return_value_anyOf_i1_orig_value"></a>
###### orig_value (required)

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### TunableQueryResultItem

- Schema name: `TunableQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_type"></a>
<a id="Return_value_anyOf_i2_items_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
###### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingReturn_value_anyOf_i2_items_var"></a>
<a id="Return_value_anyOf_i2_items_var"></a>
###### var

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingReturn_value_anyOf_i2_items_value"></a>
<a id="Return_value_anyOf_i2_items_value"></a>
###### value

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingReturn_value_anyOf_i2_items_comment"></a>
<a id="Return_value_anyOf_i2_items_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingReturn_value_anyOf_i2_items_enabled"></a>
<a id="Return_value_anyOf_i2_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this tunable is active and should be applied.

<a id="headingReturn_value_anyOf_i2_items_update_initramfs"></a>
<a id="Return_value_anyOf_i2_items_update_initramfs"></a>
###### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingReturn_value_anyOf_i2_items_orig_value"></a>
<a id="Return_value_anyOf_i2_items_orig_value"></a>
###### orig_value

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [TunableQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `TunableQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_type"></a>
<a id="Return_value_anyOf_i3_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
###### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingReturn_value_anyOf_i3_var"></a>
<a id="Return_value_anyOf_i3_var"></a>
###### var

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingReturn_value_anyOf_i3_value"></a>
<a id="Return_value_anyOf_i3_value"></a>
###### value

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingReturn_value_anyOf_i3_comment"></a>
<a id="Return_value_anyOf_i3_comment"></a>
###### comment

- Schema name: `Comment`
- Type: string

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingReturn_value_anyOf_i3_enabled"></a>
<a id="Return_value_anyOf_i3_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this tunable is active and should be applied.

<a id="headingReturn_value_anyOf_i3_update_initramfs"></a>
<a id="Return_value_anyOf_i3_update_initramfs"></a>
###### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingReturn_value_anyOf_i3_orig_value"></a>
<a id="Return_value_anyOf_i3_orig_value"></a>
###### orig_value

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
