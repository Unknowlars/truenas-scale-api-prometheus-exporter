---
title: vm.update
kind: method
source_rst: _sources/api_methods_vm.update.rst.txt
source_html: api_methods_vm.update.html
required_roles:
  - VM_WRITE
---

# vm.update

## Summary

Update all information of a specific VM.

`devices` is a list of virtualized hardware to attach to the virtual machine. If `devices` is not present, no change is made to devices. If either the device list order or data stored by the device changes when the attribute is passed, these actions are taken:

1) If there is no device in the `devices` list which was previously attached to the VM, that device is removed from the virtual machine. 2) Devices are updated in the `devices` list when they contain a valid `id` attribute that corresponds to an existing device. 3) Devices that do not have an `id` attribute are created and attached to `id` VM.

## Required Roles

- `VM_WRITE`

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

ID of the virtual machine to update.

#### Parameter 2: vm_update

#### vm_update

- Schema name: `vm_update`
- Type: object

Updated configuration for the virtual machine.
- No Additional Properties
##### command_line_args

- Schema name: `Command Line Args`
- Type: string

Additional command line arguments passed to the VM hypervisor.

##### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.

##### cpu_model

- Schema name: `Cpu Model`

Specific CPU model to emulate. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### name

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

##### description

- Schema name: `Description`
- Type: string

Optional description or notes about the virtual machine.

##### vcpus

- Schema name: `Vcpus`
- Type: integer

Number of virtual CPUs allocated to the VM.
- Value must be greater or equal to `1`

##### cores

- Schema name: `Cores`
- Type: integer

Number of CPU cores per socket.
- Value must be greater or equal to `1`

##### threads

- Schema name: `Threads`
- Type: integer

Number of threads per CPU core.
- Value must be greater or equal to `1`

##### cpuset

- Schema name: `Cpuset`

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### nodeset

- Schema name: `Nodeset`

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean

Whether to expose detailed CPU topology information to the guest OS.

##### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

##### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean

Whether to suspend the VM when taking snapshots.

##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

##### memory

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in megabytes.
- Value must be greater or equal to `20`

##### min_memory

- Schema name: `Min Memory`

Minimum memory allocation for dynamic memory ballooning in megabytes. Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `20`

####### Option 2

- Type: null

##### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

##### autostart

- Schema name: `Autostart`
- Type: boolean

Whether to automatically start the VM when the host system boots.

##### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean

Whether to hide hypervisor signatures from guest OS MSR access.

##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean

Whether to ensure at least one display device is configured for the VM.

##### time

- Schema name: `Time`
- Type: enum (of string)

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.

##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

##### arch_type

- Schema name: `Arch Type`

Guest architecture type. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### machine_type

- Schema name: `Machine Type`

Virtual machine type/chipset. `null` to use hypervisor default.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### uuid

- Schema name: `Uuid`

Unique UUID for the VM. `null` to auto-generate.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `VMEntry`
- Type: object

The updated virtual machine configuration.
- No Additional Properties
#### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor.

#### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.

#### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

#### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

#### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPUs allocated to the VM.
- Value must be greater or equal to `1`

#### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

#### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

#### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

#### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

#### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: false

Whether to suspend the VM when taking snapshots.

#### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

#### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in megabytes.
- Value must be greater or equal to `20`

#### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in megabytes. Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `20`

###### Option 2

- Type: null

#### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

#### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

#### bootloader_ovmf

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

#### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

#### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide hypervisor signatures from guest OS MSR access.

#### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure at least one display device is configured for the VM.

#### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.

#### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

#### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### uuid

- Schema name: `Uuid`
- Default: null

Unique UUID for the VM. `null` to auto-generate.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

##### Each item of this array must be:

##### VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.

###### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

###### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

#### display_available (required)

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

#### status (required)

- Schema name: `VMStatus`
- Type: object

Current runtime status information for the VM.
- No Additional Properties
##### state

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

##### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### domain_state (required)

- Schema name: `Domain State`
- Type: string

Hypervisor-specific domain state.
- Must be at least `1` characters long

#### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
