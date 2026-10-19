---
title: ipmi.chassis.info
kind: method
source_rst: _sources/api_methods_ipmi.chassis.info.rst.txt
source_html: api_methods_ipmi.chassis.info.html
required_roles:
  - IPMI_READ
---

# ipmi.chassis.info

## Summary

Return IPMI chassis info.

`query-remote`: [optional] if True on HA system, then return info from remote controller.

## Required Roles

- `IPMI_READ`

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

Request parameters for IPMI chassis information.
- No Additional Properties
<a id="headingCall_parameters_items_i0_query-remote"></a>
<a id="Call_parameters_items_i0_query-remote"></a>
##### query-remote

- Schema name: `Query-Remote`
- Type: boolean
- Default: false

Whether to query remote IPMI chassis information on HA systems.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`

IPMI chassis information or raw dictionary if parsing fails.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [IPMIChassisInfo](#tab-pane_Return_value_anyOf_i0)

- Schema name: `IPMIChassisInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_system_power"></a>
<a id="Return_value_anyOf_i0_system_power"></a>
###### system_power (required)

- Schema name: `System Power`
- Type: string

Current system power state.
Examples:

```json
"on"
```
Examples:

```json
"off"
```

<a id="headingReturn_value_anyOf_i0_power_overload"></a>
<a id="Return_value_anyOf_i0_power_overload"></a>
###### power_overload (required)

- Schema name: `Power Overload`
- Type: string

Power overload status indicator.

<a id="headingReturn_value_anyOf_i0_interlock"></a>
<a id="Return_value_anyOf_i0_interlock"></a>
###### interlock (required)

- Schema name: `Interlock`
- Type: string

Chassis interlock status.

<a id="headingReturn_value_anyOf_i0_power_fault"></a>
<a id="Return_value_anyOf_i0_power_fault"></a>
###### power_fault (required)

- Schema name: `Power Fault`
- Type: string

Power fault status indicator.

<a id="headingReturn_value_anyOf_i0_power_control_fault"></a>
<a id="Return_value_anyOf_i0_power_control_fault"></a>
###### power_control_fault (required)

- Schema name: `Power Control Fault`
- Type: string

Power control fault status indicator.

<a id="headingReturn_value_anyOf_i0_power_restore_policy"></a>
<a id="Return_value_anyOf_i0_power_restore_policy"></a>
###### power_restore_policy (required)

- Schema name: `Power Restore Policy`
- Type: string

Policy for restoring power after a power loss.

<a id="headingReturn_value_anyOf_i0_last_power_event"></a>
<a id="Return_value_anyOf_i0_last_power_event"></a>
###### last_power_event (required)

- Schema name: `Last Power Event`
- Type: string

Description of the last power-related event.

<a id="headingReturn_value_anyOf_i0_chassis_intrusion"></a>
<a id="Return_value_anyOf_i0_chassis_intrusion"></a>
###### chassis_intrusion (required)

- Schema name: `Chassis Intrusion`
- Type: string

Chassis intrusion detection status.

<a id="headingReturn_value_anyOf_i0_front_panel_lockout"></a>
<a id="Return_value_anyOf_i0_front_panel_lockout"></a>
###### front_panel_lockout (required)

- Schema name: `Front Panel Lockout`
- Type: string

Front panel lockout status indicator.

<a id="headingReturn_value_anyOf_i0_drive_fault"></a>
<a id="Return_value_anyOf_i0_drive_fault"></a>
###### drive_fault (required)

- Schema name: `Drive Fault`
- Type: string

Drive fault status indicator.

<a id="headingReturn_value_anyOf_i0_cooling/fan_fault"></a>
<a id="Return_value_anyOf_i0_cooling/fan_fault"></a>
###### cooling/fan_fault (required)

- Schema name: `Cooling/Fan Fault`
- Type: string

Cooling fan fault status indicator.

<a id="headingReturn_value_anyOf_i0_chassis_identify_state"></a>
<a id="Return_value_anyOf_i0_chassis_identify_state"></a>
###### chassis_identify_state (required)

- Schema name: `Chassis Identify State`
- Type: string

Current chassis identify LED state.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
