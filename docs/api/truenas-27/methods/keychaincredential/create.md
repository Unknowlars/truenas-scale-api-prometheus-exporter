---
title: keychaincredential.create
kind: method
source_rst: _sources/api_methods_keychaincredential.create.rst.txt
source_html: api_methods_keychaincredential.create.html
required_roles:
  - KEYCHAIN_CREDENTIAL_WRITE
---

# keychaincredential.create

## Summary

Create a Keychain Credential.

The following `type`s are supported: * `SSH_KEY_PAIR` * `SSH_CREDENTIALS`

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "keychaincredential.create", "params": [{ "name": "Work SSH connection", "type": "SSH_CREDENTIALS", "attributes": { "host": "work.freenas.org", "private_key": 12, "remote_host_key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMn1VjdSMatGnxbOsrneKyai+dh6d4Hm" } }] }

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

#### Parameter 1: keychain_credential_create

<a id="Call_parameters_items_i0"></a>
#### keychain_credential_create

- Schema name: `keychain_credential_create`

Credential configuration data for the new keychain entry.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [KeychainCredentialCreateSSHKeyPairEntry](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Schema name: `KeychainCredentialCreateSSHKeyPairEntry`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i0_name"></a>
<a id="Call_parameters_items_i0_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_anyOf_i0_type"></a>
<a id="Call_parameters_items_i0_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH key pairs.
- Specific value: `"SSH_KEY_PAIR"`

<a id="headingCall_parameters_items_i0_anyOf_i0_attributes"></a>
<a id="Call_parameters_items_i0_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH key pair attributes including public and private keys.
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i0_attributes_private_key"></a>
<a id="Call_parameters_items_i0_anyOf_i0_attributes_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="Call_parameters_items_i0_anyOf_i0_attributes_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_private_key_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_anyOf_i0_attributes_public_key"></a>
<a id="Call_parameters_items_i0_anyOf_i0_attributes_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="Call_parameters_items_i0_anyOf_i0_attributes_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i0_attributes_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [KeychainCredentialCreateSSHCredentialsEntry](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Schema name: `KeychainCredentialCreateSSHCredentialsEntry`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i1_name"></a>
<a id="Call_parameters_items_i0_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_anyOf_i1_type"></a>
<a id="Call_parameters_items_i0_anyOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH connection credentials.
- Specific value: `"SSH_CREDENTIALS"`

<a id="headingCall_parameters_items_i0_anyOf_i1_attributes"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH connection attributes including host, authentication, and connection settings.
- No Additional Properties
<a id="headingCall_parameters_items_i0_anyOf_i1_attributes_host"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingCall_parameters_items_i0_anyOf_i1_attributes_port"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingCall_parameters_items_i0_anyOf_i1_attributes_username"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingCall_parameters_items_i0_anyOf_i1_attributes_private_key"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingCall_parameters_items_i0_anyOf_i1_attributes_remote_host_key"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingCall_parameters_items_i0_anyOf_i1_attributes_connect_timeout"></a>
<a id="Call_parameters_items_i0_anyOf_i1_attributes_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

The newly created keychain credential entry.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [SSHKeyPairEntry](#tab-pane_Return_value_anyOf_i0)

- Schema name: `SSHKeyPairEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_id"></a>
<a id="Return_value_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingReturn_value_anyOf_i0_name"></a>
<a id="Return_value_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_type"></a>
<a id="Return_value_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH key pairs.
- Specific value: `"SSH_KEY_PAIR"`

<a id="headingReturn_value_anyOf_i0_attributes"></a>
<a id="Return_value_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH key pair attributes including public and private keys.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_attributes_private_key"></a>
<a id="Return_value_anyOf_i0_attributes_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="Return_value_anyOf_i0_attributes_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_attributes_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_attributes_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_attributes_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_attributes_private_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_attributes_public_key"></a>
<a id="Return_value_anyOf_i0_attributes_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="Return_value_anyOf_i0_attributes_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_attributes_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_attributes_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_attributes_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_attributes_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [SSHCredentialsEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `SSHCredentialsEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_type"></a>
<a id="Return_value_anyOf_i1_type"></a>
###### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH connection credentials.
- Specific value: `"SSH_CREDENTIALS"`

<a id="headingReturn_value_anyOf_i1_attributes"></a>
<a id="Return_value_anyOf_i1_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH connection attributes including host, authentication, and connection settings.
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_attributes_host"></a>
<a id="Return_value_anyOf_i1_attributes_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingReturn_value_anyOf_i1_attributes_port"></a>
<a id="Return_value_anyOf_i1_attributes_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingReturn_value_anyOf_i1_attributes_username"></a>
<a id="Return_value_anyOf_i1_attributes_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingReturn_value_anyOf_i1_attributes_private_key"></a>
<a id="Return_value_anyOf_i1_attributes_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingReturn_value_anyOf_i1_attributes_remote_host_key"></a>
<a id="Return_value_anyOf_i1_attributes_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingReturn_value_anyOf_i1_attributes_connect_timeout"></a>
<a id="Return_value_anyOf_i1_attributes_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
