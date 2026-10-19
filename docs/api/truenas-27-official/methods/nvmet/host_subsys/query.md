---
title: nvmet.host_subsys.query
kind: method
source_rst: _sources/api_methods_nvmet.host_subsys.query.rst.txt
source_html: api_methods_nvmet.host_subsys.query.html
required_roles:
  - SHARING_NVME_TARGET_READ
---

# nvmet.host_subsys.query

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
###### NVMetHostSubsysEntry

- Schema name: `NVMetHostSubsysEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the host-subsystem association.

<a id="headingReturn_value_anyOf_i0_items_host"></a>
<a id="Return_value_anyOf_i0_items_host"></a>
###### host (required)

- Schema name: `NVMetHostEntry`
- Type: object

NVMe-oF host that is authorized to access the subsystem.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_host_id"></a>
<a id="Return_value_anyOf_i0_items_host_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

<a id="headingReturn_value_anyOf_i0_items_host_hostnqn"></a>
<a id="Return_value_anyOf_i0_items_host_hostnqn"></a>
###### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_host_description"></a>
<a id="Return_value_anyOf_i0_items_host_description"></a>
###### description

- Schema name: `Description`
- Type: string
- Default: ""

Description of the NVMet host.

<a id="headingReturn_value_anyOf_i0_items_host_dhchap_key"></a>
<a id="Return_value_anyOf_i0_items_host_dhchap_key"></a>
###### dhchap_key

- Schema name: `Dhchap Key`
- Default: ""

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_anyOf_i0_items_host_dhchap_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_host_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_host_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_host_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_host_dhchap_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_host_dhchap_ctrl_key"></a>
<a id="Return_value_anyOf_i0_items_host_dhchap_ctrl_key"></a>
###### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: ""

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_anyOf_i0_items_host_dhchap_ctrl_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_host_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_host_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i0_items_host_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_host_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_host_dhchap_dhgroup"></a>
<a id="Return_value_anyOf_i0_items_host_dhchap_dhgroup"></a>
###### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="Return_value_anyOf_i0_items_host_dhchap_dhgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_host_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_host_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_Return_value_anyOf_i0_items_host_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_host_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_host_dhchap_hash"></a>
<a id="Return_value_anyOf_i0_items_host_dhchap_hash"></a>
###### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
###### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

<a id="headingReturn_value_anyOf_i0_items_subsys"></a>
<a id="Return_value_anyOf_i0_items_subsys"></a>
###### subsys (required)

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that the host is authorized to access.
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

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [NVMetHostSubsysEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `NVMetHostSubsysEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the host-subsystem association.

<a id="headingReturn_value_anyOf_i1_host"></a>
<a id="Return_value_anyOf_i1_host"></a>
###### host (required)

- Type: object

NVMe-oF host that is authorized to access the subsystem.

<a id="headingReturn_value_anyOf_i1_subsys"></a>
<a id="Return_value_anyOf_i1_subsys"></a>
###### subsys (required)

- Type: object

NVMe-oF subsystem that the host is authorized to access.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### NVMetHostSubsysQueryResultItem

- Schema name: `NVMetHostSubsysQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the host-subsystem association.

<a id="headingReturn_value_anyOf_i2_items_host"></a>
<a id="Return_value_anyOf_i2_items_host"></a>
###### host

- Schema name: `NVMetHostEntry`
- Type: object

NVMe-oF host that is authorized to access the subsystem.
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_host_id"></a>
<a id="Return_value_anyOf_i2_items_host_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NVMe-oF host.

<a id="headingReturn_value_anyOf_i2_items_host_hostnqn"></a>
<a id="Return_value_anyOf_i2_items_host_hostnqn"></a>
###### hostnqn (required)

- Schema name: `Hostnqn`
- Type: string

NQN of the host that will connect to this TrueNAS.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i2_items_host_description"></a>
<a id="Return_value_anyOf_i2_items_host_description"></a>
###### description

- Schema name: `Description`
- Type: string
- Default: ""

Description of the NVMet host.

<a id="headingReturn_value_anyOf_i2_items_host_dhchap_key"></a>
<a id="Return_value_anyOf_i2_items_host_dhchap_key"></a>
###### dhchap_key

- Schema name: `Dhchap Key`
- Default: ""

If set, the secret that the host must present when connecting. A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_anyOf_i2_items_host_dhchap_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_host_dhchap_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_host_dhchap_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_host_dhchap_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_host_dhchap_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_host_dhchap_ctrl_key"></a>
<a id="Return_value_anyOf_i2_items_host_dhchap_ctrl_key"></a>
###### dhchap_ctrl_key

- Schema name: `Dhchap Ctrl Key`
- Default: ""

If set, the secret that this TrueNAS will present to the host when the host is connecting (Bi-Directional Authentication). A suitable secret can be generated using `nvme gen-dhchap-key`, or by using the `nvmet.host.generate_key` API.
<a id="Return_value_anyOf_i2_items_host_dhchap_ctrl_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_host_dhchap_ctrl_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_host_dhchap_ctrl_key_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_anyOf_i2_items_host_dhchap_ctrl_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_host_dhchap_ctrl_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_host_dhchap_dhgroup"></a>
<a id="Return_value_anyOf_i2_items_host_dhchap_dhgroup"></a>
###### dhchap_dhgroup

- Schema name: `Dhchap Dhgroup`
- Default: null

If selected, the DH (Diffie-Hellman) key exchange built on top of CHAP to be used for authentication.
<a id="Return_value_anyOf_i2_items_host_dhchap_dhgroup_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_host_dhchap_dhgroup_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_host_dhchap_dhgroup_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "2048-BIT"
- "3072-BIT"
- "4096-BIT"
- "6144-BIT"
- "8192-BIT"

<a id="tab-pane_Return_value_anyOf_i2_items_host_dhchap_dhgroup_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_host_dhchap_dhgroup_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_host_dhchap_hash"></a>
<a id="Return_value_anyOf_i2_items_host_dhchap_hash"></a>
###### dhchap_hash

- Schema name: `Dhchap Hash`
- Type: enum (of string)
- Default: "SHA-256"

HMAC (Hashed Message Authentication Code) to be used in conjunction if a `dhchap_dhgroup` is selected.
###### Must be one of:

- "SHA-256"
- "SHA-384"
- "SHA-512"

<a id="headingReturn_value_anyOf_i2_items_subsys"></a>
<a id="Return_value_anyOf_i2_items_subsys"></a>
###### subsys

- Schema name: `NVMetSubsysEntry`
- Type: object

NVMe-oF subsystem that the host is authorized to access.
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

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [NVMetHostSubsysQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `NVMetHostSubsysQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the host-subsystem association.

<a id="headingReturn_value_anyOf_i3_host"></a>
<a id="Return_value_anyOf_i3_host"></a>
###### host

- Type: object

NVMe-oF host that is authorized to access the subsystem.

<a id="headingReturn_value_anyOf_i3_subsys"></a>
<a id="Return_value_anyOf_i3_subsys"></a>
###### subsys

- Type: object

NVMe-oF subsystem that the host is authorized to access.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
