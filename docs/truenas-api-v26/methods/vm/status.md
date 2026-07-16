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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

ID of the virtual machine to get status for.

### Return value

- Schema name: `VMStatus`
- Type: object

Current status and runtime information for the virtual machine.
- No Additional Properties
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

#### pid (required)

- Schema name: `Pid`

Process ID of the running VM. `null` if not running.
##### Any of

###### Option 1

- Type: integer

###### Option 2

- Type: null

#### domain_state (required)

- Schema name: `Domain State`

Hypervisor-specific domain state.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
