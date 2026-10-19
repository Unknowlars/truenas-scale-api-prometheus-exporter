---
title: pool.scrub.run
kind: method
source_rst: _sources/api_methods_pool.scrub.run.rst.txt
source_html: api_methods_pool.scrub.run.html
required_roles:
  - POOL_WRITE
---

# pool.scrub.run

## Summary

Initiate a scrub of pool `name` if the most recent scrub finished more than `threshold` days ago. Does nothing if the scrub is not yet due or if this node is not the active controller on an HA system.

.. deprecated:: 27.0.0 Use [zpool.scrub.run](../../zpool/scrub/run.md) instead.

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

#### Parameter 1: name

<a id="Call_parameters_items_i0"></a>
#### name

- Schema name: `name`
- Type: string

Name of the pool to run scrub on.

#### Parameter 2: threshold

<a id="Call_parameters_items_i1"></a>
#### threshold

- Schema name: `threshold`
- Type: integer
- Default: 35

Days before a scrub is due when the scrub should start.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful scrub start.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
