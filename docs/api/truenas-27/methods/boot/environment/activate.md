---
title: boot.environment.activate
kind: method
source_rst: _sources/api_methods_boot.environment.activate.rst.txt
source_html: api_methods_boot.environment.activate.html
required_roles:
  - BOOT_ENV_WRITE
---

# boot.environment.activate

## Required Roles

- `BOOT_ENV_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: boot_environment_activate

<a id="Call_parameters_items_i0"></a>
#### boot_environment_activate

- Schema name: `boot_environment_activate`
- Type: object

BootEnvironmentActivateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_id"></a>
<a id="Call_parameters_items_i0_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Name of the boot environment to activate for next boot.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `BootEnvironmentEntry`
- Type: object

The activated boot environment configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

The name of the boot environment referenced by the boot environment tool.
- Must be at least `1` characters long

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`
- Type: string

The name of the zfs dataset that represents the boot environment.
- Must be at least `1` characters long

<a id="headingReturn_value_active"></a>
<a id="Return_value_active"></a>
#### active (required)

- Schema name: `Active`
- Type: boolean

This is the currently running boot environment.

<a id="headingReturn_value_activated"></a>
<a id="Return_value_activated"></a>
#### activated (required)

- Schema name: `Activated`
- Type: boolean

Use this boot environment on next boot.

<a id="headingReturn_value_created"></a>
<a id="Return_value_created"></a>
#### created (required)

- Schema name: `Created`
- Type: string
- Type: Format: date-time

The date when the boot environment was created.

<a id="headingReturn_value_used_bytes"></a>
<a id="Return_value_used_bytes"></a>
#### used_bytes (required)

- Schema name: `Used Bytes`
- Type: integer

The total amount of bytes used by the boot environment.

<a id="headingReturn_value_used"></a>
<a id="Return_value_used"></a>
#### used (required)

- Schema name: `Used`
- Type: string

The boot environment's used space in human readable format.
- Must be at least `1` characters long

<a id="headingReturn_value_keep"></a>
<a id="Return_value_keep"></a>
#### keep (required)

- Schema name: `Keep`
- Type: boolean

When set to false, this makes the boot environment subject to automatic deletion if the TrueNAS updater needs space for an update. Otherwise, the updater will not delete this boot environment if it is set to true.

<a id="headingReturn_value_can_activate"></a>
<a id="Return_value_can_activate"></a>
#### can_activate (required)

- Schema name: `Can Activate`
- Type: boolean

The given boot environment may be activated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
