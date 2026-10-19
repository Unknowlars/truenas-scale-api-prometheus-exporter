---
title: audit.query
kind: method
source_rst: _sources/api_methods_audit.query.rst.txt
source_html: api_methods_audit.query.html
required_roles:
  - SYSTEM_AUDIT_READ
---

# audit.query

## Summary

Query contents of audit databases specified by `services`.

## Required Roles

- `SYSTEM_AUDIT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

<a id="Call_parameters_items_i0"></a>
#### data

- Schema name: `data`
- Type: object
- Default:
```json
{
  "services": [
    "MIDDLEWARE"
  ],
  "query-filters": [],
  "query-options": {
    "count": false,
    "extra": {},
    "force_sql_filters": false,
    "get": false,
    "limit": 0,
    "offset": 0,
    "order_by": [],
    "select": []
  },
  "remote_controller": false
}
```

Audit query configuration specifying services, filters, and options.
- No Additional Properties
<a id="headingCall_parameters_items_i0_services"></a>
<a id="Call_parameters_items_i0_services"></a>
##### services

- Schema name: `Services`
- Type: array of enum (of string)
- Default: ["MIDDLEWARE"]

Array of services to include in the audit query.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_services_items"></a>
- Type: enum (of string)
###### Must be one of:

- "MIDDLEWARE"
- "S3"
- "SMB"
- "SUDO"
- "SYSTEM"

<a id="headingCall_parameters_items_i0_query-filters"></a>
<a id="Call_parameters_items_i0_query-filters"></a>
##### query-filters

- Schema name: `Query-Filters`
- Type: array
- Default: []

Array of filters to apply to the audit query results.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-filters_items"></a>
- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

<a id="headingCall_parameters_items_i0_query-options"></a>
<a id="Call_parameters_items_i0_query-options"></a>
##### query-options

- Schema name: `QueryOptions`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

If the query-option `force_sql_filters` is true, then the query will be converted into a more efficient form for better performance. This will not be possible if filters use keys within `svc_data` and `event_data`.
- No Additional Properties
<a id="headingCall_parameters_items_i0_query-options_extra"></a>
<a id="Call_parameters_items_i0_query-options_extra"></a>
###### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i0_query-options_order_by"></a>
<a id="Call_parameters_items_i0_query-options_order_by"></a>
###### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i0_query-options_select"></a>
<a id="Call_parameters_items_i0_query-options_select"></a>
###### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_select_items"></a>
<a id="Call_parameters_items_i0_query-options_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_query-options_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_query-options_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i0_query-options_count"></a>
<a id="Call_parameters_items_i0_query-options_count"></a>
###### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i0_query-options_get"></a>
<a id="Call_parameters_items_i0_query-options_get"></a>
###### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i0_query-options_offset"></a>
<a id="Call_parameters_items_i0_query-options_offset"></a>
###### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i0_query-options_limit"></a>
<a id="Call_parameters_items_i0_query-options_limit"></a>
###### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i0_query-options_force_sql_filters"></a>
<a id="Call_parameters_items_i0_query-options_force_sql_filters"></a>
###### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingCall_parameters_items_i0_remote_controller"></a>
<a id="Call_parameters_items_i0_remote_controller"></a>
##### remote_controller

- Schema name: `Remote Controller`
- Type: boolean
- Default: false

HA systems may direct the query to the 'remote' controller by including 'remote_controller=True'. The default is the 'current' controller.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### AuditQueryResultItemQueryResultItem

- Schema name: `AuditQueryResultItemQueryResultItem`
- Type: object
<a id="headingReturn_value_anyOf_i0_items_audit_id"></a>
<a id="Return_value_anyOf_i0_items_audit_id"></a>
###### audit_id

- Schema name: `Audit Id`

GUID uniquely identifying this specific audit event.
<a id="Return_value_anyOf_i0_items_audit_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_audit_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_audit_id_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_audit_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_audit_id_anyOf_i1)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_audit_id_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i0_items_audit_id_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_message_timestamp"></a>
<a id="Return_value_anyOf_i0_items_message_timestamp"></a>
###### message_timestamp

- Schema name: `Message Timestamp`
- Type: integer

Unix timestamp for when the audit event was written to the auditing database.

<a id="headingReturn_value_anyOf_i0_items_timestamp"></a>
<a id="Return_value_anyOf_i0_items_timestamp"></a>
###### timestamp

- Schema name: `Timestamp`
- Type: string
- Type: Format: date-time

Converted ISO-8601 timestamp from application recording when event occurred.

<a id="headingReturn_value_anyOf_i0_items_address"></a>
<a id="Return_value_anyOf_i0_items_address"></a>
###### address

- Schema name: `Address`
- Type: string

IP address of client performing action that generated the audit message.

<a id="headingReturn_value_anyOf_i0_items_username"></a>
<a id="Return_value_anyOf_i0_items_username"></a>
###### username

- Schema name: `Username`
- Type: string

Username used by client performing action.

<a id="headingReturn_value_anyOf_i0_items_session"></a>
<a id="Return_value_anyOf_i0_items_session"></a>
###### session

- Schema name: `Session`

GUID uniquely identifying the client session.
<a id="Return_value_anyOf_i0_items_session_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_session_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_session_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_session_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_session_anyOf_i1)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_session_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i0_items_session_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_service"></a>
<a id="Return_value_anyOf_i0_items_service"></a>
###### service

- Schema name: `Service`
- Type: enum (of string)

Name of the service that generated the message. This will be one of the names specified in `services`.
###### Must be one of:

- "MIDDLEWARE"
- "S3"
- "SMB"
- "SUDO"
- "SYSTEM"

<a id="headingReturn_value_anyOf_i0_items_service_data"></a>
<a id="Return_value_anyOf_i0_items_service_data"></a>
###### service_data

- Schema name: `Service Data`

JSON object containing variable data depending on the particular service. See TrueNAS auditing documentation for the service in question.
<a id="Return_value_anyOf_i0_items_service_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_service_data_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_service_data_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_service_data_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_service_data_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_event"></a>
<a id="Return_value_anyOf_i0_items_event"></a>
###### event

- Schema name: `Event`
- Type: string

Name of the event type that generated the audit record. Each service has its own unique event identifiers.

<a id="headingReturn_value_anyOf_i0_items_event_data"></a>
<a id="Return_value_anyOf_i0_items_event_data"></a>
###### event_data

- Schema name: `Event Data`

JSON object containing variable data depending on the particular event type. See TrueNAS auditing documentation for the service in question.
<a id="Return_value_anyOf_i0_items_event_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_event_data_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_event_data_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i0_items_event_data_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_event_data_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_success"></a>
<a id="Return_value_anyOf_i0_items_success"></a>
###### success

- Schema name: `Success`
- Type: boolean

The action generating the event message succeeded.

<a id="headingReturn_value_anyOf_i0_items_additionalProperties"></a>
<a id="Return_value_anyOf_i0_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [AuditQueryResultItemQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `AuditQueryResultItemQueryResultItem`
- Type: object
<a id="headingReturn_value_anyOf_i1_audit_id"></a>
<a id="Return_value_anyOf_i1_audit_id"></a>
###### audit_id

- Schema name: `Audit Id`

GUID uniquely identifying this specific audit event.
<a id="Return_value_anyOf_i1_audit_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_audit_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_audit_id_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_audit_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_audit_id_anyOf_i1)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_audit_id_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_audit_id_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i1_message_timestamp"></a>
<a id="Return_value_anyOf_i1_message_timestamp"></a>
###### message_timestamp

- Schema name: `Message Timestamp`
- Type: integer

Unix timestamp for when the audit event was written to the auditing database.

<a id="headingReturn_value_anyOf_i1_timestamp"></a>
<a id="Return_value_anyOf_i1_timestamp"></a>
###### timestamp

- Schema name: `Timestamp`
- Type: string
- Type: Format: date-time

Converted ISO-8601 timestamp from application recording when event occurred.

<a id="headingReturn_value_anyOf_i1_address"></a>
<a id="Return_value_anyOf_i1_address"></a>
###### address

- Schema name: `Address`
- Type: string

IP address of client performing action that generated the audit message.

<a id="headingReturn_value_anyOf_i1_username"></a>
<a id="Return_value_anyOf_i1_username"></a>
###### username

- Schema name: `Username`
- Type: string

Username used by client performing action.

<a id="headingReturn_value_anyOf_i1_session"></a>
<a id="Return_value_anyOf_i1_session"></a>
###### session

- Schema name: `Session`

GUID uniquely identifying the client session.
<a id="Return_value_anyOf_i1_session_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_session_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_session_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_session_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_session_anyOf_i1)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_session_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_session_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i1_service"></a>
<a id="Return_value_anyOf_i1_service"></a>
###### service

- Schema name: `Service`
- Type: enum (of string)

Name of the service that generated the message. This will be one of the names specified in `services`.
###### Must be one of:

- "MIDDLEWARE"
- "S3"
- "SMB"
- "SUDO"
- "SYSTEM"

<a id="headingReturn_value_anyOf_i1_service_data"></a>
<a id="Return_value_anyOf_i1_service_data"></a>
###### service_data

- Schema name: `Service Data`

JSON object containing variable data depending on the particular service. See TrueNAS auditing documentation for the service in question.
<a id="Return_value_anyOf_i1_service_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_service_data_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_service_data_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_service_data_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_service_data_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_event"></a>
<a id="Return_value_anyOf_i1_event"></a>
###### event

- Schema name: `Event`
- Type: string

Name of the event type that generated the audit record. Each service has its own unique event identifiers.

<a id="headingReturn_value_anyOf_i1_event_data"></a>
<a id="Return_value_anyOf_i1_event_data"></a>
###### event_data

- Schema name: `Event Data`

JSON object containing variable data depending on the particular event type. See TrueNAS auditing documentation for the service in question.
<a id="Return_value_anyOf_i1_event_data_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_event_data_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_event_data_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_event_data_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_event_data_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_success"></a>
<a id="Return_value_anyOf_i1_success"></a>
###### success

- Schema name: `Success`
- Type: boolean

The action generating the event message succeeded.

<a id="headingReturn_value_anyOf_i1_additionalProperties"></a>
<a id="Return_value_anyOf_i1_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
