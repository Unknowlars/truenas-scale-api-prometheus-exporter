---
title: pool.attachments
kind: method
source_rst: _sources/api_methods_pool.attachments.rst.txt
source_html: api_methods_pool.attachments.html
required_roles:
  - POOL_READ
---

# pool.attachments

## Summary

Return a list of services dependent of this pool.

Responsible for telling the user whether there is a related share, asking for confirmation.

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

ID of the pool to retrieve attachments for.

### Return value

- Schema name: `Result`
- Type: array of object

Array of services and resources using this pool.
- No Additional Items

#### Each item of this array must be:

#### PoolAttachment

- Schema name: `PoolAttachment`
- Type: object
- No Additional Properties
##### type (required)

- Schema name: `Type`
- Type: string

Type of attachment.

##### service (required)

- Schema name: `Service`

Name of the service using this pool. `null` if not a service attachment.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### attachments (required)

- Schema name: `Attachments`
- Type: array of string

Array of specific attachment identifiers or paths.
- No Additional Items

###### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
