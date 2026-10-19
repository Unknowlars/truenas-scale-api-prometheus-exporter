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

Create an SSH connection by performing the following steps:

1. Generate an SSH key pair if required. 2. Set up SSH credentials based on `setup_type`.

If step 2 fails, any SSH key pair generated in the process is removed.

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

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`

SSH connection setup configuration (manual or semi-automatic).
<a id="Call_parameters_items_i0_oneOf"></a>
##### One of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0"></a>
###### [SetupSSHConnectionManual](#tab-pane_Call_parameters_items_i0_oneOf_i0)

- Schema name: `SetupSSHConnectionManual`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_private_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`

SSH private key configuration (new or existing).
<a id="Call_parameters_items_i0_oneOf_i0_private_key_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i0"></a>
###### [KeychainCredentialSetupSSHConnectionKeyNew](#tab-pane_Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i0)

- Schema name: `KeychainCredentialSetupSSHConnectionKeyNew`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_private_key_oneOf_i0_generate_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i0_generate_key"></a>
###### generate_key

- Schema name: `Generate Key`
- Type: const
- Default: true

Indicates a new SSH key pair should be generated.
- Specific value: `true`

<a id="headingCall_parameters_items_i0_oneOf_i0_private_key_oneOf_i0_name"></a>
<a id="Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name for the new SSH key credential.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i1"></a>
###### [KeychainCredentialSetupSSHConnectionKeyExisting](#tab-pane_Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i1)

- Schema name: `KeychainCredentialSetupSSHConnectionKeyExisting`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_private_key_oneOf_i1_generate_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i1_generate_key"></a>
###### generate_key

- Schema name: `Generate Key`
- Type: const
- Default: false

Indicates an existing SSH key should be used.
- Specific value: `false`

<a id="headingCall_parameters_items_i0_oneOf_i0_private_key_oneOf_i1_existing_key_id"></a>
<a id="Call_parameters_items_i0_oneOf_i0_private_key_oneOf_i1_existing_key_id"></a>
###### existing_key_id (required)

- Schema name: `Existing Key Id`
- Type: integer

ID of the existing SSH private key credential to use.

<a id="headingCall_parameters_items_i0_oneOf_i0_connection_name"></a>
<a id="Call_parameters_items_i0_oneOf_i0_connection_name"></a>
###### connection_name (required)

- Schema name: `Connection Name`
- Type: string

Name for the SSH connection credential.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_oneOf_i0_setup_type"></a>
<a id="Call_parameters_items_i0_oneOf_i0_setup_type"></a>
###### setup_type

- Schema name: `Setup Type`
- Type: const
- Default: "MANUAL"

Setup method for the SSH connection.
- Specific value: `"MANUAL"`

<a id="headingCall_parameters_items_i0_oneOf_i0_manual_setup"></a>
<a id="Call_parameters_items_i0_oneOf_i0_manual_setup"></a>
###### manual_setup (required)

- Schema name: `SetupSSHConnectionManualSetup`
- Type: object

Manual SSH connection configuration parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i0_manual_setup_host"></a>
<a id="Call_parameters_items_i0_oneOf_i0_manual_setup_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingCall_parameters_items_i0_oneOf_i0_manual_setup_port"></a>
<a id="Call_parameters_items_i0_oneOf_i0_manual_setup_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingCall_parameters_items_i0_oneOf_i0_manual_setup_username"></a>
<a id="Call_parameters_items_i0_oneOf_i0_manual_setup_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingCall_parameters_items_i0_oneOf_i0_manual_setup_remote_host_key"></a>
<a id="Call_parameters_items_i0_oneOf_i0_manual_setup_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingCall_parameters_items_i0_oneOf_i0_manual_setup_connect_timeout"></a>
<a id="Call_parameters_items_i0_oneOf_i0_manual_setup_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1"></a>
###### [SetupSSHConnectionSemiautomatic](#tab-pane_Call_parameters_items_i0_oneOf_i1)

- Schema name: `SetupSSHConnectionSemiautomatic`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_private_key"></a>
<a id="Call_parameters_items_i0_oneOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`

SSH private key configuration (new or existing).
<a id="Call_parameters_items_i0_oneOf_i1_private_key_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i0"></a>
###### [KeychainCredentialSetupSSHConnectionKeyNew](#tab-pane_Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i0)

- Schema name: `KeychainCredentialSetupSSHConnectionKeyNew`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_private_key_oneOf_i0_generate_key"></a>
<a id="Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i0_generate_key"></a>
###### generate_key

- Schema name: `Generate Key`
- Type: const
- Default: true

Indicates a new SSH key pair should be generated.
- Specific value: `true`

<a id="headingCall_parameters_items_i0_oneOf_i1_private_key_oneOf_i0_name"></a>
<a id="Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name for the new SSH key credential.
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i1"></a>
###### [KeychainCredentialSetupSSHConnectionKeyExisting](#tab-pane_Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i1)

- Schema name: `KeychainCredentialSetupSSHConnectionKeyExisting`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_private_key_oneOf_i1_generate_key"></a>
<a id="Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i1_generate_key"></a>
###### generate_key

- Schema name: `Generate Key`
- Type: const
- Default: false

Indicates an existing SSH key should be used.
- Specific value: `false`

<a id="headingCall_parameters_items_i0_oneOf_i1_private_key_oneOf_i1_existing_key_id"></a>
<a id="Call_parameters_items_i0_oneOf_i1_private_key_oneOf_i1_existing_key_id"></a>
###### existing_key_id (required)

- Schema name: `Existing Key Id`
- Type: integer

ID of the existing SSH private key credential to use.

<a id="headingCall_parameters_items_i0_oneOf_i1_connection_name"></a>
<a id="Call_parameters_items_i0_oneOf_i1_connection_name"></a>
###### connection_name (required)

- Schema name: `Connection Name`
- Type: string

Name for the SSH connection credential.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_oneOf_i1_setup_type"></a>
<a id="Call_parameters_items_i0_oneOf_i1_setup_type"></a>
###### setup_type

- Schema name: `Setup Type`
- Type: const
- Default: "SEMI-AUTOMATIC"

Setup method for the SSH connection.
- Specific value: `"SEMI-AUTOMATIC"`

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup"></a>
###### semi_automatic_setup (required)

- Schema name: `KeychainCredentialSetupSSHConnectionSemiAutomaticSetup`
- Type: object

Semi-automatic SSH connection configuration parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_url"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_url"></a>
###### url (required)

- Schema name: `Url`
- Type: string
- Type: Format: uri

URL of the remote TrueNAS system for semi-automatic setup.
- Must be at least `1` characters long
- Must be at most `2083` characters long

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_verify_ssl"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_verify_ssl"></a>
###### verify_ssl

- Schema name: `Verify Ssl`
- Type: boolean
- Default: true

Whether to verify SSL certificates when connecting to the remote system.

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_token"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_token"></a>
###### token

- Schema name: `Token`
- Default: ""

API token for authentication with the remote system or `null`.
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_token_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_token_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_token_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_admin_username"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_admin_username"></a>
###### admin_username

- Schema name: `Admin Username`
- Type: string
- Default: "root"

Administrative username for the remote system.

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_password"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_password"></a>
###### password

- Schema name: `Password`
- Default: ""

Password for the administrative user or `null`.
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_password_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_password_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_password_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token"></a>
###### otp_token

- Schema name: `Otp Token`
- Default: ""

One-time password token for 2FA authentication or `null`.
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_otp_token_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_username"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

Username for the SSH connection.

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_connect_timeout"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

SSH connection timeout in seconds.

<a id="headingCall_parameters_items_i0_oneOf_i1_semi_automatic_setup_sudo"></a>
<a id="Call_parameters_items_i0_oneOf_i1_semi_automatic_setup_sudo"></a>
###### sudo

- Schema name: `Sudo`
- Type: boolean
- Default: false

Whether the SSH user should use sudo for elevated privileges.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SSHCredentialsEntry`
- Type: object

The created SSH connection credential.
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
