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

##### sed

- Schema name: `Sed`

Whether the disk is SED (Self-Encrypting Drive) capable. `null` if not yet determined.
###### Any of

####### Option 1

- Type: boolean

####### Option 2

- Type: null

##### sed_status

- Schema name: `Sed Status`

SED Status of the disk. `null` if not yet determined.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Type: object

The updated disk configuration.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
