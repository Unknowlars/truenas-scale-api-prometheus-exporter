---
title: nvmet.host_subsys.delete
kind: method
source_rst: _sources/api_methods_nvmet.host_subsys.delete.rst.txt
source_html: api_methods_nvmet.host_subsys.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.host_subsys.delete

## Summary

Delete `host`/`subsys` association of `id`.

If the subsystem does not have the `allow_any_host` attribute set, then this will remove access of the host to the subsystem.

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

ID of the host-subsystem association to delete.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the host-subsystem association is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
