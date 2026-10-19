---
title: core.arp
kind: method
source_rst: _sources/api_methods_core.arp.rst.txt
source_html: api_methods_core.arp.html
required_roles:
  - FULL_ADMIN
---

# core.arp

## Required Roles

- `FULL_ADMIN`

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

CoreArpArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_ip"></a>
<a id="Call_parameters_items_i0_ip"></a>
##### ip

- Schema name: `Ip`
- Default: null

IP address to look up in ARP table or `null` for all entries.
<a id="Call_parameters_items_i0_ip_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_ip_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_ip_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_ip_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_ip_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_interface"></a>
<a id="Call_parameters_items_i0_interface"></a>
##### interface

- Schema name: `Interface`
- Default: null

Network interface to query or `null` for all interfaces.
<a id="Call_parameters_items_i0_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object mapping IP addresses to MAC addresses from the ARP table.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
