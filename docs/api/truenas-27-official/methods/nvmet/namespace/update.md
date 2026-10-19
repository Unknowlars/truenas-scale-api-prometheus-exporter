---
title: nvmet.namespace.update
kind: method
source_rst: _sources/api_methods_nvmet.namespace.update.rst.txt
source_html: api_methods_nvmet.namespace.update.html
required_roles:
  - SHARING_NVME_TARGET_WRITE
---

# nvmet.namespace.update

## Summary

Update NVMe target namespace of `id`.

## Required Roles

- `SHARING_NVME_TARGET_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: integer

ID of the NVMe-oF namespace to update.

#### Parameter 2: nvmet_namespace_update

<a id="Call_parameters_items_i1"></a>
#### nvmet_namespace_update

- Schema name: `nvmet_namespace_update`
- Type: object

Updated NVMe-oF namespace configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_nsid"></a>
<a id="Call_parameters_items_i1_nsid"></a>
##### nsid

- Schema name: `Nsid`

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
<a id="Call_parameters_items_i1_nsid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_nsid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_nsid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

<a id="tab-pane_Call_parameters_items_i1_nsid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_nsid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_device_type"></a>
<a id="Call_parameters_items_i1_device_type"></a>
##### device_type

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.
###### Must be one of:

- "ZVOL"
- "FILE"

<a id="headingCall_parameters_items_i1_device_path"></a>
<a id="Call_parameters_items_i1_device_path"></a>
##### device_path

- Schema name: `Device Path`
- Type: string

Normalized path to the device or file for the namespace.
- Must be at least `1` characters long

<a id="headingCall_parameters_items_i1_filesize"></a>
<a id="Call_parameters_items_i1_filesize"></a>
##### filesize

- Schema name: `Filesize`

When `device_type` is "FILE" then this will be the size of the file in bytes.
<a id="Call_parameters_items_i1_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_filesize_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_filesize_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

<a id="headingCall_parameters_items_i1_subsys_id"></a>
<a id="Call_parameters_items_i1_subsys_id"></a>
##### subsys_id

- Schema name: `Subsys Id`
- Type: integer

ID of the NVMe-oF subsystem to contain this namespace.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `NVMetNamespaceEntry`
- Type: object

The updated NVMe-oF namespace configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

<a id="headingReturn_value_nsid"></a>
<a id="Return_value_nsid"></a>
#### nsid

- Schema name: `Nsid`
- Default: null

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
<a id="Return_value_nsid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_nsid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_nsid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

<a id="tab-pane_Return_value_nsid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_nsid_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys"></a>
<a id="Return_value_subsys"></a>
#### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that contains this namespace.
- No Additional Properties
<a id="headingReturn_value_subsys_id"></a>
<a id="Return_value_subsys_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingReturn_value_subsys_name"></a>
<a id="Return_value_subsys_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingReturn_value_subsys_subnqn"></a>
<a id="Return_value_subsys_subnqn"></a>
##### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="Return_value_subsys_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_subsys_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_subnqn_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_serial"></a>
<a id="Return_value_subsys_serial"></a>
##### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingReturn_value_subsys_allow_any_host"></a>
<a id="Return_value_subsys_allow_any_host"></a>
##### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingReturn_value_subsys_pi_enable"></a>
<a id="Return_value_subsys_pi_enable"></a>
##### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="Return_value_subsys_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_subsys_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_qid_max"></a>
<a id="Return_value_subsys_qid_max"></a>
##### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="Return_value_subsys_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_subsys_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_qid_max_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_ieee_oui"></a>
<a id="Return_value_subsys_ieee_oui"></a>
##### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="Return_value_subsys_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_subsys_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_ieee_oui_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_ana"></a>
<a id="Return_value_subsys_ana"></a>
##### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="Return_value_subsys_ana_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_subsys_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_ana_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_hosts"></a>
<a id="Return_value_subsys_hosts"></a>
##### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_subsys_hosts_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_subsys_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_subsys_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_hosts_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_namespaces"></a>
<a id="Return_value_subsys_namespaces"></a>
##### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_subsys_namespaces_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_subsys_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_subsys_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_namespaces_anyOf_i1)

- Type: null

<a id="headingReturn_value_subsys_ports"></a>
<a id="Return_value_subsys_ports"></a>
##### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_subsys_ports_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_subsys_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_subsys_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_subsys_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_subsys_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_subsys_ports_anyOf_i1)

- Type: null

<a id="headingReturn_value_device_type"></a>
<a id="Return_value_device_type"></a>
#### device_type (required)

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.
##### Must be one of:

- "ZVOL"
- "FILE"

<a id="headingReturn_value_device_path"></a>
<a id="Return_value_device_path"></a>
#### device_path (required)

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the file-based namespace (e.g., 'tank/nvmet'). Returns `null` for ZVOL-based namespaces or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "device_path".
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_relative_path"></a>
<a id="Return_value_relative_path"></a>
#### relative_path (required)

- Schema name: `Relative Path`

The path of the file-based namespace relative to the dataset mountpoint (e.g., 'namespaces/ns1.img'). An empty string indicates the file is at the dataset root. Returns `null` for ZVOL-based namespaces or if the path cannot be resolved yet. This is a read-only field automatically populated from "device_path".
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_filesize"></a>
<a id="Return_value_filesize"></a>
#### filesize

- Schema name: `Filesize`
- Default: null

When `device_type` is "FILE" then this will be the size of the file in bytes.
<a id="Return_value_filesize_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_filesize_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_filesize_anyOf_i1)

- Type: null

<a id="headingReturn_value_device_uuid"></a>
<a id="Return_value_device_uuid"></a>
#### device_uuid (required)

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_device_nguid"></a>
<a id="Return_value_device_nguid"></a>
#### device_nguid (required)

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
<a id="Return_value_locked_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_locked_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
