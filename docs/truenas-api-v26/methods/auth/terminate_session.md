---
title: auth.terminate_session
kind: method
source_rst: _sources/api_methods_auth.terminate_session.rst.txt
source_html: api_methods_auth.terminate_session.html
required_roles:
  - AUTH_SESSIONS_WRITE
---

# auth.terminate_session

## Summary

Terminates session `id`.

## Required Roles

- `AUTH_SESSIONS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

Session ID to terminate.

### Return value

- Schema name: `Result`
- Type: boolean

Returns `true` if the session was successfully terminated, `false` otherwise.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
