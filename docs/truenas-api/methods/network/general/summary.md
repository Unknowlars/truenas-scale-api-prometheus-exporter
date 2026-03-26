---
title: network.general.summary
kind: method
source_rst: _sources/api_methods_network.general.summary.rst.txt
source_html: api_methods_network.general.summary.html
required_roles:
  - NETWORK_GENERAL_READ
---

# network.general.summary

## Summary

Retrieve general information for current Network.

Returns a dictionary. For example:

.. examples(websocket)::

:::javascript { "ips": { "vtnet0": { "IPV4": [ "192.168.0.15/24" ] } }, "default_routes": [ "192.168.0.1" ], "nameservers": [ "192.168.0.1" ] }

## Required Roles

- `NETWORK_GENERAL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `NetworkGeneralSummaryResult`
- Type: object

NetworkGeneralSummaryResult return fields.
- No Additional Properties
#### ips (required)

- Schema name: `Ips`
- Type: object

Object mapping interface names to their IP address information.
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `NetworkGeneralSummaryIP`
- Type: object
- No Additional Properties
###### IPV4

- Schema name: `Ipv4`
- Type: array of string

Array of IPv4 addresses assigned to this interface.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### IPV6

- Schema name: `Ipv6`
- Type: array of string

Array of IPv6 addresses assigned to this interface.
- No Additional Items

####### Each item of this array must be:

- Type: string

#### default_routes (required)

- Schema name: `Default Routes`
- Type: array

Array of default gateway addresses.
- No Additional Items

##### Each item of this array must be:

###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

#### nameservers (required)

- Schema name: `Nameservers`
- Type: array

Array of configured DNS server addresses.
- No Additional Items

##### Each item of this array must be:

###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
