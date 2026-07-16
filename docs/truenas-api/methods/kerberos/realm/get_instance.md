---
title: kerberos.realm.get_instance
kind: method
source_rst: _sources/api_methods_kerberos.realm.get_instance.rst.txt
source_html: api_methods_kerberos.realm.get_instance.html
required_roles:
  - DIRECTORY_SERVICE_READ
---

# kerberos.realm.get_instance

## Summary

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `DIRECTORY_SERVICE_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: integer

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default: {}

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `KerberosRealmEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the Kerberos realm configuration.

#### realm (required)

- Schema name: `Realm`
- Type: string

Kerberos realm name. This is external to TrueNAS and is case-sensitive. The general convention for kerberos realms is that they are upper-case.
- Must be at least `1` characters long

#### primary_kdc

- Schema name: `Primary Kdc`
- Default: null

The master Kerberos domain controller for this realm. TrueNAS uses this as a fallback if it cannot get credentials because of an invalid password. This can help in environments where the domain uses a hub-and-spoke topology. Use this setting to reduce credential errors after TrueNAS automatically changes its machine password.
##### Any of

###### Option 1

- Type: string
- Must be at least `1` characters long

###### Option 2

- Type: null

#### kdc

- Schema name: `Kdc`
- Type: array of string
- Default: []

List of kerberos domain controllers. If the list is empty then the kerberos libraries will use DNS to look up KDCs. In some situations this is undesirable as kerberos libraries are, for intance, not active directory site aware and so may be suboptimal.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### admin_server

- Schema name: `Admin Server`
- Type: array of string
- Default: []

List of kerberos admin servers. If the list is empty then the kerberos libraries will use DNS to look them up.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

#### kpasswd_server

- Schema name: `Kpasswd Server`
- Type: array of string
- Default: []

List of kerberos kpasswd servers. If the list is empty then DNS will be used to look them up if needed.
- No Additional Items

##### Each item of this array must be:

- Type: string
- Must be at least `1` characters long

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
