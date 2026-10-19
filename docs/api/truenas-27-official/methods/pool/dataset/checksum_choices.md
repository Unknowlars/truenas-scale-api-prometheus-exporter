---
title: pool.dataset.checksum_choices
kind: method
source_rst: _sources/api_methods_pool.dataset.checksum_choices.rst.txt
source_html: api_methods_pool.dataset.checksum_choices.html
required_roles:
  - DATASET_READ
  - READONLY_ADMIN
---

# pool.dataset.checksum_choices

## Summary

Retrieve checksums supported for ZFS dataset.

## Required Roles

- `DATASET_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolDatasetChecksumChoicesResult`
- Type: object

PoolDatasetChecksumChoicesResult return fields.
- No Additional Properties
<a id="headingReturn_value_ON"></a>
<a id="Return_value_ON"></a>
#### ON (required)

- Schema name: `On`
- Type: const
- Specific value: `"ON"`

<a id="headingReturn_value_FLETCHER2"></a>
<a id="Return_value_FLETCHER2"></a>
#### FLETCHER2 (required)

- Schema name: `Fletcher2`
- Type: const
- Specific value: `"FLETCHER2"`

<a id="headingReturn_value_FLETCHER4"></a>
<a id="Return_value_FLETCHER4"></a>
#### FLETCHER4 (required)

- Schema name: `Fletcher4`
- Type: const
- Specific value: `"FLETCHER4"`

<a id="headingReturn_value_SHA256"></a>
<a id="Return_value_SHA256"></a>
#### SHA256 (required)

- Schema name: `Sha256`
- Type: const
- Specific value: `"SHA256"`

<a id="headingReturn_value_SHA512"></a>
<a id="Return_value_SHA512"></a>
#### SHA512 (required)

- Schema name: `Sha512`
- Type: const
- Specific value: `"SHA512"`

<a id="headingReturn_value_SKEIN"></a>
<a id="Return_value_SKEIN"></a>
#### SKEIN (required)

- Schema name: `Skein`
- Type: const
- Specific value: `"SKEIN"`

<a id="headingReturn_value_EDONR"></a>
<a id="Return_value_EDONR"></a>
#### EDONR (required)

- Schema name: `Edonr`
- Type: const
- Specific value: `"EDONR"`

<a id="headingReturn_value_BLAKE3"></a>
<a id="Return_value_BLAKE3"></a>
#### BLAKE3 (required)

- Schema name: `Blake3`
- Type: const
- Specific value: `"BLAKE3"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
