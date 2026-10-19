---
title: rsynctask.query
kind: event
source_rst: _sources/api_events_rsynctask.query.rst.txt
source_html: api_events_rsynctask.query.html
required_roles:
  - SNAPSHOT_TASK_READ
---

# rsynctask.query

## Summary

Sent on rsynctask changes.

## Required Roles

- `SNAPSHOT_TASK_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `RsyncTaskAddedEvent`
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

- Schema name: `RsyncTaskEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the rsync task.

<a id="headingADDED_fields_path"></a>
<a id="ADDED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

<a id="headingADDED_fields_dataset"></a>
<a id="ADDED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the rsync task path (e.g., 'tank/data'). Returns `null` if the path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
<a id="ADDED_fields_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_dataset_anyOf_i1)

- Type: null

<a id="headingADDED_fields_relative_path"></a>
<a id="ADDED_fields_relative_path"></a>
##### relative_path (required)

- Schema name: `Relative Path`

The path of the rsync task relative to the dataset mountpoint (e.g., 'backups/daily'). An empty string indicates the task path is at the dataset root. Returns `null` if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="ADDED_fields_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_relative_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_user"></a>
<a id="ADDED_fields_user"></a>
##### user (required)

- Schema name: `User`
- Type: string

Username to run the rsync task as.

<a id="headingADDED_fields_mode"></a>
<a id="ADDED_fields_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "MODULE"

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.
###### Must be one of:

- "MODULE"
- "SSH"

<a id="headingADDED_fields_remotehost"></a>
<a id="ADDED_fields_remotehost"></a>
##### remotehost

- Schema name: `Remotehost`
- Default: null

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
<a id="ADDED_fields_remotehost_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_remotehost_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_remotehost_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_remotehost_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_remotehost_anyOf_i1)

- Type: null

<a id="headingADDED_fields_remoteport"></a>
<a id="ADDED_fields_remoteport"></a>
##### remoteport

- Schema name: `Remoteport`
- Default: null

Port number for SSH connection. Only applies when `mode` is SSH.
<a id="ADDED_fields_remoteport_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_remoteport_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_remoteport_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_remoteport_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_remoteport_anyOf_i1)

- Type: null

<a id="headingADDED_fields_remotemodule"></a>
<a id="ADDED_fields_remotemodule"></a>
##### remotemodule

- Schema name: `Remotemodule`
- Default: null

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
<a id="ADDED_fields_remotemodule_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_remotemodule_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_remotemodule_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_remotemodule_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_remotemodule_anyOf_i1)

- Type: null

<a id="headingADDED_fields_ssh_credentials"></a>
<a id="ADDED_fields_ssh_credentials"></a>
##### ssh_credentials

- Default: null

In SSH mode, if `ssh_credentials` (a keychain credential of `SSH_CREDENTIALS` type) is specified then it is used to connect to the remote host. If it is not specified, then keys in `user`'s .ssh directory are used.
<a id="ADDED_fields_ssh_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0"></a>
###### [KeychainCredentialEntry](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_ssh_credentials_anyOf_i0_id"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_name"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_type"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
###### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
<a id="ADDED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="tab-pane_ADDED_fields_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingADDED_fields_remotepath"></a>
<a id="ADDED_fields_remotepath"></a>
##### remotepath

- Schema name: `Remotepath`
- Type: string
- Default: ""

Path on the remote system to synchronize with.

<a id="headingADDED_fields_direction"></a>
<a id="ADDED_fields_direction"></a>
##### direction

- Schema name: `Direction`
- Type: enum (of string)
- Default: "PUSH"

Specify if data should be PULLED or PUSHED from the remote system.
###### Must be one of:

- "PULL"
- "PUSH"

<a id="headingADDED_fields_desc"></a>
<a id="ADDED_fields_desc"></a>
##### desc

- Schema name: `Desc`
- Type: string
- Default: ""

Description of the rsync task.

<a id="headingADDED_fields_schedule"></a>
<a id="ADDED_fields_schedule"></a>
##### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
<a id="headingADDED_fields_schedule_minute"></a>
<a id="ADDED_fields_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

<a id="headingADDED_fields_schedule_hour"></a>
<a id="ADDED_fields_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_schedule_dom"></a>
<a id="ADDED_fields_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_schedule_month"></a>
<a id="ADDED_fields_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_schedule_dow"></a>
<a id="ADDED_fields_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_recursive"></a>
<a id="ADDED_fields_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: true

Recursively transfer subdirectories.

<a id="headingADDED_fields_times"></a>
<a id="ADDED_fields_times"></a>
##### times

- Schema name: `Times`
- Type: boolean
- Default: true

Preserve modification times of files.

<a id="headingADDED_fields_compress"></a>
<a id="ADDED_fields_compress"></a>
##### compress

- Schema name: `Compress`
- Type: boolean
- Default: true

Reduce the size of the data to be transmitted.

<a id="headingADDED_fields_archive"></a>
<a id="ADDED_fields_archive"></a>
##### archive

- Schema name: `Archive`
- Type: boolean
- Default: false

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

<a id="headingADDED_fields_delete"></a>
<a id="ADDED_fields_delete"></a>
##### delete

- Schema name: `Delete`
- Type: boolean
- Default: false

Delete files in the destination directory that do not exist in the source directory.

<a id="headingADDED_fields_quiet"></a>
<a id="ADDED_fields_quiet"></a>
##### quiet

- Schema name: `Quiet`
- Type: boolean
- Default: false

Suppress informational messages from rsync.

<a id="headingADDED_fields_preserveperm"></a>
<a id="ADDED_fields_preserveperm"></a>
##### preserveperm

- Schema name: `Preserveperm`
- Type: boolean
- Default: false

Preserve original file permissions.

<a id="headingADDED_fields_preserveattr"></a>
<a id="ADDED_fields_preserveattr"></a>
##### preserveattr

- Schema name: `Preserveattr`
- Type: boolean
- Default: false

Preserve extended attributes of files.

<a id="headingADDED_fields_delayupdates"></a>
<a id="ADDED_fields_delayupdates"></a>
##### delayupdates

- Schema name: `Delayupdates`
- Type: boolean
- Default: true

Delay updating destination files until all transfers are complete.

<a id="headingADDED_fields_extra"></a>
<a id="ADDED_fields_extra"></a>
##### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_extra_items"></a>
- Type: string

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this rsync task is enabled.

<a id="headingADDED_fields_locked"></a>
<a id="ADDED_fields_locked"></a>
##### locked (required)

- Schema name: `Locked`
- Type: boolean

Whether this rsync task is currently locked (running).

<a id="headingADDED_fields_job"></a>
<a id="ADDED_fields_job"></a>
##### job (required)

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
<a id="ADDED_fields_job_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_job_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_job_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_job_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `RsyncTaskChangedEvent`
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

- Schema name: `RsyncTaskEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the rsync task.

<a id="headingCHANGED_fields_path"></a>
<a id="CHANGED_fields_path"></a>
##### path (required)

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

<a id="headingCHANGED_fields_dataset"></a>
<a id="CHANGED_fields_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`

The ZFS dataset containing the rsync task path (e.g., 'tank/data'). Returns `null` if the path cannot be resolved yet (encrypted dataset not unlocked, etc.). This is a read-only field automatically populated from "path".
<a id="CHANGED_fields_dataset_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_dataset_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_dataset_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_dataset_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_dataset_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_relative_path"></a>
<a id="CHANGED_fields_relative_path"></a>
##### relative_path (required)

- Schema name: `Relative Path`

The path of the rsync task relative to the dataset mountpoint (e.g., 'backups/daily'). An empty string indicates the task path is at the dataset root. Returns `null` if the path cannot be resolved yet. This is a read-only field automatically populated from "path".
<a id="CHANGED_fields_relative_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_relative_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_relative_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_relative_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_relative_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_user"></a>
<a id="CHANGED_fields_user"></a>
##### user (required)

- Schema name: `User`
- Type: string

Username to run the rsync task as.

<a id="headingCHANGED_fields_mode"></a>
<a id="CHANGED_fields_mode"></a>
##### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "MODULE"

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.
###### Must be one of:

- "MODULE"
- "SSH"

<a id="headingCHANGED_fields_remotehost"></a>
<a id="CHANGED_fields_remotehost"></a>
##### remotehost

- Schema name: `Remotehost`
- Default: null

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
<a id="CHANGED_fields_remotehost_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_remotehost_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_remotehost_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_remotehost_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_remotehost_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_remoteport"></a>
<a id="CHANGED_fields_remoteport"></a>
##### remoteport

- Schema name: `Remoteport`
- Default: null

Port number for SSH connection. Only applies when `mode` is SSH.
<a id="CHANGED_fields_remoteport_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_remoteport_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_remoteport_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_remoteport_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_remoteport_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_remotemodule"></a>
<a id="CHANGED_fields_remotemodule"></a>
##### remotemodule

- Schema name: `Remotemodule`
- Default: null

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
<a id="CHANGED_fields_remotemodule_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_remotemodule_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_remotemodule_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_remotemodule_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_remotemodule_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_ssh_credentials"></a>
<a id="CHANGED_fields_ssh_credentials"></a>
##### ssh_credentials

- Default: null

In SSH mode, if `ssh_credentials` (a keychain credential of `SSH_CREDENTIALS` type) is specified then it is used to connect to the remote host. If it is not specified, then keys in `user`'s .ssh directory are used.
<a id="CHANGED_fields_ssh_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0"></a>
###### [KeychainCredentialEntry](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0)

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_id"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_name"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_type"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication
###### Must be one of:

- "SSH_KEY_PAIR"
- "SSH_CREDENTIALS"

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes"></a>
###### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0"></a>
###### [SSHKeyPair](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0)

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key"></a>
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_private_key_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key"></a>
###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i0_public_key_anyOf_i1)

- Type: null

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1"></a>
###### [SSHCredentials](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1)

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_port"></a>
###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_private_key"></a>
###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_remote_host_key"></a>
###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

<a id="headingCHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
<a id="CHANGED_fields_ssh_credentials_anyOf_i0_attributes_anyOf_i1_connect_timeout"></a>
###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

<a id="tab-pane_CHANGED_fields_ssh_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_ssh_credentials_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_remotepath"></a>
<a id="CHANGED_fields_remotepath"></a>
##### remotepath

- Schema name: `Remotepath`
- Type: string
- Default: ""

Path on the remote system to synchronize with.

<a id="headingCHANGED_fields_direction"></a>
<a id="CHANGED_fields_direction"></a>
##### direction

- Schema name: `Direction`
- Type: enum (of string)
- Default: "PUSH"

Specify if data should be PULLED or PUSHED from the remote system.
###### Must be one of:

- "PULL"
- "PUSH"

<a id="headingCHANGED_fields_desc"></a>
<a id="CHANGED_fields_desc"></a>
##### desc

- Schema name: `Desc`
- Type: string
- Default: ""

Description of the rsync task.

<a id="headingCHANGED_fields_schedule"></a>
<a id="CHANGED_fields_schedule"></a>
##### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
<a id="headingCHANGED_fields_schedule_minute"></a>
<a id="CHANGED_fields_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

<a id="headingCHANGED_fields_schedule_hour"></a>
<a id="CHANGED_fields_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_schedule_dom"></a>
<a id="CHANGED_fields_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_schedule_month"></a>
<a id="CHANGED_fields_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_schedule_dow"></a>
<a id="CHANGED_fields_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_recursive"></a>
<a id="CHANGED_fields_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: true

Recursively transfer subdirectories.

<a id="headingCHANGED_fields_times"></a>
<a id="CHANGED_fields_times"></a>
##### times

- Schema name: `Times`
- Type: boolean
- Default: true

Preserve modification times of files.

<a id="headingCHANGED_fields_compress"></a>
<a id="CHANGED_fields_compress"></a>
##### compress

- Schema name: `Compress`
- Type: boolean
- Default: true

Reduce the size of the data to be transmitted.

<a id="headingCHANGED_fields_archive"></a>
<a id="CHANGED_fields_archive"></a>
##### archive

- Schema name: `Archive`
- Type: boolean
- Default: false

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

<a id="headingCHANGED_fields_delete"></a>
<a id="CHANGED_fields_delete"></a>
##### delete

- Schema name: `Delete`
- Type: boolean
- Default: false

Delete files in the destination directory that do not exist in the source directory.

<a id="headingCHANGED_fields_quiet"></a>
<a id="CHANGED_fields_quiet"></a>
##### quiet

- Schema name: `Quiet`
- Type: boolean
- Default: false

Suppress informational messages from rsync.

<a id="headingCHANGED_fields_preserveperm"></a>
<a id="CHANGED_fields_preserveperm"></a>
##### preserveperm

- Schema name: `Preserveperm`
- Type: boolean
- Default: false

Preserve original file permissions.

<a id="headingCHANGED_fields_preserveattr"></a>
<a id="CHANGED_fields_preserveattr"></a>
##### preserveattr

- Schema name: `Preserveattr`
- Type: boolean
- Default: false

Preserve extended attributes of files.

<a id="headingCHANGED_fields_delayupdates"></a>
<a id="CHANGED_fields_delayupdates"></a>
##### delayupdates

- Schema name: `Delayupdates`
- Type: boolean
- Default: true

Delay updating destination files until all transfers are complete.

<a id="headingCHANGED_fields_extra"></a>
<a id="CHANGED_fields_extra"></a>
##### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_extra_items"></a>
- Type: string

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this rsync task is enabled.

<a id="headingCHANGED_fields_locked"></a>
<a id="CHANGED_fields_locked"></a>
##### locked (required)

- Schema name: `Locked`
- Type: boolean

Whether this rsync task is currently locked (running).

<a id="headingCHANGED_fields_job"></a>
<a id="CHANGED_fields_job"></a>
##### job (required)

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
<a id="CHANGED_fields_job_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_job_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_job_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_job_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `RsyncTaskRemovedEvent`
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
