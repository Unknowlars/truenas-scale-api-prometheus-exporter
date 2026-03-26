---
title: sharing.nfs.query
kind: event
source_rst: _sources/api_events_sharing.nfs.query.rst.txt
source_html: api_events_sharing.nfs.query.html
required_roles:
  - SHARING_NFS_READ
---

# sharing.nfs.query

## Summary

Sent on sharing.nfs changes.

## Required Roles

- `SHARING_NFS_READ`

## Schema

- Type: object

### ADDED

- Schema name: `NfsShareAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `NfsShareEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

##### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

##### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

##### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

##### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

##### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enterprise feature to enable access to the ZFS snapshot directory for the export. Export path must be the root directory of a ZFS dataset.

### CHANGED

- Schema name: `NfsShareChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

#### fields (required)

- Schema name: `NfsShareEntry`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the NFS share.

##### path (required)

- Schema name: `Path`
- Type: string

Local path to be exported.
- Must be at least `1` characters long

##### aliases

- Schema name: `Aliases`
- Type: array of string
- Default: []

IGNORED for now.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### comment

- Schema name: `Comment`
- Type: string
- Default: ""

User comment associated with share.

##### networks

- Schema name: `Networks`
- Type: array of string
- Default: []

List of authorized networks that are allowed to access the share having format "network/mask" CIDR notation. Each entry must be unique. If empty, all networks are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### hosts

- Schema name: `Hosts`
- Type: array of string
- Default: []

List of IP's/hostnames which are allowed to access the share. No quotes or spaces are allowed. Each entry must be unique. If empty, all IP's/hostnames are allowed. Excessively long lists should be avoided.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

##### ro

- Schema name: `Ro`
- Type: boolean
- Default: false

Export the share as read only.

##### maproot_user

- Schema name: `Maproot User`
- Default: null

Map root user client to a specified user.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### maproot_group

- Schema name: `Maproot Group`
- Default: null

Map root group client to a specified group.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### mapall_user

- Schema name: `Mapall User`
- Default: null

Map all client users to a specified user.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### mapall_group

- Schema name: `Mapall Group`
- Default: null

Map all client groups to a specified group.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### security

- Schema name: `Security`
- Type: array of enum (of string)
- Default: []

Specify the security schema.
- No Additional Items

###### Each item of this array must be:

- Type: enum (of string)

##### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Enable or disable the share.

##### locked (required)

- Schema name: `Locked`

Read-only value indicating whether the share is located on a locked dataset. Returns: - True: The share is in a locked dataset. - False: The share is not in a locked dataset. - None: Lock status is not available because path locking information was not requested.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### expose_snapshots

- Schema name: `Expose Snapshots`
- Type: boolean
- Default: false

Enterprise feature to enable access to the ZFS snapshot directory for the export. Export path must be the root directory of a ZFS dataset.

### REMOVED

- Schema name: `NfsShareRemovedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
