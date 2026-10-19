---
title: truenas.entitlements.check
kind: method
source_rst: _sources/api_methods_truenas.entitlements.check.rst.txt
source_html: api_methods_truenas.entitlements.check.html
required_roles:
  - SYSTEM_PRODUCT_READ
---

# truenas.entitlements.check

## Summary

Return the entitlement for `feature` computed from current system facts.

`POLICY` is keyed by StrEnum members, so a plain feature name looks up the same rule.

## Required Roles

- `SYSTEM_PRODUCT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: feature

<a id="Call_parameters_items_i0"></a>
#### feature

- Schema name: `feature`
- Type: string

Feature identifier to evaluate. A feature this system does not gate is reported as `NOT_GATED`, the same as its absence from the `truenas.entitlements.info` map.
- Must be at least `1` characters long

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `EntitlementEntry`
- Type: object

Entitlement decision for the requested feature.
- No Additional Properties
<a id="headingReturn_value_entitled"></a>
<a id="Return_value_entitled"></a>
#### entitled (required)

- Schema name: `Entitled`
- Type: boolean

Whether this system is entitled to use the feature.

<a id="headingReturn_value_reason"></a>
<a id="Return_value_reason"></a>
#### reason (required)

- Schema name: `Reason`
- Type: enum (of string)

Machine-readable classification of the decision: `ENTITLED`: the feature is available `NO_LICENSE`: no license is installed and the feature requires one `KEY_MISSING`: a license is installed but does not carry this feature `WRONG_HARDWARE`: this hardware can never provide the feature `TIER_INSUFFICIENT`: the support tier does not cover the feature `WRONG_LICENSE_TYPE`: the license type does not cover the feature `NOT_GATED`: nothing on this system restricts the feature New values may be added; treat an unrecognized value as a generic denial.
##### Must be one of:

- "ENTITLED"
- "NO_LICENSE"
- "KEY_MISSING"
- "WRONG_HARDWARE"
- "TIER_INSUFFICIENT"
- "WRONG_LICENSE_TYPE"
- "NOT_GATED"

<a id="headingReturn_value_message"></a>
<a id="Return_value_message"></a>
#### message (required)

- Schema name: `Message`
- Type: string

Human-readable explanation of the decision. Empty when entitled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
