---
title: system.shutdown
kind: method
source_rst: _sources/api_methods_system.shutdown.rst.txt
source_html: api_methods_system.shutdown.html
required_roles:
  - FULL_ADMIN
---

# system.shutdown

## Summary

Shuts down the operating system.

An "added" event of name "system" and id "shutdown" is emitted when shutdown is initiated.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: reason

<a id="Call_parameters_items_i0"></a>
#### reason

- Schema name: `reason`
- Type: string

Reason for the system shutdown.
- Must be at least `1` characters long

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for controlling the shutdown process.
- No Additional Properties
<a id="headingCall_parameters_items_i1_delay"></a>
<a id="Call_parameters_items_i1_delay"></a>
##### delay

- Schema name: `Delay`
- Default: null

Delay in seconds before shutting down. `null` for immediate shutdown.
<a id="Call_parameters_items_i1_delay_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_delay_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_delay_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_delay_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_delay_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful shutdown initiation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
