---
title: failover.update
kind: method
source_rst: _sources/api_methods_failover.update.rst.txt
source_html: api_methods_failover.update.html
required_roles:
  - FAILOVER_WRITE
---

# failover.update

## Summary

Update failover configuration.

## Required Roles

- `FAILOVER_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

Updated failover configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i0_disabled"></a>
<a id="Call_parameters_items_i0_disabled"></a>
##### disabled

- Schema name: `Disabled`
- Type: boolean

When true, HA will be administratively disabled.

<a id="headingCall_parameters_items_i0_master"></a>
<a id="Call_parameters_items_i0_master"></a>
##### master

- Schema name: `Master`
- Type: boolean

Marks the particular node in the chassis as the master node. The standby node will have the opposite value.

<a id="headingCall_parameters_items_i0_timeout"></a>
<a id="Call_parameters_items_i0_timeout"></a>
##### timeout

- Schema name: `Timeout`
- Type: integer

The time to WAIT (in seconds) until a failover occurs when a network event occurs on an interface that is marked critical for failover AND HA is enabled and working appropriately. The default time to wait is 2 seconds. Maximum is 120 seconds. This value is used to derive the VRRPv3 advertisement interval, which cannot exceed 40.95 seconds (RFC 5798 section 5.2.7). **NOTE: This setting does NOT effect the `disabled` or `master` parameters.**
- Value must be greater or equal to `0` and lesser or equal to `120`

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `FailoverEntry`
- Type: object

The updated failover configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the failover configuration.

<a id="headingReturn_value_disabled"></a>
<a id="Return_value_disabled"></a>
#### disabled (required)

- Schema name: `Disabled`
- Type: boolean

When true, HA will be administratively disabled.

<a id="headingReturn_value_master"></a>
<a id="Return_value_master"></a>
#### master (required)

- Schema name: `Master`
- Type: boolean

Marks the particular node in the chassis as the master node. The standby node will have the opposite value.

<a id="headingReturn_value_timeout"></a>
<a id="Return_value_timeout"></a>
#### timeout (required)

- Schema name: `Timeout`
- Type: integer

The time to WAIT (in seconds) until a failover occurs when a network event occurs on an interface that is marked critical for failover AND HA is enabled and working appropriately. The default time to wait is 2 seconds. **NOTE: This setting does NOT effect the `disabled` or `master` parameters.**

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
