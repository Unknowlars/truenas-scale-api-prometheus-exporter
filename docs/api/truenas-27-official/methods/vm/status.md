---
title: vm.status
kind: method
source_rst: _sources/api_methods_vm.status.rst.txt
source_html: api_methods_vm.status.html
required_roles:
  - VM_READ
---

# vm.status

## Summary

Get the status of `id` VM.

Returns a dict: - state, RUNNING / STOPPED / SUSPENDED - pid, process id if RUNNING

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

ID of the virtual machine to get status for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `VMStatus`
- Type: object

Current status and runtime information for the virtual machine.
- No Additional Properties
<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `State`
- Type: string

Current state of the virtual machine.
- Must be at least `1` characters long
Examples:

```json
"RUNNING"
```
Examples:

```json
"STOPPED"
```
Examples:

```json
"SUSPENDED"
```

<a id="headingReturn_value_pid"></a>
<a id="Return_value_pid"></a>
#### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
<a id="Return_value_pid_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_pid_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_pid_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_pid_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_pid_anyOf_i1)

- Type: null

<a id="headingReturn_value_domain_state"></a>
<a id="Return_value_domain_state"></a>
#### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
<a id="Return_value_domain_state_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_domain_state_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_domain_state_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_domain_state_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_domain_state_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
