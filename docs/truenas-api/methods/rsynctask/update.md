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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the rsync task to update.

#### Parameter 2: rsync_task_update

#### rsync_task_update

- Schema name: `rsync_task_update`
- Type: object

Updated configuration for the rsync task.
- No Additional Properties
##### path

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

##### user

- Schema name: `User`
- Type: string

Username to run the rsync task as.

##### mode

- Schema name: `Mode`
- Type: enum (of string)

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.

##### remotehost

- Schema name: `Remotehost`

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### remoteport

- Schema name: `Remoteport`

Port number for SSH connection. Only applies when `mode` is SSH.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### remotemodule

- Schema name: `Remotemodule`

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### ssh_credentials

- Schema name: `Ssh Credentials`

Keychain credential ID for SSH authentication. `null` to use user's SSH keys.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### remotepath

- Schema name: `Remotepath`
- Type: string

Path on the remote system to synchronize with.

##### direction

- Schema name: `Direction`
- Type: enum (of string)

Specify if data should be PULLED or PUSHED from the remote system.

##### desc

- Schema name: `Desc`
- Type: string

Description of the rsync task.

##### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

##### recursive

- Schema name: `Recursive`
- Type: boolean

Recursively transfer subdirectories.

##### times

- Schema name: `Times`
- Type: boolean

Preserve modification times of files.

##### compress

- Schema name: `Compress`
- Type: boolean

Reduce the size of the data to be transmitted.

##### archive

- Schema name: `Archive`
- Type: boolean

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

##### delete

- Schema name: `Delete`
- Type: boolean

Delete files in the destination directory that do not exist in the source directory.

##### quiet

- Schema name: `Quiet`
- Type: boolean

Suppress informational messages from rsync.

##### preserveperm

- Schema name: `Preserveperm`
- Type: boolean

Preserve original file permissions.

##### preserveattr

- Schema name: `Preserveattr`
- Type: boolean

Preserve extended attributes of files.

##### delayupdates

- Schema name: `Delayupdates`
- Type: boolean

Delay updating destination files until all transfers are complete.

##### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this rsync task is enabled.

##### validate_rpath

- Schema name: `Validate Rpath`
- Type: boolean

Validate the existence of the remote path.

##### ssh_keyscan

- Schema name: `Ssh Keyscan`
- Type: boolean

Automatically add remote host key to user's known_hosts file.

### Return value

- Schema name: `RsyncTaskEntry`
- Type: object

The updated rsync task configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the rsync task.

#### path (required)

- Schema name: `Path`
- Type: string

Local filesystem path to synchronize.
- Must be at most `1023` characters long

#### user (required)

- Schema name: `User`
- Type: string

Username to run the rsync task as.

#### mode

- Schema name: `Mode`
- Type: enum (of string)
- Default: "MODULE"

Operating mechanism for Rsync, i.e. Rsync Module mode or Rsync SSH mode.

#### remotehost

- Schema name: `Remotehost`
- Default: null

IP address or hostname of the remote system. If username differs on the remote host, "username@remote_host" format should be used.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### remoteport

- Schema name: `Remoteport`
- Default: null

Port number for SSH connection. Only applies when `mode` is SSH.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### remotemodule

- Schema name: `Remotemodule`
- Default: null

Name of remote module, this attribute should be specified when `mode` is set to MODULE.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### ssh_credentials

- Default: null

In SSH mode, if `ssh_credentials` (a keychain credential of `SSH_CREDENTIALS` type) is specified then it is used to connect to the remote host. If it is not specified, then keys in `user`'s .ssh directory are used.
##### Any of

###### KeychainCredentialEntry

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

####### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

####### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication

####### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
######## Any of

######### SSHKeyPair

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
########## private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

########## public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

######### SSHCredentials

- Type: string

######### Option 1

- Type: null

######### Option 2

- Type: string

######### Option 1

- Type: null

######### Option 2

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
########## host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

########## port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

########## username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

########## private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

########## remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

########## connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

###### Option 2

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
####### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

###### SSHKeyPair

- Type: string

###### SSHCredentials

- Type: null

###### Option 1

- Type: string

###### Option 2

- Type: null

###### Option 1

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
####### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

####### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

####### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

####### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

####### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

####### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

###### Option 2

- Type: null

#### remotepath

- Schema name: `Remotepath`
- Type: string
- Default: ""

Path on the remote system to synchronize with.

#### direction

- Schema name: `Direction`
- Type: enum (of string)
- Default: "PUSH"

Specify if data should be PULLED or PUSHED from the remote system.

#### desc

- Schema name: `Desc`
- Type: string
- Default: ""

Description of the rsync task.

#### schedule

- Schema name: `RsyncTaskSchedule`
- Type: object

Cron schedule for when the rsync task should run.
- No Additional Properties
##### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when the rsync task should run (cron format).

##### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

##### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

##### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

##### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

#### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: true

Recursively transfer subdirectories.

#### times

- Schema name: `Times`
- Type: boolean
- Default: true

Preserve modification times of files.

#### compress

- Schema name: `Compress`
- Type: boolean
- Default: true

Reduce the size of the data to be transmitted.

#### archive

- Schema name: `Archive`
- Type: boolean
- Default: false

Make rsync run recursively, preserving symlinks, permissions, modification times, group, and special files.

#### delete

- Schema name: `Delete`
- Type: boolean
- Default: false

Delete files in the destination directory that do not exist in the source directory.

#### quiet

- Schema name: `Quiet`
- Type: boolean
- Default: false

Suppress informational messages from rsync.

#### preserveperm

- Schema name: `Preserveperm`
- Type: boolean
- Default: false

Preserve original file permissions.

#### preserveattr

- Schema name: `Preserveattr`
- Type: boolean
- Default: false

Preserve extended attributes of files.

#### delayupdates

- Schema name: `Delayupdates`
- Type: boolean
- Default: true

Delay updating destination files until all transfers are complete.

#### extra

- Schema name: `Extra`
- Type: array of string

Array of additional rsync command-line options.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this rsync task is enabled.

#### locked (required)

- Schema name: `Locked`
- Type: boolean

Whether this rsync task is currently locked (running).

#### job (required)

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
##### Any of

###### Option 1

- Type: object

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
