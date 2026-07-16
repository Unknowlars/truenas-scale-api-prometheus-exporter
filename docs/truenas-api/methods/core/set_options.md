---
title: core.set_options
kind: method
source_rst: _sources/api_methods_core.set_options.rst.txt
source_html: api_methods_core.set_options.html
required_roles:
  []
---

# core.set_options

## Required Roles

- None documented.

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

Core system options to update.
##### legacy_jobs

- Schema name: `Legacy Jobs`
- Type: boolean

Whether to enable legacy job behavior for backward compatibility.

##### private_methods

- Schema name: `Private Methods`
- Type: boolean

Whether to expose private methods in API introspection.

##### py_exceptions

- Schema name: `Py Exceptions`
- Type: boolean

Whether to include Python exception details in error responses.

### Return value

- Schema name: `CoreOptions`
- Type: object

The updated core system options.
#### legacy_jobs

- Schema name: `Legacy Jobs`
- Type: boolean

Whether to enable legacy job behavior for backward compatibility.

#### private_methods

- Schema name: `Private Methods`
- Type: boolean

Whether to expose private methods in API introspection.

#### py_exceptions

- Schema name: `Py Exceptions`
- Type: boolean

Whether to include Python exception details in error responses.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
