---
title: sharing.smb.create
kind: method
source_rst: _sources/api_methods_sharing.smb.create.rst.txt
source_html: api_methods_sharing.smb.create.html
required_roles:
  - SHARING_SMB_WRITE
---

# sharing.smb.create

## Summary

Create an SMB share.

The behavior and available options of the share are determined by its `purpose`; most deployments should use `DEFAULT_SHARE`. Before creating a share, the server should be joined to a directory service or have at least one local SMB user; [sharing.smb.share_precheck](share_precheck.md) can be used to validate this and the share name in advance.

.. note::

Setting raw `smb.conf` auxiliary parameters (`options.auxsmbconf`) is restricted to callers with full administrative privileges. Auxiliary parameters that would break the SMB server are rejected, returning a JSON-RPC `error` response (code `-32602`, *Invalid params*).

## Required Roles

- `SHARING_SMB_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object

SMB share configuration data for the new share.
- No Additional Properties
<a id="headingCall_parameters_items_i0_purpose"></a>
<a id="Call_parameters_items_i0_purpose"></a>
##### purpose

- Schema name: `Purpose`
- Type: enum (of string)
- Default: "DEFAULT_SHARE"

This parameter sets the purpose of the SMB share. It controls how the SMB share behaves and what features are available through options. The DEFAULT_SHARE setting is best for most applications, and should be used, unless there is a specific reason to change it. `DEFAULT_SHARE`: Set the SMB share for best compatibility with common SMB clients. `LEGACY_SHARE`: Set the SMB share for compatibility with older TrueNAS versions. Automated backend migrations use this to help the administrator move to better-supported share settings. It should not be used for new SMB shares. `TIMEMACHINE_SHARE`: The SMB share is presented to MacOS clients as a time machine target. NOTE: `aapl_extensions` must be set in the global `smb.config`. `MULTIPROTOCOL_SHARE`: The SMB share is configured for multi-protocol access. Set this if the `path` is shared through NFS, FTP, or used by containers or apps. NOTE: This setting can reduce SMB share performance because it turns off some SMB features for safer interoperability with external processes. `TIME_LOCKED_SHARE`: The SMB share makes files read-only through the SMB protocol after the set grace_period ends. WARNING: This setting does not work if the `path` is accessed locally or if another SMB share without the `TIME_LOCKED_SHARE` purpose uses the same path. WARNING: This setting might not meet regulatory requirements for write-once storage. `PRIVATE_DATASETS_SHARE`: The server uses the specified `dataset_naming_schema` in `options` to make a new ZFS dataset when the client connects. The server uses this dataset as the share path during the SMB session. `EXTERNAL_SHARE`: The SMB share is a DFS proxy to a share hosted on an external SMB server. `VEEAM_REPOSITORY_SHARE`: The SMB share is a repository for Veeam Backup & Replication and supports Fast Clone. NOTE: This feature is available only for TrueNAS Enterprise customers. `FCP_SHARE`: The SMB share is a used for Final Cut Pro storage. This feature automatically configures the share to provide storage according to Apple support guidelines described in https://support.apple.com/en-ca/101919. NOTE: `aapl_extensions` must be set in the global `smb.config`. WARNING: This feature forcibly enables `aapl_name_mangling` on the SMB share which may cause unexpected behavior for data that was written without this feature enabled.
###### Must be one of:

- "DEFAULT_SHARE"
- "LEGACY_SHARE"
- "TIMEMACHINE_SHARE"
- "MULTIPROTOCOL_SHARE"
- "TIME_LOCKED_SHARE"
- "PRIVATE_DATASETS_SHARE"
- "EXTERNAL_SHARE"
- "VEEAM_REPOSITORY_SHARE"
- "FCP_SHARE"

<a id="headingCall_parameters_items_i0_name"></a>
<a id="Call_parameters_items_i0_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

SMB share name. SMB share names are case-insensitive and must be unique, and are subject to the following restrictions: A share name must be no more than 80 characters in length. The following characters are illegal in a share name: `\ / [ ] : | < > + = ; , * ? "` Unicode control characters are illegal in a share name. The following share names are not allowed: global, printers, homes.
Examples:

```json
"SHARE"
```
Examples:

```json
"Macrodata_refinement"
```

<a id="headingCall_parameters_items_i0_path"></a>
<a id="Call_parameters_items_i0_path"></a>
##### path (required)

- Schema name: `Path`

Local server path to share by using the SMB protocol. The path must start with `/mnt/` and must be in a ZFS pool. Use the string `EXTERNAL` if the share works as a DFS proxy. WARNING: The TrueNAS server does not check if external paths are reachable.
<a id="Call_parameters_items_i0_path_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_path_anyOf_i1)

- Type: const
- Specific value: `"EXTERNAL"`

Examples:

```json
"/mnt/dozer/SHARE"
```
Examples:

```json
"EXTERNAL"
```

<a id="headingCall_parameters_items_i0_enabled"></a>
<a id="Call_parameters_items_i0_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the SMB share is not available over the SMB protocol.

<a id="headingCall_parameters_items_i0_comment"></a>
<a id="Call_parameters_items_i0_comment"></a>
##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Text field that is seen next to a share when an SMB client requests a list of SMB shares on the TrueNAS server.
Examples:

```json
"Mammalian nurturable"
```

<a id="headingCall_parameters_items_i0_readonly"></a>
<a id="Call_parameters_items_i0_readonly"></a>
##### readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

If set, SMB clients cannot create or change files and directories in the SMB share. NOTE: If set, the share path is still writeable by local processes or other file sharing protocols.

<a id="headingCall_parameters_items_i0_browsable"></a>
<a id="Call_parameters_items_i0_browsable"></a>
##### browsable

- Schema name: `Browsable`
- Type: boolean
- Default: true

If set, the share is included when an SMB client requests a list of SMB shares on the TrueNAS server.

<a id="headingCall_parameters_items_i0_access_based_share_enumeration"></a>
<a id="Call_parameters_items_i0_access_based_share_enumeration"></a>
##### access_based_share_enumeration

- Schema name: `Access Based Share Enumeration`
- Type: boolean
- Default: false

If set, the share is only included when an SMB client requests a list of shares on the SMB server if the share (not filesystem) access control list (see `sharing.smb.getacl`) grants access to the user.

<a id="headingCall_parameters_items_i0_audit"></a>
<a id="Call_parameters_items_i0_audit"></a>
##### audit

- Schema name: `SmbAuditConfig`
- Type: object

Audit configuration for monitoring SMB share access and operations.
- No Additional Properties
Examples:

```json
{
    "enable": true,
    "ignore_list": [],
    "watch_list": [
        "interns"
    ]
}
```
Examples:

```json
{
    "enable": true,
    "ignore_list": [
        "automation"
    ],
    "watch_list": []
}
```
<a id="headingCall_parameters_items_i0_audit_enable"></a>
<a id="Call_parameters_items_i0_audit_enable"></a>
###### enable

- Schema name: `Enable`
- Type: boolean
- Default: false

Turn on auditing for the SMB share. SMB share auditing may not be enabled if `minimum_protocol` is `SMB1` in the SMB service configuration.

<a id="headingCall_parameters_items_i0_audit_watch_list"></a>
<a id="Call_parameters_items_i0_audit_watch_list"></a>
###### watch_list

- Schema name: `Watch List`
- Type: array of string
- Default: []

Only audit the listed group accounts. If the list is empty, all groups will be audited.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_audit_watch_list_items"></a>
- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "interns",
    "contractors"
]
```

<a id="headingCall_parameters_items_i0_audit_ignore_list"></a>
<a id="Call_parameters_items_i0_audit_ignore_list"></a>
###### ignore_list

- Schema name: `Ignore List`
- Type: array of string
- Default: []

List of groups that will not be audited.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_audit_ignore_list_items"></a>
- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "automation",
    "apps"
]
```

<a id="headingCall_parameters_items_i0_options"></a>
<a id="Call_parameters_items_i0_options"></a>
##### options

- Schema name: `Options`
- Default: null

Additional configuration related to the configured SMB share purpose. If null, then the default options related to the share purpose will be applied.
<a id="Call_parameters_items_i0_options_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_anyOf_i0)

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0"></a>
###### [LegacyOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0)

- Schema name: `LegacyOpt`
- Type: object

These configuration options apply to shares with the `LEGACY_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"LEGACY_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_recyclebin"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_recyclebin"></a>
###### recyclebin

- Schema name: `Recyclebin`
- Type: boolean
- Default: false

If set, deleted files are moved to per-user subdirectories in the `.recycle` directory. The SMB server creates the `.recycle` directory at the root of the SMB share if the file is in the same ZFS dataset as the share `path`. If the file is in a child ZFS dataset, the server uses the `mountpoint` of that dataset to create the `.recycle` directory. NOTE: This feature does not work with recycle bin features in client operating systems. WARNING: Do not use this feature instead of backups or ZFS snapshots.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix"></a>
###### path_suffix

- Schema name: `Path Suffix`
- Default: null

Path suffix template for dynamic path generation. Uses SMB variable substitution patterns like `%D` (domain) and `%U` (username).
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i1)

- Type: null

Examples:

```json
"%D/%U"
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_guestok"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_guestok"></a>
###### guestok

- Schema name: `Guestok`
- Type: boolean
- Default: false

If set, guest access to the share is allowed. This should not be used in production environments. NOTE: If a user account does not exist, the SMB server maps access to the guest account. WARNING: Additional client-side configuration downgrading security settings may be required in order to use this feature.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_streams"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_streams"></a>
###### streams

- Schema name: `Streams`
- Type: boolean
- Default: true

If set, support for SMB alternate data streams is enabled. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_durablehandle"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_durablehandle"></a>
###### durablehandle

- Schema name: `Durablehandle`
- Type: boolean
- Default: true

If set, support for SMB durable handles is enabled. WARNING: This feature is incompatible with multiprotocol and local filesystem access.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_shadowcopy"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_shadowcopy"></a>
###### shadowcopy

- Schema name: `Shadowcopy`
- Type: boolean
- Default: true

If set, previous versions of files contained in ZFS snapshots are accessible through standard SMB protocol operations on previous versions of files.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_fsrvp"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_fsrvp"></a>
###### fsrvp

- Schema name: `Fsrvp`
- Type: boolean
- Default: false

If set, enable support for the File Server Remote VSS Protocol. This allows clients to manage snapshots for the specified SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_home"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_home"></a>
###### home

- Schema name: `Home`
- Type: boolean
- Default: false

Use the `path` to store user home directories. Each user has a personal home directory and share. Users cannot access other user directories when connecting to shares. NOTE: This parameter changes the share `name` to `homes`. It also creates a dynamic share that mirrors the username of the user. Both shares use the same `path`. You can hide the homes share by turning off `browsable`. The dynamic user home share cannot be hidden. WARNING: This parameter changes the global server configuration. The SMB server will not authenticate users without a valid home directory or shell.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_acl"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_acl"></a>
###### acl

- Schema name: `Acl`
- Type: boolean
- Default: true

If set, enable mapping of local filesystem ACLs to NT ACLs for SMB clients.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_afp"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_afp"></a>
###### afp

- Schema name: `Afp`
- Type: boolean
- Default: false

If set, SMB server will read and store file metadata in an on-disk format compatible with the legacy AFP file server. WARNING: This should not be set unless the SMB server is sharing data that was originally written via the AFP protocol.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_timemachine"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_timemachine"></a>
###### timemachine

- Schema name: `Timemachine`
- Type: boolean
- Default: false

If set, MacOS clients can use the share as a time machine target.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_timemachine_quota"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_timemachine_quota"></a>
###### timemachine_quota

- Schema name: `Timemachine Quota`
- Type: integer
- Default: 0

If set, it defines the maximum size of a single time machine sparsebundle volume by limiting the reported disk size to the SMB client. A value of zero means no quota is applied to the share. NOTE: Modern MacOS versions you set Time Machine quotas client-side. This gives more predictable server and client behavior.
- Value must be greater or equal to `0` and lesser or equal to `109951162777600`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_aapl_name_mangling"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid"></a>
###### vuid

- Schema name: `Vuid`
- Default: null

This value is the Time Machine volume UUID for the SMB share. The TrueNAS server uses this value in the mDNS advertisement for the Time Machine share. MacOS clients may use it to identify the volume. When you create or update a share, setting this value to null makes the TrueNAS server generate a new UUID for the share.
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_vuid_anyOf_i1)

- Type: null

Examples:

```json
"d12aafdc-a7ac-4e3c-8bbd-6001f7f19819"
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i0_auxsmbconf"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i0_auxsmbconf"></a>
###### auxsmbconf

- Schema name: `Auxsmbconf`
- Type: string
- Default: ""

Additional parameters to set on the SMB share. Parameters must be separated by the new-line character. WARNING: These parameters are not validated and may cause undefined server behavior including data corruption or data loss. WARNING: Auxiliary parameters are an unsupported configuration.
- Must be at most `2147483647` characters long

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i1"></a>
###### [DefaultOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i1)

- Schema name: `DefaultOpt`
- Type: object

These configuration options apply to shares with the `DEFAULT_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i1_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i1_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"DEFAULT_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i1_aapl_name_mangling"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i1_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i1_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i1_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i1_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i1_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i1_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i1_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2"></a>
###### [TimeMachineOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2)

- Schema name: `TimeMachineOpt`
- Type: object

These configuration options apply to shares with the `TIMEMACHINE_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"TIMEMACHINE_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_timemachine_quota"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_timemachine_quota"></a>
###### timemachine_quota

- Schema name: `Timemachine Quota`
- Type: integer
- Default: 0

If set, it defines the maximum size in bytes of a single time machine sparsebundle volume by limiting the reported disk size to the SMB client. A value of zero means no quota is set. NOTE: Modern MacOS versions you set Time Machine quotas client-side. This gives more predictable server and client behavior.
- Value must be greater or equal to `0` and lesser or equal to `109951162777600`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_auto_snapshot"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_auto_snapshot"></a>
###### auto_snapshot

- Schema name: `Auto Snapshot`
- Type: boolean
- Default: false

If set, the server makes a ZFS snapshot of the share dataset when the client makes a new Time Machine backup.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_auto_dataset_creation"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_auto_dataset_creation"></a>
###### auto_dataset_creation

- Schema name: `Auto Dataset Creation`
- Type: boolean
- Default: false

If set, the server uses the `dataset_naming_schema` to make a new ZFS dataset when the client connects. The server uses this dataset as the share path during the SMB session. NOTE: this setting requires the share path to be a dataset mountpoint.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema"></a>
###### dataset_naming_schema

- Schema name: `Dataset Naming Schema`
- Default: null

The naming schema to use when `auto_dataset_creation` is specified. If you do not set a schema, the server uses `%U` (username) if it is not joined to Active Directory. If the server is joined to Active Directory it uses `%D/%U` (domain/username). See the `VARIABLE SUBSTITUTIONS` section in the smb.conf manpage for valid strings. WARNING: ZFS dataset naming rules are more restrictive than normal path rules. For example, if `%u` is specified then the character `\` may be inserted in the username (which is not supported in ZFS).
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i1)

- Type: null

Examples:

```json
"%D/%U"
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid"></a>
###### vuid

- Schema name: `Vuid`
- Default: null

This value is the Time Machine volume UUID for the SMB share. The TrueNAS server uses this value in the mDNS advertisement for the Time Machine share. MacOS clients may use it to identify the volume. When you create or update a share, setting this value to null makes the TrueNAS server generate a new UUID for the share.
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_vuid_anyOf_i1)

- Type: null

Examples:

```json
"d12aafdc-a7ac-4e3c-8bbd-6001f7f19819"
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i2_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i2_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i3"></a>
###### [MultiprotocolOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i3)

- Schema name: `MultiprotocolOpt`
- Type: object

These configuration options apply to shares with the `MULTIPROTOCOL_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i3_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i3_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"MULTIPROTOCOL_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i3_aapl_name_mangling"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i3_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i3_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i3_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i3_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i3_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i3_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i3_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i4"></a>
###### [TimeLockedOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i4)

- Schema name: `TimeLockedOpt`
- Type: object

These configuration options apply to shares with the `TIME_LOCKED_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i4_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"TIME_LOCKED_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i4_grace_period"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_grace_period"></a>
###### grace_period

- Schema name: `Grace Period`
- Type: integer
- Default: 900

Time in seconds when write access to the file or directory is allowed.
- Value must be greater or equal to `60` and lesser or equal to `15552000`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i4_aapl_name_mangling"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i4_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i4_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i4_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i5"></a>
###### [PrivateDatasetOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i5)

- Schema name: `PrivateDatasetOpt`
- Type: object

These configuration options apply to shares with the `PRIVATE_DATASETS_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i5_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"PRIVATE_DATASETS_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema"></a>
###### dataset_naming_schema

- Schema name: `Dataset Naming Schema`
- Default: null

The naming schema to use. If you do not set a schema, the server uses `%U` (username) if it is not joined to Active Directory. If the server is joined to Active Directory it uses `%D/%U` (domain/username). WARNING: ZFS dataset naming rules are more restrictive than normal path rules.
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i1)

- Type: null

Examples:

```json
"%D/%U"
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i5_auto_quota"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_auto_quota"></a>
###### auto_quota

- Schema name: `Auto Quota`
- Type: integer
- Default: 0

Set the specified ZFS quota (in gibibytes) on new datasets. If the value is zero, TrueNAS disables automatic quotas for the share.
- Value must be greater or equal to `0`
Examples:

```json
10
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i5_aapl_name_mangling"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i5_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i5_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i5_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i6"></a>
###### [ExternalOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i6)

- Schema name: `ExternalOpt`
- Type: object

These configuration options apply to shares with the `EXTERNAL_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i6_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i6_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"EXTERNAL_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i6_remote_path"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i6_remote_path"></a>
###### remote_path (required)

- Schema name: `Remote Path`
- Type: array of string

This is the path to the external server and share. Each server entry must include a full domain name or IP address and share name. Separate the server and share with the `\` character. WARNING: The SMB server and TrueNAS middleware do not check if external paths are reachable.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i6_remote_path_items"></a>
- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "192.168.0.200\\SHARE"
]
```
Examples:

```json
[
    "SERVER1.MYDOM.INTERNAL\\SHARE"
]
```
Examples:

```json
[
    "SERVER1.MYDOM.INTERNAL\\SHARE, SERVER2.MYDOM.INTERNAL\\SHARE"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i7"></a>
###### [VeeamRepositoryOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i7)

- Schema name: `VeeamRepositoryOpt`
- Type: object

These configuration options apply to shares with the `VEEAM_REPOSITORY_SHARE` purpose.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i7_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i7_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"VEEAM_REPOSITORY_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i7_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i7_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i7_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i7_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i7_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i7_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i8"></a>
###### [FCPStorageOpt](#tab-pane_Call_parameters_items_i0_options_anyOf_i0_oneOf_i8)

- Schema name: `FCPStorageOpt`
- Type: object

These configuration options apply to shares with the `FCP_SHARE` purpose as a storage location for Final Cut Pro data.
- No Additional Properties
<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i8_purpose"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i8_purpose"></a>
###### purpose (required)

- Schema name: `Purpose`
- Type: const
- Specific value: `"FCP_SHARE"`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i8_aapl_name_mangling"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i8_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: const
- Default: true

Illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients.
- Specific value: `true`

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i8_hostsallow"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i8_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i8_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingCall_parameters_items_i0_options_anyOf_i0_oneOf_i8_hostsdeny"></a>
<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i8_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_options_anyOf_i0_oneOf_i8_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Call_parameters_items_i0_options_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_options_anyOf_i1)

- Type: null

Examples:

```json
{
    "auto_snapshot": true
}
```
Examples:

```json
{
    "auto_quota": 100
}
```

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `SharingSMBEntry`
- Type: object

The created SMB share configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this SMB share.

<a id="headingReturn_value_purpose"></a>
<a id="Return_value_purpose"></a>
#### purpose

- Schema name: `Purpose`
- Type: enum (of string)
- Default: "DEFAULT_SHARE"

This parameter sets the purpose of the SMB share. It controls how the SMB share behaves and what features are available through options. The DEFAULT_SHARE setting is best for most applications, and should be used, unless there is a specific reason to change it. `DEFAULT_SHARE`: Set the SMB share for best compatibility with common SMB clients. `LEGACY_SHARE`: Set the SMB share for compatibility with older TrueNAS versions. Automated backend migrations use this to help the administrator move to better-supported share settings. It should not be used for new SMB shares. `TIMEMACHINE_SHARE`: The SMB share is presented to MacOS clients as a time machine target. NOTE: `aapl_extensions` must be set in the global `smb.config`. `MULTIPROTOCOL_SHARE`: The SMB share is configured for multi-protocol access. Set this if the `path` is shared through NFS, FTP, or used by containers or apps. NOTE: This setting can reduce SMB share performance because it turns off some SMB features for safer interoperability with external processes. `TIME_LOCKED_SHARE`: The SMB share makes files read-only through the SMB protocol after the set grace_period ends. WARNING: This setting does not work if the `path` is accessed locally or if another SMB share without the `TIME_LOCKED_SHARE` purpose uses the same path. WARNING: This setting might not meet regulatory requirements for write-once storage. `PRIVATE_DATASETS_SHARE`: The server uses the specified `dataset_naming_schema` in `options` to make a new ZFS dataset when the client connects. The server uses this dataset as the share path during the SMB session. `EXTERNAL_SHARE`: The SMB share is a DFS proxy to a share hosted on an external SMB server. `VEEAM_REPOSITORY_SHARE`: The SMB share is a repository for Veeam Backup & Replication and supports Fast Clone. NOTE: This feature is available only for TrueNAS Enterprise customers. `FCP_SHARE`: The SMB share is a used for Final Cut Pro storage. This feature automatically configures the share to provide storage according to Apple support guidelines described in https://support.apple.com/en-ca/101919. NOTE: `aapl_extensions` must be set in the global `smb.config`. WARNING: This feature forcibly enables `aapl_name_mangling` on the SMB share which may cause unexpected behavior for data that was written without this feature enabled.
##### Must be one of:

- "DEFAULT_SHARE"
- "LEGACY_SHARE"
- "TIMEMACHINE_SHARE"
- "MULTIPROTOCOL_SHARE"
- "TIME_LOCKED_SHARE"
- "PRIVATE_DATASETS_SHARE"
- "EXTERNAL_SHARE"
- "VEEAM_REPOSITORY_SHARE"
- "FCP_SHARE"

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

SMB share name. SMB share names are case-insensitive and must be unique, and are subject to the following restrictions: A share name must be no more than 80 characters in length. The following characters are illegal in a share name: `\ / [ ] : | < > + = ; , * ? "` Unicode control characters are illegal in a share name. The following share names are not allowed: global, printers, homes.
Examples:

```json
"SHARE"
```
Examples:

```json
"Macrodata_refinement"
```

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`

Local server path to share by using the SMB protocol. The path must start with `/mnt/` and must be in a ZFS pool. Use the string `EXTERNAL` if the share works as a DFS proxy. WARNING: The TrueNAS server does not check if external paths are reachable.
<a id="Return_value_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_path_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_path_anyOf_i1)

- Type: const
- Specific value: `"EXTERNAL"`

Examples:

```json
"/mnt/dozer/SHARE"
```
Examples:

```json
"EXTERNAL"
```

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing this SMB share (e.g., 'tank/share'). Returns `null` for external shares or if the path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
<a id="Return_value_dataset_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_dataset_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_dataset_anyOf_i1)

- Type: null

Examples:

```json
"dozer/SHARE"
```

<a id="headingReturn_value_relative_path"></a>
<a id="Return_value_relative_path"></a>
#### relative_path (required)

- Schema name: `Relative Path`

The path of the share relative to the dataset mountpoint (e.g., 'subfolder/data'). An empty string indicates the share is at the dataset root. Returns `null` for external shares or if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the SMB share is not available over the SMB protocol.

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Text field that is seen next to a share when an SMB client requests a list of SMB shares on the TrueNAS server.
Examples:

```json
"Mammalian nurturable"
```

<a id="headingReturn_value_readonly"></a>
<a id="Return_value_readonly"></a>
#### readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

If set, SMB clients cannot create or change files and directories in the SMB share. NOTE: If set, the share path is still writeable by local processes or other file sharing protocols.

<a id="headingReturn_value_browsable"></a>
<a id="Return_value_browsable"></a>
#### browsable

- Schema name: `Browsable`
- Type: boolean
- Default: true

If set, the share is included when an SMB client requests a list of SMB shares on the TrueNAS server.

<a id="headingReturn_value_access_based_share_enumeration"></a>
<a id="Return_value_access_based_share_enumeration"></a>
#### access_based_share_enumeration

- Schema name: `Access Based Share Enumeration`
- Type: boolean
- Default: false

If set, the share is only included when an SMB client requests a list of shares on the SMB server if the share (not filesystem) access control list (see `sharing.smb.getacl`) grants access to the user.

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
<a id="Return_value_locked_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_locked_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_locked_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_locked_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_locked_anyOf_i1)

- Type: null

<a id="headingReturn_value_audit"></a>
<a id="Return_value_audit"></a>
#### audit

- Schema name: `SmbAuditConfig`
- Type: object

Audit configuration for monitoring SMB share access and operations.
- No Additional Properties
Examples:

```json
{
    "enable": true,
    "ignore_list": [],
    "watch_list": [
        "interns"
    ]
}
```
Examples:

```json
{
    "enable": true,
    "ignore_list": [
        "automation"
    ],
    "watch_list": []
}
```
<a id="headingReturn_value_audit_enable"></a>
<a id="Return_value_audit_enable"></a>
##### enable

- Schema name: `Enable`
- Type: boolean
- Default: false

Turn on auditing for the SMB share. SMB share auditing may not be enabled if `minimum_protocol` is `SMB1` in the SMB service configuration.

<a id="headingReturn_value_audit_watch_list"></a>
<a id="Return_value_audit_watch_list"></a>
##### watch_list

- Schema name: `Watch List`
- Type: array of string
- Default: []

Only audit the listed group accounts. If the list is empty, all groups will be audited.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_audit_watch_list_items"></a>
- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "interns",
    "contractors"
]
```

<a id="headingReturn_value_audit_ignore_list"></a>
<a id="Return_value_audit_ignore_list"></a>
##### ignore_list

- Schema name: `Ignore List`
- Type: array of string
- Default: []

List of groups that will not be audited.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_audit_ignore_list_items"></a>
- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "automation",
    "apps"
]
```

<a id="headingReturn_value_options"></a>
<a id="Return_value_options"></a>
#### options

- Schema name: `Options`
- Default: null

Additional configuration related to the configured SMB share purpose. If null, then the default options related to the share purpose will be applied.
<a id="Return_value_options_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_options_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_options_anyOf_i0)

<a id="Return_value_options_anyOf_i0_oneOf"></a>
###### One of

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i0"></a>
###### [LegacyOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i0)

- Schema name: `LegacyOpt`
- Type: object

These configuration options apply to shares with the `LEGACY_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_recyclebin"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_recyclebin"></a>
###### recyclebin

- Schema name: `Recyclebin`
- Type: boolean
- Default: false

If set, deleted files are moved to per-user subdirectories in the `.recycle` directory. The SMB server creates the `.recycle` directory at the root of the SMB share if the file is in the same ZFS dataset as the share `path`. If the file is in a child ZFS dataset, the server uses the `mountpoint` of that dataset to create the `.recycle` directory. NOTE: This feature does not work with recycle bin features in client operating systems. WARNING: Do not use this feature instead of backups or ZFS snapshots.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_path_suffix"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_path_suffix"></a>
###### path_suffix

- Schema name: `Path Suffix`
- Default: null

Path suffix template for dynamic path generation. Uses SMB variable substitution patterns like `%D` (domain) and `%U` (username).
<a id="Return_value_options_anyOf_i0_oneOf_i0_path_suffix_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_options_anyOf_i0_oneOf_i0_path_suffix_anyOf_i1)

- Type: null

Examples:

```json
"%D/%U"
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i0_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i0_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_guestok"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_guestok"></a>
###### guestok

- Schema name: `Guestok`
- Type: boolean
- Default: false

If set, guest access to the share is allowed. This should not be used in production environments. NOTE: If a user account does not exist, the SMB server maps access to the guest account. WARNING: Additional client-side configuration downgrading security settings may be required in order to use this feature.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_streams"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_streams"></a>
###### streams

- Schema name: `Streams`
- Type: boolean
- Default: true

If set, support for SMB alternate data streams is enabled. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_durablehandle"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_durablehandle"></a>
###### durablehandle

- Schema name: `Durablehandle`
- Type: boolean
- Default: true

If set, support for SMB durable handles is enabled. WARNING: This feature is incompatible with multiprotocol and local filesystem access.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_shadowcopy"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_shadowcopy"></a>
###### shadowcopy

- Schema name: `Shadowcopy`
- Type: boolean
- Default: true

If set, previous versions of files contained in ZFS snapshots are accessible through standard SMB protocol operations on previous versions of files.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_fsrvp"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_fsrvp"></a>
###### fsrvp

- Schema name: `Fsrvp`
- Type: boolean
- Default: false

If set, enable support for the File Server Remote VSS Protocol. This allows clients to manage snapshots for the specified SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_home"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_home"></a>
###### home

- Schema name: `Home`
- Type: boolean
- Default: false

Use the `path` to store user home directories. Each user has a personal home directory and share. Users cannot access other user directories when connecting to shares. NOTE: This parameter changes the share `name` to `homes`. It also creates a dynamic share that mirrors the username of the user. Both shares use the same `path`. You can hide the homes share by turning off `browsable`. The dynamic user home share cannot be hidden. WARNING: This parameter changes the global server configuration. The SMB server will not authenticate users without a valid home directory or shell.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_acl"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_acl"></a>
###### acl

- Schema name: `Acl`
- Type: boolean
- Default: true

If set, enable mapping of local filesystem ACLs to NT ACLs for SMB clients.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_afp"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_afp"></a>
###### afp

- Schema name: `Afp`
- Type: boolean
- Default: false

If set, SMB server will read and store file metadata in an on-disk format compatible with the legacy AFP file server. WARNING: This should not be set unless the SMB server is sharing data that was originally written via the AFP protocol.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_timemachine"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_timemachine"></a>
###### timemachine

- Schema name: `Timemachine`
- Type: boolean
- Default: false

If set, MacOS clients can use the share as a time machine target.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_timemachine_quota"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_timemachine_quota"></a>
###### timemachine_quota

- Schema name: `Timemachine Quota`
- Type: integer
- Default: 0

If set, it defines the maximum size of a single time machine sparsebundle volume by limiting the reported disk size to the SMB client. A value of zero means no quota is applied to the share. NOTE: Modern MacOS versions you set Time Machine quotas client-side. This gives more predictable server and client behavior.
- Value must be greater or equal to `0` and lesser or equal to `109951162777600`

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_aapl_name_mangling"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_vuid"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_vuid"></a>
###### vuid

- Schema name: `Vuid`
- Default: null

This value is the Time Machine volume UUID for the SMB share. The TrueNAS server uses this value in the mDNS advertisement for the Time Machine share. MacOS clients may use it to identify the volume. When you create or update a share, setting this value to null makes the TrueNAS server generate a new UUID for the share.
<a id="Return_value_options_anyOf_i0_oneOf_i0_vuid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i0_vuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_options_anyOf_i0_oneOf_i0_vuid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i0_vuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_options_anyOf_i0_oneOf_i0_vuid_anyOf_i1)

- Type: null

Examples:

```json
"d12aafdc-a7ac-4e3c-8bbd-6001f7f19819"
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i0_auxsmbconf"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i0_auxsmbconf"></a>
###### auxsmbconf

- Schema name: `Auxsmbconf`
- Type: string
- Default: ""

Additional parameters to set on the SMB share. Parameters must be separated by the new-line character. WARNING: These parameters are not validated and may cause undefined server behavior including data corruption or data loss. WARNING: Auxiliary parameters are an unsupported configuration.
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i1"></a>
###### [DefaultOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i1)

- Schema name: `DefaultOpt`
- Type: object

These configuration options apply to shares with the `DEFAULT_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i1_aapl_name_mangling"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i1_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i1_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i1_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i1_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i1_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i1_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i1_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i2"></a>
###### [TimeMachineOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i2)

- Schema name: `TimeMachineOpt`
- Type: object

These configuration options apply to shares with the `TIMEMACHINE_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_timemachine_quota"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_timemachine_quota"></a>
###### timemachine_quota

- Schema name: `Timemachine Quota`
- Type: integer
- Default: 0

If set, it defines the maximum size in bytes of a single time machine sparsebundle volume by limiting the reported disk size to the SMB client. A value of zero means no quota is set. NOTE: Modern MacOS versions you set Time Machine quotas client-side. This gives more predictable server and client behavior.
- Value must be greater or equal to `0` and lesser or equal to `109951162777600`

<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_auto_snapshot"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_auto_snapshot"></a>
###### auto_snapshot

- Schema name: `Auto Snapshot`
- Type: boolean
- Default: false

If set, the server makes a ZFS snapshot of the share dataset when the client makes a new Time Machine backup.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_auto_dataset_creation"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_auto_dataset_creation"></a>
###### auto_dataset_creation

- Schema name: `Auto Dataset Creation`
- Type: boolean
- Default: false

If set, the server uses the `dataset_naming_schema` to make a new ZFS dataset when the client connects. The server uses this dataset as the share path during the SMB session. NOTE: this setting requires the share path to be a dataset mountpoint.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema"></a>
###### dataset_naming_schema

- Schema name: `Dataset Naming Schema`
- Default: null

The naming schema to use when `auto_dataset_creation` is specified. If you do not set a schema, the server uses `%U` (username) if it is not joined to Active Directory. If the server is joined to Active Directory it uses `%D/%U` (domain/username). See the `VARIABLE SUBSTITUTIONS` section in the smb.conf manpage for valid strings. WARNING: ZFS dataset naming rules are more restrictive than normal path rules. For example, if `%u` is specified then the character `\` may be inserted in the username (which is not supported in ZFS).
<a id="Return_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_options_anyOf_i0_oneOf_i2_dataset_naming_schema_anyOf_i1)

- Type: null

Examples:

```json
"%D/%U"
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_vuid"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_vuid"></a>
###### vuid

- Schema name: `Vuid`
- Default: null

This value is the Time Machine volume UUID for the SMB share. The TrueNAS server uses this value in the mDNS advertisement for the Time Machine share. MacOS clients may use it to identify the volume. When you create or update a share, setting this value to null makes the TrueNAS server generate a new UUID for the share.
<a id="Return_value_options_anyOf_i0_oneOf_i2_vuid_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i2_vuid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_options_anyOf_i0_oneOf_i2_vuid_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i2_vuid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_options_anyOf_i0_oneOf_i2_vuid_anyOf_i1)

- Type: null

Examples:

```json
"d12aafdc-a7ac-4e3c-8bbd-6001f7f19819"
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i2_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i2_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i2_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i2_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i3"></a>
###### [MultiprotocolOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i3)

- Schema name: `MultiprotocolOpt`
- Type: object

These configuration options apply to shares with the `MULTIPROTOCOL_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i3_aapl_name_mangling"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i3_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i3_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i3_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i3_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i3_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i3_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i3_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i4"></a>
###### [TimeLockedOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i4)

- Schema name: `TimeLockedOpt`
- Type: object

These configuration options apply to shares with the `TIME_LOCKED_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i4_grace_period"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i4_grace_period"></a>
###### grace_period

- Schema name: `Grace Period`
- Type: integer
- Default: 900

Time in seconds when write access to the file or directory is allowed.
- Value must be greater or equal to `60` and lesser or equal to `15552000`

<a id="headingReturn_value_options_anyOf_i0_oneOf_i4_aapl_name_mangling"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i4_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i4_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i4_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i4_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i4_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i4_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i4_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i5"></a>
###### [PrivateDatasetOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i5)

- Schema name: `PrivateDatasetOpt`
- Type: object

These configuration options apply to shares with the `PRIVATE_DATASETS_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema"></a>
###### dataset_naming_schema

- Schema name: `Dataset Naming Schema`
- Default: null

The naming schema to use. If you do not set a schema, the server uses `%U` (username) if it is not joined to Active Directory. If the server is joined to Active Directory it uses `%D/%U` (domain/username). WARNING: ZFS dataset naming rules are more restrictive than normal path rules.
<a id="Return_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_options_anyOf_i0_oneOf_i5_dataset_naming_schema_anyOf_i1)

- Type: null

Examples:

```json
"%D/%U"
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i5_auto_quota"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i5_auto_quota"></a>
###### auto_quota

- Schema name: `Auto Quota`
- Type: integer
- Default: 0

Set the specified ZFS quota (in gibibytes) on new datasets. If the value is zero, TrueNAS disables automatic quotas for the share.
- Value must be greater or equal to `0`
Examples:

```json
10
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i5_aapl_name_mangling"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i5_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

<a id="headingReturn_value_options_anyOf_i0_oneOf_i5_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i5_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i5_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i5_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i5_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i5_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i6"></a>
###### [ExternalOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i6)

- Schema name: `ExternalOpt`
- Type: object

These configuration options apply to shares with the `EXTERNAL_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i6_remote_path"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i6_remote_path"></a>
###### remote_path (required)

- Schema name: `Remote Path`
- Type: array of string

This is the path to the external server and share. Each server entry must include a full domain name or IP address and share name. Separate the server and share with the `\` character. WARNING: The SMB server and TrueNAS middleware do not check if external paths are reachable.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i6_remote_path_items"></a>
- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "192.168.0.200\\SHARE"
]
```
Examples:

```json
[
    "SERVER1.MYDOM.INTERNAL\\SHARE"
]
```
Examples:

```json
[
    "SERVER1.MYDOM.INTERNAL\\SHARE, SERVER2.MYDOM.INTERNAL\\SHARE"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i7"></a>
###### [VeeamRepositoryOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i7)

- Schema name: `VeeamRepositoryOpt`
- Type: object

These configuration options apply to shares with the `VEEAM_REPOSITORY_SHARE` purpose.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i7_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i7_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i7_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i7_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i7_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i7_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i0_oneOf_i8"></a>
###### [FCPStorageOpt](#tab-pane_Return_value_options_anyOf_i0_oneOf_i8)

- Schema name: `FCPStorageOpt`
- Type: object

These configuration options apply to shares with the `FCP_SHARE` purpose as a storage location for Final Cut Pro data.
- No Additional Properties
<a id="headingReturn_value_options_anyOf_i0_oneOf_i8_aapl_name_mangling"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i8_aapl_name_mangling"></a>
###### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: const
- Default: true

Illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients.
- Specific value: `true`

<a id="headingReturn_value_options_anyOf_i0_oneOf_i8_hostsallow"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i8_hostsallow"></a>
###### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i8_hostsallow_items"></a>
- Type: string

Examples:

```json
[
    "192.168.0.200",
    "150.203."
]
```
Examples:

```json
[
    "150.203.15.0/255.255.255.0"
]
```
Examples:

```json
[
    "150.203. EXCEPT 150.203.6.66"
]
```

<a id="headingReturn_value_options_anyOf_i0_oneOf_i8_hostsdeny"></a>
<a id="Return_value_options_anyOf_i0_oneOf_i8_hostsdeny"></a>
###### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_options_anyOf_i0_oneOf_i8_hostsdeny_items"></a>
- Type: string

Examples:

```json
[
    "150.203.4."
]
```
Examples:

```json
[
    "ALL"
]
```
Examples:

```json
[
    "0.0.0.0/0"
]
```

<a id="tab-pane_Return_value_options_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_options_anyOf_i1)

- Type: null

Examples:

```json
{
    "auto_snapshot": true
}
```
Examples:

```json
{
    "auto_quota": 100
}
```

<a id="headingReturn_value_tier"></a>
<a id="Return_value_tier"></a>
#### tier

- Default: null

Storage tier in which the share's underlying dataset is located. This field is read-only; configure the dataset's tier via `zfs.tier.dataset_set_tier`. NOTE: this is a licensed feature. Will be `null` if TrueNAS is unlicensed, if tiering is disabled, or if the pool has no SPECIAL vdev.
<a id="Return_value_tier_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_Return_value_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_type"></a>
<a id="Return_value_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_tier_anyOf_i0_tier_job"></a>
<a id="Return_value_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="Return_value_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_tier_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
