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

Discover a remote host key (useful for `SSH_CREDENTIALS`)

.. examples(websocket)::

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "keychaincredential.delete", "params": [{ "host": "work.freenas.org" }] }

## Required Roles

- `KEYCHAIN_CREDENTIAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: keychain_remote_ssh_host_key_scan

#### keychain_remote_ssh_host_key_scan

- Schema name: `keychain_remote_ssh_host_key_scan`
- Type: object

KeychainCredentialRemoteSshHostKeyScanArgs parameters.
- No Additional Properties
##### host (required)

- Schema name: `Host`
- Type: string

Hostname or IP address of the remote SSH server to scan.
- Must be at least `1` characters long

##### port

- Schema name: `Port`
- Type: integer
- Default: 22

TCP port number for the SSH connection.

##### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds.

### Return value

- Schema name: `Result`
- Type: string

SSH host public key retrieved from the remote server.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
