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

.. deprecated:: 26.0.0 Use :doc:`zpool.scrub.run <api_methods_zpool.scrub.run>` instead.

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: string

Name of the pool to run scrub on.

#### Parameter 2: threshold

#### threshold

- Schema name: `threshold`
- Type: integer
- Default: 35

Days before a scrub is due when the scrub should start.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful scrub start.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
