---
title: tunable.update
kind: method
source_rst: _sources/api_methods_tunable.update.rst.txt
source_html: api_methods_tunable.update.html
required_roles:
  - SYSTEM_TUNABLE_WRITE
---

# tunable.update

## Summary

Update Tunable of `id`.

This method is a job.

## Required Roles

- `SYSTEM_TUNABLE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the tunable to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated configuration for the tunable.
- No Additional Properties
##### value

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

##### comment

- Schema name: `Comment`
- Type: string

Optional descriptive comment explaining the purpose of this tunable.

##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this tunable is active and should be applied.

##### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

### Return value

- Schema name: `TunableEntry`
- Type: object

The updated tunable configuration.
- No Additional Properties
#### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SYSCTL"

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).

#### var (required)

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

#### value (required)

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment explaining the purpose of this tunable.

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this tunable is active and should be applied.

#### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean
- Default: true

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

#### orig_value (required)

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
