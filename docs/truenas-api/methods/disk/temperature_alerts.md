---
title: disk.temperature_alerts
kind: method
source_rst: _sources/api_methods_disk.temperature_alerts.rst.txt
source_html: api_methods_disk.temperature_alerts.html
required_roles:
  - REPORTING_READ
---

# disk.temperature_alerts

## Summary

Returns existing temperature alerts for specified disks.

## Required Roles

- `REPORTING_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: names

#### names

- Schema name: `names`
- Type: array of string

Array of disk names to check for temperature-related alerts.
- No Additional Items

##### Each item of this array must be:

- Type: string

### Return value

- Schema name: `Result`
- Type: array of object

Array of active temperature alerts for the specified disks.
- No Additional Items

#### Each item of this array must be:

#### Alert

- Schema name: `Alert`
- Type: object
- No Additional Properties
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique identifier for the alert.

##### source (required)

- Schema name: `Source`
- Type: string

Source component that generated the alert.

##### klass (required)

- Schema name: `Klass`
- Type: string

Alert class identifier for categorization.

##### args (required)

- Schema name: `Args`
- Type: object

Arguments and parameters specific to the alert type.

##### node (required)

- Schema name: `Node`
- Type: string

Node identifier in HA systems or hostname for single-node systems.

##### key (required)

- Schema name: `Key`
- Type: string

Unique key used for alert deduplication and identification.

##### datetime (required)

- Schema name: `Datetime`
- Type: string
- Type: Format: date-time

Timestamp when the alert was first created.

##### last_occurrence (required)

- Schema name: `Last Occurrence`
- Type: string
- Type: Format: date-time

Timestamp of the most recent occurrence of this alert.

##### dismissed (required)

- Schema name: `Dismissed`
- Type: boolean

Whether the alert has been manually dismissed by a user.

##### mail (required)

- Schema name: `Mail`
- Type: object

Email notification configuration and status for this alert.

##### text (required)

- Schema name: `Text`
- Type: string

Human-readable description of the alert.

##### id (required)

- Schema name: `Id`
- Type: string

Alert identifier used for API operations.

##### level (required)

- Schema name: `Level`
- Type: string

Severity level of the alert (INFO, WARNING, ERROR, etc.).

##### formatted (required)

- Schema name: `Formatted`

Formatted alert message with HTML.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### one_shot (required)

- Schema name: `One Shot`
- Type: boolean

Whether this alert will not be dismissed automatically.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
