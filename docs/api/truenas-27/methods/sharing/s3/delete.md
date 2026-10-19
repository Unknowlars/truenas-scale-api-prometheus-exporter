---
title: sharing.s3.delete
kind: method
source_rst: _sources/api_methods_sharing.s3.delete.rst.txt
source_html: api_methods_sharing.s3.delete.html
required_roles:
  - SHARING_S3_WRITE
---

# sharing.s3.delete

## Summary

Deregister S3 bucket `id`.

The bucket's dataset and every object in it are left in place, retained objects included; the S3 service simply stops serving them. Restarts the S3 service.

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

ID of the bucket to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the bucket is successfully deregistered.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
