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
#### state

- Schema name: `State`
- Type: string
- Default: "127.0.0.1"

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
- Type: string

Hypervisor-specific domain state.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
