---
title: pool.scrub.query
kind: event
source_rst: _sources/api_events_pool.scrub.query.rst.txt
source_html: api_events_pool.scrub.query.html
required_roles:
  - POOL_SCRUB_READ
---

# pool.scrub.query

## Summary

Sent on pool.scrub changes.

## Required Roles

- `POOL_SCRUB_READ`

## Schema

- Type: object

### ADDED

- Schema name: `PoolScrubAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `PoolScrubEntry`
- Type: object
- No Additional Properties
##### pool (required)

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

##### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description or notes for this scrub schedule.

##### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

###### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

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
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this scrub schedule is enabled.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the scrub schedule.

##### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool being scrubbed.

### CHANGED

- Schema name: `PoolScrubChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `PoolScrubEntry`
- Type: object
- No Additional Properties
##### pool (required)

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

##### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description or notes for this scrub schedule.

##### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

###### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

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
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this scrub schedule is enabled.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the scrub schedule.

##### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool being scrubbed.

### REMOVED

- Schema name: `PoolScrubRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
