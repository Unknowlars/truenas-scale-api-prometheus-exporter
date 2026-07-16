---
title: webshare.config
kind: method
source_rst: _sources/api_methods_webshare.config.rst.txt
source_html: api_methods_webshare.config.html
required_roles:
  - SHARING_WEBSHARE_READ
---

# webshare.config

## Required Roles

- `SHARING_WEBSHARE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `WebshareEntry`
- Type: object

TrueNAS Webshare server configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Webshare service configuration.

#### bindip (required)

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS Webshare server.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### search (required)

- Schema name: `Search`
- Type: boolean

Search indexing is enabled.

#### passkey (required)

- Schema name: `Passkey`
- Type: enum (of string)

Passkey authentication mode.

#### groups (required)

- Schema name: `Groups`
- Type: array of string

A list of AD/LDAP group names whose members will be granted access to Webshare.
- No Additional Items

##### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
