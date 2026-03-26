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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Request parameters for IPMI chassis information.
- No Additional Properties
##### query-remote

- Schema name: `Query-Remote`
- Type: boolean
- Default: false

Whether to query remote IPMI chassis information on HA systems.

### Return value

- Schema name: `Result`

IPMI chassis information or raw dictionary if parsing fails.
#### Any of

##### IPMIChassisInfo

- Schema name: `IPMIChassisInfo`
- Type: object
- No Additional Properties
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

###### power_overload (required)

- Schema name: `Power Overload`
- Type: string

Power overload status indicator.

###### interlock (required)

- Schema name: `Interlock`
- Type: string

Chassis interlock status.

###### power_fault (required)

- Schema name: `Power Fault`
- Type: string

Power fault status indicator.

###### power_control_fault (required)

- Schema name: `Power Control Fault`
- Type: string

Power control fault status indicator.

###### power_restore_policy (required)

- Schema name: `Power Restore Policy`
- Type: string

Policy for restoring power after a power loss.

###### last_power_event (required)

- Schema name: `Last Power Event`
- Type: string

Description of the last power-related event.

###### chassis_intrusion (required)

- Schema name: `Chassis Intrusion`
- Type: string

Chassis intrusion detection status.

###### front_panel_lockout (required)

- Schema name: `Front Panel Lockout`
- Type: string

Front panel lockout status indicator.

###### drive_fault (required)

- Schema name: `Drive Fault`
- Type: string

Drive fault status indicator.

###### cooling/fan_fault (required)

- Schema name: `Cooling/Fan Fault`
- Type: string

Cooling fan fault status indicator.

###### chassis_identify_state (required)

- Schema name: `Chassis Identify State`
- Type: string

Current chassis identify LED state.

##### Option 2

- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
