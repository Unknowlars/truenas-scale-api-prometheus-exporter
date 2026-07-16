---
title: sharing.smb.get_instance
kind: method
source_rst: _sources/api_methods_sharing.smb.get_instance.rst.txt
source_html: api_methods_sharing.smb.get_instance.html
required_roles:
  - SHARING_SMB_READ
---

# sharing.smb.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `SHARING_SMB_READ`

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

- Schema name: `SmbShareEntry`
- Type: object

SMB share entry on the TrueNAS server.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this SMB share.

#### purpose

- Schema name: `Purpose`
- Type: enum (of string)
- Default: "DEFAULT_SHARE"

This parameter sets the purpose of the SMB share. It controls how the SMB share behaves and what features are available through options. The DEFAULT_SHARE setting is best for most applications, and should be used, unless there is a specific reason to change it. `DEFAULT_SHARE`: Set the SMB share for best compatibility with common SMB clients. `LEGACY_SHARE`: Set the SMB share for compatibility with older TrueNAS versions. Automated backend migrations use this to help the administrator move to better-supported share settings. It should not be used for new SMB shares. `TIMEMACHINE_SHARE`: The SMB share is presented to MacOS clients as a time machine target. NOTE: `aapl_extensions` must be set in the global `smb.config`. `MULTIPROTOCOL_SHARE`: The SMB share is configured for multi-protocol access. Set this if the `path` is shared through NFS, FTP, or used by containers or apps. NOTE: This setting can reduce SMB share performance because it turns off some SMB features for safer interoperability with external processes. `TIME_LOCKED_SHARE`: The SMB share makes files read-only through the SMB protocol after the set grace_period ends. WARNING: This setting does not work if the `path` is accessed locally or if another SMB share without the `TIME_LOCKED_SHARE` purpose uses the same path. WARNING: This setting might not meet regulatory requirements for write-once storage. `PRIVATE_DATASETS_SHARE`: The server uses the specified `dataset_naming_schema` in `options` to make a new ZFS dataset when the client connects. The server uses this dataset as the share path during the SMB session. `EXTERNAL_SHARE`: The SMB share is a DFS proxy to a share hosted on an external SMB server. `VEEAM_REPOSITORY_SHARE`: The SMB share is a repository for Veeam Backup & Replication and supports Fast Clone. NOTE: This feature is available only for TrueNAS Enterprise customers. `FCP_SHARE`: The SMB share is a used for Final Cut Pro storage. This feature automatically configures the share to provide storage according to Apple support guidelines described in https://support.apple.com/en-ca/101919. NOTE: `aapl_extensions` must be set in the global `smb.config`. WARNING: This feature forcibly enables `aapl_name_mangling` on the SMB share which may cause unexpected behavior for data that was written without this feature enabled.

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

#### path (required)

- Schema name: `Path`

Local server path to share by using the SMB protocol. The path must start with `/mnt/` and must be in a ZFS pool. Use the string `EXTERNAL` if the share works as a DFS proxy. WARNING: The TrueNAS server does not check if external paths are reachable.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: const

Examples:

```json
"/mnt/dozer/SHARE"
```
Examples:

```json
"EXTERNAL"
```

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

If unset, the SMB share is not available over the SMB protocol.

#### comment

- Schema name: `Comment`
- Type: string
- Default: ""

Text field that is seen next to a share when an SMB client requests a list of SMB shares on the TrueNAS server.
Examples:

```json
"Mammalian nurturable"
```

#### readonly

- Schema name: `Readonly`
- Type: boolean
- Default: false

If set, SMB clients cannot create or change files and directories in the SMB share. NOTE: If set, the share path is still writeable by local processes or other file sharing protocols.

#### browsable

- Schema name: `Browsable`
- Type: boolean
- Default: true

If set, the share is included when an SMB client requests a list of SMB shares on the TrueNAS server.

#### access_based_share_enumeration

- Schema name: `Access Based Share Enumeration`
- Type: boolean
- Default: false

If set, the share is only included when an SMB client requests a list of shares on the SMB server if the share (not filesystem) access control list (see `sharing.smb.getacl`) grants access to the user.

#### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
##### Any of

###### Option 1

- Type: boolean

###### Option 2

- Type: null

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
##### enable

- Schema name: `Enable`
- Type: boolean
- Default: false

Turn on auditing for the SMB share. SMB share auditing may not be enabled if `enable_smb1` is `true` in the SMB service configuration.

##### watch_list

- Schema name: `Watch List`
- Type: array of string
- Default: []

Only audit the listed group accounts. If the list is empty, all groups will be audited.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "interns",
    "contractors"
]
```

##### ignore_list

- Schema name: `Ignore List`
- Type: array of string
- Default: []

List of groups that will not be audited.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

Examples:

```json
[
    "automation",
    "apps"
]
```

#### options

- Schema name: `Options`
- Default: null

Additional configuration related to the configured SMB share purpose. If null, then the default options related to the share purpose will be applied.
##### Any of

###### Option 1

###### Option 2

- Schema name: `LegacyOpt`
- Type: object

These configuration options apply to shares with the `LEGACY_SHARE` purpose.
- No Additional Properties
####### recyclebin

- Schema name: `Recyclebin`
- Type: boolean
- Default: false

If set, deleted files are moved to per-user subdirectories in the `.recycle` directory. The SMB server creates the `.recycle` directory at the root of the SMB share if the file is in the same ZFS dataset as the share `path`. If the file is in a child ZFS dataset, the server uses the `mountpoint` of that dataset to create the `.recycle` directory. NOTE: This feature does not work with recycle bin features in client operating systems. WARNING: Do not use this feature instead of backups or ZFS snapshots.

####### path_suffix

- Schema name: `Path Suffix`
- Default: null

Path suffix template for dynamic path generation. Uses SMB variable substitution patterns like `%D` (domain) and `%U` (username).
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

Examples:

```json
"%D/%U"
```

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

####### guestok

- Schema name: `Guestok`
- Type: boolean
- Default: false

If set, guest access to the share is allowed. This should not be used in production environments. NOTE: If a user account does not exist, the SMB server maps access to the guest account. WARNING: Additional client-side configuration downgrading security settings may be required in order to use this feature.

####### streams

- Schema name: `Streams`
- Type: boolean
- Default: true

If set, support for SMB alternate data streams is enabled. WARNING: This value should not be changed once data is written to the SMB share.

####### durablehandle

- Schema name: `Durablehandle`
- Type: boolean
- Default: true

If set, support for SMB durable handles is enabled. WARNING: This feature is incompatible with multiprotocol and local filesystem access.

####### shadowcopy

- Schema name: `Shadowcopy`
- Type: boolean
- Default: true

If set, previous versions of files contained in ZFS snapshots are accessible through standard SMB protocol operations on previous versions of files.

####### fsrvp

- Schema name: `Fsrvp`
- Type: boolean
- Default: false

If set, enable support for the File Server Remote VSS Protocol. This allows clients to manage snapshots for the specified SMB share.

####### home

- Schema name: `Home`
- Type: boolean
- Default: false

Use the `path` to store user home directories. Each user has a personal home directory and share. Users cannot access other user directories when connecting to shares. NOTE: This parameter changes the share `name` to `homes`. It also creates a dynamic share that mirrors the username of the user. Both shares use the same `path`. You can hide the homes share by turning off `browsable`. The dynamic user home share cannot be hidden. WARNING: This parameter changes the global server configuration. The SMB server will not authenticate users without a valid home directory or shell.

####### acl

- Schema name: `Acl`
- Type: boolean
- Default: true

If set, enable mapping of local filesystem ACLs to NT ACLs for SMB clients.

####### afp

- Schema name: `Afp`
- Type: boolean
- Default: false

If set, SMB server will read and store file metadata in an on-disk format compatible with the legacy AFP file server. WARNING: This should not be set unless the SMB server is sharing data that was originally written via the AFP protocol.

####### timemachine

- Schema name: `Timemachine`
- Type: boolean
- Default: false

If set, MacOS clients can use the share as a time machine target.

####### timemachine_quota

- Schema name: `Timemachine Quota`
- Type: integer
- Default: 0

If set, it defines the maximum size of a single time machine sparsebundle volume by limiting the reported disk size to the SMB client. A value of zero means no quota is applied to the share. NOTE: Modern MacOS versions you set Time Machine quotas client-side. This gives more predictable server and client behavior.
- Value must be greater or equal to `0` and lesser or equal to `109951162777600`

####### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

####### vuid

- Schema name: `Vuid`
- Default: null

This value is the Time Machine volume UUID for the SMB share. The TrueNAS server uses this value in the mDNS advertisement for the Time Machine share. MacOS clients may use it to identify the volume. When you create or update a share, setting this value to null makes the TrueNAS server generate a new UUID for the share.
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

Examples:

```json
"d12aafdc-a7ac-4e3c-8bbd-6001f7f19819"
```

####### auxsmbconf

- Schema name: `Auxsmbconf`
- Type: string
- Default: ""

Additional parameters to set on the SMB share. Parameters must be separated by the new-line character. WARNING: These parameters are not validated and may cause undefined server behavior including data corruption or data loss. WARNING: Auxiliary parameters are an unsupported configuration.

###### LegacyOpt

- Type: string
- Must be at least `1` characters long

###### DefaultOpt

- Type: null

###### TimeMachineOpt

- Type: string
- Must be at least `1` characters long

###### MultiprotocolOpt

- Type: null

###### TimeLockedOpt

- Schema name: `DefaultOpt`
- Type: object

These configuration options apply to shares with the `DEFAULT_SHARE` purpose.
- No Additional Properties
####### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### PrivateDatasetOpt

- Schema name: `TimeMachineOpt`
- Type: object

These configuration options apply to shares with the `TIMEMACHINE_SHARE` purpose.
- No Additional Properties
####### timemachine_quota

- Schema name: `Timemachine Quota`
- Type: integer
- Default: 0

If set, it defines the maximum size in bytes of a single time machine sparsebundle volume by limiting the reported disk size to the SMB client. A value of zero means no quota is set. NOTE: Modern MacOS versions you set Time Machine quotas client-side. This gives more predictable server and client behavior.
- Value must be greater or equal to `0` and lesser or equal to `109951162777600`

####### auto_snapshot

- Schema name: `Auto Snapshot`
- Type: boolean
- Default: false

If set, the server makes a ZFS snapshot of the share dataset when the client makes a new Time Machine backup.

####### auto_dataset_creation

- Schema name: `Auto Dataset Creation`
- Type: boolean
- Default: false

If set, the server uses the `dataset_naming_schema` to make a new ZFS dataset when the client connects. The server uses this dataset as the share path during the SMB session. NOTE: this setting requires the share path to be a dataset mountpoint.

####### dataset_naming_schema

- Schema name: `Dataset Naming Schema`
- Default: null

The naming schema to use when `auto_dataset_creation` is specified. If you do not set a schema, the server uses `%U` (username) if it is not joined to Active Directory. If the server is joined to Active Directory it uses `%D/%U` (domain/username). See the `VARIABLE SUBSTITUTIONS` section in the smb.conf manpage for valid strings. WARNING: ZFS dataset naming rules are more restrictive than normal path rules. For example, if `%u` is specified then the character `\` may be inserted in the username (which is not supported in ZFS).
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

Examples:

```json
"%D/%U"
```

####### vuid

- Schema name: `Vuid`
- Default: null

This value is the Time Machine volume UUID for the SMB share. The TrueNAS server uses this value in the mDNS advertisement for the Time Machine share. MacOS clients may use it to identify the volume. When you create or update a share, setting this value to null makes the TrueNAS server generate a new UUID for the share.
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

Examples:

```json
"d12aafdc-a7ac-4e3c-8bbd-6001f7f19819"
```

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### ExternalOpt

- Type: string

###### VeeamRepositoryOpt

- Type: null

###### FCPStorageOpt

- Type: string
- Must be at least `1` characters long

###### Option 1

- Type: null

###### Option 2

- Schema name: `MultiprotocolOpt`
- Type: object

These configuration options apply to shares with the `MULTIPROTOCOL_SHARE` purpose.
- No Additional Properties
####### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### Option 1

- Schema name: `TimeLockedOpt`
- Type: object

These configuration options apply to shares with the `TIME_LOCKED_SHARE` purpose.
- No Additional Properties
####### grace_period

- Schema name: `Grace Period`
- Type: integer
- Default: 900

Time in seconds when write access to the file or directory is allowed.
- Value must be greater or equal to `60` and lesser or equal to `15552000`

####### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### Option 2

- Schema name: `PrivateDatasetOpt`
- Type: object

These configuration options apply to shares with the `PRIVATE_DATASETS_SHARE` purpose.
- No Additional Properties
####### dataset_naming_schema

- Schema name: `Dataset Naming Schema`
- Default: null

The naming schema to use. If you do not set a schema, the server uses `%U` (username) if it is not joined to Active Directory. If the server is joined to Active Directory it uses `%D/%U` (domain/username). WARNING: ZFS dataset naming rules are more restrictive than normal path rules.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

Examples:

```json
"%D/%U"
```

####### auto_quota

- Schema name: `Auto Quota`
- Type: integer
- Default: 0

Set the specified ZFS quota (in gibibytes) on new datasets. If the value is zero, TrueNAS disables automatic quotas for the share.
- Value must be greater or equal to `0`
Examples:

```json
10
```

####### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: boolean
- Default: false

If set, illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients. WARNING: This value should not be changed once data is written to the SMB share.

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### Option 1

- Type: string

###### Option 2

- Type: null

###### Option 1

- Schema name: `ExternalOpt`
- Type: object

These configuration options apply to shares with the `EXTERNAL_SHARE` purpose.
- No Additional Properties
####### remote_path (required)

- Schema name: `Remote Path`
- Type: array of string

This is the path to the external server and share. Each server entry must include a full domain name or IP address and share name. Separate the server and share with the `\` character. WARNING: The SMB server and TrueNAS middleware do not check if external paths are reachable.
- No Additional Items

######## Each item of this array must be:

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

###### Option 2

- Schema name: `VeeamRepositoryOpt`
- Type: object

These configuration options apply to shares with the `VEEAM_REPOSITORY_SHARE` purpose.
- No Additional Properties
####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### Option 1

- Schema name: `FCPStorageOpt`
- Type: object

These configuration options apply to shares with the `FCP_SHARE` purpose as a storage location for Final Cut Pro data.
- No Additional Properties
####### aapl_name_mangling

- Schema name: `Aapl Name Mangling`
- Type: const
- Default: true

Illegal NTFS characters commonly used by MacOS clients are stored with their native values on the SMB server's local filesystem. NOTE: Files with illegal NTFS characters in their names may not be accessible to non-MacOS SMB clients.

####### hostsallow

- Schema name: `Hostsallow`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are allowed to access the SMB share. The EXCEPT keyword may be used to limit a wildcard list. NOTE: Hostname lookups are disabled on the SMB server for performance reasons.
- No Additional Items

######## Each item of this array must be:

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

####### hostsdeny

- Schema name: `Hostsdeny`
- Type: array of string
- Default: []

A list of IP addresses or subnets that are not allowed to access the SMB share. The keyword `ALL` or the netmask `0.0.0.0/0` may be used to deny all by default.
- No Additional Items

######## Each item of this array must be:

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

###### Option 2

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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
