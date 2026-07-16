---
title: alertservice.query
kind: event
source_rst: _sources/api_events_alertservice.query.rst.txt
source_html: api_events_alertservice.query.html
required_roles:
  - ALERT_READ
---

# alertservice.query

## Summary

Sent on alertservice changes.

## Required Roles

- `ALERT_READ`

## Schema

- Type: object

### ADDED

- Schema name: `AlertServiceAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `AlertServiceEntry`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

##### attributes (required)

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).

##### level (required)

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the alert service is active and will send notifications.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the alert service.

##### type__title (required)

- Schema name: `Type Title`
- Type: string

Human-readable title for the alert service type.

### CHANGED

- Schema name: `AlertServiceChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `AlertServiceEntry`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

##### attributes (required)

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).

##### level (required)

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the alert service is active and will send notifications.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the alert service.

##### type__title (required)

- Schema name: `Type Title`
- Type: string

Human-readable title for the alert service type.

### REMOVED

- Schema name: `AlertServiceRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
