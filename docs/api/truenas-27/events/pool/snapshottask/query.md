---
title: pool.snapshottask.query
kind: event
source_rst: _sources/api_events_pool.snapshottask.query.rst.txt
source_html: api_events_pool.snapshottask.query.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# pool.snapshottask.query

## Summary

Sent on pool.snapshottask changes.

## Required Roles

- `SNAPSHOT_TASK_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `PeriodicSnapshotTaskAddedEvent`
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

- Schema name: `PeriodicSnapshotTaskEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingADDED_fields_recursive"></a>
<a id="ADDED_fields_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingADDED_fields_lifetime_value"></a>
<a id="ADDED_fields_lifetime_value"></a>
##### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_lifetime_unit"></a>
<a id="ADDED_fields_lifetime_unit"></a>
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

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingADDED_fields_exclude"></a>
<a id="ADDED_fields_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_exclude_items"></a>
- Type: string

<a id="headingADDED_fields_naming_schema"></a>
<a id="ADDED_fields_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingADDED_fields_allow_empty"></a>
<a id="ADDED_fields_allow_empty"></a>
##### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingADDED_fields_schedule"></a>
<a id="ADDED_fields_schedule"></a>
##### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingADDED_fields_schedule_minute"></a>
<a id="ADDED_fields_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingADDED_fields_schedule_hour"></a>
<a id="ADDED_fields_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_schedule_dom"></a>
<a id="ADDED_fields_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_schedule_month"></a>
<a id="ADDED_fields_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_schedule_dow"></a>
<a id="ADDED_fields_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_schedule_begin"></a>
<a id="ADDED_fields_schedule_begin"></a>
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

<a id="headingADDED_fields_schedule_end"></a>
<a id="ADDED_fields_schedule_end"></a>
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

<a id="headingADDED_fields_vmware_sync"></a>
<a id="ADDED_fields_vmware_sync"></a>
##### vmware_sync (required)

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: object

Detailed state information for the task.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `PeriodicSnapshotTaskChangedEvent`
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

- Schema name: `PeriodicSnapshotTaskEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingCHANGED_fields_recursive"></a>
<a id="CHANGED_fields_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingCHANGED_fields_lifetime_value"></a>
<a id="CHANGED_fields_lifetime_value"></a>
##### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_lifetime_unit"></a>
<a id="CHANGED_fields_lifetime_unit"></a>
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

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingCHANGED_fields_exclude"></a>
<a id="CHANGED_fields_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_exclude_items"></a>
- Type: string

<a id="headingCHANGED_fields_naming_schema"></a>
<a id="CHANGED_fields_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingCHANGED_fields_allow_empty"></a>
<a id="CHANGED_fields_allow_empty"></a>
##### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingCHANGED_fields_schedule"></a>
<a id="CHANGED_fields_schedule"></a>
##### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingCHANGED_fields_schedule_minute"></a>
<a id="CHANGED_fields_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingCHANGED_fields_schedule_hour"></a>
<a id="CHANGED_fields_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_schedule_dom"></a>
<a id="CHANGED_fields_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_schedule_month"></a>
<a id="CHANGED_fields_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_schedule_dow"></a>
<a id="CHANGED_fields_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_schedule_begin"></a>
<a id="CHANGED_fields_schedule_begin"></a>
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

<a id="headingCHANGED_fields_schedule_end"></a>
<a id="CHANGED_fields_schedule_end"></a>
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

<a id="headingCHANGED_fields_vmware_sync"></a>
<a id="CHANGED_fields_vmware_sync"></a>
##### vmware_sync (required)

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: object

Detailed state information for the task.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `PeriodicSnapshotTaskRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
