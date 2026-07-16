---
title: vm.get_instance
kind: method
source_rst: _sources/api_methods_vm.get_instance.rst.txt
source_html: api_methods_vm.get_instance.html
required_roles:
  - VM_READ
---

# vm.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `VM_READ`

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

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
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

- Schema name: `VMEntry`
- Type: object
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
