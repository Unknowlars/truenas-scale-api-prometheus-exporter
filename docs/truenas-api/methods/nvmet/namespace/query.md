---
title: nvmet.namespace.query
kind: method
source_rst: _sources/api_methods_nvmet.namespace.query.rst.txt
source_html: api_methods_nvmet.namespace.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.namespace.query

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

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
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

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

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### NVMetNamespaceQueryResultItem

- Schema name: `NVMetNamespaceQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

####### nsid

- Schema name: `Nsid`

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
######## Any of

######### Option 1

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

######### Option 2

- Type: null

####### subsys

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that contains this namespace.
- No Additional Properties
######## id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

######## name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

######## subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

######## allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

######## pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
######### Any of

########## Option 1

- Type: boolean

########## Option 2

- Type: null

######## qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
######### Any of

########## Option 1

- Type: boolean

########## Option 2

- Type: null

######## hosts

- Schema name: `Hosts`
- Default: []

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
######### Any of

########## Option 1

- Type: array of integer
- No Additional Items

########### Each item of this array must be:

- Type: integer

########## Option 2

- Type: null

######## namespaces

- Schema name: `Namespaces`
- Default: []

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
######### Any of

########## Option 1

- Type: array of integer
- No Additional Items

########### Each item of this array must be:

- Type: integer

########## Option 2

- Type: null

######## ports

- Schema name: `Ports`
- Default: []

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
######### Any of

########## Option 1

- Type: array of integer
- No Additional Items

########### Each item of this array must be:

- Type: integer

########## Option 2

- Type: null

####### device_type

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.

####### device_path

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

####### filesize

- Schema name: `Filesize`

When `device_type` is "FILE" then this will be the size of the file in bytes.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### device_uuid

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

####### device_nguid

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

####### enabled

- Schema name: `Enabled`
- Type: boolean

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

####### locked

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
######## Any of

######### Option 1

- Type: boolean

######### Option 2

- Type: null

##### NVMetNamespaceQueryResultItem

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

##### Option 3

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: boolean

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: boolean

##### Option 2

- Type: null

##### Option 1

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: boolean

##### Option 2

- Type: null

##### Option 1

- Schema name: `NVMetNamespaceQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

###### nsid

- Schema name: `Nsid`

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

######## Option 2

- Type: null

###### subsys

- Type: object

NVMe-oF subsystem that contains this namespace.

###### device_type

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.

###### device_path

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

###### filesize

- Schema name: `Filesize`

When `device_type` is "FILE" then this will be the size of the file in bytes.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### device_uuid

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

###### device_nguid

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

###### enabled

- Schema name: `Enabled`
- Type: boolean

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

###### locked

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: boolean

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
