---
title: replication.query
kind: event
source_rst: _sources/api_events_replication.query.rst.txt
source_html: api_events_replication.query.html
required_roles:
  - REPLICATION_TASK_READ
---

# replication.query

## Summary

Sent on replication changes.

## Required Roles

- `REPLICATION_TASK_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `ReplicationAddedEvent`
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

- Schema name: `ReplicationEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this replication task.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name for replication task.
- Must be at least `1` characters long

<a id="headingADDED_fields_direction"></a>
<a id="ADDED_fields_direction"></a>
##### direction (required)

- Schema name: `Direction`
- Type: enum (of string)

Whether task will `PUSH` or `PULL` snapshots.
###### Must be one of:

- "PUSH"
- "PULL"

<a id="headingADDED_fields_transport"></a>
<a id="ADDED_fields_transport"></a>
##### transport (required)

- Schema name: `Transport`
- Type: enum (of string)

Method of snapshots transfer. `SSH` transfers snapshots via SSH connection. This method is supported everywhere but does not achieve great performance. `SSH+NETCAT` uses unencrypted connection for data transfer. This can only be used in trusted networks and requires a port (specified by range from `netcat_active_side_port_min` to `netcat_active_side_port_max`) to be open on `netcat_active_side`. `LOCAL` replicates to or from localhost.
###### Must be one of:

- "SSH"
- "SSH+NETCAT"
- "LOCAL"

<a id="headingADDED_fields_ssh_credentials"></a>
<a id="ADDED_fields_ssh_credentials"></a>
##### ssh_credentials

- Default: null

Keychain Credential of type `SSH_CREDENTIALS`.
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

<a id="headingADDED_fields_netcat_active_side"></a>
<a id="ADDED_fields_netcat_active_side"></a>
##### netcat_active_side

- Schema name: `Netcat Active Side`
- Default: null

Which side actively establishes the netcat connection for `SSH+NETCAT` transport. `LOCAL`: Local system initiates the connection `REMOTE`: Remote system initiates the connection `null`: Not applicable for other transport types
<a id="ADDED_fields_netcat_active_side_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_netcat_active_side_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_netcat_active_side_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "LOCAL"
- "REMOTE"

<a id="tab-pane_ADDED_fields_netcat_active_side_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_netcat_active_side_anyOf_i1)

- Type: null

<a id="headingADDED_fields_netcat_active_side_listen_address"></a>
<a id="ADDED_fields_netcat_active_side_listen_address"></a>
##### netcat_active_side_listen_address

- Schema name: `Netcat Active Side Listen Address`
- Default: null

IP address for the active side to listen on for `SSH+NETCAT` transport. `null` if not applicable.
<a id="ADDED_fields_netcat_active_side_listen_address_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_netcat_active_side_listen_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_netcat_active_side_listen_address_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_netcat_active_side_listen_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_netcat_active_side_listen_address_anyOf_i1)

- Type: null

<a id="headingADDED_fields_netcat_active_side_port_min"></a>
<a id="ADDED_fields_netcat_active_side_port_min"></a>
##### netcat_active_side_port_min

- Schema name: `Netcat Active Side Port Min`
- Default: null

Minimum port number in the range for netcat connections. `null` if not applicable.
<a id="ADDED_fields_netcat_active_side_port_min_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_netcat_active_side_port_min_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_netcat_active_side_port_min_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_ADDED_fields_netcat_active_side_port_min_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_netcat_active_side_port_min_anyOf_i1)

- Type: null

<a id="headingADDED_fields_netcat_active_side_port_max"></a>
<a id="ADDED_fields_netcat_active_side_port_max"></a>
##### netcat_active_side_port_max

- Schema name: `Netcat Active Side Port Max`
- Default: null

Maximum port number in the range for netcat connections. `null` if not applicable.
<a id="ADDED_fields_netcat_active_side_port_max_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_netcat_active_side_port_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_netcat_active_side_port_max_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_ADDED_fields_netcat_active_side_port_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_netcat_active_side_port_max_anyOf_i1)

- Type: null

<a id="headingADDED_fields_netcat_passive_side_connect_address"></a>
<a id="ADDED_fields_netcat_passive_side_connect_address"></a>
##### netcat_passive_side_connect_address

- Schema name: `Netcat Passive Side Connect Address`
- Default: null

IP address for the passive side to connect to for `SSH+NETCAT` transport. `null` if not applicable.
<a id="ADDED_fields_netcat_passive_side_connect_address_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_netcat_passive_side_connect_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_netcat_passive_side_connect_address_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_netcat_passive_side_connect_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_netcat_passive_side_connect_address_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sudo"></a>
<a id="ADDED_fields_sudo"></a>
##### sudo

- Schema name: `Sudo`
- Type: boolean
- Default: false

`SSH` and `SSH+NETCAT` transports should use sudo (which is expected to be passwordless) to run `zfs` command on the remote machine.

<a id="headingADDED_fields_source_datasets"></a>
<a id="ADDED_fields_source_datasets"></a>
##### source_datasets (required)

- Schema name: `Source Datasets`
- Type: array of string

List of datasets to replicate snapshots from.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_source_datasets_items"></a>
- Type: string

<a id="headingADDED_fields_target_dataset"></a>
<a id="ADDED_fields_target_dataset"></a>
##### target_dataset (required)

- Schema name: `Target Dataset`
- Type: string

Dataset to put snapshots into.

<a id="headingADDED_fields_recursive"></a>
<a id="ADDED_fields_recursive"></a>
##### recursive (required)

- Schema name: `Recursive`
- Type: boolean

Whether to recursively replicate child datasets.

<a id="headingADDED_fields_exclude"></a>
<a id="ADDED_fields_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from replication.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_exclude_items"></a>
- Type: string

<a id="headingADDED_fields_properties"></a>
<a id="ADDED_fields_properties"></a>
##### properties

- Schema name: `Properties`
- Type: boolean
- Default: true

Send dataset properties along with snapshots.

<a id="headingADDED_fields_properties_exclude"></a>
<a id="ADDED_fields_properties_exclude"></a>
##### properties_exclude

- Schema name: `Properties Exclude`
- Type: array of string
- Default: []

Array of dataset property names to exclude from replication.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_properties_exclude_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_properties_override"></a>
<a id="ADDED_fields_properties_override"></a>
##### properties_override

- Schema name: `Properties Override`
- Type: object
- Default: {}

Object mapping dataset property names to override values during replication.
<a id="headingADDED_fields_properties_override_additionalProperties"></a>
<a id="ADDED_fields_properties_override_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingADDED_fields_replicate"></a>
<a id="ADDED_fields_replicate"></a>
##### replicate

- Schema name: `Replicate`
- Type: boolean
- Default: false

Whether to use full ZFS replication.

<a id="headingADDED_fields_encryption"></a>
<a id="ADDED_fields_encryption"></a>
##### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether to enable encryption for the replicated datasets.

<a id="headingADDED_fields_encryption_inherit"></a>
<a id="ADDED_fields_encryption_inherit"></a>
##### encryption_inherit

- Schema name: `Encryption Inherit`
- Default: null

Whether replicated datasets should inherit encryption from parent. `null` if encryption is disabled.
<a id="ADDED_fields_encryption_inherit_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_inherit_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_inherit_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_encryption_inherit_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_inherit_anyOf_i1)

- Type: null

<a id="headingADDED_fields_encryption_key"></a>
<a id="ADDED_fields_encryption_key"></a>
##### encryption_key

- Schema name: `Encryption Key`
- Default: null

Encryption key for replicated datasets. `null` if not specified.
<a id="ADDED_fields_encryption_key_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_key_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_encryption_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_key_anyOf_i1)

- Type: null

<a id="headingADDED_fields_encryption_key_format"></a>
<a id="ADDED_fields_encryption_key_format"></a>
##### encryption_key_format

- Schema name: `Encryption Key Format`
- Default: null

Format of the encryption key. `HEX`: Hexadecimal-encoded key `PASSPHRASE`: Text passphrase `null`: Not applicable when encryption is disabled
<a id="ADDED_fields_encryption_key_format_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_key_format_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_key_format_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "HEX"
- "PASSPHRASE"

<a id="tab-pane_ADDED_fields_encryption_key_format_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_key_format_anyOf_i1)

- Type: null

<a id="headingADDED_fields_encryption_key_location"></a>
<a id="ADDED_fields_encryption_key_location"></a>
##### encryption_key_location

- Schema name: `Encryption Key Location`
- Default: null

Filesystem path where encryption key is stored. `null` if not using key file.
<a id="ADDED_fields_encryption_key_location_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_encryption_key_location_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_encryption_key_location_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_encryption_key_location_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_encryption_key_location_anyOf_i1)

- Type: null

<a id="headingADDED_fields_periodic_snapshot_tasks"></a>
<a id="ADDED_fields_periodic_snapshot_tasks"></a>
##### periodic_snapshot_tasks (required)

- Schema name: `Periodic Snapshot Tasks`
- Type: array of object

List of periodic snapshot tasks that are sources of snapshots for this replication task. Only push replication tasks can be bound to periodic snapshot tasks.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_periodic_snapshot_tasks_items"></a>
###### PoolSnapshotTaskDBEntry

- Schema name: `PoolSnapshotTaskDBEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_periodic_snapshot_tasks_items_id"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingADDED_fields_periodic_snapshot_tasks_items_dataset"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingADDED_fields_periodic_snapshot_tasks_items_recursive"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingADDED_fields_periodic_snapshot_tasks_items_lifetime_value"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_lifetime_value"></a>
###### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_periodic_snapshot_tasks_items_lifetime_unit"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_lifetime_unit"></a>
###### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingADDED_fields_periodic_snapshot_tasks_items_enabled"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingADDED_fields_periodic_snapshot_tasks_items_exclude"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_periodic_snapshot_tasks_items_exclude_items"></a>
- Type: string

<a id="headingADDED_fields_periodic_snapshot_tasks_items_naming_schema"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_naming_schema"></a>
###### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingADDED_fields_periodic_snapshot_tasks_items_allow_empty"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_allow_empty"></a>
###### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule"></a>
###### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_minute"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_hour"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_dom"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_month"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_dow"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_begin"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_begin"></a>
###### begin

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

<a id="headingADDED_fields_periodic_snapshot_tasks_items_schedule_end"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_schedule_end"></a>
###### end

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

<a id="headingADDED_fields_periodic_snapshot_tasks_items_state"></a>
<a id="ADDED_fields_periodic_snapshot_tasks_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

<a id="headingADDED_fields_naming_schema"></a>
<a id="ADDED_fields_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: array of string
- Default: []

List of naming schemas for pull replication.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_naming_schema_items"></a>
- Type: string

<a id="headingADDED_fields_also_include_naming_schema"></a>
<a id="ADDED_fields_also_include_naming_schema"></a>
##### also_include_naming_schema

- Schema name: `Also Include Naming Schema`
- Type: array of string
- Default: []

List of naming schemas for push replication.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_also_include_naming_schema_items"></a>
- Type: string

<a id="headingADDED_fields_name_regex"></a>
<a id="ADDED_fields_name_regex"></a>
##### name_regex

- Schema name: `Name Regex`
- Default: null

Replicate all snapshots which names match specified regular expression.
<a id="ADDED_fields_name_regex_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_name_regex_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_name_regex_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_name_regex_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_name_regex_anyOf_i1)

- Type: null

<a id="headingADDED_fields_auto"></a>
<a id="ADDED_fields_auto"></a>
##### auto (required)

- Schema name: `Auto`
- Type: boolean

Allow replication to run automatically on schedule or after bound periodic snapshot task.

<a id="headingADDED_fields_schedule"></a>
<a id="ADDED_fields_schedule"></a>
##### schedule

- Default: null

Schedule to run replication task. Only `auto` replication tasks without bound periodic snapshot tasks can have a schedule.
<a id="ADDED_fields_schedule_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_schedule_anyOf_i0"></a>
###### [ReplicationTimeCronModel](#tab-pane_ADDED_fields_schedule_anyOf_i0)

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_schedule_anyOf_i0_minute"></a>
<a id="ADDED_fields_schedule_anyOf_i0_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingADDED_fields_schedule_anyOf_i0_hour"></a>
<a id="ADDED_fields_schedule_anyOf_i0_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_schedule_anyOf_i0_dom"></a>
<a id="ADDED_fields_schedule_anyOf_i0_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_schedule_anyOf_i0_month"></a>
<a id="ADDED_fields_schedule_anyOf_i0_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_schedule_anyOf_i0_dow"></a>
<a id="ADDED_fields_schedule_anyOf_i0_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_schedule_anyOf_i0_begin"></a>
<a id="ADDED_fields_schedule_anyOf_i0_begin"></a>
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

<a id="headingADDED_fields_schedule_anyOf_i0_end"></a>
<a id="ADDED_fields_schedule_anyOf_i0_end"></a>
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

<a id="tab-pane_ADDED_fields_schedule_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_schedule_anyOf_i1)

- Type: null

<a id="headingADDED_fields_restrict_schedule"></a>
<a id="ADDED_fields_restrict_schedule"></a>
##### restrict_schedule

- Default: null

Restricts when replication task with bound periodic snapshot tasks runs. For example, you can have periodic snapshot tasks that run every 15 minutes, but only run replication task every hour.
<a id="ADDED_fields_restrict_schedule_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_restrict_schedule_anyOf_i0"></a>
###### [ReplicationTimeCronModel](#tab-pane_ADDED_fields_restrict_schedule_anyOf_i0)

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_restrict_schedule_anyOf_i0_minute"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingADDED_fields_restrict_schedule_anyOf_i0_hour"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_restrict_schedule_anyOf_i0_dom"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_restrict_schedule_anyOf_i0_month"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_restrict_schedule_anyOf_i0_dow"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_restrict_schedule_anyOf_i0_begin"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_begin"></a>
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

<a id="headingADDED_fields_restrict_schedule_anyOf_i0_end"></a>
<a id="ADDED_fields_restrict_schedule_anyOf_i0_end"></a>
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

<a id="tab-pane_ADDED_fields_restrict_schedule_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_restrict_schedule_anyOf_i1)

- Type: null

<a id="headingADDED_fields_only_matching_schedule"></a>
<a id="ADDED_fields_only_matching_schedule"></a>
##### only_matching_schedule

- Schema name: `Only Matching Schedule`
- Type: boolean
- Default: false

Will only replicate snapshots that match `schedule` or `restrict_schedule`.

<a id="headingADDED_fields_allow_from_scratch"></a>
<a id="ADDED_fields_allow_from_scratch"></a>
##### allow_from_scratch

- Schema name: `Allow From Scratch`
- Type: boolean
- Default: false

Will destroy all snapshots on target side and replicate everything from scratch if none of the snapshots on target side matches source snapshots.

<a id="headingADDED_fields_readonly"></a>
<a id="ADDED_fields_readonly"></a>
##### readonly

- Schema name: `Readonly`
- Type: enum (of string)
- Default: "SET"

Controls destination datasets readonly property. `SET`: Set all destination datasets to readonly=on after finishing the replication. `REQUIRE`: Require all existing destination datasets to have readonly=on property. `IGNORE`: Avoid this kind of behavior.
###### Must be one of:

- "SET"
- "REQUIRE"
- "IGNORE"

<a id="headingADDED_fields_hold_pending_snapshots"></a>
<a id="ADDED_fields_hold_pending_snapshots"></a>
##### hold_pending_snapshots

- Schema name: `Hold Pending Snapshots`
- Type: boolean
- Default: false

Prevent source snapshots from being deleted by retention of replication fails for some reason.

<a id="headingADDED_fields_retention_policy"></a>
<a id="ADDED_fields_retention_policy"></a>
##### retention_policy (required)

- Schema name: `Retention Policy`
- Type: enum (of string)

How to delete old snapshots on target side: `SOURCE`: Delete snapshots that are absent on source side. `CUSTOM`: Delete snapshots that are older than `lifetime_value` and `lifetime_unit`. `NONE`: Do not delete any snapshots.
###### Must be one of:

- "SOURCE"
- "CUSTOM"
- "NONE"

<a id="headingADDED_fields_lifetime_value"></a>
<a id="ADDED_fields_lifetime_value"></a>
##### lifetime_value

- Schema name: `Lifetime Value`
- Default: null

Number of time units to retain snapshots for custom retention policy. Only applies when `retention_policy` is CUSTOM.
<a id="ADDED_fields_lifetime_value_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_lifetime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_lifetime_value_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1`

<a id="tab-pane_ADDED_fields_lifetime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_lifetime_value_anyOf_i1)

- Type: null

<a id="headingADDED_fields_lifetime_unit"></a>
<a id="ADDED_fields_lifetime_unit"></a>
##### lifetime_unit

- Schema name: `Lifetime Unit`
- Default: null

Time unit for snapshot retention for custom retention policy. Only applies when `retention_policy` is CUSTOM.
<a id="ADDED_fields_lifetime_unit_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_lifetime_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_lifetime_unit_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="tab-pane_ADDED_fields_lifetime_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_lifetime_unit_anyOf_i1)

- Type: null

<a id="headingADDED_fields_lifetimes"></a>
<a id="ADDED_fields_lifetimes"></a>
##### lifetimes

- Schema name: `Lifetimes`
- Type: array of object
- Default: []

Array of different retention schedules with their own cron schedules and lifetime settings.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_lifetimes_items"></a>
###### ReplicationLifetimeModel

- Schema name: `ReplicationLifetimeModel`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_lifetimes_items_schedule"></a>
<a id="ADDED_fields_lifetimes_items_schedule"></a>
###### schedule (required)

- Schema name: `CronModel`
- Type: object

Cron schedule for when snapshot retention policies are applied.
- No Additional Properties
<a id="headingADDED_fields_lifetimes_items_schedule_minute"></a>
<a id="ADDED_fields_lifetimes_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "*"

"00" - "59".

<a id="headingADDED_fields_lifetimes_items_schedule_hour"></a>
<a id="ADDED_fields_lifetimes_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingADDED_fields_lifetimes_items_schedule_dom"></a>
<a id="ADDED_fields_lifetimes_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingADDED_fields_lifetimes_items_schedule_month"></a>
<a id="ADDED_fields_lifetimes_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingADDED_fields_lifetimes_items_schedule_dow"></a>
<a id="ADDED_fields_lifetimes_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingADDED_fields_lifetimes_items_lifetime_value"></a>
<a id="ADDED_fields_lifetimes_items_lifetime_value"></a>
###### lifetime_value (required)

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_lifetimes_items_lifetime_unit"></a>
<a id="ADDED_fields_lifetimes_items_lifetime_unit"></a>
###### lifetime_unit (required)

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Time unit for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingADDED_fields_compression"></a>
<a id="ADDED_fields_compression"></a>
##### compression

- Schema name: `Compression`
- Default: null

Compresses SSH stream. Available only for SSH transport.
<a id="ADDED_fields_compression_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_compression_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_compression_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "LZ4"
- "PIGZ"
- "PLZIP"

<a id="tab-pane_ADDED_fields_compression_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_compression_anyOf_i1)

- Type: null

<a id="headingADDED_fields_speed_limit"></a>
<a id="ADDED_fields_speed_limit"></a>
##### speed_limit

- Schema name: `Speed Limit`
- Default: null

Limits speed of SSH stream. Available only for SSH transport.
<a id="ADDED_fields_speed_limit_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_speed_limit_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_speed_limit_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1`

<a id="tab-pane_ADDED_fields_speed_limit_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_speed_limit_anyOf_i1)

- Type: null

<a id="headingADDED_fields_large_block"></a>
<a id="ADDED_fields_large_block"></a>
##### large_block

- Schema name: `Large Block`
- Type: boolean
- Default: true

Enable large block support for ZFS send streams.

<a id="headingADDED_fields_embed"></a>
<a id="ADDED_fields_embed"></a>
##### embed

- Schema name: `Embed`
- Type: boolean
- Default: false

Enable embedded block support for ZFS send streams.

<a id="headingADDED_fields_compressed"></a>
<a id="ADDED_fields_compressed"></a>
##### compressed

- Schema name: `Compressed`
- Type: boolean
- Default: true

Enable compressed ZFS send streams.

<a id="headingADDED_fields_retries"></a>
<a id="ADDED_fields_retries"></a>
##### retries

- Schema name: `Retries`
- Type: integer
- Default: 5

Number of retries before considering replication failed.
- Value must be greater or equal to `1`

<a id="headingADDED_fields_logging_level"></a>
<a id="ADDED_fields_logging_level"></a>
##### logging_level

- Schema name: `Logging Level`
- Default: null

Log level for replication task execution. Controls verbosity of replication logs.
<a id="ADDED_fields_logging_level_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_logging_level_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_logging_level_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "DEBUG"
- "INFO"
- "WARNING"
- "ERROR"

<a id="tab-pane_ADDED_fields_logging_level_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_logging_level_anyOf_i1)

- Type: null

<a id="headingADDED_fields_enabled"></a>
<a id="ADDED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this replication task is enabled.

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: object

Current state information for the replication task.

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

<a id="headingADDED_fields_has_encrypted_dataset_keys"></a>
<a id="ADDED_fields_has_encrypted_dataset_keys"></a>
##### has_encrypted_dataset_keys (required)

- Schema name: `Has Encrypted Dataset Keys`
- Type: boolean

Whether this replication task has encrypted dataset keys available.

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `ReplicationChangedEvent`
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

- Schema name: `ReplicationEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this replication task.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name for replication task.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_direction"></a>
<a id="CHANGED_fields_direction"></a>
##### direction (required)

- Schema name: `Direction`
- Type: enum (of string)

Whether task will `PUSH` or `PULL` snapshots.
###### Must be one of:

- "PUSH"
- "PULL"

<a id="headingCHANGED_fields_transport"></a>
<a id="CHANGED_fields_transport"></a>
##### transport (required)

- Schema name: `Transport`
- Type: enum (of string)

Method of snapshots transfer. `SSH` transfers snapshots via SSH connection. This method is supported everywhere but does not achieve great performance. `SSH+NETCAT` uses unencrypted connection for data transfer. This can only be used in trusted networks and requires a port (specified by range from `netcat_active_side_port_min` to `netcat_active_side_port_max`) to be open on `netcat_active_side`. `LOCAL` replicates to or from localhost.
###### Must be one of:

- "SSH"
- "SSH+NETCAT"
- "LOCAL"

<a id="headingCHANGED_fields_ssh_credentials"></a>
<a id="CHANGED_fields_ssh_credentials"></a>
##### ssh_credentials

- Default: null

Keychain Credential of type `SSH_CREDENTIALS`.
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

<a id="headingCHANGED_fields_netcat_active_side"></a>
<a id="CHANGED_fields_netcat_active_side"></a>
##### netcat_active_side

- Schema name: `Netcat Active Side`
- Default: null

Which side actively establishes the netcat connection for `SSH+NETCAT` transport. `LOCAL`: Local system initiates the connection `REMOTE`: Remote system initiates the connection `null`: Not applicable for other transport types
<a id="CHANGED_fields_netcat_active_side_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_netcat_active_side_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_netcat_active_side_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "LOCAL"
- "REMOTE"

<a id="tab-pane_CHANGED_fields_netcat_active_side_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_netcat_active_side_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_netcat_active_side_listen_address"></a>
<a id="CHANGED_fields_netcat_active_side_listen_address"></a>
##### netcat_active_side_listen_address

- Schema name: `Netcat Active Side Listen Address`
- Default: null

IP address for the active side to listen on for `SSH+NETCAT` transport. `null` if not applicable.
<a id="CHANGED_fields_netcat_active_side_listen_address_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_netcat_active_side_listen_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_netcat_active_side_listen_address_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_netcat_active_side_listen_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_netcat_active_side_listen_address_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_netcat_active_side_port_min"></a>
<a id="CHANGED_fields_netcat_active_side_port_min"></a>
##### netcat_active_side_port_min

- Schema name: `Netcat Active Side Port Min`
- Default: null

Minimum port number in the range for netcat connections. `null` if not applicable.
<a id="CHANGED_fields_netcat_active_side_port_min_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_netcat_active_side_port_min_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_netcat_active_side_port_min_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_CHANGED_fields_netcat_active_side_port_min_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_netcat_active_side_port_min_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_netcat_active_side_port_max"></a>
<a id="CHANGED_fields_netcat_active_side_port_max"></a>
##### netcat_active_side_port_max

- Schema name: `Netcat Active Side Port Max`
- Default: null

Maximum port number in the range for netcat connections. `null` if not applicable.
<a id="CHANGED_fields_netcat_active_side_port_max_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_netcat_active_side_port_max_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_netcat_active_side_port_max_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `65535`

<a id="tab-pane_CHANGED_fields_netcat_active_side_port_max_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_netcat_active_side_port_max_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_netcat_passive_side_connect_address"></a>
<a id="CHANGED_fields_netcat_passive_side_connect_address"></a>
##### netcat_passive_side_connect_address

- Schema name: `Netcat Passive Side Connect Address`
- Default: null

IP address for the passive side to connect to for `SSH+NETCAT` transport. `null` if not applicable.
<a id="CHANGED_fields_netcat_passive_side_connect_address_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_netcat_passive_side_connect_address_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_netcat_passive_side_connect_address_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_netcat_passive_side_connect_address_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_netcat_passive_side_connect_address_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sudo"></a>
<a id="CHANGED_fields_sudo"></a>
##### sudo

- Schema name: `Sudo`
- Type: boolean
- Default: false

`SSH` and `SSH+NETCAT` transports should use sudo (which is expected to be passwordless) to run `zfs` command on the remote machine.

<a id="headingCHANGED_fields_source_datasets"></a>
<a id="CHANGED_fields_source_datasets"></a>
##### source_datasets (required)

- Schema name: `Source Datasets`
- Type: array of string

List of datasets to replicate snapshots from.
- Must contain a minimum of `1` items
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_source_datasets_items"></a>
- Type: string

<a id="headingCHANGED_fields_target_dataset"></a>
<a id="CHANGED_fields_target_dataset"></a>
##### target_dataset (required)

- Schema name: `Target Dataset`
- Type: string

Dataset to put snapshots into.

<a id="headingCHANGED_fields_recursive"></a>
<a id="CHANGED_fields_recursive"></a>
##### recursive (required)

- Schema name: `Recursive`
- Type: boolean

Whether to recursively replicate child datasets.

<a id="headingCHANGED_fields_exclude"></a>
<a id="CHANGED_fields_exclude"></a>
##### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from replication.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_exclude_items"></a>
- Type: string

<a id="headingCHANGED_fields_properties"></a>
<a id="CHANGED_fields_properties"></a>
##### properties

- Schema name: `Properties`
- Type: boolean
- Default: true

Send dataset properties along with snapshots.

<a id="headingCHANGED_fields_properties_exclude"></a>
<a id="CHANGED_fields_properties_exclude"></a>
##### properties_exclude

- Schema name: `Properties Exclude`
- Type: array of string
- Default: []

Array of dataset property names to exclude from replication.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_properties_exclude_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_properties_override"></a>
<a id="CHANGED_fields_properties_override"></a>
##### properties_override

- Schema name: `Properties Override`
- Type: object
- Default: {}

Object mapping dataset property names to override values during replication.
<a id="headingCHANGED_fields_properties_override_additionalProperties"></a>
<a id="CHANGED_fields_properties_override_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="headingCHANGED_fields_replicate"></a>
<a id="CHANGED_fields_replicate"></a>
##### replicate

- Schema name: `Replicate`
- Type: boolean
- Default: false

Whether to use full ZFS replication.

<a id="headingCHANGED_fields_encryption"></a>
<a id="CHANGED_fields_encryption"></a>
##### encryption

- Schema name: `Encryption`
- Type: boolean
- Default: false

Whether to enable encryption for the replicated datasets.

<a id="headingCHANGED_fields_encryption_inherit"></a>
<a id="CHANGED_fields_encryption_inherit"></a>
##### encryption_inherit

- Schema name: `Encryption Inherit`
- Default: null

Whether replicated datasets should inherit encryption from parent. `null` if encryption is disabled.
<a id="CHANGED_fields_encryption_inherit_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_inherit_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_inherit_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_encryption_inherit_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_inherit_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_encryption_key"></a>
<a id="CHANGED_fields_encryption_key"></a>
##### encryption_key

- Schema name: `Encryption Key`
- Default: null

Encryption key for replicated datasets. `null` if not specified.
<a id="CHANGED_fields_encryption_key_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_key_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_key_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_encryption_key_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_key_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_encryption_key_format"></a>
<a id="CHANGED_fields_encryption_key_format"></a>
##### encryption_key_format

- Schema name: `Encryption Key Format`
- Default: null

Format of the encryption key. `HEX`: Hexadecimal-encoded key `PASSPHRASE`: Text passphrase `null`: Not applicable when encryption is disabled
<a id="CHANGED_fields_encryption_key_format_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_key_format_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_key_format_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "HEX"
- "PASSPHRASE"

<a id="tab-pane_CHANGED_fields_encryption_key_format_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_key_format_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_encryption_key_location"></a>
<a id="CHANGED_fields_encryption_key_location"></a>
##### encryption_key_location

- Schema name: `Encryption Key Location`
- Default: null

Filesystem path where encryption key is stored. `null` if not using key file.
<a id="CHANGED_fields_encryption_key_location_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_encryption_key_location_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_encryption_key_location_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_encryption_key_location_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_encryption_key_location_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_periodic_snapshot_tasks"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks"></a>
##### periodic_snapshot_tasks (required)

- Schema name: `Periodic Snapshot Tasks`
- Type: array of object

List of periodic snapshot tasks that are sources of snapshots for this replication task. Only push replication tasks can be bound to periodic snapshot tasks.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_periodic_snapshot_tasks_items"></a>
###### PoolSnapshotTaskDBEntry

- Schema name: `PoolSnapshotTaskDBEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_id"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the periodic snapshot task.

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_dataset"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_dataset"></a>
###### dataset (required)

- Schema name: `Dataset`
- Type: string

The dataset to take snapshots of.

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_recursive"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_recursive"></a>
###### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Whether to recursively snapshot child datasets.

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_lifetime_value"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_lifetime_value"></a>
###### lifetime_value

- Schema name: `Lifetime Value`
- Type: integer
- Default: 2

Number of time units to retain snapshots. `lifetime_unit` gives the time unit.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_lifetime_unit"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_lifetime_unit"></a>
###### lifetime_unit

- Schema name: `Lifetime Unit`
- Type: enum (of string)
- Default: "WEEK"

Unit of time for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_enabled"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_enabled"></a>
###### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this periodic snapshot task is enabled.

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_exclude"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_exclude"></a>
###### exclude

- Schema name: `Exclude`
- Type: array of string
- Default: []

Array of dataset patterns to exclude from recursive snapshots.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_periodic_snapshot_tasks_items_exclude_items"></a>
- Type: string

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_naming_schema"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_naming_schema"></a>
###### naming_schema

- Schema name: `Naming Schema`
- Type: string
- Default: "auto-%Y-%m-%d_%H-%M"

Naming pattern for generated snapshots using strftime format.

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_allow_empty"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_allow_empty"></a>
###### allow_empty

- Schema name: `Allow Empty`
- Type: boolean
- Default: true

Whether to take snapshots even if no data has changed.

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule"></a>
###### schedule

- Schema name: `PoolSnapshotTaskCron`
- Type: object

Cron schedule for when snapshots should be taken.
- No Additional Properties
<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_minute"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

Minute when snapshots should be taken (cron format).

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_hour"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_dom"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_month"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_dow"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_begin"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_begin"></a>
###### begin

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

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_schedule_end"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_schedule_end"></a>
###### end

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

<a id="headingCHANGED_fields_periodic_snapshot_tasks_items_state"></a>
<a id="CHANGED_fields_periodic_snapshot_tasks_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: string

<a id="headingCHANGED_fields_naming_schema"></a>
<a id="CHANGED_fields_naming_schema"></a>
##### naming_schema

- Schema name: `Naming Schema`
- Type: array of string
- Default: []

List of naming schemas for pull replication.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_naming_schema_items"></a>
- Type: string

<a id="headingCHANGED_fields_also_include_naming_schema"></a>
<a id="CHANGED_fields_also_include_naming_schema"></a>
##### also_include_naming_schema

- Schema name: `Also Include Naming Schema`
- Type: array of string
- Default: []

List of naming schemas for push replication.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_also_include_naming_schema_items"></a>
- Type: string

<a id="headingCHANGED_fields_name_regex"></a>
<a id="CHANGED_fields_name_regex"></a>
##### name_regex

- Schema name: `Name Regex`
- Default: null

Replicate all snapshots which names match specified regular expression.
<a id="CHANGED_fields_name_regex_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_name_regex_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_name_regex_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_name_regex_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_name_regex_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_auto"></a>
<a id="CHANGED_fields_auto"></a>
##### auto (required)

- Schema name: `Auto`
- Type: boolean

Allow replication to run automatically on schedule or after bound periodic snapshot task.

<a id="headingCHANGED_fields_schedule"></a>
<a id="CHANGED_fields_schedule"></a>
##### schedule

- Default: null

Schedule to run replication task. Only `auto` replication tasks without bound periodic snapshot tasks can have a schedule.
<a id="CHANGED_fields_schedule_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_schedule_anyOf_i0"></a>
###### [ReplicationTimeCronModel](#tab-pane_CHANGED_fields_schedule_anyOf_i0)

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_schedule_anyOf_i0_minute"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingCHANGED_fields_schedule_anyOf_i0_hour"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_schedule_anyOf_i0_dom"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_schedule_anyOf_i0_month"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_schedule_anyOf_i0_dow"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_schedule_anyOf_i0_begin"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_begin"></a>
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

<a id="headingCHANGED_fields_schedule_anyOf_i0_end"></a>
<a id="CHANGED_fields_schedule_anyOf_i0_end"></a>
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

<a id="tab-pane_CHANGED_fields_schedule_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_schedule_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_restrict_schedule"></a>
<a id="CHANGED_fields_restrict_schedule"></a>
##### restrict_schedule

- Default: null

Restricts when replication task with bound periodic snapshot tasks runs. For example, you can have periodic snapshot tasks that run every 15 minutes, but only run replication task every hour.
<a id="CHANGED_fields_restrict_schedule_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_restrict_schedule_anyOf_i0"></a>
###### [ReplicationTimeCronModel](#tab-pane_CHANGED_fields_restrict_schedule_anyOf_i0)

- Schema name: `ReplicationTimeCronModel`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_minute"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "00"

"00" - "59".

<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_hour"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_dom"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_month"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_dow"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_begin"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_begin"></a>
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

<a id="headingCHANGED_fields_restrict_schedule_anyOf_i0_end"></a>
<a id="CHANGED_fields_restrict_schedule_anyOf_i0_end"></a>
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

<a id="tab-pane_CHANGED_fields_restrict_schedule_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_restrict_schedule_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_only_matching_schedule"></a>
<a id="CHANGED_fields_only_matching_schedule"></a>
##### only_matching_schedule

- Schema name: `Only Matching Schedule`
- Type: boolean
- Default: false

Will only replicate snapshots that match `schedule` or `restrict_schedule`.

<a id="headingCHANGED_fields_allow_from_scratch"></a>
<a id="CHANGED_fields_allow_from_scratch"></a>
##### allow_from_scratch

- Schema name: `Allow From Scratch`
- Type: boolean
- Default: false

Will destroy all snapshots on target side and replicate everything from scratch if none of the snapshots on target side matches source snapshots.

<a id="headingCHANGED_fields_readonly"></a>
<a id="CHANGED_fields_readonly"></a>
##### readonly

- Schema name: `Readonly`
- Type: enum (of string)
- Default: "SET"

Controls destination datasets readonly property. `SET`: Set all destination datasets to readonly=on after finishing the replication. `REQUIRE`: Require all existing destination datasets to have readonly=on property. `IGNORE`: Avoid this kind of behavior.
###### Must be one of:

- "SET"
- "REQUIRE"
- "IGNORE"

<a id="headingCHANGED_fields_hold_pending_snapshots"></a>
<a id="CHANGED_fields_hold_pending_snapshots"></a>
##### hold_pending_snapshots

- Schema name: `Hold Pending Snapshots`
- Type: boolean
- Default: false

Prevent source snapshots from being deleted by retention of replication fails for some reason.

<a id="headingCHANGED_fields_retention_policy"></a>
<a id="CHANGED_fields_retention_policy"></a>
##### retention_policy (required)

- Schema name: `Retention Policy`
- Type: enum (of string)

How to delete old snapshots on target side: `SOURCE`: Delete snapshots that are absent on source side. `CUSTOM`: Delete snapshots that are older than `lifetime_value` and `lifetime_unit`. `NONE`: Do not delete any snapshots.
###### Must be one of:

- "SOURCE"
- "CUSTOM"
- "NONE"

<a id="headingCHANGED_fields_lifetime_value"></a>
<a id="CHANGED_fields_lifetime_value"></a>
##### lifetime_value

- Schema name: `Lifetime Value`
- Default: null

Number of time units to retain snapshots for custom retention policy. Only applies when `retention_policy` is CUSTOM.
<a id="CHANGED_fields_lifetime_value_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_lifetime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_lifetime_value_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1`

<a id="tab-pane_CHANGED_fields_lifetime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_lifetime_value_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_lifetime_unit"></a>
<a id="CHANGED_fields_lifetime_unit"></a>
##### lifetime_unit

- Schema name: `Lifetime Unit`
- Default: null

Time unit for snapshot retention for custom retention policy. Only applies when `retention_policy` is CUSTOM.
<a id="CHANGED_fields_lifetime_unit_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_lifetime_unit_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_lifetime_unit_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="tab-pane_CHANGED_fields_lifetime_unit_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_lifetime_unit_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_lifetimes"></a>
<a id="CHANGED_fields_lifetimes"></a>
##### lifetimes

- Schema name: `Lifetimes`
- Type: array of object
- Default: []

Array of different retention schedules with their own cron schedules and lifetime settings.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_lifetimes_items"></a>
###### ReplicationLifetimeModel

- Schema name: `ReplicationLifetimeModel`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_lifetimes_items_schedule"></a>
<a id="CHANGED_fields_lifetimes_items_schedule"></a>
###### schedule (required)

- Schema name: `CronModel`
- Type: object

Cron schedule for when snapshot retention policies are applied.
- No Additional Properties
<a id="headingCHANGED_fields_lifetimes_items_schedule_minute"></a>
<a id="CHANGED_fields_lifetimes_items_schedule_minute"></a>
###### minute

- Schema name: `Minute`
- Type: string
- Default: "*"

"00" - "59".

<a id="headingCHANGED_fields_lifetimes_items_schedule_hour"></a>
<a id="CHANGED_fields_lifetimes_items_schedule_hour"></a>
###### hour

- Schema name: `Hour`
- Type: string
- Default: "*"

"00" - "23".

<a id="headingCHANGED_fields_lifetimes_items_schedule_dom"></a>
<a id="CHANGED_fields_lifetimes_items_schedule_dom"></a>
###### dom

- Schema name: `Dom`
- Type: string
- Default: "*"

"1" - "31".

<a id="headingCHANGED_fields_lifetimes_items_schedule_month"></a>
<a id="CHANGED_fields_lifetimes_items_schedule_month"></a>
###### month

- Schema name: `Month`
- Type: string
- Default: "*"

"1" (January) - "12" (December).

<a id="headingCHANGED_fields_lifetimes_items_schedule_dow"></a>
<a id="CHANGED_fields_lifetimes_items_schedule_dow"></a>
###### dow

- Schema name: `Dow`
- Type: string
- Default: "*"

"1" (Monday) - "7" (Sunday).

<a id="headingCHANGED_fields_lifetimes_items_lifetime_value"></a>
<a id="CHANGED_fields_lifetimes_items_lifetime_value"></a>
###### lifetime_value (required)

- Schema name: `Lifetime Value`
- Type: integer

Number of time units to retain snapshots.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_lifetimes_items_lifetime_unit"></a>
<a id="CHANGED_fields_lifetimes_items_lifetime_unit"></a>
###### lifetime_unit (required)

- Schema name: `Lifetime Unit`
- Type: enum (of string)

Time unit for snapshot retention.
###### Must be one of:

- "HOUR"
- "DAY"
- "WEEK"
- "MONTH"
- "YEAR"

<a id="headingCHANGED_fields_compression"></a>
<a id="CHANGED_fields_compression"></a>
##### compression

- Schema name: `Compression`
- Default: null

Compresses SSH stream. Available only for SSH transport.
<a id="CHANGED_fields_compression_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_compression_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_compression_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "LZ4"
- "PIGZ"
- "PLZIP"

<a id="tab-pane_CHANGED_fields_compression_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_compression_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_speed_limit"></a>
<a id="CHANGED_fields_speed_limit"></a>
##### speed_limit

- Schema name: `Speed Limit`
- Default: null

Limits speed of SSH stream. Available only for SSH transport.
<a id="CHANGED_fields_speed_limit_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_speed_limit_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_speed_limit_anyOf_i0)

- Type: integer
- Value must be greater or equal to `1`

<a id="tab-pane_CHANGED_fields_speed_limit_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_speed_limit_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_large_block"></a>
<a id="CHANGED_fields_large_block"></a>
##### large_block

- Schema name: `Large Block`
- Type: boolean
- Default: true

Enable large block support for ZFS send streams.

<a id="headingCHANGED_fields_embed"></a>
<a id="CHANGED_fields_embed"></a>
##### embed

- Schema name: `Embed`
- Type: boolean
- Default: false

Enable embedded block support for ZFS send streams.

<a id="headingCHANGED_fields_compressed"></a>
<a id="CHANGED_fields_compressed"></a>
##### compressed

- Schema name: `Compressed`
- Type: boolean
- Default: true

Enable compressed ZFS send streams.

<a id="headingCHANGED_fields_retries"></a>
<a id="CHANGED_fields_retries"></a>
##### retries

- Schema name: `Retries`
- Type: integer
- Default: 5

Number of retries before considering replication failed.
- Value must be greater or equal to `1`

<a id="headingCHANGED_fields_logging_level"></a>
<a id="CHANGED_fields_logging_level"></a>
##### logging_level

- Schema name: `Logging Level`
- Default: null

Log level for replication task execution. Controls verbosity of replication logs.
<a id="CHANGED_fields_logging_level_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_logging_level_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_logging_level_anyOf_i0)

- Type: enum (of string)
###### Must be one of:

- "DEBUG"
- "INFO"
- "WARNING"
- "ERROR"

<a id="tab-pane_CHANGED_fields_logging_level_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_logging_level_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_enabled"></a>
<a id="CHANGED_fields_enabled"></a>
##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether this replication task is enabled.

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: object

Current state information for the replication task.

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

<a id="headingCHANGED_fields_has_encrypted_dataset_keys"></a>
<a id="CHANGED_fields_has_encrypted_dataset_keys"></a>
##### has_encrypted_dataset_keys (required)

- Schema name: `Has Encrypted Dataset Keys`
- Type: boolean

Whether this replication task has encrypted dataset keys available.

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `ReplicationRemovedEvent`
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
