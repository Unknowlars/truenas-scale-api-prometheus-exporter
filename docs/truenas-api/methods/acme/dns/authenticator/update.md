---
title: acme.dns.authenticator.update
kind: method
source_rst: _sources/api_methods_acme.dns.authenticator.update.rst.txt
source_html: api_methods_acme.dns.authenticator.update.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# acme.dns.authenticator.update

## Summary

Update DNS Authenticator of `id`

.. examples(websocket)::

Update a DNS Authenticator of `id`

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "acme.dns.authenticator.update", "params": [ 1, { "name": "route53_authenticator", "attributes": { "access_key_id": "AQX13", "secret_access_key": "JKW90", "authenticator": "route53" } } ] }

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

ID of the DNS authenticator to update.

#### Parameter 2: dns_authenticator_update

#### dns_authenticator_update

- Schema name: `dns_authenticator_update`
- Type: object

Updated DNS authenticator configuration data.
- No Additional Properties
##### attributes

- Schema name: `Attributes`

Authentication credentials and configuration for the DNS provider.

##### name

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

### Return value

- Schema name: `ACMEDNSAuthenticatorEntry`
- Type: object

The updated DNS authenticator configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

#### attributes (required)

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
