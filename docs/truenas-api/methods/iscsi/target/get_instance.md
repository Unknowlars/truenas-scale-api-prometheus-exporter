---
title: iscsi.target.get_instance
kind: method
source_rst: _sources/api_methods_iscsi.target.get_instance.rst.txt
source_html: api_methods_iscsi.target.get_instance.html
required_roles:
  - SHARING_ISCSI_TARGET_READ
---

# iscsi.target.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_ISCSI_TARGET_READ`

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

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `IscsiTargetEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the iSCSI target.

#### name (required)

- Schema name: `Name`
- Type: string

Name of the iSCSI target (maximum 120 characters).
- Must be at least `1` characters long
- Must be at most `120` characters long

#### alias

- Schema name: `Alias`
- Default: null

Optional alias name for the iSCSI target.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "ISCSI"

Protocol mode for the target. `ISCSI`: iSCSI protocol only `FC`: Fibre Channel protocol only `BOTH`: Both iSCSI and Fibre Channel protocols Fibre Channel may only be selected on TrueNAS Enterprise-licensed systems with a suitable Fibre Channel HBA.

#### groups

- Schema name: `Groups`
- Type: array of object
- Default: []

Array of portal-initiator group associations for this target.
- No Additional Items

##### Each item of this array must be:

##### IscsiGroup

- Schema name: `IscsiGroup`
- Type: object
- No Additional Properties
###### portal (required)

- Schema name: `Portal`
- Type: integer

ID of the iSCSI portal to use for this target group.

###### initiator

- Schema name: `Initiator`
- Default: null

ID of the authorized initiator group or `null` to allow any initiator.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### authmethod

- Schema name: `Authmethod`
- Type: enum (of string)
- Default: "NONE"

Authentication method for this target group.

###### auth

- Schema name: `Auth`
- Default: null

ID of the authentication credential or `null` if no authentication.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

#### auth_networks

- Schema name: `Auth Networks`
- Type: array of string
- Default: []

Array of network addresses allowed to access this target.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### rel_tgt_id (required)

- Schema name: `Rel Tgt Id`
- Type: integer

Relative target ID number assigned by the system.

#### iscsi_parameters

- Default: null

Optional iSCSI-specific parameters for this target.
##### Any of

###### IscsiTargetParameters

- Schema name: `IscsiTargetParameters`
- Type: object
- No Additional Properties
####### QueuedCommands

- Schema name: `Queuedcommands`
- Default: null

Maximum number of queued commands per iSCSI session. `32`: Standard queue depth for most use cases `128`: Higher queue depth for performance-critical applications
######## Any of

######### Option 1

- Type: enum (of integer)

######### Option 2

- Type: null

###### Option 2

- Type: enum (of integer)

###### Option 1

- Type: null

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
