---
title: tunable.query
kind: event
source_rst: _sources/api_events_tunable.query.rst.txt
source_html: api_events_tunable.query.html
required_roles:
  - SYSTEM_TUNABLE_READ
---

# tunable.query

## Summary

Sent on tunable changes.

## Required Roles

- `SYSTEM_TUNABLE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `TunableAddedEvent`
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

- Schema name: `TunableEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SYSCTL"

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
###### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingADDED_fields_var"></a>
<a id="ADDED_fields_var"></a>
##### var (required)

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingADDED_fields_value"></a>
<a id="ADDED_fields_value"></a>
##### value (required)

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingADDED_fields_comment"></a>
<a id="ADDED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this tunable is active and should be applied.

<a id="headingADDED_fields_update_initramfs"></a>
<a id="ADDED_fields_update_initramfs"></a>
##### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean
- Default: true

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingADDED_fields_orig_value"></a>
<a id="ADDED_fields_orig_value"></a>
##### orig_value (required)

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `TunableChangedEvent`
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

- Schema name: `TunableEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SYSCTL"

`SYSCTL`: `var` is a sysctl name (e.g. `kernel.watchdog`) and `value` is its corresponding value (e.g. `0`). `UDEV`: `var` is a udev rules file name (e.g. `10-disable-usb`, `.rules` suffix will be appended automatically) and `value` is its contents (e.g. `BUS=="usb", OPTIONS+="ignore_device"`). `ZFS`: `var` is a ZFS kernel module parameter name (e.g. `zfs_dirty_data_max_max`) and `value` is its value (e.g. `783091712`).
###### Must be one of:

- "SYSCTL"
- "UDEV"
- "ZFS"

<a id="headingCHANGED_fields_var"></a>
<a id="CHANGED_fields_var"></a>
##### var (required)

- Schema name: `Var`
- Type: string

Name or identifier of the system parameter to tune.

<a id="headingCHANGED_fields_value"></a>
<a id="CHANGED_fields_value"></a>
##### value (required)

- Schema name: `Value`
- Type: string

Value to assign to the tunable parameter.

<a id="headingCHANGED_fields_comment"></a>
<a id="CHANGED_fields_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Optional descriptive comment explaining the purpose of this tunable.

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this tunable is active and should be applied.

<a id="headingCHANGED_fields_update_initramfs"></a>
<a id="CHANGED_fields_update_initramfs"></a>
##### update_initramfs

- Schema name: `Update Initramfs`
- Type: boolean
- Default: true

If `false`, then initramfs will not be updated after creating a ZFS tunable and you will need to run `system boot update_initramfs` manually.

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the tunable configuration.

<a id="headingCHANGED_fields_orig_value"></a>
<a id="CHANGED_fields_orig_value"></a>
##### orig_value (required)

- Schema name: `Orig Value`
- Type: string

Original system value of the parameter before this tunable was applied.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `TunableRemovedEvent`
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
