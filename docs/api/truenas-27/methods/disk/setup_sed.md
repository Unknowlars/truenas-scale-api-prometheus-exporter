---
title: disk.setup_sed
kind: method
source_rst: _sources/api_methods_disk.setup_sed.rst.txt
source_html: api_methods_disk.setup_sed.html
required_roles:
  - DISK_WRITE
---

# disk.setup_sed

## Summary

Setup specified `options.name` SED disk.

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

#### Parameter 1: disk_sed_setup

<a id="Call_parameters_items_i0"></a>
#### disk_sed_setup

- Schema name: `disk_sed_setup`
- Type: object

DiskSetupSedArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of disk to setup.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_password"></a>
<a id="Call_parameters_items_i0_password"></a>
##### password

- Schema name: `Password`
- Default: null

Password to use to setup the disk. If this is not set, first if a password on disk is set, it will be used else global configured SED password will be used.
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

Returns true if the disk setup was successful.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
