---
title: keychaincredential.generate_ssh_key_pair
kind: method
source_rst: _sources/api_methods_keychaincredential.generate_ssh_key_pair.rst.txt
source_html: api_methods_keychaincredential.generate_ssh_key_pair.html
required_roles:
  - KEYCHAIN_CREDENTIAL_WRITE
---

# keychaincredential.generate_ssh_key_pair

## Summary

Generate a public/private key pair (useful for `SSH_KEY_PAIR` type)

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "keychaincredential.generate_ssh_key_pair", "params": [] }

## Required Roles

- `KEYCHAIN_CREDENTIAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `KeychainCredentialGenerateSshKeyPairResult`
- Type: object

KeychainCredentialGenerateSshKeyPairResult return fields.
- No Additional Properties
#### private_key (required)

- Schema name: `Private Key`
- Type: string

Generated SSH private key in PEM format.

#### public_key (required)

- Schema name: `Public Key`
- Type: string

Generated SSH public key in OpenSSH format.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
