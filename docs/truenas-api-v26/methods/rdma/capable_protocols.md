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

Possible values are `NFS`, `ISER`, and `NVMET`. An empty array is returned when the system is not enterprise, is a MINI, or has no RDMA-capable network cards installed.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of enum (of string)

Array of protocols that support RDMA acceleration.
- No Additional Items

#### Each item of this array must be:

- Type: enum (of string)

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
