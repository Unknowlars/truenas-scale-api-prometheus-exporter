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

### ADDED

- Schema name: `CronJobAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `CronJobEntry`
- Type: object
- No Additional Properties
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the cron job is active and will be executed.

##### stderr

- Schema name: `Stderr`
- Type: boolean
- Default: false

Whether to IGNORE standard error (if `false`, it will be added to email).

##### stdout

- Schema name: `Stdout`
- Type: boolean
- Default: true

Whether to IGNORE standard output (if `false`, it will be added to email).

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
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

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

##### command (required)

- Schema name: `Command`
- Type: string

Shell command or script to execute.

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of what this cron job does.

##### user (required)

- Schema name: `User`
- Type: string

System user account to run the command as.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cron job.

### CHANGED

- Schema name: `CronJobChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `CronJobEntry`
- Type: object
- No Additional Properties
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the cron job is active and will be executed.

##### stderr

- Schema name: `Stderr`
- Type: boolean
- Default: false

Whether to IGNORE standard error (if `false`, it will be added to email).

##### stdout

- Schema name: `Stdout`
- Type: boolean
- Default: true

Whether to IGNORE standard output (if `false`, it will be added to email).

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
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

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

##### command (required)

- Schema name: `Command`
- Type: string

Shell command or script to execute.

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of what this cron job does.

##### user (required)

- Schema name: `User`
- Type: string

System user account to run the command as.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cron job.

### REMOVED

- Schema name: `CronJobRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
