---
title: iscsi.target.query
kind: event
source_rst: _sources/api_events_iscsi.target.query.rst.txt
source_html: api_events_iscsi.target.query.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# iscsi.target.query

## Summary

Sent on iscsi.target changes.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

### ADDED

- Schema name: `IscsiTargetAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiTargetEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

##### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.

##### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
####### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

####### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.

####### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

##### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

##### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
###### Any of

####### IscsiTargetParameters

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
######## QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
######### Any of

########## Option 1

- Type: enum (of integer)

########## Option 2

- Type: null

####### Option 2

- Type: enum (of integer)

####### Option 1

- Type: null

####### Option 2

- Type: null

### CHANGED

- Schema name: `IscsiTargetChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `IscsiTargetEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

##### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.

##### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
####### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

####### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.

####### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

##### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

##### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
###### Any of

####### IscsiTargetParameters

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
######## QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
######### Any of

########## Option 1

- Type: enum (of integer)

########## Option 2

- Type: null

####### Option 2

- Type: enum (of integer)

####### Option 1

- Type: null

####### Option 2

- Type: null

### REMOVED

- Schema name: `IscsiTargetRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
