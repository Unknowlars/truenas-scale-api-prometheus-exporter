---
title: api_key.convert_raw_key
kind: method
source_rst: _sources/api_methods_api_key.convert_raw_key.rst.txt
source_html: api_methods_api_key.convert_raw_key.html
required_roles:
  - API_KEY_READ
---

# api_key.convert_raw_key

## Summary

Convert a raw API key into its SCRAM authentication components.

This allows API key consumers to transform a raw API key (format: `id-key`) into the precomputed SCRAM authentication material for improved performance.

.. note::

This is a convenience method for API consumers. It does not impact the API key stored server-side.

## Required Roles

- `API_KEY_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: raw_key

#### raw_key

- Schema name: `raw_key`
- Type: string

The raw API key to convert (format: id-key).
- Must be at least `1` characters long

### Return value

- Schema name: `ApiKeyScramData`
- Type: object

SCRAM authentication data derived from the raw API key.
- No Additional Properties
#### api_key_id (required)

- Schema name: `Api Key Id`
- Type: integer

API key ID.

#### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

#### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

#### client_key (required)

- Schema name: `Client Key`
- Type: string

Pre-computed SCRAM ClientKey.

#### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

#### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
