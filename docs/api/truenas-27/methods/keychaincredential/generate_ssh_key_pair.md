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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `KeychainCredentialGenerateSshKeyPairResult`
- Type: object

KeychainCredentialGenerateSshKeyPairResult return fields.
- No Additional Properties
<a id="headingReturn_value_private_key"></a>
<a id="Return_value_private_key"></a>
#### private_key (required)

- Schema name: `Private Key`
- Type: string

Generated SSH private key in PEM format.

<a id="headingReturn_value_public_key"></a>
<a id="Return_value_public_key"></a>
#### public_key (required)

- Schema name: `Public Key`
- Type: string

Generated SSH public key in OpenSSH format.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
