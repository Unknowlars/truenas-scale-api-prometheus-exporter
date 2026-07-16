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

Create a Periodic Snapshot Task

Create a Periodic Snapshot Task that will take snapshots of specified `dataset` at specified `schedule`. Recursive snapshots can be created if `recursive` flag is enabled. You can `exclude` specific child datasets or zvols from the snapshot. Snapshots will be automatically destroyed after a certain amount of time, specified by `lifetime_value` and `lifetime_unit`. If multiple periodic tasks create snapshots at the same time (for example hourly and daily at 00:00) the snapshot will be kept until the last of these tasks reaches its expiry time. Snapshots will be named according to `naming_schema` which is a `strftime`-like template for snapshot name and must contain `%Y`, `%m`, `%d`, `%H` and `%M`.

.. examples(websocket)::

Create a recursive Periodic Snapshot Task for dataset `data/work` excluding `data/work/temp`. Snapshots will be created on weekdays every hour from 09:00 to 18:00 and will be stored for two weeks.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.snapshottask.create", "params": [{ "dataset": "data/work", "recursive": true, "exclude": ["data/work/temp"], "lifetime_value": 2, "lifetime_unit": "WEEK", "naming_schema": "auto_%Y-%m-%d_%H-%M", "schedule": { "minute": "0", "hour": "*", "dom": "*", "month": "*", "dow": "1,2,3,4,5", "begin": "09:00", "end": "18:00" } }] }

## Required Roles

- `SNAPSHOT_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Configuration for the new periodic snapshot task.
- No Additional Properties
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

##### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.

##### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

##### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

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

- Schema name: `PoolSnapshotTaskEntry`
- Type: object

The newly created periodic snapshot task configuration.
- No Additional Properties
#### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

#### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

#### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.

#### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

#### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

#### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

#### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

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

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

#### state (required)

- Schema name: `State`
- Type: object

Detailed state information for the task.

#### vmware_sync (required)

- Schema name: `Vmware Sync`
- Type: boolean

Whether VMware VMs are synced before taking snapshots.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
