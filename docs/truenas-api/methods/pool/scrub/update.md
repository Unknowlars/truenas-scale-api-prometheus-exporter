---
title: pool.scrub.update
kind: method
source_rst: _sources/api_methods_pool.scrub.update.rst.txt
source_html: api_methods_pool.scrub.update.html
required_roles:
  - POOL_SCRUB_WRITE
---

# pool.scrub.update

## Summary

Update scrub task of `id`.

## Required Roles

- `POOL_SCRUB_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id_

#### id_

- Schema name: `id_`
- Type: integer

ID of the scrub schedule to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated configuration for the scrub schedule.
- No Additional Properties
##### pool

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

##### threshold

- Schema name: `Threshold`
- Type: integer

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

##### description

- Schema name: `Description`
- Type: string

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

Whether this scrub schedule is enabled.

### Return value

- Schema name: `PoolScrubEntry`
- Type: object

The updated scrub schedule configuration.
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
