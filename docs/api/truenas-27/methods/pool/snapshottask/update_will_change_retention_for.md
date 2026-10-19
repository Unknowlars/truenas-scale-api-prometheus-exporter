---
title: pool.snapshottask.update_will_change_retention_for
kind: method
source_rst: _sources/api_methods_pool.snapshottask.update_will_change_retention_for.rst.txt
source_html: api_methods_pool.snapshottask.update_will_change_retention_for.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# pool.snapshottask.update_will_change_retention_for

## Summary

Returns a list of snapshots which will change the retention if periodic snapshot task `id` is updated with `data`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the periodic snapshot task to analyze.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Proposed configuration changes to analyze.
- No Additional Properties
<a id="headingCall_parameters_items_i1_dataset"></a>
<a id="Call_parameters_items_i1_dataset"></a>
##### dataset

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean

Whether to recursively snapshot child datasets.

<a id="headingCall_parameters_items_i1_lifetime_value"></a>
<a id="Call_parameters_items_i1_lifetime_value"></a>
##### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i1_lifetime_unit"></a>
<a id="Call_parameters_items_i1_lifetime_unit"></a>
##### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this periodic snapshot task is enabled.

<a id="headingCall_parameters_items_i1_exclude"></a>
<a id="Call_parameters_items_i1_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_exclude_items"></a>
- Type: string

<a id="headingCall_parameters_items_i1_naming_schema"></a>
<a id="Call_parameters_items_i1_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: string

Naming pattern for generated snapshots using strftime format.

<a id="headingCall_parameters_items_i1_allow_empty"></a>
<a id="Call_parameters_items_i1_allow_empty"></a>
##### allow_empty

- Schema name: `Allow Empty`
- Type: boolean

Whether to take snapshots even if no data has changed.

<a id="headingCall_parameters_items_i1_schedule"></a>
<a id="Call_parameters_items_i1_schedule"></a>
##### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingCall_parameters_items_i1_schedule_minute"></a>
<a id="Call_parameters_items_i1_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingCall_parameters_items_i1_schedule_hour"></a>
<a id="Call_parameters_items_i1_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCall_parameters_items_i1_schedule_dom"></a>
<a id="Call_parameters_items_i1_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCall_parameters_items_i1_schedule_month"></a>
<a id="Call_parameters_items_i1_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCall_parameters_items_i1_schedule_dow"></a>
<a id="Call_parameters_items_i1_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCall_parameters_items_i1_schedule_begin"></a>
<a id="Call_parameters_items_i1_schedule_begin"></a>
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

<a id="headingCall_parameters_items_i1_schedule_end"></a>
<a id="Call_parameters_items_i1_schedule_end"></a>
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

- Schema name: `Result`
- Type: object

Object mapping retention change types to arrays of affected snapshot names.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_additionalProperties_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
