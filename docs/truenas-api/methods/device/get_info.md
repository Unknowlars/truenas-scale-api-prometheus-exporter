---
title: device.get_info
kind: method
source_rst: _sources/api_methods_device.get_info.rst.txt
source_html: api_methods_device.get_info.html
required_roles:
  - READONLY_ADMIN
---

# device.get_info

## Summary

Get info for `type` device.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`

Device information query parameters specifying type and options.
##### Any of

###### DeviceGetInfoDisk

- Schema name: `DeviceGetInfoDisk`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: const

Get disk info.

####### get_partitions

- Schema name: `Get Partitions`
- Type: boolean
- Default: false

If set, query partition information for the disks. **NOTE: This can be expensive on systems with a large number of disks present.**

####### serials_only

- Schema name: `Serials Only`
- Type: boolean
- Default: false

If set, query *ONLY* serial information for the disks (overrides `get_partitions`).

###### DeviceGetInfoOther

- Schema name: `DeviceGetInfoOther`
- Type: object
- No Additional Properties
####### type (required)

- Schema name: `Type`
- Type: enum (of string)

Get info for either serial devices or GPUs.

### Return value

- Schema name: `Result`

Return an object if `type="DISK"` or an array otherwise.
#### Any of

##### Option 1

- Type: object
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

##### Option 2

- Type: object
###### Additional Properties

Each additional property must conform to the following schema
- Type: object

##### Option 3

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### SerialInfo

- Schema name: `SerialInfo`
- Type: object
- No Additional Properties
####### name (required)

- Schema name: `Name`
- Type: string

Device name for the serial port.

####### location (required)

- Schema name: `Location`
- Type: string

Physical location or path of the serial device.

####### drivername (required)

- Schema name: `Drivername`
- Type: string

Name of the kernel driver handling this serial device.

####### start (required)

- Schema name: `Start`
- Type: string

Starting address or identifier for the serial device.

####### size (required)

- Schema name: `Size`
- Type: integer

Size or capacity information for the serial device.

####### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the serial device.

##### Option 4

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### GPUInfo

- Schema name: `GPUInfo`
- Type: object
####### addr (required)

- Schema name: `GPUInfoAddr`
- Type: object

PCI address information for the GPU.
- No Additional Properties
######## pci_slot (required)

- Schema name: `Pci Slot`
- Type: string

PCI slot identifier for the GPU.

######## domain (required)

- Schema name: `Domain`
- Type: string

PCI domain number.

######## bus (required)

- Schema name: `Bus`
- Type: string

PCI bus number.

######## slot (required)

- Schema name: `Slot`
- Type: string

PCI slot number.

####### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the GPU.

####### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of PCI devices associated with this GPU.
- No Additional Items

######## Each item of this array must be:

######## GPUInfoDevice

- Schema name: `GPUInfoDevice`
- Type: object
- No Additional Properties
######### pci_id (required)

- Schema name: `Pci Id`
- Type: string

PCI device identifier.

######### pci_slot (required)

- Schema name: `Pci Slot`
- Type: string

PCI slot location.

######### vm_pci_slot (required)

- Schema name: `Vm Pci Slot`
- Type: string

Virtual machine PCI slot mapping.

####### vendor (required)

- Schema name: `Vendor`

GPU vendor name or `null` if unknown.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### available_to_host (required)

- Schema name: `Available To Host`
- Type: boolean

Whether the GPU is available for use by the host system.

####### uses_system_critical_devices (required)

- Schema name: `Uses System Critical Devices`
- Type: boolean

Whether the GPU uses devices critical for system operation.

####### critical_reason (required)

- Schema name: `Critical Reason`

Reason why GPU is considered critical or `null` if not critical.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### Additional Properties

Additional Properties of any type are allowed.
- Type: object

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
