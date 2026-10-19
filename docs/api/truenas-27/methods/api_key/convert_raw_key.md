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

This allows API key consumers to transform a raw API key (format: id-key) into the precomputed SCRAM authentication material for improved performance.

NOTE: this is a convenience function for API consumers. It does not impact API key stored server-side.

## Required Roles

- `API_KEY_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: raw_key

<a id="Call_parameters_items_i0"></a>
#### raw_key

- Schema name: `raw_key`
- Type: string

The raw API key to convert (format: id-key).
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `ApiKeyScramData`
- Type: object

SCRAM authentication data derived from the raw API key.
- No Additional Properties
<a id="headingReturn_value_api_key_id"></a>
<a id="Return_value_api_key_id"></a>
#### api_key_id (required)

- Schema name: `Api Key Id`
- Type: integer

API key ID.

<a id="headingReturn_value_iterations"></a>
<a id="Return_value_iterations"></a>
#### iterations (required)

- Schema name: `Iterations`
- Type: integer

Number of iterations of PBKDF2-SHA512.

<a id="headingReturn_value_salt"></a>
<a id="Return_value_salt"></a>
#### salt (required)

- Schema name: `Salt`
- Type: string

Base64 encoded salt for API key.

<a id="headingReturn_value_client_key"></a>
<a id="Return_value_client_key"></a>
#### client_key (required)

- Schema name: `Client Key`
- Type: string

Pre-computed SCRAM ClientKey.

<a id="headingReturn_value_stored_key"></a>
<a id="Return_value_stored_key"></a>
#### stored_key (required)

- Schema name: `Stored Key`
- Type: string

SCRAM StoredKey for API key.

<a id="headingReturn_value_server_key"></a>
<a id="Return_value_server_key"></a>
#### server_key (required)

- Schema name: `Server Key`
- Type: string

SCRAM ServerKey for API key.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
