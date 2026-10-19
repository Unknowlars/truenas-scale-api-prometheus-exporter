---
title: core.get_methods
kind: method
source_rst: _sources/api_methods_core.get_methods.rst.txt
source_html: api_methods_core.get_methods.html
required_roles:
  []
---

# core.get_methods

## Summary

Return methods metadata of every available service.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: service

<a id="Call_parameters_items_i0"></a>
#### service

- Schema name: `service`
- Default: null

Filters the result for a single service.
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

#### Parameter 2: target

<a id="Call_parameters_items_i1"></a>
#### target

- Schema name: `target`
- Type: enum (of string)
- Default: "WS"

Target interface to get methods for. `WS` for WebSocket, `CLI` for command line, `REST` for HTTP API.
##### Must be one of:

- "WS"
- "CLI"
- "REST"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object mapping method names to their signatures, documentation, and metadata.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
