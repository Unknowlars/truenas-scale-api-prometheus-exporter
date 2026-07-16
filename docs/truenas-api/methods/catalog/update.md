---
title: catalog.update
kind: method
source_rst: _sources/api_methods_catalog.update.rst.txt
source_html: api_methods_catalog.update.html
required_roles:
  - CATALOG_WRITE
---

# catalog.update

## Summary

Update catalog preferences.

## Required Roles

- `CATALOG_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: catalog_update

#### catalog_update

- Schema name: `catalog_update`
- Type: object

CatalogUpdateArgs parameters.
- No Additional Properties
##### preferred_trains

- Schema name: `Preferred Trains`
- Type: array of string

Updated array of preferred train names for the catalog.
- No Additional Items

###### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

### Return value

- Schema name: `CatalogEntry`
- Type: object

The updated catalog configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the catalog.
- Must be at least `1` characters long

#### label

- Schema name: `Label`
- Type: string
- Default: "nobody"

Catalog identifier. Must start with alphanumeric, then allow alphanumeric, periods, and hyphens.
- Must be at least `1` characters long

#### preferred_trains (required)

- Schema name: `Preferred Trains`
- Type: array of string

Array of preferred train names for this catalog.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### location (required)

- Schema name: `Location`
- Type: string

Git repository URL or local path to the catalog.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
