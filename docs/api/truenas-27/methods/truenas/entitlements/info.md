---
title: truenas.entitlements.info
kind: method
source_rst: _sources/api_methods_truenas.entitlements.info.rst.txt
source_html: api_methods_truenas.entitlements.info.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# truenas.entitlements.info

## Summary

Return the entitlement decision for every gated feature.

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

- Schema name: `EntitlementsInfo`
- Type: object

Entitlement decisions for all license-gated features on this system.
- No Additional Properties
<a id="headingReturn_value_features"></a>
<a id="Return_value_features"></a>
#### features (required)

- Schema name: `Features`
- Type: object

Entitlement decision for every license-gated feature known to this system, keyed by feature identifier. Identifiers are added over time: ignore keys you do not recognize, and treat an absent key as not gated.
<a id="headingReturn_value_features_additionalProperties"></a>
<a id="Return_value_features_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `EntitlementEntry`
- Type: object

Decision for a single license-gated feature.
- No Additional Properties
<a id="headingReturn_value_features_additionalProperties_entitled"></a>
<a id="Return_value_features_additionalProperties_entitled"></a>
###### entitled (required)

- Schema name: `Entitled`
- Type: boolean

Whether this system is entitled to use the feature.

<a id="headingReturn_value_features_additionalProperties_reason"></a>
<a id="Return_value_features_additionalProperties_reason"></a>
###### reason (required)

- Schema name: `Reason`
- Type: enum (of string)

Machine-readable classification of the decision: `ENTITLED`: the feature is available `NO_LICENSE`: no license is installed and the feature requires one `KEY_MISSING`: a license is installed but does not carry this feature `WRONG_HARDWARE`: this hardware can never provide the feature `TIER_INSUFFICIENT`: the support tier does not cover the feature `WRONG_LICENSE_TYPE`: the license type does not cover the feature `NOT_GATED`: nothing on this system restricts the feature New values may be added; treat an unrecognized value as a generic denial.
###### Must be one of:

- "ENTITLED"
- "NO_LICENSE"
- "KEY_MISSING"
- "WRONG_HARDWARE"
- "TIER_INSUFFICIENT"
- "WRONG_LICENSE_TYPE"
- "NOT_GATED"

<a id="headingReturn_value_features_additionalProperties_message"></a>
<a id="Return_value_features_additionalProperties_message"></a>
###### message (required)

- Schema name: `Message`
- Type: string

Human-readable explanation of the decision. Empty when entitled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
