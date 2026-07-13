---
title: tn_connect.config
kind: event
source_rst: _sources/api_events_tn_connect.config.rst.txt
source_html: api_events_tn_connect.config.html
required_roles:
  - TRUENAS_CONNECT_READ
---

# tn_connect.config

## Summary

Sent on TrueNAS Connect configuration changes

## Required Roles

- `TRUENAS_CONNECT_READ`

## Schema

- Type: object

### CHANGED

- Schema name: `TrueNASConnectConfigChangedEvent`
- Type: object
- No Additional Properties
#### fields (required)

- Schema name: `TrueNASConnectEntry`
- Type: object

Event data.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the TrueNAS Connect configuration.

##### enabled (required)

- Schema name: `Enabled`
- Type: boolean

Whether TrueNAS Connect service is enabled.

##### registration_details (required)

- Schema name: `Registration Details`
- Type: object

Object containing registration information and credentials for TrueNAS Connect.

##### status (required)

- Schema name: `Status`
- Type: string

Current operational status of the TrueNAS Connect service.
- Must be at least `1` characters long

##### status_reason (required)

- Schema name: `Status Reason`
- Type: string

Detailed explanation of the current status, including any error conditions.
- Must be at least `1` characters long

##### certificate (required)

- Schema name: `Certificate`

ID of the SSL certificate used for TrueNAS Connect communications. `null` if using default.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### account_service_base_url (required)

- Schema name: `Account Service Base Url`
- Type: string
- Type: Format: uri

Base URL for the TrueNAS Connect account service API.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### leca_service_base_url (required)

- Schema name: `Leca Service Base Url`
- Type: string
- Type: Format: uri

Base URL for the Let's Encrypt Certificate Authority service used by TrueNAS Connect.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### tnc_base_url (required)

- Schema name: `Tnc Base Url`
- Type: string
- Type: Format: uri

Base URL for the TrueNAS Connect service.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### heartbeat_url (required)

- Schema name: `Heartbeat Url`
- Type: string
- Type: Format: uri

URL endpoint for sending heartbeat signals to maintain connection status.
- Must be at least `1` characters long
- Must be at most `2083` characters long

##### tier (required)

- Schema name: `Tier`

TrueNAS Connect tier.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### last_heartbeat_failure_datetime (required)

- Schema name: `Last Heartbeat Failure Datetime`

Datetime of when the current heartbeat failure streak began. Null if heartbeat is not currently failing.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
