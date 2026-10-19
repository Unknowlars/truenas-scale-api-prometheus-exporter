---
title: keychaincredential.delete
kind: method
source_rst: _sources/api_methods_keychaincredential.delete.rst.txt
source_html: api_methods_keychaincredential.delete.html
required_roles:
  - KEYCHAIN_CREDENTIAL_WRITE
---

# keychaincredential.delete

## Summary

Delete Keychain Credential with specific `id`.

## Required Roles

- `KEYCHAIN_CREDENTIAL_WRITE`

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

Unique identifier of the keychain credential to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default: {"cascade": false}

Options controlling the deletion behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_cascade"></a>
<a id="Call_parameters_items_i1_cascade"></a>
##### cascade

- Schema name: `Cascade`
- Type: boolean
- Default: false

Whether to force deletion even if the credential is in use by other services.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
