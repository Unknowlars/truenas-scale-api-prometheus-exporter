---
title: truenas.license.info
kind: method
source_rst: _sources/api_methods_truenas.license.info.rst.txt
source_html: api_methods_truenas.license.info.html
required_roles:
  - READONLY_ADMIN
---

# truenas.license.info

## Summary

Returns the parsed license object, or null if no license exists.

## Required Roles

- `READONLY_ADMIN`

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

Parsed license, or `null` if no license is installed.
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [LicenseInfoEntry](#tab-pane_Return_value_anyOf_i0)

- Schema name: `LicenseInfoEntry`
- Type: object

An installed license, normalized identically whichever format produced it.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_id"></a>
<a id="Return_value_anyOf_i0_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

Identifier of the installed license.

<a id="headingReturn_value_anyOf_i0_type"></a>
<a id="Return_value_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

License type: one of `ENTERPRISE`, `COMMERCIAL`, `COMMUNITY` or `UNKNOWN`. New values may be added; treat an unrecognized value as `UNKNOWN`.

<a id="headingReturn_value_anyOf_i0_model"></a>
<a id="Return_value_anyOf_i0_model"></a>
###### model (required)

- Schema name: `Model`

Hardware model the license was issued for, or `null` if unspecified.
<a id="Return_value_anyOf_i0_model_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_model_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_model_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_model_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_model_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_features"></a>
<a id="Return_value_anyOf_i0_features"></a>
###### features (required)

- Schema name: `Features`
- Type: array of object

Every feature this license grants.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_features_items"></a>
###### LicenseFeatureEntry

- Schema name: `LicenseFeatureEntry`
- Type: object

A single feature an installed license grants.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_features_items_name"></a>
<a id="Return_value_anyOf_i0_features_items_name"></a>
###### name (required)

- Schema name: `Name`
- Type: string

Feature identifier, for example `SUPPORT` or `VMS`.

<a id="headingReturn_value_anyOf_i0_features_items_start_date"></a>
<a id="Return_value_anyOf_i0_features_items_start_date"></a>
###### start_date (required)

- Schema name: `Start Date`

Date the feature became active, or `null` when the license records no start date.
<a id="Return_value_anyOf_i0_features_items_start_date_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_features_items_start_date_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_features_items_start_date_anyOf_i0)

- Type: string
- Type: Format: date

<a id="tab-pane_Return_value_anyOf_i0_features_items_start_date_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_features_items_start_date_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_features_items_expires_at"></a>
<a id="Return_value_anyOf_i0_features_items_expires_at"></a>
###### expires_at (required)

- Schema name: `Expires At`

Date the feature expires, or `null` when it is perpetual.
<a id="Return_value_anyOf_i0_features_items_expires_at_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_features_items_expires_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_features_items_expires_at_anyOf_i0)

- Type: string
- Type: Format: date

<a id="tab-pane_Return_value_anyOf_i0_features_items_expires_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_features_items_expires_at_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_features_items_type"></a>
<a id="Return_value_anyOf_i0_features_items_type"></a>
###### type (required)

- Schema name: `Type`

Tier qualifier the feature carries, for example `GOLD`. `null` when it carries none.
<a id="Return_value_anyOf_i0_features_items_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_features_items_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_features_items_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_features_items_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_features_items_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_serials"></a>
<a id="Return_value_anyOf_i0_serials"></a>
###### serials (required)

- Schema name: `Serials`
- Type: array of string

System serial numbers the license covers.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_serials_items"></a>
- Type: string

<a id="headingReturn_value_anyOf_i0_enclosures"></a>
<a id="Return_value_anyOf_i0_enclosures"></a>
###### enclosures (required)

- Schema name: `Enclosures`
- Type: object

Count of licensed expansion shelves, keyed by enclosure model.
<a id="headingReturn_value_anyOf_i0_enclosures_additionalProperties"></a>
<a id="Return_value_anyOf_i0_enclosures_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: integer

<a id="headingReturn_value_anyOf_i0_contract_type"></a>
<a id="Return_value_anyOf_i0_contract_type"></a>
###### contract_type (required)

- Schema name: `Contract Type`

Support contract tier, or `null` when the license carries no support entitlement.
<a id="Return_value_anyOf_i0_contract_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_contract_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_contract_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_contract_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_contract_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_issued_at"></a>
<a id="Return_value_anyOf_i0_issued_at"></a>
###### issued_at (required)

- Schema name: `Issued At`

When the license was issued, exactly as recorded in the license: an RFC 3339 UTC timestamp, or for a legacy-format license the `YYYY-MM-DD` start date of its support contract. `null` when not recorded.
<a id="Return_value_anyOf_i0_issued_at_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_issued_at_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_issued_at_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_issued_at_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_issued_at_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [Option 2](#tab-pane_Return_value_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
