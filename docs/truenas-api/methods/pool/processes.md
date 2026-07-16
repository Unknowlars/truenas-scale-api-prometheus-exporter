---
title: pool.processes
kind: method
source_rst: _sources/api_methods_pool.processes.rst.txt
source_html: api_methods_pool.processes.html
required_roles:
  - POOL_READ
---

# pool.processes

## Summary

Returns a list of running processes using this pool.

## Required Roles

- `POOL_READ`

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

ID of the pool to get processes for.

### Return value

- Schema name: `Result`
- Type: array of object

Array of processes currently using the pool.
- No Additional Items

#### Each item of this array must be:

#### PoolProcess

- Schema name: `PoolProcess`
- Type: object
- No Additional Properties
##### pid (required)

- Schema name: `Pid`
- Type: integer

Process ID of the process using the pool.

##### name (required)

- Schema name: `Name`
- Type: string

Name of the process using the pool.

##### service (required)

- Schema name: `Service`

Name of the service if this process belongs to a system service.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### cmdline (required)

- Schema name: `Cmdline`

Full command line of the process.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
