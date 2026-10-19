---
title: disk.reset_sed
kind: method
source_rst: _sources/api_methods_disk.reset_sed.rst.txt
source_html: api_methods_disk.reset_sed.html
required_roles:
  - DISK_WRITE
---

# disk.reset_sed

## Summary

Reset SED disk.

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

#### Parameter 1: disk_sed_reset

<a id="Call_parameters_items_i0"></a>
#### disk_sed_reset

- Schema name: `disk_sed_reset`
- Type: object

DiskResetSedArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of disk to reset.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_psid"></a>
<a id="Call_parameters_items_i0_psid"></a>
##### psid (required)

- Schema name: `Psid`
- Type: string

PID of disk to reset.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns true if the disk reset was successful.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
