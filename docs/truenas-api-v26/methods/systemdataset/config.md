---
title: systemdataset.config
kind: method
source_rst: _sources/api_methods_systemdataset.config.rst.txt
source_html: api_methods_systemdataset.config.html
required_roles:
  - DATASET_READ
---

# systemdataset.config

## Required Roles

- `DATASET_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `SystemDatasetEntry`
- Type: object
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
