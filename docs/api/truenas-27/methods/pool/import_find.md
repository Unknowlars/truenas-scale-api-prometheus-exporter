---
title: pool.import_find
kind: method
source_rst: _sources/api_methods_pool.import_find.rst.txt
source_html: api_methods_pool.import_find.html
required_roles:
  - POOL_READ
---

# pool.import_find

## Summary

Returns a job id which can be used to retrieve a list of pools available for import with the following details as a result of the job: name, guid, status, hostname.

This method is a job.

## Required Roles

- `POOL_READ`

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

- Schema name: `Result`
- Type: array of object

Pools available for import.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### PoolImportFind

- Schema name: `PoolImportFind`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

Name of the pool available for import.

<a id="headingReturn_value_items_guid"></a>
<a id="Return_value_items_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: string

GUID of the pool available for import.

<a id="headingReturn_value_items_status"></a>
<a id="Return_value_items_status"></a>
##### status (required)

- Schema name: `Status`
- Type: string

Current status of the importable pool.

<a id="headingReturn_value_items_hostname"></a>
<a id="Return_value_items_hostname"></a>
##### hostname (required)

- Schema name: `Hostname`
- Type: string

Hostname where the pool was last mounted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
