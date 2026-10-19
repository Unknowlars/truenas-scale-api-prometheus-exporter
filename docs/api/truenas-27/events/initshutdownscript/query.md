---
title: initshutdownscript.query
kind: event
source_rst: _sources/api_events_initshutdownscript.query.rst.txt
source_html: api_events_initshutdownscript.query.html
required_roles:
  - SYSTEM_CRON_READ
---

# initshutdownscript.query

## Summary

Sent on initshutdownscript changes.

## Required Roles

- `SYSTEM_CRON_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `InitShutdownScriptAddedEvent`
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

- Schema name: `InitShutdownScriptEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of init/shutdown script to execute. `COMMAND`: Execute a single command `SCRIPT`: Execute a script file
###### Must be one of:

- "COMMAND"
- "SCRIPT"

<a id="headingADDED_fields_command"></a>
<a id="ADDED_fields_command"></a>
##### command

- Schema name: `Command`
- Default: ""

Must be given if `type="COMMAND"`.
<a id="ADDED_fields_command_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_command_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_command_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_command_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_command_anyOf_i1)

- Type: null

<a id="headingADDED_fields_script"></a>
<a id="ADDED_fields_script"></a>
##### script

- Schema name: `Script`
- Default: ""

Must be given if `type="SCRIPT"`.
<a id="ADDED_fields_script_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_script_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_script_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_script_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_script_anyOf_i1)

- Type: null

<a id="headingADDED_fields_when"></a>
<a id="ADDED_fields_when"></a>
##### when (required)

- Schema name: `When`
- Type: enum (of string)

"PREINIT": Early in the boot process before all services have started. "POSTINIT": Late in the boot process when most services have started. "SHUTDOWN": On shutdown.
###### Must be one of:

- "PREINIT"
- "POSTINIT"
- "SHUTDOWN"

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the init/shutdown script is enabled to execute.

<a id="headingADDED_fields_timeout"></a>
<a id="ADDED_fields_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 10

An integer time in seconds that the system should wait for the execution of the script/command. A hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the purpose of this script.
- Must be at most `255` characters long

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the init/shutdown script.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `InitShutdownScriptChangedEvent`
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

- Schema name: `InitShutdownScriptEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of init/shutdown script to execute. `COMMAND`: Execute a single command `SCRIPT`: Execute a script file
###### Must be one of:

- "COMMAND"
- "SCRIPT"

<a id="headingCHANGED_fields_command"></a>
<a id="CHANGED_fields_command"></a>
##### command

- Schema name: `Command`
- Default: ""

Must be given if `type="COMMAND"`.
<a id="CHANGED_fields_command_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_command_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_command_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_command_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_command_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_script"></a>
<a id="CHANGED_fields_script"></a>
##### script

- Schema name: `Script`
- Default: ""

Must be given if `type="SCRIPT"`.
<a id="CHANGED_fields_script_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_script_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_script_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_script_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_script_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_when"></a>
<a id="CHANGED_fields_when"></a>
##### when (required)

- Schema name: `When`
- Type: enum (of string)

"PREINIT": Early in the boot process before all services have started. "POSTINIT": Late in the boot process when most services have started. "SHUTDOWN": On shutdown.
###### Must be one of:

- "PREINIT"
- "POSTINIT"
- "SHUTDOWN"

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the init/shutdown script is enabled to execute.

<a id="headingCHANGED_fields_timeout"></a>
<a id="CHANGED_fields_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 10

An integer time in seconds that the system should wait for the execution of the script/command. A hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the purpose of this script.
- Must be at most `255` characters long

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the init/shutdown script.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `InitShutdownScriptRemovedEvent`
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
