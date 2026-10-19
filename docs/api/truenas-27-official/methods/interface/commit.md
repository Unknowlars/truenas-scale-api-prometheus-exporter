---
title: interface.commit
kind: method
source_rst: _sources/api_methods_interface.commit.rst.txt
source_html: api_methods_interface.commit.html
required_roles:
  - NETWORK_INTERFACE_WRITE
---

# interface.commit

## Summary

Commit/apply pending interfaces changes.

Fails if any interface could not be configured, rolling the changes back first when `rollback` is set.

## Required Roles

- `NETWORK_INTERFACE_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: options

<a id="Call_parameters_items_i0"></a>
#### options

- Schema name: `options`
- Type: object

Options for committing interface changes.
- No Additional Properties
<a id="headingCall_parameters_items_i0_rollback"></a>
<a id="Call_parameters_items_i0_rollback"></a>
##### rollback

- Schema name: `Rollback`
- Type: boolean
- Default: true

Roll back changes in case they fail to apply.

<a id="headingCall_parameters_items_i0_checkin_timeout"></a>
<a id="Call_parameters_items_i0_checkin_timeout"></a>
##### checkin_timeout

- Schema name: `Checkin Timeout`
- Type: integer
- Default: 60

Number of seconds to wait for the checkin call to acknowledge the interface changes happened as planned from the user. If checkin does not happen within this period of time, the changes will get reverted.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

No return value for successful commit operation.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
