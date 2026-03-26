---
title: system.shutdown
kind: method
source_rst: _sources/api_methods_system.shutdown.rst.txt
source_html: api_methods_system.shutdown.html
required_roles:
  - FULL_ADMIN
---

# system.shutdown

## Summary

Shuts down the operating system.

An "added" event of name "system" and id "shutdown" is emitted when shutdown is initiated.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: reason

#### reason

- Schema name: `reason`
- Type: string

Reason for the system shutdown.
- Must be at least `1` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object

Options for controlling the shutdown process.
- No Additional Properties
##### delay

- Schema name: `Delay`
- Default: null

Delay in seconds before shutting down. `null` for immediate shutdown.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful shutdown initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
