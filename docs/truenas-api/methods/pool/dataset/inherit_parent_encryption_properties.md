---
title: pool.dataset.inherit_parent_encryption_properties
kind: method
source_rst: _sources/api_methods_pool.dataset.inherit_parent_encryption_properties.rst.txt
source_html: api_methods_pool.dataset.inherit_parent_encryption_properties.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.inherit_parent_encryption_properties

## Summary

Allows inheriting parent's encryption root discarding its current encryption settings. This can only be done where `id` has an encrypted parent and `id` itself is an encryption root.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to inherit encryption properties from its parent.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful inheritance of parent encryption properties.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
