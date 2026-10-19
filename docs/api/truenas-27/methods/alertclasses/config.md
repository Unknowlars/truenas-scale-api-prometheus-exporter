---
title: alertclasses.config
kind: method
source_rst: _sources/api_methods_alertclasses.config.rst.txt
source_html: api_methods_alertclasses.config.html
required_roles:
  - ALERT_READ
---

# alertclasses.config

## Required Roles

- `ALERT_READ`

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

- Schema name: `AlertClassesEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the alert classes configuration.

<a id="headingReturn_value_classes"></a>
<a id="Return_value_classes"></a>
#### classes (required)

- Schema name: `Classes`
- Type: object

Object mapping alert class names to their configuration settings.
<a id="headingReturn_value_classes_additionalProperties"></a>
<a id="Return_value_classes_additionalProperties"></a>
##### Additional Properties

Each additional property must conform to the following schema
- Schema name: `AlertClassConfiguration`
- Type: object
- No Additional Properties
<a id="headingReturn_value_classes_additionalProperties_level"></a>
<a id="Return_value_classes_additionalProperties_level"></a>
###### level

- Schema name: `Level`
- Type: enum (of string)

Severity level for alerts of this class.
###### Must be one of:

- "INFO"
- "NOTICE"
- "WARNING"
- "ERROR"
- "CRITICAL"
- "ALERT"
- "EMERGENCY"

<a id="headingReturn_value_classes_additionalProperties_policy"></a>
<a id="Return_value_classes_additionalProperties_policy"></a>
###### policy

- Schema name: `Policy`
- Type: enum (of string)

Notification policy for alerts of this class. `IMMEDIATELY`: Send notifications as soon as alerts occur `HOURLY`: Batch notifications and send hourly `DAILY`: Batch notifications and send daily `NEVER`: Do not send notifications for this alert class
###### Must be one of:

- "IMMEDIATELY"
- "HOURLY"
- "DAILY"
- "NEVER"

<a id="headingReturn_value_classes_additionalProperties_proactive_support"></a>
<a id="Return_value_classes_additionalProperties_proactive_support"></a>
###### proactive_support

- Schema name: `Proactive Support`
- Type: boolean

Whether to include alerts of this class in proactive support reporting.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
