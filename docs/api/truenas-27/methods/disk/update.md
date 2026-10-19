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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

Disk identifier to update.

#### Parameter 2: data

<a id="Call_parameters_items_i1"></a>
#### data

- Schema name: `data`
- Type: object

Updated disk configuration data.
- No Additional Properties
<a id="headingCall_parameters_items_i1_number"></a>
<a id="Call_parameters_items_i1_number"></a>
##### number

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

<a id="headingCall_parameters_items_i1_lunid"></a>
<a id="Call_parameters_items_i1_lunid"></a>
##### lunid

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
<a id="Call_parameters_items_i1_lunid_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_lunid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_lunid_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_lunid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_lunid_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_description"></a>
<a id="Call_parameters_items_i1_description"></a>
##### description

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

<a id="headingCall_parameters_items_i1_hddstandby"></a>
<a id="Call_parameters_items_i1_hddstandby"></a>
##### hddstandby

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

<a id="headingCall_parameters_items_i1_advpowermgmt"></a>
<a id="Call_parameters_items_i1_advpowermgmt"></a>
##### advpowermgmt

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

<a id="headingCall_parameters_items_i1_bus"></a>
<a id="Call_parameters_items_i1_bus"></a>
##### bus

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

<a id="headingCall_parameters_items_i1_enclosure"></a>
<a id="Call_parameters_items_i1_enclosure"></a>
##### enclosure

Physical enclosure information or `null` if not in an enclosure.
<a id="Call_parameters_items_i1_enclosure_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_enclosure_anyOf_i0"></a>
###### [DiskEntryEnclosure](#tab-pane_Call_parameters_items_i1_enclosure_anyOf_i0)

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
<a id="headingCall_parameters_items_i1_enclosure_anyOf_i0_number"></a>
<a id="Call_parameters_items_i1_enclosure_anyOf_i0_number"></a>
###### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

<a id="headingCall_parameters_items_i1_enclosure_anyOf_i0_slot"></a>
<a id="Call_parameters_items_i1_enclosure_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

<a id="tab-pane_Call_parameters_items_i1_enclosure_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_enclosure_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_pool"></a>
<a id="Call_parameters_items_i1_pool"></a>
##### pool

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
<a id="Call_parameters_items_i1_pool_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_pool_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_pool_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i1_passwd"></a>
<a id="Call_parameters_items_i1_passwd"></a>
##### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

<a id="headingCall_parameters_items_i1_sed_status"></a>
<a id="Call_parameters_items_i1_sed_status"></a>
##### sed_status

- Schema name: `Sed Status`

SED Status of the disk. `null` if not yet determined.
<a id="Call_parameters_items_i1_sed_status_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_sed_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_sed_status_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_sed_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_sed_status_anyOf_i1)

- Type: null

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `DiskEntry`
- Type: object

The updated disk configuration.
- No Additional Properties
<a id="headingReturn_value_identifier"></a>
<a id="Return_value_identifier"></a>
#### identifier (required)

- Schema name: `Identifier`
- Type: string

Unique identifier for the disk device.

<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

System name of the disk device.

<a id="headingReturn_value_subsystem"></a>
<a id="Return_value_subsystem"></a>
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

<a id="headingReturn_value_number"></a>
<a id="Return_value_number"></a>
#### number (required)

- Schema name: `Number`
- Type: integer

Numeric identifier assigned to the disk.

<a id="headingReturn_value_serial"></a>
<a id="Return_value_serial"></a>
#### serial (required)

- Schema name: `Serial`
- Type: string

Manufacturer serial number of the disk.

<a id="headingReturn_value_lunid"></a>
<a id="Return_value_lunid"></a>
#### lunid (required)

- Schema name: `Lunid`

Logical unit number identifier or `null` if not applicable.
<a id="Return_value_lunid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_lunid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_lunid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_lunid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_lunid_anyOf_i1)

- Type: null

<a id="headingReturn_value_size"></a>
<a id="Return_value_size"></a>
#### size (required)

- Schema name: `Size`

Total size of the disk in bytes. `null` if not available.
<a id="Return_value_size_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_size_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_size_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_size_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_size_anyOf_i1)

- Type: null

<a id="headingReturn_value_description"></a>
<a id="Return_value_description"></a>
#### description (required)

- Schema name: `Description`
- Type: string

Human-readable description of the disk device.

<a id="headingReturn_value_transfermode"></a>
<a id="Return_value_transfermode"></a>
#### transfermode (required)

- Schema name: `Transfermode`
- Type: string

Data transfer mode and capabilities of the disk.

<a id="headingReturn_value_hddstandby"></a>
<a id="Return_value_hddstandby"></a>
#### hddstandby (required)

- Schema name: `Hddstandby`
- Type: enum (of string)

Hard disk standby timer in minutes or `ALWAYS ON` to disable standby.
##### Must be one of:

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

<a id="headingReturn_value_advpowermgmt"></a>
<a id="Return_value_advpowermgmt"></a>
#### advpowermgmt (required)

- Schema name: `Advpowermgmt`
- Type: enum (of string)

Advanced power management level or `DISABLED` to turn off power management.
##### Must be one of:

- "DISABLED"
- "1"
- "64"
- "127"
- "128"
- "192"
- "254"

<a id="headingReturn_value_expiretime"></a>
<a id="Return_value_expiretime"></a>
#### expiretime (required)

- Schema name: `Expiretime`

Expiration timestamp for disk data or `null` if not applicable.
<a id="Return_value_expiretime_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_expiretime_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_expiretime_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_expiretime_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_expiretime_anyOf_i1)

- Type: null

<a id="headingReturn_value_model"></a>
<a id="Return_value_model"></a>
#### model (required)

- Schema name: `Model`

Manufacturer model name/number of the disk. `null` if not available.
<a id="Return_value_model_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_model_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_model_anyOf_i1)

- Type: null

<a id="headingReturn_value_rotationrate"></a>
<a id="Return_value_rotationrate"></a>
#### rotationrate (required)

- Schema name: `Rotationrate`

Disk rotation speed in RPM or `null` for SSDs and unknown devices.
<a id="Return_value_rotationrate_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_rotationrate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_rotationrate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_rotationrate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_rotationrate_anyOf_i1)

- Type: null

<a id="headingReturn_value_type"></a>
<a id="Return_value_type"></a>
#### type (required)

- Schema name: `Type`

Disk type classification or `null` if not determined.
<a id="Return_value_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_zfs_guid"></a>
<a id="Return_value_zfs_guid"></a>
#### zfs_guid (required)

- Schema name: `Zfs Guid`

ZFS globally unique identifier for this disk or `null` if not used in ZFS.
<a id="Return_value_zfs_guid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_zfs_guid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_zfs_guid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_zfs_guid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_zfs_guid_anyOf_i1)

- Type: null

<a id="headingReturn_value_bus"></a>
<a id="Return_value_bus"></a>
#### bus (required)

- Schema name: `Bus`
- Type: string

System bus type the disk is connected to.

<a id="headingReturn_value_devname"></a>
<a id="Return_value_devname"></a>
#### devname (required)

- Schema name: `Devname`
- Type: string

Device name in the operating system.
Examples:

```json
"/dev/sda"
```

<a id="headingReturn_value_enclosure"></a>
<a id="Return_value_enclosure"></a>
#### enclosure (required)

Physical enclosure information or `null` if not in an enclosure.
<a id="Return_value_enclosure_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_enclosure_anyOf_i0"></a>
###### [DiskEntryEnclosure](#tab-pane_Return_value_enclosure_anyOf_i0)

- Schema name: `DiskEntryEnclosure`
- Type: object
- No Additional Properties
<a id="headingReturn_value_enclosure_anyOf_i0_number"></a>
<a id="Return_value_enclosure_anyOf_i0_number"></a>
###### number (required)

- Schema name: `Number`
- Type: integer

Enclosure number where the disk is located.

<a id="headingReturn_value_enclosure_anyOf_i0_slot"></a>
<a id="Return_value_enclosure_anyOf_i0_slot"></a>
###### slot (required)

- Schema name: `Slot`
- Type: integer

Physical slot position within the enclosure.

<a id="tab-pane_Return_value_enclosure_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_enclosure_anyOf_i1)

- Type: null

<a id="headingReturn_value_pool"></a>
<a id="Return_value_pool"></a>
#### pool (required)

- Schema name: `Pool`

Name of the storage pool this disk belongs to. `null` if not part of any pool.
<a id="Return_value_pool_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pool_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pool_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_pool_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pool_anyOf_i1)

- Type: null

<a id="headingReturn_value_passwd"></a>
<a id="Return_value_passwd"></a>
#### passwd

- Schema name: `Passwd`
- Type: string

Disk encryption password (masked for security).

<a id="headingReturn_value_kmip_uid"></a>
<a id="Return_value_kmip_uid"></a>
#### kmip_uid

- Schema name: `Kmip Uid`

KMIP (Key Management Interoperability Protocol) unique identifier or `null`.
<a id="Return_value_kmip_uid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_kmip_uid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_kmip_uid_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_kmip_uid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_kmip_uid_anyOf_i1)

- Type: null

<a id="headingReturn_value_sed"></a>
<a id="Return_value_sed"></a>
#### sed (required)

- Schema name: `Sed`

Whether the disk is SED (Self-Encrypting Drive) capable. `null` if not yet determined.
<a id="Return_value_sed_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sed_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sed_anyOf_i0)

- Type: boolean

<a id="tab-pane_Return_value_sed_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sed_anyOf_i1)

- Type: null

<a id="headingReturn_value_sed_status"></a>
<a id="Return_value_sed_status"></a>
#### sed_status

- Schema name: `Sed Status`

SED Status of the disk. `null` if not yet determined.
<a id="Return_value_sed_status_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_sed_status_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_sed_status_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_sed_status_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_sed_status_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
