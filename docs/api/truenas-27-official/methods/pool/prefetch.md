---
title: pool.prefetch
kind: method
source_rst: _sources/api_methods_pool.prefetch.rst.txt
source_html: api_methods_pool.prefetch.html
required_roles:
  - POOL_WRITE
---

# pool.prefetch

## Summary

Prefetch pool metadata (DDT and BRT) into ARC.

Loads both the Deduplication Table (DDT) and Block Reference Table (BRT) into the ARC to reduce latency of subsequent operations. This is useful for warming up the cache before performing operations that benefit from having this metadata readily available.

The DDT tracks deduplication metadata, while the BRT tracks block cloning metadata used for efficient copy-on-write operations.

This method is a job.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: pool_name

<a id="Call_parameters_items_i0"></a>
#### pool_name

- Schema name: `pool_name`
- Type: string

Name of the pool to prefetch metadata for.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful metadata prefetch.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
