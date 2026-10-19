---
title: service.started
kind: method
source_rst: _sources/api_methods_service.started.rst.txt
source_html: api_methods_service.started.html
required_roles:
  - SERVICE_READ
---

# service.started

## Summary

Test if service specified by `service` has been started.

## Required Roles

- `SERVICE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: service

<a id="Call_parameters_items_i0"></a>
#### service

- Schema name: `service`
- Type: string

Name of the service to check if running.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: boolean

Service is running.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
