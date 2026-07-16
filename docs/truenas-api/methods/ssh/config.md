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

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `SSHEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the SSH service configuration.

#### bindiface (required)

- Schema name: `Bindiface`
- Type: array of string

Array of network interface names to bind the SSH service to.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### tcpport (required)

- Schema name: `Tcpport`
- Type: integer

TCP port number for SSH connections.
- Value must be greater or equal to `1` and lesser or equal to `65535`

#### password_login_groups (required)

- Schema name: `Password Login Groups`
- Type: array of string

Array of group names allowed to authenticate with passwords.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### passwordauth (required)

- Schema name: `Passwordauth`
- Type: boolean

Whether password authentication is enabled.

#### kerberosauth (required)

- Schema name: `Kerberosauth`
- Type: boolean

Whether Kerberos authentication is enabled.

#### tcpfwd (required)

- Schema name: `Tcpfwd`
- Type: boolean

Whether TCP forwarding is enabled.

#### compression (required)

- Schema name: `Compression`
- Type: boolean

Whether compression is enabled for SSH connections.

#### sftp_log_level (required)

- Schema name: `Sftp Log Level`
- Type: enum (of string)

Logging level for SFTP subsystem (empty string means default).

#### sftp_log_facility (required)

- Schema name: `Sftp Log Facility`
- Type: enum (of string)

Syslog facility for SFTP logging (empty string means default).

#### weak_ciphers (required)

- Schema name: `Weak Ciphers`
- Type: array of enum (of string)

Array of weak ciphers to enable for compatibility with legacy clients.
- No Additional Items

##### Each item of this array must be:

- Type: enum (of string)

#### options (required)

- Schema name: `Options`
- Type: string

Additional SSH daemon configuration options.

#### privatekey (required)

- Schema name: `Privatekey`
- Type: string

SSH host private key data.

#### host_dsa_key (required)

- Schema name: `Host Dsa Key`

DSA host private key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_dsa_key_pub (required)

- Schema name: `Host Dsa Key Pub`

DSA host public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_dsa_key_cert_pub (required)

- Schema name: `Host Dsa Key Cert Pub`

DSA host certificate public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_ecdsa_key (required)

- Schema name: `Host Ecdsa Key`

ECDSA host private key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_ecdsa_key_pub (required)

- Schema name: `Host Ecdsa Key Pub`

ECDSA host public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_ecdsa_key_cert_pub (required)

- Schema name: `Host Ecdsa Key Cert Pub`

ECDSA host certificate public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_ed25519_key (required)

- Schema name: `Host Ed25519 Key`

Ed25519 host private key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_ed25519_key_pub (required)

- Schema name: `Host Ed25519 Key Pub`

Ed25519 host public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_ed25519_key_cert_pub (required)

- Schema name: `Host Ed25519 Key Cert Pub`

Ed25519 host certificate public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_key (required)

- Schema name: `Host Key`

Legacy SSH host private key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_key_pub (required)

- Schema name: `Host Key Pub`

Legacy SSH host public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_rsa_key (required)

- Schema name: `Host Rsa Key`

RSA host private key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_rsa_key_pub (required)

- Schema name: `Host Rsa Key Pub`

RSA host public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### host_rsa_key_cert_pub (required)

- Schema name: `Host Rsa Key Cert Pub`

RSA host certificate public key. `null` if not configured.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
