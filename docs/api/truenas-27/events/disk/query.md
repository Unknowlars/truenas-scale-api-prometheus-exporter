---
title: disk.query
kind: event
source_rst: _sources/api_events_disk.query.rst.txt
source_html: api_events_disk.query.html
required_roles:
  - READONLY_ADMIN
---

# disk.query

## Summary

Sent on disk changes.

## Required Roles

- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `DiskQueryAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Disk identifier.

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `DiskEntry`
- Type: object

Event fields.
- No Additional Properties
<a id="headingADDED_fields_identifier"></a>
<a id="ADDED_fields_identifier"></a>
##### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

System name of the disk device.

<a id="headingADDED_fields_subsystem"></a>
<a id="ADDED_fields_subsystem"></a>
##### subsystem (required)

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

<a id="headingADDED_fields_number"></a>
<a id="ADDED_fields_number"></a>
##### number (required)

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

<a id="headingADDED_fields_serial"></a>
<a id="ADDED_fields_serial"></a>
##### serial (required)

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

<a id="headingADDED_fields_lunid"></a>
<a id="ADDED_fields_lunid"></a>
##### lunid (required)

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
<a id="ADDED_fields_lunid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_lunid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_lunid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_lunid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_lunid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_size"></a>
<a id="ADDED_fields_size"></a>
##### size (required)

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
<a id="ADDED_fields_size_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_size_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_size_anyOf_i1)

- Type: null

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

<a id="headingADDED_fields_transfermode"></a>
<a id="ADDED_fields_transfermode"></a>
##### transfermode (required)

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

<a id="headingADDED_fields_hddstandby"></a>
<a id="ADDED_fields_hddstandby"></a>
##### hddstandby (required)

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.
###### Must be one of:

- "ALWAYS ON"
- "5"
- "10"
- "20"
- "30"
- "60"
- "120"
- "180"
- "240"
- "300"
- "330"

<a id="headingADDED_fields_advpowermgmt"></a>
<a id="ADDED_fields_advpowermgmt"></a>
##### advpowermgmt (required)

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.
###### Must be one of:

- "DISABLED"
- "1"
- "64"
- "127"
- "128"
- "192"
- "254"

<a id="headingADDED_fields_expiretime"></a>
<a id="ADDED_fields_expiretime"></a>
##### expiretime (required)

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
<a id="ADDED_fields_expiretime_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_expiretime_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_expiretime_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_expiretime_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_expiretime_anyOf_i1)

- Type: null

<a id="headingADDED_fields_model"></a>
<a id="ADDED_fields_model"></a>
##### model (required)

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
<a id="ADDED_fields_model_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_model_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_model_anyOf_i1)

- Type: null

<a id="headingADDED_fields_rotationrate"></a>
<a id="ADDED_fields_rotationrate"></a>
##### rotationrate (required)

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
<a id="ADDED_fields_rotationrate_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_rotationrate_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_rotationrate_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_rotationrate_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_rotationrate_anyOf_i1)

- Type: null

<a id="headingADDED_fields_type"></a>
<a id="ADDED_fields_type"></a>
##### type (required)

- Schema name: `Type`

Disk type classification or `null` if not determined.
<a id="ADDED_fields_type_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_type_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_type_anyOf_i1)

- Type: null

<a id="headingADDED_fields_zfs_guid"></a>
<a id="ADDED_fields_zfs_guid"></a>
##### zfs_guid (required)

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
<a id="ADDED_fields_zfs_guid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_zfs_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_zfs_guid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_zfs_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_zfs_guid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_bus"></a>
<a id="ADDED_fields_bus"></a>
##### bus (required)

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

<a id="headingADDED_fields_devname"></a>
<a id="ADDED_fields_devname"></a>
##### devname (required)

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

<a id="headingADDED_fields_enclosure"></a>
<a id="ADDED_fields_enclosure"></a>
##### enclosure (required)

Physical enclosure information or `null` if not in an enclosure.
<a id="ADDED_fields_enclosure_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_enclosure_anyOf_i0"></a>
###### [DiskEntryEnclosure](#tab-pane_ADDED_fields_enclosure_anyOf_i0)

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_enclosure_anyOf_i0_number"></a>
<a id="ADDED_fields_enclosure_anyOf_i0_number"></a>
###### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

<a id="headingADDED_fields_enclosure_anyOf_i0_slot"></a>
<a id="ADDED_fields_enclosure_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

<a id="tab-pane_ADDED_fields_enclosure_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_enclosure_anyOf_i1)

- Type: null

<a id="headingADDED_fields_pool"></a>
<a id="ADDED_fields_pool"></a>
##### pool (required)

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
<a id="ADDED_fields_pool_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_pool_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_pool_anyOf_i1)

- Type: null

<a id="headingADDED_fields_passwd"></a>
<a id="ADDED_fields_passwd"></a>
##### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

<a id="headingADDED_fields_kmip_uid"></a>
<a id="ADDED_fields_kmip_uid"></a>
##### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
<a id="ADDED_fields_kmip_uid_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_kmip_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_kmip_uid_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_kmip_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_kmip_uid_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sed"></a>
<a id="ADDED_fields_sed"></a>
##### sed (required)

- Schema name: `Sed`

Whether the disk is SED (Self-Encrypting Drive) capable. `null` if not yet determined.
<a id="ADDED_fields_sed_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_ADDED_fields_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sed_anyOf_i1)

- Type: null

<a id="headingADDED_fields_sed_status"></a>
<a id="ADDED_fields_sed_status"></a>
##### sed_status

- Schema name: `Sed Status`

SED Status of the disk. `null` if not yet determined.
<a id="ADDED_fields_sed_status_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_sed_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_sed_status_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_sed_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_sed_status_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `DiskQueryChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Disk identifier.

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `DiskEntry`
- Type: object

Event fields.
- No Additional Properties
<a id="headingCHANGED_fields_identifier"></a>
<a id="CHANGED_fields_identifier"></a>
##### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

System name of the disk device.

<a id="headingCHANGED_fields_subsystem"></a>
<a id="CHANGED_fields_subsystem"></a>
##### subsystem (required)

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

<a id="headingCHANGED_fields_number"></a>
<a id="CHANGED_fields_number"></a>
##### number (required)

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

<a id="headingCHANGED_fields_serial"></a>
<a id="CHANGED_fields_serial"></a>
##### serial (required)

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

<a id="headingCHANGED_fields_lunid"></a>
<a id="CHANGED_fields_lunid"></a>
##### lunid (required)

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
<a id="CHANGED_fields_lunid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_lunid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_lunid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_lunid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_lunid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_size"></a>
<a id="CHANGED_fields_size"></a>
##### size (required)

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
<a id="CHANGED_fields_size_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_size_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_size_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

<a id="headingCHANGED_fields_transfermode"></a>
<a id="CHANGED_fields_transfermode"></a>
##### transfermode (required)

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

<a id="headingCHANGED_fields_hddstandby"></a>
<a id="CHANGED_fields_hddstandby"></a>
##### hddstandby (required)

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.
###### Must be one of:

- "ALWAYS ON"
- "5"
- "10"
- "20"
- "30"
- "60"
- "120"
- "180"
- "240"
- "300"
- "330"

<a id="headingCHANGED_fields_advpowermgmt"></a>
<a id="CHANGED_fields_advpowermgmt"></a>
##### advpowermgmt (required)

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.
###### Must be one of:

- "DISABLED"
- "1"
- "64"
- "127"
- "128"
- "192"
- "254"

<a id="headingCHANGED_fields_expiretime"></a>
<a id="CHANGED_fields_expiretime"></a>
##### expiretime (required)

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
<a id="CHANGED_fields_expiretime_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_expiretime_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_expiretime_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_expiretime_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_expiretime_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_model"></a>
<a id="CHANGED_fields_model"></a>
##### model (required)

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
<a id="CHANGED_fields_model_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_model_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_model_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_rotationrate"></a>
<a id="CHANGED_fields_rotationrate"></a>
##### rotationrate (required)

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
<a id="CHANGED_fields_rotationrate_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_rotationrate_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_rotationrate_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_rotationrate_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_rotationrate_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_type"></a>
<a id="CHANGED_fields_type"></a>
##### type (required)

- Schema name: `Type`

Disk type classification or `null` if not determined.
<a id="CHANGED_fields_type_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_type_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_type_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_zfs_guid"></a>
<a id="CHANGED_fields_zfs_guid"></a>
##### zfs_guid (required)

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
<a id="CHANGED_fields_zfs_guid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_zfs_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_zfs_guid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_zfs_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_zfs_guid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_bus"></a>
<a id="CHANGED_fields_bus"></a>
##### bus (required)

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

<a id="headingCHANGED_fields_devname"></a>
<a id="CHANGED_fields_devname"></a>
##### devname (required)

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

<a id="headingCHANGED_fields_enclosure"></a>
<a id="CHANGED_fields_enclosure"></a>
##### enclosure (required)

Physical enclosure information or `null` if not in an enclosure.
<a id="CHANGED_fields_enclosure_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_enclosure_anyOf_i0"></a>
###### [DiskEntryEnclosure](#tab-pane_CHANGED_fields_enclosure_anyOf_i0)

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_enclosure_anyOf_i0_number"></a>
<a id="CHANGED_fields_enclosure_anyOf_i0_number"></a>
###### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

<a id="headingCHANGED_fields_enclosure_anyOf_i0_slot"></a>
<a id="CHANGED_fields_enclosure_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

<a id="tab-pane_CHANGED_fields_enclosure_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_enclosure_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_pool"></a>
<a id="CHANGED_fields_pool"></a>
##### pool (required)

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
<a id="CHANGED_fields_pool_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_pool_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_pool_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_passwd"></a>
<a id="CHANGED_fields_passwd"></a>
##### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

<a id="headingCHANGED_fields_kmip_uid"></a>
<a id="CHANGED_fields_kmip_uid"></a>
##### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
<a id="CHANGED_fields_kmip_uid_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_kmip_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_kmip_uid_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_kmip_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_kmip_uid_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sed"></a>
<a id="CHANGED_fields_sed"></a>
##### sed (required)

- Schema name: `Sed`

Whether the disk is SED (Self-Encrypting Drive) capable. `null` if not yet determined.
<a id="CHANGED_fields_sed_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_CHANGED_fields_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sed_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_sed_status"></a>
<a id="CHANGED_fields_sed_status"></a>
##### sed_status

- Schema name: `Sed Status`

SED Status of the disk. `null` if not yet determined.
<a id="CHANGED_fields_sed_status_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_sed_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_sed_status_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_sed_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_sed_status_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `DiskQueryRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Disk identifier.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
