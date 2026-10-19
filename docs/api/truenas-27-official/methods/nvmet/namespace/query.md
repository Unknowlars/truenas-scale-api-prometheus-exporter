---
title: nvmet.namespace.query
kind: method
source_rst: _sources/api_methods_nvmet.namespace.query.rst.txt
source_html: api_methods_nvmet.namespace.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.namespace.query

## Required Roles

- `SHARING_NVME_TARGET_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
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
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### NVMetNamespaceEntry

- Schema name: `NVMetNamespaceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

<a id="headingReturn_value_anyOf_i0_items_nsid"></a>
<a id="Return_value_anyOf_i0_items_nsid"></a>
###### nsid

- Schema name: `Nsid`
- Default: null

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
<a id="Return_value_anyOf_i0_items_nsid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_nsid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_nsid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

<a id="tab-pane_Return_value_anyOf_i0_items_nsid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_nsid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys"></a>
<a id="Return_value_anyOf_i0_items_subsys"></a>
###### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that contains this namespace.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_subsys_id"></a>
<a id="Return_value_anyOf_i0_items_subsys_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingReturn_value_anyOf_i0_items_subsys_name"></a>
<a id="Return_value_anyOf_i0_items_subsys_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_subsys_subnqn"></a>
<a id="Return_value_anyOf_i0_items_subsys_subnqn"></a>
###### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="Return_value_anyOf_i0_items_subsys_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_subnqn_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_serial"></a>
<a id="Return_value_anyOf_i0_items_subsys_serial"></a>
###### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingReturn_value_anyOf_i0_items_subsys_allow_any_host"></a>
<a id="Return_value_anyOf_i0_items_subsys_allow_any_host"></a>
###### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingReturn_value_anyOf_i0_items_subsys_pi_enable"></a>
<a id="Return_value_anyOf_i0_items_subsys_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="Return_value_anyOf_i0_items_subsys_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_qid_max"></a>
<a id="Return_value_anyOf_i0_items_subsys_qid_max"></a>
###### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="Return_value_anyOf_i0_items_subsys_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_qid_max_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_ieee_oui"></a>
<a id="Return_value_anyOf_i0_items_subsys_ieee_oui"></a>
###### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="Return_value_anyOf_i0_items_subsys_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_ieee_oui_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_ana"></a>
<a id="Return_value_anyOf_i0_items_subsys_ana"></a>
###### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="Return_value_anyOf_i0_items_subsys_ana_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_ana_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_hosts"></a>
<a id="Return_value_anyOf_i0_items_subsys_hosts"></a>
###### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_anyOf_i0_items_subsys_hosts_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_subsys_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_hosts_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_namespaces"></a>
<a id="Return_value_anyOf_i0_items_subsys_namespaces"></a>
###### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_anyOf_i0_items_subsys_namespaces_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_subsys_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_namespaces_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_subsys_ports"></a>
<a id="Return_value_anyOf_i0_items_subsys_ports"></a>
###### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_anyOf_i0_items_subsys_ports_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_subsys_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_subsys_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_subsys_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_subsys_ports_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_device_type"></a>
<a id="Return_value_anyOf_i0_items_device_type"></a>
###### device_type (required)

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.
###### Must be one of:

- "ZVOL"
- "FILE"

<a id="headingReturn_value_anyOf_i0_items_device_path"></a>
<a id="Return_value_anyOf_i0_items_device_path"></a>
###### device_path (required)

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the file-based namespace (e.g., 'tank/nvmet'). Returns `null` for ZVOL-based namespaces or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i0_items_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_relative_path"></a>
<a id="Return_value_anyOf_i0_items_relative_path"></a>
###### relative_path (required)

- Schema name: `Relative Path`

The path of the file-based namespace relative to the dataset mountpoint (e.g., 'namespaces/ns1.img'). An empty string indicates the file is at the dataset root. Returns `null` for ZVOL-based namespaces or if the path cannot be resolved yet. This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i0_items_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_filesize"></a>
<a id="Return_value_anyOf_i0_items_filesize"></a>
###### filesize

- Schema name: `Filesize`
- Default: null

When `device_type` is "FILE" then this will be the size of the file in bytes.
<a id="Return_value_anyOf_i0_items_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_filesize_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_filesize_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_device_uuid"></a>
<a id="Return_value_anyOf_i0_items_device_uuid"></a>
###### device_uuid (required)

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_device_nguid"></a>
<a id="Return_value_anyOf_i0_items_device_nguid"></a>
###### device_nguid (required)

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_enabled"></a>
<a id="Return_value_anyOf_i0_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

<a id="headingReturn_value_anyOf_i0_items_locked"></a>
<a id="Return_value_anyOf_i0_items_locked"></a>
###### locked (required)

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
<a id="Return_value_anyOf_i0_items_locked_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_locked_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [NVMetNamespaceEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `NVMetNamespaceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

<a id="headingReturn_value_anyOf_i1_nsid"></a>
<a id="Return_value_anyOf_i1_nsid"></a>
###### nsid

- Schema name: `Nsid`
- Default: null

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
<a id="Return_value_anyOf_i1_nsid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_nsid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_nsid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

<a id="tab-pane_Return_value_anyOf_i1_nsid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_nsid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_subsys"></a>
<a id="Return_value_anyOf_i1_subsys"></a>
###### subsys (required)

- Type: object

NVMe-oF subsystem that contains this namespace.

<a id="headingReturn_value_anyOf_i1_device_type"></a>
<a id="Return_value_anyOf_i1_device_type"></a>
###### device_type (required)

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.
###### Must be one of:

- "ZVOL"
- "FILE"

<a id="headingReturn_value_anyOf_i1_device_path"></a>
<a id="Return_value_anyOf_i1_device_path"></a>
###### device_path (required)

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the file-based namespace (e.g., 'tank/nvmet'). Returns `null` for ZVOL-based namespaces or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i1_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_relative_path"></a>
<a id="Return_value_anyOf_i1_relative_path"></a>
###### relative_path (required)

- Schema name: `Relative Path`

The path of the file-based namespace relative to the dataset mountpoint (e.g., 'namespaces/ns1.img'). An empty string indicates the file is at the dataset root. Returns `null` for ZVOL-based namespaces or if the path cannot be resolved yet. This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i1_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_filesize"></a>
<a id="Return_value_anyOf_i1_filesize"></a>
###### filesize

- Schema name: `Filesize`
- Default: null

When `device_type` is "FILE" then this will be the size of the file in bytes.
<a id="Return_value_anyOf_i1_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_filesize_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_filesize_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_device_uuid"></a>
<a id="Return_value_anyOf_i1_device_uuid"></a>
###### device_uuid (required)

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_device_nguid"></a>
<a id="Return_value_anyOf_i1_device_nguid"></a>
###### device_nguid (required)

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i1_enabled"></a>
<a id="Return_value_anyOf_i1_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

<a id="headingReturn_value_anyOf_i1_locked"></a>
<a id="Return_value_anyOf_i1_locked"></a>
###### locked (required)

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
<a id="Return_value_anyOf_i1_locked_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i1_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_locked_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### NVMetNamespaceQueryResultItem

- Schema name: `NVMetNamespaceQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

<a id="headingReturn_value_anyOf_i2_items_nsid"></a>
<a id="Return_value_anyOf_i2_items_nsid"></a>
###### nsid

- Schema name: `Nsid`

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
<a id="Return_value_anyOf_i2_items_nsid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_nsid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_nsid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

<a id="tab-pane_Return_value_anyOf_i2_items_nsid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_nsid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys"></a>
<a id="Return_value_anyOf_i2_items_subsys"></a>
###### subsys

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that contains this namespace.
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_subsys_id"></a>
<a id="Return_value_anyOf_i2_items_subsys_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF subsystem.

<a id="headingReturn_value_anyOf_i2_items_subsys_name"></a>
<a id="Return_value_anyOf_i2_items_subsys_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Human readable name for the subsystem. If `subnqn` is not provided on creation, then this name will be appended to the `basenqn` from `nvmet.global.config` to generate a subnqn.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_subsys_subnqn"></a>
<a id="Return_value_anyOf_i2_items_subsys_subnqn"></a>
###### subnqn

- Schema name: `Subnqn`
- Default: null

NVMe Qualified Name (NQN) for the subsystem. If not provided during creation, will be auto-generated by appending the `name` to the `basenqn` from `nvmet.global.config`.
<a id="Return_value_anyOf_i2_items_subsys_subnqn_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_subnqn_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_subnqn_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_subnqn_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_subnqn_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_serial"></a>
<a id="Return_value_anyOf_i2_items_subsys_serial"></a>
###### serial (required)

- Schema name: `Serial`
- Type: string

Serial number assigned to the subsystem.

<a id="headingReturn_value_anyOf_i2_items_subsys_allow_any_host"></a>
<a id="Return_value_anyOf_i2_items_subsys_allow_any_host"></a>
###### allow_any_host

- Schema name: `Allow Any Host`
- Type: boolean
- Default: false

Any host can access the storage associated with this subsystem (i.e. no access control).

<a id="headingReturn_value_anyOf_i2_items_subsys_pi_enable"></a>
<a id="Return_value_anyOf_i2_items_subsys_pi_enable"></a>
###### pi_enable

- Schema name: `Pi Enable`
- Default: null

Enable Protection Information (PI) for data integrity checking.
<a id="Return_value_anyOf_i2_items_subsys_pi_enable_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_pi_enable_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_pi_enable_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_pi_enable_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_pi_enable_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_qid_max"></a>
<a id="Return_value_anyOf_i2_items_subsys_qid_max"></a>
###### qid_max

- Schema name: `Qid Max`
- Default: null

Maximum number of queue IDs allowed for this subsystem.
<a id="Return_value_anyOf_i2_items_subsys_qid_max_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_qid_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_qid_max_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_qid_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_qid_max_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_ieee_oui"></a>
<a id="Return_value_anyOf_i2_items_subsys_ieee_oui"></a>
###### ieee_oui

- Schema name: `Ieee Oui`
- Default: null

IEEE Organizationally Unique Identifier for the subsystem.
<a id="Return_value_anyOf_i2_items_subsys_ieee_oui_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_ieee_oui_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_ieee_oui_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_ieee_oui_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_ieee_oui_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_ana"></a>
<a id="Return_value_anyOf_i2_items_subsys_ana"></a>
###### ana

- Schema name: `Ana`
- Default: null

If set to either `True` or `False`, then *override* the global `ana` setting from `nvmet.global.config` for this subsystem only. If `null`, then the global `ana` setting will take effect.
<a id="Return_value_anyOf_i2_items_subsys_ana_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_ana_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_ana_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_ana_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_ana_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_hosts"></a>
<a id="Return_value_anyOf_i2_items_subsys_hosts"></a>
###### hosts

- Schema name: `Hosts`

List of host ids which have access to this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_anyOf_i2_items_subsys_hosts_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_hosts_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_hosts_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_subsys_hosts_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_hosts_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_hosts_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_namespaces"></a>
<a id="Return_value_anyOf_i2_items_subsys_namespaces"></a>
###### namespaces

- Schema name: `Namespaces`

List of namespaces ids in this subsystem. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_anyOf_i2_items_subsys_namespaces_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_namespaces_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_namespaces_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_subsys_namespaces_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_namespaces_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_namespaces_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_subsys_ports"></a>
<a id="Return_value_anyOf_i2_items_subsys_ports"></a>
###### ports

- Schema name: `Ports`

List of ports ids on which this subsystem is available. Only populated on query if `extra.options.verbose` is set.
<a id="Return_value_anyOf_i2_items_subsys_ports_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_ports_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_subsys_ports_anyOf_i0)

- Type: array of integer
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_subsys_ports_anyOf_i0_items"></a>
- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_subsys_ports_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_subsys_ports_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_device_type"></a>
<a id="Return_value_anyOf_i2_items_device_type"></a>
###### device_type

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.
###### Must be one of:

- "ZVOL"
- "FILE"

<a id="headingReturn_value_anyOf_i2_items_device_path"></a>
<a id="Return_value_anyOf_i2_items_device_path"></a>
###### device_path

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_dataset"></a>
<a id="Return_value_anyOf_i2_items_dataset"></a>
###### dataset

- Schema name: `Dataset`

The ZFS dataset containing the file-based namespace (e.g., 'tank/nvmet'). Returns `null` for ZVOL-based namespaces or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i2_items_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_relative_path"></a>
<a id="Return_value_anyOf_i2_items_relative_path"></a>
###### relative_path

- Schema name: `Relative Path`

The path of the file-based namespace relative to the dataset mountpoint (e.g., 'namespaces/ns1.img'). An empty string indicates the file is at the dataset root. Returns `null` for ZVOL-based namespaces or if the path cannot be resolved yet. This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i2_items_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_filesize"></a>
<a id="Return_value_anyOf_i2_items_filesize"></a>
###### filesize

- Schema name: `Filesize`

When `device_type` is "FILE" then this will be the size of the file in bytes.
<a id="Return_value_anyOf_i2_items_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_filesize_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_filesize_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_device_uuid"></a>
<a id="Return_value_anyOf_i2_items_device_uuid"></a>
###### device_uuid

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_device_nguid"></a>
<a id="Return_value_anyOf_i2_items_device_nguid"></a>
###### device_nguid

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_enabled"></a>
<a id="Return_value_anyOf_i2_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

<a id="headingReturn_value_anyOf_i2_items_locked"></a>
<a id="Return_value_anyOf_i2_items_locked"></a>
###### locked

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
<a id="Return_value_anyOf_i2_items_locked_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i2_items_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_locked_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [NVMetNamespaceQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `NVMetNamespaceQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF namespace.

<a id="headingReturn_value_anyOf_i3_nsid"></a>
<a id="Return_value_anyOf_i3_nsid"></a>
###### nsid

- Schema name: `Nsid`

Namespace ID (NSID). Each namespace within a subsystem has an associated NSID, unique within that subsystem. If not supplied during `namespace` creation then the next available NSID will be used.
<a id="Return_value_anyOf_i3_nsid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_nsid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_nsid_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and strictly lesser than `4294967295`

<a id="tab-pane_Return_value_anyOf_i3_nsid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_nsid_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_subsys"></a>
<a id="Return_value_anyOf_i3_subsys"></a>
###### subsys

- Type: object

NVMe-oF subsystem that contains this namespace.

<a id="headingReturn_value_anyOf_i3_device_type"></a>
<a id="Return_value_anyOf_i3_device_type"></a>
###### device_type

- Schema name: `Device Type`
- Type: enum (of string)

Type of device (or file) used to implement the namespace.
###### Must be one of:

- "ZVOL"
- "FILE"

<a id="headingReturn_value_anyOf_i3_device_path"></a>
<a id="Return_value_anyOf_i3_device_path"></a>
###### device_path

- Schema name: `Device Path`
- Type: string

Path to the device or file being used to implement the namespace. When `device_type` is: "ZVOL": `device_path` is e.g. "zvol/poolname/zvolname" "FILE": `device_path` is e.g. "/mnt/poolmnt/path/to/file". The file will be created if necessary.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_dataset"></a>
<a id="Return_value_anyOf_i3_dataset"></a>
###### dataset

- Schema name: `Dataset`

The ZFS dataset containing the file-based namespace (e.g., 'tank/nvmet'). Returns `null` for ZVOL-based namespaces or if the FILE path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i3_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_dataset_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_relative_path"></a>
<a id="Return_value_anyOf_i3_relative_path"></a>
###### relative_path

- Schema name: `Relative Path`

The path of the file-based namespace relative to the dataset mountpoint (e.g., 'namespaces/ns1.img'). An empty string indicates the file is at the dataset root. Returns `null` for ZVOL-based namespaces or if the path cannot be resolved yet. This is a read-only field automatically populated from "device_path".
<a id="Return_value_anyOf_i3_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_filesize"></a>
<a id="Return_value_anyOf_i3_filesize"></a>
###### filesize

- Schema name: `Filesize`

When `device_type` is "FILE" then this will be the size of the file in bytes.
<a id="Return_value_anyOf_i3_filesize_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_filesize_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_filesize_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_filesize_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_filesize_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_device_uuid"></a>
<a id="Return_value_anyOf_i3_device_uuid"></a>
###### device_uuid

- Schema name: `Device Uuid`
- Type: string

Unique device identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_device_nguid"></a>
<a id="Return_value_anyOf_i3_device_nguid"></a>
###### device_nguid

- Schema name: `Device Nguid`
- Type: string

Namespace Globally Unique Identifier for the namespace.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i3_enabled"></a>
<a id="Return_value_anyOf_i3_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

If `enabled` is `False` then the namespace will not be accessible. Some namespace configuration changes are blocked when that namespace is enabled.

<a id="headingReturn_value_anyOf_i3_locked"></a>
<a id="Return_value_anyOf_i3_locked"></a>
###### locked

- Schema name: `Locked`

Reflect the locked state of the namespace. The underlying `device_path` could be an encrypted ZVOL, or a file on an encrypted dataset. In either case `locked` will be `True` if the underlying entity is locked.
<a id="Return_value_anyOf_i3_locked_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_anyOf_i3_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_locked_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
