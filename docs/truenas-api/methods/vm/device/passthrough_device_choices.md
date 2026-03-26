---
title: vm.device.passthrough_device_choices
kind: method
source_rst: _sources/api_methods_vm.device.passthrough_device_choices.rst.txt
source_html: api_methods_vm.device.passthrough_device_choices.html
required_roles:
  - READONLY_ADMIN | VM_DEVICE_READ
---

# vm.device.passthrough_device_choices

## Summary

Available choices for PCI passthru devices

## Required Roles

- `READONLY_ADMIN | VM_DEVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `VMDevicePassthroughInfo`
- Type: object

Object of available PCI devices for passthrough with their detailed information.
#### Additional Properties

Each additional property must conform to the following schema
- Schema name: `VMDevicePassthroughDevice`
- Type: object
- No Additional Properties
##### capability (required)

- Schema name: `VMDeviceCapability`
- Type: object

PCI device capability information.
- No Additional Properties
###### class (required)

- Schema name: `Class`

PCI device class identifier. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### domain (required)

- Schema name: `Domain`

PCI domain number. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### bus (required)

- Schema name: `Bus`

PCI bus number. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### slot (required)

- Schema name: `Slot`

PCI slot number. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### function (required)

- Schema name: `Function`

PCI function number. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### product (required)

- Schema name: `Product`

Product name of the PCI device. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### vendor (required)

- Schema name: `Vendor`

Vendor name of the PCI device. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### controller_type (required)

- Schema name: `Controller Type`

Type of controller this device provides. `null` if not a controller.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### iommu_group

- Default: null

IOMMU group information for device isolation. `null` if IOMMU not available.
###### Any of

####### VMDeviceIOMMUGroup

- Schema name: `VMDeviceIOMMUGroup`
- Type: object
- No Additional Properties
######## number (required)

- Schema name: `Number`
- Type: integer

IOMMU group number for device isolation.

######## addresses (required)

- Schema name: `Addresses`
- Type: array of object

Array of PCI addresses in this IOMMU group.
- No Additional Items

######### Each item of this array must be:

######### VMDeviceIOMMUGroupAddress

- Schema name: `VMDeviceIOMMUGroupAddress`
- Type: object
- No Additional Properties
########## domain (required)

- Schema name: `Domain`
- Type: string

PCI domain number for this IOMMU group address.

########## bus (required)

- Schema name: `Bus`
- Type: string

PCI bus number for this IOMMU group address.

########## slot (required)

- Schema name: `Slot`
- Type: string

PCI slot number for this IOMMU group address.

########## function (required)

- Schema name: `Function`
- Type: string

PCI function number for this IOMMU group address.

####### Option 2

- Type: null

##### available (required)

- Schema name: `Available`
- Type: boolean

Whether the device is available for passthrough to virtual machines.

##### drivers (required)

- Schema name: `Drivers`
- Type: array of string

Array of kernel drivers currently bound to this device.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### error (required)

- Schema name: `Error`

Error message if the device cannot be used for passthrough. `null` if no error.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### reset_mechanism_defined (required)

- Schema name: `Reset Mechanism Defined`
- Type: boolean

Whether the device supports proper reset mechanisms for passthrough.

##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the PCI device.

##### critical (required)

- Schema name: `Critical`
- Type: boolean

Whether this device is critical to host system operation.

##### device_path (required)

- Schema name: `Device Path`

Device filesystem path. `null` if not available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
