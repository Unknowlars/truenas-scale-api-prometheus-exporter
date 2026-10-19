---
title: cronjob.query
kind: event
source_rst: _sources/api_events_cronjob.query.rst.txt
source_html: api_events_cronjob.query.html
required_roles:
  - SYSTEM_CRON_READ
---

# cronjob.query

## Summary

Sent on cronjob changes.

## Required Roles

- `SYSTEM_CRON_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `CronJobAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `CronJobEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the cron job is active and will be executed.

<a id="headingADDED_fields_stderr"></a>
<a id="ADDED_fields_stderr"></a>
##### stderr

- Schema name: `Stderr`
- Type: boolean
- Default: false

Whether to IGNORE standard error (if `false`, it will be added to email).

<a id="headingADDED_fields_stdout"></a>
<a id="ADDED_fields_stdout"></a>
##### stdout

- Schema name: `Stdout`
- Type: boolean
- Default: true

Whether to IGNORE standard output (if `false`, it will be added to email).

<a id="headingADDED_fields_schedule"></a>
<a id="ADDED_fields_schedule"></a>
##### schedule

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
<a id="headingADDED_fields_schedule_minute"></a>
<a id="ADDED_fields_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingADDED_fields_schedule_hour"></a>
<a id="ADDED_fields_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_schedule_dom"></a>
<a id="ADDED_fields_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_schedule_month"></a>
<a id="ADDED_fields_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_schedule_dow"></a>
<a id="ADDED_fields_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_command"></a>
<a id="ADDED_fields_command"></a>
##### command (required)

- Schema name: `Command`
- Type: string

Shell command or script to execute.

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of what this cron job does.

<a id="headingADDED_fields_user"></a>
<a id="ADDED_fields_user"></a>
##### user (required)

- Schema name: `User`
- Type: string

System user account to run the command as.

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cron job.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `CronJobChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `CronJobEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the cron job is active and will be executed.

<a id="headingCHANGED_fields_stderr"></a>
<a id="CHANGED_fields_stderr"></a>
##### stderr

- Schema name: `Stderr`
- Type: boolean
- Default: false

Whether to IGNORE standard error (if `false`, it will be added to email).

<a id="headingCHANGED_fields_stdout"></a>
<a id="CHANGED_fields_stdout"></a>
##### stdout

- Schema name: `Stdout`
- Type: boolean
- Default: true

Whether to IGNORE standard output (if `false`, it will be added to email).

<a id="headingCHANGED_fields_schedule"></a>
<a id="CHANGED_fields_schedule"></a>
##### schedule

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
<a id="headingCHANGED_fields_schedule_minute"></a>
<a id="CHANGED_fields_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingCHANGED_fields_schedule_hour"></a>
<a id="CHANGED_fields_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_schedule_dom"></a>
<a id="CHANGED_fields_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_schedule_month"></a>
<a id="CHANGED_fields_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_schedule_dow"></a>
<a id="CHANGED_fields_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_command"></a>
<a id="CHANGED_fields_command"></a>
##### command (required)

- Schema name: `Command`
- Type: string

Shell command or script to execute.

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of what this cron job does.

<a id="headingCHANGED_fields_user"></a>
<a id="CHANGED_fields_user"></a>
##### user (required)

- Schema name: `User`
- Type: string

System user account to run the command as.

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cron job.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `CronJobRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
