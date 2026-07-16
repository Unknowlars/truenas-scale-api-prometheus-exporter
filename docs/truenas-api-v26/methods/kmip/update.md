---
title: kmip.update
kind: method
source_rst: _sources/api_methods_kmip.update.rst.txt
source_html: api_methods_kmip.update.html
required_roles:
  - KMIP_WRITE
---

# kmip.update

## Summary

Update KMIP Server Configuration.

The system authenticates to the remote KMIP server with a TLS handshake and synchronizes ZFS/SED keys between the local database and the server according to the configuration.

This method is a job.

## Required Roles

- `KMIP_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: kmip_update

#### kmip_update

- Schema name: `kmip_update`
- Type: object

KMIPUpdateArgs parameters.
- No Additional Properties
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether to enable KMIP functionality.

##### manage_sed_disks

- Schema name: `Manage Sed Disks`
- Type: boolean

Whether to use KMIP for managing SED (Self-Encrypting Drive) keys.

##### manage_zfs_keys

- Schema name: `Manage Zfs Keys`
- Type: boolean

Whether to use KMIP for managing ZFS encryption keys.

##### certificate

- Schema name: `Certificate`

ID of the client certificate for KMIP authentication or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### certificate_authority

- Schema name: `Certificate Authority`

ID of the certificate authority for server verification or `null`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### port

- Schema name: `Port`
- Type: integer

TCP port number for the KMIP server connection.
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### server

- Schema name: `Server`

Hostname or IP address of the KMIP server or `null` if not configured.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### ssl_version

- Schema name: `Ssl Version`
- Type: enum (of string)

SSL/TLS protocol version to use for KMIP connections.

##### force_clear

- Schema name: `Force Clear`
- Type: boolean

Whether to force clear existing keys when disabling KMIP.

##### change_server

- Schema name: `Change Server`
- Type: boolean

Whether the KMIP server configuration is being changed.

##### validate

- Schema name: `Validate`
- Type: boolean

Whether to validate the KMIP server connection before saving.

### Return value

- Schema name: `KMIPEntry`
- Type: object

The updated KMIP configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the KMIP configuration.

#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether KMIP (Key Management Interoperability Protocol) is enabled.

#### manage_sed_disks (required)

- Schema name: `Manage Sed Disks`
- Type: boolean

Whether to use KMIP for managing SED (Self-Encrypting Drive) keys.

#### manage_zfs_keys (required)

- Schema name: `Manage Zfs Keys`
- Type: boolean

Whether to use KMIP for managing ZFS encryption keys.

#### certificate (required)

- Schema name: `Certificate`

ID of the client certificate for KMIP authentication or `null`.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### certificate_authority (required)

- Schema name: `Certificate Authority`

ID of the certificate authority for server verification or `null`.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the KMIP server connection.
- Value must be greater or equal to `1` and lesser or equal to `65535`

#### server (required)

- Schema name: `Server`

Hostname or IP address of the KMIP server or `null` if not configured.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### ssl_version (required)

- Schema name: `Ssl Version`
- Type: enum (of string)

SSL/TLS protocol version to use for KMIP connections.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
