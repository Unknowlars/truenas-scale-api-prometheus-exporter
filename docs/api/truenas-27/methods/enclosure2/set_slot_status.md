---
title: enclosure2.set_slot_status
kind: method
source_rst: _sources/api_methods_enclosure2.set_slot_status.rst.txt
source_html: api_methods_enclosure2.set_slot_status.html
required_roles:
  - ENCLOSURE_WRITE
---

# enclosure2.set_slot_status

## Summary

Set enclosure bay number `slot` to `status` for `enclosure_id`.

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

#### Parameter 1: Enclosure2SetSlotStatus

<a id="Call_parameters_items_i0"></a>
#### Enclosure2SetSlotStatus

- Schema name: `Enclosure2SetSlotStatus`
- Type: object

Enclosure2SetSlotStatusArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_enclosure_id"></a>
<a id="Call_parameters_items_i0_enclosure_id"></a>
##### enclosure_id (required)

- Schema name: `Enclosure Id`
- Type: string

Logical identifier of the enclosure.

<a id="headingCall_parameters_items_i0_slot"></a>
<a id="Call_parameters_items_i0_slot"></a>
##### slot (required)

- Schema name: `Slot`
- Type: integer

Number of the drive bay whose status should change.

<a id="headingCall_parameters_items_i0_status"></a>
<a id="Call_parameters_items_i0_status"></a>
##### status (required)

- Schema name: `Status`
- Type: enum (of string)

The status to set on the slot.
###### Must be one of:

- "CLEAR"
- "ON"
- "OFF"

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
