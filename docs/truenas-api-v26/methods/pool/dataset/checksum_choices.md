---
title: pool.dataset.checksum_choices
kind: method
source_rst: _sources/api_methods_pool.dataset.checksum_choices.rst.txt
source_html: api_methods_pool.dataset.checksum_choices.html
required_roles:
  - DATASET_READ | READONLY_ADMIN
---

# pool.dataset.checksum_choices

## Summary

Retrieve checksums supported for ZFS dataset.

## Required Roles

- `DATASET_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `PoolDatasetChecksumChoicesResult`
- Type: object

PoolDatasetChecksumChoicesResult return fields.
- No Additional Properties
#### ON (required)

- Schema name: `On`
- Type: const

#### FLETCHER2 (required)

- Schema name: `Fletcher2`
- Type: const

#### FLETCHER4 (required)

- Schema name: `Fletcher4`
- Type: const

#### SHA256 (required)

- Schema name: `Sha256`
- Type: const

#### SHA512 (required)

- Schema name: `Sha512`
- Type: const

#### SKEIN (required)

- Schema name: `Skein`
- Type: const

#### EDONR (required)

- Schema name: `Edonr`
- Type: const

#### BLAKE3 (required)

- Schema name: `Blake3`
- Type: const

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
