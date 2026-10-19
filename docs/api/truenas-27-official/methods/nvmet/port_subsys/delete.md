---
title: nvmet.port_subsys.delete
kind: method
source_rst: _sources/api_methods_nvmet.port_subsys.delete.rst.txt
source_html: api_methods_nvmet.port_subsys.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.port_subsys.delete

## Summary

Delete `port`/`subsys` association of `id`.

The specified subsystem will no longer be accessible on the `port`.

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the port-subsystem association to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the port-subsystem association is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
