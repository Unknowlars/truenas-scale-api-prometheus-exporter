---
title: system.ntpserver.create
kind: method
source_rst: _sources/api_methods_system.ntpserver.create.rst.txt
source_html: api_methods_system.ntpserver.create.html
required_roles:
  - NETWORK_GENERAL_WRITE
---

# system.ntpserver.create

## Summary

Add an NTP Server.

`address` specifies the hostname/IP address of the NTP server.

`burst` when enabled makes sure that if server is reachable, sends a burst of eight packets instead of one. This is designed to improve timekeeping quality with the server command.

`iburst` when enabled speeds up the initial synchronization, taking seconds rather than minutes.

`prefer` marks the specified server as preferred. When all other things are equal, this host is chosen for synchronization acquisition with the server command. It is recommended that they be used for servers with time monitoring hardware.

`minpoll` is minimum polling time in seconds. It must be a power of 2 and less than `maxpoll`.

`maxpoll` is maximum polling time in seconds. It must be a power of 2 and greater than `minpoll`.

`force` when enabled forces the addition of NTP server even if it is currently unreachable.

## Required Roles

- `NETWORK_GENERAL_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: ntp_server_create

<a id="Call_parameters_items_i0"></a>
#### ntp_server_create

- Schema name: `ntp_server_create`
- Type: object

Configuration for creating a new NTP server.
- No Additional Properties
<a id="headingCall_parameters_items_i0_address"></a>
<a id="Call_parameters_items_i0_address"></a>
##### address (required)

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

<a id="headingCall_parameters_items_i0_burst"></a>
<a id="Call_parameters_items_i0_burst"></a>
##### burst

- Schema name: `Burst`
- Type: boolean
- Default: false

Send a burst of packets when the server is reachable.

<a id="headingCall_parameters_items_i0_iburst"></a>
<a id="Call_parameters_items_i0_iburst"></a>
##### iburst

- Schema name: `Iburst`
- Type: boolean
- Default: true

Send a burst of packets when the server is unreachable.

<a id="headingCall_parameters_items_i0_prefer"></a>
<a id="Call_parameters_items_i0_prefer"></a>
##### prefer

- Schema name: `Prefer`
- Type: boolean
- Default: false

Mark this server as preferred for time synchronization.

<a id="headingCall_parameters_items_i0_minpoll"></a>
<a id="Call_parameters_items_i0_minpoll"></a>
##### minpoll

- Schema name: `Minpoll`
- Type: integer
- Default: 6

Minimum polling interval (log2 seconds).

<a id="headingCall_parameters_items_i0_maxpoll"></a>
<a id="Call_parameters_items_i0_maxpoll"></a>
##### maxpoll

- Schema name: `Maxpoll`
- Type: integer
- Default: 10

Maximum polling interval (log2 seconds).

<a id="headingCall_parameters_items_i0_force"></a>
<a id="Call_parameters_items_i0_force"></a>
##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force creation even if the server is unreachable.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NTPServerEntry`
- Type: object

The newly created NTP server configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NTP server configuration.

<a id="headingReturn_value_address"></a>
<a id="Return_value_address"></a>
#### address (required)

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

<a id="headingReturn_value_burst"></a>
<a id="Return_value_burst"></a>
#### burst

- Schema name: `Burst`
- Type: boolean
- Default: false

Send a burst of packets when the server is reachable.

<a id="headingReturn_value_iburst"></a>
<a id="Return_value_iburst"></a>
#### iburst

- Schema name: `Iburst`
- Type: boolean
- Default: true

Send a burst of packets when the server is unreachable.

<a id="headingReturn_value_prefer"></a>
<a id="Return_value_prefer"></a>
#### prefer

- Schema name: `Prefer`
- Type: boolean
- Default: false

Mark this server as preferred for time synchronization.

<a id="headingReturn_value_minpoll"></a>
<a id="Return_value_minpoll"></a>
#### minpoll

- Schema name: `Minpoll`
- Type: integer
- Default: 6

Minimum polling interval (log2 seconds).

<a id="headingReturn_value_maxpoll"></a>
<a id="Return_value_maxpoll"></a>
#### maxpoll

- Schema name: `Maxpoll`
- Type: integer
- Default: 10

Maximum polling interval (log2 seconds).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
