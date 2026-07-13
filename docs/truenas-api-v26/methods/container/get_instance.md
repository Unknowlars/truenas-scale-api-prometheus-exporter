---
title: container.get_instance
kind: method
source_rst: _sources/api_methods_container.get_instance.rst.txt
source_html: api_methods_container.get_instance.html
required_roles:
  - CONTAINER_READ
---

# container.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `CONTAINER_READ`

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
- Value must be greater or equal to `0`

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `ContainerEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Container ID.

#### uuid (required)

- Schema name: `Uuid`
- Type: string

Container UUID (for libvirt).

#### name (required)

- Schema name: `Name`
- Type: string

Container name.
- Must be at least `1` characters long

#### description

- Schema name: `Description`
- Type: string
- Default: ""

Container description.

#### devices

- Schema name: `Devices`
- Type: array of object
- Default: []

Container's devices.
- No Additional Items

##### Each item of this array must be:

##### ContainerDeviceEntry

- Schema name: `ContainerDeviceEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the containers device.

###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

###### container (required)

- Schema name: `Container`
- Type: integer

ID of the container this device belongs to.

#### cpuset

- Schema name: `Cpuset`
- Default: null

List of physical CPU numbers that domain process and virtual CPUs can be pinned to by default.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Automatically start the container on boot.

#### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Whether container time should be local time or UTC time.

#### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

How many seconds to wait for container to shut down before killing it.
- Value must be greater or equal to `5` and lesser or equal to `300`

#### dataset (required)

- Schema name: `Dataset`
- Type: string

Which dataset to use as the container root filesystem.

#### init

- Schema name: `Init`
- Type: string
- Default: "/sbin/init"

"init" process commandline.

#### initdir

- Schema name: `Initdir`
- Default: null

"init" process working dir.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### initenv

- Schema name: `Initenv`
- Type: object
- Default: {}

"init" process environment variables.
##### Additional Properties

Each additional property must conform to the following schema
- Type: string

#### inituser

- Schema name: `Inituser`
- Default: null

"init" process username.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### initgroup

- Schema name: `Initgroup`
- Default: null

"init" process group.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### idmap

- Schema name: `Idmap`
- Default: {"type": "DEFAULT"}

Idmap configuration for the container There are three two possible values: DEFAULT: This applies the standard TrueNAS idmap namespace configuration. It changes user ID (UID) 0 (root) in the container to UID 2147000001 (truenas*container*unpriv_root). It offsets the other container UIDs by the same amount. For example, UID 1000 in the container becomes UID 2147001001 in the host. ISOLATED: Same as `DEFAULT`, but UID will be calculated as `2147000001 + 65536 * slice`. This will ensure unique ID for each container (provided that the `slice` is also unique). None: The container does not apply any idmap namespace. Container UIDs map directly to host UIDs. For example, UID 0 in the container is UID 0 in the host. WARNING: For security, use the DEFAULT value. Security best practice is to run containers with idmap namespaces.
##### Any of

###### Option 1

###### Option 2

- Schema name: `DefaultIdmapConfiguration`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: const

Configuration type for default ID mapping.

###### DefaultIdmapConfiguration

- Schema name: `IsolatedIdmapConfiguration`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: const

Configuration type for isolated ID mapping.

####### slice (required)

- Schema name: `Slice`

`null` when creating means we'll look up an unused slice on backend.
######## Any of

######### Option 1

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

######### Option 2

- Type: null

###### IsolatedIdmapConfiguration

- Type: integer
- Value must be strictly greater than `0` and strictly lesser than `1000`

###### Option 1

- Type: null

###### Option 2

- Type: null

#### capabilities_policy

- Schema name: `Capabilities Policy`
- Type: enum (of string)
- Default: "DEFAULT"

Default rules for capabilities: either keep the default behavior that is dropping the following capabilities: sys*module, sys*time, mknod, audit*control, mac*admin. Or keep all capabilities, or drop all capabilities.

#### capabilities_state

- Schema name: `Capabilities State`
- Type: object
- Default: {}

Enable or disable specific capabilities.
##### Additional Properties

Each additional property must conform to the following schema
- Type: boolean

#### default_network

- Schema name: `Default Network`
- Default: null

The default network bridge this container will use when no NIC devices are explicitly attached. When the container has explicitly configured NIC devices, this is `null` because the NIC configuration is visible in the `devices` list.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### status (required)

- Schema name: `ContainerStatus`
- Type: object

Container state.
- No Additional Properties
##### state (required)

- Schema name: `State`
- Type: enum (of string)

Container state.

##### pid (required)

- Schema name: `Pid`

Container host PID (if running). Informational only do not rely on this value to identify the container's init process.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### domain_state (required)

- Schema name: `Domain State`

Domain state reported by libvirt.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
