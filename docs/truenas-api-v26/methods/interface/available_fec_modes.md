---
title: interface.available_fec_modes
kind: method
source_rst: _sources/api_methods_interface.available_fec_modes.rst.txt
source_html: api_methods_interface.available_fec_modes.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.available_fec_modes

## Summary

Returns FEC modes supported by interface `id`.

Returns an empty list if the interface does not exist or does not support FEC.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

ID of the interface to query for supported FEC modes.

### Return value

- Schema name: `Result`
- Type: array of enum (of string)

List of FEC modes supported by the interface. Empty list if FEC is not supported. "AUTO": Selects the best FEC mode based on cable/port capabilities "RS": RS-FEC (Reed-Solomon), often used for 25GbE/100GbE+ NICs "BASER": BaseR-FEC (FireCode) "OFF": Disables FEC "LLRS": Low Latency Reed-Solomon FEC, used for 25GBASE-KR/CR
- No Additional Items

#### Each item of this array must be:

- Type: enum (of string)

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
