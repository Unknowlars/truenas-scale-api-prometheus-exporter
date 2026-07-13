---
title: pool.dataset.details
kind: method
source_rst: _sources/api_methods_pool.dataset.details.rst.txt
source_html: api_methods_pool.dataset.details.html
required_roles:
  - DATASET_READ
---

# pool.dataset.details

## Summary

Retrieve all dataset(s) details outlining any services/tasks which might be consuming them.

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of detailed dataset information objects.
- No Additional Items

#### Each item of this array must be:

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
