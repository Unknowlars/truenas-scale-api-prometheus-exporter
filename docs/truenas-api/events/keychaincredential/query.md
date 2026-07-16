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

### ADDED

- Schema name: `KeychainCredentialAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

##### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication

##### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
###### Any of

####### SSHKeyPair

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
######## private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### SSHCredentials

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
######## host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

######## port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

######## username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

######## private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

######## remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

######## connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

### CHANGED

- Schema name: `KeychainCredentialChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

##### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

##### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication

##### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
###### Any of

####### SSHKeyPair

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
######## private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### SSHCredentials

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
######## host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

######## port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

######## username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

######## private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

######## remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

######## connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

### REMOVED

- Schema name: `KeychainCredentialRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
