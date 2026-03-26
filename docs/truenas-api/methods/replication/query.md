---
title: replication.query
kind: method
source_rst: _sources/api_methods_replication.query.rst.txt
source_html: api_methods_replication.query.html
required_roles:
  - REPLICATION_TASK_READ
---

# replication.query

## Required Roles

- `REPLICATION_TASK_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

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
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

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

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### ReplicationQueryResultItem

- Schema name: `ReplicationQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for this replication task.

####### name

- Schema name: `Name`
- Type: string

Name for replication task.
- Must be at least `1` characters long

####### direction

- Schema name: `Direction`
- Type: enum (of string)

Whether task will `PUSH` or `PULL` snapshots.

####### transport

- Schema name: `Transport`
- Type: enum (of string)

Method of snapshots transfer. `SSH` transfers snapshots via SSH connection. This method is supported everywhere but does not achieve great performance. `SSH+NETCAT` uses unencrypted connection for data transfer. This can only be used in trusted networks and requires a port (specified by range from `netcat_active_side_port_min` to `netcat_active_side_port_max`) to be open on `netcat_active_side`. `LOCAL` replicates to or from localhost.

####### ssh_credentials

Keychain Credential of type `SSH_CREDENTIALS`.
######## Any of

######### KeychainCredentialEntry

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
########## id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

########## name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

########## type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication

########## attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
########### Any of

############ SSHKeyPair

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
############# private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
############## Any of

############### Option 1

- Type: string

############### Option 2

- Type: null

############# public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
############## Any of

############### Option 1

- Type: string

############### Option 2

- Type: null

############ SSHCredentials

- Type: string

############ Option 1

- Type: null

############ Option 2

- Type: string

############ Option 1

- Type: null

############ Option 2

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
############# host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

############# port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

############# username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

############# private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

############# remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

############# connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

######### Option 2

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

######### SSHKeyPair

- Type: string

######### SSHCredentials

- Type: null

######### Option 1

- Type: string

######### Option 2

- Type: null

######### Option 1

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

######### Option 2

- Type: null

####### netcat_active_side

- Schema name: `Netcat Active Side`

Which side actively establishes the netcat connection for `SSH+NETCAT` transport. `LOCAL`: Local system initiates the connection `REMOTE`: Remote system initiates the connection `null`: Not applicable for other transport types
######## Any of

######### Option 1

- Type: enum (of string)

######### Option 2

- Type: null

####### netcat_active_side_listen_address

- Schema name: `Netcat Active Side Listen Address`

IP address for the active side to listen on for `SSH+NETCAT` transport. `null` if not applicable.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### netcat_active_side_port_min

- Schema name: `Netcat Active Side Port Min`

Minimum port number in the range for netcat connections. `null` if not applicable.
######## Any of

######### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

######### Option 2

- Type: null

####### netcat_active_side_port_max

- Schema name: `Netcat Active Side Port Max`

Maximum port number in the range for netcat connections. `null` if not applicable.
######## Any of

######### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

######### Option 2

- Type: null

####### netcat_passive_side_connect_address

- Schema name: `Netcat Passive Side Connect Address`

IP address for the passive side to connect to for `SSH+NETCAT` transport. `null` if not applicable.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### sudo

- Schema name: `Sudo`
- Type: boolean

`SSH` and `SSH+NETCAT` transports should use sudo (which is expected to be passwordless) to run `zfs` command on the remote machine.

####### source_datasets

- Schema name: `Source Datasets`
- Type: array of string

List of datasets to replicate snapshots from.
- Must contain a minimum of `1` items
- No Additional Items

######## Each item of this array must be:

- Type: string

####### target_dataset

- Schema name: `Target Dataset`
- Type: string

Dataset to put snapshots into.

####### recursive

- Schema name: `Recursive`
- Type: boolean

Whether to recursively replicate child datasets.

####### exclude

- Schema name: `Exclude`
- Type: array of string

Array of dataset patterns to exclude from replication.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### properties

- Schema name: `Properties`
- Type: boolean

Send dataset properties along with snapshots.

####### properties_exclude

- Schema name: `Properties Exclude`
- Type: array of string

Array of dataset property names to exclude from replication.
- No Additional Items

######## Each item of this array must be:

- Type: string
- Must be at least `1` characters long

####### properties_override

- Schema name: `Properties Override`
- Type: object

Object mapping dataset property names to override values during replication.
######## Additional Properties

Each additional property must conform to the following schema
- Type: string

####### replicate

- Schema name: `Replicate`
- Type: boolean

Whether to use full ZFS replication.

####### encryption

- Schema name: `Encryption`
- Type: boolean

Whether to enable encryption for the replicated datasets.

####### encryption_inherit

- Schema name: `Encryption Inherit`

Whether replicated datasets should inherit encryption from parent. `null` if encryption is disabled.
######## Any of

######### Option 1

- Type: boolean

######### Option 2

- Type: null

####### encryption_key

- Schema name: `Encryption Key`

Encryption key for replicated datasets. `null` if not specified.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### encryption_key_format

- Schema name: `Encryption Key Format`

Format of the encryption key. `HEX`: Hexadecimal-encoded key `PASSPHRASE`: Text passphrase `null`: Not applicable when encryption is disabled
######## Any of

######### Option 1

- Type: enum (of string)

######### Option 2

- Type: null

####### encryption_key_location

- Schema name: `Encryption Key Location`

Filesystem path where encryption key is stored. `null` if not using key file.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### periodic_snapshot_tasks

- Schema name: `Periodic Snapshot Tasks`
- Type: array of object

List of periodic snapshot tasks that are sources of snapshots for this replication task. Only push replication tasks can be bound to periodic snapshot tasks.
- No Additional Items

######## Each item of this array must be:

######## PoolSnapshotTaskDBEntry

- Schema name: `PoolSnapshotTaskDBEntry`
- Type: object
- No Additional Properties
######### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

######### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

######### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.

######### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.

######### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

######### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

########## Each item of this array must be:

- Type: string

######### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

######### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

######### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
########## minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

########## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

########## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

########## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

########## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

########## begin

- Schema name: `Begin`
- Type: string
- Default: "00:00"

Start time of the window when snapshots can be taken.
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

########## end

- Schema name: `End`
- Type: string
- Default: "23:59"

End time of the window when snapshots can be taken.
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

######### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

######### state (required)

- Schema name: `State`
- Type: string

Current state of the task.

####### naming_schema

- Schema name: `Naming Schema`
- Type: array of string

List of naming schemas for pull replication.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### also_include_naming_schema

- Schema name: `Also Include Naming Schema`
- Type: array of string

List of naming schemas for push replication.
- No Additional Items

######## Each item of this array must be:

- Type: string

####### name_regex

- Schema name: `Name Regex`

Replicate all snapshots which names match specified regular expression.
######## Any of

######### Option 1

- Type: string
- Must be at least `1` characters long

######### Option 2

- Type: null

####### auto

- Schema name: `Auto`
- Type: boolean

Allow replication to run automatically on schedule or after bound periodic snapshot task.

####### schedule

Schedule to run replication task. Only `auto` replication tasks without bound periodic snapshot tasks can have a schedule.
######## Any of

######### ReplicationTimeCronModel

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
########## minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

########## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

########## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

########## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

########## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

########## begin

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

########## end

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

######### Option 2

- Type: null

####### restrict_schedule

Restricts when replication task with bound periodic snapshot tasks runs. For example, you can have periodic snapshot tasks that run every 15 minutes, but only run replication task every hour.
######## Any of

######### ReplicationTimeCronModel

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
########## minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

########## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

########## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

########## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

########## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

########## begin

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

########## end

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

######### Option 2

- Type: null

####### only_matching_schedule

- Schema name: `Only Matching Schedule`
- Type: boolean

Will only replicate snapshots that match `schedule` or `restrict_schedule`.

####### allow_from_scratch

- Schema name: `Allow From Scratch`
- Type: boolean

Will destroy all snapshots on target side and replicate everything from scratch if none of the snapshots on target side matches source snapshots.

####### readonly

- Schema name: `Readonly`
- Type: enum (of string)

Controls destination datasets readonly property. `SET`: Set all destination datasets to readonly=on after finishing the replication. `REQUIRE`: Require all existing destination datasets to have readonly=on property. `IGNORE`: Avoid this kind of behavior.

####### hold_pending_snapshots

- Schema name: `Hold Pending Snapshots`
- Type: boolean

Prevent source snapshots from being deleted by retention of replication fails for some reason.

####### retention_policy

- Schema name: `Retention Policy`
- Type: enum (of string)

How to delete old snapshots on target side: `SOURCE`: Delete snapshots that are absent on source side. `CUSTOM`: Delete snapshots that are older than `lifetime_value` and `lifetime_unit`. `NONE`: Do not delete any snapshots.

####### lifetime_value

- Schema name: `Lifetime Value`

Number of time units to retain snapshots for custom retention policy. Only applies when `retention_policy` is CUSTOM.
######## Any of

######### Option 1

- Type: integer
- Value must be greater or equal to `1`

######### Option 2

- Type: null

####### lifetime_unit

- Schema name: `Lifetime Unit`

Time unit for snapshot retention for custom retention policy. Only applies when `retention_policy` is CUSTOM.
######## Any of

######### Option 1

- Type: enum (of string)

######### Option 2

- Type: null

####### lifetimes

- Schema name: `Lifetimes`
- Type: array of object

Array of different retention schedules with their own cron schedules and lifetime settings.
- No Additional Items

######## Each item of this array must be:

######## ReplicationLifetimeModel

- Schema name: `ReplicationLifetimeModel`
- Type: object
- No Additional Properties
######### schedule (required)

- Schema name: `CronModel`
- Type: object

Cron schedule for when snapshot retention policies are applied.
- No Additional Properties
########## minute

- Schema name: `Minute`
- Type: string
- Default: "*"

"00" - "59"

########## hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23"

########## dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31"

########## month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December)

########## dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday)

######### lifetime_value (required)

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots.
- Value must be greater or equal to `1`

######### lifetime_unit (required)

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Time unit for snapshot retention.

####### compression

- Schema name: `Compression`

Compresses SSH stream. Available only for SSH transport.
######## Any of

######### Option 1

- Type: enum (of string)

######### Option 2

- Type: null

####### speed_limit

- Schema name: `Speed Limit`

Limits speed of SSH stream. Available only for SSH transport.
######## Any of

######### Option 1

- Type: integer
- Value must be greater or equal to `1`

######### Option 2

- Type: null

####### large_block

- Schema name: `Large Block`
- Type: boolean

Enable large block support for ZFS send streams.

####### embed

- Schema name: `Embed`
- Type: boolean

Enable embedded block support for ZFS send streams.

####### compressed

- Schema name: `Compressed`
- Type: boolean

Enable compressed ZFS send streams.

####### retries

- Schema name: `Retries`
- Type: integer

Number of retries before considering replication failed.
- Value must be greater or equal to `1`

####### logging_level

- Schema name: `Logging Level`

Log level for replication task execution. Controls verbosity of replication logs.
######## Any of

######### Option 1

- Type: enum (of string)

######### Option 2

- Type: null

####### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this replication task is enabled.

####### state

- Schema name: `State`
- Type: object

Current state information for the replication task.

####### job

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
######## Any of

######### Option 1

- Type: object

######### Option 2

- Type: null

####### has_encrypted_dataset_keys

- Schema name: `Has Encrypted Dataset Keys`
- Type: boolean

Whether this replication task has encrypted dataset keys available.

##### ReplicationQueryResultItem

- Schema name: `KeychainCredentialEntry`
- Type: object
- No Additional Properties
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this keychain credential.

###### name (required)

- Schema name: `Name`
- Type: string

Distinguishes this Keychain Credential from others.
- Must be at least `1` characters long

###### type (required)

- Schema name: `Type`
- Type: enum (of string)

Type of credential stored in the keychain. `SSH_KEY_PAIR`: SSH public/private key pair `SSH_CREDENTIALS`: SSH connection credentials including host and authentication

###### attributes (required)

- Schema name: `Attributes`

Credential-specific configuration and authentication data.
####### Any of

######## SSHKeyPair

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
######### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
########## Any of

########### Option 1

- Type: string

########### Option 2

- Type: null

######## SSHCredentials

- Type: string

######## Option 1

- Type: null

######## Option 2

- Type: string

######## Option 1

- Type: null

######## Option 2

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
######### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

######### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

######### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

######### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

######### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

######### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

##### Option 3

- Schema name: `SSHKeyPair`
- Type: object

At least one of the two keys must be provided on creation.
- No Additional Properties
###### private_key

- Schema name: `Private Key`
- Default: null

SSH private key in OpenSSH format. `null` if only public key is provided.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### public_key

- Schema name: `Public Key`
- Default: null

Can be omitted and automatically derived from the private key.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### KeychainCredentialEntry

- Type: string

##### Option 2

- Type: null

##### SSHKeyPair

- Type: string

##### SSHCredentials

- Type: null

##### Option 1

- Schema name: `SSHCredentials`
- Type: object
- No Additional Properties
###### host (required)

- Schema name: `Host`
- Type: string

SSH server hostname or IP address.

###### port

- Schema name: `Port`
- Type: integer
- Default: 22

SSH server port number.

###### username

- Schema name: `Username`
- Type: string
- Default: "root"

SSH username for authentication.

###### private_key (required)

- Schema name: `Private Key`
- Type: integer

Keychain Credential ID.

###### remote_host_key (required)

- Schema name: `Remote Host Key`
- Type: string

Can be discovered with keychaincredential.remote*ssh*host*key*scan.

###### connect_timeout

- Schema name: `Connect Timeout`
- Type: integer
- Default: 10

Connection timeout in seconds for SSH connections.

##### Option 2

- Type: null

##### Option 1

- Type: enum (of string)

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: boolean

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: enum (of string)

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string
- Must be at least `1` characters long

##### Option 2

- Type: null

##### Option 1

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

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

###### begin

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

###### end

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

##### Option 2

- Type: null

##### ReplicationTimeCronModel

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59"

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

###### begin

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

###### end

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

##### Option 2

- Type: null

##### ReplicationTimeCronModel

- Type: integer
- Value must be greater or equal to `1`

##### Option 2

- Type: null

##### Option 1

- Type: enum (of string)

##### Option 2

- Type: null

##### Option 1

- Type: enum (of string)

##### Option 2

- Type: null

##### Option 1

- Type: integer
- Value must be greater or equal to `1`

##### Option 2

- Type: null

##### Option 1

- Type: enum (of string)

##### Option 2

- Type: null

##### Option 1

- Type: object

##### Option 2

- Type: null

##### Option 1

- Schema name: `ReplicationQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this replication task.

###### name

- Schema name: `Name`
- Type: string

Name for replication task.
- Must be at least `1` characters long

###### direction

- Schema name: `Direction`
- Type: enum (of string)

Whether task will `PUSH` or `PULL` snapshots.

###### transport

- Schema name: `Transport`
- Type: enum (of string)

Method of snapshots transfer. `SSH` transfers snapshots via SSH connection. This method is supported everywhere but does not achieve great performance. `SSH+NETCAT` uses unencrypted connection for data transfer. This can only be used in trusted networks and requires a port (specified by range from `netcat_active_side_port_min` to `netcat_active_side_port_max`) to be open on `netcat_active_side`. `LOCAL` replicates to or from localhost.

###### ssh_credentials

Keychain Credential of type `SSH_CREDENTIALS`.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### netcat_active_side

- Schema name: `Netcat Active Side`

Which side actively establishes the netcat connection for `SSH+NETCAT` transport. `LOCAL`: Local system initiates the connection `REMOTE`: Remote system initiates the connection `null`: Not applicable for other transport types
####### Any of

######## Option 1

- Type: enum (of string)

######## Option 2

- Type: null

###### netcat_active_side_listen_address

- Schema name: `Netcat Active Side Listen Address`

IP address for the active side to listen on for `SSH+NETCAT` transport. `null` if not applicable.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### netcat_active_side_port_min

- Schema name: `Netcat Active Side Port Min`

Minimum port number in the range for netcat connections. `null` if not applicable.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

######## Option 2

- Type: null

###### netcat_active_side_port_max

- Schema name: `Netcat Active Side Port Max`

Maximum port number in the range for netcat connections. `null` if not applicable.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

######## Option 2

- Type: null

###### netcat_passive_side_connect_address

- Schema name: `Netcat Passive Side Connect Address`

IP address for the passive side to connect to for `SSH+NETCAT` transport. `null` if not applicable.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### sudo

- Schema name: `Sudo`
- Type: boolean

`SSH` and `SSH+NETCAT` transports should use sudo (which is expected to be passwordless) to run `zfs` command on the remote machine.

###### source_datasets

- Schema name: `Source Datasets`
- Type: array of string

List of datasets to replicate snapshots from.
- Must contain a minimum of `1` items
- No Additional Items

####### Each item of this array must be:

- Type: string

###### target_dataset

- Schema name: `Target Dataset`
- Type: string

Dataset to put snapshots into.

###### recursive

- Schema name: `Recursive`
- Type: boolean

Whether to recursively replicate child datasets.

###### exclude

- Schema name: `Exclude`
- Type: array of string

Array of dataset patterns to exclude from replication.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### properties

- Schema name: `Properties`
- Type: boolean

Send dataset properties along with snapshots.

###### properties_exclude

- Schema name: `Properties Exclude`
- Type: array of string

Array of dataset property names to exclude from replication.
- No Additional Items

####### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

###### properties_override

- Schema name: `Properties Override`
- Type: object

Object mapping dataset property names to override values during replication.
####### Additional Properties

Each additional property must conform to the following schema
- Type: string

###### replicate

- Schema name: `Replicate`
- Type: boolean

Whether to use full ZFS replication.

###### encryption

- Schema name: `Encryption`
- Type: boolean

Whether to enable encryption for the replicated datasets.

###### encryption_inherit

- Schema name: `Encryption Inherit`

Whether replicated datasets should inherit encryption from parent. `null` if encryption is disabled.
####### Any of

######## Option 1

- Type: boolean

######## Option 2

- Type: null

###### encryption_key

- Schema name: `Encryption Key`

Encryption key for replicated datasets. `null` if not specified.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### encryption_key_format

- Schema name: `Encryption Key Format`

Format of the encryption key. `HEX`: Hexadecimal-encoded key `PASSPHRASE`: Text passphrase `null`: Not applicable when encryption is disabled
####### Any of

######## Option 1

- Type: enum (of string)

######## Option 2

- Type: null

###### encryption_key_location

- Schema name: `Encryption Key Location`

Filesystem path where encryption key is stored. `null` if not using key file.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### periodic_snapshot_tasks

- Schema name: `Periodic Snapshot Tasks`
- Type: array

List of periodic snapshot tasks that are sources of snapshots for this replication task. Only push replication tasks can be bound to periodic snapshot tasks.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### naming_schema

- Schema name: `Naming Schema`
- Type: array of string

List of naming schemas for pull replication.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### also_include_naming_schema

- Schema name: `Also Include Naming Schema`
- Type: array of string

List of naming schemas for push replication.
- No Additional Items

####### Each item of this array must be:

- Type: string

###### name_regex

- Schema name: `Name Regex`

Replicate all snapshots which names match specified regular expression.
####### Any of

######## Option 1

- Type: string
- Must be at least `1` characters long

######## Option 2

- Type: null

###### auto

- Schema name: `Auto`
- Type: boolean

Allow replication to run automatically on schedule or after bound periodic snapshot task.

###### schedule

Schedule to run replication task. Only `auto` replication tasks without bound periodic snapshot tasks can have a schedule.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### restrict_schedule

Restricts when replication task with bound periodic snapshot tasks runs. For example, you can have periodic snapshot tasks that run every 15 minutes, but only run replication task every hour.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### only_matching_schedule

- Schema name: `Only Matching Schedule`
- Type: boolean

Will only replicate snapshots that match `schedule` or `restrict_schedule`.

###### allow_from_scratch

- Schema name: `Allow From Scratch`
- Type: boolean

Will destroy all snapshots on target side and replicate everything from scratch if none of the snapshots on target side matches source snapshots.

###### readonly

- Schema name: `Readonly`
- Type: enum (of string)

Controls destination datasets readonly property. `SET`: Set all destination datasets to readonly=on after finishing the replication. `REQUIRE`: Require all existing destination datasets to have readonly=on property. `IGNORE`: Avoid this kind of behavior.

###### hold_pending_snapshots

- Schema name: `Hold Pending Snapshots`
- Type: boolean

Prevent source snapshots from being deleted by retention of replication fails for some reason.

###### retention_policy

- Schema name: `Retention Policy`
- Type: enum (of string)

How to delete old snapshots on target side: `SOURCE`: Delete snapshots that are absent on source side. `CUSTOM`: Delete snapshots that are older than `lifetime_value` and `lifetime_unit`. `NONE`: Do not delete any snapshots.

###### lifetime_value

- Schema name: `Lifetime Value`

Number of time units to retain snapshots for custom retention policy. Only applies when `retention_policy` is CUSTOM.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `1`

######## Option 2

- Type: null

###### lifetime_unit

- Schema name: `Lifetime Unit`

Time unit for snapshot retention for custom retention policy. Only applies when `retention_policy` is CUSTOM.
####### Any of

######## Option 1

- Type: enum (of string)

######## Option 2

- Type: null

###### lifetimes

- Schema name: `Lifetimes`
- Type: array

Array of different retention schedules with their own cron schedules and lifetime settings.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### compression

- Schema name: `Compression`

Compresses SSH stream. Available only for SSH transport.
####### Any of

######## Option 1

- Type: enum (of string)

######## Option 2

- Type: null

###### speed_limit

- Schema name: `Speed Limit`

Limits speed of SSH stream. Available only for SSH transport.
####### Any of

######## Option 1

- Type: integer
- Value must be greater or equal to `1`

######## Option 2

- Type: null

###### large_block

- Schema name: `Large Block`
- Type: boolean

Enable large block support for ZFS send streams.

###### embed

- Schema name: `Embed`
- Type: boolean

Enable embedded block support for ZFS send streams.

###### compressed

- Schema name: `Compressed`
- Type: boolean

Enable compressed ZFS send streams.

###### retries

- Schema name: `Retries`
- Type: integer

Number of retries before considering replication failed.
- Value must be greater or equal to `1`

###### logging_level

- Schema name: `Logging Level`

Log level for replication task execution. Controls verbosity of replication logs.
####### Any of

######## Option 1

- Type: enum (of string)

######## Option 2

- Type: null

###### enabled

- Schema name: `Enabled`
- Type: boolean

Whether this replication task is enabled.

###### state

- Schema name: `State`
- Type: object

Current state information for the replication task.

###### job

- Schema name: `Job`

Information about the currently running job. `null` if no job is running.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### has_encrypted_dataset_keys

- Schema name: `Has Encrypted Dataset Keys`
- Type: boolean

Whether this replication task has encrypted dataset keys available.

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: enum (of string)

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: boolean

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: enum (of string)

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string
- Must be at least `1` characters long

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `1`

##### Option 1

- Type: null

##### Option 2

- Type: enum (of string)

##### Option 1

- Type: null

##### Option 2

- Type: enum (of string)

##### Option 1

- Type: null

##### Option 2

- Type: integer
- Value must be greater or equal to `1`

##### Option 1

- Type: null

##### Option 2

- Type: enum (of string)

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
