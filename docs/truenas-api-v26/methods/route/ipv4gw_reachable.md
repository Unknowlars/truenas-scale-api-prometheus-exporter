---
title: route.ipv4gw_reachable
kind: method
source_rst: _sources/api_methods_route.ipv4gw_reachable.rst.txt
source_html: api_methods_route.ipv4gw_reachable.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# route.ipv4gw_reachable

## Summary

Get the IPv4 gateway and verify if it is reachable by any interface.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: ipv4_gateway

#### ipv4_gateway

- Schema name: `ipv4_gateway`
- Type: string

IPv4 gateway address to test for reachability.

### Return value

- Schema name: `Result`
- Type: boolean

Whether the specified IPv4 gateway is reachable.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
