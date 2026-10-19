---
title: pool.dataset.attachments
kind: method
source_rst: _sources/api_methods_pool.dataset.attachments.rst.txt
source_html: api_methods_pool.dataset.attachments.html
required_roles:
  - DATASET_READ
---

# pool.dataset.attachments

## Summary

Return a list of services dependent of this dataset.

Responsible for telling the user whether there is a related share, asking for confirmation.

Example return value: [ { "type": "NFS Share", "service": "nfs", "attachments": ["/mnt/tank/work"] } ]

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

The dataset ID (full path) to retrieve attachments for.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of services and resources attached to the dataset.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### PoolAttachment

- Schema name: `PoolAttachment`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_type"></a>
<a id="Return_value_items_type"></a>
##### type (required)

- Schema name: `Type`
- Type: string

Type of attachment.

<a id="headingReturn_value_items_service"></a>
<a id="Return_value_items_service"></a>
##### service (required)

- Schema name: `Service`

Name of the service using this pool. `null` if not a service attachment.
<a id="Return_value_items_service_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_service_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_service_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_service_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_service_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_attachments"></a>
<a id="Return_value_items_attachments"></a>
##### attachments (required)

- Schema name: `Attachments`
- Type: array of string

Array of specific attachment identifiers or paths.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_attachments_items"></a>
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
