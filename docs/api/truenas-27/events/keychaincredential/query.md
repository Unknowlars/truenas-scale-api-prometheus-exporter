---
title: keychaincredential.query
kind: event
source_rst: _sources/api_events_keychaincredential.query.rst.txt
source_html: api_events_keychaincredential.query.html
required_roles:
  - KEYCHAIN_CREDENTIAL_READ
---

# keychaincredential.query

## Summary

Sent on keychaincredential changes.

## Required Roles

- `KEYCHAIN_CREDENTIAL_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `KeychainCredentialAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
###### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingADDED_fields_attributes"></a>
<a id="ADDED_fields_attributes"></a>
##### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="ADDED_fields_attributes_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_ADDED_fields_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingADDED_fields_attributes_anyOf_i0_private_key"></a>
<a id="ADDED_fields_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="ADDED_fields_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_anyOf_i0_public_key"></a>
<a id="ADDED_fields_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="ADDED_fields_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_ADDED_fields_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_anyOf_i1_host"></a>
<a id="ADDED_fields_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingADDED_fields_attributes_anyOf_i1_port"></a>
<a id="ADDED_fields_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingADDED_fields_attributes_anyOf_i1_username"></a>
<a id="ADDED_fields_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingADDED_fields_attributes_anyOf_i1_private_key"></a>
<a id="ADDED_fields_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingADDED_fields_attributes_anyOf_i1_remote_host_key"></a>
<a id="ADDED_fields_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingADDED_fields_attributes_anyOf_i1_connect_timeout"></a>
<a id="ADDED_fields_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `KeychainCredentialChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
###### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingCHANGED_fields_attributes"></a>
<a id="CHANGED_fields_attributes"></a>
##### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="CHANGED_fields_attributes_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_CHANGED_fields_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingCHANGED_fields_attributes_anyOf_i0_private_key"></a>
<a id="CHANGED_fields_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="CHANGED_fields_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_anyOf_i0_public_key"></a>
<a id="CHANGED_fields_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="CHANGED_fields_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_CHANGED_fields_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_anyOf_i1_host"></a>
<a id="CHANGED_fields_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingCHANGED_fields_attributes_anyOf_i1_port"></a>
<a id="CHANGED_fields_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingCHANGED_fields_attributes_anyOf_i1_username"></a>
<a id="CHANGED_fields_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingCHANGED_fields_attributes_anyOf_i1_private_key"></a>
<a id="CHANGED_fields_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingCHANGED_fields_attributes_anyOf_i1_remote_host_key"></a>
<a id="CHANGED_fields_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingCHANGED_fields_attributes_anyOf_i1_connect_timeout"></a>
<a id="CHANGED_fields_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `KeychainCredentialRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
