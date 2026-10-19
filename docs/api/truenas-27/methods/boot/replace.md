---
title: boot.replace
kind: method
source_rst: _sources/api_methods_boot.replace.rst.txt
source_html: api_methods_boot.replace.html
required_roles:
  - DISK_WRITE
---

# boot.replace

## Summary

Replace device `label` on boot pool with `dev`.

This method is a job.

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

#### Parameter 1: label

<a id="Call_parameters_items_i0"></a>
#### label

- Schema name: `label`
- Type: string

Label of the disk in the boot pool to replace.

#### Parameter 2: dev

<a id="Call_parameters_items_i1"></a>
#### dev

- Schema name: `dev`
- Type: string

Device name or path of the replacement disk.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the disk replacement is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
