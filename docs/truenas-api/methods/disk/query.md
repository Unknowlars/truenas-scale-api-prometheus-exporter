---
title: disk.query
kind: method
source_rst: _sources/api_methods_disk.query.rst.txt
source_html: api_methods_disk.query.html
required_roles:
  - DISK_READ
---

# disk.query

## Summary

Query disks.

The following extra options are supported:

`include_expired` (bool): Also include expired disks (default: false). `passwords` (bool): Don't hide KMIP password for the disks (default: false). `pools` (bool): Join pool name for each disk (default: false).

## Required Roles

- `DISK_READ`

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

###### DiskQueryResultItem

- Schema name: `DiskQueryResultItem`
- Type: object
- No Additional Properties
####### identifier

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

####### name

- Schema name: `Name`
- Type: string

System name of the disk device.

####### subsystem

- Schema name: `Subsystem`
- Type: string

Storage subsystem type.
Examples:

```json
"SCSI"
```
Examples:

```json
"ATA"
```

####### number

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

####### serial

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

####### lunid

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### size

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### description

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

####### transfermode

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

####### hddstandby

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.

####### advpowermgmt

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.

####### expiretime

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
######## Any of

######### Option 1

- Type: string
- Type: Format: date-time

######### Option 2

- Type: null

####### model

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### rotationrate

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

####### type

- Schema name: `Type`

Disk type classification or `null` if not determined.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### zfs_guid

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### bus

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

####### devname

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

####### enclosure

Physical enclosure information or `null` if not in an enclosure.
######## Any of

######### DiskEntryEnclosure

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
########## number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

########## slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

######### Option 2

- Type: null

####### pool

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

####### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

##### DiskQueryResultItem

- Type: string

##### Option 3

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: string
- Type: Format: date-time

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
###### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

###### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

##### Option 2

- Type: null

##### DiskEntryEnclosure

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `DiskQueryResultItem`
- Type: object
- No Additional Properties
###### identifier

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

###### name

- Schema name: `Name`
- Type: string

System name of the disk device.

###### subsystem

- Schema name: `Subsystem`
- Type: string

Storage subsystem type.
Examples:

```json
"SCSI"
```
Examples:

```json
"ATA"
```

###### number

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

###### serial

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

###### lunid

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### size

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### description

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

###### transfermode

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

###### hddstandby

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.

###### advpowermgmt

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.

###### expiretime

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### model

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### rotationrate

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### type

- Schema name: `Type`

Disk type classification or `null` if not determined.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### zfs_guid

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### bus

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

###### devname

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

###### enclosure

Physical enclosure information or `null` if not in an enclosure.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### pool

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

###### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
