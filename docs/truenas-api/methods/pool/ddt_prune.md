---
title: pool.ddt_prune
kind: method
source_rst: _sources/api_methods_pool.ddt_prune.rst.txt
source_html: api_methods_pool.ddt_prune.html
required_roles:
  - POOL_WRITE
---

# pool.ddt_prune

## Summary

Prune DDT entries in pool `pool_name` based on the specified options.

`percentage` is the percentage of DDT entries to prune.

`days` is the number of days to prune DDT entries.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object

PoolDdtPruneArgs parameters.
- No Additional Properties
##### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the pool to prune deduplication table entries from.
- Must be at least `1` characters long

##### percentage

- Schema name: `Percentage`
- Default: null

Percentage of deduplication table entries to prune.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `100`

####### Option 2

- Type: null

##### days

- Schema name: `Days`
- Default: null

Remove entries older than this many days.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1`

####### Option 2

- Type: null

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful deduplication table pruning.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
