---
title: ftp.update
kind: method
source_rst: _sources/api_methods_ftp.update.rst.txt
source_html: api_methods_ftp.update.html
required_roles:
  - SHARING_FTP_WRITE
---

# ftp.update

## Summary

Update ftp service configuration.

## Required Roles

- `SHARING_FTP_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: ftp_update

<a id="Call_parameters_items_i0"></a>
#### ftp_update

- Schema name: `ftp_update`
- Type: object

FTPUpdateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_port"></a>
<a id="Call_parameters_items_i0_port"></a>
##### port

- Schema name: `Port`
- Type: integer

TCP port number on which the FTP service listens for incoming connections.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingCall_parameters_items_i0_clients"></a>
<a id="Call_parameters_items_i0_clients"></a>
##### clients

- Schema name: `Clients`
- Type: integer

Maximum number of simultaneous client connections allowed.
- Value must be greater or equal to `1` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i0_ipconnections"></a>
<a id="Call_parameters_items_i0_ipconnections"></a>
##### ipconnections

- Schema name: `Ipconnections`
- Type: integer

Maximum number of connections allowed from a single IP address. 0 means unlimited.
- Value must be greater or equal to `0` and lesser or equal to `1000`

<a id="headingCall_parameters_items_i0_loginattempt"></a>
<a id="Call_parameters_items_i0_loginattempt"></a>
##### loginattempt

- Schema name: `Loginattempt`
- Type: integer

Maximum number of failed login attempts before blocking an IP address. 0 disables this limit.
- Value must be greater or equal to `0` and lesser or equal to `1000`

<a id="headingCall_parameters_items_i0_timeout"></a>
<a id="Call_parameters_items_i0_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer

Idle timeout in seconds before disconnecting inactive clients. 0 disables timeout.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i0_timeout_notransfer"></a>
<a id="Call_parameters_items_i0_timeout_notransfer"></a>
##### timeout_notransfer

- Schema name: `Timeout Notransfer`
- Type: integer

Timeout in seconds for clients that connect but do not transfer data. 0 disables timeout.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i0_onlyanonymous"></a>
<a id="Call_parameters_items_i0_onlyanonymous"></a>
##### onlyanonymous

- Schema name: `Onlyanonymous`
- Type: boolean

Whether to allow only anonymous FTP access, disabling authenticated user login.

<a id="headingCall_parameters_items_i0_anonpath"></a>
<a id="Call_parameters_items_i0_anonpath"></a>
##### anonpath

- Schema name: `Anonpath`

Filesystem path for anonymous FTP users. `null` to use the default anonymous FTP directory.
<a id="Call_parameters_items_i0_anonpath_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_anonpath_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anonpath_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anonpath_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anonpath_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_onlylocal"></a>
<a id="Call_parameters_items_i0_onlylocal"></a>
##### onlylocal

- Schema name: `Onlylocal`
- Type: boolean

Whether to allow only local system users to login, disabling anonymous access.

<a id="headingCall_parameters_items_i0_banner"></a>
<a id="Call_parameters_items_i0_banner"></a>
##### banner

- Schema name: `Banner`
- Type: string

Welcome message displayed to FTP clients upon connection.

<a id="headingCall_parameters_items_i0_filemask"></a>
<a id="Call_parameters_items_i0_filemask"></a>
##### filemask

- Schema name: `Filemask`
- Type: string

Default Unix permissions (umask) for files created by FTP users.

<a id="headingCall_parameters_items_i0_dirmask"></a>
<a id="Call_parameters_items_i0_dirmask"></a>
##### dirmask

- Schema name: `Dirmask`
- Type: string

Default Unix permissions (umask) for directories created by FTP users.

<a id="headingCall_parameters_items_i0_fxp"></a>
<a id="Call_parameters_items_i0_fxp"></a>
##### fxp

- Schema name: `Fxp`
- Type: boolean

Whether to enable File eXchange Protocol (FXP) for server-to-server transfers.

<a id="headingCall_parameters_items_i0_resume"></a>
<a id="Call_parameters_items_i0_resume"></a>
##### resume

- Schema name: `Resume`
- Type: boolean

Whether to allow clients to resume interrupted file transfers.

<a id="headingCall_parameters_items_i0_defaultroot"></a>
<a id="Call_parameters_items_i0_defaultroot"></a>
##### defaultroot

- Schema name: `Defaultroot`
- Type: boolean

Whether to restrict users to their home directories (chroot jail).

<a id="headingCall_parameters_items_i0_ident"></a>
<a id="Call_parameters_items_i0_ident"></a>
##### ident

- Schema name: `Ident`
- Type: boolean

Whether to perform RFC 1413 ident lookups on connecting clients.

<a id="headingCall_parameters_items_i0_reversedns"></a>
<a id="Call_parameters_items_i0_reversedns"></a>
##### reversedns

- Schema name: `Reversedns`
- Type: boolean

Whether to perform reverse DNS lookups on client IP addresses for logging.

<a id="headingCall_parameters_items_i0_masqaddress"></a>
<a id="Call_parameters_items_i0_masqaddress"></a>
##### masqaddress

- Schema name: `Masqaddress`
- Type: string

Public IP address to advertise to clients for passive mode connections when behind NAT.

<a id="headingCall_parameters_items_i0_passiveportsmin"></a>
<a id="Call_parameters_items_i0_passiveportsmin"></a>
##### passiveportsmin

- Schema name: `Passiveportsmin`
- Type: integer

Minimum port number for passive mode data connections. Must be 0 or between 1024-65535.

<a id="headingCall_parameters_items_i0_passiveportsmax"></a>
<a id="Call_parameters_items_i0_passiveportsmax"></a>
##### passiveportsmax

- Schema name: `Passiveportsmax`
- Type: integer

Maximum port number for passive mode data connections. Must be 0 or between 1024-65535.

<a id="headingCall_parameters_items_i0_localuserbw"></a>
<a id="Call_parameters_items_i0_localuserbw"></a>
##### localuserbw

- Schema name: `Localuserbw`
- Type: integer

Maximum upload bandwidth in KiB/s for local users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_localuserdlbw"></a>
<a id="Call_parameters_items_i0_localuserdlbw"></a>
##### localuserdlbw

- Schema name: `Localuserdlbw`
- Type: integer

Maximum download bandwidth in KiB/s for local users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_anonuserbw"></a>
<a id="Call_parameters_items_i0_anonuserbw"></a>
##### anonuserbw

- Schema name: `Anonuserbw`
- Type: integer

Maximum upload bandwidth in KiB/s for anonymous users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_anonuserdlbw"></a>
<a id="Call_parameters_items_i0_anonuserdlbw"></a>
##### anonuserdlbw

- Schema name: `Anonuserdlbw`
- Type: integer

Maximum download bandwidth in KiB/s for anonymous users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_tls"></a>
<a id="Call_parameters_items_i0_tls"></a>
##### tls

- Schema name: `Tls`
- Type: boolean

Whether to enable TLS/SSL encryption for FTP connections.

<a id="headingCall_parameters_items_i0_tls_policy"></a>
<a id="Call_parameters_items_i0_tls_policy"></a>
##### tls_policy

- Schema name: `Tls Policy`
- Type: enum (of string)

TLS policy for connections. Values include: `"on"` (required), `"off"` (disabled), `"data"` (data only), `"auth"` (authentication only), `"ctrl"` (control only), or combinations with `+` and `!` modifiers.
###### Must be one of:

- ""
- "on"
- "off"
- "data"
- "!data"
- "auth"
- "ctrl"
- "ctrl+data"
- "ctrl+!data"
- "auth+data"
- "auth+!data"

<a id="headingCall_parameters_items_i0_tls_opt_allow_client_renegotiations"></a>
<a id="Call_parameters_items_i0_tls_opt_allow_client_renegotiations"></a>
##### tls_opt_allow_client_renegotiations

- Schema name: `Tls Opt Allow Client Renegotiations`
- Type: boolean

Whether to allow TLS clients to initiate renegotiation of the TLS connection.

<a id="headingCall_parameters_items_i0_tls_opt_allow_dot_login"></a>
<a id="Call_parameters_items_i0_tls_opt_allow_dot_login"></a>
##### tls_opt_allow_dot_login

- Schema name: `Tls Opt Allow Dot Login`
- Type: boolean

Whether to allow .ftpaccess files to override TLS requirements for specific users.

<a id="headingCall_parameters_items_i0_tls_opt_allow_per_user"></a>
<a id="Call_parameters_items_i0_tls_opt_allow_per_user"></a>
##### tls_opt_allow_per_user

- Schema name: `Tls Opt Allow Per User`
- Type: boolean

Whether to allow per-user TLS configuration overrides.

<a id="headingCall_parameters_items_i0_tls_opt_common_name_required"></a>
<a id="Call_parameters_items_i0_tls_opt_common_name_required"></a>
##### tls_opt_common_name_required

- Schema name: `Tls Opt Common Name Required`
- Type: boolean

Whether to require client certificates to have a Common Name field.

<a id="headingCall_parameters_items_i0_tls_opt_enable_diags"></a>
<a id="Call_parameters_items_i0_tls_opt_enable_diags"></a>
##### tls_opt_enable_diags

- Schema name: `Tls Opt Enable Diags`
- Type: boolean

Whether to enable detailed TLS diagnostic logging.

<a id="headingCall_parameters_items_i0_tls_opt_export_cert_data"></a>
<a id="Call_parameters_items_i0_tls_opt_export_cert_data"></a>
##### tls_opt_export_cert_data

- Schema name: `Tls Opt Export Cert Data`
- Type: boolean

Whether to export client certificate data to environment variables.

<a id="headingCall_parameters_items_i0_tls_opt_no_empty_fragments"></a>
<a id="Call_parameters_items_i0_tls_opt_no_empty_fragments"></a>
##### tls_opt_no_empty_fragments

- Schema name: `Tls Opt No Empty Fragments`
- Type: boolean

Whether to disable empty TLS record fragments to improve compatibility with some clients. Disabling increases vulnerability to some attack vectors.

<a id="headingCall_parameters_items_i0_tls_opt_no_session_reuse_required"></a>
<a id="Call_parameters_items_i0_tls_opt_no_session_reuse_required"></a>
##### tls_opt_no_session_reuse_required

- Schema name: `Tls Opt No Session Reuse Required`
- Type: boolean

Whether to disable the requirement for TLS session reuse.

<a id="headingCall_parameters_items_i0_tls_opt_stdenvvars"></a>
<a id="Call_parameters_items_i0_tls_opt_stdenvvars"></a>
##### tls_opt_stdenvvars

- Schema name: `Tls Opt Stdenvvars`
- Type: boolean

Whether to export standard TLS environment variables for use by external programs.

<a id="headingCall_parameters_items_i0_tls_opt_dns_name_required"></a>
<a id="Call_parameters_items_i0_tls_opt_dns_name_required"></a>
##### tls_opt_dns_name_required

- Schema name: `Tls Opt Dns Name Required`
- Type: boolean

Whether to require client certificates to contain a DNS name in the Subject Alternative Name extension. The `reversedns` setting must also be enabled.

<a id="headingCall_parameters_items_i0_tls_opt_ip_address_required"></a>
<a id="Call_parameters_items_i0_tls_opt_ip_address_required"></a>
##### tls_opt_ip_address_required

- Schema name: `Tls Opt Ip Address Required`
- Type: boolean

Whether to require client certificates to contain an IP address in the Subject Alternative Name extension.

<a id="headingCall_parameters_items_i0_ssltls_certificate"></a>
<a id="Call_parameters_items_i0_ssltls_certificate"></a>
##### ssltls_certificate

- Schema name: `Ssltls Certificate`

ID of the certificate to use for TLS/SSL connections. `null` to use the default system certificate.
<a id="Call_parameters_items_i0_ssltls_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_ssltls_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_ssltls_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_ssltls_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_ssltls_certificate_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `Options`
- Type: string

Additional ProFTPD configuration directives to include in the server configuration. Manual directives may render the FTP service non-functional and should be used with caution.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FTPEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `Port`
- Type: integer

TCP port number on which the FTP service listens for incoming connections.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_clients"></a>
<a id="Return_value_clients"></a>
#### clients (required)

- Schema name: `Clients`
- Type: integer

Maximum number of simultaneous client connections allowed.
- Value must be greater or equal to `1` and lesser or equal to `10000`

<a id="headingReturn_value_ipconnections"></a>
<a id="Return_value_ipconnections"></a>
#### ipconnections (required)

- Schema name: `Ipconnections`
- Type: integer

Maximum number of connections allowed from a single IP address. 0 means unlimited.
- Value must be greater or equal to `0` and lesser or equal to `1000`

<a id="headingReturn_value_loginattempt"></a>
<a id="Return_value_loginattempt"></a>
#### loginattempt (required)

- Schema name: `Loginattempt`
- Type: integer

Maximum number of failed login attempts before blocking an IP address. 0 disables this limit.
- Value must be greater or equal to `0` and lesser or equal to `1000`

<a id="headingReturn_value_timeout"></a>
<a id="Return_value_timeout"></a>
#### timeout (required)

- Schema name: `Timeout`
- Type: integer

Idle timeout in seconds before disconnecting inactive clients. 0 disables timeout.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingReturn_value_timeout_notransfer"></a>
<a id="Return_value_timeout_notransfer"></a>
#### timeout_notransfer (required)

- Schema name: `Timeout Notransfer`
- Type: integer

Timeout in seconds for clients that connect but do not transfer data. 0 disables timeout.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingReturn_value_onlyanonymous"></a>
<a id="Return_value_onlyanonymous"></a>
#### onlyanonymous (required)

- Schema name: `Onlyanonymous`
- Type: boolean

Whether to allow only anonymous FTP access, disabling authenticated user login.

<a id="headingReturn_value_anonpath"></a>
<a id="Return_value_anonpath"></a>
#### anonpath (required)

- Schema name: `Anonpath`

Filesystem path for anonymous FTP users. `null` to use the default anonymous FTP directory.
<a id="Return_value_anonpath_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_anonpath_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anonpath_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anonpath_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anonpath_anyOf_i1)

- Type: null

<a id="headingReturn_value_onlylocal"></a>
<a id="Return_value_onlylocal"></a>
#### onlylocal (required)

- Schema name: `Onlylocal`
- Type: boolean

Whether to allow only local system users to login, disabling anonymous access.

<a id="headingReturn_value_banner"></a>
<a id="Return_value_banner"></a>
#### banner (required)

- Schema name: `Banner`
- Type: string

Welcome message displayed to FTP clients upon connection.

<a id="headingReturn_value_filemask"></a>
<a id="Return_value_filemask"></a>
#### filemask (required)

- Schema name: `Filemask`
- Type: string

Default Unix permissions (umask) for files created by FTP users.

<a id="headingReturn_value_dirmask"></a>
<a id="Return_value_dirmask"></a>
#### dirmask (required)

- Schema name: `Dirmask`
- Type: string

Default Unix permissions (umask) for directories created by FTP users.

<a id="headingReturn_value_fxp"></a>
<a id="Return_value_fxp"></a>
#### fxp (required)

- Schema name: `Fxp`
- Type: boolean

Whether to enable File eXchange Protocol (FXP) for server-to-server transfers.

<a id="headingReturn_value_resume"></a>
<a id="Return_value_resume"></a>
#### resume (required)

- Schema name: `Resume`
- Type: boolean

Whether to allow clients to resume interrupted file transfers.

<a id="headingReturn_value_defaultroot"></a>
<a id="Return_value_defaultroot"></a>
#### defaultroot (required)

- Schema name: `Defaultroot`
- Type: boolean

Whether to restrict users to their home directories (chroot jail).

<a id="headingReturn_value_ident"></a>
<a id="Return_value_ident"></a>
#### ident (required)

- Schema name: `Ident`
- Type: boolean

Whether to perform RFC 1413 ident lookups on connecting clients.

<a id="headingReturn_value_reversedns"></a>
<a id="Return_value_reversedns"></a>
#### reversedns (required)

- Schema name: `Reversedns`
- Type: boolean

Whether to perform reverse DNS lookups on client IP addresses for logging.

<a id="headingReturn_value_masqaddress"></a>
<a id="Return_value_masqaddress"></a>
#### masqaddress (required)

- Schema name: `Masqaddress`
- Type: string

Public IP address to advertise to clients for passive mode connections when behind NAT.

<a id="headingReturn_value_passiveportsmin"></a>
<a id="Return_value_passiveportsmin"></a>
#### passiveportsmin (required)

- Schema name: `Passiveportsmin`
- Type: integer

Minimum port number for passive mode data connections. Must be 0 or between 1024-65535.

<a id="headingReturn_value_passiveportsmax"></a>
<a id="Return_value_passiveportsmax"></a>
#### passiveportsmax (required)

- Schema name: `Passiveportsmax`
- Type: integer

Maximum port number for passive mode data connections. Must be 0 or between 1024-65535.

<a id="headingReturn_value_localuserbw"></a>
<a id="Return_value_localuserbw"></a>
#### localuserbw (required)

- Schema name: `Localuserbw`
- Type: integer

Maximum upload bandwidth in KiB/s for local users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingReturn_value_localuserdlbw"></a>
<a id="Return_value_localuserdlbw"></a>
#### localuserdlbw (required)

- Schema name: `Localuserdlbw`
- Type: integer

Maximum download bandwidth in KiB/s for local users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingReturn_value_anonuserbw"></a>
<a id="Return_value_anonuserbw"></a>
#### anonuserbw (required)

- Schema name: `Anonuserbw`
- Type: integer

Maximum upload bandwidth in KiB/s for anonymous users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingReturn_value_anonuserdlbw"></a>
<a id="Return_value_anonuserdlbw"></a>
#### anonuserdlbw (required)

- Schema name: `Anonuserdlbw`
- Type: integer

Maximum download bandwidth in KiB/s for anonymous users. 0 means unlimited.
- Value must be greater or equal to `0`

<a id="headingReturn_value_tls"></a>
<a id="Return_value_tls"></a>
#### tls (required)

- Schema name: `Tls`
- Type: boolean

Whether to enable TLS/SSL encryption for FTP connections.

<a id="headingReturn_value_tls_policy"></a>
<a id="Return_value_tls_policy"></a>
#### tls_policy (required)

- Schema name: `Tls Policy`
- Type: enum (of string)

TLS policy for connections. Values include: `"on"` (required), `"off"` (disabled), `"data"` (data only), `"auth"` (authentication only), `"ctrl"` (control only), or combinations with `+` and `!` modifiers.
##### Must be one of:

- ""
- "on"
- "off"
- "data"
- "!data"
- "auth"
- "ctrl"
- "ctrl+data"
- "ctrl+!data"
- "auth+data"
- "auth+!data"

<a id="headingReturn_value_tls_opt_allow_client_renegotiations"></a>
<a id="Return_value_tls_opt_allow_client_renegotiations"></a>
#### tls_opt_allow_client_renegotiations (required)

- Schema name: `Tls Opt Allow Client Renegotiations`
- Type: boolean

Whether to allow TLS clients to initiate renegotiation of the TLS connection.

<a id="headingReturn_value_tls_opt_allow_dot_login"></a>
<a id="Return_value_tls_opt_allow_dot_login"></a>
#### tls_opt_allow_dot_login (required)

- Schema name: `Tls Opt Allow Dot Login`
- Type: boolean

Whether to allow .ftpaccess files to override TLS requirements for specific users.

<a id="headingReturn_value_tls_opt_allow_per_user"></a>
<a id="Return_value_tls_opt_allow_per_user"></a>
#### tls_opt_allow_per_user (required)

- Schema name: `Tls Opt Allow Per User`
- Type: boolean

Whether to allow per-user TLS configuration overrides.

<a id="headingReturn_value_tls_opt_common_name_required"></a>
<a id="Return_value_tls_opt_common_name_required"></a>
#### tls_opt_common_name_required (required)

- Schema name: `Tls Opt Common Name Required`
- Type: boolean

Whether to require client certificates to have a Common Name field.

<a id="headingReturn_value_tls_opt_enable_diags"></a>
<a id="Return_value_tls_opt_enable_diags"></a>
#### tls_opt_enable_diags (required)

- Schema name: `Tls Opt Enable Diags`
- Type: boolean

Whether to enable detailed TLS diagnostic logging.

<a id="headingReturn_value_tls_opt_export_cert_data"></a>
<a id="Return_value_tls_opt_export_cert_data"></a>
#### tls_opt_export_cert_data (required)

- Schema name: `Tls Opt Export Cert Data`
- Type: boolean

Whether to export client certificate data to environment variables.

<a id="headingReturn_value_tls_opt_no_empty_fragments"></a>
<a id="Return_value_tls_opt_no_empty_fragments"></a>
#### tls_opt_no_empty_fragments (required)

- Schema name: `Tls Opt No Empty Fragments`
- Type: boolean

Whether to disable empty TLS record fragments to improve compatibility with some clients. Disabling increases vulnerability to some attack vectors.

<a id="headingReturn_value_tls_opt_no_session_reuse_required"></a>
<a id="Return_value_tls_opt_no_session_reuse_required"></a>
#### tls_opt_no_session_reuse_required (required)

- Schema name: `Tls Opt No Session Reuse Required`
- Type: boolean

Whether to disable the requirement for TLS session reuse.

<a id="headingReturn_value_tls_opt_stdenvvars"></a>
<a id="Return_value_tls_opt_stdenvvars"></a>
#### tls_opt_stdenvvars (required)

- Schema name: `Tls Opt Stdenvvars`
- Type: boolean

Whether to export standard TLS environment variables for use by external programs.

<a id="headingReturn_value_tls_opt_dns_name_required"></a>
<a id="Return_value_tls_opt_dns_name_required"></a>
#### tls_opt_dns_name_required (required)

- Schema name: `Tls Opt Dns Name Required`
- Type: boolean

Whether to require client certificates to contain a DNS name in the Subject Alternative Name extension. The `reversedns` setting must also be enabled.

<a id="headingReturn_value_tls_opt_ip_address_required"></a>
<a id="Return_value_tls_opt_ip_address_required"></a>
#### tls_opt_ip_address_required (required)

- Schema name: `Tls Opt Ip Address Required`
- Type: boolean

Whether to require client certificates to contain an IP address in the Subject Alternative Name extension.

<a id="headingReturn_value_ssltls_certificate"></a>
<a id="Return_value_ssltls_certificate"></a>
#### ssltls_certificate (required)

- Schema name: `Ssltls Certificate`

ID of the certificate to use for TLS/SSL connections. `null` to use the default system certificate.
<a id="Return_value_ssltls_certificate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ssltls_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ssltls_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_ssltls_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ssltls_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_options"></a>
<a id="Return_value_options"></a>
#### options (required)

- Schema name: `Options`
- Type: string

Additional ProFTPD configuration directives to include in the server configuration. Manual directives may render the FTP service non-functional and should be used with caution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
