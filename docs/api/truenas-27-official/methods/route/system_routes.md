---
title: route.system_routes
kind: method
source_rst: _sources/api_methods_route.system_routes.rst.txt
source_html: api_methods_route.system_routes.html
required_roles:
  - NETWORK_INTERFACE_READ
---

# route.system_routes

## Summary

Query IPv4 and IPv6 routes from the kernel's main routing table.

Returns routes currently installed in the system, including static routes, DHCP-learned routes, and directly connected networks. The default route (0.0.0.0/0 or ::/0) will have both network and netmask set to all zeros.

## Required Roles

- `NETWORK_INTERFACE_READ`

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
###### RouteSystemRoutesItem

- Schema name: `RouteSystemRoutesItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_network"></a>
<a id="Return_value_anyOf_i0_items_network"></a>
###### network (required)

- Schema name: `Network`

Network address for this route.
<a id="Return_value_anyOf_i0_items_network_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_network_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i0_items_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_network_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i0_items_netmask"></a>
<a id="Return_value_anyOf_i0_items_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`

Network mask for this route.
<a id="Return_value_anyOf_i0_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_netmask_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i0_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_netmask_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i0_items_gateway"></a>
<a id="Return_value_anyOf_i0_items_gateway"></a>
###### gateway (required)

- Schema name: `Gateway`

Gateway IP address for this route. `null` if directly connected.
<a id="Return_value_anyOf_i0_items_gateway_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i0_items_gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_gateway_anyOf_i1)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_gateway_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i0_items_gateway_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_interface"></a>
<a id="Return_value_anyOf_i0_items_interface"></a>
###### interface (required)

- Schema name: `Interface`

Network interface name for this route. `null` if not bound to specific interface.
<a id="Return_value_anyOf_i0_items_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_flags"></a>
<a id="Return_value_anyOf_i0_items_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array

Array of routing flags for this route.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_flags_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_table_id"></a>
<a id="Return_value_anyOf_i0_items_table_id"></a>
###### table_id (required)

- Schema name: `Table Id`
- Type: integer

Routing table ID where this route is stored.

<a id="headingReturn_value_anyOf_i0_items_scope"></a>
<a id="Return_value_anyOf_i0_items_scope"></a>
###### scope (required)

- Schema name: `Scope`
- Type: integer

Routing scope indicating the distance to the destination.

<a id="headingReturn_value_anyOf_i0_items_preferred_source"></a>
<a id="Return_value_anyOf_i0_items_preferred_source"></a>
###### preferred_source (required)

- Schema name: `Preferred Source`

Preferred source IP address for outgoing packets. `null` if not specified.
<a id="Return_value_anyOf_i0_items_preferred_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_preferred_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_preferred_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_preferred_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_preferred_source_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [RouteSystemRoutesItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `RouteSystemRoutesItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_network"></a>
<a id="Return_value_anyOf_i1_network"></a>
###### network (required)

- Schema name: `Network`

Network address for this route.
<a id="Return_value_anyOf_i1_network_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_network_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i1_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_network_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i1_netmask"></a>
<a id="Return_value_anyOf_i1_netmask"></a>
###### netmask (required)

- Schema name: `Netmask`

Network mask for this route.
<a id="Return_value_anyOf_i1_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_netmask_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i1_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_netmask_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i1_gateway"></a>
<a id="Return_value_anyOf_i1_gateway"></a>
###### gateway (required)

- Schema name: `Gateway`

Gateway IP address for this route. `null` if directly connected.
<a id="Return_value_anyOf_i1_gateway_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i1_gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_gateway_anyOf_i1)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_gateway_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i1_gateway_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i1_interface"></a>
<a id="Return_value_anyOf_i1_interface"></a>
###### interface (required)

- Schema name: `Interface`

Network interface name for this route. `null` if not bound to specific interface.
<a id="Return_value_anyOf_i1_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_flags"></a>
<a id="Return_value_anyOf_i1_flags"></a>
###### flags (required)

- Schema name: `Flags`
- Type: array

Array of routing flags for this route.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_flags_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_table_id"></a>
<a id="Return_value_anyOf_i1_table_id"></a>
###### table_id (required)

- Schema name: `Table Id`
- Type: integer

Routing table ID where this route is stored.

<a id="headingReturn_value_anyOf_i1_scope"></a>
<a id="Return_value_anyOf_i1_scope"></a>
###### scope (required)

- Schema name: `Scope`
- Type: integer

Routing scope indicating the distance to the destination.

<a id="headingReturn_value_anyOf_i1_preferred_source"></a>
<a id="Return_value_anyOf_i1_preferred_source"></a>
###### preferred_source (required)

- Schema name: `Preferred Source`

Preferred source IP address for outgoing packets. `null` if not specified.
<a id="Return_value_anyOf_i1_preferred_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_preferred_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_preferred_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_preferred_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_preferred_source_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### RouteSystemRoutesItemQueryResultItem

- Schema name: `RouteSystemRoutesItemQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_network"></a>
<a id="Return_value_anyOf_i2_items_network"></a>
###### network

- Schema name: `Network`

Network address for this route.
<a id="Return_value_anyOf_i2_items_network_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_network_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i2_items_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_network_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i2_items_netmask"></a>
<a id="Return_value_anyOf_i2_items_netmask"></a>
###### netmask

- Schema name: `Netmask`

Network mask for this route.
<a id="Return_value_anyOf_i2_items_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_netmask_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i2_items_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_netmask_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i2_items_gateway"></a>
<a id="Return_value_anyOf_i2_items_gateway"></a>
###### gateway

- Schema name: `Gateway`

Gateway IP address for this route. `null` if directly connected.
<a id="Return_value_anyOf_i2_items_gateway_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i2_items_gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_gateway_anyOf_i1)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_gateway_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i2_items_gateway_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_interface"></a>
<a id="Return_value_anyOf_i2_items_interface"></a>
###### interface

- Schema name: `Interface`

Network interface name for this route. `null` if not bound to specific interface.
<a id="Return_value_anyOf_i2_items_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_flags"></a>
<a id="Return_value_anyOf_i2_items_flags"></a>
###### flags

- Schema name: `Flags`
- Type: array

Array of routing flags for this route.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items_flags_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i2_items_table_id"></a>
<a id="Return_value_anyOf_i2_items_table_id"></a>
###### table_id

- Schema name: `Table Id`
- Type: integer

Routing table ID where this route is stored.

<a id="headingReturn_value_anyOf_i2_items_scope"></a>
<a id="Return_value_anyOf_i2_items_scope"></a>
###### scope

- Schema name: `Scope`
- Type: integer

Routing scope indicating the distance to the destination.

<a id="headingReturn_value_anyOf_i2_items_preferred_source"></a>
<a id="Return_value_anyOf_i2_items_preferred_source"></a>
###### preferred_source

- Schema name: `Preferred Source`

Preferred source IP address for outgoing packets. `null` if not specified.
<a id="Return_value_anyOf_i2_items_preferred_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_preferred_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_preferred_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i2_items_preferred_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_preferred_source_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [RouteSystemRoutesItemQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `RouteSystemRoutesItemQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_network"></a>
<a id="Return_value_anyOf_i3_network"></a>
###### network

- Schema name: `Network`

Network address for this route.
<a id="Return_value_anyOf_i3_network_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_network_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_network_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i3_network_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_network_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i3_netmask"></a>
<a id="Return_value_anyOf_i3_netmask"></a>
###### netmask

- Schema name: `Netmask`

Network mask for this route.
<a id="Return_value_anyOf_i3_netmask_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_netmask_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_netmask_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i3_netmask_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_netmask_anyOf_i1)

- Type: string

<a id="headingReturn_value_anyOf_i3_gateway"></a>
<a id="Return_value_anyOf_i3_gateway"></a>
###### gateway

- Schema name: `Gateway`

Gateway IP address for this route. `null` if directly connected.
<a id="Return_value_anyOf_i3_gateway_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_gateway_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_gateway_anyOf_i0)

- Type: const
- Specific value: `""`

<a id="tab-pane_Return_value_anyOf_i3_gateway_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_gateway_anyOf_i1)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_gateway_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_anyOf_i3_gateway_anyOf_i2)

- Type: null

<a id="headingReturn_value_anyOf_i3_interface"></a>
<a id="Return_value_anyOf_i3_interface"></a>
###### interface

- Schema name: `Interface`

Network interface name for this route. `null` if not bound to specific interface.
<a id="Return_value_anyOf_i3_interface_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_interface_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_interface_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_interface_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_interface_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_flags"></a>
<a id="Return_value_anyOf_i3_flags"></a>
###### flags

- Schema name: `Flags`
- Type: array

Array of routing flags for this route.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i3_flags_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i3_table_id"></a>
<a id="Return_value_anyOf_i3_table_id"></a>
###### table_id

- Schema name: `Table Id`
- Type: integer

Routing table ID where this route is stored.

<a id="headingReturn_value_anyOf_i3_scope"></a>
<a id="Return_value_anyOf_i3_scope"></a>
###### scope

- Schema name: `Scope`
- Type: integer

Routing scope indicating the distance to the destination.

<a id="headingReturn_value_anyOf_i3_preferred_source"></a>
<a id="Return_value_anyOf_i3_preferred_source"></a>
###### preferred_source

- Schema name: `Preferred Source`

Preferred source IP address for outgoing packets. `null` if not specified.
<a id="Return_value_anyOf_i3_preferred_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_preferred_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_preferred_source_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i3_preferred_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_preferred_source_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
