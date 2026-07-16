---
title: rdma.get_card_choices
kind: method
source_rst: _sources/api_methods_rdma.get_card_choices.rst.txt
source_html: api_methods_rdma.get_card_choices.html
required_roles:
  - NETWORK_INTERFACE_READ | READONLY_ADMIN
---

# rdma.get_card_choices

## Summary

Return an array containing details about each RDMA card. Dual cards will contain two RDMA links.

## Required Roles

- `NETWORK_INTERFACE_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of RDMA cards available on the system.
- No Additional Items

#### Each item of this array must be:

#### RdmaCardConfig

- Schema name: `RdmaCardConfig`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name of the RDMA card.

##### serial (required)

- Schema name: `Serial`
- Type: string

Serial number of the RDMA card.

##### product (required)

- Schema name: `Product`
- Type: string

Product name of the RDMA card.

##### part_number (required)

- Schema name: `Part Number`
- Type: string

Part number of the RDMA card.

##### links (required)

- Schema name: `Links`
- Type: array of object

Array of RDMA link configurations available on this card.
- No Additional Items

###### Each item of this array must be:

###### RdmaLinkConfig

- Schema name: `RdmaLinkConfig`
- Type: object
- No Additional Properties
####### rdma (required)

- Schema name: `Rdma`
- Type: string

Name of the RDMA device.

####### netdev (required)

- Schema name: `Netdev`
- Type: string

Name of the corresponding network device.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
