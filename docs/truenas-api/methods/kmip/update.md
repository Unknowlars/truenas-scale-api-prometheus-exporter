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

System currently authenticates connection with remote KMIP Server with a TLS handshake. `certificate` and `certificate_authority` determine the certs which will be used to initiate the TLS handshake with `server`.

`validate` is enabled by default. When enabled, system will test connection to `server` making sure it's reachable.

`manage_zfs_keys`/`manage_sed_disks` when enabled will sync keys from local database to remote KMIP server. When disabled, if there are any keys left to be retrieved from the KMIP server, it will sync them back to local database.

`enabled` if true, cannot be set to disabled if there are existing keys pending to be synced. However users can still perform this action by enabling `force_clear`.

`ssl_version` can be specified to match the ssl configuration being used by KMIP server.

`change_server` is a boolean field which allows users to migrate data between two KMIP servers. System will first migrate keys from old KMIP server to local database and then migrate the keys from local database to new KMIP server. If it is unable to retrieve all the keys from old server, this will fail. Users can bypass this by enabling `force_clear`.

`force_clear` is a boolean option which when enabled will in this case remove all pending keys to be synced from database. It should be used with extreme caution as users may end up with not having ZFS dataset or SED disks keys leaving them locked forever. It is disabled by default.

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

- Schema name: `KmipEntry`
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
