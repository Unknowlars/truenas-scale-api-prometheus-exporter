---
title: core.debug
kind: method
source_rst: _sources/api_methods_core.debug.rst.txt
source_html: api_methods_core.debug.html
required_roles:
  - FULL_ADMIN
---

# core.debug

## Summary

Setup middlewared for remote debugging.

engine currently used: - REMOTE_PDB: Remote vanilla PDB (over TCP sockets)

options: - bind_address: local ip address to bind the remote debug session to - bind_port: local port to listen on - threaded: run debugger in a new thread instead of the main event loop

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object

CoreDebugArgs parameters.
- No Additional Properties
##### bind_address

- Schema name: `Bind Address`
- Type: string
- Default: "0.0.0.0"

IP address to bind the debug server to.

##### bind_port

- Schema name: `Bind Port`
- Type: integer
- Default: 3000

Port number to bind the debug server to.

##### threaded

- Schema name: `Threaded`
- Type: boolean
- Default: false

Whether to enable threaded debugging support.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the debug server is successfully started.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
