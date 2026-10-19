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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NetworkGeneralSummaryResult`
- Type: object

NetworkGeneralSummaryResult return fields.
- No Additional Properties
<a id="headingReturn_value_ips"></a>
<a id="Return_value_ips"></a>
#### ips (required)

- Schema name: `Ips`
- Type: object

Object mapping interface names to their IP address information.
<a id="headingReturn_value_ips_additionalProperties"></a>
<a id="Return_value_ips_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `NetworkGeneralSummaryIP`
- Type: object
- No Additional Properties
<a id="headingReturn_value_ips_additionalProperties_IPV4"></a>
<a id="Return_value_ips_additionalProperties_IPV4"></a>
###### IPV4

- Schema name: `Ipv4`
- Type: array of string

Array of IPv4 addresses assigned to this interface.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ips_additionalProperties_IPV4_items"></a>
- Type: string

<a id="headingReturn_value_ips_additionalProperties_IPV6"></a>
<a id="Return_value_ips_additionalProperties_IPV6"></a>
###### IPV6

- Schema name: `Ipv6`
- Type: array of string

Array of IPv6 addresses assigned to this interface.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_ips_additionalProperties_IPV6_items"></a>
- Type: string

<a id="headingReturn_value_default_routes"></a>
<a id="Return_value_default_routes"></a>
#### default_routes (required)

- Schema name: `Default Routes`
- Type: array

Array of default gateway addresses.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_default_routes_items"></a>
<a id="Return_value_default_routes_items_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_default_routes_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_default_routes_items_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_default_routes_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_default_routes_items_anyOf_i1)

- Type: string

<a id="headingReturn_value_nameservers"></a>
<a id="Return_value_nameservers"></a>
#### nameservers (required)

- Schema name: `Nameservers`
- Type: array

Array of configured DNS server addresses.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_nameservers_items"></a>
<a id="Return_value_nameservers_items_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_nameservers_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nameservers_items_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_nameservers_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nameservers_items_anyOf_i1)

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
