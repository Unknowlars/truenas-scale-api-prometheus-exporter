---
title: ups.update
kind: method
source_rst: _sources/api_methods_ups.update.rst.txt
source_html: api_methods_ups.update.html
required_roles:
  - SYSTEM_GENERAL_WRITE
---

# ups.update

## Summary

Update UPS Service Configuration.

`powerdown` when enabled, sets UPS to power off after shutting down the system.

`nocommwarntime` is a value in seconds which makes UPS Service wait the specified seconds before alerting that the Service cannot reach configured UPS.

`shutdowntimer` is a value in seconds which tells the Service to wait specified seconds for the UPS before initiating a shutdown. This only applies when `shutdown` is set to "BATT".

`shutdowncmd` is the command which is executed to initiate a shutdown. It defaults to "poweroff".

## Required Roles

- `SYSTEM_GENERAL_WRITE`

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

Data to update the UPS configuration.
- No Additional Properties
<a id="headingCall_parameters_items_i0_powerdown"></a>
<a id="Call_parameters_items_i0_powerdown"></a>
##### powerdown

- Schema name: `Powerdown`
- Type: boolean

Whether the UPS should power down after completing the shutdown sequence.

<a id="headingCall_parameters_items_i0_rmonitor"></a>
<a id="Call_parameters_items_i0_rmonitor"></a>
##### rmonitor

- Schema name: `Rmonitor`
- Type: boolean

Whether to enable remote monitoring of the UPS status over the network.

<a id="headingCall_parameters_items_i0_nocommwarntime"></a>
<a id="Call_parameters_items_i0_nocommwarntime"></a>
##### nocommwarntime

- Schema name: `Nocommwarntime`

Seconds to wait before warning about communication loss with UPS. `null` for default.
<a id="Call_parameters_items_i0_nocommwarntime_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_nocommwarntime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_nocommwarntime_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_nocommwarntime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_nocommwarntime_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_remoteport"></a>
<a id="Call_parameters_items_i0_remoteport"></a>
##### remoteport

- Schema name: `Remoteport`
- Type: integer

Network port for communicating with remote UPS monitoring systems.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingCall_parameters_items_i0_shutdowntimer"></a>
<a id="Call_parameters_items_i0_shutdowntimer"></a>
##### shutdowntimer

- Schema name: `Shutdowntimer`
- Type: integer

Seconds to wait after initiating shutdown before forcing power off.

<a id="headingCall_parameters_items_i0_hostsync"></a>
<a id="Call_parameters_items_i0_hostsync"></a>
##### hostsync

- Schema name: `Hostsync`
- Type: integer

Maximum seconds to wait for other systems to shutdown before continuing.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string

Human-readable description of this UPS configuration.

<a id="headingCall_parameters_items_i0_driver"></a>
<a id="Call_parameters_items_i0_driver"></a>
##### driver

- Schema name: `Driver`
- Type: string

UPS driver name that handles communication with the specific UPS hardware model.

<a id="headingCall_parameters_items_i0_extrausers"></a>
<a id="Call_parameters_items_i0_extrausers"></a>
##### extrausers

- Schema name: `Extrausers`
- Type: string

Additional user configurations for UPS monitoring access.

<a id="headingCall_parameters_items_i0_identifier"></a>
<a id="Call_parameters_items_i0_identifier"></a>
##### identifier

- Schema name: `Identifier`
- Type: string

Unique identifier name for this UPS device within the monitoring system.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_mode"></a>
<a id="Call_parameters_items_i0_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)

Operating mode. * `MASTER` controls the UPS directly * `SLAVE` monitors remotely
###### Must be one of:

- "MASTER"
- "SLAVE"

<a id="headingCall_parameters_items_i0_monpwd"></a>
<a id="Call_parameters_items_i0_monpwd"></a>
##### monpwd

- Schema name: `Monpwd`
- Type: string

Password for UPS monitoring authentication (required for updates).
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_monuser"></a>
<a id="Call_parameters_items_i0_monuser"></a>
##### monuser

- Schema name: `Monuser`
- Type: string

Username for UPS monitoring authentication.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `Options`
- Type: string

Additional configuration options passed to the UPS driver.

<a id="headingCall_parameters_items_i0_optionsupsd"></a>
<a id="Call_parameters_items_i0_optionsupsd"></a>
##### optionsupsd

- Schema name: `Optionsupsd`
- Type: string

Additional configuration options for the UPS daemon.

<a id="headingCall_parameters_items_i0_port"></a>
<a id="Call_parameters_items_i0_port"></a>
##### port

- Schema name: `Port`
- Type: string

Serial port or device path for UPS communication.

<a id="headingCall_parameters_items_i0_remotehost"></a>
<a id="Call_parameters_items_i0_remotehost"></a>
##### remotehost

- Schema name: `Remotehost`
- Type: string

Hostname or IP address of remote UPS server when operating in SLAVE mode.

<a id="headingCall_parameters_items_i0_shutdown"></a>
<a id="Call_parameters_items_i0_shutdown"></a>
##### shutdown

- Schema name: `Shutdown`
- Type: enum (of string)

Shutdown trigger condition: LOWBATT on low battery, BATT when on battery power.
###### Must be one of:

- "LOWBATT"
- "BATT"

<a id="headingCall_parameters_items_i0_shutdowncmd"></a>
<a id="Call_parameters_items_i0_shutdowncmd"></a>
##### shutdowncmd

- Schema name: `Shutdowncmd`

Custom command to execute during UPS shutdown sequence. `null` for default.
<a id="Call_parameters_items_i0_shutdowncmd_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_shutdowncmd_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_shutdowncmd_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_shutdowncmd_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_shutdowncmd_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `UPSEntry`
- Type: object

The updated UPS configuration.
- No Additional Properties
<a id="headingReturn_value_powerdown"></a>
<a id="Return_value_powerdown"></a>
#### powerdown (required)

- Schema name: `Powerdown`
- Type: boolean

Whether the UPS should power down after completing the shutdown sequence.

<a id="headingReturn_value_rmonitor"></a>
<a id="Return_value_rmonitor"></a>
#### rmonitor (required)

- Schema name: `Rmonitor`
- Type: boolean

Whether to enable remote monitoring of the UPS status over the network.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the UPS configuration.

<a id="headingReturn_value_nocommwarntime"></a>
<a id="Return_value_nocommwarntime"></a>
#### nocommwarntime (required)

- Schema name: `Nocommwarntime`

Seconds to wait before warning about communication loss with UPS. `null` for default.
<a id="Return_value_nocommwarntime_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nocommwarntime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nocommwarntime_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_nocommwarntime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nocommwarntime_anyOf_i1)

- Type: null

<a id="headingReturn_value_remoteport"></a>
<a id="Return_value_remoteport"></a>
#### remoteport (required)

- Schema name: `Remoteport`
- Type: integer

Network port for communicating with remote UPS monitoring systems.
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="headingReturn_value_shutdowntimer"></a>
<a id="Return_value_shutdowntimer"></a>
#### shutdowntimer (required)

- Schema name: `Shutdowntimer`
- Type: integer

Seconds to wait after initiating shutdown before forcing power off.

<a id="headingReturn_value_hostsync"></a>
<a id="Return_value_hostsync"></a>
#### hostsync (required)

- Schema name: `Hostsync`
- Type: integer

Maximum seconds to wait for other systems to shutdown before continuing.
- Value must be greater or equal to `0`

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of this UPS configuration.

<a id="headingReturn_value_driver"></a>
<a id="Return_value_driver"></a>
#### driver (required)

- Schema name: `Driver`
- Type: string

UPS driver name that handles communication with the specific UPS hardware model.

<a id="headingReturn_value_extrausers"></a>
<a id="Return_value_extrausers"></a>
#### extrausers (required)

- Schema name: `Extrausers`
- Type: string

Additional user configurations for UPS monitoring access.

<a id="headingReturn_value_identifier"></a>
<a id="Return_value_identifier"></a>
#### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier name for this UPS device within the monitoring system.
- Must be at least `1` characters long

<a id="headingReturn_value_mode"></a>
<a id="Return_value_mode"></a>
#### mode (required)

- Schema name: `Mode`
- Type: enum (of string)

Operating mode. * `MASTER` controls the UPS directly * `SLAVE` monitors remotely
##### Must be one of:

- "MASTER"
- "SLAVE"

<a id="headingReturn_value_monpwd"></a>
<a id="Return_value_monpwd"></a>
#### monpwd (required)

- Schema name: `Monpwd`
- Type: string

Password for UPS monitoring authentication.

<a id="headingReturn_value_monuser"></a>
<a id="Return_value_monuser"></a>
#### monuser (required)

- Schema name: `Monuser`
- Type: string

Username for UPS monitoring authentication.
- Must be at least `1` characters long

<a id="headingReturn_value_options"></a>
<a id="Return_value_options"></a>
#### options (required)

- Schema name: `Options`
- Type: string

Additional configuration options passed to the UPS driver.

<a id="headingReturn_value_optionsupsd"></a>
<a id="Return_value_optionsupsd"></a>
#### optionsupsd (required)

- Schema name: `Optionsupsd`
- Type: string

Additional configuration options for the UPS daemon.

<a id="headingReturn_value_port"></a>
<a id="Return_value_port"></a>
#### port (required)

- Schema name: `Port`
- Type: string

Serial port or device path for UPS communication.

<a id="headingReturn_value_remotehost"></a>
<a id="Return_value_remotehost"></a>
#### remotehost (required)

- Schema name: `Remotehost`
- Type: string

Hostname or IP address of remote UPS server when operating in SLAVE mode.

<a id="headingReturn_value_shutdown"></a>
<a id="Return_value_shutdown"></a>
#### shutdown (required)

- Schema name: `Shutdown`
- Type: enum (of string)

Shutdown trigger condition: LOWBATT on low battery, BATT when on battery power.
##### Must be one of:

- "LOWBATT"
- "BATT"

<a id="headingReturn_value_shutdowncmd"></a>
<a id="Return_value_shutdowncmd"></a>
#### shutdowncmd (required)

- Schema name: `Shutdowncmd`

Custom command to execute during UPS shutdown sequence. `null` for default.
<a id="Return_value_shutdowncmd_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_shutdowncmd_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_shutdowncmd_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_shutdowncmd_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_shutdowncmd_anyOf_i1)

- Type: null

<a id="headingReturn_value_complete_identifier"></a>
<a id="Return_value_complete_identifier"></a>
#### complete_identifier (required)

- Schema name: `Complete Identifier`
- Type: string

Complete UPS identifier including hostname for network monitoring.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
