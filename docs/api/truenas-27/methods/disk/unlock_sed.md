---
title: disk.unlock_sed
kind: method
source_rst: _sources/api_methods_disk.unlock_sed.rst.txt
source_html: api_methods_disk.unlock_sed.html
required_roles:
  - DISK_WRITE
---

# disk.unlock_sed

## Summary

Unlock specified `options.name` SED disk.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: disk_sed_unlock

<a id="Call_parameters_items_i0"></a>
#### disk_sed_unlock

- Schema name: `disk_sed_unlock`
- Type: object

DiskUnlockSedArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of disk to unlock.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_password"></a>
<a id="Call_parameters_items_i0_password"></a>
##### password

- Schema name: `Password`
- Default: null

Password for disk to unlock.
<a id="Call_parameters_items_i0_password_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_password_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_password_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns true if the disk unlock was successful.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
