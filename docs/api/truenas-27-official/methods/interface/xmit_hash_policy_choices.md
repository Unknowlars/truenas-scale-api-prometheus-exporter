---
title: interface.xmit_hash_policy_choices
kind: method
source_rst: _sources/api_methods_interface.xmit_hash_policy_choices.rst.txt
source_html: api_methods_interface.xmit_hash_policy_choices.html
required_roles:
  - NETWORK_INTERFACE_READ
  - READONLY_ADMIN
---

# interface.xmit_hash_policy_choices

## Summary

Available transmit hash policies for the LACP or LOADBALANCE lagg type interfaces.

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

- Schema name: `InterfaceXmitHashPolicyChoicesResult`
- Type: object

InterfaceXmitHashPolicyChoicesResult return fields.
- No Additional Properties
<a id="headingReturn_value_LAYER2"></a>
<a id="Return_value_LAYER2"></a>
#### LAYER2 (required)

- Schema name: `Layer2`
- Type: const

Use MAC addresses for traffic distribution across bond members.
- Specific value: `"LAYER2"`

<a id="headingReturn_value_LAYER2+3"></a>
<a id="Return_value_LAYER2+3"></a>
#### LAYER2+3 (required)

- Schema name: `Layer2+3`
- Type: const

Use MAC and IP addresses for traffic distribution across bond members.
- Specific value: `"LAYER2+3"`

<a id="headingReturn_value_LAYER3+4"></a>
<a id="Return_value_LAYER3+4"></a>
#### LAYER3+4 (required)

- Schema name: `Layer3+4`
- Type: const

Use MAC, IP, and TCP/UDP port information for traffic distribution across bond members.
- Specific value: `"LAYER3+4"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
