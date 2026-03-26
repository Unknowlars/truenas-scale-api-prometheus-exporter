---
title: pool.snapshottask.update
kind: method
source_rst: _sources/api_methods_pool.snapshottask.update.rst.txt
source_html: api_methods_pool.snapshottask.update.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# pool.snapshottask.update

## Summary

Update a Periodic Snapshot Task with specific `id`

See the documentation for `create` method for information on payload contents

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.snapshottask.update", "params": [ 1, { "dataset": "data/work", "recursive": true, "exclude": ["data/work/temp"], "lifetime_value": 2, "lifetime_unit": "WEEK", "naming_schema": "auto_%Y-%m-%d_%H-%M", "schedule": { "minute": "0", "hour": "*", "dom": "*", "month": "*", "dow": "1,2,3,4,5", "begin": "09:00", "end": "18:00" } } ] }

## Required Roles

- `SNAPSHOT_TASK_WRITE`

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

ID of the periodic snapshot task to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated configuration for the periodic snapshot task.
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

##### fixate_removal_date

- Schema name: `Fixate Removal Date`
- Type: boolean

Whether to fix the removal date of existing snapshots when retention settings change.

### Return value

- Schema name: `PoolSnapshotTaskEntry`
- Type: object

The updated periodic snapshot task configuration.
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
