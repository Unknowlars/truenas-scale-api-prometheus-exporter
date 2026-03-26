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

If the certificate is an ACME based certificate, certificate service will try to revoke the certificate by updating it's status with the ACME server, if it fails an exception is raised and the certificate is not deleted from the system. However, if `force` is set to True, certificate is deleted from the system even if some error occurred while revoking the certificate with the ACME Server

.. examples(websocket)::

Delete certificate of `id`

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "certificate.delete", "params": [ 1, true ] }

This method is a job.

## Required Roles

- `CERTIFICATE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the certificate to delete.

#### Parameter 2: force

#### force

- Schema name: `force`
- Type: boolean
- Default: false

Whether to force deletion even if certificate is in use.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the certificate is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
