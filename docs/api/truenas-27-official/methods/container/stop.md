---
title: container.stop
kind: method
source_rst: _sources/api_methods_container.stop.rst.txt
source_html: api_methods_container.stop.html
required_roles:
  - CONTAINER_WRITE
---

# container.stop

## Summary

Stop `id` container.

This method is a job.

## Required Roles

- `CONTAINER_WRITE`

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

Container ID.

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "force": false,
  "force_after_timeout": false
}
```

Container stop options.
- No Additional Properties
<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Kill the container.

<a id="headingCall_parameters_items_i1_force_after_timeout"></a>
<a id="Call_parameters_items_i1_force_after_timeout"></a>
##### force_after_timeout

- Schema name: `Force After Timeout`
- Type: boolean
- Default: false

Kill the container if it does not stop within the `shutdown_timeout`.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
