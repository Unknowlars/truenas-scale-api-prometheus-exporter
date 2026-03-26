---
title: keychaincredential.setup_ssh_connection
kind: method
source_rst: _sources/api_methods_keychaincredential.setup_ssh_connection.rst.txt
source_html: api_methods_keychaincredential.setup_ssh_connection.html
required_roles:
  - KEYCHAIN_CREDENTIAL_WRITE
---

# keychaincredential.setup_ssh_connection

## Summary

Creates an SSH Connection performing the following steps:

1) Generate SSH Key Pair if required 2) Set up SSH Credentials based on `setup_type`

In case (2) fails, it will be ensured that SSH Key Pair generated (if applicable) in the process is removed.

## Required Roles

- `KEYCHAIN_CREDENTIAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`

SSH connection setup configuration (manual or semi-automatic).

### Return value

- Schema name: `SSHCredentialsEntry`
- Type: object

The created SSH connection credential.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

#### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

#### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH connection credentials.

#### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH connection attributes including host, authentication, and connection settings.
- No Additional Properties
##### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

##### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

##### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

##### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

##### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

##### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
