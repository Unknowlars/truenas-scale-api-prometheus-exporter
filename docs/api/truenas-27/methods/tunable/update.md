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

ID of the tunable to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated configuration for the tunable.
- No Additional Properties
<a id="headingCall_parameters_items_i1_value"></a>
<a id="Call_parameters_items_i1_value"></a>
##### value

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingCall_parameters_items_i1_comment"></a>
<a id="Call_parameters_items_i1_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this tunable is active and should be applied.

<a id="headingCall_parameters_items_i1_update_initramfs"></a>
<a id="Call_parameters_items_i1_update_initramfs"></a>
##### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `TunableEntry`
- Type: object

The updated tunable configuration.
- No Additional Properties
<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SYSCTL"

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
##### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingReturn_value_var"></a>
<a id="Return_value_var"></a>
#### var (required)

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingReturn_value_value"></a>
<a id="Return_value_value"></a>
#### value (required)

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this tunable is active and should be applied.

<a id="headingReturn_value_update_initramfs"></a>
<a id="Return_value_update_initramfs"></a>
#### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean
- Default: true

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingReturn_value_orig_value"></a>
<a id="Return_value_orig_value"></a>
#### orig_value (required)

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
