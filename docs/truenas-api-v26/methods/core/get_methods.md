---
title: core.get_methods
kind: method
source_rst: _sources/api_methods_core.get_methods.rst.txt
source_html: api_methods_core.get_methods.html
required_roles:
  []
---

# core.get_methods

## Summary

Return methods metadata of every available service.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: service

#### service

- Schema name: `service`
- Default: null

Filters the result for a single service.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### Parameter 2: target

#### target

- Schema name: `target`
- Type: enum (of string)
- Default: "WS"

Target interface to get methods for. `WS` for WebSocket, `CLI` for command line, `REST` for HTTP API.

### Return value

- Schema name: `Result`
- Type: object

Object mapping method names to their signatures, documentation, and metadata.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
