---
title: pool.scrub.scrub
kind: method
source_rst: _sources/api_methods_pool.scrub.scrub.rst.txt
source_html: api_methods_pool.scrub.scrub.html
required_roles:
  - POOL_WRITE
---

# pool.scrub.scrub

## Summary

Start, stop, or pause a scrub on pool `name`.

START begins a regular scrub and blocks until it finishes, is paused, or is canceled. STOP cancels an in-progress scrub. PAUSE pauses it.

.. deprecated:: 27.0.0 Use [zpool.scrub.run](../../zpool/scrub/run.md) instead.

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

#### Parameter 1: name

<a id="Call_parameters_items_i0"></a>
#### name

- Schema name: `name`
- Type: string

Name of the pool to perform scrub action on.

#### Parameter 2: action

<a id="Call_parameters_items_i1"></a>
#### action

- Schema name: `action`
- Type: enum (of string)
- Default: "START"

The scrub action to perform on the pool.
##### Must be one of:

- "START"
- "STOP"
- "PAUSE"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful scrub action.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
