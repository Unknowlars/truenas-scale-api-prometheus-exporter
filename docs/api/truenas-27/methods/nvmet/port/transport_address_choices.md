---
title: nvmet.port.transport_address_choices
kind: method
source_rst: _sources/api_methods_nvmet.port.transport_address_choices.rst.txt
source_html: api_methods_nvmet.port.transport_address_choices.html
required_roles:
  - READONLY_ADMIN
  - SHARING_NVME_TARGET_READ
---

# nvmet.port.transport_address_choices

## Summary

Returns possible choices for `addr_traddr` attribute of `port` create and update.

## Required Roles

- `READONLY_ADMIN`
- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: addr_trtype

<a id="Call_parameters_items_i0"></a>
#### addr_trtype

- Schema name: `addr_trtype`
- Type: enum (of string)

Fabric transport technology name.
##### Must be one of:

- "TCP"
- "RDMA"
- "FC"

#### Parameter 2: force_ana

<a id="Call_parameters_items_i1"></a>
#### force_ana

- Schema name: `force_ana`
- Type: boolean
- Default: false

Return information as if ANA was enabled.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object mapping transport addresses to their descriptions.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
