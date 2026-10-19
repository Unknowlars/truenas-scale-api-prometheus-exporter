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

A maximum of 16 guest virtual CPUs are allowed. The CPU topology is configured through the `vcpus`, `cores`, and `threads` attributes.

## Required Roles

- `VM_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_create

<a id="Call_parameters_items_i0"></a>
#### vm_create

- Schema name: `vm_create`
- Type: object

VMCreateArgs parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i0_command_line_args"></a>
<a id="Call_parameters_items_i0_command_line_args"></a>
##### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor.

<a id="headingCall_parameters_items_i0_cpu_mode"></a>
<a id="Call_parameters_items_i0_cpu_mode"></a>
##### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.
###### Must be one of:

- "CUSTOM"
- "HOST-MODEL"
- "HOST-PASSTHROUGH"

<a id="headingCall_parameters_items_i0_cpu_model"></a>
<a id="Call_parameters_items_i0_cpu_model"></a>
##### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
<a id="Call_parameters_items_i0_cpu_model_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_cpu_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_cpu_model_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_cpu_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_cpu_model_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i0_description"></a>
<a id="Call_parameters_items_i0_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

<a id="headingCall_parameters_items_i0_vcpus"></a>
<a id="Call_parameters_items_i0_vcpus"></a>
##### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPUs allocated to the VM.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_cores"></a>
<a id="Call_parameters_items_i0_cores"></a>
##### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_threads"></a>
<a id="Call_parameters_items_i0_threads"></a>
##### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

<a id="headingCall_parameters_items_i0_cpuset"></a>
<a id="Call_parameters_items_i0_cpuset"></a>
##### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
<a id="Call_parameters_items_i0_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_cpuset_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_nodeset"></a>
<a id="Call_parameters_items_i0_nodeset"></a>
##### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
<a id="Call_parameters_items_i0_nodeset_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_nodeset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_nodeset_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_nodeset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_nodeset_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_enable_cpu_topology_extension"></a>
<a id="Call_parameters_items_i0_enable_cpu_topology_extension"></a>
##### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

<a id="headingCall_parameters_items_i0_pin_vcpus"></a>
<a id="Call_parameters_items_i0_pin_vcpus"></a>
##### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

<a id="headingCall_parameters_items_i0_suspend_on_snapshot"></a>
<a id="Call_parameters_items_i0_suspend_on_snapshot"></a>
##### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: true

Whether to suspend the VM when taking snapshots.

<a id="headingCall_parameters_items_i0_trusted_platform_module"></a>
<a id="Call_parameters_items_i0_trusted_platform_module"></a>
##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

<a id="headingCall_parameters_items_i0_memory"></a>
<a id="Call_parameters_items_i0_memory"></a>
##### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in mebibytes (MiB).
- Value must be greater or equal to `20`

<a id="headingCall_parameters_items_i0_min_memory"></a>
<a id="Call_parameters_items_i0_min_memory"></a>
##### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in mebibytes (MiB). Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
<a id="Call_parameters_items_i0_min_memory_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_min_memory_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_min_memory_anyOf_i0)

- Type: integer
- Value must be greater or equal to `20`

<a id="tab-pane_Call_parameters_items_i0_min_memory_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_min_memory_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_hyperv_enlightenments"></a>
<a id="Call_parameters_items_i0_hyperv_enlightenments"></a>
##### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

<a id="headingCall_parameters_items_i0_bootloader"></a>
<a id="Call_parameters_items_i0_bootloader"></a>
##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.
###### Must be one of:

- "UEFI_CSM"
- "UEFI"

<a id="headingCall_parameters_items_i0_bootloader_ovmf"></a>
<a id="Call_parameters_items_i0_bootloader_ovmf"></a>
##### bootloader_ovmf

- Schema name: `Bootloader Ovmf`
- Default: null

OVMF firmware file to use for UEFI boot.
<a id="Call_parameters_items_i0_bootloader_ovmf_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_bootloader_ovmf_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_bootloader_ovmf_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_bootloader_ovmf_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_bootloader_ovmf_anyOf_i1)

- Type: null

Examples:

```json
"OVMF_CODE.fd"
```
Examples:

```json
"OVMF_CODE.secboot.fd"
```

<a id="headingCall_parameters_items_i0_autostart"></a>
<a id="Call_parameters_items_i0_autostart"></a>
##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

<a id="headingCall_parameters_items_i0_hide_from_msr"></a>
<a id="Call_parameters_items_i0_hide_from_msr"></a>
##### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide hypervisor signatures from guest OS MSR access.

<a id="headingCall_parameters_items_i0_ensure_display_device"></a>
<a id="Call_parameters_items_i0_ensure_display_device"></a>
##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure at least one display device is configured for the VM.

<a id="headingCall_parameters_items_i0_time"></a>
<a id="Call_parameters_items_i0_time"></a>
##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingCall_parameters_items_i0_shutdown_timeout"></a>
<a id="Call_parameters_items_i0_shutdown_timeout"></a>
##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingCall_parameters_items_i0_arch_type"></a>
<a id="Call_parameters_items_i0_arch_type"></a>
##### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
<a id="Call_parameters_items_i0_arch_type_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_arch_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_arch_type_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_arch_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_arch_type_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_machine_type"></a>
<a id="Call_parameters_items_i0_machine_type"></a>
##### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
<a id="Call_parameters_items_i0_machine_type_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_machine_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_machine_type_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_machine_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_machine_type_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_uuid"></a>
<a id="Call_parameters_items_i0_uuid"></a>
##### uuid

- Schema name: `Uuid`
- Default: null

Unique UUID for the VM. `null` to auto-generate. Normalized to lowercase hyphenated form.
<a id="Call_parameters_items_i0_uuid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_uuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_uuid_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_uuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_uuid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_enable_secure_boot"></a>
<a id="Call_parameters_items_i0_enable_secure_boot"></a>
##### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMEntry`
- Type: object

The newly created virtual machine configuration.
- No Additional Properties
<a id="headingReturn_value_command_line_args"></a>
<a id="Return_value_command_line_args"></a>
#### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor.

<a id="headingReturn_value_cpu_mode"></a>
<a id="Return_value_cpu_mode"></a>
#### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.
##### Must be one of:

- "CUSTOM"
- "HOST-MODEL"
- "HOST-PASSTHROUGH"

<a id="headingReturn_value_cpu_model"></a>
<a id="Return_value_cpu_model"></a>
#### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
<a id="Return_value_cpu_model_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_cpu_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_cpu_model_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_cpu_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_cpu_model_anyOf_i1)

- Type: null

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

<a id="headingReturn_value_vcpus"></a>
<a id="Return_value_vcpus"></a>
#### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPUs allocated to the VM.
- Value must be greater or equal to `1`

<a id="headingReturn_value_cores"></a>
<a id="Return_value_cores"></a>
#### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

<a id="headingReturn_value_threads"></a>
<a id="Return_value_threads"></a>
#### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

<a id="headingReturn_value_cpuset"></a>
<a id="Return_value_cpuset"></a>
#### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
<a id="Return_value_cpuset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_cpuset_anyOf_i1)

- Type: null

<a id="headingReturn_value_nodeset"></a>
<a id="Return_value_nodeset"></a>
#### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
<a id="Return_value_nodeset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nodeset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nodeset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_nodeset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nodeset_anyOf_i1)

- Type: null

<a id="headingReturn_value_enable_cpu_topology_extension"></a>
<a id="Return_value_enable_cpu_topology_extension"></a>
#### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

<a id="headingReturn_value_pin_vcpus"></a>
<a id="Return_value_pin_vcpus"></a>
#### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

<a id="headingReturn_value_suspend_on_snapshot"></a>
<a id="Return_value_suspend_on_snapshot"></a>
#### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: true

Whether to suspend the VM when taking snapshots.

<a id="headingReturn_value_trusted_platform_module"></a>
<a id="Return_value_trusted_platform_module"></a>
#### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

<a id="headingReturn_value_memory"></a>
<a id="Return_value_memory"></a>
#### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in mebibytes (MiB).
- Value must be greater or equal to `20`

<a id="headingReturn_value_min_memory"></a>
<a id="Return_value_min_memory"></a>
#### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in mebibytes (MiB). Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
<a id="Return_value_min_memory_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_min_memory_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_min_memory_anyOf_i0)

- Type: integer
- Value must be greater or equal to `20`

<a id="tab-pane_Return_value_min_memory_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_min_memory_anyOf_i1)

- Type: null

<a id="headingReturn_value_hyperv_enlightenments"></a>
<a id="Return_value_hyperv_enlightenments"></a>
#### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

<a id="headingReturn_value_bootloader"></a>
<a id="Return_value_bootloader"></a>
#### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.
##### Must be one of:

- "UEFI_CSM"
- "UEFI"

<a id="headingReturn_value_bootloader_ovmf"></a>
<a id="Return_value_bootloader_ovmf"></a>
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

<a id="headingReturn_value_autostart"></a>
<a id="Return_value_autostart"></a>
#### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

<a id="headingReturn_value_hide_from_msr"></a>
<a id="Return_value_hide_from_msr"></a>
#### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide hypervisor signatures from guest OS MSR access.

<a id="headingReturn_value_ensure_display_device"></a>
<a id="Return_value_ensure_display_device"></a>
#### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure at least one display device is configured for the VM.

<a id="headingReturn_value_time"></a>
<a id="Return_value_time"></a>
#### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.
##### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingReturn_value_shutdown_timeout"></a>
<a id="Return_value_shutdown_timeout"></a>
#### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingReturn_value_arch_type"></a>
<a id="Return_value_arch_type"></a>
#### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
<a id="Return_value_arch_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_arch_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_arch_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_arch_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_arch_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_machine_type"></a>
<a id="Return_value_machine_type"></a>
#### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
<a id="Return_value_machine_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_machine_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_machine_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_machine_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_machine_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_uuid"></a>
<a id="Return_value_uuid"></a>
#### uuid

- Schema name: `Uuid`
- Default: null

Unique UUID for the VM. `null` to auto-generate.
<a id="Return_value_uuid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_uuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_uuid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_uuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_uuid_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices"></a>
<a id="Return_value_devices"></a>
#### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_devices_items"></a>
##### VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_id"></a>
<a id="Return_value_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

<a id="headingReturn_value_devices_items_attributes"></a>
<a id="Return_value_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="Return_value_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i0"></a>
###### [VMCDROMDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i0)

- Schema name: `VMCDROMDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for CD-ROM/DVD devices.
- Specific value: `"CDROM"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i0_path"></a>
<a id="Return_value_devices_items_attributes_oneOf_i0_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Path must not contain "{", "}" characters, and it should start with "/mnt/".
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1"></a>
###### [VMDisplayDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i1)

- Schema name: `VMDisplayDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.
- Specific value: `"DISPLAY"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_resolution"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_resolution"></a>
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

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_port"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_port"></a>
###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
<a id="Return_value_devices_items_attributes_oneOf_i1_port_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i1_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i1_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_web_port"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_web_port"></a>
###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
<a id="Return_value_devices_items_attributes_oneOf_i1_web_port_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1_web_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i1_web_port_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1_web_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i1_web_port_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_bind"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_bind"></a>
###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_wait"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_wait"></a>
###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_password"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_password"></a>
###### password

- Schema name: `Password`
- Default: ""

Password for display server authentication.
<a id="Return_value_devices_items_attributes_oneOf_i1_password_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i1_password_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i1_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i1_password_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_web"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_web"></a>
###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

<a id="headingReturn_value_devices_items_attributes_oneOf_i1_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.
###### Must be one of:

- "SPICE"
- "VNC"

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2"></a>
###### [VMNICDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i2)

- Schema name: `VMNICDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_nic_attach"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_nic_attach_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i2_mac"></a>
<a id="Return_value_devices_items_attributes_oneOf_i2_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="Return_value_devices_items_attributes_oneOf_i2_mac_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i2_mac_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i3"></a>
###### [VMPCIDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i3)

- Schema name: `VMPCIDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for PCI passthrough devices.
- Specific value: `"PCI"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i3_pptdev"></a>
<a id="Return_value_devices_items_attributes_oneOf_i3_pptdev"></a>
###### pptdev (required)

- Schema name: `Pptdev`
- Type: string

Host PCI device identifier to pass through to the VM.
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4"></a>
###### [VMRAWDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i4)

- Schema name: `VMRAWDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i4_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for raw disk devices.
- Specific value: `"RAW"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_path"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to the raw disk device or image file.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_exists"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_exists"></a>
###### exists

- Schema name: `Exists`
- Type: boolean
- Default: false

Whether the disk file already exists or should be created.

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_boot"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_boot"></a>
###### boot

- Schema name: `Boot`
- Type: boolean
- Default: false

Whether this disk should be marked as bootable.

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_size"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_size"></a>
###### size

- Schema name: `Size`
- Default: null

Size of the disk in bytes. Required if creating a new disk file.
<a id="Return_value_devices_items_attributes_oneOf_i4_size_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_logical_sectorsize"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="Return_value_devices_items_attributes_oneOf_i4_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_physical_sectorsize"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="Return_value_devices_items_attributes_oneOf_i4_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_iotype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingReturn_value_devices_items_attributes_oneOf_i4_serial"></a>
<a id="Return_value_devices_items_attributes_oneOf_i4_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="Return_value_devices_items_attributes_oneOf_i4_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i4_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i4_serial_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5"></a>
###### [VMDiskDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i5)

- Schema name: `VMDiskDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i5_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for virtual disk devices.
- Specific value: `"DISK"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_path"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_path"></a>
###### path

- Schema name: `Path`
- Default: null

Path to existing disk file or ZFS volume. `null` if creating a new ZFS volume.
<a id="Return_value_devices_items_attributes_oneOf_i5_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_create_zvol"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_create_zvol"></a>
###### create_zvol

- Schema name: `Create Zvol`
- Type: boolean
- Default: false

Whether to create a new ZFS volume for this disk.

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_zvol_name"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_zvol_name"></a>
###### zvol_name

- Schema name: `Zvol Name`
- Default: null

Name for the new ZFS volume. Required if `create_zvol` is true.
<a id="Return_value_devices_items_attributes_oneOf_i5_zvol_name_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_name_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_name_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_zvol_volsize"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_zvol_volsize"></a>
###### zvol_volsize

- Schema name: `Zvol Volsize`
- Default: null

Size of the new ZFS volume in bytes. Required if `create_zvol` is true.
<a id="Return_value_devices_items_attributes_oneOf_i5_zvol_volsize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_volsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_volsize_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_volsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_zvol_volsize_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_logical_sectorsize"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="Return_value_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_physical_sectorsize"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="Return_value_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_iotype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingReturn_value_devices_items_attributes_oneOf_i5_serial"></a>
<a id="Return_value_devices_items_attributes_oneOf_i5_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="Return_value_devices_items_attributes_oneOf_i5_serial_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i5_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i5_serial_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i6"></a>
###### [VMUSBDevice](#tab-pane_Return_value_devices_items_attributes_oneOf_i6)

- Schema name: `VMUSBDevice`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i6_dtype"></a>
<a id="Return_value_devices_items_attributes_oneOf_i6_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingReturn_value_devices_items_attributes_oneOf_i6_usb"></a>
<a id="Return_value_devices_items_attributes_oneOf_i6_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="Return_value_devices_items_attributes_oneOf_i6_usb_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i6_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_Return_value_devices_items_attributes_oneOf_i6_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_devices_items_attributes_oneOf_i6_usb_anyOf_i0_vendor_id"></a>
<a id="Return_value_devices_items_attributes_oneOf_i6_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingReturn_value_devices_items_attributes_oneOf_i6_usb_anyOf_i0_product_id"></a>
<a id="Return_value_devices_items_attributes_oneOf_i6_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i6_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i6_usb_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_attributes_oneOf_i6_controller_type"></a>
<a id="Return_value_devices_items_attributes_oneOf_i6_controller_type"></a>
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

<a id="headingReturn_value_devices_items_attributes_oneOf_i6_device"></a>
<a id="Return_value_devices_items_attributes_oneOf_i6_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="Return_value_devices_items_attributes_oneOf_i6_device_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i6_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_devices_items_attributes_oneOf_i6_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_devices_items_attributes_oneOf_i6_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_devices_items_attributes_oneOf_i6_device_anyOf_i1)

- Type: null

<a id="headingReturn_value_devices_items_vm"></a>
<a id="Return_value_devices_items_vm"></a>
###### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

<a id="headingReturn_value_devices_items_order"></a>
<a id="Return_value_devices_items_order"></a>
###### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

<a id="headingReturn_value_display_available"></a>
<a id="Return_value_display_available"></a>
#### display_available (required)

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

<a id="headingReturn_value_status"></a>
<a id="Return_value_status"></a>
#### status (required)

- Schema name: `VMStatus`
- Type: object

Current runtime status information for the VM.
- No Additional Properties
<a id="headingReturn_value_status_state"></a>
<a id="Return_value_status_state"></a>
##### state (required)

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

<a id="headingReturn_value_status_pid"></a>
<a id="Return_value_status_pid"></a>
##### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
<a id="Return_value_status_pid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_status_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_status_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_pid_anyOf_i1)

- Type: null

<a id="headingReturn_value_status_domain_state"></a>
<a id="Return_value_status_domain_state"></a>
##### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
<a id="Return_value_status_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_status_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_status_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_status_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_status_domain_state_anyOf_i1)

- Type: null

<a id="headingReturn_value_enable_secure_boot"></a>
<a id="Return_value_enable_secure_boot"></a>
#### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
