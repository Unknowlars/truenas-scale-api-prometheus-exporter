---
title: boot.environment.keep
kind: method
source_rst: _sources/api_methods_boot.environment.keep.rst.txt
source_html: api_methods_boot.environment.keep.html
required_roles:
  - BOOT_ENV_WRITE
---

# boot.environment.keep

## Required Roles

- `BOOT_ENV_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: boot_environment_destroy

#### boot_environment_destroy

- Schema name: `boot_environment_destroy`
- Type: object

BootEnvironmentKeepArgs parameters.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Name of the boot environment to modify.
- Must be at least `1` characters long

##### value (required)

- Schema name: `Value`
- Type: boolean

Whether to protect this boot environment from automatic deletion.

### Return value

- Schema name: `BootEnvironmentEntry`
- Type: object

The updated boot environment with modified keep setting.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

The name of the boot environment referenced by the boot environment tool.
- Must be at least `1` characters long

#### dataset (required)

- Schema name: `Dataset`
- Type: string

The name of the zfs dataset that represents the boot environment.
- Must be at least `1` characters long

#### active (required)

- Schema name: `Active`
- Type: boolean

This is the currently running boot environment.

#### activated (required)

- Schema name: `Activated`
- Type: boolean

Use this boot environment on next boot.

#### created (required)

- Schema name: `Created`
- Type: string
- Type: Format: date-time

The date when the boot environment was created.

#### used_bytes (required)

- Schema name: `Used Bytes`
- Type: integer

The total amount of bytes used by the boot environment.

#### used (required)

- Schema name: `Used`
- Type: string

The boot environment's used space in human readable format.
- Must be at least `1` characters long

#### keep (required)

- Schema name: `Keep`
- Type: boolean

When set to false, this makes the boot environment subject to automatic deletion if the TrueNAS updater needs space for an update. Otherwise, the updater will not delete this boot environment if it is set to true.

#### can_activate (required)

- Schema name: `Can Activate`
- Type: boolean

The given boot environment may be activated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
