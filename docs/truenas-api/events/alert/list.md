---
title: alert.list
kind: event
source_rst: _sources/api_events_alert.list.rst.txt
source_html: api_events_alert.list.html
required_roles:
  - ALERT_LIST_READ
---

# alert.list

## Summary

Sent on alert changes.

## Required Roles

- `ALERT_LIST_READ`

## Schema

- Type: object

### ADDED

- Schema name: `AlertListAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Event identifier for the added alert.

#### fields (required)

- Schema name: `Alert`
- Type: object

Complete alert data for the newly added alert.
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

### CHANGED

- Schema name: `AlertListChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Event identifier for the changed alert.

#### fields (required)

- Schema name: `Alert`
- Type: object

Updated alert data with changes.
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

### REMOVED

- Schema name: `AlertListRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Event identifier for the removed alert.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
