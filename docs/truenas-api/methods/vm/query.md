---
title: vm.query
kind: method
source_rst: _sources/api_methods_vm.query.rst.txt
source_html: api_methods_vm.query.html
required_roles:
  - VM_READ
---

# vm.query

## Required Roles

- `VM_READ`

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

###### VMQueryResultItem

- Schema name: `VMQueryResultItem`
- Type: object
- No Additional Properties
####### command_line_args

- Schema name: `Command Line Args`
- Type: string

Additional command line arguments passed to the VM hypervisor.

####### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.

####### cpu_model

- Schema name: `Cpu Model`

Specific CPU model to emulate. `null` to use hypervisor default.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### name

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

####### description

- Schema name: `Description`
- Type: string

Optional description or notes about the virtual machine.

####### vcpus

- Schema name: `Vcpus`
- Type: integer

Number of virtual CPUs allocated to the VM.
- Value must be greater or equal to `1`

####### cores

- Schema name: `Cores`
- Type: integer

Number of CPU cores per socket.
- Value must be greater or equal to `1`

####### threads

- Schema name: `Threads`
- Type: integer

Number of threads per CPU core.
- Value must be greater or equal to `1`

####### cpuset

- Schema name: `Cpuset`

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### nodeset

- Schema name: `Nodeset`

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean

Whether to expose detailed CPU topology information to the guest OS.

####### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

####### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean

Whether to suspend the VM when taking snapshots.

####### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

####### memory

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in megabytes.
- Value must be greater or equal to `20`

####### min_memory

- Schema name: `Min Memory`

Minimum memory allocation for dynamic memory ballooning in megabytes. Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
######## Any of

######### Option 1

- Type: integer
- Value must be greater or equal to `20`

######### Option 2

- Type: null

####### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

####### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

####### bootloader_ovmf

- Schema name: `Bootloader Ovmf`
- Type: string

OVMF firmware file to use for UEFI boot.
Examples:

```json
"OVMF_CODE.fd"
```
Examples:

```json
"OVMF_CODE.secboot.fd"
```

####### autostart

- Schema name: `Autostart`
- Type: boolean

Whether to automatically start the VM when the host system boots.

####### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean

Whether to hide hypervisor signatures from guest OS MSR access.

####### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean

Whether to ensure at least one display device is configured for the VM.

####### time

- Schema name: `Time`
- Type: enum (of string)

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.

####### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

####### arch_type

- Schema name: `Arch Type`

Guest architecture type. `null` to use hypervisor default.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### machine_type

- Schema name: `Machine Type`

Virtual machine type/chipset. `null` to use hypervisor default.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### uuid

- Schema name: `Uuid`

Unique UUID for the VM. `null` to auto-generate.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### devices

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

######## Each item of this array must be:

######## VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
######### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

######### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

######### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

######### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

####### display_available

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

####### id

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

####### status

- Schema name: `VMStatus`
- Type: object

Current runtime status information for the VM.
- No Additional Properties
######## state

- Schema name: `State`
- Type: string
- Default: "127.0.0.1"

Current state of the virtual machine.
- Must be at least `1` characters long
Examples:

```json
"RUNNING"
```
Examples:

```json
"STOPPED"
```
Examples:

```json
"SUSPENDED"
```

######## pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## domain_state (required)

- Schema name: `Domain State`
- Type: string

Hypervisor-specific domain state.
- Must be at least `1` characters long

####### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean

Whether to enable UEFI Secure Boot for enhanced security.

##### VMQueryResultItem

- Type: string

##### Option 3

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `20`

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `VMCDROMDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for CD-ROM/DVD devices.

###### path

- Schema name: `Path`
- Type: string
- Default: "*"

Path must not contain "{", "}" characters, and it should start with "/mnt/".
- Must be at least `1` characters long

##### Option 2

- Schema name: `VMDisplayDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.

###### resolution

- Schema name: `Resolution`
- Type: enum (of string)
- Default: "1024x768"

Screen resolution for the virtual display.

###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

######## Option 2

- Type: null

###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

###### password

- Schema name: `Password`
- Default: null

Password for display server authentication.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.

##### VMCDROMDevice

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

##### VMDisplayDevice

- Type: null

##### VMNICDevice

- Type: integer

##### VMPCIDevice

- Type: null

##### VMRAWDevice

- Type: string

##### VMDiskDevice

- Type: null

##### VMUSBDevice

- Schema name: `VMNICDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.

###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.

###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `VMPCIDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for PCI passthrough devices.

###### pptdev (required)

- Schema name: `Pptdev`
- Type: string

Host PCI device identifier to pass through to the VM.
- Must be at least `1` characters long

##### Option 2

- Schema name: `VMRAWDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for raw disk devices.

###### path

- Schema name: `Path`
- Type: string
- Default: "127.0.0.1"

Path must not contain "{", "}" characters.
- Must be at least `1` characters long

###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.

###### exists

- Schema name: `Exists`
- Type: boolean
- Default: false

Whether the disk file already exists or should be created.

###### boot

- Schema name: `Boot`
- Type: boolean
- Default: false

Whether this disk should be marked as bootable.

###### size

- Schema name: `Size`
- Default: null

Size of the disk in bytes. Required if creating a new disk file.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
####### Any of

######## Option 1

- Type: enum (of integer or null)

######## Option 2

- Type: null

###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
####### Any of

######## Option 1

- Type: enum (of integer or null)

######## Option 2

- Type: null

###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.

###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: enum (of integer or null)

##### Option 2

- Type: null

##### Option 1

- Type: enum (of integer or null)

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Schema name: `VMDiskDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for virtual disk devices.

###### path

- Schema name: `Path`
- Default: null

Path to existing disk file or ZFS volume. `null` if creating a new ZFS volume.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.

###### create_zvol

- Schema name: `Create Zvol`
- Type: boolean
- Default: false

Whether to create a new ZFS volume for this disk.

###### zvol_name

- Schema name: `Zvol Name`
- Default: null

Name for the new ZFS volume. Required if `create_zvol` is true.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### zvol_volsize

- Schema name: `Zvol Volsize`
- Default: null

Size of the new ZFS volume in bytes. Required if `create_zvol` is true.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
####### Any of

######## Option 1

- Type: enum (of integer or null)

######## Option 2

- Type: null

###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
####### Any of

######## Option 1

- Type: enum (of integer or null)

######## Option 2

- Type: null

###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.

###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

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

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: enum (of integer or null)

##### Option 1

- Type: null

##### Option 2

- Type: enum (of integer or null)

##### Option 1

- Type: null

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Schema name: `VMUSBDevice`
- Type: object
- No Additional Properties
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.

###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
####### Any of

######## USBAttributes

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
######### vendor_id

- Schema name: `Vendor Id`
- Type: string
- Default: "127.0.0.1"

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must be at least `1` characters long

######### product_id

- Schema name: `Product Id`
- Type: string
- Default: "127.0.0.1"

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must be at least `1` characters long

######## Option 2

- Type: null

###### controller_type

- Schema name: `Controller Type`
- Type: enum (of string)
- Default: "nec-xhci"

USB controller type for the virtual machine.

###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

##### Option 1

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
###### vendor_id

- Schema name: `Vendor Id`
- Type: string
- Default: "127.0.0.1"

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must be at least `1` characters long

###### product_id

- Schema name: `Product Id`
- Type: string
- Default: "127.0.0.1"

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must be at least `1` characters long

##### Option 2

- Type: null

##### USBAttributes

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Schema name: `VMQueryResultItem`
- Type: object
- No Additional Properties
###### command_line_args

- Schema name: `Command Line Args`
- Type: string

Additional command line arguments passed to the VM hypervisor.

###### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.

###### cpu_model

- Schema name: `Cpu Model`

Specific CPU model to emulate. `null` to use hypervisor default.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### name

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

###### description

- Schema name: `Description`
- Type: string

Optional description or notes about the virtual machine.

###### vcpus

- Schema name: `Vcpus`
- Type: integer

Number of virtual CPUs allocated to the VM.
- Value must be greater or equal to `1`

###### cores

- Schema name: `Cores`
- Type: integer

Number of CPU cores per socket.
- Value must be greater or equal to `1`

###### threads

- Schema name: `Threads`
- Type: integer

Number of threads per CPU core.
- Value must be greater or equal to `1`

###### cpuset

- Schema name: `Cpuset`

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### nodeset

- Schema name: `Nodeset`

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean

Whether to expose detailed CPU topology information to the guest OS.

###### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

###### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean

Whether to suspend the VM when taking snapshots.

###### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

###### memory

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in megabytes.
- Value must be greater or equal to `20`

###### min_memory

- Schema name: `Min Memory`

Minimum memory allocation for dynamic memory ballooning in megabytes. Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `20`

######## Option 2

- Type: null

###### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

###### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

###### bootloader_ovmf

- Schema name: `Bootloader Ovmf`
- Type: string

OVMF firmware file to use for UEFI boot.
Examples:

```json
"OVMF_CODE.fd"
```
Examples:

```json
"OVMF_CODE.secboot.fd"
```

###### autostart

- Schema name: `Autostart`
- Type: boolean

Whether to automatically start the VM when the host system boots.

###### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean

Whether to hide hypervisor signatures from guest OS MSR access.

###### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean

Whether to ensure at least one display device is configured for the VM.

###### time

- Schema name: `Time`
- Type: enum (of string)

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.

###### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

###### arch_type

- Schema name: `Arch Type`

Guest architecture type. `null` to use hypervisor default.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### machine_type

- Schema name: `Machine Type`

Virtual machine type/chipset. `null` to use hypervisor default.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### uuid

- Schema name: `Uuid`

Unique UUID for the VM. `null` to auto-generate.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### devices

- Schema name: `Devices`
- Type: array

Array of virtual devices attached to this VM.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### display_available

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

###### status

- Type: object

Current runtime status information for the VM.

###### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean

Whether to enable UEFI Secure Boot for enhanced security.

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `20`

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
