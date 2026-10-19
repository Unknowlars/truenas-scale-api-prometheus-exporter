---
title: rsynctask.update
kind: method
source_rst: _sources/api_methods_rsynctask.update.rst.txt
source_html: api_methods_rsynctask.update.html
required_roles:
  - SNAPSHOT_TASK_WRITE
---

# rsynctask.update

## Summary

Update Rsync Task of `id`.

## Required Roles

- `SNAPSHOT_TASK_WRITE`

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

ID of the rsync task to update.

#### Parameter 2: rsync_task_update

<a id="Call_parameters_items_i1"></a>
#### rsync_task_update

- Schema name: `rsync_task_update`
- Type: object

Updated configuration for the rsync task.
- No Additional Properties
<a id="headingCall_parameters_items_i1_path"></a>
<a id="Call_parameters_items_i1_path"></a>
##### path

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

<a id="headingCall_parameters_items_i1_user"></a>
<a id="Call_parameters_items_i1_user"></a>
##### user

- Schema name: `User`
- Type: string

Username to run the rsync task as.

<a id="headingCall_parameters_items_i1_mode"></a>
<a id="Call_parameters_items_i1_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.
###### Must be one of:

- "MODULE"
- "SSH"

<a id="headingCall_parameters_items_i1_remotehost"></a>
<a id="Call_parameters_items_i1_remotehost"></a>
##### remotehost

- Schema name: `Remotehost`

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
<a id="Call_parameters_items_i1_remotehost_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_remotehost_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_remotehost_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_remotehost_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_remotehost_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_remoteport"></a>
<a id="Call_parameters_items_i1_remoteport"></a>
##### remoteport

- Schema name: `Remoteport`

Port number for SSH connection. Only applies when `mode` is SSH.
<a id="Call_parameters_items_i1_remoteport_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_remoteport_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_remoteport_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_remoteport_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_remoteport_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_remotemodule"></a>
<a id="Call_parameters_items_i1_remotemodule"></a>
##### remotemodule

- Schema name: `Remotemodule`

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
<a id="Call_parameters_items_i1_remotemodule_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_remotemodule_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_remotemodule_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_remotemodule_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_remotemodule_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_ssh_credentials"></a>
<a id="Call_parameters_items_i1_ssh_credentials"></a>
##### ssh_credentials

- Schema name: `Ssh Credentials`

Keychain credential ID for SSH authentication. `null` to use user's SSH keys.
<a id="Call_parameters_items_i1_ssh_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_ssh_credentials_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_ssh_credentials_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i1_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_remotepath"></a>
<a id="Call_parameters_items_i1_remotepath"></a>
##### remotepath

- Schema name: `Remotepath`
- Type: string

Path on the remote system to synchronize with.

<a id="headingCall_parameters_items_i1_direction"></a>
<a id="Call_parameters_items_i1_direction"></a>
##### direction

- Schema name: `Direction`
- Type: enum (of string)

Specify if data should be PULLED or PUSHED from the remote system.
###### Must be one of:

- "PULL"
- "PUSH"

<a id="headingCall_parameters_items_i1_desc"></a>
<a id="Call_parameters_items_i1_desc"></a>
##### desc

- Schema name: `Desc`
- Type: string

Description of the rsync task.

<a id="headingCall_parameters_items_i1_schedule"></a>
<a id="Call_parameters_items_i1_schedule"></a>
##### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
<a id="headingCall_parameters_items_i1_schedule_minute"></a>
<a id="Call_parameters_items_i1_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

<a id="headingCall_parameters_items_i1_schedule_hour"></a>
<a id="Call_parameters_items_i1_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCall_parameters_items_i1_schedule_dom"></a>
<a id="Call_parameters_items_i1_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCall_parameters_items_i1_schedule_month"></a>
<a id="Call_parameters_items_i1_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCall_parameters_items_i1_schedule_dow"></a>
<a id="Call_parameters_items_i1_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCall_parameters_items_i1_recursive"></a>
<a id="Call_parameters_items_i1_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean

Recursively transfer subdirectories.

<a id="headingCall_parameters_items_i1_times"></a>
<a id="Call_parameters_items_i1_times"></a>
##### times

- Schema name: `Times`
- Type: boolean

Preserve modification times of files.

<a id="headingCall_parameters_items_i1_compress"></a>
<a id="Call_parameters_items_i1_compress"></a>
##### compress

- Schema name: `Compress`
- Type: boolean

Reduce the size of the data to be transmitted.

<a id="headingCall_parameters_items_i1_archive"></a>
<a id="Call_parameters_items_i1_archive"></a>
##### archive

- Schema name: `Archive`
- Type: boolean

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

<a id="headingCall_parameters_items_i1_delete"></a>
<a id="Call_parameters_items_i1_delete"></a>
##### delete

- Schema name: `Delete`
- Type: boolean

Delete files in the destination directory that do not exist in the source directory.

<a id="headingCall_parameters_items_i1_quiet"></a>
<a id="Call_parameters_items_i1_quiet"></a>
##### quiet

- Schema name: `Quiet`
- Type: boolean

Suppress informational messages from rsync.

<a id="headingCall_parameters_items_i1_preserveperm"></a>
<a id="Call_parameters_items_i1_preserveperm"></a>
##### preserveperm

- Schema name: `Preserveperm`
- Type: boolean

Preserve original file permissions.

<a id="headingCall_parameters_items_i1_preserveattr"></a>
<a id="Call_parameters_items_i1_preserveattr"></a>
##### preserveattr

- Schema name: `Preserveattr`
- Type: boolean

Preserve extended attributes of files.

<a id="headingCall_parameters_items_i1_delayupdates"></a>
<a id="Call_parameters_items_i1_delayupdates"></a>
##### delayupdates

- Schema name: `Delayupdates`
- Type: boolean

Delay updating destination files until all transfers are complete.

<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_extra_items"></a>
- Type: string

<a id="headingCall_parameters_items_i1_enabled"></a>
<a id="Call_parameters_items_i1_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this rsync task is enabled.

<a id="headingCall_parameters_items_i1_validate_rpath"></a>
<a id="Call_parameters_items_i1_validate_rpath"></a>
##### validate_rpath

- Schema name: `Validate Rpath`
- Type: boolean

Validate the existence of the remote path.

<a id="headingCall_parameters_items_i1_ssh_keyscan"></a>
<a id="Call_parameters_items_i1_ssh_keyscan"></a>
##### ssh_keyscan

- Schema name: `Ssh Keyscan`
- Type: boolean

Automatically add remote host key to user's known_hosts file.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `RsyncTaskEntry`
- Type: object

The updated rsync task configuration.
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the rsync task.

<a id="headingReturn_value_path"></a>
<a id="Return_value_path"></a>
#### path (required)

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

<a id="headingReturn_value_dataset"></a>
<a id="Return_value_dataset"></a>
#### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the rsync task path (e.g., 'tank/data'). Returns `null` if the path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
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

The path of the rsync task relative to the dataset mountpoint (e.g., 'backups/daily'). An empty string indicates the task path is at the dataset root. Returns `null` if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="Return_value_relative_path_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_relative_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_user"></a>
<a id="Return_value_user"></a>
#### user (required)

- Schema name: `User`
- Type: string

Username to run the rsync task as.

<a id="headingReturn_value_mode"></a>
<a id="Return_value_mode"></a>
#### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "MODULE"

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.
##### Must be one of:

- "MODULE"
- "SSH"

<a id="headingReturn_value_remotehost"></a>
<a id="Return_value_remotehost"></a>
#### remotehost

- Schema name: `Remotehost`
- Default: null

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
<a id="Return_value_remotehost_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_remotehost_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_remotehost_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_remotehost_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remotehost_anyOf_i1)

- Type: null

<a id="headingReturn_value_remoteport"></a>
<a id="Return_value_remoteport"></a>
#### remoteport

- Schema name: `Remoteport`
- Default: null

Port number for SSH connection. Only applies when `mode` is SSH.
<a id="Return_value_remoteport_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_remoteport_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_remoteport_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_remoteport_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remoteport_anyOf_i1)

- Type: null

<a id="headingReturn_value_remotemodule"></a>
<a id="Return_value_remotemodule"></a>
#### remotemodule

- Schema name: `Remotemodule`
- Default: null

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
<a id="Return_value_remotemodule_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_remotemodule_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_remotemodule_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_remotemodule_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_remotemodule_anyOf_i1)

- Type: null

<a id="headingReturn_value_ssh_credentials"></a>
<a id="Return_value_ssh_credentials"></a>
#### ssh_credentials

- Default: null

In SSH mode, if `ssh_credentials` (a keychain credential of `SSH_CREDENTIALS` type) is specified then it is used to connect to the remote host. If it is not specified, then keys in `user`'s .ssh directory are used.
<a id="Return_value_ssh_credentials_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0"></a>
###### [KeychainCredentialEntry](#tab-pane_Return_value_ssh_credentials_anyOf_i0)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_ssh_credentials_anyOf_i0_id"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingReturn_value_ssh_credentials_anyOf_i0_name"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingReturn_value_ssh_credentials_anyOf_i0_type"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
###### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingReturn_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
<a id="Return_value_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="tab-pane_Return_value_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingReturn_value_remotepath"></a>
<a id="Return_value_remotepath"></a>
#### remotepath

- Schema name: `Remotepath`
- Type: string
- Default: ""

Path on the remote system to synchronize with.

<a id="headingReturn_value_direction"></a>
<a id="Return_value_direction"></a>
#### direction

- Schema name: `Direction`
- Type: enum (of string)
- Default: "PUSH"

Specify if data should be PULLED or PUSHED from the remote system.
##### Must be one of:

- "PULL"
- "PUSH"

<a id="headingReturn_value_desc"></a>
<a id="Return_value_desc"></a>
#### desc

- Schema name: `Desc`
- Type: string
- Default: ""

Description of the rsync task.

<a id="headingReturn_value_schedule"></a>
<a id="Return_value_schedule"></a>
#### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
<a id="headingReturn_value_schedule_minute"></a>
<a id="Return_value_schedule_minute"></a>
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

<a id="headingReturn_value_schedule_hour"></a>
<a id="Return_value_schedule_hour"></a>
##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingReturn_value_schedule_dom"></a>
<a id="Return_value_schedule_dom"></a>
##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingReturn_value_schedule_month"></a>
<a id="Return_value_schedule_month"></a>
##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingReturn_value_schedule_dow"></a>
<a id="Return_value_schedule_dow"></a>
##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingReturn_value_recursive"></a>
<a id="Return_value_recursive"></a>
#### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: true

Recursively transfer subdirectories.

<a id="headingReturn_value_times"></a>
<a id="Return_value_times"></a>
#### times

- Schema name: `Times`
- Type: boolean
- Default: true

Preserve modification times of files.

<a id="headingReturn_value_compress"></a>
<a id="Return_value_compress"></a>
#### compress

- Schema name: `Compress`
- Type: boolean
- Default: true

Reduce the size of the data to be transmitted.

<a id="headingReturn_value_archive"></a>
<a id="Return_value_archive"></a>
#### archive

- Schema name: `Archive`
- Type: boolean
- Default: false

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

<a id="headingReturn_value_delete"></a>
<a id="Return_value_delete"></a>
#### delete

- Schema name: `Delete`
- Type: boolean
- Default: false

Delete files in the destination directory that do not exist in the source directory.

<a id="headingReturn_value_quiet"></a>
<a id="Return_value_quiet"></a>
#### quiet

- Schema name: `Quiet`
- Type: boolean
- Default: false

Suppress informational messages from rsync.

<a id="headingReturn_value_preserveperm"></a>
<a id="Return_value_preserveperm"></a>
#### preserveperm

- Schema name: `Preserveperm`
- Type: boolean
- Default: false

Preserve original file permissions.

<a id="headingReturn_value_preserveattr"></a>
<a id="Return_value_preserveattr"></a>
#### preserveattr

- Schema name: `Preserveattr`
- Type: boolean
- Default: false

Preserve extended attributes of files.

<a id="headingReturn_value_delayupdates"></a>
<a id="Return_value_delayupdates"></a>
#### delayupdates

- Schema name: `Delayupdates`
- Type: boolean
- Default: true

Delay updating destination files until all transfers are complete.

<a id="headingReturn_value_extra"></a>
<a id="Return_value_extra"></a>
#### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_extra_items"></a>
- Type: string

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this rsync task is enabled.

<a id="headingReturn_value_locked"></a>
<a id="Return_value_locked"></a>
#### locked (required)

- Schema name: `Locked`
- Type: boolean

Whether this rsync task is currently locked (running).

<a id="headingReturn_value_job"></a>
<a id="Return_value_job"></a>
#### job (required)

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
<a id="Return_value_job_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_job_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_job_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_job_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
