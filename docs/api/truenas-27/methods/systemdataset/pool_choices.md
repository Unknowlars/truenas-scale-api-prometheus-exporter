---
title: systemdataset.pool_choices
kind: method
source_rst: _sources/api_methods_systemdataset.pool_choices.rst.txt
source_html: api_methods_systemdataset.pool_choices.html
required_roles:
  - DATASET_READ
  - POOL_READ
  - READONLY_ADMIN
---

# systemdataset.pool_choices

## Summary

Retrieve pool choices which can be used for configuring system dataset.

## Required Roles

- `DATASET_READ`
- `POOL_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: include_current_pool

<a id="Call_parameters_items_i0"></a>
#### include_current_pool

- Schema name: `include_current_pool`
- Type: boolean
- Default: true

Include the currently set pool in the result.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Names of pools that can be used for configuring system dataset.
<a id="headingReturn_value_additionalProperties"></a>
<a id="Return_value_additionalProperties"></a>
#### Additional Properties

Each additional property must conform to the following schema
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
