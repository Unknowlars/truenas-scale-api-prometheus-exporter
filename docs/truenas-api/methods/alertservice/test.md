---
title: alertservice.test
kind: method
source_rst: _sources/api_methods_alertservice.test.rst.txt
source_html: api_methods_alertservice.test.html
required_roles:
  - ALERT_WRITE
---

# alertservice.test

## Summary

Send a test alert using `type` of Alert Service.

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

Alert service configuration to test for connectivity and functionality.
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

- Schema name: `Result`
- Type: boolean

Returns `true` if the alert service test was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
