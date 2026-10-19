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

Get all IPv4 / IPv6 from all valid interfaces.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object

Options for filtering IP addresses in use.
- No Additional Properties
<a id="headingCall_parameters_items_i0_ipv4"></a>
<a id="Call_parameters_items_i0_ipv4"></a>
##### ipv4

- Schema name: `Ipv4`
- Type: boolean
- Default: true

Include IPv4 addresses in the results.

<a id="headingCall_parameters_items_i0_ipv6"></a>
<a id="Call_parameters_items_i0_ipv6"></a>
##### ipv6

- Schema name: `Ipv6`
- Type: boolean
- Default: true

Include IPv6 addresses in the results.

<a id="headingCall_parameters_items_i0_ipv6_link_local"></a>
<a id="Call_parameters_items_i0_ipv6_link_local"></a>
##### ipv6_link_local

- Schema name: `Ipv6 Link Local`
- Type: boolean
- Default: false

Include IPv6 link-local addresses in the results.

<a id="headingCall_parameters_items_i0_loopback"></a>
<a id="Call_parameters_items_i0_loopback"></a>
##### loopback

- Schema name: `Loopback`
- Type: boolean
- Default: false

Return loopback interface addresses.

<a id="headingCall_parameters_items_i0_any"></a>
<a id="Call_parameters_items_i0_any"></a>
##### any

- Schema name: `Any`
- Type: boolean
- Default: false

Return wildcard addresses (0.0.0.0 and ::).

<a id="headingCall_parameters_items_i0_static"></a>
<a id="Call_parameters_items_i0_static"></a>
##### static

- Schema name: `Static`
- Type: boolean
- Default: false

Only return configured static IPs.

<a id="headingCall_parameters_items_i0_interfaces"></a>
<a id="Call_parameters_items_i0_interfaces"></a>
##### interfaces

- Schema name: `Interfaces`
- Type: array of string

Only return IPs from specified interfaces. If empty, returns IPs from all interfaces.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_interfaces_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### InterfaceIPInUseItem

- Schema name: `InterfaceIPInUseItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_type"></a>
<a id="Return_value_items_type"></a>
##### type (required)

- Schema name: `Type`
- Type: string

The type of IP address (INET for IPv4, INET6 for IPv6).

<a id="headingReturn_value_items_address"></a>
<a id="Return_value_items_address"></a>
##### address (required)

- Schema name: `Address`

The IP address that is in use.
<a id="Return_value_items_address_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_address_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_items_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_address_anyOf_i1)

- Type: string

<a id="headingReturn_value_items_netmask"></a>
<a id="Return_value_items_netmask"></a>
##### netmask (required)

- Schema name: `Netmask`
- Type: integer

The network mask in CIDR notation.

<a id="headingReturn_value_items_broadcast"></a>
<a id="Return_value_items_broadcast"></a>
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
