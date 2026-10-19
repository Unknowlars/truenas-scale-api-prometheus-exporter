---
title: nvmet.subsys.delete
kind: method
source_rst: _sources/api_methods_nvmet.subsys.delete.rst.txt
source_html: api_methods_nvmet.subsys.delete.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.subsys.delete

## Summary

Delete NVMe target subsystem (`subsys`) of `id`.

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

ID of the subsystem to delete.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Options for subsystem deletion behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force subsystem deletion, even if currently associated with one or more namespaces or ports.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Indicates successful deletion of the subsystem.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
