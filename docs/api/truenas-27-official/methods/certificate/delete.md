---
title: certificate.delete
kind: method
source_rst: _sources/api_methods_certificate.delete.rst.txt
source_html: api_methods_certificate.delete.html
required_roles:
  - CERTIFICATE_WRITE
---

# certificate.delete

## Summary

Delete certificate of `id`.

If the certificate is an ACME based certificate, the certificate service will try to revoke the certificate by updating its status with the ACME server. If that fails, an exception is raised and the certificate is not deleted from the system. However, if `force` is set to `true`, the certificate is deleted from the system even if some error occurred while revoking the certificate with the ACME server.

This method is a job.

## Required Roles

- `CERTIFICATE_WRITE`

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

ID of the certificate to delete.

#### Parameter 2: force

<a id="Call_parameters_items_i1"></a>
#### force

- Schema name: `force`
- Type: boolean
- Default: false

Whether to force deletion even if certificate is in use.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the certificate is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
