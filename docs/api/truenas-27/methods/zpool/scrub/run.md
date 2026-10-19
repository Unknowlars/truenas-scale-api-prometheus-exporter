---
title: zpool.scrub.run
kind: method
source_rst: _sources/api_methods_zpool.scrub.run.rst.txt
source_html: api_methods_zpool.scrub.run.html
required_roles:
  - POOL_WRITE
---

# zpool.scrub.run

## Summary

Start, pause, or cancel a scrub on a ZFS pool.

When `action` is START, the pool is validated before the scrub begins: the pool must be ONLINE or DEGRADED, must not have an active resilver, and the most recent scrub must be older than `threshold` days. If any of these checks fail the call returns silently (no error, no alert). The job blocks until the scrub finishes, is paused, or is canceled.

PAUSE and CANCEL skip validation entirely and operate on the pool directly.

At most 10 scrubs may run concurrently across all pools. Attempting to start an 11th raises an error.

On a successful START a `ScrubStarted` alert is created. If the start fails for a reason other than the threshold or HA checks, a `ScrubNotStarted` alert is created instead.

.. versionadded:: 27.0.0

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

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Scrub run parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_pool_name"></a>
<a id="Call_parameters_items_i0_pool_name"></a>
##### pool_name (required)

- Schema name: `Pool Name`
- Type: string

Name of the zpool.

<a id="headingCall_parameters_items_i0_scan_type"></a>
<a id="Call_parameters_items_i0_scan_type"></a>
##### scan_type

- Schema name: `Scan Type`
- Type: enum (of string)
- Default: "SCRUB"

SCRUB: full data integrity scan. ERRORSCRUB: targeted scan of blocks with known errors.
###### Must be one of:

- "SCRUB"
- "ERRORSCRUB"

<a id="headingCall_parameters_items_i0_action"></a>
<a id="Call_parameters_items_i0_action"></a>
##### action

- Schema name: `Action`
- Type: enum (of string)
- Default: "START"

START: begin or resume. PAUSE: pause in-progress scan. CANCEL: stop entirely.
###### Must be one of:

- "START"
- "PAUSE"
- "CANCEL"

<a id="headingCall_parameters_items_i0_threshold"></a>
<a id="Call_parameters_items_i0_threshold"></a>
##### threshold

- Schema name: `Threshold`
- Type: integer
- Default: 35

Days before a scrub is due when the scrub should start.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
