---
title: keychaincredential.remote_ssh_host_key_scan
kind: method
source_rst: _sources/api_methods_keychaincredential.remote_ssh_host_key_scan.rst.txt
source_html: api_methods_keychaincredential.remote_ssh_host_key_scan.html
required_roles:
  - KEYCHAIN_CREDENTIAL_WRITE
---

# keychaincredential.remote_ssh_host_key_scan

## Summary

Discover a remote host key (useful for `SSH_CREDENTIALS`).

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

#### Parameter 1: keychain_remote_ssh_host_key_scan

<a id="Call_parameters_items_i0"></a>
#### keychain_remote_ssh_host_key_scan

- Schema name: `keychain_remote_ssh_host_key_scan`
- Type: object

KeychainCredentialRemoteSshHostKeyScanArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_host"></a>
<a id="Call_parameters_items_i0_host"></a>
##### host (required)

- Schema name: `Host`
- Type: string

Hostname or IP address of the remote SSH server to scan.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_port"></a>
<a id="Call_parameters_items_i0_port"></a>
##### port

- Schema name: `Port`
- Type: integer
- Default: 22

TCP port number for the SSH connection.

<a id="headingCall_parameters_items_i0_connect_timeout"></a>
<a id="Call_parameters_items_i0_connect_timeout"></a>
##### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

SSH host public key retrieved from the remote server.
- Must be at most `2147483647` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
