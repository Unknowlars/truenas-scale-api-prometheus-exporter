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

## Required Roles

- `NETWORK_GENERAL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: ntp_server_create

#### ntp_server_create

- Schema name: `ntp_server_create`
- Type: object

Configuration for creating a new NTP server.
- No Additional Properties
##### address (required)

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

##### burst

- Schema name: `Burst`
- Type: boolean
- Default: false

Send a burst of packets when the server is reachable.

##### iburst

- Schema name: `Iburst`
- Type: boolean
- Default: true

Send a burst of packets when the server is unreachable.

##### prefer

- Schema name: `Prefer`
- Type: boolean
- Default: false

Mark this server as preferred for time synchronization.

##### minpoll

- Schema name: `Minpoll`
- Type: integer
- Default: 6

Minimum polling interval (log2 seconds).

##### maxpoll

- Schema name: `Maxpoll`
- Type: integer
- Default: 10

Maximum polling interval (log2 seconds).

##### force

- Schema name: `Force`
- Type: boolean
- Default: false

Force creation even if the server is unreachable.

### Return value

- Schema name: `NTPServerEntry`
- Type: object

The newly created NTP server configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NTP server configuration.

#### address (required)

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

#### burst

- Schema name: `Burst`
- Type: boolean
- Default: false

Send a burst of packets when the server is reachable.

#### iburst

- Schema name: `Iburst`
- Type: boolean
- Default: true

Send a burst of packets when the server is unreachable.

#### prefer

- Schema name: `Prefer`
- Type: boolean
- Default: false

Mark this server as preferred for time synchronization.

#### minpoll

- Schema name: `Minpoll`
- Type: integer
- Default: 6

Minimum polling interval (log2 seconds).

#### maxpoll

- Schema name: `Maxpoll`
- Type: integer
- Default: 10

Maximum polling interval (log2 seconds).

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
