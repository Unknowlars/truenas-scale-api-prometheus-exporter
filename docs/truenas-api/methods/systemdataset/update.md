---
title: systemdataset.update
kind: method
source_rst: _sources/api_methods_systemdataset.update.rst.txt
source_html: api_methods_systemdataset.update.html
required_roles:
  - DATASET_WRITE
---

# systemdataset.update

## Summary

Update System Dataset Service Configuration.

This method is a job.

## Required Roles

- `DATASET_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

Updated configuration for the system dataset.
- No Additional Properties
##### pool

- Schema name: `Pool`

The name of a valid pool configured in the system to host the system dataset.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### pool_exclude

- Schema name: `Pool Exclude`

The name of a pool to not place the system dataset on if `pool` is not provided.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

### Return value

- Schema name: `SystemDatasetEntry`
- Type: object

The updated system dataset configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the system dataset configuration.

#### pool (required)

- Schema name: `Pool`
- Type: string

Name of the pool hosting the system dataset.

#### pool_set (required)

- Schema name: `Pool Set`
- Type: boolean

Whether a pool has been explicitly set for the system dataset.

#### uuid (required)

- Schema name: `Uuid`
- Type: string

UUID of the system dataset.

#### basename (required)

- Schema name: `Basename`
- Type: string

Base name of the system dataset.

#### path (required)

- Schema name: `Path`

Filesystem path to the system dataset. `null` if not mounted.
##### Any of

###### Option 1

- Type: string

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
