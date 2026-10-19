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

The dataset ID (full path) to list processes for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of processes currently using the dataset.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### PoolProcess

- Schema name: `PoolProcess`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_pid"></a>
<a id="Return_value_items_pid"></a>
##### pid (required)

- Schema name: `Pid`
- Type: integer

Process ID of the process using the pool.

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the process using the pool.

<a id="headingReturn_value_items_service"></a>
<a id="Return_value_items_service"></a>
##### service (required)

- Schema name: `Service`

Name of the service if this process belongs to a system service.
<a id="Return_value_items_service_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_service_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_service_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_service_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_service_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_cmdline"></a>
<a id="Return_value_items_cmdline"></a>
##### cmdline (required)

- Schema name: `Cmdline`

Full command line of the process.
<a id="Return_value_items_cmdline_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_cmdline_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_cmdline_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_cmdline_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_cmdline_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
