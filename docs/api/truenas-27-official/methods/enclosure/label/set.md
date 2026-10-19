---
title: enclosure.label.set
kind: method
source_rst: _sources/api_methods_enclosure.label.set.rst.txt
source_html: api_methods_enclosure.label.set.html
required_roles:
  - ENCLOSURE_WRITE
---

# enclosure.label.set

## Summary

Set a user-defined label for the enclosure identified by `id`.

A JSON-RPC `error` response (code `-32602`, *Invalid params*) is returned when no enclosure with the given `id` exists.

## Required Roles

- `ENCLOSURE_WRITE`

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
- Type: string

Enclosure identifier to set the label for.

#### Parameter 2: label

<a id="Call_parameters_items_i1"></a>
#### label

- Schema name: `label`
- Type: string

New label to assign to the enclosure.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the enclosure label is successfully updated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
