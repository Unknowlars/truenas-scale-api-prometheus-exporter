---
title: vm.import_disk_image
kind: method
source_rst: _sources/api_methods_vm.import_disk_image.rst.txt
source_html: api_methods_vm.import_disk_image.html
required_roles:
  - VM_WRITE
---

# vm.import_disk_image

## Summary

Imports a specified disk image.

Utilized qemu-img with the auto-detect functionality to auto-convert any supported disk image format to RAW -> ZVOL

As of this implementation it supports:

- QCOW2 - QED - RAW - VDI - VPC - VMDK

`diskimg` is an required parameter for the incoming disk image `zvol` is the required target for the imported disk image

This method is a job.

## Required Roles

- `VM_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_import_disk_image

#### vm_import_disk_image

- Schema name: `vm_import_disk_image`
- Type: object

VMImportDiskImageArgs parameters.
- No Additional Properties
##### diskimg (required)

- Schema name: `Diskimg`
- Type: string

Path to the disk image file to import.
- Must be at least `1` characters long

##### zvol (required)

- Schema name: `Zvol`
- Type: string

Target ZFS volume path where the disk image will be imported.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: boolean

Whether the disk image import operation was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
