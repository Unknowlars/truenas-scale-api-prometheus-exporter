---
title: interface.services_restarted_on_sync
kind: method
source_rst: _sources/api_methods_interface.services_restarted_on_sync.rst.txt
source_html: api_methods_interface.services_restarted_on_sync.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# interface.services_restarted_on_sync

## Summary

Returns which services will be set to listen on 0.0.0.0 (and, thus, restarted) on sync.

Example result::

[ // Samba service will be set ot listen on 0.0.0.0 and restarted because it was set up to listen on // 192.168.0.1 which is being removed. {"type": "SYSTEM_SERVICE", "service": "cifs", "ips": ["192.168.0.1"]}, ]

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
- Type: array of object

List of services that were restarted during interface synchronization.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### InterfaceServicesRestartedOnSyncItem

- Schema name: `InterfaceServicesRestartedOnSyncItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_type"></a>
<a id="Return_value_items_type"></a>
##### type (required)

- Schema name: `Type`
- Type: string

The type of service restart event.

<a id="headingReturn_value_items_service"></a>
<a id="Return_value_items_service"></a>
##### service (required)

- Schema name: `Service`
- Type: string

The name of the service that was restarted.

<a id="headingReturn_value_items_ips"></a>
<a id="Return_value_items_ips"></a>
##### ips (required)

- Schema name: `Ips`
- Type: array of string

List of IP addresses associated with the service restart.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_ips_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
