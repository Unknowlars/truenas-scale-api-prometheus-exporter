---
title: iscsi.target.query
kind: method
source_rst: _sources/api_methods_iscsi.target.query.rst.txt
source_html: api_methods_iscsi.target.query.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# iscsi.target.query

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### iSCSITargetEntry

- Schema name: `iSCSITargetEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingReturn_value_anyOf_i0_items_name"></a>
<a id="Return_value_anyOf_i0_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingReturn_value_anyOf_i0_items_alias"></a>
<a id="Return_value_anyOf_i0_items_alias"></a>
###### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
<a id="Return_value_anyOf_i0_items_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_mode"></a>
<a id="Return_value_anyOf_i0_items_mode"></a>
###### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingReturn_value_anyOf_i0_items_groups"></a>
<a id="Return_value_anyOf_i0_items_groups"></a>
###### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_groups_items"></a>
###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_groups_items_portal"></a>
<a id="Return_value_anyOf_i0_items_groups_items_portal"></a>
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

<a id="headingReturn_value_anyOf_i0_items_groups_items_initiator"></a>
<a id="Return_value_anyOf_i0_items_groups_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
<a id="Return_value_anyOf_i0_items_groups_items_initiator_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_groups_items_initiator_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_groups_items_initiator_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_groups_items_initiator_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_groups_items_initiator_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_groups_items_authmethod"></a>
<a id="Return_value_anyOf_i0_items_groups_items_authmethod"></a>
###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingReturn_value_anyOf_i0_items_groups_items_auth"></a>
<a id="Return_value_anyOf_i0_items_groups_items_auth"></a>
###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
<a id="Return_value_anyOf_i0_items_groups_items_auth_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_groups_items_auth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_groups_items_auth_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_groups_items_auth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_groups_items_auth_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_auth_networks"></a>
<a id="Return_value_anyOf_i0_items_auth_networks"></a>
###### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_auth_networks_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_rel_tgt_id"></a>
<a id="Return_value_anyOf_i0_items_rel_tgt_id"></a>
###### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingReturn_value_anyOf_i0_items_iscsi_parameters"></a>
<a id="Return_value_anyOf_i0_items_iscsi_parameters"></a>
###### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
<a id="Return_value_anyOf_i0_items_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0"></a>
###### [IscsiTargetParameters](#tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0)

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
<a id="Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
###### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
<a id="Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 32
- 128

<a id="tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_iscsi_parameters_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [iSCSITargetEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `iSCSITargetEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingReturn_value_anyOf_i1_name"></a>
<a id="Return_value_anyOf_i1_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingReturn_value_anyOf_i1_alias"></a>
<a id="Return_value_anyOf_i1_alias"></a>
###### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
<a id="Return_value_anyOf_i1_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_mode"></a>
<a id="Return_value_anyOf_i1_mode"></a>
###### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingReturn_value_anyOf_i1_groups"></a>
<a id="Return_value_anyOf_i1_groups"></a>
###### groups

- Schema name: `Groups`
- Type: array
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_groups_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_auth_networks"></a>
<a id="Return_value_anyOf_i1_auth_networks"></a>
###### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_auth_networks_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_rel_tgt_id"></a>
<a id="Return_value_anyOf_i1_rel_tgt_id"></a>
###### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingReturn_value_anyOf_i1_iscsi_parameters"></a>
<a id="Return_value_anyOf_i1_iscsi_parameters"></a>
###### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
<a id="Return_value_anyOf_i1_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_iscsi_parameters_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_iscsi_parameters_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_iscsi_parameters_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### iSCSITargetQueryResultItem

- Schema name: `iSCSITargetQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingReturn_value_anyOf_i2_items_name"></a>
<a id="Return_value_anyOf_i2_items_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingReturn_value_anyOf_i2_items_alias"></a>
<a id="Return_value_anyOf_i2_items_alias"></a>
###### alias

- Schema name: `Alias`

Optional alias name for the iSCSI target.
<a id="Return_value_anyOf_i2_items_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_mode"></a>
<a id="Return_value_anyOf_i2_items_mode"></a>
###### mode

- Schema name: `Mode`
- Type: enum (of string)

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingReturn_value_anyOf_i2_items_groups"></a>
<a id="Return_value_anyOf_i2_items_groups"></a>
###### groups

- Schema name: `Groups`
- Type: array of object

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_groups_items"></a>
###### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_groups_items_portal"></a>
<a id="Return_value_anyOf_i2_items_groups_items_portal"></a>
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

<a id="headingReturn_value_anyOf_i2_items_groups_items_initiator"></a>
<a id="Return_value_anyOf_i2_items_groups_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
<a id="Return_value_anyOf_i2_items_groups_items_initiator_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_groups_items_initiator_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_groups_items_initiator_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_groups_items_initiator_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_groups_items_initiator_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_groups_items_authmethod"></a>
<a id="Return_value_anyOf_i2_items_groups_items_authmethod"></a>
###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.
###### Must be one of:

- "NONE"
- "CHAP"
- "CHAP_MUTUAL"

<a id="headingReturn_value_anyOf_i2_items_groups_items_auth"></a>
<a id="Return_value_anyOf_i2_items_groups_items_auth"></a>
###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
<a id="Return_value_anyOf_i2_items_groups_items_auth_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_groups_items_auth_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_groups_items_auth_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_groups_items_auth_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_groups_items_auth_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_auth_networks"></a>
<a id="Return_value_anyOf_i2_items_auth_networks"></a>
###### auth_networks

- Schema name: `Auth Networks`
- Type: array of string

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_auth_networks_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i2_items_rel_tgt_id"></a>
<a id="Return_value_anyOf_i2_items_rel_tgt_id"></a>
###### rel_tgt_id

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingReturn_value_anyOf_i2_items_iscsi_parameters"></a>
<a id="Return_value_anyOf_i2_items_iscsi_parameters"></a>
###### iscsi_parameters

Optional iSCSI-specific parameters for this target.
<a id="Return_value_anyOf_i2_items_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0"></a>
###### [IscsiTargetParameters](#tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0)

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
<a id="Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands"></a>
###### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
<a id="Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i0)

- Type: enum (of integer)
###### Must be one of:

- 32
- 128

<a id="tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i0_QueuedCommands_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_iscsi_parameters_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [iSCSITargetQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `iSCSITargetQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

<a id="headingReturn_value_anyOf_i3_name"></a>
<a id="Return_value_anyOf_i3_name"></a>
###### name

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

<a id="headingReturn_value_anyOf_i3_alias"></a>
<a id="Return_value_anyOf_i3_alias"></a>
###### alias

- Schema name: `Alias`

Optional alias name for the iSCSI target.
<a id="Return_value_anyOf_i3_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_mode"></a>
<a id="Return_value_anyOf_i3_mode"></a>
###### mode

- Schema name: `Mode`
- Type: enum (of string)

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.
###### Must be one of:

- "ISCSI"
- "FC"
- "BOTH"

<a id="headingReturn_value_anyOf_i3_groups"></a>
<a id="Return_value_anyOf_i3_groups"></a>
###### groups

- Schema name: `Groups`
- Type: array

Array of portal-initiator group associations for this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_groups_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i3_auth_networks"></a>
<a id="Return_value_anyOf_i3_auth_networks"></a>
###### auth_networks

- Schema name: `Auth Networks`
- Type: array of string

Array of network addresses allowed to access this target.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_auth_networks_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i3_rel_tgt_id"></a>
<a id="Return_value_anyOf_i3_rel_tgt_id"></a>
###### rel_tgt_id

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

<a id="headingReturn_value_anyOf_i3_iscsi_parameters"></a>
<a id="Return_value_anyOf_i3_iscsi_parameters"></a>
###### iscsi_parameters

Optional iSCSI-specific parameters for this target.
<a id="Return_value_anyOf_i3_iscsi_parameters_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_iscsi_parameters_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_iscsi_parameters_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i3_iscsi_parameters_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_iscsi_parameters_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
