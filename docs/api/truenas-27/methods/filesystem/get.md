---
title: filesystem.get
kind: method
source_rst: _sources/api_methods_filesystem.get.rst.txt
source_html: api_methods_filesystem.get.html
required_roles:
  - FULL_ADMIN
---

# filesystem.get

## Summary

Job to get contents of `path`.

This method is a job.

*This job MUST be used with* [core.download](../core/download.md).

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: path

<a id="Call_parameters_items_i0"></a>
#### path

- Schema name: `path`
- Type: string

Path of the file to read.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the file is successfully read.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
