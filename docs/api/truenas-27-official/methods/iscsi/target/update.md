---
title: iscsi.target.update
kind: method
source_rst: _sources/api_methods_iscsi.target.update.rst.txt
source_html: api_methods_iscsi.target.update.html
required_roles:
  - SHARING_ISCSI_TARGET_WRITE
---

# iscsi.target.update

## Summary

Update iSCSI Target of `id`.

## Required Roles

- `SHARING_ISCSI_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the iSCSI target to update.

#### Parameter 2: iscsi_target_update

<a id="Call_parameters_items_i1"></a>
#### iscsi_target_update

- Schema name: `iscsi_target_update`
- Type: object

Updated iSCSI target configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_name"></a>
<a id="Call_parameters_items_i1_name"></a>
##### name

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingCall_parameters_items_i1_alias"></a>
<a id="Call_parameters_items_i1_alias"></a>
##### alias

- Schema name: `Alias`

Optional alias name for the iSCSI target.
<a id="Call_parameters_items_i1_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_alias_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_mode"></a>
<a id="Call_parameters_items_i1_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingCall_parameters_items_i1_groups"></a>
<a id="Call_parameters_items_i1_groups"></a>
##### groups

- Schema name: `Groups`
- Type: array of object

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_groups_items"></a>
###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_groups_items_portal"></a>
<a id="Call_parameters_items_i1_groups_items_portal"></a>
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

<a id="headingCall_parameters_items_i1_groups_items_initiator"></a>
<a id="Call_parameters_items_i1_groups_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
<a id="Call_parameters_items_i1_groups_items_initiator_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_groups_items_initiator_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_groups_items_initiator_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_groups_items_initiator_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_groups_items_initiator_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_groups_items_authmethod"></a>
<a id="Call_parameters_items_i1_groups_items_authmethod"></a>
###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingCall_parameters_items_i1_groups_items_auth"></a>
<a id="Call_parameters_items_i1_groups_items_auth"></a>
###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
<a id="Call_parameters_items_i1_groups_items_auth_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_groups_items_auth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_groups_items_auth_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_groups_items_auth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_groups_items_auth_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_auth_networks"></a>
<a id="Call_parameters_items_i1_auth_networks"></a>
##### auth_networks

- Schema name: `Auth Networks`
- Type: array of string

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_auth_networks_items"></a>
- Type: string

<a id="headingCall_parameters_items_i1_iscsi_parameters"></a>
<a id="Call_parameters_items_i1_iscsi_parameters"></a>
##### iscsi_parameters

Optional iSCSI-specific parameters for this target.
<a id="Call_parameters_items_i1_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i0"></a>
###### [IscsiTargetParameters](#tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i0)

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
<a id="Call_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
###### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
<a id="Call_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 32
- 128

<a id="tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1)

- Type: null

<a id="tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_iscsi_parameters_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `iSCSITargetEntry`
- Type: object

The updated iSCSI target configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingReturn_value_alias"></a>
<a id="Return_value_alias"></a>
#### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
<a id="Return_value_alias_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_mode"></a>
<a id="Return_value_mode"></a>
#### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
##### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingReturn_value_groups"></a>
<a id="Return_value_groups"></a>
#### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_groups_items"></a>
##### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
<a id="headingReturn_value_groups_items_portal"></a>
<a id="Return_value_groups_items_portal"></a>
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

<a id="headingReturn_value_groups_items_initiator"></a>
<a id="Return_value_groups_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
<a id="Return_value_groups_items_initiator_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_groups_items_initiator_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_groups_items_initiator_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_groups_items_initiator_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_groups_items_initiator_anyOf_i1)

- Type: null

<a id="headingReturn_value_groups_items_authmethod"></a>
<a id="Return_value_groups_items_authmethod"></a>
###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingReturn_value_groups_items_auth"></a>
<a id="Return_value_groups_items_auth"></a>
###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
<a id="Return_value_groups_items_auth_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_groups_items_auth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_groups_items_auth_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_groups_items_auth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_groups_items_auth_anyOf_i1)

- Type: null

<a id="headingReturn_value_auth_networks"></a>
<a id="Return_value_auth_networks"></a>
#### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_auth_networks_items"></a>
- Type: string

<a id="headingReturn_value_rel_tgt_id"></a>
<a id="Return_value_rel_tgt_id"></a>
#### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingReturn_value_iscsi_parameters"></a>
<a id="Return_value_iscsi_parameters"></a>
#### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
<a id="Return_value_iscsi_parameters_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_iscsi_parameters_anyOf_i0"></a>
###### [IscsiTargetParameters](#tab-pane_Return_value_iscsi_parameters_anyOf_i0)

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
<a id="headingReturn_value_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
<a id="Return_value_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
###### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
<a id="Return_value_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 32
- 128

<a id="tab-pane_Return_value_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_iscsi_parameters_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
