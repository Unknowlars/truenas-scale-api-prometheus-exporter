---
title: interface.network_config_to_be_removed
kind: method
source_rst: _sources/api_methods_interface.network_config_to_be_removed.rst.txt
source_html: api_methods_interface.network_config_to_be_removed.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.network_config_to_be_removed

## Summary

Determines which network configuration items will be removed during interface setup.

On a fresh install of SCALE, DHCP is started for every interface so IP addresses/routes could be installed via that program. However, when the end-user goes to configure the first interface we tear down all other interfaces configs AND delete the default route. We also remove the default route if the configured gateway doesn't match the one currently installed in kernel.

Additionally, this checks for nameserver configurations that exist in the current network state but are not configured in the database, indicating they will be removed during reconfiguration.

## Required Roles

- `NETWORK_INTERFACE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of enum (of string)

The network configuration fields that will be wiped on the next `interface.checkin` call. The current values of these fields can be retrieved by calling `network.configuration.config`.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
- Type: enum (of string)
##### Must be one of:

- "ipv4gateway"
- "nameserver1"
- "nameserver2"
- "nameserver3"

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
