---
title: ssh.config
kind: method
source_rst: _sources/api_methods_ssh.config.rst.txt
source_html: api_methods_ssh.config.html
required_roles:
  - SSH_READ
---

# ssh.config

## Required Roles

- `SSH_READ`

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

- Schema name: `SSHEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the SSH service configuration.

<a id="headingReturn_value_bindiface"></a>
<a id="Return_value_bindiface"></a>
#### bindiface (required)

- Schema name: `Bindiface`
- Type: array of string

Array of network interface names to bind the SSH service to.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_bindiface_items"></a>
- Type: string

<a id="headingReturn_value_tcpport"></a>
<a id="Return_value_tcpport"></a>
#### tcpport (required)

- Schema name: `Tcpport`
- Type: integer

TCP port number for SSH connections.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_password_login_groups"></a>
<a id="Return_value_password_login_groups"></a>
#### password_login_groups (required)

- Schema name: `Password Login Groups`
- Type: array of string

Array of group names allowed to authenticate with passwords.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_password_login_groups_items"></a>
- Type: string

<a id="headingReturn_value_passwordauth"></a>
<a id="Return_value_passwordauth"></a>
#### passwordauth (required)

- Schema name: `Passwordauth`
- Type: boolean

Whether password authentication is enabled.

<a id="headingReturn_value_kerberosauth"></a>
<a id="Return_value_kerberosauth"></a>
#### kerberosauth (required)

- Schema name: `Kerberosauth`
- Type: boolean

Whether Kerberos authentication is enabled.

<a id="headingReturn_value_tcpfwd"></a>
<a id="Return_value_tcpfwd"></a>
#### tcpfwd (required)

- Schema name: `Tcpfwd`
- Type: boolean

Whether TCP forwarding is enabled.

<a id="headingReturn_value_compression"></a>
<a id="Return_value_compression"></a>
#### compression (required)

- Schema name: `Compression`
- Type: boolean

Whether compression is enabled for SSH connections.

<a id="headingReturn_value_sftp_log_level"></a>
<a id="Return_value_sftp_log_level"></a>
#### sftp_log_level (required)

- Schema name: `Sftp Log Level`
- Type: enum (of string)

Logging level for SFTP subsystem (empty string means default).
##### Must be one of:

- ""
- "QUIET"
- "FATAL"
- "ERROR"
- "INFO"
- "VERBOSE"
- "DEBUG"
- "DEBUG2"
- "DEBUG3"

<a id="headingReturn_value_sftp_log_facility"></a>
<a id="Return_value_sftp_log_facility"></a>
#### sftp_log_facility (required)

- Schema name: `Sftp Log Facility`
- Type: enum (of string)

Syslog facility for SFTP logging (empty string means default).
##### Must be one of:

- ""
- "DAEMON"
- "USER"
- "AUTH"
- "LOCAL0"
- "LOCAL1"
- "LOCAL2"
- "LOCAL3"
- "LOCAL4"
- "LOCAL5"
- "LOCAL6"
- "LOCAL7"

<a id="headingReturn_value_weak_ciphers"></a>
<a id="Return_value_weak_ciphers"></a>
#### weak_ciphers (required)

- Schema name: `Weak Ciphers`
- Type: array of enum (of string)

Array of weak ciphers to enable for compatibility with legacy clients.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_weak_ciphers_items"></a>
- Type: enum (of string)
###### Must be one of:

- "AES128-CBC"
- "NONE"

<a id="headingReturn_value_options"></a>
<a id="Return_value_options"></a>
#### options (required)

- Schema name: `Options`
- Type: string

Additional SSH daemon configuration options.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_privatekey"></a>
<a id="Return_value_privatekey"></a>
#### privatekey (required)

- Schema name: `Privatekey`
- Type: string

SSH host private key data.
- Must be at most `2147483647` characters long

<a id="headingReturn_value_host_dsa_key"></a>
<a id="Return_value_host_dsa_key"></a>
#### host_dsa_key (required)

- Schema name: `Host Dsa Key`

DSA host private key. `null` if not configured.
<a id="Return_value_host_dsa_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_dsa_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_dsa_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_dsa_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_dsa_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_dsa_key_pub"></a>
<a id="Return_value_host_dsa_key_pub"></a>
#### host_dsa_key_pub (required)

- Schema name: `Host Dsa Key Pub`

DSA host public key. `null` if not configured.
<a id="Return_value_host_dsa_key_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_dsa_key_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_dsa_key_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_dsa_key_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_dsa_key_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_dsa_key_cert_pub"></a>
<a id="Return_value_host_dsa_key_cert_pub"></a>
#### host_dsa_key_cert_pub (required)

- Schema name: `Host Dsa Key Cert Pub`

DSA host certificate public key. `null` if not configured.
<a id="Return_value_host_dsa_key_cert_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_dsa_key_cert_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_dsa_key_cert_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_dsa_key_cert_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_dsa_key_cert_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_ecdsa_key"></a>
<a id="Return_value_host_ecdsa_key"></a>
#### host_ecdsa_key (required)

- Schema name: `Host Ecdsa Key`

ECDSA host private key. `null` if not configured.
<a id="Return_value_host_ecdsa_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_ecdsa_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_ecdsa_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_ecdsa_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_ecdsa_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_ecdsa_key_pub"></a>
<a id="Return_value_host_ecdsa_key_pub"></a>
#### host_ecdsa_key_pub (required)

- Schema name: `Host Ecdsa Key Pub`

ECDSA host public key. `null` if not configured.
<a id="Return_value_host_ecdsa_key_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_ecdsa_key_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_ecdsa_key_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_ecdsa_key_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_ecdsa_key_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_ecdsa_key_cert_pub"></a>
<a id="Return_value_host_ecdsa_key_cert_pub"></a>
#### host_ecdsa_key_cert_pub (required)

- Schema name: `Host Ecdsa Key Cert Pub`

ECDSA host certificate public key. `null` if not configured.
<a id="Return_value_host_ecdsa_key_cert_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_ecdsa_key_cert_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_ecdsa_key_cert_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_ecdsa_key_cert_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_ecdsa_key_cert_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_ed25519_key"></a>
<a id="Return_value_host_ed25519_key"></a>
#### host_ed25519_key (required)

- Schema name: `Host Ed25519 Key`

Ed25519 host private key. `null` if not configured.
<a id="Return_value_host_ed25519_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_ed25519_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_ed25519_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_ed25519_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_ed25519_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_ed25519_key_pub"></a>
<a id="Return_value_host_ed25519_key_pub"></a>
#### host_ed25519_key_pub (required)

- Schema name: `Host Ed25519 Key Pub`

Ed25519 host public key. `null` if not configured.
<a id="Return_value_host_ed25519_key_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_ed25519_key_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_ed25519_key_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_ed25519_key_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_ed25519_key_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_ed25519_key_cert_pub"></a>
<a id="Return_value_host_ed25519_key_cert_pub"></a>
#### host_ed25519_key_cert_pub (required)

- Schema name: `Host Ed25519 Key Cert Pub`

Ed25519 host certificate public key. `null` if not configured.
<a id="Return_value_host_ed25519_key_cert_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_ed25519_key_cert_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_ed25519_key_cert_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_ed25519_key_cert_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_ed25519_key_cert_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_key"></a>
<a id="Return_value_host_key"></a>
#### host_key (required)

- Schema name: `Host Key`

Legacy SSH host private key. `null` if not configured.
<a id="Return_value_host_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_key_pub"></a>
<a id="Return_value_host_key_pub"></a>
#### host_key_pub (required)

- Schema name: `Host Key Pub`

Legacy SSH host public key. `null` if not configured.
<a id="Return_value_host_key_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_key_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_key_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_key_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_key_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_rsa_key"></a>
<a id="Return_value_host_rsa_key"></a>
#### host_rsa_key (required)

- Schema name: `Host Rsa Key`

RSA host private key. `null` if not configured.
<a id="Return_value_host_rsa_key_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_rsa_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_rsa_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_rsa_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_rsa_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_rsa_key_pub"></a>
<a id="Return_value_host_rsa_key_pub"></a>
#### host_rsa_key_pub (required)

- Schema name: `Host Rsa Key Pub`

RSA host public key. `null` if not configured.
<a id="Return_value_host_rsa_key_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_rsa_key_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_rsa_key_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_rsa_key_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_rsa_key_pub_anyOf_i1)

- Type: null

<a id="headingReturn_value_host_rsa_key_cert_pub"></a>
<a id="Return_value_host_rsa_key_cert_pub"></a>
#### host_rsa_key_cert_pub (required)

- Schema name: `Host Rsa Key Cert Pub`

RSA host certificate public key. `null` if not configured.
<a id="Return_value_host_rsa_key_cert_pub_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_host_rsa_key_cert_pub_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_host_rsa_key_cert_pub_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_host_rsa_key_cert_pub_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_host_rsa_key_cert_pub_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
