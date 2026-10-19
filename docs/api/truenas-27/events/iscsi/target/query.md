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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `iSCSITargetAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `iSCSITargetEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingADDED_fields_alias"></a>
<a id="ADDED_fields_alias"></a>
##### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
<a id="ADDED_fields_alias_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_alias_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_alias_anyOf_i1)

- Type: null

<a id="headingADDED_fields_mode"></a>
<a id="ADDED_fields_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingADDED_fields_groups"></a>
<a id="ADDED_fields_groups"></a>
##### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_groups_items"></a>
###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_groups_items_portal"></a>
<a id="ADDED_fields_groups_items_portal"></a>
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

<a id="headingADDED_fields_groups_items_initiator"></a>
<a id="ADDED_fields_groups_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
<a id="ADDED_fields_groups_items_initiator_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_groups_items_initiator_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_groups_items_initiator_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_groups_items_initiator_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_groups_items_initiator_anyOf_i1)

- Type: null

<a id="headingADDED_fields_groups_items_authmethod"></a>
<a id="ADDED_fields_groups_items_authmethod"></a>
###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingADDED_fields_groups_items_auth"></a>
<a id="ADDED_fields_groups_items_auth"></a>
###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
<a id="ADDED_fields_groups_items_auth_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_groups_items_auth_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_groups_items_auth_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_groups_items_auth_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_groups_items_auth_anyOf_i1)

- Type: null

<a id="headingADDED_fields_auth_networks"></a>
<a id="ADDED_fields_auth_networks"></a>
##### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_auth_networks_items"></a>
- Type: string

<a id="headingADDED_fields_rel_tgt_id"></a>
<a id="ADDED_fields_rel_tgt_id"></a>
##### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingADDED_fields_iscsi_parameters"></a>
<a id="ADDED_fields_iscsi_parameters"></a>
##### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
<a id="ADDED_fields_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_iscsi_parameters_anyOf_i0"></a>
###### [IscsiTargetParameters](#tab-pane_ADDED_fields_iscsi_parameters_anyOf_i0)

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
<a id="ADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
###### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
<a id="ADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 32
- 128

<a id="tab-pane_ADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_iscsi_parameters_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `iSCSITargetChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `iSCSITargetEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingCHANGED_fields_alias"></a>
<a id="CHANGED_fields_alias"></a>
##### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
<a id="CHANGED_fields_alias_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_alias_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_alias_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_mode"></a>
<a id="CHANGED_fields_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingCHANGED_fields_groups"></a>
<a id="CHANGED_fields_groups"></a>
##### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_groups_items"></a>
###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_groups_items_portal"></a>
<a id="CHANGED_fields_groups_items_portal"></a>
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

<a id="headingCHANGED_fields_groups_items_initiator"></a>
<a id="CHANGED_fields_groups_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
<a id="CHANGED_fields_groups_items_initiator_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_groups_items_initiator_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_groups_items_initiator_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_groups_items_initiator_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_groups_items_initiator_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_groups_items_authmethod"></a>
<a id="CHANGED_fields_groups_items_authmethod"></a>
###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingCHANGED_fields_groups_items_auth"></a>
<a id="CHANGED_fields_groups_items_auth"></a>
###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
<a id="CHANGED_fields_groups_items_auth_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_groups_items_auth_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_groups_items_auth_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_groups_items_auth_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_groups_items_auth_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_auth_networks"></a>
<a id="CHANGED_fields_auth_networks"></a>
##### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_auth_networks_items"></a>
- Type: string

<a id="headingCHANGED_fields_rel_tgt_id"></a>
<a id="CHANGED_fields_rel_tgt_id"></a>
##### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingCHANGED_fields_iscsi_parameters"></a>
<a id="CHANGED_fields_iscsi_parameters"></a>
##### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
<a id="CHANGED_fields_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i0"></a>
###### [IscsiTargetParameters](#tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i0)

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
<a id="CHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
###### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
<a id="CHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 32
- 128

<a id="tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_iscsi_parameters_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `iSCSITargetRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
