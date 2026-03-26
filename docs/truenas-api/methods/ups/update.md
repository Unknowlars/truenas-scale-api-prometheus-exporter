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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: ups_update

#### ups_update

- Schema name: `ups_update`
- Type: object

UPSUpdateArgs parameters.
- No Additional Properties
##### powerdown

- Schema name: `Powerdown`
- Type: boolean

Whether the UPS should power down after completing the shutdown sequence.

##### rmonitor

- Schema name: `Rmonitor`
- Type: boolean

Whether to enable remote monitoring of the UPS status over the network.

##### nocommwarntime

- Schema name: `Nocommwarntime`

Seconds to wait before warning about communication loss with UPS. `null` for default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### remoteport

- Schema name: `Remoteport`
- Type: integer

Network port for communicating with remote UPS monitoring systems.
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### shutdowntimer

- Schema name: `Shutdowntimer`
- Type: integer

Seconds to wait after initiating shutdown before forcing power off.

##### hostsync

- Schema name: `Hostsync`
- Type: integer

Maximum seconds to wait for other systems to shutdown before continuing.
- Value must be greater or equal to `0`

##### description

- Schema name: `Description`
- Type: string

Human-readable description of this UPS configuration.

##### driver

- Schema name: `Driver`
- Type: string

UPS driver name that handles communication with the specific UPS hardware model.

##### extrausers

- Schema name: `Extrausers`
- Type: string

Additional user configurations for UPS monitoring access.

##### identifier

- Schema name: `Identifier`
- Type: string

Unique identifier name for this UPS device within the monitoring system.
- Must be at least `1` characters long

##### mode

- Schema name: `Mode`
- Type: enum (of string)

Operating mode. * `MASTER` controls the UPS directly * `SLAVE` monitors remotely

##### monpwd

- Schema name: `Monpwd`
- Type: string

Password for UPS monitoring authentication (required for updates).
- Must be at least `1` characters long

##### monuser

- Schema name: `Monuser`
- Type: string

Username for UPS monitoring authentication.
- Must be at least `1` characters long

##### options

- Schema name: `Options`
- Type: string

Additional configuration options passed to the UPS driver.

##### optionsupsd

- Schema name: `Optionsupsd`
- Type: string

Additional configuration options for the UPS daemon.

##### port

- Schema name: `Port`
- Type: string

Serial port or device path for UPS communication.

##### remotehost

- Schema name: `Remotehost`
- Type: string

Hostname or IP address of remote UPS server when operating in SLAVE mode.

##### shutdown

- Schema name: `Shutdown`
- Type: enum (of string)

Shutdown trigger condition: LOWBATT on low battery, BATT when on battery power.

##### shutdowncmd

- Schema name: `Shutdowncmd`

Custom command to execute during UPS shutdown sequence. `null` for default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `UPSEntry`
- Type: object

The updated UPS configuration.
- No Additional Properties
#### powerdown (required)

- Schema name: `Powerdown`
- Type: boolean

Whether the UPS should power down after completing the shutdown sequence.

#### rmonitor (required)

- Schema name: `Rmonitor`
- Type: boolean

Whether to enable remote monitoring of the UPS status over the network.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the UPS configuration.

#### nocommwarntime (required)

- Schema name: `Nocommwarntime`

Seconds to wait before warning about communication loss with UPS. `null` for default.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### remoteport (required)

- Schema name: `Remoteport`
- Type: integer

Network port for communicating with remote UPS monitoring systems.
- Value must be greater or equal to `1` and lesser or equal to `65535`

#### shutdowntimer (required)

- Schema name: `Shutdowntimer`
- Type: integer

Seconds to wait after initiating shutdown before forcing power off.

#### hostsync (required)

- Schema name: `Hostsync`
- Type: integer

Maximum seconds to wait for other systems to shutdown before continuing.
- Value must be greater or equal to `0`

#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of this UPS configuration.

#### driver (required)

- Schema name: `Driver`
- Type: string

UPS driver name that handles communication with the specific UPS hardware model.

#### extrausers (required)

- Schema name: `Extrausers`
- Type: string

Additional user configurations for UPS monitoring access.

#### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier name for this UPS device within the monitoring system.
- Must be at least `1` characters long

#### mode (required)

- Schema name: `Mode`
- Type: enum (of string)

Operating mode. * `MASTER` controls the UPS directly * `SLAVE` monitors remotely

#### monpwd (required)

- Schema name: `Monpwd`
- Type: string

Password for UPS monitoring authentication.

#### monuser (required)

- Schema name: `Monuser`
- Type: string

Username for UPS monitoring authentication.
- Must be at least `1` characters long

#### options (required)

- Schema name: `Options`
- Type: string

Additional configuration options passed to the UPS driver.

#### optionsupsd (required)

- Schema name: `Optionsupsd`
- Type: string

Additional configuration options for the UPS daemon.

#### port (required)

- Schema name: `Port`
- Type: string

Serial port or device path for UPS communication.

#### remotehost (required)

- Schema name: `Remotehost`
- Type: string

Hostname or IP address of remote UPS server when operating in SLAVE mode.

#### shutdown (required)

- Schema name: `Shutdown`
- Type: enum (of string)

Shutdown trigger condition: LOWBATT on low battery, BATT when on battery power.

#### shutdowncmd (required)

- Schema name: `Shutdowncmd`

Custom command to execute during UPS shutdown sequence. `null` for default.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### complete_identifier (required)

- Schema name: `Complete Identifier`
- Type: string

Complete UPS identifier including hostname for network monitoring.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
