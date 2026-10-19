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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id_

<a id="Call_parameters_items_i0"></a>
#### id_

- Schema name: `id_`
- Type: integer

ID of the scrub schedule to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated configuration for the scrub schedule.
- No Additional Properties
<a id="headingCall_parameters_items_i1_pool"></a>
<a id="Call_parameters_items_i1_pool"></a>
##### pool

- Schema name: `Pool`
- Type: integer

ID of the pool to scrub.
- Value must be strictly greater than `0`

<a id="headingCall_parameters_items_i1_threshold"></a>
<a id="Call_parameters_items_i1_threshold"></a>
##### threshold

- Schema name: `Threshold`
- Type: integer

Days before a scrub is due when a scrub should automatically start.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_description"></a>
<a id="Call_parameters_items_i1_description"></a>
##### description

- Schema name: `Description`
- Type: string

Description or notes for this scrub schedule.

<a id="headingCall_parameters_items_i1_schedule"></a>
<a id="Call_parameters_items_i1_schedule"></a>
##### schedule

- Schema name: `PoolScrubCron`
- Type: object

Cron schedule for when scrubs should run.
- No Additional Properties
<a id="headingCall_parameters_items_i1_schedule_minute"></a>
<a id="Call_parameters_items_i1_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the scrub should run (cron format).

<a id="headingCall_parameters_items_i1_schedule_hour"></a>
<a id="Call_parameters_items_i1_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "00"

Hour when the scrub should run (cron format).

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
- Default: "7"

Day of week when the scrub should run (cron format, 7=Sunday).

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this scrub schedule is enabled.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolScrubEntry`
- Type: object

The updated scrub schedule configuration.
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
