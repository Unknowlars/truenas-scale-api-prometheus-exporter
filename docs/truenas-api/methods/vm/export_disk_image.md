---
title: vm.export_disk_image
kind: method
source_rst: _sources/api_methods_vm.export_disk_image.rst.txt
source_html: api_methods_vm.export_disk_image.html
required_roles:
  - VM_WRITE
---

# vm.export_disk_image

## Summary

Exports a zvol to a formatted VM disk image.

Utilized qemu-img with the conversion functionality to export a zvol to any supported disk image format, from RAW -> ${OTHER}. The resulting file will be set to inherit the permissions of the target directory.

As of this implementation it supports the following {format} options :

- QCOW2 - QED - RAW - VDI - VPC - VMDK

`format` is an required parameter for the exported disk image `directory` is an required parameter for the export disk image `zvol` is the source for the disk image

This method is a job.

## Required Roles

- `VM_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: vm_export_disk_image

#### vm_export_disk_image

- Schema name: `vm_export_disk_image`
- Type: object

VMExportDiskImageArgs parameters.
- No Additional Properties
##### format (required)

- Schema name: `Format`
- Type: string

Output format for the exported disk image (e.g., 'qcow2', 'raw').
- Must be at least `1` characters long

##### directory (required)

- Schema name: `Directory`
- Type: string

Directory path where the exported disk image will be saved.
- Must be at least `1` characters long

##### zvol (required)

- Schema name: `Zvol`
- Type: string

Source ZFS volume to export as a disk image.
- Must be at least `1` characters long

### Return value

- Schema name: `Result`
- Type: boolean

Whether the disk image export operation was successful.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
