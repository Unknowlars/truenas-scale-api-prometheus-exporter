---
title: fc.fc_host.query
kind: event
source_rst: _sources/api_events_fc.fc_host.query.rst.txt
source_html: api_events_fc.fc_host.query.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# fc.fc_host.query

## Summary

Sent on fc.fc_host changes.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

### ADDED

- Schema name: `FCHostAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `FCHostEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel host configuration.

##### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must be at least `1` characters long
- Must be at most `32` characters long

##### wwpn

- Schema name: `Wwpn`
- Default: null

World Wide Port Name for port A or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b

- Schema name: `Wwpn B`
- Default: null

World Wide Port Name for port B or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

### CHANGED

- Schema name: `FCHostChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `FCHostEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Fibre Channel host configuration.

##### alias (required)

- Schema name: `Alias`
- Type: string

Human-readable alias for the Fibre Channel host.
- Must be at least `1` characters long
- Must be at most `32` characters long

##### wwpn

- Schema name: `Wwpn`
- Default: null

World Wide Port Name for port A or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### wwpn_b

- Schema name: `Wwpn B`
- Default: null

World Wide Port Name for port B or `null` if not configured.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### npiv

- Schema name: `Npiv`
- Type: integer
- Default: 0

Number of N_Port ID Virtualization (NPIV) virtual ports to create.

### REMOVED

- Schema name: `FCHostRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
