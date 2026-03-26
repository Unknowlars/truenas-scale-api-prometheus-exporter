---
title: pool.filesystem_choices
kind: method
source_rst: _sources/api_methods_pool.filesystem_choices.rst.txt
source_html: api_methods_pool.filesystem_choices.html
required_roles:
  - DATASET_READ | POOL_READ | READONLY_ADMIN
---

# pool.filesystem_choices

## Summary

Returns all available datasets, except the following: 1. system datasets 2. application(s) internal datasets

.. examples(websocket)::

Get all datasets.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.filesystem_choices", "params": [] }

Get only filesystems (exclude volumes).

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.filesystem_choices", "params": [["FILESYSTEM"]] }

## Required Roles

- `DATASET_READ | POOL_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: types

#### types

- Schema name: `types`
- Type: array of enum (of string)
- Default: ["FILESYSTEM", "VOLUME"]

Dataset types to include in the results.
- No Additional Items

##### Each item of this array must be:

- Type: enum (of string)

### Return value

- Schema name: `Result`
- Type: array of string

Array of available filesystem/dataset paths.
- No Additional Items

#### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
