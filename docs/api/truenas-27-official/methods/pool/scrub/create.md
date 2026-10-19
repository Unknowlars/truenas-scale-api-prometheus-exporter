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

Create a scrub task for pool of id 1, to run every Sunday at 3AM with a threshold of 35 days::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.scrub.create", "params": [{ "pool": 1, "threshold": 35, "description": "Monthly scrub for tank", "schedule": "0 3 * * 7", "enabled": true }] }

## Required Roles

- `POOL_SCRUB_WRITE`

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

Configuration for the new scrub schedule.
- No Additional Properties
<a id="headingCall_parameters_items_i0_pool"></a>
<a id="Call_parameters_items_i0_pool"></a>
##### pool (required)

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

<a id="headingCall_parameters_items_i0_threshold"></a>
<a id="Call_parameters_items_i0_threshold"></a>
##### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Description or notes for this scrub schedule.

<a id="headingCall_parameters_items_i0_schedule"></a>
<a id="Call_parameters_items_i0_schedule"></a>
##### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
<a id="headingCall_parameters_items_i0_schedule_minute"></a>
<a id="Call_parameters_items_i0_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

<a id="headingCall_parameters_items_i0_schedule_hour"></a>
<a id="Call_parameters_items_i0_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

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
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this scrub schedule is enabled.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolScrubEntry`
- Type: object

The newly created scrub schedule configuration.
- No Additional Properties
<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool (required)

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

<a id="headingReturn_value_threshold"></a>
<a id="Return_value_threshold"></a>
#### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

Description or notes for this scrub schedule.

<a id="headingReturn_value_schedule"></a>
<a id="Return_value_schedule"></a>
#### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
<a id="headingReturn_value_schedule_minute"></a>
<a id="Return_value_schedule_minute"></a>
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

<a id="headingReturn_value_schedule_hour"></a>
<a id="Return_value_schedule_hour"></a>
##### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

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
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this scrub schedule is enabled.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the scrub schedule.

<a id="headingReturn_value_pool_name"></a>
<a id="Return_value_pool_name"></a>
#### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool being scrubbed.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
