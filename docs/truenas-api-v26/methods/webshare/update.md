---
title: webshare.update
kind: method
source_rst: _sources/api_methods_webshare.update.rst.txt
source_html: api_methods_webshare.update.html
required_roles:
  - SHARING_WEBSHARE_WRITE
---

# webshare.update

## Summary

Update Webshare Service Configuration.

## Required Roles

- `SHARING_WEBSHARE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: webshare_update

#### webshare_update

- Schema name: `webshare_update`
- Type: object

Updated webshare configuration data.
- No Additional Properties
##### bindip

- Schema name: `Bindip`
- Type: array of string

List of IP addresses used by the TrueNAS Webshare server.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### search

- Schema name: `Search`
- Type: boolean

Search indexing is enabled.

##### passkey

- Schema name: `Passkey`
- Type: enum (of string)

Passkey authentication mode.

##### groups

- Schema name: `Groups`
- Type: array of string

A list of AD/LDAP group names whose members will be granted access to Webshare.
- No Additional Items

###### Each item of this array must be:

- Type: string

### Return value

- Schema name: `WebshareEntry`
- Type: object

The updated Webshare service configuration.
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
