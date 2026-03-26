---
title: virt.instance.query
kind: event
source_rst: _sources/api_events_virt.instance.query.rst.txt
source_html: api_events_virt.instance.query.html
required_roles:
  - VIRT_INSTANCE_READ
---

# virt.instance.query

## Summary

Sent on virt.instance changes.

## Required Roles

- `VIRT_INSTANCE_READ`

## Schema

- Type: object

### ADDED

- Schema name: `VirtInstanceAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `VirtInstanceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtual instance.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the virtual instance.
- Must be at least `1` characters long
- Must be at most `200` characters long

##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "CONTAINER"

Type of virtual instance.

##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current operational status of the virtual instance.

##### cpu (required)

- Schema name: `Cpu`

CPU configuration string or `null` for default allocation.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### memory (required)

- Schema name: `Memory`

Memory allocation in bytes or `null` for default allocation.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### autostart (required)

- Schema name: `Autostart`
- Type: boolean

Whether the instance automatically starts when the host boots.

##### environment (required)

- Schema name: `Environment`
- Type: object

Environment variables to set inside the instance.
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

##### aliases (required)

- Schema name: `Aliases`
- Type: array of object

Array of IP aliases configured for the instance.
- No Additional Items

###### Each item of this array must be:

###### VirtInstanceAlias

- Schema name: `VirtInstanceAlias`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of IP address (INET for IPv4, INET6 for IPv6).

####### address (required)

- Schema name: `Address`
- Type: string

IP address for the virtual instance.
- Must be at least `1` characters long

####### netmask (required)

- Schema name: `Netmask`

Network mask in CIDR notation.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

##### image (required)

- Schema name: `Image`
- Type: object

Image information used to create this instance.
- No Additional Properties
###### architecture (required)

- Schema name: `Architecture`

Hardware architecture of the image (e.g., amd64, arm64).
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### description (required)

- Schema name: `Description`

Human-readable description of the image.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### os (required)

- Schema name: `Os`

Operating system family of the image.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### release (required)

- Schema name: `Release`

Version or release name of the operating system.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### serial (required)

- Schema name: `Serial`

Unique serial identifier for the image.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### type (required)

- Schema name: `Type`

Type of image (container, virtual-machine, etc.).
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### variant (required)

- Schema name: `Variant`

Image variant (default, cloud, minimal, etc.).
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### secureboot (required)

- Schema name: `Secureboot`

Whether the image supports UEFI Secure Boot.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

##### userns_idmap (required)

User namespace ID mapping configuration for privilege isolation.
###### Any of

####### UserNsIdmap

- Schema name: `UserNsIdmap`
- Type: object
- No Additional Properties
######## uid (required)

User ID mapping configuration for user namespace isolation.
######### Any of

########## IdmapUserNsEntry

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
########### hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

########### maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

########### nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

########## Option 2

- Type: null

######## gid (required)

Group ID mapping configuration for user namespace isolation.
######### Any of

########## IdmapUserNsEntry

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
########### hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

########### maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

########### nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

########## Option 2

- Type: null

####### Option 2

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
######## hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

######## maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

######## nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

####### IdmapUserNsEntry

- Type: null

####### Option 2

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
######## hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

######## maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

######## nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

####### IdmapUserNsEntry

- Type: null

####### Option 2

- Type: null

##### raw (required)

- Schema name: `Raw`

Raw low-level configuration options (advanced use only).
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### vnc_enabled (required)

- Schema name: `Vnc Enabled`
- Type: boolean

Whether VNC remote access is enabled for the instance.

##### vnc_port (required)

- Schema name: `Vnc Port`

TCP port number for VNC connections or `null` if VNC is disabled.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### vnc_password (required)

- Schema name: `Vnc Password`

Password for VNC access or `null` if no password is set.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### secure_boot (required)

- Schema name: `Secure Boot`

Whether UEFI Secure Boot is enabled (VMs only) or `null` for containers.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### privileged_mode (required)

- Schema name: `Privileged Mode`

Whether the container runs in privileged mode or `null` for VMs.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### root_disk_size (required)

- Schema name: `Root Disk Size`

Size of the root disk in GB or `null` for default size.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### root_disk_io_bus (required)

- Schema name: `Root Disk Io Bus`
- Type: enum (of null or string)

I/O bus type for the root disk or `null` for default.

##### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Storage pool in which the root of the instance is located.
- Must be at least `1` characters long

### CHANGED

- Schema name: `VirtInstanceChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

#### fields (required)

- Schema name: `VirtInstanceEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtual instance.

##### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the virtual instance.
- Must be at least `1` characters long
- Must be at most `200` characters long

##### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "CONTAINER"

Type of virtual instance.

##### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current operational status of the virtual instance.

##### cpu (required)

- Schema name: `Cpu`

CPU configuration string or `null` for default allocation.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### memory (required)

- Schema name: `Memory`

Memory allocation in bytes or `null` for default allocation.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### autostart (required)

- Schema name: `Autostart`
- Type: boolean

Whether the instance automatically starts when the host boots.

##### environment (required)

- Schema name: `Environment`
- Type: object

Environment variables to set inside the instance.
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

##### aliases (required)

- Schema name: `Aliases`
- Type: array of object

Array of IP aliases configured for the instance.
- No Additional Items

###### Each item of this array must be:

###### VirtInstanceAlias

- Schema name: `VirtInstanceAlias`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of IP address (INET for IPv4, INET6 for IPv6).

####### address (required)

- Schema name: `Address`
- Type: string

IP address for the virtual instance.
- Must be at least `1` characters long

####### netmask (required)

- Schema name: `Netmask`

Network mask in CIDR notation.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

##### image (required)

- Schema name: `Image`
- Type: object

Image information used to create this instance.
- No Additional Properties
###### architecture (required)

- Schema name: `Architecture`

Hardware architecture of the image (e.g., amd64, arm64).
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### description (required)

- Schema name: `Description`

Human-readable description of the image.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### os (required)

- Schema name: `Os`

Operating system family of the image.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### release (required)

- Schema name: `Release`

Version or release name of the operating system.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### serial (required)

- Schema name: `Serial`

Unique serial identifier for the image.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### type (required)

- Schema name: `Type`

Type of image (container, virtual-machine, etc.).
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### variant (required)

- Schema name: `Variant`

Image variant (default, cloud, minimal, etc.).
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### secureboot (required)

- Schema name: `Secureboot`

Whether the image supports UEFI Secure Boot.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

##### userns_idmap (required)

User namespace ID mapping configuration for privilege isolation.
###### Any of

####### UserNsIdmap

- Schema name: `UserNsIdmap`
- Type: object
- No Additional Properties
######## uid (required)

User ID mapping configuration for user namespace isolation.
######### Any of

########## IdmapUserNsEntry

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
########### hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

########### maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

########### nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

########## Option 2

- Type: null

######## gid (required)

Group ID mapping configuration for user namespace isolation.
######### Any of

########## IdmapUserNsEntry

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
########### hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

########### maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

########### nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

########## Option 2

- Type: null

####### Option 2

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
######## hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

######## maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

######## nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

####### IdmapUserNsEntry

- Type: null

####### Option 2

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
######## hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

######## maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

######## nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

####### IdmapUserNsEntry

- Type: null

####### Option 2

- Type: null

##### raw (required)

- Schema name: `Raw`

Raw low-level configuration options (advanced use only).
###### Any of

####### Option 1

- Type: object

####### Option 2

- Type: null

##### vnc_enabled (required)

- Schema name: `Vnc Enabled`
- Type: boolean

Whether VNC remote access is enabled for the instance.

##### vnc_port (required)

- Schema name: `Vnc Port`

TCP port number for VNC connections or `null` if VNC is disabled.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### vnc_password (required)

- Schema name: `Vnc Password`

Password for VNC access or `null` if no password is set.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### secure_boot (required)

- Schema name: `Secure Boot`

Whether UEFI Secure Boot is enabled (VMs only) or `null` for containers.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### privileged_mode (required)

- Schema name: `Privileged Mode`

Whether the container runs in privileged mode or `null` for VMs.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### root_disk_size (required)

- Schema name: `Root Disk Size`

Size of the root disk in GB or `null` for default size.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### root_disk_io_bus (required)

- Schema name: `Root Disk Io Bus`
- Type: enum (of null or string)

I/O bus type for the root disk or `null` for default.

##### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Storage pool in which the root of the instance is located.
- Must be at least `1` characters long

### REMOVED

- Schema name: `VirtInstanceRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
