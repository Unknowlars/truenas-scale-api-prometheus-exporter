---
title: boot.attach
kind: method
source_rst: _sources/api_methods_boot.attach.rst.txt
source_html: api_methods_boot.attach.html
required_roles:
  - DISK_WRITE
---

# boot.attach

## Summary

Attach a disk to the boot pool, turning a stripe into a mirror.

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

#### Parameter 1: dev

<a id="Call_parameters_items_i0"></a>
#### dev

- Schema name: `dev`
- Type: string

Device name or path to attach to the boot pool.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for the attach operation.
- No Additional Properties
<a id="headingCall_parameters_items_i1_expand"></a>
<a id="Call_parameters_items_i1_expand"></a>
##### expand

- Schema name: `Expand`
- Type: boolean
- Default: false

Whether to expand the boot pool after attaching the disk.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the disk is successfully attached to the boot pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
