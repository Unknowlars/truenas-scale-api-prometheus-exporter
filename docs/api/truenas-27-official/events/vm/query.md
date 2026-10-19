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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `VMAddedEvent`
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

- Schema name: `VMEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_command_line_args"></a>
<a id="ADDED_fields_command_line_args"></a>
##### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor. Only a user with the `FULL_ADMIN` role may set or change this field.

<a id="headingADDED_fields_cpu_mode"></a>
<a id="ADDED_fields_cpu_mode"></a>
##### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.
###### Must be one of:

- "CUSTOM"
- "HOST-MODEL"
- "HOST-PASSTHROUGH"

<a id="headingADDED_fields_cpu_model"></a>
<a id="ADDED_fields_cpu_model"></a>
##### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
<a id="ADDED_fields_cpu_model_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_cpu_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_cpu_model_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_cpu_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_cpu_model_anyOf_i1)

- Type: null

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

<a id="headingADDED_fields_vcpus"></a>
<a id="ADDED_fields_vcpus"></a>
##### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPU sockets. The total number of guest vCPUs is `vcpus` * `cores` * `threads` (maximum 16).
- Value must be greater or equal to `1`

<a id="headingADDED_fields_cores"></a>
<a id="ADDED_fields_cores"></a>
##### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_threads"></a>
<a id="ADDED_fields_threads"></a>
##### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_cpuset"></a>
<a id="ADDED_fields_cpuset"></a>
##### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
<a id="ADDED_fields_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_cpuset_anyOf_i1)

- Type: null

<a id="headingADDED_fields_nodeset"></a>
<a id="ADDED_fields_nodeset"></a>
##### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
<a id="ADDED_fields_nodeset_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_nodeset_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_nodeset_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_nodeset_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_nodeset_anyOf_i1)

- Type: null

<a id="headingADDED_fields_enable_cpu_topology_extension"></a>
<a id="ADDED_fields_enable_cpu_topology_extension"></a>
##### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

<a id="headingADDED_fields_pin_vcpus"></a>
<a id="ADDED_fields_pin_vcpus"></a>
##### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

<a id="headingADDED_fields_suspend_on_snapshot"></a>
<a id="ADDED_fields_suspend_on_snapshot"></a>
##### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: true

Whether to automatically suspend the VM when a periodic snapshot task runs. For manual snapshots, the VM is suspended only if explicitly included in the snapshot's VM pause list.

<a id="headingADDED_fields_trusted_platform_module"></a>
<a id="ADDED_fields_trusted_platform_module"></a>
##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

<a id="headingADDED_fields_memory"></a>
<a id="ADDED_fields_memory"></a>
##### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in mebibytes (MiB).
- Value must be greater or equal to `20`

<a id="headingADDED_fields_min_memory"></a>
<a id="ADDED_fields_min_memory"></a>
##### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in mebibytes (MiB). Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
<a id="ADDED_fields_min_memory_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_min_memory_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_min_memory_anyOf_i0)

- Type: integer
- Value must be greater or equal to `20`

<a id="tab-pane_ADDED_fields_min_memory_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_min_memory_anyOf_i1)

- Type: null

<a id="headingADDED_fields_hyperv_enlightenments"></a>
<a id="ADDED_fields_hyperv_enlightenments"></a>
##### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

<a id="headingADDED_fields_bootloader"></a>
<a id="ADDED_fields_bootloader"></a>
##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.
###### Must be one of:

- "UEFI_CSM"
- "UEFI"

<a id="headingADDED_fields_bootloader_ovmf"></a>
<a id="ADDED_fields_bootloader_ovmf"></a>
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

<a id="headingADDED_fields_autostart"></a>
<a id="ADDED_fields_autostart"></a>
##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

<a id="headingADDED_fields_hide_from_msr"></a>
<a id="ADDED_fields_hide_from_msr"></a>
##### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide the KVM hypervisor from standard MSR-based discovery. Useful when doing GPU passthrough.

<a id="headingADDED_fields_ensure_display_device"></a>
<a id="ADDED_fields_ensure_display_device"></a>
##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure the guest always has access to a video device. Required for headless OS installations (e.g. Ubuntu Server). Set to `false` when using GPU passthrough without a separate display device.

<a id="headingADDED_fields_time"></a>
<a id="ADDED_fields_time"></a>
##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingADDED_fields_shutdown_timeout"></a>
<a id="ADDED_fields_shutdown_timeout"></a>
##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingADDED_fields_arch_type"></a>
<a id="ADDED_fields_arch_type"></a>
##### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
<a id="ADDED_fields_arch_type_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_arch_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_arch_type_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_arch_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_arch_type_anyOf_i1)

- Type: null

<a id="headingADDED_fields_machine_type"></a>
<a id="ADDED_fields_machine_type"></a>
##### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
<a id="ADDED_fields_machine_type_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_machine_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_machine_type_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_machine_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_machine_type_anyOf_i1)

- Type: null

<a id="headingADDED_fields_uuid"></a>
<a id="ADDED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique UUID for the VM. Assigned when the VM is created and cannot be changed afterwards.

<a id="headingADDED_fields_devices"></a>
<a id="ADDED_fields_devices"></a>
##### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_devices_items"></a>
###### VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_id"></a>
<a id="ADDED_fields_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

<a id="headingADDED_fields_devices_items_attributes"></a>
<a id="ADDED_fields_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="ADDED_fields_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i0"></a>
###### [VMCDROMDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i0)

- Schema name: `VMCDROMDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for CD-ROM/DVD devices.
- Specific value: `"CDROM"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i0_path"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i0_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Path must not contain "{", "}" characters, and it should start with "/mnt/".
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1"></a>
###### [VMDisplayDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1)

- Schema name: `VMDisplayDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.
- Specific value: `"DISPLAY"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_resolution"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_resolution"></a>
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

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_port"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_port"></a>
###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_port_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_web_port"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_web_port"></a>
###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_bind"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_bind"></a>
###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_wait"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_wait"></a>
###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_password"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_password"></a>
###### password

- Schema name: `Password`
- Default: ""

Password for display server authentication.
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_password_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_web"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_web"></a>
###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i1_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.
###### Must be one of:

- "SPICE"
- "VNC"

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2"></a>
###### [VMISCSIDiskDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2)

- Schema name: `VMISCSIDiskDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for iSCSI disk devices.
- Specific value: `"ISCSI_DISK"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_portal_address"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_portal_address"></a>
###### portal_address (required)

- Schema name: `Portal Address`

IP address of the iSCSI target portal.
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i1)

- Type: string

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_targets"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_targets"></a>
###### targets (required)

- Schema name: `Targets`
- Type: array of object

iSCSI targets to attach, one entry per target IQN.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_devices_items_attributes_oneOf_i2_targets_items"></a>
###### VMISCSIDiskTarget

- Schema name: `VMISCSIDiskTarget`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_targets_items_iqn"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_targets_items_iqn"></a>
###### iqn (required)

- Schema name: `Iqn`
- Type: string

iSCSI Qualified Name of the target.
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_targets_items_luns"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_targets_items_luns"></a>
###### luns

- Schema name: `Luns`
- Type: array of integer
- Default: [0]

LUN numbers to access on this target.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_devices_items_attributes_oneOf_i2_targets_items_luns_items"></a>
- Type: integer

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_initiator_iqn"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_initiator_iqn"></a>
###### initiator_iqn (required)

- Schema name: `Initiator Iqn`
- Type: string

IQN identifying this VM as an iSCSI initiator.
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i2_controller_slot"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i2_controller_slot"></a>
###### controller_slot

- Schema name: `Controller Slot`
- Type: integer
- Default: 21

PCI slot for the virtio-scsi-pci controller on the root bus (pcie.0 on q35/aarch64, pci.0 on i440fx). Conflicts with other explicitly-placed devices are detected at device creation time.
- Value must be greater or equal to `1` and lesser or equal to `30`

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3"></a>
###### [VMNICDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3)

- Schema name: `VMNICDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_trust_guest_rx_filters"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_nic_attach"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_mac"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_mac_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_pci_address"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_pci_address"></a>
###### pci_address

- Default: null

Pin this NIC to a specific PCI controller bus rather than letting libvirt auto-assign an address. `null` for automatic assignment.
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0"></a>
###### [VMNICPciAddress](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0)

- Schema name: `VMNICPciAddress`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_bus"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_bus"></a>
###### bus (required)

- Schema name: `Bus`
- Type: integer

PCI bus number. Must be >= 1; bus 0 is the root complex.
- Value must be greater or equal to `1` and lesser or equal to `255`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_slot"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

PCI slot number (0-31). No default: correct value depends on machine type.
- Value must be greater or equal to `0` and lesser or equal to `31`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_function"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_function"></a>
###### function

- Schema name: `Function`
- Type: integer
- Default: 0

PCI function number (0-7).
- Value must be greater or equal to `0` and lesser or equal to `7`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_domain"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_domain"></a>
###### domain

- Schema name: `Domain`
- Type: integer
- Default: 0

PCI domain number. Must be 0; multi-segment topologies are not supported.
- Value must be greater or equal to `0` and lesser or equal to `0`

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i4"></a>
###### [VMPCIDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i4)

- Schema name: `VMPCIDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i4_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i4_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for PCI passthrough devices.
- Specific value: `"PCI"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i4_pptdev"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i4_pptdev"></a>
###### pptdev (required)

- Schema name: `Pptdev`
- Type: string

Host PCI device identifier to pass through to the VM.
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5"></a>
###### [VMRAWDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5)

- Schema name: `VMRAWDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for raw disk devices.
- Specific value: `"RAW"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_path"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to the raw disk device or image file.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_exists"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_exists"></a>
###### exists

- Schema name: `Exists`
- Type: boolean
- Default: false

Whether the disk file already exists or should be created.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_boot"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_boot"></a>
###### boot

- Schema name: `Boot`
- Type: boolean
- Default: false

Whether this disk should be marked as bootable.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_size"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_size"></a>
###### size

- Schema name: `Size`
- Default: null

Size of the disk in bytes. Required if creating a new disk file.
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_iotype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i5_serial"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="ADDED_fields_devices_items_attributes_oneOf_i5_serial_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6"></a>
###### [VMDiskDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6)

- Schema name: `VMDiskDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for virtual disk devices.
- Specific value: `"DISK"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_path"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_path"></a>
###### path

- Schema name: `Path`
- Default: null

Path to existing disk file or ZFS volume. `null` if creating a new ZFS volume.
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_create_zvol"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_create_zvol"></a>
###### create_zvol

- Schema name: `Create Zvol`
- Type: boolean
- Default: false

Whether to create a new ZFS volume for this disk.

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_zvol_name"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_zvol_name"></a>
###### zvol_name

- Schema name: `Zvol Name`
- Default: null

Name for the new ZFS volume. Required if `create_zvol` is true.
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize"></a>
###### zvol_volsize

- Schema name: `Zvol Volsize`
- Default: null

Size of the new ZFS volume in bytes. Required if `create_zvol` is true.
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_iotype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingADDED_fields_devices_items_attributes_oneOf_i6_serial"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="ADDED_fields_devices_items_attributes_oneOf_i6_serial_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7"></a>
###### [VMUSBDevice](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7)

- Schema name: `VMUSBDevice`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i7_dtype"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingADDED_fields_devices_items_attributes_oneOf_i7_usb"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_vendor_id"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_product_id"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_attributes_oneOf_i7_controller_type"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_controller_type"></a>
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

<a id="headingADDED_fields_devices_items_attributes_oneOf_i7_device"></a>
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="ADDED_fields_devices_items_attributes_oneOf_i7_device_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i1)

- Type: null

<a id="headingADDED_fields_devices_items_vm"></a>
<a id="ADDED_fields_devices_items_vm"></a>
###### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

<a id="headingADDED_fields_devices_items_order"></a>
<a id="ADDED_fields_devices_items_order"></a>
###### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

<a id="headingADDED_fields_display_available"></a>
<a id="ADDED_fields_display_available"></a>
##### display_available (required)

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

<a id="headingADDED_fields_status"></a>
<a id="ADDED_fields_status"></a>
##### status (required)

Current runtime status information for the VM. `null` if `query-options.extra.retrieve_status` is `false`.
<a id="ADDED_fields_status_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_anyOf_i0"></a>
###### [VMStatus](#tab-pane_ADDED_fields_status_anyOf_i0)

- Schema name: `VMStatus`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_status_anyOf_i0_state"></a>
<a id="ADDED_fields_status_anyOf_i0_state"></a>
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

<a id="headingADDED_fields_status_anyOf_i0_pid"></a>
<a id="ADDED_fields_status_anyOf_i0_pid"></a>
###### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
<a id="ADDED_fields_status_anyOf_i0_pid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_anyOf_i0_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_anyOf_i0_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_status_anyOf_i0_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_anyOf_i0_pid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_status_anyOf_i0_domain_state"></a>
<a id="ADDED_fields_status_anyOf_i0_domain_state"></a>
###### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
<a id="ADDED_fields_status_anyOf_i0_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_status_anyOf_i0_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_status_anyOf_i0_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_status_anyOf_i0_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_anyOf_i0_domain_state_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_status_anyOf_i1)

- Type: null

<a id="headingADDED_fields_enable_secure_boot"></a>
<a id="ADDED_fields_enable_secure_boot"></a>
##### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `VMChangedEvent`
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

- Schema name: `VMEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_command_line_args"></a>
<a id="CHANGED_fields_command_line_args"></a>
##### command_line_args

- Schema name: `Command Line Args`
- Type: string
- Default: ""

Additional command line arguments passed to the VM hypervisor. Only a user with the `FULL_ADMIN` role may set or change this field.

<a id="headingCHANGED_fields_cpu_mode"></a>
<a id="CHANGED_fields_cpu_mode"></a>
##### cpu_mode

- Schema name: `Cpu Mode`
- Type: enum (of string)
- Default: "CUSTOM"

CPU virtualization mode. `CUSTOM`: Use specified model. `HOST-MODEL`: Mirror host CPU. `HOST-PASSTHROUGH`: Provide direct access to host CPU features.
###### Must be one of:

- "CUSTOM"
- "HOST-MODEL"
- "HOST-PASSTHROUGH"

<a id="headingCHANGED_fields_cpu_model"></a>
<a id="CHANGED_fields_cpu_model"></a>
##### cpu_model

- Schema name: `Cpu Model`
- Default: null

Specific CPU model to emulate. `null` to use hypervisor default.
<a id="CHANGED_fields_cpu_model_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_cpu_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_cpu_model_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_cpu_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_cpu_model_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Display name of the virtual machine.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description

- Schema name: `Description`
- Type: string
- Default: ""

Optional description or notes about the virtual machine.

<a id="headingCHANGED_fields_vcpus"></a>
<a id="CHANGED_fields_vcpus"></a>
##### vcpus

- Schema name: `Vcpus`
- Type: integer
- Default: 1

Number of virtual CPU sockets. The total number of guest vCPUs is `vcpus` * `cores` * `threads` (maximum 16).
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_cores"></a>
<a id="CHANGED_fields_cores"></a>
##### cores

- Schema name: `Cores`
- Type: integer
- Default: 1

Number of CPU cores per socket.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_threads"></a>
<a id="CHANGED_fields_threads"></a>
##### threads

- Schema name: `Threads`
- Type: integer
- Default: 1

Number of threads per CPU core.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_cpuset"></a>
<a id="CHANGED_fields_cpuset"></a>
##### cpuset

- Schema name: `Cpuset`
- Default: null

Set of host CPU cores to pin VM CPUs to. `null` for no pinning.
<a id="CHANGED_fields_cpuset_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_cpuset_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_cpuset_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_cpuset_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_cpuset_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_nodeset"></a>
<a id="CHANGED_fields_nodeset"></a>
##### nodeset

- Schema name: `Nodeset`
- Default: null

Set of NUMA nodes to constrain VM memory allocation. `null` for no constraints.
<a id="CHANGED_fields_nodeset_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_nodeset_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_nodeset_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_nodeset_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_nodeset_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enable_cpu_topology_extension"></a>
<a id="CHANGED_fields_enable_cpu_topology_extension"></a>
##### enable_cpu_topology_extension

- Schema name: `Enable Cpu Topology Extension`
- Type: boolean
- Default: false

Whether to expose detailed CPU topology information to the guest OS.

<a id="headingCHANGED_fields_pin_vcpus"></a>
<a id="CHANGED_fields_pin_vcpus"></a>
##### pin_vcpus

- Schema name: `Pin Vcpus`
- Type: boolean
- Default: false

Whether to pin virtual CPUs to specific host CPU cores. Improves performance but reduces host flexibility.

<a id="headingCHANGED_fields_suspend_on_snapshot"></a>
<a id="CHANGED_fields_suspend_on_snapshot"></a>
##### suspend_on_snapshot

- Schema name: `Suspend On Snapshot`
- Type: boolean
- Default: true

Whether to automatically suspend the VM when a periodic snapshot task runs. For manual snapshots, the VM is suspended only if explicitly included in the snapshot's VM pause list.

<a id="headingCHANGED_fields_trusted_platform_module"></a>
<a id="CHANGED_fields_trusted_platform_module"></a>
##### trusted_platform_module

- Schema name: `Trusted Platform Module`
- Type: boolean
- Default: false

Whether to enable virtual Trusted Platform Module (TPM) for the VM.

<a id="headingCHANGED_fields_memory"></a>
<a id="CHANGED_fields_memory"></a>
##### memory (required)

- Schema name: `Memory`
- Type: integer

Amount of memory allocated to the VM in mebibytes (MiB).
- Value must be greater or equal to `20`

<a id="headingCHANGED_fields_min_memory"></a>
<a id="CHANGED_fields_min_memory"></a>
##### min_memory

- Schema name: `Min Memory`
- Default: null

Minimum memory allocation for dynamic memory ballooning in mebibytes (MiB). Allows VM memory to shrink during low usage but guarantees this minimum. `null` to disable ballooning.
<a id="CHANGED_fields_min_memory_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_min_memory_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_min_memory_anyOf_i0)

- Type: integer
- Value must be greater or equal to `20`

<a id="tab-pane_CHANGED_fields_min_memory_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_min_memory_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_hyperv_enlightenments"></a>
<a id="CHANGED_fields_hyperv_enlightenments"></a>
##### hyperv_enlightenments

- Schema name: `Hyperv Enlightenments`
- Type: boolean
- Default: false

Whether to enable Hyper-V enlightenments for improved Windows guest performance.

<a id="headingCHANGED_fields_bootloader"></a>
<a id="CHANGED_fields_bootloader"></a>
##### bootloader

- Schema name: `Bootloader`
- Type: enum (of string)
- Default: "UEFI"

Boot firmware type. `UEFI` for modern UEFI, `UEFI_CSM` for legacy BIOS compatibility.
###### Must be one of:

- "UEFI_CSM"
- "UEFI"

<a id="headingCHANGED_fields_bootloader_ovmf"></a>
<a id="CHANGED_fields_bootloader_ovmf"></a>
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

<a id="headingCHANGED_fields_autostart"></a>
<a id="CHANGED_fields_autostart"></a>
##### autostart

- Schema name: `Autostart`
- Type: boolean
- Default: true

Whether to automatically start the VM when the host system boots.

<a id="headingCHANGED_fields_hide_from_msr"></a>
<a id="CHANGED_fields_hide_from_msr"></a>
##### hide_from_msr

- Schema name: `Hide From Msr`
- Type: boolean
- Default: false

Whether to hide the KVM hypervisor from standard MSR-based discovery. Useful when doing GPU passthrough.

<a id="headingCHANGED_fields_ensure_display_device"></a>
<a id="CHANGED_fields_ensure_display_device"></a>
##### ensure_display_device

- Schema name: `Ensure Display Device`
- Type: boolean
- Default: true

Whether to ensure the guest always has access to a video device. Required for headless OS installations (e.g. Ubuntu Server). Set to `false` when using GPU passthrough without a separate display device.

<a id="headingCHANGED_fields_time"></a>
<a id="CHANGED_fields_time"></a>
##### time

- Schema name: `Time`
- Type: enum (of string)
- Default: "LOCAL"

Guest OS time zone reference. `LOCAL` uses host timezone, `UTC` uses coordinated universal time.
###### Must be one of:

- "LOCAL"
- "UTC"

<a id="headingCHANGED_fields_shutdown_timeout"></a>
<a id="CHANGED_fields_shutdown_timeout"></a>
##### shutdown_timeout

- Schema name: `Shutdown Timeout`
- Type: integer
- Default: 90

Maximum time in seconds to wait for graceful shutdown before forcing power off. Default 90s balances allowing sufficient time for clean shutdown while avoiding indefinite hangs.
- Value must be greater or equal to `5` and lesser or equal to `300`

<a id="headingCHANGED_fields_arch_type"></a>
<a id="CHANGED_fields_arch_type"></a>
##### arch_type

- Schema name: `Arch Type`
- Default: null

Guest architecture type. `null` to use hypervisor default.
<a id="CHANGED_fields_arch_type_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_arch_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_arch_type_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_arch_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_arch_type_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_machine_type"></a>
<a id="CHANGED_fields_machine_type"></a>
##### machine_type

- Schema name: `Machine Type`
- Default: null

Virtual machine type/chipset. `null` to use hypervisor default.
<a id="CHANGED_fields_machine_type_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_machine_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_machine_type_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_machine_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_machine_type_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_uuid"></a>
<a id="CHANGED_fields_uuid"></a>
##### uuid (required)

- Schema name: `Uuid`
- Type: string

Unique UUID for the VM. Assigned when the VM is created and cannot be changed afterwards.

<a id="headingCHANGED_fields_devices"></a>
<a id="CHANGED_fields_devices"></a>
##### devices (required)

- Schema name: `Devices`
- Type: array of object

Array of virtual devices attached to this VM.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_devices_items"></a>
###### VMDeviceEntry

- Schema name: `VMDeviceEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_id"></a>
<a id="CHANGED_fields_devices_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the VM device.

<a id="headingCHANGED_fields_devices_items_attributes"></a>
<a id="CHANGED_fields_devices_items_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Device-specific configuration attributes.
<a id="CHANGED_fields_devices_items_attributes_oneOf"></a>
###### One of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i0"></a>
###### [VMCDROMDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i0)

- Schema name: `VMCDROMDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i0_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for CD-ROM/DVD devices.
- Specific value: `"CDROM"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i0_path"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i0_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Path must not contain "{", "}" characters, and it should start with "/mnt/".
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1"></a>
###### [VMDisplayDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1)

- Schema name: `VMDisplayDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for display/graphics devices.
- Specific value: `"DISPLAY"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_resolution"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_resolution"></a>
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

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_port"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_port"></a>
###### port

- Schema name: `Port`
- Default: null

VNC/SPICE port number for remote display access. `null` for auto-assignment.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_port_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i0)

- Type: integer
- Value must be greater or equal to `5900` and lesser or equal to `65535`

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_port_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_web_port"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_web_port"></a>
###### web_port

- Schema name: `Web Port`
- Default: null

Web-based display access port number. `null` for auto-assignment.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_web_port_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_bind"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_bind"></a>
###### bind

- Schema name: `Bind`
- Type: string
- Default: "127.0.0.1"

IP address to bind the display server to.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_wait"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_wait"></a>
###### wait

- Schema name: `Wait`
- Type: boolean
- Default: false

Whether to wait for a client connection before starting the VM.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_password"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_password"></a>
###### password

- Schema name: `Password`
- Default: ""

Password for display server authentication.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_password_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i1_password_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_web"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_web"></a>
###### web

- Schema name: `Web`
- Type: boolean
- Default: true

Whether to enable web-based display access.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i1_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i1_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "SPICE"

Display protocol type.
###### Must be one of:

- "SPICE"
- "VNC"

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2"></a>
###### [VMISCSIDiskDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2)

- Schema name: `VMISCSIDiskDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for iSCSI disk devices.
- Specific value: `"ISCSI_DISK"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_portal_address"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_portal_address"></a>
###### portal_address (required)

- Schema name: `Portal Address`

IP address of the iSCSI target portal.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i2_portal_address_anyOf_i1)

- Type: string

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_targets"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_targets"></a>
###### targets (required)

- Schema name: `Targets`
- Type: array of object

iSCSI targets to attach, one entry per target IQN.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_targets_items"></a>
###### VMISCSIDiskTarget

- Schema name: `VMISCSIDiskTarget`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_targets_items_iqn"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_targets_items_iqn"></a>
###### iqn (required)

- Schema name: `Iqn`
- Type: string

iSCSI Qualified Name of the target.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_targets_items_luns"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_targets_items_luns"></a>
###### luns

- Schema name: `Luns`
- Type: array of integer
- Default: [0]

LUN numbers to access on this target.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_targets_items_luns_items"></a>
- Type: integer

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_initiator_iqn"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_initiator_iqn"></a>
###### initiator_iqn (required)

- Schema name: `Initiator Iqn`
- Type: string

IQN identifying this VM as an iSCSI initiator.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i2_controller_slot"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i2_controller_slot"></a>
###### controller_slot

- Schema name: `Controller Slot`
- Type: integer
- Default: 21

PCI slot for the virtio-scsi-pci controller on the root bus (pcie.0 on q35/aarch64, pci.0 on i440fx). Conflicts with other explicitly-placed devices are detected at device creation time.
- Value must be greater or equal to `1` and lesser or equal to `30`

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3"></a>
###### [VMNICDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3)

- Schema name: `VMNICDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for network interface cards.
- Specific value: `"NIC"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_trust_guest_rx_filters"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_trust_guest_rx_filters"></a>
###### trust_guest_rx_filters

- Schema name: `Trust Guest Rx Filters`
- Type: boolean
- Default: false

Whether to trust guest OS receive filter settings for better performance.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "E1000"

Network interface controller type. `E1000` for Intel compatibility, `VIRTIO` for performance.
###### Must be one of:

- "E1000"
- "VIRTIO"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach"></a>
###### nic_attach

- Schema name: `Nic Attach`
- Default: null

Host network interface or bridge to attach to. `null` for no attachment.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_nic_attach_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_mac"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_mac"></a>
###### mac

- Schema name: `Mac`
- Default: null

MAC address for the virtual network interface. `null` for auto-generation.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_mac_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_mac_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_pci_address"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address"></a>
###### pci_address

- Default: null

Pin this NIC to a specific PCI controller bus rather than letting libvirt auto-assign an address. `null` for automatic assignment.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0"></a>
###### [VMNICPciAddress](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0)

- Schema name: `VMNICPciAddress`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_bus"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_bus"></a>
###### bus (required)

- Schema name: `Bus`
- Type: integer

PCI bus number. Must be >= 1; bus 0 is the root complex.
- Value must be greater or equal to `1` and lesser or equal to `255`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_slot"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

PCI slot number (0-31). No default: correct value depends on machine type.
- Value must be greater or equal to `0` and lesser or equal to `31`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_function"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_function"></a>
###### function

- Schema name: `Function`
- Type: integer
- Default: 0

PCI function number (0-7).
- Value must be greater or equal to `0` and lesser or equal to `7`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_domain"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i0_domain"></a>
###### domain

- Schema name: `Domain`
- Type: integer
- Default: 0

PCI domain number. Must be 0; multi-segment topologies are not supported.
- Value must be greater or equal to `0` and lesser or equal to `0`

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i3_pci_address_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i4"></a>
###### [VMPCIDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i4)

- Schema name: `VMPCIDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i4_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i4_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for PCI passthrough devices.
- Specific value: `"PCI"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i4_pptdev"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i4_pptdev"></a>
###### pptdev (required)

- Schema name: `Pptdev`
- Type: string

Host PCI device identifier to pass through to the VM.
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5"></a>
###### [VMRAWDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5)

- Schema name: `VMRAWDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for raw disk devices.
- Specific value: `"RAW"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_path"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_path"></a>
###### path (required)

- Schema name: `Path`
- Type: string

Filesystem path to the raw disk device or image file.
- Must match regular expression: `^[^{}]*$`
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_exists"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_exists"></a>
###### exists

- Schema name: `Exists`
- Type: boolean
- Default: false

Whether the disk file already exists or should be created.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_boot"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_boot"></a>
###### boot

- Schema name: `Boot`
- Type: boolean
- Default: false

Whether this disk should be marked as bootable.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_size"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_size"></a>
###### size

- Schema name: `Size`
- Default: null

Size of the disk in bytes. Required if creating a new disk file.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_iotype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i5_serial"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i5_serial_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i5_serial_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6"></a>
###### [VMDiskDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6)

- Schema name: `VMDiskDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for virtual disk devices.
- Specific value: `"DISK"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_path"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_path"></a>
###### path

- Schema name: `Path`
- Default: null

Path to existing disk file or ZFS volume. `null` if creating a new ZFS volume.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_type"></a>
###### type

- Schema name: `Type`
- Type: enum (of string)
- Default: "AHCI"

Disk controller interface type. AHCI for compatibility, VIRTIO for performance.
###### Must be one of:

- "AHCI"
- "VIRTIO"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_create_zvol"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_create_zvol"></a>
###### create_zvol

- Schema name: `Create Zvol`
- Type: boolean
- Default: false

Whether to create a new ZFS volume for this disk.

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name"></a>
###### zvol_name

- Schema name: `Zvol Name`
- Default: null

Name for the new ZFS volume. Required if `create_zvol` is true.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_name_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize"></a>
###### zvol_volsize

- Schema name: `Zvol Volsize`
- Default: null

Size of the new ZFS volume in bytes. Required if `create_zvol` is true.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_zvol_volsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize"></a>
###### logical_sectorsize

- Schema name: `Logical Sectorsize`
- Default: null

Logical sector size for the disk. `null` for default.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_logical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize"></a>
###### physical_sectorsize

- Schema name: `Physical Sectorsize`
- Default: null

Physical sector size for the disk. `null` for default.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i0)

- Type: enum (of integer or null)
###### Must be one of:

- null
- 512
- 4096

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_physical_sectorsize_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_iotype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_iotype"></a>
###### iotype

- Schema name: `Iotype`
- Type: enum (of string)
- Default: "THREADS"

I/O backend type for disk operations.
###### Must be one of:

- "NATIVE"
- "THREADS"
- "IO_URING"

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i6_serial"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_serial"></a>
###### serial

- Schema name: `Serial`
- Default: null

Serial number to assign to the virtual disk. `null` for auto-generated.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i6_serial_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i6_serial_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7"></a>
###### [VMUSBDevice](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7)

- Schema name: `VMUSBDevice`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i7_dtype"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_dtype"></a>
###### dtype (required)

- Schema name: `Dtype`
- Type: const

Device type identifier for USB devices.
- Specific value: `"USB"`

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i7_usb"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_usb"></a>
###### usb

- Default: null

USB device attributes for identification. `null` for USB host controller only.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0"></a>
###### [USBAttributes](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0)

- Schema name: `USBAttributes`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_vendor_id"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_vendor_id"></a>
###### vendor_id (required)

- Schema name: `Vendor Id`
- Type: string

USB vendor identifier in hexadecimal format (e.g., '0x1d6b' for Linux Foundation).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_product_id"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i0_product_id"></a>
###### product_id (required)

- Schema name: `Product Id`
- Type: string

USB product identifier in hexadecimal format (e.g., '0x0002' for 2.0 root hub).
- Must match regular expression: `^0x.*`
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_usb_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i7_controller_type"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_controller_type"></a>
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

<a id="headingCHANGED_fields_devices_items_attributes_oneOf_i7_device"></a>
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_device"></a>
###### device

- Schema name: `Device`
- Default: null

Host USB device path to pass through. `null` for controller only.
<a id="CHANGED_fields_devices_items_attributes_oneOf_i7_device_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_devices_items_attributes_oneOf_i7_device_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_devices_items_vm"></a>
<a id="CHANGED_fields_devices_items_vm"></a>
###### vm (required)

- Schema name: `Vm`
- Type: integer

ID of the virtual machine this device belongs to.

<a id="headingCHANGED_fields_devices_items_order"></a>
<a id="CHANGED_fields_devices_items_order"></a>
###### order (required)

- Schema name: `Order`
- Type: integer

Boot order priority for this device (lower numbers boot first).

<a id="headingCHANGED_fields_display_available"></a>
<a id="CHANGED_fields_display_available"></a>
##### display_available (required)

- Schema name: `Display Available`
- Type: boolean

Whether at least one display device is available for this VM.

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the virtual machine.

<a id="headingCHANGED_fields_status"></a>
<a id="CHANGED_fields_status"></a>
##### status (required)

Current runtime status information for the VM. `null` if `query-options.extra.retrieve_status` is `false`.
<a id="CHANGED_fields_status_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_anyOf_i0"></a>
###### [VMStatus](#tab-pane_CHANGED_fields_status_anyOf_i0)

- Schema name: `VMStatus`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_status_anyOf_i0_state"></a>
<a id="CHANGED_fields_status_anyOf_i0_state"></a>
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

<a id="headingCHANGED_fields_status_anyOf_i0_pid"></a>
<a id="CHANGED_fields_status_anyOf_i0_pid"></a>
###### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
<a id="CHANGED_fields_status_anyOf_i0_pid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_anyOf_i0_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_anyOf_i0_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_status_anyOf_i0_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_anyOf_i0_pid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_status_anyOf_i0_domain_state"></a>
<a id="CHANGED_fields_status_anyOf_i0_domain_state"></a>
###### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
<a id="CHANGED_fields_status_anyOf_i0_domain_state_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_status_anyOf_i0_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_status_anyOf_i0_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_status_anyOf_i0_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_anyOf_i0_domain_state_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_status_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enable_secure_boot"></a>
<a id="CHANGED_fields_enable_secure_boot"></a>
##### enable_secure_boot

- Schema name: `Enable Secure Boot`
- Type: boolean
- Default: false

Whether to enable UEFI Secure Boot for enhanced security.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `VMRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
