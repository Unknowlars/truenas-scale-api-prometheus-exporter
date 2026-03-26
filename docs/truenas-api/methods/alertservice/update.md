---
title: alertservice.update
kind: method
source_rst: _sources/api_methods_alertservice.update.rst.txt
source_html: api_methods_alertservice.update.html
required_roles:
  - ALERT_WRITE
---

# alertservice.update

## Summary

Update Alert Service of `id`.

## Required Roles

- `ALERT_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the alert service to update.

#### Parameter 2: alert_service_update

#### alert_service_update

- Schema name: `alert_service_update`
- Type: object

Updated alert service configuration data.
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

The updated alert service configuration.
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
