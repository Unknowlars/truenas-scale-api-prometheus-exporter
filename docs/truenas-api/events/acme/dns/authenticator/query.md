---
title: acme.dns.authenticator.query
kind: event
source_rst: _sources/api_events_acme.dns.authenticator.query.rst.txt
source_html: api_events_acme.dns.authenticator.query.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# acme.dns.authenticator.query

## Summary

Sent on acme.dns.authenticator changes.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### ADDED

- Schema name: `ACMEDNSAuthenticatorAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ACMEDNSAuthenticatorEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

##### attributes (required)

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

### CHANGED

- Schema name: `ACMEDNSAuthenticatorChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `ACMEDNSAuthenticatorEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the DNS authenticator.

##### attributes (required)

- Schema name: `Attributes`

Authentication credentials and configuration (masked for security).

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the DNS authenticator.

### REMOVED

- Schema name: `ACMEDNSAuthenticatorRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../../shared/query_methods.md)
