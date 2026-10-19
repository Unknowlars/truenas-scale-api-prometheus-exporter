---
title: rdma.get_card_choices
kind: method
source_rst: _sources/api_methods_rdma.get_card_choices.rst.txt
source_html: api_methods_rdma.get_card_choices.html
required_roles:
  - NETWORK_INTERFACE_READ
  - READONLY_ADMIN
---

# rdma.get_card_choices

## Summary

Return an array containing details about each RDMA card. Dual cards will contain two RDMA links.

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

- Schema name: `Result`
- Type: array of object

Array of RDMA cards available on the system.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### RdmaCardConfig

- Schema name: `RdmaCardConfig`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the RDMA card.

<a id="headingReturn_value_items_serial"></a>
<a id="Return_value_items_serial"></a>
##### serial (required)

- Schema name: `Serial`
- Type: string

Serial number of the RDMA card.

<a id="headingReturn_value_items_product"></a>
<a id="Return_value_items_product"></a>
##### product (required)

- Schema name: `Product`
- Type: string

Product name of the RDMA card.

<a id="headingReturn_value_items_part_number"></a>
<a id="Return_value_items_part_number"></a>
##### part_number (required)

- Schema name: `Part Number`
- Type: string

Part number of the RDMA card.

<a id="headingReturn_value_items_links"></a>
<a id="Return_value_items_links"></a>
##### links (required)

- Schema name: `Links`
- Type: array of object

Array of RDMA link configurations available on this card.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_links_items"></a>
###### RdmaLinkConfig

- Schema name: `RdmaLinkConfig`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_links_items_rdma"></a>
<a id="Return_value_items_links_items_rdma"></a>
###### rdma (required)

- Schema name: `Rdma`
- Type: string

Name of the RDMA device.

<a id="headingReturn_value_items_links_items_netdev"></a>
<a id="Return_value_items_links_items_netdev"></a>
###### netdev (required)

- Schema name: `Netdev`
- Type: string

Name of the corresponding network device.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
