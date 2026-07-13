---
title: alertservice.create
kind: method
source_rst: _sources/api_methods_alertservice.create.rst.txt
source_html: api_methods_alertservice.create.html
required_roles:
  - ALERT_WRITE
---

# alertservice.create

## Summary

Create an Alert Service of specified `type`.

If `enabled`, it sends alerts to the configured `type` of Alert Service.

## Required Roles

- `ALERT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: alert_service_create

#### alert_service_create

- Schema name: `alert_service_create`
- Type: object

Alert service configuration data for the new service.
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

### Return value

- Schema name: `AlertServiceEntry`
- Type: object

The created alert service configuration.
- No Additional Properties
#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the alert service.
- Must be at least `1` characters long

#### attributes (required)

- Schema name: `Attributes`

Service-specific configuration attributes (credentials, endpoints, etc.).

#### level (required)

- Schema name: `Level`
- Type: enum (of string)

Minimum alert severity level that triggers notifications through this service.

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the alert service is active and will send notifications.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the alert service.

#### type__title (required)

- Schema name: `Type Title`
- Type: string

Human-readable title for the alert service type.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
