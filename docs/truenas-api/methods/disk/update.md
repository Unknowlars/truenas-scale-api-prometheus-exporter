---
title: disk.update
kind: method
source_rst: _sources/api_methods_disk.update.rst.txt
source_html: api_methods_disk.update.html
required_roles:
  - DISK_WRITE
---

# disk.update

## Summary

Update disk of `id`.

## Required Roles

- `DISK_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

Disk identifier to update.

#### Parameter 2: data

#### data

- Schema name: `data`
- Type: object

Updated disk configuration data.
- No Additional Properties
##### number

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

##### lunid

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### description

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

##### hddstandby

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.

##### advpowermgmt

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.

##### bus

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

##### enclosure

Physical enclosure information or `null` if not in an enclosure.
###### Any of

####### DiskEntryEnclosure

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
######## number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

######## slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

####### Option 2

- Type: null

##### pool

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

### Return value

- Schema name: `DiskEntry`
- Type: object

The updated disk configuration.
- No Additional Properties
#### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

#### name (required)

- Schema name: `Name`
- Type: string

System name of the disk device.

#### subsystem (required)

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

#### number (required)

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

#### serial (required)

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

#### lunid (required)

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### size (required)

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

#### transfermode (required)

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

#### hddstandby (required)

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.

#### advpowermgmt (required)

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.

#### expiretime (required)

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
##### Any of

###### Option 1

- Type: string
- Type: Format: date-time

###### Option 2

- Type: null

#### model (required)

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### rotationrate (required)

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### type (required)

- Schema name: `Type`

Disk type classification or `null` if not determined.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### zfs_guid (required)

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### bus (required)

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

#### devname (required)

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

#### enclosure (required)

Physical enclosure information or `null` if not in an enclosure.
##### Any of

###### DiskEntryEnclosure

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
####### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

####### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

###### Option 2

- Type: null

#### pool (required)

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

#### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

#### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
