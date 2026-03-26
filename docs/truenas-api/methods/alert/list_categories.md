---
title: alert.list_categories
kind: method
source_rst: _sources/api_methods_alert.list_categories.rst.txt
source_html: api_methods_alert.list_categories.html
required_roles:
  - ALERT_LIST_READ
---

# alert.list_categories

## Summary

List all types of alerts which the system can issue.

## Required Roles

- `ALERT_LIST_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `Result`
- Type: array of object

Array of available alert categories and their classes.
- No Additional Items

#### Each item of this array must be:

#### AlertCategory

- Schema name: `AlertCategory`
- Type: object
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the alert category.

##### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the alert category.

##### classes (required)

- Schema name: `Classes`
- Type: array of object

Array of alert classes within this category.
- No Additional Items

###### Each item of this array must be:

###### AlertCategoryClass

- Schema name: `AlertCategoryClass`
- Type: object
- No Additional Properties
####### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the alert class.

####### title (required)

- Schema name: `Title`
- Type: string

Human-readable title for the alert class.

####### level (required)

- Schema name: `Level`
- Type: string

Default severity level for alerts in this class.

####### proactive_support (required)

- Schema name: `Proactive Support`
- Type: boolean

Whether this alert class is included in proactive support monitoring.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
