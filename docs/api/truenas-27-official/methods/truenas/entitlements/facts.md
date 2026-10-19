---
title: truenas.entitlements.facts
kind: method
source_rst: _sources/api_methods_truenas.entitlements.facts.rst.txt
source_html: api_methods_truenas.entitlements.facts.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# truenas.entitlements.facts

## Summary

Return the hardware and license facts every entitlement decision is computed from.

## Required Roles

- `SYSTEM_PRODUCT_READ`

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

- Schema name: `EntitlementFactsEntry`
- Type: object

Hardware and license facts for this system.
- No Additional Properties
<a id="headingReturn_value_hardware_type"></a>
<a id="Return_value_hardware_type"></a>
#### hardware_type (required)

- Schema name: `Hardware Type`
- Type: enum (of string)

Hardware this system runs on. `TRUENAS` for TrueNAS appliance hardware, `COMMUNITY` otherwise.
##### Must be one of:

- "TRUENAS"
- "COMMUNITY"

<a id="headingReturn_value_license_type"></a>
<a id="Return_value_license_type"></a>
#### license_type (required)

- Schema name: `License Type`

Type of the installed license, e.g. `COMMUNITY`, `ENTERPRISE` or `COMMERCIAL`. `null` when no license issued by TrueNAS is installed.
<a id="Return_value_license_type_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_license_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_license_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_license_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_license_type_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
