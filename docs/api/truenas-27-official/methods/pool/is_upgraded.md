---
title: pool.is_upgraded
kind: method
source_rst: _sources/api_methods_pool.is_upgraded.rst.txt
source_html: api_methods_pool.is_upgraded.html
required_roles:
  - POOL_READ
---

# pool.is_upgraded

## Summary

Returns whether the pool of `id` is on the latest version and with all feature flags enabled.

Queries the database for the pool matching the given `id`, then checks each ZFS feature flag on the pool. Returns `true` only when every feature flag is in the ENABLED or ACTIVE state.

Raises a `ValidationError` if `id` does not match any pool in the database.

*DEPRECATED: this method is scheduled to be removed in v27.*

## Required Roles

- `POOL_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the pool to check upgrade status for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Whether the pool has been upgraded to the latest feature flags.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
