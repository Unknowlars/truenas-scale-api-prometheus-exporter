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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the periodic snapshot task to analyze.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Proposed configuration changes to analyze.
- No Additional Properties
##### dataset

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

##### recursive

- Schema name: `Recursive`
- Type: boolean

Whether to recursively snapshot child datasets.

##### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.

##### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Unit of time for snapshot retention.

##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this periodic snapshot task is enabled.

##### exclude

- Schema name: `Exclude`
- Type: array of string

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### naming_schema

- Schema name: `Naming Schema`
- Type: string

Naming pattern for generated snapshots using strftime format.

##### allow_empty

- Schema name: `Allow Empty`
- Type: boolean

Whether to take snapshots even if no data has changed.

##### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

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

### Return value

- Schema name: `Result`
- Type: object

Object mapping retention change types to arrays of affected snapshot names.
#### Additional Properties

Each additional property must conform to the following schema
- Type: array of string
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
