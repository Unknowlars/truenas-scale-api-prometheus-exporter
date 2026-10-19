---
title: kmip.config
kind: method
source_rst: _sources/api_methods_kmip.config.rst.txt
source_html: api_methods_kmip.config.html
required_roles:
  - KMIP_READ
---

# kmip.config

## Required Roles

- `KMIP_READ`

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

- Schema name: `KMIPEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the KMIP configuration.

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether KMIP (Key Management Interoperability Protocol) is enabled.

<a id="headingReturn_value_manage_sed_disks"></a>
<a id="Return_value_manage_sed_disks"></a>
#### manage_sed_disks (required)

- Schema name: `Manage Sed Disks`
- Type: boolean

Whether to use KMIP for managing SED (Self-Encrypting Drive) keys.

<a id="headingReturn_value_manage_zfs_keys"></a>
<a id="Return_value_manage_zfs_keys"></a>
#### manage_zfs_keys (required)

- Schema name: `Manage Zfs Keys`
- Type: boolean

Whether to use KMIP for managing ZFS encryption keys.

<a id="headingReturn_value_certificate"></a>
<a id="Return_value_certificate"></a>
#### certificate (required)

- Schema name: `Certificate`

ID of the client certificate for KMIP authentication or `null`.
<a id="Return_value_certificate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_certificate_authority"></a>
<a id="Return_value_certificate_authority"></a>
#### certificate_authority (required)

- Schema name: `Certificate Authority`

ID of the certificate authority for server verification or `null`.
<a id="Return_value_certificate_authority_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_certificate_authority_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_certificate_authority_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_certificate_authority_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_certificate_authority_anyOf_i1)

- Type: null

<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `Port`
- Type: integer

TCP port number for the KMIP server connection.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_server"></a>
<a id="Return_value_server"></a>
#### server (required)

- Schema name: `Server`

Hostname or IP address of the KMIP server or `null` if not configured.
<a id="Return_value_server_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_server_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_server_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_server_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_server_anyOf_i1)

- Type: null

<a id="headingReturn_value_ssl_version"></a>
<a id="Return_value_ssl_version"></a>
#### ssl_version (required)

- Schema name: `Ssl Version`
- Type: enum (of string)

SSL/TLS protocol version to use for KMIP connections.
##### Must be one of:

- "PROTOCOL_TLSv1"
- "PROTOCOL_TLSv1_1"
- "PROTOCOL_TLSv1_2"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
