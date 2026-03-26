---
title: acme.dns.authenticator.authenticator_schemas
kind: method
source_rst: _sources/api_methods_acme.dns.authenticator.authenticator_schemas.rst.txt
source_html: api_methods_acme.dns.authenticator.authenticator_schemas.html
required_roles:
  - READONLY_ADMIN
---

# acme.dns.authenticator.authenticator_schemas

## Summary

Get the schemas for all DNS providers we support for ACME DNS Challenge and the respective attributes required for connecting to them while validating a DNS Challenge

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Available DNS authenticator schemas with their configuration requirements.
- No Additional Items

#### Each item of this array must be:

#### ACMEDNSAuthenticatorSchema

- Schema name: `ACMEDNSAuthenticatorSchema`
- Type: object
- No Additional Properties
##### key (required)

- Schema name: `Key`
- Type: string

Unique identifier for the DNS authenticator type.

##### schema (required)

- Schema name: `ACMEDNSAuthenticatorAttributeSchema`
- Type: object

Schema definition for the authenticator's required attributes.
###### _name_ (required)

- Schema name: `Name`
- Type: string

Internal name of the schema attribute.

###### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the schema attribute.

###### _required_ (required)

- Schema name: `Required`
- Type: boolean

Whether this attribute is required for the authenticator.

###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
