---
title: system.ntpserver.update
kind: method
source_rst: _sources/api_methods_system.ntpserver.update.rst.txt
source_html: api_methods_system.ntpserver.update.html
required_roles:
  - NETWORK_GENERAL_WRITE
---

# system.ntpserver.update

## Summary

Update NTP server of `id`.

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

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the NTP server to update.

#### Parameter 2: ntp_server_update

<a id="Call_parameters_items_i1"></a>
#### ntp_server_update

- Schema name: `ntp_server_update`
- Type: object

Updated configuration for the NTP server.
- No Additional Properties
<a id="headingCall_parameters_items_i1_address"></a>
<a id="Call_parameters_items_i1_address"></a>
##### address

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

<a id="headingCall_parameters_items_i1_burst"></a>
<a id="Call_parameters_items_i1_burst"></a>
##### burst

- Schema name: `Burst`
- Type: boolean

Send a burst of packets when the server is reachable.

<a id="headingCall_parameters_items_i1_iburst"></a>
<a id="Call_parameters_items_i1_iburst"></a>
##### iburst

- Schema name: `Iburst`
- Type: boolean

Send a burst of packets when the server is unreachable.

<a id="headingCall_parameters_items_i1_prefer"></a>
<a id="Call_parameters_items_i1_prefer"></a>
##### prefer

- Schema name: `Prefer`
- Type: boolean

Mark this server as preferred for time synchronization.

<a id="headingCall_parameters_items_i1_minpoll"></a>
<a id="Call_parameters_items_i1_minpoll"></a>
##### minpoll

- Schema name: `Minpoll`
- Type: integer

Minimum polling interval (log2 seconds).

<a id="headingCall_parameters_items_i1_maxpoll"></a>
<a id="Call_parameters_items_i1_maxpoll"></a>
##### maxpoll

- Schema name: `Maxpoll`
- Type: integer

Maximum polling interval (log2 seconds).

<a id="headingCall_parameters_items_i1_force"></a>
<a id="Call_parameters_items_i1_force"></a>
##### force

- Schema name: `Force`
- Type: boolean

Force creation even if the server is unreachable.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NTPServerEntry`
- Type: object

The updated NTP server configuration.
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
