---
title: ipmi.lan.query
kind: method
source_rst: _sources/api_methods_ipmi.lan.query.rst.txt
source_html: api_methods_ipmi.lan.query.html
required_roles:
  - IPMI_READ
---

# ipmi.lan.query

## Summary

Query available IPMI Channels with `query-filters` and `query-options`.

## Required Roles

- `IPMI_READ`

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

Query parameters for IPMI LAN configuration.
- No Additional Properties
<a id="headingCall_parameters_items_i0_query-filters"></a>
<a id="Call_parameters_items_i0_query-filters"></a>
##### query-filters

- Schema name: `Query-Filters`
- Type: array
- Default: []

Query filters to apply to IPMI LAN configuration results.
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

Query options for sorting and pagination.
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
- Value must be greater or equal to `0`

<a id="headingCall_parameters_items_i0_query-options_limit"></a>
<a id="Call_parameters_items_i0_query-options_limit"></a>
###### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.
- Value must be greater or equal to `0` and lesser or equal to `10000`

<a id="headingCall_parameters_items_i0_query-options_force_sql_filters"></a>
<a id="Call_parameters_items_i0_query-options_force_sql_filters"></a>
###### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingCall_parameters_items_i0_ipmi-options"></a>
<a id="Call_parameters_items_i0_ipmi-options"></a>
##### ipmi-options

- Schema name: `IPMILanQueryOptions`
- Type: object

IPMI-specific query options.
- No Additional Properties
<a id="headingCall_parameters_items_i0_ipmi-options_query-remote"></a>
<a id="Call_parameters_items_i0_ipmi-options_query-remote"></a>
###### query-remote

- Schema name: `Query-Remote`
- Type: boolean
- Default: false

Whether to query remote IPMI LAN configuration on HA systems.

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
###### IPMILanEntry

- Schema name: `IPMILanEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_channel"></a>
<a id="Return_value_anyOf_i0_items_channel"></a>
###### channel

- Schema name: `Channel`
- Type: integer

IPMI LAN channel number.

<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the IPMI LAN configuration.

<a id="headingReturn_value_anyOf_i0_items_ip_address_source"></a>
<a id="Return_value_anyOf_i0_items_ip_address_source"></a>
###### ip_address_source

- Schema name: `Ip Address Source`
- Type: string

Source type for IP address assignment (e.g., "DHCP", "Static").

<a id="headingReturn_value_anyOf_i0_items_ip_address"></a>
<a id="Return_value_anyOf_i0_items_ip_address"></a>
###### ip_address

- Schema name: `Ip Address`
- Type: string

Current IP address assigned to the IPMI interface.

<a id="headingReturn_value_anyOf_i0_items_mac_address"></a>
<a id="Return_value_anyOf_i0_items_mac_address"></a>
###### mac_address

- Schema name: `Mac Address`
- Type: string

MAC address of the IPMI network interface.

<a id="headingReturn_value_anyOf_i0_items_subnet_mask"></a>
<a id="Return_value_anyOf_i0_items_subnet_mask"></a>
###### subnet_mask

- Schema name: `Subnet Mask`
- Type: string

Subnet mask for the IPMI network interface.

<a id="headingReturn_value_anyOf_i0_items_default_gateway_ip_address"></a>
<a id="Return_value_anyOf_i0_items_default_gateway_ip_address"></a>
###### default_gateway_ip_address

- Schema name: `Default Gateway Ip Address`
- Type: string

IP address of the default gateway.

<a id="headingReturn_value_anyOf_i0_items_default_gateway_mac_address"></a>
<a id="Return_value_anyOf_i0_items_default_gateway_mac_address"></a>
###### default_gateway_mac_address

- Schema name: `Default Gateway Mac Address`
- Type: string

MAC address of the default gateway.

<a id="headingReturn_value_anyOf_i0_items_backup_gateway_ip_address"></a>
<a id="Return_value_anyOf_i0_items_backup_gateway_ip_address"></a>
###### backup_gateway_ip_address

- Schema name: `Backup Gateway Ip Address`
- Type: string

IP address of the backup gateway.

<a id="headingReturn_value_anyOf_i0_items_backup_gateway_mac_address"></a>
<a id="Return_value_anyOf_i0_items_backup_gateway_mac_address"></a>
###### backup_gateway_mac_address

- Schema name: `Backup Gateway Mac Address`
- Type: string

MAC address of the backup gateway.

<a id="headingReturn_value_anyOf_i0_items_vlan_id"></a>
<a id="Return_value_anyOf_i0_items_vlan_id"></a>
###### vlan_id

- Schema name: `Vlan Id`

VLAN ID number or `null` if VLAN is not configured.
<a id="Return_value_anyOf_i0_items_vlan_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_vlan_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_vlan_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_vlan_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_vlan_id_enable"></a>
<a id="Return_value_anyOf_i0_items_vlan_id_enable"></a>
###### vlan_id_enable

- Schema name: `Vlan Id Enable`
- Type: boolean

Whether VLAN tagging is enabled for this interface.

<a id="headingReturn_value_anyOf_i0_items_vlan_priority"></a>
<a id="Return_value_anyOf_i0_items_vlan_priority"></a>
###### vlan_priority

- Schema name: `Vlan Priority`
- Type: integer

VLAN priority level for tagged packets.

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [IPMILanEntry](#tab-pane_Return_value_anyOf_i1)

- Schema name: `IPMILanEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_channel"></a>
<a id="Return_value_anyOf_i1_channel"></a>
###### channel

- Schema name: `Channel`
- Type: integer

IPMI LAN channel number.

<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the IPMI LAN configuration.

<a id="headingReturn_value_anyOf_i1_ip_address_source"></a>
<a id="Return_value_anyOf_i1_ip_address_source"></a>
###### ip_address_source

- Schema name: `Ip Address Source`
- Type: string

Source type for IP address assignment (e.g., "DHCP", "Static").

<a id="headingReturn_value_anyOf_i1_ip_address"></a>
<a id="Return_value_anyOf_i1_ip_address"></a>
###### ip_address

- Schema name: `Ip Address`
- Type: string

Current IP address assigned to the IPMI interface.

<a id="headingReturn_value_anyOf_i1_mac_address"></a>
<a id="Return_value_anyOf_i1_mac_address"></a>
###### mac_address

- Schema name: `Mac Address`
- Type: string

MAC address of the IPMI network interface.

<a id="headingReturn_value_anyOf_i1_subnet_mask"></a>
<a id="Return_value_anyOf_i1_subnet_mask"></a>
###### subnet_mask

- Schema name: `Subnet Mask`
- Type: string

Subnet mask for the IPMI network interface.

<a id="headingReturn_value_anyOf_i1_default_gateway_ip_address"></a>
<a id="Return_value_anyOf_i1_default_gateway_ip_address"></a>
###### default_gateway_ip_address

- Schema name: `Default Gateway Ip Address`
- Type: string

IP address of the default gateway.

<a id="headingReturn_value_anyOf_i1_default_gateway_mac_address"></a>
<a id="Return_value_anyOf_i1_default_gateway_mac_address"></a>
###### default_gateway_mac_address

- Schema name: `Default Gateway Mac Address`
- Type: string

MAC address of the default gateway.

<a id="headingReturn_value_anyOf_i1_backup_gateway_ip_address"></a>
<a id="Return_value_anyOf_i1_backup_gateway_ip_address"></a>
###### backup_gateway_ip_address

- Schema name: `Backup Gateway Ip Address`
- Type: string

IP address of the backup gateway.

<a id="headingReturn_value_anyOf_i1_backup_gateway_mac_address"></a>
<a id="Return_value_anyOf_i1_backup_gateway_mac_address"></a>
###### backup_gateway_mac_address

- Schema name: `Backup Gateway Mac Address`
- Type: string

MAC address of the backup gateway.

<a id="headingReturn_value_anyOf_i1_vlan_id"></a>
<a id="Return_value_anyOf_i1_vlan_id"></a>
###### vlan_id

- Schema name: `Vlan Id`

VLAN ID number or `null` if VLAN is not configured.
<a id="Return_value_anyOf_i1_vlan_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_vlan_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_vlan_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i1_vlan_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_vlan_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_vlan_id_enable"></a>
<a id="Return_value_anyOf_i1_vlan_id_enable"></a>
###### vlan_id_enable

- Schema name: `Vlan Id Enable`
- Type: boolean

Whether VLAN tagging is enabled for this interface.

<a id="headingReturn_value_anyOf_i1_vlan_priority"></a>
<a id="Return_value_anyOf_i1_vlan_priority"></a>
###### vlan_priority

- Schema name: `Vlan Priority`
- Type: integer

VLAN priority level for tagged packets.

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i2_items"></a>
###### IPMILanQueryResultItem

- Schema name: `IPMILanQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i2_items_channel"></a>
<a id="Return_value_anyOf_i2_items_channel"></a>
###### channel

- Schema name: `Channel`
- Type: integer

IPMI LAN channel number.

<a id="headingReturn_value_anyOf_i2_items_id"></a>
<a id="Return_value_anyOf_i2_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the IPMI LAN configuration.

<a id="headingReturn_value_anyOf_i2_items_ip_address_source"></a>
<a id="Return_value_anyOf_i2_items_ip_address_source"></a>
###### ip_address_source

- Schema name: `Ip Address Source`
- Type: string

Source type for IP address assignment (e.g., "DHCP", "Static").

<a id="headingReturn_value_anyOf_i2_items_ip_address"></a>
<a id="Return_value_anyOf_i2_items_ip_address"></a>
###### ip_address

- Schema name: `Ip Address`
- Type: string

Current IP address assigned to the IPMI interface.

<a id="headingReturn_value_anyOf_i2_items_mac_address"></a>
<a id="Return_value_anyOf_i2_items_mac_address"></a>
###### mac_address

- Schema name: `Mac Address`
- Type: string

MAC address of the IPMI network interface.

<a id="headingReturn_value_anyOf_i2_items_subnet_mask"></a>
<a id="Return_value_anyOf_i2_items_subnet_mask"></a>
###### subnet_mask

- Schema name: `Subnet Mask`
- Type: string

Subnet mask for the IPMI network interface.

<a id="headingReturn_value_anyOf_i2_items_default_gateway_ip_address"></a>
<a id="Return_value_anyOf_i2_items_default_gateway_ip_address"></a>
###### default_gateway_ip_address

- Schema name: `Default Gateway Ip Address`
- Type: string

IP address of the default gateway.

<a id="headingReturn_value_anyOf_i2_items_default_gateway_mac_address"></a>
<a id="Return_value_anyOf_i2_items_default_gateway_mac_address"></a>
###### default_gateway_mac_address

- Schema name: `Default Gateway Mac Address`
- Type: string

MAC address of the default gateway.

<a id="headingReturn_value_anyOf_i2_items_backup_gateway_ip_address"></a>
<a id="Return_value_anyOf_i2_items_backup_gateway_ip_address"></a>
###### backup_gateway_ip_address

- Schema name: `Backup Gateway Ip Address`
- Type: string

IP address of the backup gateway.

<a id="headingReturn_value_anyOf_i2_items_backup_gateway_mac_address"></a>
<a id="Return_value_anyOf_i2_items_backup_gateway_mac_address"></a>
###### backup_gateway_mac_address

- Schema name: `Backup Gateway Mac Address`
- Type: string

MAC address of the backup gateway.

<a id="headingReturn_value_anyOf_i2_items_vlan_id"></a>
<a id="Return_value_anyOf_i2_items_vlan_id"></a>
###### vlan_id

- Schema name: `Vlan Id`

VLAN ID number or `null` if VLAN is not configured.
<a id="Return_value_anyOf_i2_items_vlan_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i2_items_vlan_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i2_items_vlan_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i2_items_vlan_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i2_items_vlan_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i2_items_vlan_id_enable"></a>
<a id="Return_value_anyOf_i2_items_vlan_id_enable"></a>
###### vlan_id_enable

- Schema name: `Vlan Id Enable`
- Type: boolean

Whether VLAN tagging is enabled for this interface.

<a id="headingReturn_value_anyOf_i2_items_vlan_priority"></a>
<a id="Return_value_anyOf_i2_items_vlan_priority"></a>
###### vlan_priority

- Schema name: `Vlan Priority`
- Type: integer

VLAN priority level for tagged packets.

<a id="tab-pane_Return_value_anyOf_i3"></a>
##### [IPMILanQueryResultItem](#tab-pane_Return_value_anyOf_i3)

- Schema name: `IPMILanQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i3_channel"></a>
<a id="Return_value_anyOf_i3_channel"></a>
###### channel

- Schema name: `Channel`
- Type: integer

IPMI LAN channel number.

<a id="headingReturn_value_anyOf_i3_id"></a>
<a id="Return_value_anyOf_i3_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for the IPMI LAN configuration.

<a id="headingReturn_value_anyOf_i3_ip_address_source"></a>
<a id="Return_value_anyOf_i3_ip_address_source"></a>
###### ip_address_source

- Schema name: `Ip Address Source`
- Type: string

Source type for IP address assignment (e.g., "DHCP", "Static").

<a id="headingReturn_value_anyOf_i3_ip_address"></a>
<a id="Return_value_anyOf_i3_ip_address"></a>
###### ip_address

- Schema name: `Ip Address`
- Type: string

Current IP address assigned to the IPMI interface.

<a id="headingReturn_value_anyOf_i3_mac_address"></a>
<a id="Return_value_anyOf_i3_mac_address"></a>
###### mac_address

- Schema name: `Mac Address`
- Type: string

MAC address of the IPMI network interface.

<a id="headingReturn_value_anyOf_i3_subnet_mask"></a>
<a id="Return_value_anyOf_i3_subnet_mask"></a>
###### subnet_mask

- Schema name: `Subnet Mask`
- Type: string

Subnet mask for the IPMI network interface.

<a id="headingReturn_value_anyOf_i3_default_gateway_ip_address"></a>
<a id="Return_value_anyOf_i3_default_gateway_ip_address"></a>
###### default_gateway_ip_address

- Schema name: `Default Gateway Ip Address`
- Type: string

IP address of the default gateway.

<a id="headingReturn_value_anyOf_i3_default_gateway_mac_address"></a>
<a id="Return_value_anyOf_i3_default_gateway_mac_address"></a>
###### default_gateway_mac_address

- Schema name: `Default Gateway Mac Address`
- Type: string

MAC address of the default gateway.

<a id="headingReturn_value_anyOf_i3_backup_gateway_ip_address"></a>
<a id="Return_value_anyOf_i3_backup_gateway_ip_address"></a>
###### backup_gateway_ip_address

- Schema name: `Backup Gateway Ip Address`
- Type: string

IP address of the backup gateway.

<a id="headingReturn_value_anyOf_i3_backup_gateway_mac_address"></a>
<a id="Return_value_anyOf_i3_backup_gateway_mac_address"></a>
###### backup_gateway_mac_address

- Schema name: `Backup Gateway Mac Address`
- Type: string

MAC address of the backup gateway.

<a id="headingReturn_value_anyOf_i3_vlan_id"></a>
<a id="Return_value_anyOf_i3_vlan_id"></a>
###### vlan_id

- Schema name: `Vlan Id`

VLAN ID number or `null` if VLAN is not configured.
<a id="Return_value_anyOf_i3_vlan_id_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i3_vlan_id_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i3_vlan_id_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i3_vlan_id_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i3_vlan_id_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i3_vlan_id_enable"></a>
<a id="Return_value_anyOf_i3_vlan_id_enable"></a>
###### vlan_id_enable

- Schema name: `Vlan Id Enable`
- Type: boolean

Whether VLAN tagging is enabled for this interface.

<a id="headingReturn_value_anyOf_i3_vlan_priority"></a>
<a id="Return_value_anyOf_i3_vlan_priority"></a>
###### vlan_priority

- Schema name: `Vlan Priority`
- Type: integer

VLAN priority level for tagged packets.

<a id="tab-pane_Return_value_anyOf_i4"></a>
##### [Option 5](#tab-pane_Return_value_anyOf_i4)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
