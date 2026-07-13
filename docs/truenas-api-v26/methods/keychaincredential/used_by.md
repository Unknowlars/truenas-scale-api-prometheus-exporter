---
title: keychaincredential.used_by
kind: method
source_rst: _sources/api_methods_keychaincredential.used_by.rst.txt
source_html: api_methods_keychaincredential.used_by.html
required_roles:
  - KEYCHAIN_CREDENTIAL_READ
---

# keychaincredential.used_by

## Summary

Returns list of objects that use this credential.

## Required Roles

- `KEYCHAIN_CREDENTIAL_READ`

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

Unique identifier of the keychain credential to check usage for.

### Return value

- Schema name: `Result`
- Type: array of object

Array of services or features using this keychain credential.
- No Additional Items

#### Each item of this array must be:

#### UsedKeychainCredential

- Schema name: `UsedKeychainCredential`
- Type: object
- No Additional Properties
##### title (required)

- Schema name: `Title`
- Type: string

Human-readable description of where the credential is being used.

##### unbind_method (required)

- Schema name: `Unbind Method`
- Type: enum (of string)

How to remove the credential dependency. `delete`: Delete the dependent configuration `disable`: Disable the dependent service or feature

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
