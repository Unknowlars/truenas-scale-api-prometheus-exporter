---
title: tunable.tunable_type_choices
kind: method
source_rst: _sources/api_methods_tunable.tunable_type_choices.rst.txt
source_html: api_methods_tunable.tunable_type_choices.html
required_roles:
  - READONLY_ADMIN
  - SYSTEM_TUNABLE_READ
---

# tunable.tunable_type_choices

## Summary

Retrieve the supported tunable types that can be changed.

## Required Roles

- `READONLY_ADMIN`
- `SYSTEM_TUNABLE_READ`

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

- Schema name: `TunableTunableTypeChoices`
- Type: object

Available tunable types with their identifiers.
- No Additional Properties
<a id="headingReturn_value_SYSCTL"></a>
<a id="Return_value_SYSCTL"></a>
#### SYSCTL (required)

- Schema name: `Sysctl`
- Type: const

System control parameters that affect kernel behavior.
- Specific value: `"SYSCTL"`

<a id="headingReturn_value_UDEV"></a>
<a id="Return_value_UDEV"></a>
#### UDEV (required)

- Schema name: `Udev`
- Type: const

Device management rules for hardware detection and configuration.
- Specific value: `"UDEV"`

<a id="headingReturn_value_ZFS"></a>
<a id="Return_value_ZFS"></a>
#### ZFS (required)

- Schema name: `Zfs`
- Type: const

ZFS filesystem kernel module parameters.
- Specific value: `"ZFS"`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
