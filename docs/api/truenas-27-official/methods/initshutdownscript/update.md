---
title: initshutdownscript.update
kind: method
source_rst: _sources/api_methods_initshutdownscript.update.rst.txt
source_html: api_methods_initshutdownscript.update.html
required_roles:
  - SYSTEM_CRON_WRITE
---

# initshutdownscript.update

## Summary

Update initshutdown script task of `id`.

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

ID of the init/shutdown script to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated init/shutdown script configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_type"></a>
<a id="Call_parameters_items_i1_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)

Type of init/shutdown script to execute. `COMMAND`: Execute a single command `SCRIPT`: Execute a script file
###### Must be one of:

- "COMMAND"
- "SCRIPT"

<a id="headingCall_parameters_items_i1_command"></a>
<a id="Call_parameters_items_i1_command"></a>
##### command

- Schema name: `Command`

Must be given if `type="COMMAND"`.
<a id="Call_parameters_items_i1_command_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_command_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_command_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_command_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_command_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_script"></a>
<a id="Call_parameters_items_i1_script"></a>
##### script

- Schema name: `Script`

Must be given if `type="SCRIPT"`.
<a id="Call_parameters_items_i1_script_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_script_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_script_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_script_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_script_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_when"></a>
<a id="Call_parameters_items_i1_when"></a>
##### when

- Schema name: `When`
- Type: enum (of string)

"PREINIT": Early in the boot process before all services have started. "POSTINIT": Late in the boot process when most services have started. "SHUTDOWN": On shutdown.
###### Must be one of:

- "PREINIT"
- "POSTINIT"
- "SHUTDOWN"

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether the init/shutdown script is enabled to execute.

<a id="headingCall_parameters_items_i1_timeout"></a>
<a id="Call_parameters_items_i1_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer

An integer time in seconds that the system should wait for the execution of the script/command. A hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

<a id="headingCall_parameters_items_i1_comment"></a>
<a id="Call_parameters_items_i1_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string

Optional comment describing the purpose of this script.
- Must be at most `255` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `InitShutdownScriptEntry`
- Type: object

The updated init/shutdown script configuration.
- No Additional Properties
<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of init/shutdown script to execute. `COMMAND`: Execute a single command `SCRIPT`: Execute a script file
##### Must be one of:

- "COMMAND"
- "SCRIPT"

<a id="headingReturn_value_command"></a>
<a id="Return_value_command"></a>
#### command

- Schema name: `Command`
- Default: ""

Must be given if `type="COMMAND"`.
<a id="Return_value_command_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_command_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_command_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_command_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_command_anyOf_i1)

- Type: null

<a id="headingReturn_value_script"></a>
<a id="Return_value_script"></a>
#### script

- Schema name: `Script`
- Default: ""

Must be given if `type="SCRIPT"`.
<a id="Return_value_script_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_script_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_script_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_script_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_script_anyOf_i1)

- Type: null

<a id="headingReturn_value_when"></a>
<a id="Return_value_when"></a>
#### when (required)

- Schema name: `When`
- Type: enum (of string)

"PREINIT": Early in the boot process before all services have started. "POSTINIT": Late in the boot process when most services have started. "SHUTDOWN": On shutdown.
##### Must be one of:

- "PREINIT"
- "POSTINIT"
- "SHUTDOWN"

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the init/shutdown script is enabled to execute.

<a id="headingReturn_value_timeout"></a>
<a id="Return_value_timeout"></a>
#### timeout

- Schema name: `Timeout`
- Type: integer
- Default: 10

An integer time in seconds that the system should wait for the execution of the script/command. A hard limit for a timeout is configured by the base OS, so when a script/command is set to execute on SHUTDOWN, the hard limit configured by the base OS is changed adding the timeout specified by script/command so it can be ensured that it executes as desired and is not interrupted by the base OS's limit.

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional comment describing the purpose of this script.
- Must be at most `255` characters long

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the init/shutdown script.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
