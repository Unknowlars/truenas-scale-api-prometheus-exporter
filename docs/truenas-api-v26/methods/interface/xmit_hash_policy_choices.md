---
title: interface.xmit_hash_policy_choices
kind: method
source_rst: _sources/api_methods_interface.xmit_hash_policy_choices.rst.txt
source_html: api_methods_interface.xmit_hash_policy_choices.html
required_roles:
  - NETWORK_INTERFACE_READ | READONLY_ADMIN
---

# interface.xmit_hash_policy_choices

## Summary

Available transmit hash policies for the LACP or LOADBALANCE lagg type interfaces.

## Required Roles

- `NETWORK_INTERFACE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `InterfaceXmitHashPolicyChoicesResult`
- Type: object

InterfaceXmitHashPolicyChoicesResult return fields.
- No Additional Properties
#### LAYER2 (required)

- Schema name: `Layer2`
- Type: const

Use MAC addresses for traffic distribution across bond members.

#### LAYER2+3 (required)

- Schema name: `Layer2+3`
- Type: const

Use MAC and IP addresses for traffic distribution across bond members.

#### LAYER3+4 (required)

- Schema name: `Layer3+4`
- Type: const

Use MAC, IP, and TCP/UDP port information for traffic distribution across bond members.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
