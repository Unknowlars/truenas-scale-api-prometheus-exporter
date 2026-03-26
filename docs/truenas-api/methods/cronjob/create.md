---
title: cronjob.create
kind: method
source_rst: _sources/api_methods_cronjob.create.rst.txt
source_html: api_methods_cronjob.create.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# cronjob.create

## Summary

Create a new cron job.

`stderr` and `stdout` are boolean values which if `true`, represent that we would like to suppress standard error / standard output respectively.

.. examples(websocket)::

Create a cron job which executes `touch /tmp/testfile` after every 5 minutes.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "cronjob.create", "params": [{ "enabled": true, "schedule": { "minute": "5", "hour": "*", "dom": "*", "month": "*", "dow": "*" }, "command": "touch /tmp/testfile", "description": "Test command", "user": "root", "stderr": true, "stdout": true }] }

## Required Roles

- `SYSTEM_CRON_WRITE`

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

Cron job configuration data for the new job.
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

### Return value

- Schema name: `CronJobEntry`
- Type: object

The created cron job configuration.
- No Additional Properties
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the cron job is active and will be executed.

#### stderr

- Schema name: `Stderr`
- Type: boolean
- Default: false

Whether to IGNORE standard error (if `false`, it will be added to email).

#### stdout

- Schema name: `Stdout`
- Type: boolean
- Default: true

Whether to IGNORE standard output (if `false`, it will be added to email).

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
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

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

#### command (required)

- Schema name: `Command`
- Type: string

Shell command or script to execute.

#### description

- Schema name: `Description`
- Type: string
- Default: ""

Human-readable description of what this cron job does.

#### user (required)

- Schema name: `User`
- Type: string

System user account to run the command as.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the cron job.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
