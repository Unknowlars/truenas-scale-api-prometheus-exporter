---
title: acme.dns.authenticator.delete
kind: method
source_rst: _sources/api_methods_acme.dns.authenticator.delete.rst.txt
source_html: api_methods_acme.dns.authenticator.delete.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# acme.dns.authenticator.delete

## Summary

Delete DNS Authenticator of `id`

.. examples(websocket)::

Delete a DNS Authenticator of `id`

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "acme.dns.authenticator.delete", "params": [ 1 ] }

## Required Roles

- `NETWORK_INTERFACE_WRITE`

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

ID of the DNS authenticator to delete.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the DNS authenticator is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
