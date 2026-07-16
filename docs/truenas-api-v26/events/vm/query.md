---
title: vm.query
kind: event
source_rst: _sources/api_events_vm.query.rst.txt
source_html: api_events_vm.query.html
required_roles:
  - VM_READ
---

# vm.query

## Summary

Sent on vm changes.

## Required Roles

- `VM_READ`

## Schema

- Type: object

### ADDED

- Schema name: `VMAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `VMEntry`
- Type: object
- No Additional Properties
##### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor.

##### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.

##### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

##### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPU sockets. The total number of guest vCPUs is `vcpus` * `cores` * `threads` (maximum 16).
- Value must be greater or equal to `1`

##### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

##### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

##### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

##### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

##### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: true

Whether to automatically suspend the VM when a periodic snapshot task runs. For manual snapshots, the VM is suspended only if explicitly included in the snapshot's VM pause list.

##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

##### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in mebibytes (MiB).
- Value must be greater or equal to `20`

##### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in mebibytes (MiB). Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `20`

####### Option 2

- Type: null

##### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

##### bootloader_ovmf

- Schema name: `Bootloader Ovmf`
- Type: string
- Default: "OVMF_CODE.fd"

OVMF firmware file to use for UEFI boot.
Examples:

```json
"OVMF_CODE.fd"
```
Examples:

```json
"OVMF_CODE.secboot.fd"
```

##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

##### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide the KVM hypervisor from standard MSR-based discovery. Useful when doing GPU passthrough.

##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure the guest always has access to a video device. Required for headless OS installations (e.g. Ubuntu Server). Set to `false` when using GPU passthrough without a separate display device.

##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.

##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

##### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique UUID for the VM.

##### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

###### Each item of this array must be:

###### VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

####### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

####### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

####### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

##### display_available (required)

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

##### status (required)

- Schema name: `VMStatus`
- Type: object

Current runtime status information for the VM.
- No Additional Properties
###### state (required)

- Schema name: `State`
- Type: string

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

###### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

##### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

### CHANGED

- Schema name: `VMChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `VMEntry`
- Type: object
- No Additional Properties
##### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor.

##### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.

##### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

##### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPU sockets. The total number of guest vCPUs is `vcpus` * `cores` * `threads` (maximum 16).
- Value must be greater or equal to `1`

##### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

##### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

##### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

##### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

##### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: true

Whether to automatically suspend the VM when a periodic snapshot task runs. For manual snapshots, the VM is suspended only if explicitly included in the snapshot's VM pause list.

##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

##### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in mebibytes (MiB).
- Value must be greater or equal to `20`

##### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in mebibytes (MiB). Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `20`

####### Option 2

- Type: null

##### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

##### bootloader_ovmf

- Schema name: `Bootloader Ovmf`
- Type: string
- Default: "OVMF_CODE.fd"

OVMF firmware file to use for UEFI boot.
Examples:

```json
"OVMF_CODE.fd"
```
Examples:

```json
"OVMF_CODE.secboot.fd"
```

##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

##### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide the KVM hypervisor from standard MSR-based discovery. Useful when doing GPU passthrough.

##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure the guest always has access to a video device. Required for headless OS installations (e.g. Ubuntu Server). Set to `false` when using GPU passthrough without a separate display device.

##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.

##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

##### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique UUID for the VM.

##### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

###### Each item of this array must be:

###### VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

####### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

####### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

####### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

##### display_available (required)

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

##### status (required)

- Schema name: `VMStatus`
- Type: object

Current runtime status information for the VM.
- No Additional Properties
###### state (required)

- Schema name: `State`
- Type: string

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

###### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

##### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

### REMOVED

- Schema name: `VMRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
