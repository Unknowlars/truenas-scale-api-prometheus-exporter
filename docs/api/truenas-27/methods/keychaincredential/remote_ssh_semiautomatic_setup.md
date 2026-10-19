---
title: keychaincredential.remote_ssh_semiautomatic_setup
kind: method
source_rst: _sources/api_methods_keychaincredential.remote_ssh_semiautomatic_setup.rst.txt
source_html: api_methods_keychaincredential.remote_ssh_semiautomatic_setup.html
required_roles:
  - KEYCHAIN_CREDENTIAL_WRITE
---

# keychaincredential.remote_ssh_semiautomatic_setup

## Summary

Perform semi-automatic SSH connection setup with other TrueNAS machine.

It creates an `SSH_CREDENTIALS` credential with specified `name` that can be used to connect to TrueNAS machine with specified `url` and temporary auth `token`. Other TrueNAS machine adds `private_key` to allowed `username`'s private keys. Other `SSH_CREDENTIALS` attributes such as `connect_timeout` can be specified as well.

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "keychaincredential.remote_ssh_semiautomatic_setup", "params": [{ "name": "Work SSH connection", "url": "https://work.freenas.org", "token": "8c8d5fd1-f749-4429-b379-9c186db4f834", "private_key": 12 }] }

## Required Roles

- `KEYCHAIN_CREDENTIAL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Configuration data for semi-automatic SSH credential setup.
- No Additional Properties
<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name for the SSH connection credential.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_url"></a>
<a id="Call_parameters_items_i0_url"></a>
##### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

URL of the remote TrueNAS system for semi-automatic setup.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingCall_parameters_items_i0_verify_ssl"></a>
<a id="Call_parameters_items_i0_verify_ssl"></a>
##### verify_ssl

- Schema name: `Verify Ssl`
- Type: boolean
- Default: true

Whether to verify SSL certificates when connecting to the remote system.

<a id="headingCall_parameters_items_i0_token"></a>
<a id="Call_parameters_items_i0_token"></a>
##### token

- Schema name: `Token`
- Default: null

API token for authentication with the remote system or `null`.
<a id="Call_parameters_items_i0_token_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_token_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_token_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_admin_username"></a>
<a id="Call_parameters_items_i0_admin_username"></a>
##### admin_username

- Schema name: `Admin Username`
- Type: string
- Default: "root"

Administrative username for the remote system.

<a id="headingCall_parameters_items_i0_password"></a>
<a id="Call_parameters_items_i0_password"></a>
##### password

- Schema name: `Password`
- Default: null

Password for the administrative user or `null`.
<a id="Call_parameters_items_i0_password_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_password_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_password_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_otp_token"></a>
<a id="Call_parameters_items_i0_otp_token"></a>
##### otp_token

- Schema name: `Otp Token`
- Default: null

One-time password token for 2FA authentication or `null`.
<a id="Call_parameters_items_i0_otp_token_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_otp_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_otp_token_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_otp_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_otp_token_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_username"></a>
<a id="Call_parameters_items_i0_username"></a>
##### username

- Schema name: `Username`
- Type: string
- Default: "root"

Username for the SSH connection.

<a id="headingCall_parameters_items_i0_private_key"></a>
<a id="Call_parameters_items_i0_private_key"></a>
##### private_key (required)

- Schema name: `Private Key`
- Type: integer

ID of the existing private key credential to use for SSH authentication.

<a id="headingCall_parameters_items_i0_connect_timeout"></a>
<a id="Call_parameters_items_i0_connect_timeout"></a>
##### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

SSH connection timeout in seconds.

<a id="headingCall_parameters_items_i0_sudo"></a>
<a id="Call_parameters_items_i0_sudo"></a>
##### sudo

- Schema name: `Sudo`
- Type: boolean
- Default: false

Whether the SSH user should use sudo for elevated privileges.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SSHCredentialsEntry`
- Type: object

The created SSH credential configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`
- Type: const

Keychain credential type identifier for SSH connection credentials.
- Specific value: `"SSH_CREDENTIALS"`

<a id="headingReturn_value_attributes"></a>
<a id="Return_value_attributes"></a>
#### attributes (required)

- Schema name: `Attributes`
- Type: object

SSH connection attributes including host, authentication, and connection settings.
- No Additional Properties
<a id="headingReturn_value_attributes_host"></a>
<a id="Return_value_attributes_host"></a>
##### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingReturn_value_attributes_port"></a>
<a id="Return_value_attributes_port"></a>
##### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingReturn_value_attributes_username"></a>
<a id="Return_value_attributes_username"></a>
##### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingReturn_value_attributes_private_key"></a>
<a id="Return_value_attributes_private_key"></a>
##### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingReturn_value_attributes_remote_host_key"></a>
<a id="Return_value_attributes_remote_host_key"></a>
##### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingReturn_value_attributes_connect_timeout"></a>
<a id="Return_value_attributes_connect_timeout"></a>
##### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
