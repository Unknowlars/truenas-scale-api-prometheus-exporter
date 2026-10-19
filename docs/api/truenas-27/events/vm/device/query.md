---
title: vm.device.query
kind: event
source_rst: _sources/api_events_vm.device.query.rst.txt
source_html: api_events_vm.device.query.html
required_roles:
  - VM_DEVICE_READ
---

# vm.device.query

## Summary

Sent on vm.device changes.

## Required Roles

- `VM_DEVICE_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `VMDeviceAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

<a id="headingADDED_fields_attributes"></a>
<a id="ADDED_fields_attributes"></a>
##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="ADDED_fields_attributes_oneOf"></a>
###### One of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i0"></a>
###### [VMCDROMDevice](#tab-pane_ADDED_fields_attributes_oneOf_i0)

- Schema name: `VMCDROMDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i0_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for CD-ROM/DVD devices.
- Specific value: `"CDROM"`

<a id="headingADDED_fields_attributes_oneOf_i0_path"></a>
<a id="ADDED_fields_attributes_oneOf_i0_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Path must not contain "{", "}" characters, and it should start with "/mnt/".
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1"></a>
###### [VMDisplayDevice](#tab-pane_ADDED_fields_attributes_oneOf_i1)

- Schema name: `VMDisplayDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i1_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.
- Specific value: `"DISPLAY"`

<a id="headingADDED_fields_attributes_oneOf_i1_resolution"></a>
<a id="ADDED_fields_attributes_oneOf_i1_resolution"></a>
###### resolution

- Schema name: `Resolution`
- Type: enum (of string)
- Default: "1024x768"

Screen resolution for the virtual display.
###### Must be one of:

- "1920x1200"
- "1920x1080"
- "1600x1200"
- "1600x900"
- "1400x1050"
- "1280x1024"
- "1280x720"
- "1024x768"
- "800x600"
- "640x480"

<a id="headingADDED_fields_attributes_oneOf_i1_port"></a>
<a id="ADDED_fields_attributes_oneOf_i1_port"></a>
###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
<a id="ADDED_fields_attributes_oneOf_i1_port_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i1_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i1_port_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i1_web_port"></a>
<a id="ADDED_fields_attributes_oneOf_i1_web_port"></a>
###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
<a id="ADDED_fields_attributes_oneOf_i1_web_port_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1_web_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i1_web_port_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1_web_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i1_web_port_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i1_bind"></a>
<a id="ADDED_fields_attributes_oneOf_i1_bind"></a>
###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

<a id="headingADDED_fields_attributes_oneOf_i1_wait"></a>
<a id="ADDED_fields_attributes_oneOf_i1_wait"></a>
###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

<a id="headingADDED_fields_attributes_oneOf_i1_password"></a>
<a id="ADDED_fields_attributes_oneOf_i1_password"></a>
###### password

- Schema name: `Password`
- Default: null

Password for display server authentication.
<a id="ADDED_fields_attributes_oneOf_i1_password_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i1_password_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_attributes_oneOf_i1_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i1_password_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i1_web"></a>
<a id="ADDED_fields_attributes_oneOf_i1_web"></a>
###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

<a id="headingADDED_fields_attributes_oneOf_i1_type"></a>
<a id="ADDED_fields_attributes_oneOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.
###### Must be one of:

- "SPICE"
- "VNC"

<a id="tab-pane_ADDED_fields_attributes_oneOf_i2"></a>
###### [VMNICDevice](#tab-pane_ADDED_fields_attributes_oneOf_i2)

- Schema name: `VMNICDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i2_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingADDED_fields_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="ADDED_fields_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingADDED_fields_attributes_oneOf_i2_type"></a>
<a id="ADDED_fields_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingADDED_fields_attributes_oneOf_i2_nic_attach"></a>
<a id="ADDED_fields_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="ADDED_fields_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i2_mac"></a>
<a id="ADDED_fields_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="ADDED_fields_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_attributes_oneOf_i3"></a>
###### [VMPCIDevice](#tab-pane_ADDED_fields_attributes_oneOf_i3)

- Schema name: `VMPCIDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i3_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for PCI passthrough devices.
- Specific value: `"PCI"`

<a id="headingADDED_fields_attributes_oneOf_i3_pptdev"></a>
<a id="ADDED_fields_attributes_oneOf_i3_pptdev"></a>
###### pptdev (required)

- Schema name: `Pptdev`
- Type: string

Host PCI device identifier to pass through to the VM.
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4"></a>
###### [VMRAWDevice](#tab-pane_ADDED_fields_attributes_oneOf_i4)

- Schema name: `VMRAWDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i4_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i4_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for raw disk devices.
- Specific value: `"RAW"`

<a id="headingADDED_fields_attributes_oneOf_i4_path"></a>
<a id="ADDED_fields_attributes_oneOf_i4_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to the raw disk device or image file.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingADDED_fields_attributes_oneOf_i4_type"></a>
<a id="ADDED_fields_attributes_oneOf_i4_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingADDED_fields_attributes_oneOf_i4_exists"></a>
<a id="ADDED_fields_attributes_oneOf_i4_exists"></a>
###### exists

- Schema name: `Exists`
- Type: boolean
- Default: false

Whether the disk file already exists or should be created.

<a id="headingADDED_fields_attributes_oneOf_i4_boot"></a>
<a id="ADDED_fields_attributes_oneOf_i4_boot"></a>
###### boot

- Schema name: `Boot`
- Type: boolean
- Default: false

Whether this disk should be marked as bootable.

<a id="headingADDED_fields_attributes_oneOf_i4_size"></a>
<a id="ADDED_fields_attributes_oneOf_i4_size"></a>
###### size

- Schema name: `Size`
- Default: null

Size of the disk in bytes. Required if creating a new disk file.
<a id="ADDED_fields_attributes_oneOf_i4_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i4_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i4_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i4_logical_sectorsize"></a>
<a id="ADDED_fields_attributes_oneOf_i4_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="ADDED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i4_physical_sectorsize"></a>
<a id="ADDED_fields_attributes_oneOf_i4_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="ADDED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i4_iotype"></a>
<a id="ADDED_fields_attributes_oneOf_i4_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingADDED_fields_attributes_oneOf_i4_serial"></a>
<a id="ADDED_fields_attributes_oneOf_i4_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="ADDED_fields_attributes_oneOf_i4_serial_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i4_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i4_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i4_serial_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5"></a>
###### [VMDiskDevice](#tab-pane_ADDED_fields_attributes_oneOf_i5)

- Schema name: `VMDiskDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i5_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i5_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for virtual disk devices.
- Specific value: `"DISK"`

<a id="headingADDED_fields_attributes_oneOf_i5_path"></a>
<a id="ADDED_fields_attributes_oneOf_i5_path"></a>
###### path

- Schema name: `Path`
- Default: null

Path to existing disk file or ZFS volume. `null` if creating a new ZFS volume.
<a id="ADDED_fields_attributes_oneOf_i5_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i5_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i5_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i5_type"></a>
<a id="ADDED_fields_attributes_oneOf_i5_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingADDED_fields_attributes_oneOf_i5_create_zvol"></a>
<a id="ADDED_fields_attributes_oneOf_i5_create_zvol"></a>
###### create_zvol

- Schema name: `Create Zvol`
- Type: boolean
- Default: false

Whether to create a new ZFS volume for this disk.

<a id="headingADDED_fields_attributes_oneOf_i5_zvol_name"></a>
<a id="ADDED_fields_attributes_oneOf_i5_zvol_name"></a>
###### zvol_name

- Schema name: `Zvol Name`
- Default: null

Name for the new ZFS volume. Required if `create_zvol` is true.
<a id="ADDED_fields_attributes_oneOf_i5_zvol_name_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_name_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_name_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i5_zvol_volsize"></a>
<a id="ADDED_fields_attributes_oneOf_i5_zvol_volsize"></a>
###### zvol_volsize

- Schema name: `Zvol Volsize`
- Default: null

Size of the new ZFS volume in bytes. Required if `create_zvol` is true.
<a id="ADDED_fields_attributes_oneOf_i5_zvol_volsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i5_logical_sectorsize"></a>
<a id="ADDED_fields_attributes_oneOf_i5_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="ADDED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i5_physical_sectorsize"></a>
<a id="ADDED_fields_attributes_oneOf_i5_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="ADDED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i5_iotype"></a>
<a id="ADDED_fields_attributes_oneOf_i5_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingADDED_fields_attributes_oneOf_i5_serial"></a>
<a id="ADDED_fields_attributes_oneOf_i5_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="ADDED_fields_attributes_oneOf_i5_serial_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i5_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i5_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i5_serial_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_attributes_oneOf_i6"></a>
###### [VMUSBDevice](#tab-pane_ADDED_fields_attributes_oneOf_i6)

- Schema name: `VMUSBDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i6_dtype"></a>
<a id="ADDED_fields_attributes_oneOf_i6_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingADDED_fields_attributes_oneOf_i6_usb"></a>
<a id="ADDED_fields_attributes_oneOf_i6_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="ADDED_fields_attributes_oneOf_i6_usb_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i6_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_ADDED_fields_attributes_oneOf_i6_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_attributes_oneOf_i6_usb_anyOf_i0_vendor_id"></a>
<a id="ADDED_fields_attributes_oneOf_i6_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingADDED_fields_attributes_oneOf_i6_usb_anyOf_i0_product_id"></a>
<a id="ADDED_fields_attributes_oneOf_i6_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i6_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i6_usb_anyOf_i1)

- Type: null

<a id="headingADDED_fields_attributes_oneOf_i6_controller_type"></a>
<a id="ADDED_fields_attributes_oneOf_i6_controller_type"></a>
###### controller_type

- Schema name: `Controller Type`
- Type: enum (of string)
- Default: "nec-xhci"

USB controller type for the virtual machine.
###### Must be one of:

- "piix3-uhci"
- "piix4-uhci"
- "ehci"
- "ich9-ehci1"
- "vt82c686b-uhci"
- "pci-ohci"
- "nec-xhci"
- "qemu-xhci"

<a id="headingADDED_fields_attributes_oneOf_i6_device"></a>
<a id="ADDED_fields_attributes_oneOf_i6_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="ADDED_fields_attributes_oneOf_i6_device_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_attributes_oneOf_i6_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_attributes_oneOf_i6_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_attributes_oneOf_i6_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_attributes_oneOf_i6_device_anyOf_i1)

- Type: null

<a id="headingADDED_fields_vm"></a>
<a id="ADDED_fields_vm"></a>
##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

<a id="headingADDED_fields_order"></a>
<a id="ADDED_fields_order"></a>
##### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `VMDeviceChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

<a id="headingCHANGED_fields_attributes"></a>
<a id="CHANGED_fields_attributes"></a>
##### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="CHANGED_fields_attributes_oneOf"></a>
###### One of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i0"></a>
###### [VMCDROMDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i0)

- Schema name: `VMCDROMDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i0_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for CD-ROM/DVD devices.
- Specific value: `"CDROM"`

<a id="headingCHANGED_fields_attributes_oneOf_i0_path"></a>
<a id="CHANGED_fields_attributes_oneOf_i0_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Path must not contain "{", "}" characters, and it should start with "/mnt/".
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1"></a>
###### [VMDisplayDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i1)

- Schema name: `VMDisplayDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i1_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.
- Specific value: `"DISPLAY"`

<a id="headingCHANGED_fields_attributes_oneOf_i1_resolution"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_resolution"></a>
###### resolution

- Schema name: `Resolution`
- Type: enum (of string)
- Default: "1024x768"

Screen resolution for the virtual display.
###### Must be one of:

- "1920x1200"
- "1920x1080"
- "1600x1200"
- "1600x900"
- "1400x1050"
- "1280x1024"
- "1280x720"
- "1024x768"
- "800x600"
- "640x480"

<a id="headingCHANGED_fields_attributes_oneOf_i1_port"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_port"></a>
###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
<a id="CHANGED_fields_attributes_oneOf_i1_port_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i1_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i1_port_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i1_web_port"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_web_port"></a>
###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
<a id="CHANGED_fields_attributes_oneOf_i1_web_port_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1_web_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i1_web_port_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1_web_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i1_web_port_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i1_bind"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_bind"></a>
###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_attributes_oneOf_i1_wait"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_wait"></a>
###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

<a id="headingCHANGED_fields_attributes_oneOf_i1_password"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_password"></a>
###### password

- Schema name: `Password`
- Default: null

Password for display server authentication.
<a id="CHANGED_fields_attributes_oneOf_i1_password_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i1_password_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i1_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i1_password_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i1_web"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_web"></a>
###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

<a id="headingCHANGED_fields_attributes_oneOf_i1_type"></a>
<a id="CHANGED_fields_attributes_oneOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.
###### Must be one of:

- "SPICE"
- "VNC"

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i2"></a>
###### [VMNICDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i2)

- Schema name: `VMNICDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i2_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingCHANGED_fields_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="CHANGED_fields_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingCHANGED_fields_attributes_oneOf_i2_type"></a>
<a id="CHANGED_fields_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingCHANGED_fields_attributes_oneOf_i2_nic_attach"></a>
<a id="CHANGED_fields_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="CHANGED_fields_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i2_mac"></a>
<a id="CHANGED_fields_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="CHANGED_fields_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i3"></a>
###### [VMPCIDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i3)

- Schema name: `VMPCIDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i3_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for PCI passthrough devices.
- Specific value: `"PCI"`

<a id="headingCHANGED_fields_attributes_oneOf_i3_pptdev"></a>
<a id="CHANGED_fields_attributes_oneOf_i3_pptdev"></a>
###### pptdev (required)

- Schema name: `Pptdev`
- Type: string

Host PCI device identifier to pass through to the VM.
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4"></a>
###### [VMRAWDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i4)

- Schema name: `VMRAWDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i4_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for raw disk devices.
- Specific value: `"RAW"`

<a id="headingCHANGED_fields_attributes_oneOf_i4_path"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to the raw disk device or image file.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingCHANGED_fields_attributes_oneOf_i4_type"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingCHANGED_fields_attributes_oneOf_i4_exists"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_exists"></a>
###### exists

- Schema name: `Exists`
- Type: boolean
- Default: false

Whether the disk file already exists or should be created.

<a id="headingCHANGED_fields_attributes_oneOf_i4_boot"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_boot"></a>
###### boot

- Schema name: `Boot`
- Type: boolean
- Default: false

Whether this disk should be marked as bootable.

<a id="headingCHANGED_fields_attributes_oneOf_i4_size"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_size"></a>
###### size

- Schema name: `Size`
- Default: null

Size of the disk in bytes. Required if creating a new disk file.
<a id="CHANGED_fields_attributes_oneOf_i4_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i4_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i4_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i4_logical_sectorsize"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="CHANGED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i4_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i4_physical_sectorsize"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="CHANGED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i4_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i4_iotype"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingCHANGED_fields_attributes_oneOf_i4_serial"></a>
<a id="CHANGED_fields_attributes_oneOf_i4_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="CHANGED_fields_attributes_oneOf_i4_serial_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i4_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i4_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i4_serial_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5"></a>
###### [VMDiskDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i5)

- Schema name: `VMDiskDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i5_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for virtual disk devices.
- Specific value: `"DISK"`

<a id="headingCHANGED_fields_attributes_oneOf_i5_path"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_path"></a>
###### path

- Schema name: `Path`
- Default: null

Path to existing disk file or ZFS volume. `null` if creating a new ZFS volume.
<a id="CHANGED_fields_attributes_oneOf_i5_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i5_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i5_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i5_type"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingCHANGED_fields_attributes_oneOf_i5_create_zvol"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_create_zvol"></a>
###### create_zvol

- Schema name: `Create Zvol`
- Type: boolean
- Default: false

Whether to create a new ZFS volume for this disk.

<a id="headingCHANGED_fields_attributes_oneOf_i5_zvol_name"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_zvol_name"></a>
###### zvol_name

- Schema name: `Zvol Name`
- Default: null

Name for the new ZFS volume. Required if `create_zvol` is true.
<a id="CHANGED_fields_attributes_oneOf_i5_zvol_name_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_name_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_name_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i5_zvol_volsize"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_zvol_volsize"></a>
###### zvol_volsize

- Schema name: `Zvol Volsize`
- Default: null

Size of the new ZFS volume in bytes. Required if `create_zvol` is true.
<a id="CHANGED_fields_attributes_oneOf_i5_zvol_volsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i5_zvol_volsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i5_logical_sectorsize"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="CHANGED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i5_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i5_physical_sectorsize"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="CHANGED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i5_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i5_iotype"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingCHANGED_fields_attributes_oneOf_i5_serial"></a>
<a id="CHANGED_fields_attributes_oneOf_i5_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="CHANGED_fields_attributes_oneOf_i5_serial_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i5_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i5_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i5_serial_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i6"></a>
###### [VMUSBDevice](#tab-pane_CHANGED_fields_attributes_oneOf_i6)

- Schema name: `VMUSBDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i6_dtype"></a>
<a id="CHANGED_fields_attributes_oneOf_i6_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingCHANGED_fields_attributes_oneOf_i6_usb"></a>
<a id="CHANGED_fields_attributes_oneOf_i6_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="CHANGED_fields_attributes_oneOf_i6_usb_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i6_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_CHANGED_fields_attributes_oneOf_i6_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_attributes_oneOf_i6_usb_anyOf_i0_vendor_id"></a>
<a id="CHANGED_fields_attributes_oneOf_i6_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingCHANGED_fields_attributes_oneOf_i6_usb_anyOf_i0_product_id"></a>
<a id="CHANGED_fields_attributes_oneOf_i6_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i6_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i6_usb_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_attributes_oneOf_i6_controller_type"></a>
<a id="CHANGED_fields_attributes_oneOf_i6_controller_type"></a>
###### controller_type

- Schema name: `Controller Type`
- Type: enum (of string)
- Default: "nec-xhci"

USB controller type for the virtual machine.
###### Must be one of:

- "piix3-uhci"
- "piix4-uhci"
- "ehci"
- "ich9-ehci1"
- "vt82c686b-uhci"
- "pci-ohci"
- "nec-xhci"
- "qemu-xhci"

<a id="headingCHANGED_fields_attributes_oneOf_i6_device"></a>
<a id="CHANGED_fields_attributes_oneOf_i6_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="CHANGED_fields_attributes_oneOf_i6_device_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i6_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_attributes_oneOf_i6_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_attributes_oneOf_i6_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_attributes_oneOf_i6_device_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_vm"></a>
<a id="CHANGED_fields_vm"></a>
##### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

<a id="headingCHANGED_fields_order"></a>
<a id="CHANGED_fields_order"></a>
##### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `VMDeviceRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
