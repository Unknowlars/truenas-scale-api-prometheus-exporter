---
title: system.ntpserver.query
kind: event
source_rst: _sources/api_events_system.ntpserver.query.rst.txt
source_html: api_events_system.ntpserver.query.html
required_roles:
  - NETWORK_GENERAL_READ
---

# system.ntpserver.query

## Summary

Sent on system.ntpserver changes.

## Required Roles

- `NETWORK_GENERAL_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `NTPServerAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `NTPServerEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NTP server configuration.

<a id="headingADDED_fields_address"></a>
<a id="ADDED_fields_address"></a>
##### address (required)

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

<a id="headingADDED_fields_burst"></a>
<a id="ADDED_fields_burst"></a>
##### burst

- Schema name: `Burst`
- Type: boolean
- Default: false

Send a burst of packets when the server is reachable.

<a id="headingADDED_fields_iburst"></a>
<a id="ADDED_fields_iburst"></a>
##### iburst

- Schema name: `Iburst`
- Type: boolean
- Default: true

Send a burst of packets when the server is unreachable.

<a id="headingADDED_fields_prefer"></a>
<a id="ADDED_fields_prefer"></a>
##### prefer

- Schema name: `Prefer`
- Type: boolean
- Default: false

Mark this server as preferred for time synchronization.

<a id="headingADDED_fields_minpoll"></a>
<a id="ADDED_fields_minpoll"></a>
##### minpoll

- Schema name: `Minpoll`
- Type: integer
- Default: 6

Minimum polling interval (log2 seconds).

<a id="headingADDED_fields_maxpoll"></a>
<a id="ADDED_fields_maxpoll"></a>
##### maxpoll

- Schema name: `Maxpoll`
- Type: integer
- Default: 10

Maximum polling interval (log2 seconds).

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `NTPServerChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `NTPServerEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NTP server configuration.

<a id="headingCHANGED_fields_address"></a>
<a id="CHANGED_fields_address"></a>
##### address (required)

- Schema name: `Address`
- Type: string

Hostname or IP address of the NTP server.

<a id="headingCHANGED_fields_burst"></a>
<a id="CHANGED_fields_burst"></a>
##### burst

- Schema name: `Burst`
- Type: boolean
- Default: false

Send a burst of packets when the server is reachable.

<a id="headingCHANGED_fields_iburst"></a>
<a id="CHANGED_fields_iburst"></a>
##### iburst

- Schema name: `Iburst`
- Type: boolean
- Default: true

Send a burst of packets when the server is unreachable.

<a id="headingCHANGED_fields_prefer"></a>
<a id="CHANGED_fields_prefer"></a>
##### prefer

- Schema name: `Prefer`
- Type: boolean
- Default: false

Mark this server as preferred for time synchronization.

<a id="headingCHANGED_fields_minpoll"></a>
<a id="CHANGED_fields_minpoll"></a>
##### minpoll

- Schema name: `Minpoll`
- Type: integer
- Default: 6

Minimum polling interval (log2 seconds).

<a id="headingCHANGED_fields_maxpoll"></a>
<a id="CHANGED_fields_maxpoll"></a>
##### maxpoll

- Schema name: `Maxpoll`
- Type: integer
- Default: 10

Maximum polling interval (log2 seconds).

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `NTPServerRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
