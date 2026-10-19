---
title: config.reset
kind: method
source_rst: _sources/api_methods_config.reset.rst.txt
source_html: api_methods_config.reset.html
required_roles:
  - FULL_ADMIN
---

# config.reset

## Summary

Reset database to configuration defaults.

When configured to reboot, this job reboots the system after it has completed with a delay of 10 seconds.

This method is a job.

## Required Roles

- `FULL_ADMIN`

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
- Default: {"reboot": true}

Options controlling the configuration reset behavior.
- No Additional Properties
<a id="headingCall_parameters_items_i0_reboot"></a>
<a id="Call_parameters_items_i0_reboot"></a>
##### reboot

- Schema name: `Reboot`
- Type: boolean
- Default: true

Whether to reboot the system after resetting configuration.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the configuration reset is successfully initiated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
