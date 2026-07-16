---
title: interface.ip_in_use
kind: method
source_rst: _sources/api_methods_interface.ip_in_use.rst.txt
source_html: api_methods_interface.ip_in_use.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.ip_in_use

## Summary

Get all IPv4 / IPv6 from all valid interfaces

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

#### options

- Schema name: `options`
- Type: object

Options for filtering IP addresses in use.
- No Additional Properties
##### ipv4

- Schema name: `Ipv4`
- Type: boolean
- Default: true

Include IPv4 addresses in the results.

##### ipv6

- Schema name: `Ipv6`
- Type: boolean
- Default: true

Include IPv6 addresses in the results.

##### ipv6_link_local

- Schema name: `Ipv6 Link Local`
- Type: boolean
- Default: false

Include IPv6 link-local addresses in the results.

##### loopback

- Schema name: `Loopback`
- Type: boolean
- Default: false

Return loopback interface addresses.

##### any

- Schema name: `Any`
- Type: boolean
- Default: false

Return wildcard addresses (0.0.0.0 and ::).

##### static

- Schema name: `Static`
- Type: boolean
- Default: false

Only return configured static IPs.

##### interfaces

- Schema name: `Interfaces`
- Type: array of string

Only return IPs from specified interfaces. If empty, returns IPs from all interfaces.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

#### InterfaceIPInUseItem

- Schema name: `InterfaceIPInUseItem`
- Type: object
- No Additional Properties
##### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

##### address (required)

- Schema name: `Address`

The IP address that is in use.
###### Any of

####### Option 1

- Type: const

####### Option 2

- Type: string

##### netmask (required)

- Schema name: `Netmask`
- Type: integer

The network mask in CIDR notation.

##### broadcast

- Schema name: `Broadcast`
- Type: string

The broadcast address for IPv4 networks.

Examples:

```json
[
    {
        "address": "fe80::5054:ff:fe16:4aac",
        "netmask": 64,
        "type": "INET6"
    },
    {
        "address": "192.168.122.148",
        "broadcast": "192.168.122.255",
        "netmask": 24,
        "type": "INET"
    }
]
```

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
