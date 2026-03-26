---
title: ftp.config
kind: method
source_rst: _sources/api_methods_ftp.config.rst.txt
source_html: api_methods_ftp.config.html
required_roles:
  - SHARING_FTP_READ
---

# ftp.config

## Required Roles

- `SHARING_FTP_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `FtpEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

#### port (required)

- Schema name: `Port`
- Type: integer

TCP port number on which the FTP service listens for incoming connections.
- Value must be greater or equal to `1` and lesser or equal to `65535`

#### clients (required)

- Schema name: `Clients`
- Type: integer

Maximum number of simultaneous client connections allowed.
- Value must be greater or equal to `1` and lesser or equal to `10000`

#### ipconnections (required)

- Schema name: `Ipconnections`
- Type: integer

Maximum number of connections allowed from a single IP address. 0 means unlimited.
- Value must be greater or equal to `0` and lesser or equal to `1000`

#### loginattempt (required)

- Schema name: `Loginattempt`
- Type: integer

Maximum number of failed login attempts before blocking an IP address. 0 disables this limit.
- Value must be greater or equal to `0` and lesser or equal to `1000`

#### timeout (required)

- Schema name: `Timeout`
- Type: integer

Idle timeout in seconds before disconnecting inactive clients. 0 disables timeout.
- Value must be greater or equal to `0` and lesser or equal to `10000`

#### timeout_notransfer (required)

- Schema name: `Timeout Notransfer`
- Type: integer

Timeout in seconds for clients that connect but do not transfer data. 0 disables timeout.
- Value must be greater or equal to `0` and lesser or equal to `10000`

#### onlyanonymous (required)

- Schema name: `Onlyanonymous`
- Type: boolean

Whether to allow only anonymous FTP access, disabling authenticated user login.

#### anonpath (required)

- Schema name: `Anonpath`

Filesystem path for anonymous FTP users. `null` to use the default anonymous FTP directory.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### onlylocal (required)

- Schema name: `Onlylocal`
- Type: boolean

Whether to allow only local system users to login, disabling anonymous access.

#### banner (required)

- Schema name: `Banner`
- Type: string

Welcome message displayed to FTP clients upon connection.

#### filemask (required)

- Schema name: `Filemask`
- Type: string

Default Unix permissions (umask) for files created by FTP users.

#### dirmask (required)

- Schema name: `Dirmask`
- Type: string

Default Unix permissions (umask) for directories created by FTP users.

#### fxp (required)

- Schema name: `Fxp`
- Type: boolean

Whether to enable File eXchange Protocol (FXP) for server-to-server transfers.

#### resume (required)

- Schema name: `Resume`
- Type: boolean

Whether to allow clients to resume interrupted file transfers.

#### defaultroot (required)

- Schema name: `Defaultroot`
- Type: boolean

Whether to restrict users to their home directories (chroot jail).

#### ident (required)

- Schema name: `Ident`
- Type: boolean

Whether to perform RFC 1413 ident lookups on connecting clients.

#### reversedns (required)

- Schema name: `Reversedns`
- Type: boolean

Whether to perform reverse DNS lookups on client IP addresses for logging.

#### masqaddress (required)

- Schema name: `Masqaddress`
- Type: string

Public IP address to advertise to clients for passive mode connections when behind NAT.

#### passiveportsmin (required)

- Schema name: `Passiveportsmin`
- Type: integer

Minimum port number for passive mode data connections. Must be 0 or between 1024-65535.

#### passiveportsmax (required)

- Schema name: `Passiveportsmax`
- Type: integer

Maximum port number for passive mode data connections. Must be 0 or between 1024-65535.

#### localuserbw (required)

- Schema name: `Localuserbw`
- Type: integer

Maximum upload bandwidth in KiB/s for local users. 0 means unlimited.
- Value must be greater or equal to `0`

#### localuserdlbw (required)

- Schema name: `Localuserdlbw`
- Type: integer

Maximum download bandwidth in KiB/s for local users. 0 means unlimited.
- Value must be greater or equal to `0`

#### anonuserbw (required)

- Schema name: `Anonuserbw`
- Type: integer

Maximum upload bandwidth in KiB/s for anonymous users. 0 means unlimited.
- Value must be greater or equal to `0`

#### anonuserdlbw (required)

- Schema name: `Anonuserdlbw`
- Type: integer

Maximum download bandwidth in KiB/s for anonymous users. 0 means unlimited.
- Value must be greater or equal to `0`

#### tls (required)

- Schema name: `Tls`
- Type: boolean

Whether to enable TLS/SSL encryption for FTP connections.

#### tls_policy (required)

- Schema name: `Tls Policy`
- Type: enum (of string)

TLS policy for connections. Values include: `"on"` (required), `"off"` (disabled), `"data"` (data only), `"auth"` (authentication only), `"ctrl"` (control only), or combinations with `+` and `!` modifiers.

#### tls_opt_allow_client_renegotiations (required)

- Schema name: `Tls Opt Allow Client Renegotiations`
- Type: boolean

Whether to allow TLS clients to initiate renegotiation of the TLS connection.

#### tls_opt_allow_dot_login (required)

- Schema name: `Tls Opt Allow Dot Login`
- Type: boolean

Whether to allow .ftpaccess files to override TLS requirements for specific users.

#### tls_opt_allow_per_user (required)

- Schema name: `Tls Opt Allow Per User`
- Type: boolean

Whether to allow per-user TLS configuration overrides.

#### tls_opt_common_name_required (required)

- Schema name: `Tls Opt Common Name Required`
- Type: boolean

Whether to require client certificates to have a Common Name field.

#### tls_opt_enable_diags (required)

- Schema name: `Tls Opt Enable Diags`
- Type: boolean

Whether to enable detailed TLS diagnostic logging.

#### tls_opt_export_cert_data (required)

- Schema name: `Tls Opt Export Cert Data`
- Type: boolean

Whether to export client certificate data to environment variables.

#### tls_opt_no_empty_fragments (required)

- Schema name: `Tls Opt No Empty Fragments`
- Type: boolean

Whether to disable empty TLS record fragments to improve compatibility with some clients. Disabling increases vulnerability to some attack vectors.

#### tls_opt_no_session_reuse_required (required)

- Schema name: `Tls Opt No Session Reuse Required`
- Type: boolean

Whether to disable the requirement for TLS session reuse.

#### tls_opt_stdenvvars (required)

- Schema name: `Tls Opt Stdenvvars`
- Type: boolean

Whether to export standard TLS environment variables for use by external programs.

#### tls_opt_dns_name_required (required)

- Schema name: `Tls Opt Dns Name Required`
- Type: boolean

Whether to require client certificates to contain a DNS name in the Subject Alternative Name extension. The `reversedns` setting must also be enabled.

#### tls_opt_ip_address_required (required)

- Schema name: `Tls Opt Ip Address Required`
- Type: boolean

Whether to require client certificates to contain an IP address in the Subject Alternative Name extension.

#### ssltls_certificate (required)

- Schema name: `Ssltls Certificate`

ID of the certificate to use for TLS/SSL connections. `null` to use the default system certificate.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### options (required)

- Schema name: `Options`
- Type: string

Additional ProFTPD configuration directives to include in the server configuration. Manual directives may render the FTP service non-functional and should be used with caution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
