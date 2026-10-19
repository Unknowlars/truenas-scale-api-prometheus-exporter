---
title: boot.detach
kind: method
source_rst: _sources/api_methods_boot.detach.rst.txt
source_html: api_methods_boot.detach.html
required_roles:
  - DISK_WRITE
---

# boot.detach

## Summary

Detach given `dev` from boot pool.

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

Device name or path to detach from the boot pool.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the disk is successfully detached from the boot pool.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
