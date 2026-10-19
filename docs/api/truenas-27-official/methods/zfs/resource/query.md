---
title: zfs.resource.query
kind: method
source_rst: _sources/api_methods_zfs.resource.query.rst.txt
source_html: api_methods_zfs.resource.query.html
required_roles:
  - ZFS_RESOURCE_READ
---

# zfs.resource.query

## Summary

List ZFS resources (datasets and volumes) with flexible filtering options.

*DEPRECATED: this method is scheduled to be removed in v28.*

## Required Roles

- `ZFS_RESOURCE_READ`

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
  "paths": [],
  "properties": [],
  "get_user_properties": false,
  "get_source": false,
  "nest_results": false,
  "get_children": false,
  "max_depth": 0,
  "exclude_internal_paths": true,
  "get_tier": false
}
```

Query parameters for retrieving ZFS resource information.
- No Additional Properties
<a id="headingCall_parameters_items_i0_paths"></a>
<a id="Call_parameters_items_i0_paths"></a>
##### paths

- Schema name: `Paths`
- Type: array of string
- Default: []

A list of zfs filesystem or volume paths to be queried. In almost all scenarios, you should provide a path of what you want to query. By providing path(s) here, it allows the API to apply optimizations so that the requested information is retrieved as efficiently and quickly as possible. Example 1: {"paths": ["tank/foo"]} will query the relevant information for this resource only. Example 2: {"paths": ["tank/foo", "dozer/test"]} will query the relevant information for these resources only. NOTE: paths must be non-overlapping if `get_children` is True. (i.e. this won't work and will raise a validation error) { "paths": ["tank/foo1", "tank/foo1/foo2"], "get_children": True }
- All items must be unique
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_paths_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_properties"></a>
<a id="Call_parameters_items_i0_properties"></a>
##### properties

- Schema name: `Properties`
- Default: []

A list of zfs properties to be retrieved. Defaults to an empty list which will return a default set of zfs properties. Setting this to None will retrieve no zfs properties.
<a id="Call_parameters_items_i0_properties_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i0_properties_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_properties_anyOf_i0)

- Type: array of string
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_properties_anyOf_i0_items"></a>
- Type: string

<a id="tab-pane_Call_parameters_items_i0_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_properties_anyOf_i1)

- Type: null

<a id="headingCall_parameters_items_i0_get_user_properties"></a>
<a id="Call_parameters_items_i0_get_user_properties"></a>
##### get_user_properties

- Schema name: `Get User Properties`
- Type: boolean
- Default: false

Retrieve user properties for zfs resource(s).

<a id="headingCall_parameters_items_i0_get_source"></a>
<a id="Call_parameters_items_i0_get_source"></a>
##### get_source

- Schema name: `Get Source`
- Type: boolean
- Default: false

Retrieve source information for a zfs property.

<a id="headingCall_parameters_items_i0_nest_results"></a>
<a id="Call_parameters_items_i0_nest_results"></a>
##### nest_results

- Schema name: `Nest Results`
- Type: boolean
- Default: false

Return a nested object that associates all children to their respective parents in the filesystem. By default, each zfs resource is returned as a separate item in the array and is not associated to its parent.

<a id="headingCall_parameters_items_i0_get_children"></a>
<a id="Call_parameters_items_i0_get_children"></a>
##### get_children

- Schema name: `Get Children`
- Type: boolean
- Default: false

Retrieve children information for the zfs resource.

<a id="headingCall_parameters_items_i0_max_depth"></a>
<a id="Call_parameters_items_i0_max_depth"></a>
##### max_depth

- Schema name: `Max Depth`
- Type: integer
- Default: 0

Maximum depth to recurse when retrieving children. A value of 0 means unlimited recursion (default behavior). A value greater than 0 limits the recursion to that many levels deep. When max*depth > 0, get*children is automatically enabled if not already set. Examples: max*depth=0: Retrieve all descendants (unlimited depth). max*depth=1: Retrieve only immediate children. max*depth=2: Retrieve children and grandchildren. max*depth=3: Retrieve up to great-grandchildren. Note: When max*depth > 0 is specified, it takes priority over get*children. The depth is measured from the specified path(s), not from the pool root.

<a id="headingCall_parameters_items_i0_get_tier"></a>
<a id="Call_parameters_items_i0_get_tier"></a>
##### get_tier

- Schema name: `Get Tier`
- Type: boolean
- Default: false

Retrieve tier classification (REGULAR/PERFORMANCE) for FILESYSTEM resources. Requires an active Enterprise license with ZFS tiering enabled.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### ZFSResourceEntry

- Schema name: `ZFSResourceEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_createtxg"></a>
<a id="Return_value_items_createtxg"></a>
##### createtxg (required)

- Schema name: `Createtxg`
- Type: integer

Transaction group when resource was created.

<a id="headingReturn_value_items_guid"></a>
<a id="Return_value_items_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: integer

Globally unique identifier for the resource.

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

The name of the zfs resource.

<a id="headingReturn_value_items_pool"></a>
<a id="Return_value_items_pool"></a>
##### pool (required)

- Schema name: `Pool`
- Type: string

The name of the zpool that the zfs resouce is associated to.

<a id="headingReturn_value_items_properties"></a>
<a id="Return_value_items_properties"></a>
##### properties (required)

The zfs properties for the resource.
<a id="Return_value_items_properties_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0"></a>
###### [ZFSPropertiesEntry](#tab-pane_Return_value_items_properties_anyOf_i0)

- Schema name: `ZFSPropertiesEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_aclinherit"></a>
<a id="Return_value_items_properties_anyOf_i0_aclinherit"></a>
###### aclinherit

- Schema name: `Aclinherit`
- Type: object

Controls how ACEs are inherited for new files/directories.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_aclinherit_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_aclinherit_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_aclinherit_source"></a>
<a id="Return_value_items_properties_anyOf_i0_aclinherit_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0"></a>
###### [SourceValue](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0)

- Schema name: `SourceValue`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_type"></a>
<a id="Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: enum (of string)

The source type.
###### Must be one of:

- "NONE"
- "DEFAULT"
- "TEMPORARY"
- "LOCAL"
- "INHERITED"
- "RECEIVED"

<a id="headingReturn_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value"></a>
<a id="Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value"></a>
###### value (required)

- Schema name: `Value`

The source value.
<a id="Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i0_value_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_aclinherit_value"></a>
<a id="Return_value_items_properties_anyOf_i0_aclinherit_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_aclinherit_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_aclmode"></a>
<a id="Return_value_items_properties_anyOf_i0_aclmode"></a>
###### aclmode

- Schema name: `Aclmode`
- Type: object

Determines how ACLs are modified during chmod operations.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_aclmode_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_aclmode_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_aclmode_source"></a>
<a id="Return_value_items_properties_anyOf_i0_aclmode_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_aclmode_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_aclmode_value"></a>
<a id="Return_value_items_properties_anyOf_i0_aclmode_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_aclmode_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_aclmode_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_acltype"></a>
<a id="Return_value_items_properties_anyOf_i0_acltype"></a>
###### acltype

- Schema name: `Acltype`
- Type: object

Specifies type of ACL to use (off, nfsv4, posix).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_acltype_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_acltype_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_acltype_source"></a>
<a id="Return_value_items_properties_anyOf_i0_acltype_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_acltype_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_acltype_value"></a>
<a id="Return_value_items_properties_anyOf_i0_acltype_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_acltype_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_acltype_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_atime"></a>
<a id="Return_value_items_properties_anyOf_i0_atime"></a>
###### atime

- Schema name: `Atime`
- Type: object

Controls whether access time is updated on file reads.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_atime_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_atime_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_atime_source"></a>
<a id="Return_value_items_properties_anyOf_i0_atime_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_atime_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_atime_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_atime_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_atime_value"></a>
<a id="Return_value_items_properties_anyOf_i0_atime_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_atime_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_atime_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_canmount"></a>
<a id="Return_value_items_properties_anyOf_i0_canmount"></a>
###### canmount

- Schema name: `Canmount`
- Type: object

Controls whether filesystem can be mounted.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_canmount_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_canmount_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_canmount_source"></a>
<a id="Return_value_items_properties_anyOf_i0_canmount_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_canmount_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_canmount_value"></a>
<a id="Return_value_items_properties_anyOf_i0_canmount_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_canmount_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_canmount_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_casesensitivity"></a>
<a id="Return_value_items_properties_anyOf_i0_casesensitivity"></a>
###### casesensitivity

- Schema name: `Casesensitivity`
- Type: object

Determines filename matching algorithm sensitivity.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_casesensitivity_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_casesensitivity_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_casesensitivity_source"></a>
<a id="Return_value_items_properties_anyOf_i0_casesensitivity_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_casesensitivity_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_casesensitivity_value"></a>
<a id="Return_value_items_properties_anyOf_i0_casesensitivity_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_casesensitivity_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupobjquota"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupobjquota"></a>
###### defaultgroupobjquota

- Schema name: `Defaultgroupobjquota`
- Type: object

Default object quota for new groups.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupobjquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupobjquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupobjquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupobjquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defaultgroupobjquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupobjquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupobjquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupquota"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupquota"></a>
###### defaultgroupquota

- Schema name: `Defaultgroupquota`
- Type: object

Default space quota for new groups.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defaultgroupquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultgroupquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultgroupquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defaultgroupquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectobjquota"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectobjquota"></a>
###### defaultprojectobjquota

- Schema name: `Defaultprojectobjquota`
- Type: object

Default object quota for new projects.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectobjquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectobjquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectobjquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectobjquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defaultprojectobjquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectobjquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectobjquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectquota"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectquota"></a>
###### defaultprojectquota

- Schema name: `Defaultprojectquota`
- Type: object

Default space quota for new projects.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defaultprojectquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultprojectquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultprojectquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defaultprojectquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserobjquota"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserobjquota"></a>
###### defaultuserobjquota

- Schema name: `Defaultuserobjquota`
- Type: object

Default object quota for new users.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserobjquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserobjquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserobjquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserobjquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defaultuserobjquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserobjquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserobjquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserobjquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserquota"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserquota"></a>
###### defaultuserquota

- Schema name: `Defaultuserquota`
- Type: object

Default space quota for new users.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defaultuserquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defaultuserquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defaultuserquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defaultuserquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_devices"></a>
<a id="Return_value_items_properties_anyOf_i0_devices"></a>
###### devices

- Schema name: `Devices`
- Type: object

Controls whether device files can be opened.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_devices_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_devices_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_devices_source"></a>
<a id="Return_value_items_properties_anyOf_i0_devices_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_devices_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_devices_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_devices_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_devices_value"></a>
<a id="Return_value_items_properties_anyOf_i0_devices_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_devices_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_devices_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_direct"></a>
<a id="Return_value_items_properties_anyOf_i0_direct"></a>
###### direct

- Schema name: `Direct`
- Type: object

Controls direct I/O behavior (standard or always).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_direct_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_direct_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_direct_source"></a>
<a id="Return_value_items_properties_anyOf_i0_direct_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_direct_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_direct_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_direct_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_direct_value"></a>
<a id="Return_value_items_properties_anyOf_i0_direct_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_direct_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_direct_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_dnodesize"></a>
<a id="Return_value_items_properties_anyOf_i0_dnodesize"></a>
###### dnodesize

- Schema name: `Dnodesize`
- Type: object

Controls dnode size for new objects.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_dnodesize_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_dnodesize_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_dnodesize_source"></a>
<a id="Return_value_items_properties_anyOf_i0_dnodesize_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_dnodesize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_dnodesize_value"></a>
<a id="Return_value_items_properties_anyOf_i0_dnodesize_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_dnodesize_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_exec"></a>
<a id="Return_value_items_properties_anyOf_i0_exec"></a>
###### exec

- Schema name: `Exec`
- Type: object

Controls whether programs can be executed from filesystem.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_exec_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_exec_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_exec_source"></a>
<a id="Return_value_items_properties_anyOf_i0_exec_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_exec_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_exec_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_exec_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_exec_value"></a>
<a id="Return_value_items_properties_anyOf_i0_exec_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_exec_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_exec_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_count"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_count"></a>
###### filesystem_count

- Schema name: `Filesystem Count`
- Type: object

(READ-ONLY): Count of child filesystems.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_count_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_count_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_count_source"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_count_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_filesystem_count_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_count_value"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_count_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_count_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_limit"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_limit"></a>
###### filesystem_limit

- Schema name: `Filesystem Limit`
- Type: object

Maximum number of child filesystems allowed.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_limit_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_limit_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_limit_source"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_limit_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_filesystem_limit_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_filesystem_limit_value"></a>
<a id="Return_value_items_properties_anyOf_i0_filesystem_limit_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_filesystem_limit_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_longname"></a>
<a id="Return_value_items_properties_anyOf_i0_longname"></a>
###### longname

- Schema name: `Longname`
- Type: object

Controls support for long filenames.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_longname_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_longname_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_longname_source"></a>
<a id="Return_value_items_properties_anyOf_i0_longname_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_longname_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_longname_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_longname_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_longname_value"></a>
<a id="Return_value_items_properties_anyOf_i0_longname_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_longname_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_longname_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_mounted"></a>
<a id="Return_value_items_properties_anyOf_i0_mounted"></a>
###### mounted

- Schema name: `Mounted`
- Type: object

(READ-ONLY): Property indicating if filesystem is mounted.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_mounted_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_mounted_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_mounted_source"></a>
<a id="Return_value_items_properties_anyOf_i0_mounted_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_mounted_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_mounted_value"></a>
<a id="Return_value_items_properties_anyOf_i0_mounted_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_mounted_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_mounted_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_mountpoint"></a>
<a id="Return_value_items_properties_anyOf_i0_mountpoint"></a>
###### mountpoint

- Schema name: `Mountpoint`
- Type: object

Controls mount point used for this filesystem.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_mountpoint_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_mountpoint_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_mountpoint_source"></a>
<a id="Return_value_items_properties_anyOf_i0_mountpoint_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_mountpoint_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_mountpoint_value"></a>
<a id="Return_value_items_properties_anyOf_i0_mountpoint_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_mountpoint_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_nbmand"></a>
<a id="Return_value_items_properties_anyOf_i0_nbmand"></a>
###### nbmand

- Schema name: `Nbmand`
- Type: object

Controls non-blocking mandatory locking behavior.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_nbmand_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_nbmand_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_nbmand_source"></a>
<a id="Return_value_items_properties_anyOf_i0_nbmand_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_nbmand_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_nbmand_value"></a>
<a id="Return_value_items_properties_anyOf_i0_nbmand_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_nbmand_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_nbmand_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_normalization"></a>
<a id="Return_value_items_properties_anyOf_i0_normalization"></a>
###### normalization

- Schema name: `Normalization`
- Type: object

Unicode normalization property for filenames.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_normalization_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_normalization_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_normalization_source"></a>
<a id="Return_value_items_properties_anyOf_i0_normalization_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_normalization_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_normalization_value"></a>
<a id="Return_value_items_properties_anyOf_i0_normalization_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_normalization_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_normalization_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_overlay"></a>
<a id="Return_value_items_properties_anyOf_i0_overlay"></a>
###### overlay

- Schema name: `Overlay`
- Type: object

Controls overlay mount behavior.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_overlay_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_overlay_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_overlay_source"></a>
<a id="Return_value_items_properties_anyOf_i0_overlay_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_overlay_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_overlay_value"></a>
<a id="Return_value_items_properties_anyOf_i0_overlay_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_overlay_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_overlay_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_quota"></a>
<a id="Return_value_items_properties_anyOf_i0_quota"></a>
###### quota

- Schema name: `Quota`
- Type: object

Limits space consumed by dataset and descendants.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_quota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_quota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_quota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_quota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_quota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_quota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_quota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_quota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_quota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_quota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_quota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_recordsize"></a>
<a id="Return_value_items_properties_anyOf_i0_recordsize"></a>
###### recordsize

- Schema name: `Recordsize`
- Type: object

Maximum block size for files in this filesystem.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_recordsize_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_recordsize_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_recordsize_source"></a>
<a id="Return_value_items_properties_anyOf_i0_recordsize_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_recordsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_recordsize_value"></a>
<a id="Return_value_items_properties_anyOf_i0_recordsize_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_recordsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_recordsize_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_refquota"></a>
<a id="Return_value_items_properties_anyOf_i0_refquota"></a>
###### refquota

- Schema name: `Refquota`
- Type: object

Limits space consumed by dataset itself (no descendants).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_refquota_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_refquota_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_refquota_source"></a>
<a id="Return_value_items_properties_anyOf_i0_refquota_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_refquota_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_refquota_value"></a>
<a id="Return_value_items_properties_anyOf_i0_refquota_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_refquota_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_refquota_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_refreservation"></a>
<a id="Return_value_items_properties_anyOf_i0_refreservation"></a>
###### refreservation

- Schema name: `Refreservation`
- Type: object

Minimum space reserved for volume itself.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_refreservation_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_refreservation_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_refreservation_source"></a>
<a id="Return_value_items_properties_anyOf_i0_refreservation_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_refreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_refreservation_value"></a>
<a id="Return_value_items_properties_anyOf_i0_refreservation_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_refreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_refreservation_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_relatime"></a>
<a id="Return_value_items_properties_anyOf_i0_relatime"></a>
###### relatime

- Schema name: `Relatime`
- Type: object

Controls relative access time updates.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_relatime_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_relatime_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_relatime_source"></a>
<a id="Return_value_items_properties_anyOf_i0_relatime_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_relatime_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_relatime_value"></a>
<a id="Return_value_items_properties_anyOf_i0_relatime_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_relatime_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_relatime_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_setuid"></a>
<a id="Return_value_items_properties_anyOf_i0_setuid"></a>
###### setuid

- Schema name: `Setuid`
- Type: object

Controls setuid/setgid bit respect on executable files.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_setuid_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_setuid_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_setuid_source"></a>
<a id="Return_value_items_properties_anyOf_i0_setuid_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_setuid_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_setuid_value"></a>
<a id="Return_value_items_properties_anyOf_i0_setuid_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_setuid_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_setuid_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_sharenfs"></a>
<a id="Return_value_items_properties_anyOf_i0_sharenfs"></a>
###### sharenfs

- Schema name: `Sharenfs`
- Type: object

Controls NFS sharing options for the filesystem.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_sharenfs_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_sharenfs_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_sharenfs_source"></a>
<a id="Return_value_items_properties_anyOf_i0_sharenfs_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_sharenfs_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_sharenfs_value"></a>
<a id="Return_value_items_properties_anyOf_i0_sharenfs_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_sharenfs_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_sharesmb"></a>
<a id="Return_value_items_properties_anyOf_i0_sharesmb"></a>
###### sharesmb

- Schema name: `Sharesmb`
- Type: object

Controls SMB/CIFS sharing options for the filesystem.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_sharesmb_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_sharesmb_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_sharesmb_source"></a>
<a id="Return_value_items_properties_anyOf_i0_sharesmb_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_sharesmb_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_sharesmb_value"></a>
<a id="Return_value_items_properties_anyOf_i0_sharesmb_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_sharesmb_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapdir"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdir"></a>
###### snapdir

- Schema name: `Snapdir`
- Type: object

Controls snapshot directory visibility (hidden or visible).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_snapdir_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdir_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_snapdir_source"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdir_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_snapdir_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapdir_value"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdir_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_snapdir_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_snapdir_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_special_small_blocks"></a>
<a id="Return_value_items_properties_anyOf_i0_special_small_blocks"></a>
###### special_small_blocks

- Schema name: `Special Small Blocks`
- Type: object

Size threshold for storing blocks on special vdevs.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_special_small_blocks_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_special_small_blocks_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_special_small_blocks_source"></a>
<a id="Return_value_items_properties_anyOf_i0_special_small_blocks_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_special_small_blocks_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_special_small_blocks_value"></a>
<a id="Return_value_items_properties_anyOf_i0_special_small_blocks_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_special_small_blocks_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_utf8only"></a>
<a id="Return_value_items_properties_anyOf_i0_utf8only"></a>
###### utf8only

- Schema name: `Utf8Only`
- Type: object

Controls whether only UTF-8 filenames are allowed.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_utf8only_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_utf8only_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_utf8only_source"></a>
<a id="Return_value_items_properties_anyOf_i0_utf8only_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_utf8only_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_utf8only_value"></a>
<a id="Return_value_items_properties_anyOf_i0_utf8only_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_utf8only_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_utf8only_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_version"></a>
<a id="Return_value_items_properties_anyOf_i0_version"></a>
###### version

- Schema name: `Version`
- Type: object

(READ-ONLY): Filesystem version number.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_version_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_version_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_version_source"></a>
<a id="Return_value_items_properties_anyOf_i0_version_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_version_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_version_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_version_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_version_value"></a>
<a id="Return_value_items_properties_anyOf_i0_version_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_version_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_version_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volmode"></a>
<a id="Return_value_items_properties_anyOf_i0_volmode"></a>
###### volmode

- Schema name: `Volmode`
- Type: object

Controls volume mode (default, geom, dev, none).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_volmode_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_volmode_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_volmode_source"></a>
<a id="Return_value_items_properties_anyOf_i0_volmode_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_volmode_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volmode_value"></a>
<a id="Return_value_items_properties_anyOf_i0_volmode_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_volmode_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_volmode_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_vscan"></a>
<a id="Return_value_items_properties_anyOf_i0_vscan"></a>
###### vscan

- Schema name: `Vscan`
- Type: object

Controls virus scanning behavior.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_vscan_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_vscan_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_vscan_source"></a>
<a id="Return_value_items_properties_anyOf_i0_vscan_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_vscan_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_vscan_value"></a>
<a id="Return_value_items_properties_anyOf_i0_vscan_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_vscan_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_vscan_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_xattr"></a>
<a id="Return_value_items_properties_anyOf_i0_xattr"></a>
###### xattr

- Schema name: `Xattr`
- Type: object

Controls extended attribute behavior (on, off, sa, dir).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_xattr_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_xattr_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_xattr_source"></a>
<a id="Return_value_items_properties_anyOf_i0_xattr_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_xattr_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_xattr_value"></a>
<a id="Return_value_items_properties_anyOf_i0_xattr_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_xattr_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_xattr_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_zoned"></a>
<a id="Return_value_items_properties_anyOf_i0_zoned"></a>
###### zoned

- Schema name: `Zoned`
- Type: object

Controls whether filesystem is managed from a zone.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_zoned_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_zoned_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_zoned_source"></a>
<a id="Return_value_items_properties_anyOf_i0_zoned_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_zoned_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_zoned_value"></a>
<a id="Return_value_items_properties_anyOf_i0_zoned_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_zoned_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_zoned_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_available"></a>
<a id="Return_value_items_properties_anyOf_i0_available"></a>
###### available

- Schema name: `Available`
- Type: object

Amount of space available to dataset and its children.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_available_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_available_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_available_source"></a>
<a id="Return_value_items_properties_anyOf_i0_available_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_available_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_available_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_available_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_available_value"></a>
<a id="Return_value_items_properties_anyOf_i0_available_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_available_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_available_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_checksum"></a>
<a id="Return_value_items_properties_anyOf_i0_checksum"></a>
###### checksum

- Schema name: `Checksum`
- Type: object

Controls checksum algorithm used to verify data integrity.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_checksum_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_checksum_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_checksum_source"></a>
<a id="Return_value_items_properties_anyOf_i0_checksum_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_checksum_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_checksum_value"></a>
<a id="Return_value_items_properties_anyOf_i0_checksum_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_checksum_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_checksum_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_compression"></a>
<a id="Return_value_items_properties_anyOf_i0_compression"></a>
###### compression

- Schema name: `Compression`
- Type: object

Controls compression algorithm used for this dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_compression_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_compression_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_compression_source"></a>
<a id="Return_value_items_properties_anyOf_i0_compression_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_compression_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_compression_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_compression_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_compression_value"></a>
<a id="Return_value_items_properties_anyOf_i0_compression_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_compression_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_compression_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_compressratio"></a>
<a id="Return_value_items_properties_anyOf_i0_compressratio"></a>
###### compressratio

- Schema name: `Compressratio`
- Type: object

(READ-ONLY): Property showing achieved compression ratio.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_compressratio_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_compressratio_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_compressratio_source"></a>
<a id="Return_value_items_properties_anyOf_i0_compressratio_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_compressratio_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_compressratio_value"></a>
<a id="Return_value_items_properties_anyOf_i0_compressratio_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_compressratio_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_compressratio_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_context"></a>
<a id="Return_value_items_properties_anyOf_i0_context"></a>
###### context

- Schema name: `Context`
- Type: object

SELinux security context for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_context_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_context_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_context_source"></a>
<a id="Return_value_items_properties_anyOf_i0_context_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_context_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_context_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_context_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_context_value"></a>
<a id="Return_value_items_properties_anyOf_i0_context_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_context_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_context_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_copies"></a>
<a id="Return_value_items_properties_anyOf_i0_copies"></a>
###### copies

- Schema name: `Copies`
- Type: object

Controls number of copies of data stored (1, 2, or 3).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_copies_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_copies_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_copies_source"></a>
<a id="Return_value_items_properties_anyOf_i0_copies_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_copies_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_copies_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_copies_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_copies_value"></a>
<a id="Return_value_items_properties_anyOf_i0_copies_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_copies_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_copies_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_createtxg"></a>
<a id="Return_value_items_properties_anyOf_i0_createtxg"></a>
###### createtxg

- Schema name: `Createtxg`
- Type: object

(READ-ONLY): Transaction group when dataset was created.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_createtxg_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_createtxg_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_createtxg_source"></a>
<a id="Return_value_items_properties_anyOf_i0_createtxg_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_createtxg_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_createtxg_value"></a>
<a id="Return_value_items_properties_anyOf_i0_createtxg_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_createtxg_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_createtxg_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_creation"></a>
<a id="Return_value_items_properties_anyOf_i0_creation"></a>
###### creation

- Schema name: `Creation`
- Type: object

(READ-ONLY): Timestamp when dataset was created.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_creation_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_creation_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_creation_source"></a>
<a id="Return_value_items_properties_anyOf_i0_creation_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_creation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_creation_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_creation_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_creation_value"></a>
<a id="Return_value_items_properties_anyOf_i0_creation_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_creation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_creation_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_dedup"></a>
<a id="Return_value_items_properties_anyOf_i0_dedup"></a>
###### dedup

- Schema name: `Dedup`
- Type: object

Controls data deduplication for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_dedup_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_dedup_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_dedup_source"></a>
<a id="Return_value_items_properties_anyOf_i0_dedup_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_dedup_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_dedup_value"></a>
<a id="Return_value_items_properties_anyOf_i0_dedup_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_dedup_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_dedup_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defcontext"></a>
<a id="Return_value_items_properties_anyOf_i0_defcontext"></a>
###### defcontext

- Schema name: `Defcontext`
- Type: object

SELinux default security context for new files.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_defcontext_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_defcontext_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_defcontext_source"></a>
<a id="Return_value_items_properties_anyOf_i0_defcontext_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_defcontext_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_defcontext_value"></a>
<a id="Return_value_items_properties_anyOf_i0_defcontext_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_defcontext_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_defcontext_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_encryption"></a>
<a id="Return_value_items_properties_anyOf_i0_encryption"></a>
###### encryption

- Schema name: `Encryption`
- Type: object

Controls encryption cipher suite for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_encryption_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_encryption_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_encryption_source"></a>
<a id="Return_value_items_properties_anyOf_i0_encryption_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_encryption_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_encryption_value"></a>
<a id="Return_value_items_properties_anyOf_i0_encryption_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_encryption_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_encryption_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_encryptionroot"></a>
<a id="Return_value_items_properties_anyOf_i0_encryptionroot"></a>
###### encryptionroot

- Schema name: `Encryptionroot`
- Type: object

(READ-ONLY): Property showing encryption root dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_encryptionroot_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_encryptionroot_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_encryptionroot_source"></a>
<a id="Return_value_items_properties_anyOf_i0_encryptionroot_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_encryptionroot_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_encryptionroot_value"></a>
<a id="Return_value_items_properties_anyOf_i0_encryptionroot_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_encryptionroot_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_fscontext"></a>
<a id="Return_value_items_properties_anyOf_i0_fscontext"></a>
###### fscontext

- Schema name: `Fscontext`
- Type: object

SELinux filesystem security context.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_fscontext_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_fscontext_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_fscontext_source"></a>
<a id="Return_value_items_properties_anyOf_i0_fscontext_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_fscontext_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_fscontext_value"></a>
<a id="Return_value_items_properties_anyOf_i0_fscontext_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_fscontext_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_fscontext_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_guid"></a>
<a id="Return_value_items_properties_anyOf_i0_guid"></a>
###### guid

- Schema name: `Guid`
- Type: object

(READ-ONLY): Globally unique identifier for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_guid_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_guid_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_guid_source"></a>
<a id="Return_value_items_properties_anyOf_i0_guid_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_guid_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_guid_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_guid_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_guid_value"></a>
<a id="Return_value_items_properties_anyOf_i0_guid_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_guid_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_guid_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_keyformat"></a>
<a id="Return_value_items_properties_anyOf_i0_keyformat"></a>
###### keyformat

- Schema name: `Keyformat`
- Type: object

Encryption key format (raw, hex, or passphrase).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_keyformat_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_keyformat_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_keyformat_source"></a>
<a id="Return_value_items_properties_anyOf_i0_keyformat_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_keyformat_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_keyformat_value"></a>
<a id="Return_value_items_properties_anyOf_i0_keyformat_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_keyformat_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_keyformat_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_keylocation"></a>
<a id="Return_value_items_properties_anyOf_i0_keylocation"></a>
###### keylocation

- Schema name: `Keylocation`
- Type: object

Location where encryption key is stored.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_keylocation_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_keylocation_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_keylocation_source"></a>
<a id="Return_value_items_properties_anyOf_i0_keylocation_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_keylocation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_keylocation_value"></a>
<a id="Return_value_items_properties_anyOf_i0_keylocation_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_keylocation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_keylocation_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_keystatus"></a>
<a id="Return_value_items_properties_anyOf_i0_keystatus"></a>
###### keystatus

- Schema name: `Keystatus`
- Type: object

(READ-ONLY): Encryption key status (available/unavailable).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_keystatus_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_keystatus_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_keystatus_source"></a>
<a id="Return_value_items_properties_anyOf_i0_keystatus_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_keystatus_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_keystatus_value"></a>
<a id="Return_value_items_properties_anyOf_i0_keystatus_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_keystatus_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_keystatus_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_logbias"></a>
<a id="Return_value_items_properties_anyOf_i0_logbias"></a>
###### logbias

- Schema name: `Logbias`
- Type: object

Controls ZIL write behavior (latency or throughput).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_logbias_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_logbias_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_logbias_source"></a>
<a id="Return_value_items_properties_anyOf_i0_logbias_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_logbias_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_logbias_value"></a>
<a id="Return_value_items_properties_anyOf_i0_logbias_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_logbias_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_logbias_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_logicalreferenced"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalreferenced"></a>
###### logicalreferenced

- Schema name: `Logicalreferenced`
- Type: object

(READ-ONLY): Logical space referenced by dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_logicalreferenced_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalreferenced_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_logicalreferenced_source"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalreferenced_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_logicalreferenced_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_logicalreferenced_value"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalreferenced_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_logicalreferenced_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_logicalused"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalused"></a>
###### logicalused

- Schema name: `Logicalused`
- Type: object

(READ-ONLY): Logical space used by dataset and descendants.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_logicalused_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalused_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_logicalused_source"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalused_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_logicalused_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_logicalused_value"></a>
<a id="Return_value_items_properties_anyOf_i0_logicalused_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_logicalused_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_logicalused_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_mlslabel"></a>
<a id="Return_value_items_properties_anyOf_i0_mlslabel"></a>
###### mlslabel

- Schema name: `Mlslabel`
- Type: object

Multi-level security label for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_mlslabel_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_mlslabel_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_mlslabel_source"></a>
<a id="Return_value_items_properties_anyOf_i0_mlslabel_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_mlslabel_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_mlslabel_value"></a>
<a id="Return_value_items_properties_anyOf_i0_mlslabel_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_mlslabel_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_objsetid"></a>
<a id="Return_value_items_properties_anyOf_i0_objsetid"></a>
###### objsetid

- Schema name: `Objsetid`
- Type: object

(READ-ONLY): Object set identifier for the dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_objsetid_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_objsetid_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_objsetid_source"></a>
<a id="Return_value_items_properties_anyOf_i0_objsetid_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_objsetid_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_objsetid_value"></a>
<a id="Return_value_items_properties_anyOf_i0_objsetid_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_objsetid_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_objsetid_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_origin"></a>
<a id="Return_value_items_properties_anyOf_i0_origin"></a>
###### origin

- Schema name: `Origin`
- Type: object

(READ-ONLY): Snapshot this dataset was cloned from.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_origin_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_origin_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_origin_source"></a>
<a id="Return_value_items_properties_anyOf_i0_origin_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_origin_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_origin_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_origin_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_origin_value"></a>
<a id="Return_value_items_properties_anyOf_i0_origin_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_origin_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_origin_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_pbkdf2iters"></a>
<a id="Return_value_items_properties_anyOf_i0_pbkdf2iters"></a>
###### pbkdf2iters

- Schema name: `Pbkdf2Iters`
- Type: object

Number of PBKDF2 iterations for key derivation.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_pbkdf2iters_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_pbkdf2iters_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_pbkdf2iters_source"></a>
<a id="Return_value_items_properties_anyOf_i0_pbkdf2iters_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_pbkdf2iters_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_pbkdf2iters_value"></a>
<a id="Return_value_items_properties_anyOf_i0_pbkdf2iters_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_pbkdf2iters_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_prefetch"></a>
<a id="Return_value_items_properties_anyOf_i0_prefetch"></a>
###### prefetch

- Schema name: `Prefetch`
- Type: object

Controls prefetch behavior (all, metadata, or none).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_prefetch_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_prefetch_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_prefetch_source"></a>
<a id="Return_value_items_properties_anyOf_i0_prefetch_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_prefetch_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_prefetch_value"></a>
<a id="Return_value_items_properties_anyOf_i0_prefetch_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_prefetch_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_prefetch_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_primarycache"></a>
<a id="Return_value_items_properties_anyOf_i0_primarycache"></a>
###### primarycache

- Schema name: `Primarycache`
- Type: object

Controls primary cache usage (all, metadata, or none).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_primarycache_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_primarycache_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_primarycache_source"></a>
<a id="Return_value_items_properties_anyOf_i0_primarycache_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_primarycache_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_primarycache_value"></a>
<a id="Return_value_items_properties_anyOf_i0_primarycache_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_primarycache_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_primarycache_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_readonly"></a>
<a id="Return_value_items_properties_anyOf_i0_readonly"></a>
###### readonly

- Schema name: `Readonly`
- Type: object

Controls whether dataset can be modified.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_readonly_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_readonly_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_readonly_source"></a>
<a id="Return_value_items_properties_anyOf_i0_readonly_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_readonly_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_readonly_value"></a>
<a id="Return_value_items_properties_anyOf_i0_readonly_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_readonly_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_readonly_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_receive_resume_token"></a>
<a id="Return_value_items_properties_anyOf_i0_receive_resume_token"></a>
###### receive_resume_token

- Schema name: `Receive Resume Token`
- Type: object

(READ-ONLY): Token for resuming interrupted zfs receive.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_receive_resume_token_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_receive_resume_token_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_receive_resume_token_source"></a>
<a id="Return_value_items_properties_anyOf_i0_receive_resume_token_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_receive_resume_token_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_receive_resume_token_value"></a>
<a id="Return_value_items_properties_anyOf_i0_receive_resume_token_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_receive_resume_token_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_redact_snaps"></a>
<a id="Return_value_items_properties_anyOf_i0_redact_snaps"></a>
###### redact_snaps

- Schema name: `Redact Snaps`
- Type: object

(READ-ONLY): List of redaction snapshots.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_redact_snaps_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_redact_snaps_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_redact_snaps_source"></a>
<a id="Return_value_items_properties_anyOf_i0_redact_snaps_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_redact_snaps_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_redact_snaps_value"></a>
<a id="Return_value_items_properties_anyOf_i0_redact_snaps_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_redact_snaps_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_redundant_metadata"></a>
<a id="Return_value_items_properties_anyOf_i0_redundant_metadata"></a>
###### redundant_metadata

- Schema name: `Redundant Metadata`
- Type: object

Controls redundant metadata storage (all or most).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_redundant_metadata_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_redundant_metadata_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_redundant_metadata_source"></a>
<a id="Return_value_items_properties_anyOf_i0_redundant_metadata_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_redundant_metadata_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_redundant_metadata_value"></a>
<a id="Return_value_items_properties_anyOf_i0_redundant_metadata_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_redundant_metadata_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_refcompressratio"></a>
<a id="Return_value_items_properties_anyOf_i0_refcompressratio"></a>
###### refcompressratio

- Schema name: `Refcompressratio`
- Type: object

(READ-ONLY): Compression ratio for referenced data.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_refcompressratio_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_refcompressratio_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_refcompressratio_source"></a>
<a id="Return_value_items_properties_anyOf_i0_refcompressratio_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_refcompressratio_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_refcompressratio_value"></a>
<a id="Return_value_items_properties_anyOf_i0_refcompressratio_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_refcompressratio_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_referenced"></a>
<a id="Return_value_items_properties_anyOf_i0_referenced"></a>
###### referenced

- Schema name: `Referenced`
- Type: object

(READ-ONLY): Space referenced by this dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_referenced_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_referenced_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_referenced_source"></a>
<a id="Return_value_items_properties_anyOf_i0_referenced_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_referenced_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_referenced_value"></a>
<a id="Return_value_items_properties_anyOf_i0_referenced_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_referenced_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_referenced_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_reservation"></a>
<a id="Return_value_items_properties_anyOf_i0_reservation"></a>
###### reservation

- Schema name: `Reservation`
- Type: object

Minimum space reserved for dataset and descendants.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_reservation_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_reservation_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_reservation_source"></a>
<a id="Return_value_items_properties_anyOf_i0_reservation_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_reservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_reservation_value"></a>
<a id="Return_value_items_properties_anyOf_i0_reservation_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_reservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_reservation_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_rootcontext"></a>
<a id="Return_value_items_properties_anyOf_i0_rootcontext"></a>
###### rootcontext

- Schema name: `Rootcontext`
- Type: object

SELinux root directory security context.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_rootcontext_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_rootcontext_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_rootcontext_source"></a>
<a id="Return_value_items_properties_anyOf_i0_rootcontext_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_rootcontext_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_rootcontext_value"></a>
<a id="Return_value_items_properties_anyOf_i0_rootcontext_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_rootcontext_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_secondarycache"></a>
<a id="Return_value_items_properties_anyOf_i0_secondarycache"></a>
###### secondarycache

- Schema name: `Secondarycache`
- Type: object

Controls secondary cache usage (all, metadata, or none).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_secondarycache_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_secondarycache_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_secondarycache_source"></a>
<a id="Return_value_items_properties_anyOf_i0_secondarycache_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_secondarycache_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_secondarycache_value"></a>
<a id="Return_value_items_properties_anyOf_i0_secondarycache_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_secondarycache_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapdev"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdev"></a>
###### snapdev

- Schema name: `Snapdev`
- Type: object

Controls snapshot device visibility (hidden or visible).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_snapdev_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdev_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_snapdev_source"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdev_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_snapdev_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapdev_value"></a>
<a id="Return_value_items_properties_anyOf_i0_snapdev_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_snapdev_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_snapdev_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_count"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_count"></a>
###### snapshot_count

- Schema name: `Snapshot Count`
- Type: object

(READ-ONLY): Count of snapshots in this dataset.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_count_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_count_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_count_source"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_count_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_snapshot_count_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_count_value"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_count_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_count_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_limit"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_limit"></a>
###### snapshot_limit

- Schema name: `Snapshot Limit`
- Type: object

Maximum number of snapshots allowed.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_limit_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_limit_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_limit_source"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_limit_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_snapshot_limit_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapshot_limit_value"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshot_limit_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_snapshot_limit_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapshots_changed"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshots_changed"></a>
###### snapshots_changed

- Schema name: `Snapshots Changed`
- Type: object

(READ-ONLY): Property indicating snapshot changes.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_snapshots_changed_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshots_changed_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_snapshots_changed_source"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshots_changed_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_snapshots_changed_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_snapshots_changed_value"></a>
<a id="Return_value_items_properties_anyOf_i0_snapshots_changed_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_snapshots_changed_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_sync"></a>
<a id="Return_value_items_properties_anyOf_i0_sync"></a>
###### sync

- Schema name: `Sync`
- Type: object

Controls synchronous write behavior (standard, always, disabled).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_sync_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_sync_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_sync_source"></a>
<a id="Return_value_items_properties_anyOf_i0_sync_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_sync_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_sync_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_sync_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_sync_value"></a>
<a id="Return_value_items_properties_anyOf_i0_sync_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_sync_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_sync_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_type"></a>
<a id="Return_value_items_properties_anyOf_i0_type"></a>
###### type

- Schema name: `Type`

(READ-ONLY): Type of ZFS dataset (filesystem, volume, etc).
<a id="Return_value_items_properties_anyOf_i0_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0"></a>
###### [PropertyValue](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0)

- Schema name: `PropertyValue`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_type_anyOf_i0_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_type_anyOf_i0_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_type_anyOf_i0_source"></a>
<a id="Return_value_items_properties_anyOf_i0_type_anyOf_i0_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_type_anyOf_i0_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_type_anyOf_i0_value"></a>
<a id="Return_value_items_properties_anyOf_i0_type_anyOf_i0_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i0_value_anyOf_i4)

- Type: null

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_used"></a>
<a id="Return_value_items_properties_anyOf_i0_used"></a>
###### used

- Schema name: `Used`
- Type: object

(READ-ONLY): Space used by dataset and descendants.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_used_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_used_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_used_source"></a>
<a id="Return_value_items_properties_anyOf_i0_used_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_used_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_used_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_used_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_used_value"></a>
<a id="Return_value_items_properties_anyOf_i0_used_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_used_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_used_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbychildren"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbychildren"></a>
###### usedbychildren

- Schema name: `Usedbychildren`
- Type: object

(READ-ONLY): Space used by child datasets.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_usedbychildren_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbychildren_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_usedbychildren_source"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbychildren_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_usedbychildren_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbychildren_value"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbychildren_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_usedbychildren_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbydataset"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbydataset"></a>
###### usedbydataset

- Schema name: `Usedbydataset`
- Type: object

(READ-ONLY): Space used by this dataset itself.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_usedbydataset_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbydataset_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_usedbydataset_source"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbydataset_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_usedbydataset_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbydataset_value"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbydataset_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_usedbydataset_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbyrefreservation"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbyrefreservation"></a>
###### usedbyrefreservation

- Schema name: `Usedbyrefreservation`
- Type: object

(READ-ONLY): Space used by refreservation.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_usedbyrefreservation_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbyrefreservation_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_usedbyrefreservation_source"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbyrefreservation_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_usedbyrefreservation_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbyrefreservation_value"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbyrefreservation_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_usedbyrefreservation_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbysnapshots"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbysnapshots"></a>
###### usedbysnapshots

- Schema name: `Usedbysnapshots`
- Type: object

(READ-ONLY): Space used by snapshots.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_usedbysnapshots_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbysnapshots_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_usedbysnapshots_source"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbysnapshots_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_usedbysnapshots_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_usedbysnapshots_value"></a>
<a id="Return_value_items_properties_anyOf_i0_usedbysnapshots_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_usedbysnapshots_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_written"></a>
<a id="Return_value_items_properties_anyOf_i0_written"></a>
###### written

- Schema name: `Written`
- Type: object

(READ-ONLY): Space referenced since previous snapshot.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_written_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_written_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_written_source"></a>
<a id="Return_value_items_properties_anyOf_i0_written_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_written_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_written_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_written_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_written_value"></a>
<a id="Return_value_items_properties_anyOf_i0_written_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_written_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_written_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volblocksize"></a>
<a id="Return_value_items_properties_anyOf_i0_volblocksize"></a>
###### volblocksize

- Schema name: `Volblocksize`
- Type: object

Block size for volume (typically 8K or 16K).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_volblocksize_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_volblocksize_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_volblocksize_source"></a>
<a id="Return_value_items_properties_anyOf_i0_volblocksize_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_volblocksize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volblocksize_value"></a>
<a id="Return_value_items_properties_anyOf_i0_volblocksize_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_volblocksize_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volsize"></a>
<a id="Return_value_items_properties_anyOf_i0_volsize"></a>
###### volsize

- Schema name: `Volsize`
- Type: object

Logical size of the volume.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_volsize_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_volsize_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_volsize_source"></a>
<a id="Return_value_items_properties_anyOf_i0_volsize_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_volsize_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volsize_value"></a>
<a id="Return_value_items_properties_anyOf_i0_volsize_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_volsize_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_volsize_value_anyOf_i4)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volthreading"></a>
<a id="Return_value_items_properties_anyOf_i0_volthreading"></a>
###### volthreading

- Schema name: `Volthreading`
- Type: object

Controls volume threading behavior.
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_volthreading_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_volthreading_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_volthreading_source"></a>
<a id="Return_value_items_properties_anyOf_i0_volthreading_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_volthreading_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_source_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_source_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_volthreading_value"></a>
<a id="Return_value_items_properties_anyOf_i0_volthreading_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_volthreading_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_volthreading_value_anyOf_i4)

- Type: null

<a id="tab-pane_Return_value_items_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_type"></a>
<a id="Return_value_items_type"></a>
##### type (required)

- Schema name: `Type`
- Type: enum (of string)

The type of ZFS resource.
###### Must be one of:

- "FILESYSTEM"
- "VOLUME"

<a id="headingReturn_value_items_user_properties"></a>
<a id="Return_value_items_user_properties"></a>
##### user_properties (required)

- Schema name: `User Properties`

Custom metadata properties with colon-separated names (max 256 chars).
<a id="Return_value_items_user_properties_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_user_properties_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_user_properties_anyOf_i0)

- Type: object
<a id="headingReturn_value_items_user_properties_anyOf_i0_additionalProperties"></a>
<a id="Return_value_items_user_properties_anyOf_i0_additionalProperties"></a>
###### Additional Properties

Each additional property must conform to the following schema
- Type: string

<a id="tab-pane_Return_value_items_user_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_user_properties_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_children"></a>
<a id="Return_value_items_children"></a>
##### children (required)

- Schema name: `Children`

The children of this zfs resource.
<a id="Return_value_items_children_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_children_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_children_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_children_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_items_children_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_children_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_tier"></a>
<a id="Return_value_items_tier"></a>
##### tier

- Default: null

Tier classification for FILESYSTEM resources. None if not requested, not applicable, or deduplication is enabled on the dataset.
<a id="Return_value_items_tier_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_tier_anyOf_i0"></a>
###### [TierInfo](#tab-pane_Return_value_items_tier_anyOf_i0)

- Schema name: `TierInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_tier_anyOf_i0_tier_type"></a>
<a id="Return_value_items_tier_anyOf_i0_tier_type"></a>
###### tier_type (required)

- Schema name: `Tier Type`
- Type: enum (of string)

Storage performance tier for this share.
###### Must be one of:

- "REGULAR"
- "PERFORMANCE"

<a id="headingReturn_value_items_tier_anyOf_i0_tier_job"></a>
<a id="Return_value_items_tier_anyOf_i0_tier_job"></a>
###### tier_job

- Default: null

Most recent rewrite job for this share's dataset, or `null` if no job history exists.
<a id="Return_value_items_tier_anyOf_i0_tier_job_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_tier_anyOf_i0_tier_job_anyOf_i0"></a>
###### [ZfsTierRewriteJobEntry](#tab-pane_Return_value_items_tier_anyOf_i0_tier_job_anyOf_i0)

- Schema name: `ZfsTierRewriteJobEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
<a id="Return_value_items_tier_anyOf_i0_tier_job_anyOf_i0_tier_job_id"></a>
###### tier_job_id (required)

- Schema name: `Tier Job Id`
- Type: string

Rewrite job identifier in `dataset_name@job_uuid` format.
- Must be at least `1` characters long

<a id="headingReturn_value_items_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
<a id="Return_value_items_tier_anyOf_i0_tier_job_anyOf_i0_dataset_name"></a>
###### dataset_name (required)

- Schema name: `Dataset Name`
- Type: string

ZFS dataset this job is operating on.
- Must be at least `1` characters long

<a id="headingReturn_value_items_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
<a id="Return_value_items_tier_anyOf_i0_tier_job_anyOf_i0_job_uuid"></a>
###### job_uuid (required)

- Schema name: `Job Uuid`
- Type: string

Unique identifier for this rewrite job.
- Must be at least `1` characters long

<a id="headingReturn_value_items_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
<a id="Return_value_items_tier_anyOf_i0_tier_job_anyOf_i0_status"></a>
###### status (required)

- Schema name: `Status`
- Type: enum (of string)

Current lifecycle state of the job. `COMPLETE` - All files in the dataset have been processed. `RUNNING` - Job is actively processing files. `QUEUED` - Job is waiting for a free execution slot (see `max_concurrent_jobs`). `CANCELLED` - Job was stopped via `zfs_tier_job.cancel`. Not resumable. `STOPPED` - Job was RUNNING but its process is no longer active (e.g. daemon restart). This state is computed on read and is never written to persistent storage. `ERROR` - Job halted due to an unrecoverable error. Use `zfs_tier_job.recover` to retry failed files.
###### Must be one of:

- "COMPLETE"
- "RUNNING"
- "QUEUED"
- "CANCELLED"
- "STOPPED"
- "ERROR"

<a id="tab-pane_Return_value_items_tier_anyOf_i0_tier_job_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_tier_anyOf_i0_tier_job_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_items_tier_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_tier_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../shared/query_methods.md)
