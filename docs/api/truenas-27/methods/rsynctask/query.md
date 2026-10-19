---
title: rsynctask.query
kind: method
source_rst: _sources/api_methods_rsynctask.query.rst.txt
source_html: api_methods_rsynctask.query.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# rsynctask.query

## Required Roles

- `SNAPSHOT_TASK_READ`

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

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

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
###### RsyncTaskQueryResultItem

- Schema name: `RsyncTaskQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the rsync task.

<a id="headingReturn_value_anyOf_i0_items_path"></a>
<a id="Return_value_anyOf_i0_items_path"></a>
###### path

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

<a id="headingReturn_value_anyOf_i0_items_dataset"></a>
<a id="Return_value_anyOf_i0_items_dataset"></a>
###### dataset

- Schema name: `Dataset`

The ZFS dataset containing the rsync task path (e.g., 'tank/data'). Returns `null` if the path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
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
###### relative_path

- Schema name: `Relative Path`

The path of the rsync task relative to the dataset mountpoint (e.g., 'backups/daily'). An empty string indicates the task path is at the dataset root. Returns `null` if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="Return_value_anyOf_i0_items_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_user"></a>
<a id="Return_value_anyOf_i0_items_user"></a>
###### user

- Schema name: `User`
- Type: string

Username to run the rsync task as.

<a id="headingReturn_value_anyOf_i0_items_mode"></a>
<a id="Return_value_anyOf_i0_items_mode"></a>
###### mode

- Schema name: `Mode`
- Type: enum (of string)

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.
###### Must be one of:

- "MODULE"
- "SSH"

<a id="headingReturn_value_anyOf_i0_items_remotehost"></a>
<a id="Return_value_anyOf_i0_items_remotehost"></a>
###### remotehost

- Schema name: `Remotehost`

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
<a id="Return_value_anyOf_i0_items_remotehost_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_remotehost_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_remotehost_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_remotehost_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_remotehost_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_remoteport"></a>
<a id="Return_value_anyOf_i0_items_remoteport"></a>
###### remoteport

- Schema name: `Remoteport`

Port number for SSH connection. Only applies when `mode` is SSH.
<a id="Return_value_anyOf_i0_items_remoteport_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_remoteport_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_remoteport_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_remoteport_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_remoteport_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_remotemodule"></a>
<a id="Return_value_anyOf_i0_items_remotemodule"></a>
###### remotemodule

- Schema name: `Remotemodule`

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
<a id="Return_value_anyOf_i0_items_remotemodule_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_remotemodule_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_remotemodule_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_remotemodule_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_remotemodule_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials"></a>
###### ssh_credentials

In SSH mode, if `ssh_credentials` (a keychain credential of `SSH_CREDENTIALS` type) is specified then it is used to connect to the remote host. If it is not specified, then keys in `user`'s .ssh directory are used.
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0"></a>
###### [KeychainCredentialEntry](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_id"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_name"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_type"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
###### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingReturn_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
<a id="Return_value_anyOf_i0_items_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_remotepath"></a>
<a id="Return_value_anyOf_i0_items_remotepath"></a>
###### remotepath

- Schema name: `Remotepath`
- Type: string

Path on the remote system to synchronize with.

<a id="headingReturn_value_anyOf_i0_items_direction"></a>
<a id="Return_value_anyOf_i0_items_direction"></a>
###### direction

- Schema name: `Direction`
- Type: enum (of string)

Specify if data should be PULLED or PUSHED from the remote system.
###### Must be one of:

- "PULL"
- "PUSH"

<a id="headingReturn_value_anyOf_i0_items_desc"></a>
<a id="Return_value_anyOf_i0_items_desc"></a>
###### desc

- Schema name: `Desc`
- Type: string

Description of the rsync task.

<a id="headingReturn_value_anyOf_i0_items_schedule"></a>
<a id="Return_value_anyOf_i0_items_schedule"></a>
###### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_schedule_minute"></a>
<a id="Return_value_anyOf_i0_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

<a id="headingReturn_value_anyOf_i0_items_schedule_hour"></a>
<a id="Return_value_anyOf_i0_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingReturn_value_anyOf_i0_items_schedule_dom"></a>
<a id="Return_value_anyOf_i0_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingReturn_value_anyOf_i0_items_schedule_month"></a>
<a id="Return_value_anyOf_i0_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingReturn_value_anyOf_i0_items_schedule_dow"></a>
<a id="Return_value_anyOf_i0_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_anyOf_i0_items_recursive"></a>
<a id="Return_value_anyOf_i0_items_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean

Recursively transfer subdirectories.

<a id="headingReturn_value_anyOf_i0_items_times"></a>
<a id="Return_value_anyOf_i0_items_times"></a>
###### times

- Schema name: `Times`
- Type: boolean

Preserve modification times of files.

<a id="headingReturn_value_anyOf_i0_items_compress"></a>
<a id="Return_value_anyOf_i0_items_compress"></a>
###### compress

- Schema name: `Compress`
- Type: boolean

Reduce the size of the data to be transmitted.

<a id="headingReturn_value_anyOf_i0_items_archive"></a>
<a id="Return_value_anyOf_i0_items_archive"></a>
###### archive

- Schema name: `Archive`
- Type: boolean

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

<a id="headingReturn_value_anyOf_i0_items_delete"></a>
<a id="Return_value_anyOf_i0_items_delete"></a>
###### delete

- Schema name: `Delete`
- Type: boolean

Delete files in the destination directory that do not exist in the source directory.

<a id="headingReturn_value_anyOf_i0_items_quiet"></a>
<a id="Return_value_anyOf_i0_items_quiet"></a>
###### quiet

- Schema name: `Quiet`
- Type: boolean

Suppress informational messages from rsync.

<a id="headingReturn_value_anyOf_i0_items_preserveperm"></a>
<a id="Return_value_anyOf_i0_items_preserveperm"></a>
###### preserveperm

- Schema name: `Preserveperm`
- Type: boolean

Preserve original file permissions.

<a id="headingReturn_value_anyOf_i0_items_preserveattr"></a>
<a id="Return_value_anyOf_i0_items_preserveattr"></a>
###### preserveattr

- Schema name: `Preserveattr`
- Type: boolean

Preserve extended attributes of files.

<a id="headingReturn_value_anyOf_i0_items_delayupdates"></a>
<a id="Return_value_anyOf_i0_items_delayupdates"></a>
###### delayupdates

- Schema name: `Delayupdates`
- Type: boolean

Delay updating destination files until all transfers are complete.

<a id="headingReturn_value_anyOf_i0_items_extra"></a>
<a id="Return_value_anyOf_i0_items_extra"></a>
###### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_extra_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_items_enabled"></a>
<a id="Return_value_anyOf_i0_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this rsync task is enabled.

<a id="headingReturn_value_anyOf_i0_items_locked"></a>
<a id="Return_value_anyOf_i0_items_locked"></a>
###### locked

- Schema name: `Locked`
- Type: boolean

Whether this rsync task is currently locked (running).

<a id="headingReturn_value_anyOf_i0_items_job"></a>
<a id="Return_value_anyOf_i0_items_job"></a>
###### job

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
<a id="Return_value_anyOf_i0_items_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_job_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_job_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [RsyncTaskQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `RsyncTaskQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the rsync task.

<a id="headingReturn_value_anyOf_i1_path"></a>
<a id="Return_value_anyOf_i1_path"></a>
###### path

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

<a id="headingReturn_value_anyOf_i1_dataset"></a>
<a id="Return_value_anyOf_i1_dataset"></a>
###### dataset

- Schema name: `Dataset`

The ZFS dataset containing the rsync task path (e.g., 'tank/data'). Returns `null` if the path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
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
###### relative_path

- Schema name: `Relative Path`

The path of the rsync task relative to the dataset mountpoint (e.g., 'backups/daily'). An empty string indicates the task path is at the dataset root. Returns `null` if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="Return_value_anyOf_i1_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_user"></a>
<a id="Return_value_anyOf_i1_user"></a>
###### user

- Schema name: `User`
- Type: string

Username to run the rsync task as.

<a id="headingReturn_value_anyOf_i1_mode"></a>
<a id="Return_value_anyOf_i1_mode"></a>
###### mode

- Schema name: `Mode`
- Type: enum (of string)

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.
###### Must be one of:

- "MODULE"
- "SSH"

<a id="headingReturn_value_anyOf_i1_remotehost"></a>
<a id="Return_value_anyOf_i1_remotehost"></a>
###### remotehost

- Schema name: `Remotehost`

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
<a id="Return_value_anyOf_i1_remotehost_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_remotehost_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_remotehost_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_remotehost_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_remotehost_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_remoteport"></a>
<a id="Return_value_anyOf_i1_remoteport"></a>
###### remoteport

- Schema name: `Remoteport`

Port number for SSH connection. Only applies when `mode` is SSH.
<a id="Return_value_anyOf_i1_remoteport_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_remoteport_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_remoteport_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_remoteport_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_remoteport_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_remotemodule"></a>
<a id="Return_value_anyOf_i1_remotemodule"></a>
###### remotemodule

- Schema name: `Remotemodule`

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
<a id="Return_value_anyOf_i1_remotemodule_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_remotemodule_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_remotemodule_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_remotemodule_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_remotemodule_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_ssh_credentials"></a>
<a id="Return_value_anyOf_i1_ssh_credentials"></a>
###### ssh_credentials

In SSH mode, if `ssh_credentials` (a keychain credential of `SSH_CREDENTIALS` type) is specified then it is used to connect to the remote host. If it is not specified, then keys in `user`'s .ssh directory are used.
<a id="Return_value_anyOf_i1_ssh_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_ssh_credentials_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_ssh_credentials_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_remotepath"></a>
<a id="Return_value_anyOf_i1_remotepath"></a>
###### remotepath

- Schema name: `Remotepath`
- Type: string

Path on the remote system to synchronize with.

<a id="headingReturn_value_anyOf_i1_direction"></a>
<a id="Return_value_anyOf_i1_direction"></a>
###### direction

- Schema name: `Direction`
- Type: enum (of string)

Specify if data should be PULLED or PUSHED from the remote system.
###### Must be one of:

- "PULL"
- "PUSH"

<a id="headingReturn_value_anyOf_i1_desc"></a>
<a id="Return_value_anyOf_i1_desc"></a>
###### desc

- Schema name: `Desc`
- Type: string

Description of the rsync task.

<a id="headingReturn_value_anyOf_i1_schedule"></a>
<a id="Return_value_anyOf_i1_schedule"></a>
###### schedule

- Type: object

Cron schedule for when the rsync task should run.

<a id="headingReturn_value_anyOf_i1_recursive"></a>
<a id="Return_value_anyOf_i1_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean

Recursively transfer subdirectories.

<a id="headingReturn_value_anyOf_i1_times"></a>
<a id="Return_value_anyOf_i1_times"></a>
###### times

- Schema name: `Times`
- Type: boolean

Preserve modification times of files.

<a id="headingReturn_value_anyOf_i1_compress"></a>
<a id="Return_value_anyOf_i1_compress"></a>
###### compress

- Schema name: `Compress`
- Type: boolean

Reduce the size of the data to be transmitted.

<a id="headingReturn_value_anyOf_i1_archive"></a>
<a id="Return_value_anyOf_i1_archive"></a>
###### archive

- Schema name: `Archive`
- Type: boolean

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

<a id="headingReturn_value_anyOf_i1_delete"></a>
<a id="Return_value_anyOf_i1_delete"></a>
###### delete

- Schema name: `Delete`
- Type: boolean

Delete files in the destination directory that do not exist in the source directory.

<a id="headingReturn_value_anyOf_i1_quiet"></a>
<a id="Return_value_anyOf_i1_quiet"></a>
###### quiet

- Schema name: `Quiet`
- Type: boolean

Suppress informational messages from rsync.

<a id="headingReturn_value_anyOf_i1_preserveperm"></a>
<a id="Return_value_anyOf_i1_preserveperm"></a>
###### preserveperm

- Schema name: `Preserveperm`
- Type: boolean

Preserve original file permissions.

<a id="headingReturn_value_anyOf_i1_preserveattr"></a>
<a id="Return_value_anyOf_i1_preserveattr"></a>
###### preserveattr

- Schema name: `Preserveattr`
- Type: boolean

Preserve extended attributes of files.

<a id="headingReturn_value_anyOf_i1_delayupdates"></a>
<a id="Return_value_anyOf_i1_delayupdates"></a>
###### delayupdates

- Schema name: `Delayupdates`
- Type: boolean

Delay updating destination files until all transfers are complete.

<a id="headingReturn_value_anyOf_i1_extra"></a>
<a id="Return_value_anyOf_i1_extra"></a>
###### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_extra_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i1_enabled"></a>
<a id="Return_value_anyOf_i1_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this rsync task is enabled.

<a id="headingReturn_value_anyOf_i1_locked"></a>
<a id="Return_value_anyOf_i1_locked"></a>
###### locked

- Schema name: `Locked`
- Type: boolean

Whether this rsync task is currently locked (running).

<a id="headingReturn_value_anyOf_i1_job"></a>
<a id="Return_value_anyOf_i1_job"></a>
###### job

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
<a id="Return_value_anyOf_i1_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_job_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_job_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
