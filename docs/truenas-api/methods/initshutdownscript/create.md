---
title: initshutdownscript.create
kind: method
source_rst: _sources/api_methods_initshutdownscript.create.rst.txt
source_html: api_methods_initshutdownscript.create.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# initshutdownscript.create

## Summary

Create an initshutdown script task.

`type` indicates if a command or script should be executed at `when`.

There are three choices for `when`:

1) PREINIT - This is early in the boot process before all the services have started 2) POSTINIT - This is late in the boot process when most of the services have started 3) SHUTDOWN - This is on shutdown

`timeout` is an integer value which indicates time in seconds which the system should wait for the execution of script/command. It should be noted that a hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

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

Init/shutdown script configuration data for creation.
- No Additional Properties
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of init/shutdown script to execute. `COMMAND`: Execute a single command `SCRIPT`: Execute a script file

##### command

- Schema name: `Command`
- Default: ""

Must be given if `type="COMMAND"`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### script

- Schema name: `Script`
- Default: ""

Must be given if `type="SCRIPT"`.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### when (required)

- Schema name: `When`
- Type: enum (of string)

"PREINIT": Early in the boot process before all services have started. "POSTINIT": Late in the boot process when most services have started. "SHUTDOWN": On shutdown.

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the init/shutdown script is enabled to execute.

##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 10

An integer time in seconds that the system should wait for the execution of the script/command. A hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the purpose of this script.
- Must be at most `255` characters long

### Return value

- Schema name: `InitShutdownScriptEntry`
- Type: object

The created init/shutdown script configuration.
- No Additional Properties
#### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of init/shutdown script to execute. `COMMAND`: Execute a single command `SCRIPT`: Execute a script file

#### command

- Schema name: `Command`
- Default: ""

Must be given if `type="COMMAND"`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### script

- Schema name: `Script`
- Default: ""

Must be given if `type="SCRIPT"`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### when (required)

- Schema name: `When`
- Type: enum (of string)

"PREINIT": Early in the boot process before all services have started. "POSTINIT": Late in the boot process when most services have started. "SHUTDOWN": On shutdown.

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the init/shutdown script is enabled to execute.

#### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 10

An integer time in seconds that the system should wait for the execution of the script/command. A hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the purpose of this script.
- Must be at most `255` characters long

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the init/shutdown script.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
