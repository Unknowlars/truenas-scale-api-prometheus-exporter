---
title: app.query
kind: event
source_rst: _sources/api_events_app.query.rst.txt
source_html: api_events_app.query.html
required_roles:
  - APPS_READ
---

# app.query

## Summary

Sent on app changes.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### ADDED

- Schema name: `AppAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `AppEntry`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.

##### upgrade_available (required)

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

##### latest_version (required)

- Schema name: `Latest Version`

The latest available version string, or `null` if no updates are available.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### image_updates_available (required)

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

##### custom_app (required)

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

##### migrated (required)

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

##### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

##### version (required)

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

##### metadata (required)

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

##### active_workloads (required)

- Schema name: `AppActiveWorkloads`
- Type: object

Information about the running containers, ports, and resources used by this application.
- No Additional Properties
###### containers (required)

- Schema name: `Containers`
- Type: integer

Total number of containers currently running for this application.

###### used_ports (required)

- Schema name: `Used Ports`
- Type: array of object

Array of all port mappings used by the application.
- No Additional Items

####### Each item of this array must be:

####### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
######## container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

######## protocol (required)

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

######## host_ports (required)

- Schema name: `Host Ports`
- Type: array of object

Array of host port mappings for this container port.
- No Additional Items

######### Each item of this array must be:

######### HostPorts

- Schema name: `HostPorts`
- Type: object
- No Additional Properties
########## host_port (required)

- Schema name: `Host Port`
- Type: integer

The port number on the host system.

########## host_ip (required)

- Schema name: `Host Ip`
- Type: string

The IP address on the host system that the port is bound to.

###### used_host_ips (required)

- Schema name: `Used Host Ips`
- Type: array of string

Array of host IP addresses in use by the application.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### container_details (required)

- Schema name: `Container Details`
- Type: array of object

Detailed information about each container in the application.
- No Additional Items

####### Each item of this array must be:

####### AppContainerDetails

- Schema name: `AppContainerDetails`
- Type: object
- No Additional Properties
######## id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.

######## service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.

######## image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.

######## port_config (required)

- Schema name: `Port Config`
- Type: array of object

Array of port mappings for this container.
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
- Type: array

Array of host port mappings for this container port.
- No Additional Items

########### Each item of this array must be:

- Type: object

######## state (required)

- Schema name: `State`
- Type: enum (of string)

Current state of the container.

######## volume_mounts (required)

- Schema name: `Volume Mounts`
- Type: array of object

Array of volume mounts configured for this container.
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

###### volumes (required)

- Schema name: `Volumes`
- Type: array of object

Array of all volume mounts used by the application.
- No Additional Items

####### Each item of this array must be:

####### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
######## source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

######## destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

######## mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

######## type (required)

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

###### images (required)

- Schema name: `Images`
- Type: array of string

Array of Docker image names used by the application.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### networks (required)

- Schema name: `Networks`
- Type: array of object

Array of Docker networks associated with the application.
- No Additional Items

####### Each item of this array must be:

####### AppNetworks

- Schema name: `AppNetworks`
- Type: object
######## Name (required)

- Schema name: `Name`
- Type: string

The name of the Docker network.

######## Id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the Docker network.

######## Labels (required)

- Schema name: `Labels`
- Type: object

Key-value pairs of labels associated with the network.

######## Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### notes (required)

- Schema name: `Notes`

User-provided notes or comments about this application instance.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### portals (required)

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

##### version_details

- Schema name: `Version Details`
- Default: null

Detailed version information including changelog and upgrade notes. `null` if not available.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### config

- Schema name: `Config`
- Default: null

Current configuration values for the application. `null` if configuration is not requested.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

### CHANGED

- Schema name: `AppChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `AppEntry`
- Type: object
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.

##### upgrade_available (required)

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

##### latest_version (required)

- Schema name: `Latest Version`

The latest available version string, or `null` if no updates are available.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### image_updates_available (required)

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

##### custom_app (required)

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

##### migrated (required)

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

##### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

##### version (required)

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

##### metadata (required)

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

##### active_workloads (required)

- Schema name: `AppActiveWorkloads`
- Type: object

Information about the running containers, ports, and resources used by this application.
- No Additional Properties
###### containers (required)

- Schema name: `Containers`
- Type: integer

Total number of containers currently running for this application.

###### used_ports (required)

- Schema name: `Used Ports`
- Type: array of object

Array of all port mappings used by the application.
- No Additional Items

####### Each item of this array must be:

####### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
######## container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

######## protocol (required)

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

######## host_ports (required)

- Schema name: `Host Ports`
- Type: array of object

Array of host port mappings for this container port.
- No Additional Items

######### Each item of this array must be:

######### HostPorts

- Schema name: `HostPorts`
- Type: object
- No Additional Properties
########## host_port (required)

- Schema name: `Host Port`
- Type: integer

The port number on the host system.

########## host_ip (required)

- Schema name: `Host Ip`
- Type: string

The IP address on the host system that the port is bound to.

###### used_host_ips (required)

- Schema name: `Used Host Ips`
- Type: array of string

Array of host IP addresses in use by the application.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### container_details (required)

- Schema name: `Container Details`
- Type: array of object

Detailed information about each container in the application.
- No Additional Items

####### Each item of this array must be:

####### AppContainerDetails

- Schema name: `AppContainerDetails`
- Type: object
- No Additional Properties
######## id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.

######## service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.

######## image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.

######## port_config (required)

- Schema name: `Port Config`
- Type: array of object

Array of port mappings for this container.
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
- Type: array

Array of host port mappings for this container port.
- No Additional Items

########### Each item of this array must be:

- Type: object

######## state (required)

- Schema name: `State`
- Type: enum (of string)

Current state of the container.

######## volume_mounts (required)

- Schema name: `Volume Mounts`
- Type: array of object

Array of volume mounts configured for this container.
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

###### volumes (required)

- Schema name: `Volumes`
- Type: array of object

Array of all volume mounts used by the application.
- No Additional Items

####### Each item of this array must be:

####### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
######## source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

######## destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

######## mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

######## type (required)

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

###### images (required)

- Schema name: `Images`
- Type: array of string

Array of Docker image names used by the application.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### networks (required)

- Schema name: `Networks`
- Type: array of object

Array of Docker networks associated with the application.
- No Additional Items

####### Each item of this array must be:

####### AppNetworks

- Schema name: `AppNetworks`
- Type: object
######## Name (required)

- Schema name: `Name`
- Type: string

The name of the Docker network.

######## Id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the Docker network.

######## Labels (required)

- Schema name: `Labels`
- Type: object

Key-value pairs of labels associated with the network.

######## Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### notes (required)

- Schema name: `Notes`

User-provided notes or comments about this application instance.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### portals (required)

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

##### version_details

- Schema name: `Version Details`
- Default: null

Detailed version information including changelog and upgrade notes. `null` if not available.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### config

- Schema name: `Config`
- Default: null

Current configuration values for the application. `null` if configuration is not requested.
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

### REMOVED

- Schema name: `AppRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
