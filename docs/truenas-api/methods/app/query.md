---
title: app.query
kind: method
source_rst: _sources/api_methods_app.query.rst.txt
source_html: api_methods_app.query.html
required_roles:
  - APPS_READ
---

# app.query

## Summary

Query all apps with `query-filters` and `query-options`.

`query-options.extra.host_ip` is a string which can be provided to override portal IP address if it is a wildcard.

`query-options.extra.include_app_schema` is a boolean which can be set to include app schema in the response.

`query-options.extra.retrieve_config` is a boolean which can be set to retrieve app configuration used to install/manage app.

## Required Roles

- `APPS_READ`

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

###### AppQueryResultItem

- Schema name: `AppQueryResultItem`
- Type: object
- No Additional Properties
####### name

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

####### id

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

####### state

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.

####### upgrade_available

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

####### latest_version

- Schema name: `Latest Version`

The latest available version string, or `null` if no updates are available.
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

####### image_updates_available

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

####### custom_app

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

####### migrated

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

####### human_version

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

####### version

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

####### metadata

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

####### active_workloads

- Schema name: `AppActiveWorkloads`
- Type: object

Information about the running containers, ports, and resources used by this application.
- No Additional Properties
######## containers (required)

- Schema name: `Containers`
- Type: integer

Total number of containers currently running for this application.

######## used_ports (required)

- Schema name: `Used Ports`
- Type: array of object

Array of all port mappings used by the application.
- No Additional Items

######### Each item of this array must be:

######### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
########## container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

########## protocol (required)

- Schema name: `Protocol`
- Type: string

The network protocol used.
Examples:

```json
"tcp"
```
Examples:

```json
"udp"
```

########## host_ports (required)

- Schema name: `Host Ports`
- Type: array of object

Array of host port mappings for this container port.
- No Additional Items

########### Each item of this array must be:

########### HostPorts

- Schema name: `HostPorts`
- Type: object
- No Additional Properties
############ host_port (required)

- Schema name: `Host Port`
- Type: integer

The port number on the host system.

############ host_ip (required)

- Schema name: `Host Ip`
- Type: string

The IP address on the host system that the port is bound to.

######## used_host_ips (required)

- Schema name: `Used Host Ips`
- Type: array of string

Array of host IP addresses in use by the application.
- No Additional Items

######### Each item of this array must be:

- Type: string

######## container_details (required)

- Schema name: `Container Details`
- Type: array of object

Detailed information about each container in the application.
- No Additional Items

######### Each item of this array must be:

######### AppContainerDetails

- Schema name: `AppContainerDetails`
- Type: object
- No Additional Properties
########## id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.

########## service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.

########## image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.

########## port_config (required)

- Schema name: `Port Config`
- Type: array of object

Array of port mappings for this container.
- No Additional Items

########### Each item of this array must be:

########### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
############ container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

############ protocol (required)

- Schema name: `Protocol`
- Type: string

The network protocol used.
Examples:

```json
"tcp"
```
Examples:

```json
"udp"
```

############ host_ports (required)

- Schema name: `Host Ports`
- Type: array

Array of host port mappings for this container port.
- No Additional Items

############# Each item of this array must be:

- Type: object

########## state (required)

- Schema name: `State`
- Type: enum (of string)

Current state of the container.

########## volume_mounts (required)

- Schema name: `Volume Mounts`
- Type: array of object

Array of volume mounts configured for this container.
- No Additional Items

########### Each item of this array must be:

########### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
############ source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

############ destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

############ mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

############ type (required)

- Schema name: `Type`
- Type: string

The volume type.
Examples:

```json
"bind"
```
Examples:

```json
"volume"
```

######## volumes (required)

- Schema name: `Volumes`
- Type: array of object

Array of all volume mounts used by the application.
- No Additional Items

######### Each item of this array must be:

######### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
########## source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

########## destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

########## mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

########## type (required)

- Schema name: `Type`
- Type: string

The volume type.
Examples:

```json
"bind"
```
Examples:

```json
"volume"
```

######## images (required)

- Schema name: `Images`
- Type: array of string

Array of Docker image names used by the application.
- No Additional Items

######### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

######## networks (required)

- Schema name: `Networks`
- Type: array of object

Array of Docker networks associated with the application.
- No Additional Items

######### Each item of this array must be:

######### AppNetworks

- Schema name: `AppNetworks`
- Type: object
########## Name (required)

- Schema name: `Name`
- Type: string

The name of the Docker network.

########## Id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the Docker network.

########## Labels (required)

- Schema name: `Labels`
- Type: object

Key-value pairs of labels associated with the network.

########## Additional Properties

Additional Properties of any type are allowed.
- Type: object

####### notes

- Schema name: `Notes`

User-provided notes or comments about this application instance.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### portals

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

####### version_details

- Schema name: `Version Details`

Detailed version information including changelog and upgrade notes. `null` if not available.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### config

- Schema name: `Config`

Current configuration values for the application. `null` if configuration is not requested.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

##### AppQueryResultItem

- Type: string
- Must be at least `1` characters long

##### Option 3

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: object

##### Option 2

- Type: null

##### Option 1

- Type: object

##### Option 2

- Type: null

##### Option 1

- Schema name: `AppQueryResultItem`
- Type: object
- No Additional Properties
###### name

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

###### id

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

###### state

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.

###### upgrade_available

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

###### latest_version

- Schema name: `Latest Version`

The latest available version string, or `null` if no updates are available.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### image_updates_available

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

###### custom_app

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

###### migrated

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

###### human_version

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

###### version

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

###### metadata

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

###### active_workloads

- Type: object

Information about the running containers, ports, and resources used by this application.

###### notes

- Schema name: `Notes`

User-provided notes or comments about this application instance.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### portals

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

###### version_details

- Schema name: `Version Details`

Detailed version information including changelog and upgrade notes. `null` if not available.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### config

- Schema name: `Config`

Current configuration values for the application. `null` if configuration is not requested.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
