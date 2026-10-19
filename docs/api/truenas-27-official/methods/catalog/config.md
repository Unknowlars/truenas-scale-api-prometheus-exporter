---
title: catalog.config
kind: method
source_rst: _sources/api_methods_catalog.config.rst.txt
source_html: api_methods_catalog.config.html
required_roles:
  - CATALOG_READ
---

# catalog.config

## Required Roles

- `CATALOG_READ`

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

- Schema name: `CatalogEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the catalog.
- Must be at least `1` characters long

<a id="headingReturn_value_label"></a>
<a id="Return_value_label"></a>
#### label (required)

- Schema name: `Label`
- Type: string

Catalog identifier. Must start with alphanumeric, then allow alphanumeric, periods, and hyphens.
- Must match regular expression: `^\w+[\w.-]*$`
- Must be at least `1` characters long

<a id="headingReturn_value_preferred_trains"></a>
<a id="Return_value_preferred_trains"></a>
#### preferred_trains (required)

- Schema name: `Preferred Trains`
- Type: array of string

Array of preferred train names for this catalog.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_preferred_trains_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_location"></a>
<a id="Return_value_location"></a>
#### location (required)

- Schema name: `Location`
- Type: string

Git repository URL or local path to the catalog.
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
