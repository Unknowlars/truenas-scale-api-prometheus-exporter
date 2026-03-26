---
title: pool.dataset.encryption_algorithm_choices
kind: method
source_rst: _sources/api_methods_pool.dataset.encryption_algorithm_choices.rst.txt
source_html: api_methods_pool.dataset.encryption_algorithm_choices.html
required_roles:
  - DATASET_READ | READONLY_ADMIN
---

# pool.dataset.encryption_algorithm_choices

## Summary

Retrieve encryption algorithms supported for ZFS dataset encryption.

## Required Roles

- `DATASET_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `PoolDatasetEncryptionAlgorithmChoicesResult`
- Type: object

PoolDatasetEncryptionAlgorithmChoicesResult return fields.
- No Additional Properties
#### AES-128-CCM (required)

- Schema name: `Aes-128-Ccm`
- Type: const

#### AES-192-CCM (required)

- Schema name: `Aes-192-Ccm`
- Type: const

#### AES-256-CCM (required)

- Schema name: `Aes-256-Ccm`
- Type: const

#### AES-128-GCM (required)

- Schema name: `Aes-128-Gcm`
- Type: const

#### AES-192-GCM (required)

- Schema name: `Aes-192-Gcm`
- Type: const

#### AES-256-GCM (required)

- Schema name: `Aes-256-Gcm`
- Type: const

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
