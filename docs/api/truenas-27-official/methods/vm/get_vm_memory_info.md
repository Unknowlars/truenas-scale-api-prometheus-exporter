---
title: vm.get_vm_memory_info
kind: method
source_rst: _sources/api_methods_vm.get_vm_memory_info.rst.txt
source_html: api_methods_vm.get_vm_memory_info.html
required_roles:
  - VM_READ
---

# vm.get_vm_memory_info

## Summary

Returns memory information for `vm_id` VM if it is going to be started.

All memory attributes are expressed in bytes.

## Required Roles

- `VM_READ`

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
- Type: integer

ID of the virtual machine to get memory information for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMGetVmMemoryInfoResult`
- Type: object

VMGetVmMemoryInfoResult return fields.
- No Additional Properties
<a id="headingReturn_value_minimum_memory_requested"></a>
<a id="Return_value_minimum_memory_requested"></a>
#### minimum_memory_requested (required)

- Schema name: `Minimum Memory Requested`

Minimum memory requested by the VM
<a id="Return_value_minimum_memory_requested_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_minimum_memory_requested_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_minimum_memory_requested_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_minimum_memory_requested_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_minimum_memory_requested_anyOf_i1)

- Type: null

<a id="headingReturn_value_total_memory_requested"></a>
<a id="Return_value_total_memory_requested"></a>
#### total_memory_requested (required)

- Schema name: `Total Memory Requested`
- Type: integer

Maximum / total memory requested by the VM

<a id="headingReturn_value_overcommit_required"></a>
<a id="Return_value_overcommit_required"></a>
#### overcommit_required (required)

- Schema name: `Overcommit Required`
- Type: boolean

Overcommit of memory is required to start VM

<a id="headingReturn_value_memory_req_fulfilled_after_overcommit"></a>
<a id="Return_value_memory_req_fulfilled_after_overcommit"></a>
#### memory_req_fulfilled_after_overcommit (required)

- Schema name: `Memory Req Fulfilled After Overcommit`
- Type: boolean

Memory requirements of VM are fulfilled if over-committing memory is specified

<a id="headingReturn_value_arc_to_shrink"></a>
<a id="Return_value_arc_to_shrink"></a>
#### arc_to_shrink (required)

- Schema name: `Arc To Shrink`

Size of ARC to shrink in bytes
<a id="Return_value_arc_to_shrink_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_arc_to_shrink_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_arc_to_shrink_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_arc_to_shrink_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_arc_to_shrink_anyOf_i1)

- Type: null

<a id="headingReturn_value_current_arc_max"></a>
<a id="Return_value_current_arc_max"></a>
#### current_arc_max (required)

- Schema name: `Current Arc Max`
- Type: integer

Current size of max ARC in bytes

<a id="headingReturn_value_arc_min"></a>
<a id="Return_value_arc_min"></a>
#### arc_min (required)

- Schema name: `Arc Min`
- Type: integer

Minimum size of ARC in bytes

<a id="headingReturn_value_arc_max_after_shrink"></a>
<a id="Return_value_arc_max_after_shrink"></a>
#### arc_max_after_shrink (required)

- Schema name: `Arc Max After Shrink`
- Type: integer

Size of max ARC in bytes after shrinking

<a id="headingReturn_value_actual_vm_requested_memory"></a>
<a id="Return_value_actual_vm_requested_memory"></a>
#### actual_vm_requested_memory (required)

- Schema name: `Actual Vm Requested Memory`
- Type: integer

VM memory in bytes to consider when making calculations for available/required memory. If VM ballooning is specified for the VM, the minimum VM memory specified by user will be taken into account otherwise total VM memory requested will be taken into account.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
