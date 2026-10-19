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

Delete DNS Authenticator of `id`.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

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

ID of the DNS authenticator to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` when the DNS authenticator is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
