---
title: fcport.query
kind: event
source_rst: _sources/api_events_fcport.query.rst.txt
source_html: api_events_fcport.query.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# fcport.query

## Summary

Sent on fcport changes.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

### ADDED

- Schema name: `FCPortAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `FCPortEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel port configuration.

##### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must be at least `1` characters long
- Must be at most `40` characters long

##### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### target (required)

- Schema name: `Target`

Target configuration object or `null` if not configured.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

### CHANGED

- Schema name: `FCPortChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `FCPortEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel port configuration.

##### port (required)

- Schema name: `Port`
- Type: string

Alias name for the Fibre Channel port.
- Must be at least `1` characters long
- Must be at most `40` characters long

##### wwpn (required)

- Schema name: `Wwpn`

World Wide Port Name for port A or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b (required)

- Schema name: `Wwpn B`

World Wide Port Name for port B or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### target (required)

- Schema name: `Target`

Target configuration object or `null` if not configured.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

### REMOVED

- Schema name: `FCPortRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
