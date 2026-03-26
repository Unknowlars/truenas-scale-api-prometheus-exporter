---
title: vm.create
kind: method
source_rst: _sources/api_methods_vm.create.rst.txt
source_html: api_methods_vm.create.html
required_roles:
  - VM_WRITE
---

# vm.create

## Summary

Create a Virtual Machine (VM).

Maximum of 16 guest virtual CPUs are allowed. By default, every virtual CPU is configured as a separate package. Multiple cores can be configured per CPU by specifying `cores` attributes. `vcpus` specifies total number of CPU sockets. `cores` specifies number of cores per socket. `threads` specifies number of threads per core.

`ensure_display_device` when set ( the default ) will ensure that the guest always has access to a video device. For headless installations like ubuntu server this is required for the guest to operate properly. However for cases where consumer would like to use GPU passthrough and does not want a display device added should set this to `false`.

`arch_type` refers to architecture type and can be specified for the guest. By default the value is `null` and system in this case will choose a reasonable default based on host.

`machine_type` refers to machine type of the guest based on the architecture type selected with `arch_type`. By default the value is `null` and system in this case will choose a reasonable default based on `arch_type` configuration.

`shutdown_timeout` indicates the time in seconds the system waits for the VM to cleanly shutdown. During system shutdown, if the VM hasn't exited after a hardware shutdown signal has been sent by the system within `shutdown_timeout` seconds, system initiates poweroff for the VM to stop it.

`hide_from_msr` is a boolean which when set will hide the KVM hypervisor from standard MSR based discovery and is useful to enable when doing GPU passthrough.

`hyperv_enlightenments` can be used to enable subset of predefined Hyper-V enlightenments for Windows guests. These enlightenments improve performance and enable otherwise missing features.

`suspend_on_snapshot` is a boolean attribute which when enabled will automatically pause/suspend VMs when a snapshot is being taken for periodic snapshot tasks. For manual snapshots, if user has specified vms to be paused, they will be in that case.

## Required Roles

- `VM_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_create

#### vm_create

- Schema name: `vm_create`
- Type: object

VMCreateArgs parameters.
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

Number of virtual CPUs allocated to the VM.
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
- Default: false

Whether to suspend the VM when taking snapshots.

##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

##### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in megabytes.
- Value must be greater or equal to `20`

##### min_memory

- Schema name: `Min Memory`
- Default: null

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
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.

##### bootloader_ovmf

- Schema name: `Bootloader Ovmf`
- Default: null

OVMF firmware file to use for UEFI boot.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

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

Whether to hide hypervisor signatures from guest OS MSR access.

##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure at least one display device is configured for the VM.

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

##### uuid

- Schema name: `Uuid`
- Default: null

Unique UUID for the VM. `null` to auto-generate.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

### Return value

- Schema name: `VMEntry`
- Type: object

The newly created virtual machine configuration.
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
