---
title: cronjob.update
kind: method
source_rst: _sources/api_methods_cronjob.update.rst.txt
source_html: api_methods_cronjob.update.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# cronjob.update

## Summary

Update cronjob of `id`.

## Required Roles

- `SYSTEM_CRON_WRITE`

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

ID of the cron job to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated cron job configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether the cron job is active and will be executed.

<a id="headingCall_parameters_items_i1_stderr"></a>
<a id="Call_parameters_items_i1_stderr"></a>
##### stderr

- Schema name: `Stderr`
- Type: boolean

Whether to IGNORE standard error (if `false`, it will be added to email).

<a id="headingCall_parameters_items_i1_stdout"></a>
<a id="Call_parameters_items_i1_stdout"></a>
##### stdout

- Schema name: `Stdout`
- Type: boolean

Whether to IGNORE standard output (if `false`, it will be added to email).

<a id="headingCall_parameters_items_i1_schedule"></a>
<a id="Call_parameters_items_i1_schedule"></a>
##### schedule

- Schema name: `CronJobSchedule`
- Type: object

Cron schedule configuration for when the job runs.
- No Additional Properties
<a id="headingCall_parameters_items_i1_schedule_minute"></a>
<a id="Call_parameters_items_i1_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

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

<a id="headingCall_parameters_items_i1_command"></a>
<a id="Call_parameters_items_i1_command"></a>
##### command

- Schema name: `Command`
- Type: string

Shell command or script to execute.

<a id="headingCall_parameters_items_i1_description"></a>
<a id="Call_parameters_items_i1_description"></a>
##### description

- Schema name: `Description`
- Type: string

Human-readable description of what this cron job does.

<a id="headingCall_parameters_items_i1_user"></a>
<a id="Call_parameters_items_i1_user"></a>
##### user

- Schema name: `User`
- Type: string

System user account to run the command as.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `CronJobEntry`
- Type: object

The updated cron job configuration.
- No Additional Properties
<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the cron job is active and will be executed.

<a id="headingReturn_value_stderr"></a>
<a id="Return_value_stderr"></a>
#### stderr

- Schema name: `Stderr`
- Type: boolean
- Default: false

Whether to IGNORE standard error (if `false`, it will be added to email).

<a id="headingReturn_value_stdout"></a>
<a id="Return_value_stdout"></a>
#### stdout

- Schema name: `Stdout`
- Type: boolean
- Default: true

Whether to IGNORE standard output (if `false`, it will be added to email).

<a id="headingReturn_value_schedule"></a>
<a id="Return_value_schedule"></a>
#### schedule

- Schema name: `CronJobSchedule`
- Type: object
- Default:
```json
{
  "minute": "00",
  "hour": "*",
  "dom": "*",
  "month": "*",
  "dow": "*"
}
```

Cron schedule configuration for when the job runs.
- No Additional Properties
<a id="headingReturn_value_schedule_minute"></a>
<a id="Return_value_schedule_minute"></a>
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingReturn_value_schedule_hour"></a>
<a id="Return_value_schedule_hour"></a>
##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

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
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_command"></a>
<a id="Return_value_command"></a>
#### command (required)

- Schema name: `Command`
- Type: string

Shell command or script to execute.

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of what this cron job does.

<a id="headingReturn_value_user"></a>
<a id="Return_value_user"></a>
#### user (required)

- Schema name: `User`
- Type: string

System user account to run the command as.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cron job.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
