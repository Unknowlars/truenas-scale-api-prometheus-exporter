---
title: virt.global.get_network
kind: method
source_rst: _sources/api_methods_virt.global.get_network.rst.txt
source_html: api_methods_virt.global.get_network.html
required_roles:
  - VIRT_GLOBAL_READ
---

# virt.global.get_network

## Summary

Details for the given network.

## Required Roles

- `VIRT_GLOBAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: name

#### name

- Schema name: `name`
- Type: string

Name of the network configuration to retrieve.
- Must be at least `1` characters long

### Return value

- Schema name: `VirtGlobalGetNetworkResult`
- Type: object

VirtGlobalGetNetworkResult return fields.
- No Additional Properties
#### type (required)

- Schema name: `Type`
- Type: const

Type of network configuration (currently only bridge networks are supported).

#### managed (required)

- Schema name: `Managed`
- Type: boolean

Whether this network is managed by the virtualization system.

#### ipv4_address (required)

- Schema name: `Ipv4 Address`
- Type: string

IPv4 address and CIDR of the bridge network.
- Must be at least `1` characters long

#### ipv4_nat (required)

- Schema name: `Ipv4 Nat`
- Type: boolean

Whether IPv4 Network Address Translation is enabled for this bridge.

#### ipv6_address (required)

- Schema name: `Ipv6 Address`
- Type: string

IPv6 address and CIDR of the bridge network.
- Must be at least `1` characters long

#### ipv6_nat (required)

- Schema name: `Ipv6 Nat`
- Type: boolean

Whether IPv6 Network Address Translation is enabled for this bridge.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
