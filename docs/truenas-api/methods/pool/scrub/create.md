---
title: pool.scrub.create
kind: method
source_rst: _sources/api_methods_pool.scrub.create.rst.txt
source_html: api_methods_pool.scrub.create.html
required_roles:
  - POOL_SCRUB_WRITE
---

# pool.scrub.create

## Summary

Create a scrub task for a pool.

`threshold` refers to the minimum amount of time in days has to be passed before a scrub can run again.

.. examples(websocket)::

Create a scrub task for pool of id 1, to run every sunday but with a threshold of 35 days. The check will run at 3AM every sunday.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.scrub.create" "params": [{ "pool": 1, "threshold": 35, "description": "Monthly scrub for tank", "schedule": "0 3 * * 7", "enabled": true }] }

## Required Roles

- `POOL_SCRUB_WRITE`

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

Configuration for the new scrub schedule.
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

### Return value

- Schema name: `PoolScrubEntry`
- Type: object

The newly created scrub schedule configuration.
- No Additional Properties
#### pool (required)

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

#### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

#### description

- Schema name: `Description`
- Type: string
- Default: ""

Description or notes for this scrub schedule.

#### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

##### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

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
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this scrub schedule is enabled.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the scrub schedule.

#### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool being scrubbed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
