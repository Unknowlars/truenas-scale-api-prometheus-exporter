---
title: rdma.capable_protocols
kind: method
source_rst: _sources/api_methods_rdma.capable_protocols.rst.txt
source_html: api_methods_rdma.capable_protocols.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# rdma.capable_protocols

## Summary

Return the list of RDMA-capable protocols supported by this system.

Possible values are `NFS`, `ISER`, and `NVMET`. An empty array is returned when the system is not entitled to RDMA or has no RDMA-capable network cards installed.

## Required Roles

- `NETWORK_INTERFACE_READ`

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
- Type: array of enum (of string)

Array of protocols that support RDMA acceleration.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: enum (of string)
##### Must be one of:

- "ISER"
- "NFS"
- "NVMET"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
