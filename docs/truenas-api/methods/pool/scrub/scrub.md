---
title: pool.scrub.scrub
kind: method
source_rst: _sources/api_methods_pool.scrub.scrub.rst.txt
source_html: api_methods_pool.scrub.scrub.html
required_roles:
  - POOL_WRITE
---

# pool.scrub.scrub

## Summary

Start/Stop/Pause a scrub on pool `name`.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: string

Name of the pool to perform scrub action on.

#### Parameter 2: action

#### action

- Schema name: `action`
- Type: enum (of string)
- Default: "START"

The scrub action to perform on the pool.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful scrub action.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
