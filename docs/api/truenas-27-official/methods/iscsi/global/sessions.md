---
title: iscsi.global.sessions
kind: method
source_rst: _sources/api_methods_iscsi.global.sessions.rst.txt
source_html: api_methods_iscsi.global.sessions.html
required_roles:
  - SHARING_ISCSI_GLOBAL_READ
---

# iscsi.global.sessions

## Summary

Get a list of currently running iSCSI sessions. This includes initiator and target names and the unique connection IDs.

## Required Roles

- `SHARING_ISCSI_GLOBAL_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
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

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

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
###### ISCSIGlobalSessionsItem

- Schema name: `ISCSIGlobalSessionsItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_initiator"></a>
<a id="Return_value_anyOf_i0_items_initiator"></a>
###### initiator (required)

- Schema name: `Initiator`
- Type: string

iSCSI Qualified Name (IQN) of the initiator.

<a id="headingReturn_value_anyOf_i0_items_initiator_addr"></a>
<a id="Return_value_anyOf_i0_items_initiator_addr"></a>
###### initiator_addr (required)

- Schema name: `Initiator Addr`
- Type: string

IP address of the initiator.

<a id="headingReturn_value_anyOf_i0_items_initiator_alias"></a>
<a id="Return_value_anyOf_i0_items_initiator_alias"></a>
###### initiator_alias (required)

- Schema name: `Initiator Alias`

Alias name of the initiator or `null` if not set.
<a id="Return_value_anyOf_i0_items_initiator_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_initiator_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_initiator_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_initiator_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_initiator_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_target"></a>
<a id="Return_value_anyOf_i0_items_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

iSCSI Qualified Name (IQN) of the target.

<a id="headingReturn_value_anyOf_i0_items_target_alias"></a>
<a id="Return_value_anyOf_i0_items_target_alias"></a>
###### target_alias (required)

- Schema name: `Target Alias`
- Type: string

Alias name of the target.

<a id="headingReturn_value_anyOf_i0_items_header_digest"></a>
<a id="Return_value_anyOf_i0_items_header_digest"></a>
###### header_digest (required)

- Schema name: `Header Digest`

Header digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i0_items_header_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_header_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_header_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_header_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_header_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_data_digest"></a>
<a id="Return_value_anyOf_i0_items_data_digest"></a>
###### data_digest (required)

- Schema name: `Data Digest`

Data digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i0_items_data_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_data_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_data_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_data_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_data_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_max_data_segment_length"></a>
<a id="Return_value_anyOf_i0_items_max_data_segment_length"></a>
###### max_data_segment_length (required)

- Schema name: `Max Data Segment Length`

Maximum data segment length for the session or `null`.
<a id="Return_value_anyOf_i0_items_max_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_max_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_max_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_max_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_max_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_max_receive_data_segment_length"></a>
<a id="Return_value_anyOf_i0_items_max_receive_data_segment_length"></a>
###### max_receive_data_segment_length (required)

- Schema name: `Max Receive Data Segment Length`

Maximum receive data segment length or `null`.
<a id="Return_value_anyOf_i0_items_max_receive_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_max_receive_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_max_receive_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_max_receive_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_max_receive_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_max_xmit_data_segment_length"></a>
<a id="Return_value_anyOf_i0_items_max_xmit_data_segment_length"></a>
###### max_xmit_data_segment_length (required)

- Schema name: `Max Xmit Data Segment Length`

Maximum transmit data segment length or `null`.
<a id="Return_value_anyOf_i0_items_max_xmit_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_max_xmit_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_max_xmit_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_max_xmit_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_max_xmit_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_max_burst_length"></a>
<a id="Return_value_anyOf_i0_items_max_burst_length"></a>
###### max_burst_length (required)

- Schema name: `Max Burst Length`

Maximum burst length for the session or `null`.
<a id="Return_value_anyOf_i0_items_max_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_max_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_max_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_max_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_max_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_first_burst_length"></a>
<a id="Return_value_anyOf_i0_items_first_burst_length"></a>
###### first_burst_length (required)

- Schema name: `First Burst Length`

First burst length for the session or `null`.
<a id="Return_value_anyOf_i0_items_first_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_first_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_first_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_first_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_first_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_immediate_data"></a>
<a id="Return_value_anyOf_i0_items_immediate_data"></a>
###### immediate_data (required)

- Schema name: `Immediate Data`
- Type: boolean

Whether immediate data transfer is enabled.

<a id="headingReturn_value_anyOf_i0_items_iser"></a>
<a id="Return_value_anyOf_i0_items_iser"></a>
###### iser (required)

- Schema name: `Iser`
- Type: boolean

Whether this session is using iSER (iSCSI Extensions for RDMA).

<a id="headingReturn_value_anyOf_i0_items_offload"></a>
<a id="Return_value_anyOf_i0_items_offload"></a>
###### offload (required)

- Schema name: `Offload`
- Type: boolean

Whether hardware offload is enabled for this session.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [ISCSIGlobalSessionsItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `ISCSIGlobalSessionsItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_initiator"></a>
<a id="Return_value_anyOf_i1_initiator"></a>
###### initiator (required)

- Schema name: `Initiator`
- Type: string

iSCSI Qualified Name (IQN) of the initiator.

<a id="headingReturn_value_anyOf_i1_initiator_addr"></a>
<a id="Return_value_anyOf_i1_initiator_addr"></a>
###### initiator_addr (required)

- Schema name: `Initiator Addr`
- Type: string

IP address of the initiator.

<a id="headingReturn_value_anyOf_i1_initiator_alias"></a>
<a id="Return_value_anyOf_i1_initiator_alias"></a>
###### initiator_alias (required)

- Schema name: `Initiator Alias`

Alias name of the initiator or `null` if not set.
<a id="Return_value_anyOf_i1_initiator_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_initiator_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_initiator_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_initiator_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_initiator_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_target"></a>
<a id="Return_value_anyOf_i1_target"></a>
###### target (required)

- Schema name: `Target`
- Type: string

iSCSI Qualified Name (IQN) of the target.

<a id="headingReturn_value_anyOf_i1_target_alias"></a>
<a id="Return_value_anyOf_i1_target_alias"></a>
###### target_alias (required)

- Schema name: `Target Alias`
- Type: string

Alias name of the target.

<a id="headingReturn_value_anyOf_i1_header_digest"></a>
<a id="Return_value_anyOf_i1_header_digest"></a>
###### header_digest (required)

- Schema name: `Header Digest`

Header digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i1_header_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_header_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_header_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_header_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_header_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_data_digest"></a>
<a id="Return_value_anyOf_i1_data_digest"></a>
###### data_digest (required)

- Schema name: `Data Digest`

Data digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i1_data_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_data_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_data_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_data_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_data_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_max_data_segment_length"></a>
<a id="Return_value_anyOf_i1_max_data_segment_length"></a>
###### max_data_segment_length (required)

- Schema name: `Max Data Segment Length`

Maximum data segment length for the session or `null`.
<a id="Return_value_anyOf_i1_max_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_max_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_max_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_max_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_max_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_max_receive_data_segment_length"></a>
<a id="Return_value_anyOf_i1_max_receive_data_segment_length"></a>
###### max_receive_data_segment_length (required)

- Schema name: `Max Receive Data Segment Length`

Maximum receive data segment length or `null`.
<a id="Return_value_anyOf_i1_max_receive_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_max_receive_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_max_receive_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_max_receive_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_max_receive_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_max_xmit_data_segment_length"></a>
<a id="Return_value_anyOf_i1_max_xmit_data_segment_length"></a>
###### max_xmit_data_segment_length (required)

- Schema name: `Max Xmit Data Segment Length`

Maximum transmit data segment length or `null`.
<a id="Return_value_anyOf_i1_max_xmit_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_max_xmit_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_max_xmit_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_max_xmit_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_max_xmit_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_max_burst_length"></a>
<a id="Return_value_anyOf_i1_max_burst_length"></a>
###### max_burst_length (required)

- Schema name: `Max Burst Length`

Maximum burst length for the session or `null`.
<a id="Return_value_anyOf_i1_max_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_max_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_max_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_max_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_max_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_first_burst_length"></a>
<a id="Return_value_anyOf_i1_first_burst_length"></a>
###### first_burst_length (required)

- Schema name: `First Burst Length`

First burst length for the session or `null`.
<a id="Return_value_anyOf_i1_first_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_first_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_first_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_first_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_first_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_immediate_data"></a>
<a id="Return_value_anyOf_i1_immediate_data"></a>
###### immediate_data (required)

- Schema name: `Immediate Data`
- Type: boolean

Whether immediate data transfer is enabled.

<a id="headingReturn_value_anyOf_i1_iser"></a>
<a id="Return_value_anyOf_i1_iser"></a>
###### iser (required)

- Schema name: `Iser`
- Type: boolean

Whether this session is using iSER (iSCSI Extensions for RDMA).

<a id="headingReturn_value_anyOf_i1_offload"></a>
<a id="Return_value_anyOf_i1_offload"></a>
###### offload (required)

- Schema name: `Offload`
- Type: boolean

Whether hardware offload is enabled for this session.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### ISCSIGlobalSessionsItemQueryResultItem

- Schema name: `ISCSIGlobalSessionsItemQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_initiator"></a>
<a id="Return_value_anyOf_i2_items_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Type: string

iSCSI Qualified Name (IQN) of the initiator.

<a id="headingReturn_value_anyOf_i2_items_initiator_addr"></a>
<a id="Return_value_anyOf_i2_items_initiator_addr"></a>
###### initiator_addr

- Schema name: `Initiator Addr`
- Type: string

IP address of the initiator.

<a id="headingReturn_value_anyOf_i2_items_initiator_alias"></a>
<a id="Return_value_anyOf_i2_items_initiator_alias"></a>
###### initiator_alias

- Schema name: `Initiator Alias`

Alias name of the initiator or `null` if not set.
<a id="Return_value_anyOf_i2_items_initiator_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_initiator_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_initiator_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_initiator_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_initiator_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_target"></a>
<a id="Return_value_anyOf_i2_items_target"></a>
###### target

- Schema name: `Target`
- Type: string

iSCSI Qualified Name (IQN) of the target.

<a id="headingReturn_value_anyOf_i2_items_target_alias"></a>
<a id="Return_value_anyOf_i2_items_target_alias"></a>
###### target_alias

- Schema name: `Target Alias`
- Type: string

Alias name of the target.

<a id="headingReturn_value_anyOf_i2_items_header_digest"></a>
<a id="Return_value_anyOf_i2_items_header_digest"></a>
###### header_digest

- Schema name: `Header Digest`

Header digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i2_items_header_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_header_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_header_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_header_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_header_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_data_digest"></a>
<a id="Return_value_anyOf_i2_items_data_digest"></a>
###### data_digest

- Schema name: `Data Digest`

Data digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i2_items_data_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_data_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_data_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_data_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_data_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_max_data_segment_length"></a>
<a id="Return_value_anyOf_i2_items_max_data_segment_length"></a>
###### max_data_segment_length

- Schema name: `Max Data Segment Length`

Maximum data segment length for the session or `null`.
<a id="Return_value_anyOf_i2_items_max_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_max_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_max_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_max_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_max_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_max_receive_data_segment_length"></a>
<a id="Return_value_anyOf_i2_items_max_receive_data_segment_length"></a>
###### max_receive_data_segment_length

- Schema name: `Max Receive Data Segment Length`

Maximum receive data segment length or `null`.
<a id="Return_value_anyOf_i2_items_max_receive_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_max_receive_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_max_receive_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_max_receive_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_max_receive_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_max_xmit_data_segment_length"></a>
<a id="Return_value_anyOf_i2_items_max_xmit_data_segment_length"></a>
###### max_xmit_data_segment_length

- Schema name: `Max Xmit Data Segment Length`

Maximum transmit data segment length or `null`.
<a id="Return_value_anyOf_i2_items_max_xmit_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_max_xmit_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_max_xmit_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_max_xmit_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_max_xmit_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_max_burst_length"></a>
<a id="Return_value_anyOf_i2_items_max_burst_length"></a>
###### max_burst_length

- Schema name: `Max Burst Length`

Maximum burst length for the session or `null`.
<a id="Return_value_anyOf_i2_items_max_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_max_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_max_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_max_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_max_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_first_burst_length"></a>
<a id="Return_value_anyOf_i2_items_first_burst_length"></a>
###### first_burst_length

- Schema name: `First Burst Length`

First burst length for the session or `null`.
<a id="Return_value_anyOf_i2_items_first_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_first_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_first_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_first_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_first_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_immediate_data"></a>
<a id="Return_value_anyOf_i2_items_immediate_data"></a>
###### immediate_data

- Schema name: `Immediate Data`
- Type: boolean

Whether immediate data transfer is enabled.

<a id="headingReturn_value_anyOf_i2_items_iser"></a>
<a id="Return_value_anyOf_i2_items_iser"></a>
###### iser

- Schema name: `Iser`
- Type: boolean

Whether this session is using iSER (iSCSI Extensions for RDMA).

<a id="headingReturn_value_anyOf_i2_items_offload"></a>
<a id="Return_value_anyOf_i2_items_offload"></a>
###### offload

- Schema name: `Offload`
- Type: boolean

Whether hardware offload is enabled for this session.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [ISCSIGlobalSessionsItemQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `ISCSIGlobalSessionsItemQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_initiator"></a>
<a id="Return_value_anyOf_i3_initiator"></a>
###### initiator

- Schema name: `Initiator`
- Type: string

iSCSI Qualified Name (IQN) of the initiator.

<a id="headingReturn_value_anyOf_i3_initiator_addr"></a>
<a id="Return_value_anyOf_i3_initiator_addr"></a>
###### initiator_addr

- Schema name: `Initiator Addr`
- Type: string

IP address of the initiator.

<a id="headingReturn_value_anyOf_i3_initiator_alias"></a>
<a id="Return_value_anyOf_i3_initiator_alias"></a>
###### initiator_alias

- Schema name: `Initiator Alias`

Alias name of the initiator or `null` if not set.
<a id="Return_value_anyOf_i3_initiator_alias_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_initiator_alias_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_initiator_alias_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_initiator_alias_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_initiator_alias_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_target"></a>
<a id="Return_value_anyOf_i3_target"></a>
###### target

- Schema name: `Target`
- Type: string

iSCSI Qualified Name (IQN) of the target.

<a id="headingReturn_value_anyOf_i3_target_alias"></a>
<a id="Return_value_anyOf_i3_target_alias"></a>
###### target_alias

- Schema name: `Target Alias`
- Type: string

Alias name of the target.

<a id="headingReturn_value_anyOf_i3_header_digest"></a>
<a id="Return_value_anyOf_i3_header_digest"></a>
###### header_digest

- Schema name: `Header Digest`

Header digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i3_header_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_header_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_header_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_header_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_header_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_data_digest"></a>
<a id="Return_value_anyOf_i3_data_digest"></a>
###### data_digest

- Schema name: `Data Digest`

Data digest algorithm used for the session or `null`.
<a id="Return_value_anyOf_i3_data_digest_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_data_digest_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_data_digest_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_data_digest_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_data_digest_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_max_data_segment_length"></a>
<a id="Return_value_anyOf_i3_max_data_segment_length"></a>
###### max_data_segment_length

- Schema name: `Max Data Segment Length`

Maximum data segment length for the session or `null`.
<a id="Return_value_anyOf_i3_max_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_max_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_max_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_max_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_max_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_max_receive_data_segment_length"></a>
<a id="Return_value_anyOf_i3_max_receive_data_segment_length"></a>
###### max_receive_data_segment_length

- Schema name: `Max Receive Data Segment Length`

Maximum receive data segment length or `null`.
<a id="Return_value_anyOf_i3_max_receive_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_max_receive_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_max_receive_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_max_receive_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_max_receive_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_max_xmit_data_segment_length"></a>
<a id="Return_value_anyOf_i3_max_xmit_data_segment_length"></a>
###### max_xmit_data_segment_length

- Schema name: `Max Xmit Data Segment Length`

Maximum transmit data segment length or `null`.
<a id="Return_value_anyOf_i3_max_xmit_data_segment_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_max_xmit_data_segment_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_max_xmit_data_segment_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_max_xmit_data_segment_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_max_xmit_data_segment_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_max_burst_length"></a>
<a id="Return_value_anyOf_i3_max_burst_length"></a>
###### max_burst_length

- Schema name: `Max Burst Length`

Maximum burst length for the session or `null`.
<a id="Return_value_anyOf_i3_max_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_max_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_max_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_max_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_max_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_first_burst_length"></a>
<a id="Return_value_anyOf_i3_first_burst_length"></a>
###### first_burst_length

- Schema name: `First Burst Length`

First burst length for the session or `null`.
<a id="Return_value_anyOf_i3_first_burst_length_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_first_burst_length_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_first_burst_length_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_first_burst_length_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_first_burst_length_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_immediate_data"></a>
<a id="Return_value_anyOf_i3_immediate_data"></a>
###### immediate_data

- Schema name: `Immediate Data`
- Type: boolean

Whether immediate data transfer is enabled.

<a id="headingReturn_value_anyOf_i3_iser"></a>
<a id="Return_value_anyOf_i3_iser"></a>
###### iser

- Schema name: `Iser`
- Type: boolean

Whether this session is using iSER (iSCSI Extensions for RDMA).

<a id="headingReturn_value_anyOf_i3_offload"></a>
<a id="Return_value_anyOf_i3_offload"></a>
###### offload

- Schema name: `Offload`
- Type: boolean

Whether hardware offload is enabled for this session.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
