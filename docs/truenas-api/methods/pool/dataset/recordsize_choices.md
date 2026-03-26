---
title: pool.dataset.recordsize_choices
kind: method
source_rst: _sources/api_methods_pool.dataset.recordsize_choices.rst.txt
source_html: api_methods_pool.dataset.recordsize_choices.html
required_roles:
  - DATASET_READ | READONLY_ADMIN
---

# pool.dataset.recordsize_choices

## Summary

Retrieve recordsize choices for datasets.

## Required Roles

- `DATASET_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_name

#### pool_name

- Schema name: `pool_name`
- Default: null

Optional pool name to get record size choices for. If not provided, returns general choices.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: array of string

Array of available record size options for filesystem datasets.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
