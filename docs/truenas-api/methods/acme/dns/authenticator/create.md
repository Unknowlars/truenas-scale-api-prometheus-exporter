---
title: acme.dns.authenticator.create
kind: method
source_rst: _sources/api_methods_acme.dns.authenticator.create.rst.txt
source_html: api_methods_acme.dns.authenticator.create.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# acme.dns.authenticator.create

## Summary

Create a DNS Authenticator

Create a specific DNS Authenticator containing required authentication details for the said provider to successfully connect with it

.. examples(websocket)::

Create a DNS Authenticator for Route53

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "acme.dns.authenticator.create", "params": [{ "name": "route53_authenticator", "attributes": { "access_key_id": "AQX13", "secret_access_key": "JKW90", "authenticator": "route53" } }] }

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: dns_authenticator_create

#### dns_authenticator_create

- Schema name: `dns_authenticator_create`
- Type: object

DNSAuthenticatorCreateArgs parameters.
- No Additional Properties
##### attributes (required)

- Schema name: `Attributes`

Authentication credentials and configuration for the DNS provider.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

### Return value

- Schema name: `ACMEDNSAuthenticatorEntry`
- Type: object

The created DNS authenticator configuration.
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
