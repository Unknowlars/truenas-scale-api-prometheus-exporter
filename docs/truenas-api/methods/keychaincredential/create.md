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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: keychain_credential_create

#### keychain_credential_create

- Schema name: `keychain_credential_create`

Credential configuration data for the new keychain entry.
##### Any of

###### KeychainCredentialCreateSSHKeyPairEntry

- Schema name: `KeychainCredentialCreateSSHKeyPairEntry`
- Type: object
- No Additional Properties
####### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

####### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH key pairs.

####### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH key pair attributes including public and private keys.
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

###### KeychainCredentialCreateSSHCredentialsEntry

- Type: string

###### Option 1

- Type: null

###### Option 2

- Type: string

###### Option 1

- Type: null

###### Option 2

- Schema name: `KeychainCredentialCreateSSHCredentialsEntry`
- Type: object
- No Additional Properties
####### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

####### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH connection credentials.

####### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH connection attributes including host, authentication, and connection settings.
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

### Return value

- Schema name: `Result`

The newly created keychain credential entry.
#### Any of

##### SSHKeyPairEntry

- Schema name: `SSHKeyPairEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

###### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH key pairs.

###### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH key pair attributes including public and private keys.
- No Additional Properties
####### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

##### SSHCredentialsEntry

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Schema name: `SSHCredentialsEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

###### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH connection credentials.

###### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH connection attributes including host, authentication, and connection settings.
- No Additional Properties
####### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

####### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

####### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

####### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

####### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

####### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
