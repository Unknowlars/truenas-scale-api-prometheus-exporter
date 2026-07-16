---
title: pool.upgrade
kind: method
source_rst: _sources/api_methods_pool.upgrade.rst.txt
source_html: api_methods_pool.upgrade.html
required_roles:
  - POOL_WRITE
---

# pool.upgrade

## Summary

Upgrade pool of `id` to latest version with all feature flags.

Queries the database for the pool matching the given `id`, then enables all supported ZFS feature flags on the pool. This is a one-way operation and cannot be reversed. Once upgraded, the pool will not be importable on systems running older ZFS versions that do not support the newly enabled features.

Raises a `ValidationError` if no pool matches the given `id` or if the pool is not currently imported.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the pool to upgrade to the latest feature flags.

### Return value

- Schema name: `Result`
- Type: const

Indicates successful pool upgrade.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
