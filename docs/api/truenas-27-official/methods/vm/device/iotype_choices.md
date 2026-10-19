---
title: vm.device.iotype_choices
kind: method
source_rst: _sources/api_methods_vm.device.iotype_choices.rst.txt
source_html: api_methods_vm.device.iotype_choices.html
required_roles:
  - READONLY_ADMIN
  - VM_DEVICE_READ
---

# vm.device.iotype_choices

## Summary

IO-type choices for storage devices.

## Required Roles

- `READONLY_ADMIN`
- `VM_DEVICE_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMDeviceIotypeChoicesResult`
- Type: object

VMDeviceIotypeChoicesResult return fields.
- No Additional Properties
<a id="headingReturn_value_NATIVE"></a>
<a id="Return_value_NATIVE"></a>
#### NATIVE

- Schema name: `Native`
- Type: string
- Default: "NATIVE"

Native asynchronous I/O for best performance with NVMe.

<a id="headingReturn_value_THREADS"></a>
<a id="Return_value_THREADS"></a>
#### THREADS

- Schema name: `Threads`
- Type: string
- Default: "THREADS"

Thread-based I/O suitable for most storage types.

<a id="headingReturn_value_IO_URING"></a>
<a id="Return_value_IO_URING"></a>
#### IO_URING

- Schema name: `Io Uring`
- Type: string
- Default: "IO_URING"

Linux io_uring interface for high-performance async I/O.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
