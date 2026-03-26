---
title: replication.run_onetime
kind: method
source_rst: _sources/api_methods_replication.run_onetime.rst.txt
source_html: api_methods_replication.run_onetime.html
required_roles:
  - REPLICATION_TASK_WRITE
---

# replication.run_onetime

## Summary

Run replication task without creating it.

This method is a job.

## Required Roles

- `REPLICATION_TASK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: replication_run_onetime

#### replication_run_onetime

- Schema name: `replication_run_onetime`
- Type: object

ReplicationRunOnetimeArgs parameters.
- No Additional Properties
##### direction (required)

- Schema name: `Direction`
- Type: enum (of string)

Whether task will `PUSH` or `PULL` snapshots.

##### transport (required)

- Schema name: `Transport`
- Type: enum (of string)

Method of snapshots transfer. `SSH` transfers snapshots via SSH connection. This method is supported everywhere but does not achieve great performance. `SSH+NETCAT` uses unencrypted connection for data transfer. This can only be used in trusted networks and requires a port (specified by range from `netcat_active_side_port_min` to `netcat_active_side_port_max`) to be open on `netcat_active_side`. `LOCAL` replicates to or from localhost.

##### ssh_credentials

- Schema name: `Ssh Credentials`
- Default: null

Keychain Credential ID of type `SSH_CREDENTIALS`.
###### Any of

####### Option 1

- Type: integer

####### Option 2

- Type: null

##### netcat_active_side

- Schema name: `Netcat Active Side`
- Default: null

Which side actively establishes the netcat connection for `SSH+NETCAT` transport. `LOCAL`: Local system initiates the connection `REMOTE`: Remote system initiates the connection `null`: Not applicable for other transport types
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### netcat_active_side_listen_address

- Schema name: `Netcat Active Side Listen Address`
- Default: null

IP address for the active side to listen on for `SSH+NETCAT` transport. `null` if not applicable.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### netcat_active_side_port_min

- Schema name: `Netcat Active Side Port Min`
- Default: null

Minimum port number in the range for netcat connections. `null` if not applicable.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

####### Option 2

- Type: null

##### netcat_active_side_port_max

- Schema name: `Netcat Active Side Port Max`
- Default: null

Maximum port number in the range for netcat connections. `null` if not applicable.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

####### Option 2

- Type: null

##### netcat_passive_side_connect_address

- Schema name: `Netcat Passive Side Connect Address`
- Default: null

IP address for the passive side to connect to for `SSH+NETCAT` transport. `null` if not applicable.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### sudo

- Schema name: `Sudo`
- Type: boolean
- Default: false

`SSH` and `SSH+NETCAT` transports should use sudo (which is expected to be passwordless) to run `zfs` command on the remote machine.

##### source_datasets (required)

- Schema name: `Source Datasets`
- Type: array of string

List of datasets to replicate snapshots from.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

- Type: string

##### target_dataset (required)

- Schema name: `Target Dataset`
- Type: string

Dataset to put snapshots into.

##### recursive (required)

- Schema name: `Recursive`
- Type: boolean

Whether to recursively replicate child datasets.

##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from replication.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### properties

- Schema name: `Properties`
- Type: boolean
- Default: true

Send dataset properties along with snapshots.

##### properties_exclude

- Schema name: `Properties Exclude`
- Type: array of string
- Default: []

Array of dataset property names to exclude from replication.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### properties_override

- Schema name: `Properties Override`
- Type: object
- Default: {}

Object mapping dataset property names to override values during replication.
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

##### replicate

- Schema name: `Replicate`
- Type: boolean
- Default: false

Whether to use full ZFS replication.

##### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether to enable encryption for the replicated datasets.

##### encryption_inherit

- Schema name: `Encryption Inherit`
- Default: null

Whether replicated datasets should inherit encryption from parent. `null` if encryption is disabled.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### encryption_key

- Schema name: `Encryption Key`
- Default: null

Encryption key for replicated datasets. `null` if not specified.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### encryption_key_format

- Schema name: `Encryption Key Format`
- Default: null

Format of the encryption key. `HEX`: Hexadecimal-encoded key `PASSPHRASE`: Text passphrase `null`: Not applicable when encryption is disabled
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### encryption_key_location

- Schema name: `Encryption Key Location`
- Default: null

Filesystem path where encryption key is stored. `null` if not using key file.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### periodic_snapshot_tasks

- Schema name: `Periodic Snapshot Tasks`
- Type: array of integer
- Default: []

List of periodic snapshot task IDs that are sources of snapshots for this replication task. Only push replication tasks can be bound to periodic snapshot tasks.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

- Type: integer

##### naming_schema

- Schema name: `Naming Schema`
- Type: array of string
- Default: []

List of naming schemas for pull replication.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### also_include_naming_schema

- Schema name: `Also Include Naming Schema`
- Type: array of string
- Default: []

List of naming schemas for push replication.
- No Additional Items

###### Each item of this array must be:

- Type: string

##### name_regex

- Schema name: `Name Regex`
- Default: null

Replicate all snapshots which names match specified regular expression.
###### Any of

####### Option 1

- Type: string
- Must be at least `1` characters long

####### Option 2

- Type: null

##### restrict_schedule

- Default: null

Restricts when replication task with bound periodic snapshot tasks runs. For example, you can have periodic snapshot tasks that run every 15 minutes, but only run replication task every hour.
###### Any of

####### ReplicationTimeCronModel

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
######## minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

######## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

######## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

######## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

######## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

######## begin

- Schema name: `Begin`
- Type: string
- Default: "00:00"

Start time for the time window in HH:MM format.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

######## end

- Schema name: `End`
- Type: string
- Default: "23:59"

End time for the time window in HH:MM format.
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

####### Option 2

- Type: null

##### allow_from_scratch

- Schema name: `Allow From Scratch`
- Type: boolean
- Default: false

Will destroy all snapshots on target side and replicate everything from scratch if none of the snapshots on target side matches source snapshots.

##### readonly

- Schema name: `Readonly`
- Type: enum (of string)
- Default: "SET"

Controls destination datasets readonly property. `SET`: Set all destination datasets to readonly=on after finishing the replication. `REQUIRE`: Require all existing destination datasets to have readonly=on property. `IGNORE`: Avoid this kind of behavior.

##### hold_pending_snapshots

- Schema name: `Hold Pending Snapshots`
- Type: boolean
- Default: false

Prevent source snapshots from being deleted by retention of replication fails for some reason.

##### retention_policy (required)

- Schema name: `Retention Policy`
- Type: enum (of string)

How to delete old snapshots on target side: `SOURCE`: Delete snapshots that are absent on source side. `CUSTOM`: Delete snapshots that are older than `lifetime_value` and `lifetime_unit`. `NONE`: Do not delete any snapshots.

##### lifetime_value

- Schema name: `Lifetime Value`
- Default: null

Number of time units to retain snapshots for custom retention policy. Only applies when `retention_policy` is CUSTOM.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1`

####### Option 2

- Type: null

##### lifetime_unit

- Schema name: `Lifetime Unit`
- Default: null

Time unit for snapshot retention for custom retention policy. Only applies when `retention_policy` is CUSTOM.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### lifetimes

- Schema name: `Lifetimes`
- Type: array of object
- Default: []

Array of different retention schedules with their own cron schedules and lifetime settings.
- No Additional Items

###### Each item of this array must be:

###### ReplicationLifetimeModel

- Schema name: `ReplicationLifetimeModel`
- Type: object
- No Additional Properties
####### schedule (required)

- Schema name: `CronModel`
- Type: object

Cron schedule for when snapshot retention policies are applied.
- No Additional Properties
######## minute

- Schema name: `Minute`
- Type: string
- Default: "*"

"00" - "59"

######## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

######## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

######## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

######## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

####### lifetime_value (required)

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots.
- Value must be greater or equal to `1`

####### lifetime_unit (required)

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Time unit for snapshot retention.

##### compression

- Schema name: `Compression`
- Default: null

Compresses SSH stream. Available only for SSH transport.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### speed_limit

- Schema name: `Speed Limit`
- Default: null

Limits speed of SSH stream. Available only for SSH transport.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `1`

####### Option 2

- Type: null

##### large_block

- Schema name: `Large Block`
- Type: boolean
- Default: true

Enable large block support for ZFS send streams.

##### embed

- Schema name: `Embed`
- Type: boolean
- Default: false

Enable embedded block support for ZFS send streams.

##### compressed

- Schema name: `Compressed`
- Type: boolean
- Default: true

Enable compressed ZFS send streams.

##### retries

- Schema name: `Retries`
- Type: integer
- Default: 5

Number of retries before considering replication failed.
- Value must be greater or equal to `1`

##### logging_level

- Schema name: `Logging Level`
- Default: null

Log level for replication task execution. Controls verbosity of replication logs.
###### Any of

####### Option 1

- Type: enum (of string)

####### Option 2

- Type: null

##### exclude_mountpoint_property

- Schema name: `Exclude Mountpoint Property`
- Type: boolean
- Default: true

Whether to exclude the mountpoint property from replication.

##### only_from_scratch

- Schema name: `Only From Scratch`
- Type: boolean
- Default: false

If `true` then replication will fail if target dataset already exists.

##### mount

- Schema name: `Mount`
- Type: boolean
- Default: true

Mount destination file system.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` on successful one-time replication execution.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
