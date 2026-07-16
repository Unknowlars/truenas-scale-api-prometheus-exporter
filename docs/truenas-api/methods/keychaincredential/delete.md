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

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "keychaincredential.delete", "params": [ 13 ] }

## Required Roles

- `KEYCHAIN_CREDENTIAL_WRITE`

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

Unique identifier of the keychain credential to delete.

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"cascade": false}

Options controlling the deletion behavior.
- No Additional Properties
##### cascade

- Schema name: `Cascade`
- Type: boolean
- Default: false

Whether to force deletion even if the credential is in use by other services.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
