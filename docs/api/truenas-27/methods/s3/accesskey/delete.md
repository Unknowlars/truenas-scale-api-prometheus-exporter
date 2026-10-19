---
title: s3.accesskey.delete
kind: method
source_rst: _sources/api_methods_s3.accesskey.delete.rst.txt
source_html: api_methods_s3.accesskey.delete.html
required_roles:
  - SHARING_S3_WRITE
---

# s3.accesskey.delete

## Summary

Delete S3 access key `id`.

## Required Roles

- `SHARING_S3_WRITE`

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

ID of the access key to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the access key is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
