---
title: pool.dataset.processes
kind: method
source_rst: _sources/api_methods_pool.dataset.processes.rst.txt
source_html: api_methods_pool.dataset.processes.html
required_roles:
  - DATASET_READ
---

# pool.dataset.processes

## Summary

Return a list of processes using this dataset.

Example return value:

[ { "pid": 2520, "name": "smbd", "service": "cifs" }, { "pid": 97778, "name": "minio", "cmdline": "/usr/local/bin/minio -C /usr/local/etc/minio server --address=0.0.0.0:9000 --quiet /mnt/tank/wk" } ]

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

The dataset ID (full path) to list processes for.

### Return value

- Schema name: `Result`
- Type: array of object

Array of processes currently using the dataset.
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

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
