---
title: pool.dataset.create
kind: method
source_rst: _sources/api_methods_pool.dataset.create.rst.txt
source_html: api_methods_pool.dataset.create.html
required_roles:
  - DATASET_WRITE
---

# pool.dataset.create

## Summary

Creates a dataset/zvol.

Create a dataset within tank pool::

{ "jsonrpc": "2.0", "id": 1, "method": "pool.dataset.create", "params": [{ "name": "tank/myuser", "comments": "Dataset for myuser" }] }

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`

Configuration data for creating a new ZFS dataset.

### Return value

- Type: object

The newly created dataset information.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
