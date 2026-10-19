---
title: interface.lacpdu_rate_choices
kind: method
source_rst: _sources/api_methods_interface.lacpdu_rate_choices.rst.txt
source_html: api_methods_interface.lacpdu_rate_choices.html
required_roles:
  - NETWORK_INTERFACE_READ
  - READONLY_ADMIN
---

# interface.lacpdu_rate_choices

## Summary

Available lacpdu rate policies for the LACP lagg type interfaces.

## Required Roles

- `NETWORK_INTERFACE_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `InterfaceLacpduRateChoicesResult`
- Type: object

InterfaceLacpduRateChoicesResult return fields.
- No Additional Properties
<a id="headingReturn_value_SLOW"></a>
<a id="Return_value_SLOW"></a>
#### SLOW (required)

- Schema name: `Slow`
- Type: const

Send LACPDUs every 30 seconds for standard link monitoring.
- Specific value: `"SLOW"`

<a id="headingReturn_value_FAST"></a>
<a id="Return_value_FAST"></a>
#### FAST (required)

- Schema name: `Fast`
- Type: const

Send LACPDUs every 1 second for rapid link failure detection.
- Specific value: `"FAST"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
