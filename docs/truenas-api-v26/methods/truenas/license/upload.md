---
title: truenas.license.upload
kind: method
source_rst: _sources/api_methods_truenas.license.upload.rst.txt
source_html: api_methods_truenas.license.upload.html
required_roles:
  - FULL_ADMIN
---

# truenas.license.upload

## Summary

Upload a PEM-wrapped license file.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: license

#### license

- Schema name: `license`
- Type: string

PEM-wrapped license to apply to the system.
- Must be at least `1` characters long
- Must be at most `2147483647` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {"ha_propagate": true}

Options.
- No Additional Properties
##### ha_propagate

- Schema name: `Ha Propagate`
- Type: boolean
- Default: true

Propagate to another HA system.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful license upload.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
