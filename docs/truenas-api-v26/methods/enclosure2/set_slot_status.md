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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: Enclosure2SetSlotStatus

#### Enclosure2SetSlotStatus

- Schema name: `Enclosure2SetSlotStatus`
- Type: object

Enclosure2SetSlotStatusArgs parameters.
- No Additional Properties
##### enclosure_id (required)

- Schema name: `Enclosure Id`
- Type: string

Logical identifier of the enclosure.

##### slot (required)

- Schema name: `Slot`
- Type: integer

Number of the drive bay whose status should change.

##### status (required)

- Schema name: `Status`
- Type: enum (of string)

The status to set on the slot.

### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
