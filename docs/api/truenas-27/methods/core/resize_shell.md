---
title: core.resize_shell
kind: method
source_rst: _sources/api_methods_core.resize_shell.rst.txt
source_html: api_methods_core.resize_shell.html
required_roles:
  []
---

# core.resize_shell

## Summary

Resize terminal session (/websocket/shell) to cols x rows

## Required Roles

- None documented.

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
- Type: string

Shell session identifier.

#### Parameter 2: cols

<a id="Call_parameters_items_i1"></a>
#### cols

- Schema name: `cols`
- Type: integer

New terminal width in columns.

#### Parameter 3: rows

<a id="Call_parameters_items_i2"></a>
#### rows

- Schema name: `rows`
- Type: integer

New terminal height in rows.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the shell is successfully resized.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
