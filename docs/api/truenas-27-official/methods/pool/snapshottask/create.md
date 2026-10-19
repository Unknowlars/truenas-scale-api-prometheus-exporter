---
title: pool.snapshottask.create
kind: method
source_rst: _sources/api_methods_pool.snapshottask.create.rst.txt
source_html: api_methods_pool.snapshottask.create.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# pool.snapshottask.create

## Summary

Create a periodic snapshot task.

Snapshots are automatically destroyed after their configured lifetime. If multiple periodic tasks create a snapshot at the same time (for example, an hourly and a daily task at 00:00), the snapshot is kept until the last of those tasks reaches its expiry time.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Configuration for the new periodic snapshot task.
- No Additional Properties
<a id="headingCall_parameters_items_i0_dataset"></a>
<a id="Call_parameters_items_i0_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingCall_parameters_items_i0_lifetime_value"></a>
<a id="Call_parameters_items_i0_lifetime_value"></a>
##### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_lifetime_unit"></a>
<a id="Call_parameters_items_i0_lifetime_unit"></a>
##### lifetime_unit

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

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingCall_parameters_items_i0_exclude"></a>
<a id="Call_parameters_items_i0_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_exclude_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_naming_schema"></a>
<a id="Call_parameters_items_i0_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingCall_parameters_items_i0_allow_empty"></a>
<a id="Call_parameters_items_i0_allow_empty"></a>
##### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingCall_parameters_items_i0_schedule"></a>
<a id="Call_parameters_items_i0_schedule"></a>
##### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingCall_parameters_items_i0_schedule_minute"></a>
<a id="Call_parameters_items_i0_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingCall_parameters_items_i0_schedule_hour"></a>
<a id="Call_parameters_items_i0_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCall_parameters_items_i0_schedule_dom"></a>
<a id="Call_parameters_items_i0_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCall_parameters_items_i0_schedule_month"></a>
<a id="Call_parameters_items_i0_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCall_parameters_items_i0_schedule_dow"></a>
<a id="Call_parameters_items_i0_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCall_parameters_items_i0_schedule_begin"></a>
<a id="Call_parameters_items_i0_schedule_begin"></a>
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

<a id="headingCall_parameters_items_i0_schedule_end"></a>
<a id="Call_parameters_items_i0_schedule_end"></a>
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

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PeriodicSnapshotTaskEntry`
- Type: object

The newly created periodic snapshot task configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingReturn_value_recursive"></a>
<a id="Return_value_recursive"></a>
#### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingReturn_value_lifetime_value"></a>
<a id="Return_value_lifetime_value"></a>
#### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingReturn_value_lifetime_unit"></a>
<a id="Return_value_lifetime_unit"></a>
#### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.
##### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingReturn_value_exclude"></a>
<a id="Return_value_exclude"></a>
#### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_exclude_items"></a>
- Type: string

<a id="headingReturn_value_naming_schema"></a>
<a id="Return_value_naming_schema"></a>
#### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingReturn_value_allow_empty"></a>
<a id="Return_value_allow_empty"></a>
#### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingReturn_value_schedule"></a>
<a id="Return_value_schedule"></a>
#### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingReturn_value_schedule_minute"></a>
<a id="Return_value_schedule_minute"></a>
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingReturn_value_schedule_hour"></a>
<a id="Return_value_schedule_hour"></a>
##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingReturn_value_schedule_dom"></a>
<a id="Return_value_schedule_dom"></a>
##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingReturn_value_schedule_month"></a>
<a id="Return_value_schedule_month"></a>
##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingReturn_value_schedule_dow"></a>
<a id="Return_value_schedule_dow"></a>
##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_schedule_begin"></a>
<a id="Return_value_schedule_begin"></a>
##### begin

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

<a id="headingReturn_value_schedule_end"></a>
<a id="Return_value_schedule_end"></a>
##### end

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

<a id="headingReturn_value_vmware_sync"></a>
<a id="Return_value_vmware_sync"></a>
#### vmware_sync (required)

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `State`
- Type: object

Detailed state information for the task.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
