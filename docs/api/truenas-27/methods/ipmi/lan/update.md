---
title: ipmi.lan.update
kind: method
source_rst: _sources/api_methods_ipmi.lan.update.rst.txt
source_html: api_methods_ipmi.lan.update.html
required_roles:
  - IPMI_WRITE
---

# ipmi.lan.update

## Summary

Update IPMI channel configuration

## Required Roles

- `IPMI_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: channel

<a id="Call_parameters_items_i0"></a>
#### channel

- Schema name: `channel`
- Type: integer

IPMI LAN channel number to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`

IPMI LAN configuration data (DHCP or static IP).
<a id="Call_parameters_items_i1_oneOf"></a>
##### One of

<a id="tab-pane_Call_parameters_items_i1_oneOf_i0"></a>
###### [IPMILanUpdateOptionsDHCP](#tab-pane_Call_parameters_items_i1_oneOf_i0)

- Schema name: `IPMILanUpdateOptionsDHCP`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_oneOf_i0_dhcp"></a>
<a id="Call_parameters_items_i1_oneOf_i0_dhcp"></a>
###### dhcp (required)

- Schema name: `Dhcp`
- Type: const

Turn on DHCP protocol for IP address management.
- Specific value: `true`

<a id="headingCall_parameters_items_i1_oneOf_i0_password"></a>
<a id="Call_parameters_items_i1_oneOf_i0_password"></a>
###### password

- Schema name: `Password`
- Default: null

The password to be applied. Must be between 8 and 16 characters long and contain only ascii upper,lower, 0-9, and special characters.
<a id="Call_parameters_items_i1_oneOf_i0_password_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_oneOf_i0_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_oneOf_i0_password_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_oneOf_i0_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_oneOf_i0_password_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_oneOf_i0_vlan"></a>
<a id="Call_parameters_items_i1_oneOf_i0_vlan"></a>
###### vlan

- Schema name: `Vlan`
- Default: null

The vlan tag number. A null value disables tagging.
<a id="Call_parameters_items_i1_oneOf_i0_vlan_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_oneOf_i0_vlan_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_oneOf_i0_vlan_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `4096`

<a id="tab-pane_Call_parameters_items_i1_oneOf_i0_vlan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_oneOf_i0_vlan_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_oneOf_i0_apply_remote"></a>
<a id="Call_parameters_items_i1_oneOf_i0_apply_remote"></a>
###### apply_remote

- Schema name: `Apply Remote`
- Type: boolean
- Default: false

If on an HA system, and this field is set to True, the settings will be sent to the remote controller.

<a id="tab-pane_Call_parameters_items_i1_oneOf_i1"></a>
###### [IPMILanUpdateOptionsStatic](#tab-pane_Call_parameters_items_i1_oneOf_i1)

- Schema name: `IPMILanUpdateOptionsStatic`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_oneOf_i1_dhcp"></a>
<a id="Call_parameters_items_i1_oneOf_i1_dhcp"></a>
###### dhcp (required)

- Schema name: `Dhcp`
- Type: const

Provide a static IP address.
- Specific value: `false`

<a id="headingCall_parameters_items_i1_oneOf_i1_password"></a>
<a id="Call_parameters_items_i1_oneOf_i1_password"></a>
###### password

- Schema name: `Password`
- Default: null

The password to be applied. Must be between 8 and 16 characters long and contain only ascii upper,lower, 0-9, and special characters.
<a id="Call_parameters_items_i1_oneOf_i1_password_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_oneOf_i1_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_oneOf_i1_password_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_oneOf_i1_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_oneOf_i1_password_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_oneOf_i1_vlan"></a>
<a id="Call_parameters_items_i1_oneOf_i1_vlan"></a>
###### vlan

- Schema name: `Vlan`
- Default: null

The vlan tag number. A null value disables tagging.
<a id="Call_parameters_items_i1_oneOf_i1_vlan_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_oneOf_i1_vlan_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_oneOf_i1_vlan_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `4096`

<a id="tab-pane_Call_parameters_items_i1_oneOf_i1_vlan_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_oneOf_i1_vlan_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_oneOf_i1_apply_remote"></a>
<a id="Call_parameters_items_i1_oneOf_i1_apply_remote"></a>
###### apply_remote

- Schema name: `Apply Remote`
- Type: boolean
- Default: false

If on an HA system, and this field is set to True, the settings will be sent to the remote controller.

<a id="headingCall_parameters_items_i1_oneOf_i1_ipaddress"></a>
<a id="Call_parameters_items_i1_oneOf_i1_ipaddress"></a>
###### ipaddress (required)

- Schema name: `Ipaddress`
- Type: string

The IPv4 address in the form of `192.168.1.150`.

<a id="headingCall_parameters_items_i1_oneOf_i1_netmask"></a>
<a id="Call_parameters_items_i1_oneOf_i1_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`
- Type: string

The netmask in the form of `255.255.255.0`.

<a id="headingCall_parameters_items_i1_oneOf_i1_gateway"></a>
<a id="Call_parameters_items_i1_oneOf_i1_gateway"></a>
###### gateway (required)

- Schema name: `Gateway`
- Type: string

The gateway in the form of `192.168.1.1`.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: integer

Returns the channel number that was updated.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
