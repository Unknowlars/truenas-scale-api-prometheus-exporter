---
title: zfs.resource.snapshot.query
kind: method
source_rst: _sources/api_methods_zfs.resource.snapshot.query.rst.txt
source_html: api_methods_zfs.resource.snapshot.query.html
required_roles:
  - SNAPSHOT_READ
---

# zfs.resource.snapshot.query

## Summary

This method provides an interface for retrieving information about ZFS snapshots, including their properties and user properties.

Args: data: Query parameters containing: - paths: List of dataset or snapshot paths to query. If empty, queries all. - properties: List of ZFS properties to retrieve. Empty list = defaults, None = none. - get_user_properties: Whether to include user-defined properties. - get_source: Whether to include property source information. - recursive: Include snapshots from child datasets. - min_txg: Minimum transaction group filter (0 = no minimum). - max_txg: Maximum transaction group filter (0 = no maximum).

Returns: List of snapshot entries with requested properties.

Examples: # Query all snapshots query({})

# Query snapshots for a specific dataset query({"paths": ["tank/data"]})

# Query a specific snapshot query({"paths": ["tank/data@backup"]})

# Query with recursion and specific properties query({ "paths": ["tank"], "recursive": True, "properties": ["used", "referenced", "creation"] })

## Required Roles

- `SNAPSHOT_READ`

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
  "recursive": false,
  "properties": [],
  "get_user_properties": false,
  "get_source": false,
  "get_holds": false,
  "min_txg": 0,
  "max_txg": 0
}
```

Query parameters for retrieving ZFS snapshot information.
- No Additional Properties
<a id="headingCall_parameters_items_i0_paths"></a>
<a id="Call_parameters_items_i0_paths"></a>
##### paths

- Schema name: `Paths`
- Type: array of string
- Default: []

Dataset paths to count snapshots for. If empty, counts all snapshots.
- All items must be unique
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i0_paths_items"></a>
- Type: string

<a id="headingCall_parameters_items_i0_recursive"></a>
<a id="Call_parameters_items_i0_recursive"></a>
##### recursive

- Schema name: `Recursive`
- Type: boolean
- Default: false

Include snapshots from child datasets when counting.

<a id="headingCall_parameters_items_i0_properties"></a>
<a id="Call_parameters_items_i0_properties"></a>
##### properties

- Schema name: `Properties`
- Default: []

List of ZFS properties to retrieve. Empty list returns default properties. None returns no properties.
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

Retrieve user-defined properties for snapshots.

<a id="headingCall_parameters_items_i0_get_source"></a>
<a id="Call_parameters_items_i0_get_source"></a>
##### get_source

- Schema name: `Get Source`
- Type: boolean
- Default: false

Include source information for each property value.

<a id="headingCall_parameters_items_i0_get_holds"></a>
<a id="Call_parameters_items_i0_get_holds"></a>
##### get_holds

- Schema name: `Get Holds`
- Type: boolean
- Default: false

Include holds information (if any) for the snapshot.

<a id="headingCall_parameters_items_i0_min_txg"></a>
<a id="Call_parameters_items_i0_min_txg"></a>
##### min_txg

- Schema name: `Min Txg`
- Type: integer
- Default: 0

Minimum transaction group for filtering snapshots. 0 means no minimum.

<a id="headingCall_parameters_items_i0_max_txg"></a>
<a id="Call_parameters_items_i0_max_txg"></a>
##### max_txg

- Schema name: `Max Txg`
- Type: integer
- Default: 0

Maximum transaction group for filtering snapshots. 0 means no maximum.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### ZFSResourceSnapshotEntry

- Schema name: `ZFSResourceSnapshotEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_createtxg"></a>
<a id="Return_value_items_createtxg"></a>
##### createtxg (required)

- Schema name: `Createtxg`
- Type: integer

The TXG in which the snapshot was created.

<a id="headingReturn_value_items_guid"></a>
<a id="Return_value_items_guid"></a>
##### guid (required)

- Schema name: `Guid`
- Type: integer

A GUID for the snapshot.

<a id="headingReturn_value_items_name"></a>
<a id="Return_value_items_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

The zfs resource for the given snapshot.

<a id="headingReturn_value_items_pool"></a>
<a id="Return_value_items_pool"></a>
##### pool (required)

- Schema name: `Pool`
- Type: string

The zpool of the snapshot.

<a id="headingReturn_value_items_dataset"></a>
<a id="Return_value_items_dataset"></a>
##### dataset (required)

- Schema name: `Dataset`
- Type: string

The zfs resource for the given snapshot.

<a id="headingReturn_value_items_snapshot_name"></a>
<a id="Return_value_items_snapshot_name"></a>
##### snapshot_name (required)

- Schema name: `Snapshot Name`
- Type: string

The name of the snapshot.

<a id="headingReturn_value_items_type"></a>
<a id="Return_value_items_type"></a>
##### type

- Schema name: `Type`
- Type: const
- Default: "SNAPSHOT"

The type of zfs resource.
- Specific value: `"SNAPSHOT"`

<a id="headingReturn_value_items_holds"></a>
<a id="Return_value_items_holds"></a>
##### holds (required)

- Schema name: `Holds`

A list of tags that hold the snapshot.
<a id="Return_value_items_holds_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_holds_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_holds_anyOf_i0)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_items_holds_anyOf_i0_items"></a>
- Type: object

<a id="tab-pane_Return_value_items_holds_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_holds_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties"></a>
<a id="Return_value_items_properties"></a>
##### properties (required)

Requested properties for the snapshot.
<a id="Return_value_items_properties_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0"></a>
###### [ZFSResourceSnapshotPropertiesEntry](#tab-pane_Return_value_items_properties_anyOf_i0)

- Schema name: `ZFSResourceSnapshotPropertiesEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_type"></a>
<a id="Return_value_items_properties_anyOf_i0_type"></a>
###### type

- Schema name: `Type`
- Type: object

(READ-ONLY): Type of ZFS dataset (filesystem, volume, etc).
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_type_raw"></a>
<a id="Return_value_items_properties_anyOf_i0_type_raw"></a>
###### raw (required)

- Schema name: `Raw`
- Type: string

The raw value of the property.

<a id="headingReturn_value_items_properties_anyOf_i0_type_source"></a>
<a id="Return_value_items_properties_anyOf_i0_type_source"></a>
###### source (required)

The source from where this property received its value.
<a id="Return_value_items_properties_anyOf_i0_type_source_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i0"></a>
###### [SourceValue](#tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i0)

- Schema name: `SourceValue`
- Type: object
- No Additional Properties
<a id="headingReturn_value_items_properties_anyOf_i0_type_source_anyOf_i0_type"></a>
<a id="Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_type"></a>
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

<a id="headingReturn_value_items_properties_anyOf_i0_type_source_anyOf_i0_value"></a>
<a id="Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_value"></a>
###### value (required)

- Schema name: `Value`

The source value.
<a id="Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_value_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i0_value_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_type_source_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_properties_anyOf_i0_type_value"></a>
<a id="Return_value_items_properties_anyOf_i0_type_value"></a>
###### value (required)

- Schema name: `Value`

The parsed raw value of the property.
<a id="Return_value_items_properties_anyOf_i0_type_value_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i1)

- Type: number

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i2"></a>
###### [Option 3](#tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i2)

- Type: string

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i3"></a>
###### [Option 4](#tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i3)

- Type: boolean

<a id="tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i4"></a>
###### [Option 5](#tab-pane_Return_value_items_properties_anyOf_i0_type_value_anyOf_i4)

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

<a id="tab-pane_Return_value_items_properties_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_items_properties_anyOf_i1)

- Type: null

<a id="headingReturn_value_items_user_properties"></a>
<a id="Return_value_items_user_properties"></a>
##### user_properties (required)

- Schema name: `User Properties`

User-defined properties for snapshots.
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

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../../../shared/query_methods.md)
