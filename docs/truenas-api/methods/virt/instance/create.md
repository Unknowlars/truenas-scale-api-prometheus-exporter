---
title: virt.instance.create
kind: method
source_rst: _sources/api_methods_virt.instance.create.rst.txt
source_html: api_methods_virt.instance.create.html
required_roles:
  - VIRT_INSTANCE_WRITE
---

# virt.instance.create

## Summary

Create a new virtualized instance.

This method is a job.

## Required Roles

- `VIRT_INSTANCE_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: virt_instance_create

#### virt_instance_create

- Schema name: `virt_instance_create`
- Type: object

VirtInstanceCreateArgs parameters.
- No Additional Properties
##### name (required)

- Schema name: `Name`
- Type: string

Name for the new virtual instance.
- Must be at least `1` characters long
- Must be at most `200` characters long

##### source_type

- Schema name: `Source Type`
- Type: const
- Default: "IMAGE"

Source type for instance creation.

##### storage_pool

- Schema name: `Storage Pool`
- Default: null

Storage pool under which to allocate root filesystem. Must be one of the pools listed in virt.global.config output under "storage_pools". If None (default) then the pool specified in the global configuration will be used.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### image (required)

- Schema name: `Image`
- Type: string

Image identifier to use for creating the instance.
- Must be at least `1` characters long
- Must be at most `200` characters long

##### root_disk_size

- Schema name: `Root Disk Size`
- Type: integer
- Default: 10

This can be specified when creating VMs so the root device's size can be configured. Root device for VMs is a sparse zvol and the field specifies space in GBs and defaults to 10 GBs.
- Value must be greater or equal to `5`

##### root_disk_io_bus

- Schema name: `Root Disk Io Bus`
- Type: enum (of string)
- Default: "NVME"

I/O bus type for the root disk (defaults to NVME for best performance).

##### remote

- Schema name: `Remote`
- Type: const
- Default: "LINUX_CONTAINERS"

Remote image source to use.

##### instance_type

- Schema name: `Instance Type`
- Type: const
- Default: "CONTAINER"

Type of instance to create.

##### environment

- Schema name: `Environment`
- Default: null

Environment variables to set inside the instance.
###### Any of

####### Option 1

- Type: object
######## Additional Properties

Each additional property must conform to the following schema
- Type: string

####### Option 2

- Type: null

##### autostart

- Schema name: `Autostart`
- Default: true

Whether the instance should automatically start when the host boots.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### cpu

- Schema name: `Cpu`
- Default: null

CPU allocation specification or `null` for automatic allocation.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### devices

- Schema name: `Devices`
- Default: null

Array of devices to attach to the instance.
###### Any of

####### Option 1

- Type: array
- No Additional Items

######## Each item of this array must be:

####### Option 2

- Schema name: `Disk`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for virtual disk devices.

######## source

- Schema name: `Source`
- Default: null

For CONTAINER instances, this would be a valid pool path. For VM instances, it can be a valid zvol path or an incus storage volume name.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## destination

- Schema name: `Destination`
- Default: null

Target path where the disk appears inside the virtualized instance.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## boot_priority

- Schema name: `Boot Priority`
- Default: null

Boot priority for this disk device. Lower numbers boot first. `null` means non-bootable.
######### Any of

########## Option 1

- Type: integer
- Value must be greater or equal to `0`

########## Option 2

- Type: null

######## io_bus

- Schema name: `Io Bus`
- Type: enum (of null or string)
- Default: null

Storage bus type for optimal performance and compatibility.

######## storage_pool

- Schema name: `Storage Pool`
- Default: null

Storage pool in which the device is located. This must be one of the storage pools listed in virt.global.config output. If this is set to None during device creation, then the default storage pool defined in virt.global.config will be used.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

####### Disk

- Type: string
- Must be at least `1` characters long

####### GPU

- Type: null

####### Proxy

- Type: string
- Must be at least `1` characters long

####### TPM

- Type: null

####### USB

- Type: string
- Must be at least `1` characters long

####### NIC

- Type: null

####### PCI

- Type: string

####### CDROM

- Type: null

####### Option 1

- Type: integer
- Value must be greater or equal to `0`

####### Option 2

- Type: null

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Schema name: `GPU`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for graphics processing units.

######## gpu_type (required)

- Schema name: `Gpu Type`
- Type: enum (of string)

Type of GPU virtualization (physical passthrough, mediated device, etc.).

######## id

- Schema name: `Id`
- Default: null

Unique identifier for the GPU device.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## gid

- Schema name: `Gid`
- Default: null

Group ID for device permissions inside the container.
######### Any of

########## Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `90000000`

########## Option 2

- Type: null

######## uid

- Schema name: `Uid`
- Default: null

User ID for device permissions inside the container.
######### Any of

########## Option 1

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `90000000`

########## Option 2

- Type: null

######## mode

- Schema name: `Mode`
- Default: null

Permission mode for device access (e.g., '660').
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## mdev

- Schema name: `Mdev`
- Default: null

Mediated device identifier for GPU virtualization.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## mig_uuid

- Schema name: `Mig Uuid`
- Default: null

Multi-Instance GPU UUID for NVIDIA GPU partitioning.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## pci

- Schema name: `Pci`
- Default: null

PCI address of the GPU device on the host system.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## productid

- Schema name: `Productid`
- Default: null

Product identifier for GPU device matching.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## vendorid

- Schema name: `Vendorid`
- Default: null

Vendor identifier for GPU device matching.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `90000000`

####### Option 1

- Type: null

####### Option 2

- Type: integer
- Value must be greater or equal to `0` and lesser or equal to `90000000`

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Schema name: `Proxy`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for network port forwarding.

######## source_proto (required)

- Schema name: `Source Proto`
- Type: enum (of string)

Network protocol (TCP or UDP) for the source connection.

######## source_port (required)

- Schema name: `Source Port`
- Type: integer

Source port number on the host system to forward from.
- Value must be greater or equal to `1` and lesser or equal to `65535`

######## dest_proto (required)

- Schema name: `Dest Proto`
- Type: enum (of string)

Network protocol (TCP or UDP) for the destination connection.

######## dest_port (required)

- Schema name: `Dest Port`
- Type: integer

Destination port number inside the virtualized instance.
- Value must be greater or equal to `1` and lesser or equal to `65535`

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Schema name: `TPM`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for Trusted Platform Module devices.

######## path

- Schema name: `Path`
- Default: null

Path to the TPM device on the host system.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## pathrm

- Schema name: `Pathrm`
- Default: null

Resource manager path for TPM device access.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Schema name: `USB`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for USB devices.

######## bus

- Schema name: `Bus`
- Default: null

USB bus number on the host system.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## dev

- Schema name: `Dev`
- Default: null

USB device number on the specified bus.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## product_id

- Schema name: `Product Id`
- Default: null

USB product identifier for device matching.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## vendor_id

- Schema name: `Vendor Id`
- Default: null

USB vendor identifier for device matching.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Type: integer

####### Option 2

- Type: null

####### Option 1

- Type: integer

####### Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: null

####### Option 1

- Type: string

####### Option 2

- Type: null

####### Option 1

- Schema name: `NIC`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for network interface cards.

######## network

- Schema name: `Network`
- Default: null

Name of the network to connect this NIC to.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## nic_type

- Schema name: `Nic Type`
- Default: null

Type of network interface (bridged or macvlan).
######### Any of

########## Option 1

- Type: enum (of string)

########## Option 2

- Type: null

######## parent

- Schema name: `Parent`
- Default: null

Parent network interface on the host system.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generated.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: enum (of string)

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Schema name: `PCI`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for PCI device passthrough.

######## address (required)

- Schema name: `Address`
- Type: string

PCI bus address of the device to pass through to the virtualized instance.
- Must be at least `1` characters long

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

####### Option 1

- Schema name: `CDROM`
- Type: object
- No Additional Properties
######## name

- Schema name: `Name`
- Default: null

Optional human-readable name for the virtualization device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## description

- Schema name: `Description`
- Default: null

Optional description explaining the purpose or configuration of this device.
######### Any of

########## Option 1

- Type: string
- Must be at least `1` characters long

########## Option 2

- Type: null

######## readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

Whether the device should be mounted in read-only mode.

######## dev_type (required)

- Schema name: `Dev Type`
- Type: const

Device type identifier for CD-ROM/DVD optical drives.

######## source (required)

- Schema name: `Source`
- Type: string

Path to the ISO image file or physical optical drive to mount.
- Must be at least `1` characters long

######## boot_priority

- Schema name: `Boot Priority`
- Default: null

Boot priority for this optical device. Lower numbers boot first. `null` means non-bootable.
######### Any of

########## Option 1

- Type: integer
- Value must be greater or equal to `0`

########## Option 2

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: string
- Must be at least `1` characters long

####### Option 1

- Type: null

####### Option 2

- Type: integer
- Value must be greater or equal to `0`

####### Option 1

- Type: null

####### Option 2

- Type: null

##### memory

- Schema name: `Memory`
- Default: null

Memory allocation in bytes or `null` for automatic allocation.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### privileged_mode

- Schema name: `Privileged Mode`
- Type: boolean
- Default: false

This is only valid for containers and should only be set when container instance which is to be deployed is to run in a privileged mode.

### Return value

- Schema name: `VirtInstanceEntry`
- Type: object

The created virtual instance configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the virtual instance.

#### name (required)

- Schema name: `Name`
- Type: string

Human-readable name for the virtual instance.
- Must be at least `1` characters long
- Must be at most `200` characters long

#### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "CONTAINER"

Type of virtual instance.

#### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current operational status of the virtual instance.

#### cpu (required)

- Schema name: `Cpu`

CPU configuration string or `null` for default allocation.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### memory (required)

- Schema name: `Memory`

Memory allocation in bytes or `null` for default allocation.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### autostart (required)

- Schema name: `Autostart`
- Type: boolean

Whether the instance automatically starts when the host boots.

#### environment (required)

- Schema name: `Environment`
- Type: object

Environment variables to set inside the instance.
##### Additional Properties

Each additional property must conform to the following schema
- Type: string

#### aliases (required)

- Schema name: `Aliases`
- Type: array of object

Array of IP aliases configured for the instance.
- No Additional Items

##### Each item of this array must be:

##### VirtInstanceAlias

- Schema name: `VirtInstanceAlias`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of IP address (INET for IPv4, INET6 for IPv6).

###### address (required)

- Schema name: `Address`
- Type: string

IP address for the virtual instance.
- Must be at least `1` characters long

###### netmask (required)

- Schema name: `Netmask`

Network mask in CIDR notation.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

#### image (required)

- Schema name: `Image`
- Type: object

Image information used to create this instance.
- No Additional Properties
##### architecture (required)

- Schema name: `Architecture`

Hardware architecture of the image (e.g., amd64, arm64).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### description (required)

- Schema name: `Description`

Human-readable description of the image.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### os (required)

- Schema name: `Os`

Operating system family of the image.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### release (required)

- Schema name: `Release`

Version or release name of the operating system.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### serial (required)

- Schema name: `Serial`

Unique serial identifier for the image.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### type (required)

- Schema name: `Type`

Type of image (container, virtual-machine, etc.).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### variant (required)

- Schema name: `Variant`

Image variant (default, cloud, minimal, etc.).
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### secureboot (required)

- Schema name: `Secureboot`

Whether the image supports UEFI Secure Boot.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

#### userns_idmap (required)

User namespace ID mapping configuration for privilege isolation.
##### Any of

###### UserNsIdmap

- Schema name: `UserNsIdmap`
- Type: object
- No Additional Properties
####### uid (required)

User ID mapping configuration for user namespace isolation.
######## Any of

######### IdmapUserNsEntry

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
########## hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

########## maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

########## nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

######### Option 2

- Type: null

####### gid (required)

Group ID mapping configuration for user namespace isolation.
######## Any of

######### IdmapUserNsEntry

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
########## hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

########## maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

########## nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

######### Option 2

- Type: null

###### Option 2

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
####### hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

####### maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

####### nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

###### IdmapUserNsEntry

- Type: null

###### Option 2

- Schema name: `IdmapUserNsEntry`
- Type: object
- No Additional Properties
####### hostid (required)

- Schema name: `Hostid`
- Type: integer

Starting host ID for the mapping range.

####### maprange (required)

- Schema name: `Maprange`
- Type: integer

Number of IDs to map in this range.

####### nsid (required)

- Schema name: `Nsid`
- Type: integer

Starting namespace ID for the mapping range.

###### IdmapUserNsEntry

- Type: null

###### Option 2

- Type: null

#### raw (required)

- Schema name: `Raw`

Raw low-level configuration options (advanced use only).
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

#### vnc_enabled (required)

- Schema name: `Vnc Enabled`
- Type: boolean

Whether VNC remote access is enabled for the instance.

#### vnc_port (required)

- Schema name: `Vnc Port`

TCP port number for VNC connections or `null` if VNC is disabled.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### vnc_password (required)

- Schema name: `Vnc Password`

Password for VNC access or `null` if no password is set.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### secure_boot (required)

- Schema name: `Secure Boot`

Whether UEFI Secure Boot is enabled (VMs only) or `null` for containers.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### privileged_mode (required)

- Schema name: `Privileged Mode`

Whether the container runs in privileged mode or `null` for VMs.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

#### root_disk_size (required)

- Schema name: `Root Disk Size`

Size of the root disk in GB or `null` for default size.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### root_disk_io_bus (required)

- Schema name: `Root Disk Io Bus`
- Type: enum (of null or string)

I/O bus type for the root disk or `null` for default.

#### storage_pool (required)

- Schema name: `Storage Pool`
- Type: string

Storage pool in which the root of the instance is located.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
