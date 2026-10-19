---
title: pool.snapshottask.query
kind: method
source_rst: _sources/api_methods_pool.snapshottask.query.rst.txt
source_html: api_methods_pool.snapshottask.query.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# pool.snapshottask.query

## Required Roles

- `SNAPSHOT_TASK_READ`

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
###### PeriodicSnapshotTaskEntry

- Schema name: `PeriodicSnapshotTaskEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingReturn_value_anyOf_i0_items_recursive"></a>
<a id="Return_value_anyOf_i0_items_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingReturn_value_anyOf_i0_items_lifetime_value"></a>
<a id="Return_value_anyOf_i0_items_lifetime_value"></a>
###### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingReturn_value_anyOf_i0_items_lifetime_unit"></a>
<a id="Return_value_anyOf_i0_items_lifetime_unit"></a>
###### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingReturn_value_anyOf_i0_items_enabled"></a>
<a id="Return_value_anyOf_i0_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingReturn_value_anyOf_i0_items_exclude"></a>
<a id="Return_value_anyOf_i0_items_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_exclude_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_naming_schema"></a>
<a id="Return_value_anyOf_i0_items_naming_schema"></a>
###### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingReturn_value_anyOf_i0_items_allow_empty"></a>
<a id="Return_value_anyOf_i0_items_allow_empty"></a>
###### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingReturn_value_anyOf_i0_items_schedule"></a>
<a id="Return_value_anyOf_i0_items_schedule"></a>
###### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_schedule_minute"></a>
<a id="Return_value_anyOf_i0_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingReturn_value_anyOf_i0_items_schedule_hour"></a>
<a id="Return_value_anyOf_i0_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingReturn_value_anyOf_i0_items_schedule_dom"></a>
<a id="Return_value_anyOf_i0_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingReturn_value_anyOf_i0_items_schedule_month"></a>
<a id="Return_value_anyOf_i0_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingReturn_value_anyOf_i0_items_schedule_dow"></a>
<a id="Return_value_anyOf_i0_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_anyOf_i0_items_schedule_begin"></a>
<a id="Return_value_anyOf_i0_items_schedule_begin"></a>
###### begin

- Schema name: `Begin`
- Type: string
- Default: "00:00"

Start time of the window when snapshots can be taken.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

<a id="headingReturn_value_anyOf_i0_items_schedule_end"></a>
<a id="Return_value_anyOf_i0_items_schedule_end"></a>
###### end

- Schema name: `End`
- Type: string
- Default: "23:59"

End time of the window when snapshots can be taken.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

<a id="headingReturn_value_anyOf_i0_items_vmware_sync"></a>
<a id="Return_value_anyOf_i0_items_vmware_sync"></a>
###### vmware_sync (required)

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingReturn_value_anyOf_i0_items_state"></a>
<a id="Return_value_anyOf_i0_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: object

Detailed state information for the task.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [PeriodicSnapshotTaskEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `PeriodicSnapshotTaskEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingReturn_value_anyOf_i1_recursive"></a>
<a id="Return_value_anyOf_i1_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingReturn_value_anyOf_i1_lifetime_value"></a>
<a id="Return_value_anyOf_i1_lifetime_value"></a>
###### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingReturn_value_anyOf_i1_lifetime_unit"></a>
<a id="Return_value_anyOf_i1_lifetime_unit"></a>
###### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingReturn_value_anyOf_i1_enabled"></a>
<a id="Return_value_anyOf_i1_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingReturn_value_anyOf_i1_exclude"></a>
<a id="Return_value_anyOf_i1_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_exclude_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_naming_schema"></a>
<a id="Return_value_anyOf_i1_naming_schema"></a>
###### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingReturn_value_anyOf_i1_allow_empty"></a>
<a id="Return_value_anyOf_i1_allow_empty"></a>
###### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingReturn_value_anyOf_i1_schedule"></a>
<a id="Return_value_anyOf_i1_schedule"></a>
###### schedule

- Type: object

Cron schedule for when snapshots should be taken.

<a id="headingReturn_value_anyOf_i1_vmware_sync"></a>
<a id="Return_value_anyOf_i1_vmware_sync"></a>
###### vmware_sync (required)

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingReturn_value_anyOf_i1_state"></a>
<a id="Return_value_anyOf_i1_state"></a>
###### state (required)

- Schema name: `State`
- Type: object

Detailed state information for the task.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### PeriodicSnapshotTaskQueryResultItem

- Schema name: `PeriodicSnapshotTaskQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingReturn_value_anyOf_i2_items_dataset"></a>
<a id="Return_value_anyOf_i2_items_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingReturn_value_anyOf_i2_items_recursive"></a>
<a id="Return_value_anyOf_i2_items_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean

Whether to recursively snapshot child datasets.

<a id="headingReturn_value_anyOf_i2_items_lifetime_value"></a>
<a id="Return_value_anyOf_i2_items_lifetime_value"></a>
###### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingReturn_value_anyOf_i2_items_lifetime_unit"></a>
<a id="Return_value_anyOf_i2_items_lifetime_unit"></a>
###### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingReturn_value_anyOf_i2_items_enabled"></a>
<a id="Return_value_anyOf_i2_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this periodic snapshot task is enabled.

<a id="headingReturn_value_anyOf_i2_items_exclude"></a>
<a id="Return_value_anyOf_i2_items_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_exclude_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i2_items_naming_schema"></a>
<a id="Return_value_anyOf_i2_items_naming_schema"></a>
###### naming_schema

- Schema name: `Naming Schema`
- Type: string

Naming pattern for generated snapshots using strftime format.

<a id="headingReturn_value_anyOf_i2_items_allow_empty"></a>
<a id="Return_value_anyOf_i2_items_allow_empty"></a>
###### allow_empty

- Schema name: `Allow Empty`
- Type: boolean

Whether to take snapshots even if no data has changed.

<a id="headingReturn_value_anyOf_i2_items_schedule"></a>
<a id="Return_value_anyOf_i2_items_schedule"></a>
###### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_schedule_minute"></a>
<a id="Return_value_anyOf_i2_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingReturn_value_anyOf_i2_items_schedule_hour"></a>
<a id="Return_value_anyOf_i2_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingReturn_value_anyOf_i2_items_schedule_dom"></a>
<a id="Return_value_anyOf_i2_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingReturn_value_anyOf_i2_items_schedule_month"></a>
<a id="Return_value_anyOf_i2_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingReturn_value_anyOf_i2_items_schedule_dow"></a>
<a id="Return_value_anyOf_i2_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_anyOf_i2_items_schedule_begin"></a>
<a id="Return_value_anyOf_i2_items_schedule_begin"></a>
###### begin

- Schema name: `Begin`
- Type: string
- Default: "00:00"

Start time of the window when snapshots can be taken.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

<a id="headingReturn_value_anyOf_i2_items_schedule_end"></a>
<a id="Return_value_anyOf_i2_items_schedule_end"></a>
###### end

- Schema name: `End`
- Type: string
- Default: "23:59"

End time of the window when snapshots can be taken.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

<a id="headingReturn_value_anyOf_i2_items_vmware_sync"></a>
<a id="Return_value_anyOf_i2_items_vmware_sync"></a>
###### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingReturn_value_anyOf_i2_items_state"></a>
<a id="Return_value_anyOf_i2_items_state"></a>
###### state

- Schema name: `State`
- Type: object

Detailed state information for the task.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [PeriodicSnapshotTaskQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `PeriodicSnapshotTaskQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingReturn_value_anyOf_i3_dataset"></a>
<a id="Return_value_anyOf_i3_dataset"></a>
###### dataset

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingReturn_value_anyOf_i3_recursive"></a>
<a id="Return_value_anyOf_i3_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean

Whether to recursively snapshot child datasets.

<a id="headingReturn_value_anyOf_i3_lifetime_value"></a>
<a id="Return_value_anyOf_i3_lifetime_value"></a>
###### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingReturn_value_anyOf_i3_lifetime_unit"></a>
<a id="Return_value_anyOf_i3_lifetime_unit"></a>
###### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingReturn_value_anyOf_i3_enabled"></a>
<a id="Return_value_anyOf_i3_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this periodic snapshot task is enabled.

<a id="headingReturn_value_anyOf_i3_exclude"></a>
<a id="Return_value_anyOf_i3_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_exclude_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i3_naming_schema"></a>
<a id="Return_value_anyOf_i3_naming_schema"></a>
###### naming_schema

- Schema name: `Naming Schema`
- Type: string

Naming pattern for generated snapshots using strftime format.

<a id="headingReturn_value_anyOf_i3_allow_empty"></a>
<a id="Return_value_anyOf_i3_allow_empty"></a>
###### allow_empty

- Schema name: `Allow Empty`
- Type: boolean

Whether to take snapshots even if no data has changed.

<a id="headingReturn_value_anyOf_i3_schedule"></a>
<a id="Return_value_anyOf_i3_schedule"></a>
###### schedule

- Type: object

Cron schedule for when snapshots should be taken.

<a id="headingReturn_value_anyOf_i3_vmware_sync"></a>
<a id="Return_value_anyOf_i3_vmware_sync"></a>
###### vmware_sync

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingReturn_value_anyOf_i3_state"></a>
<a id="Return_value_anyOf_i3_state"></a>
###### state

- Schema name: `State`
- Type: object

Detailed state information for the task.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
