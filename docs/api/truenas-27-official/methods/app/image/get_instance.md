---
title: app.image.get_instance
kind: method
source_rst: _sources/api_methods_app.image.get_instance.rst.txt
source_html: api_methods_app.image.get_instance.html
required_roles:
  - APPS_READ
---

# app.image.get_instance

## Summary

Returns instance matching `id_`. Raises InstanceNotFound if missing.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

<a id="Call_parameters_items_i0"></a>
#### id

- Schema name: `id`
- Type: string

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object

Query options customize the results returned by a query method. More complete documentation with examples are covered in the "Query methods" section of the TrueNAS API documentation.
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

- Schema name: `AppImageEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container image (usually SHA256 hash).
- Must be at least `1` characters long

<a id="headingReturn_value_repo_tags"></a>
<a id="Return_value_repo_tags"></a>
#### repo_tags (required)

- Schema name: `Repo Tags`
- Type: array of string

Array of repository tags associated with this image.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_repo_tags_items"></a>
- Type: string

<a id="headingReturn_value_repo_digests"></a>
<a id="Return_value_repo_digests"></a>
#### repo_digests (required)

- Schema name: `Repo Digests`
- Type: array of string

Array of repository digests (content-addressable identifiers) for this image.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_repo_digests_items"></a>
- Type: string

<a id="headingReturn_value_size"></a>
<a id="Return_value_size"></a>
#### size (required)

- Schema name: `Size`
- Type: integer

Size of the container image in bytes.

<a id="headingReturn_value_dangling"></a>
<a id="Return_value_dangling"></a>
#### dangling (required)

- Schema name: `Dangling`
- Type: boolean

Whether this is a dangling image (no tags or references).

<a id="headingReturn_value_update_available"></a>
<a id="Return_value_update_available"></a>
#### update_available (required)

- Schema name: `Update Available`
- Type: boolean

Whether a newer version of this image is available for download.

<a id="headingReturn_value_created"></a>
<a id="Return_value_created"></a>
#### created (required)

- Schema name: `Created`

Timestamp when the container image was created (ISO format) or `null` if not available.
<a id="Return_value_created_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_created_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_created_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_created_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_created_anyOf_i1)

- Type: null

<a id="headingReturn_value_author"></a>
<a id="Return_value_author"></a>
#### author (required)

- Schema name: `Author`

Author or maintainer of the container image or `null` if not specified.
<a id="Return_value_author_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_author_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_author_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_author_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_author_anyOf_i1)

- Type: null

<a id="headingReturn_value_comment"></a>
<a id="Return_value_comment"></a>
#### comment (required)

- Schema name: `Comment`

Comment or description provided by the image author or `null` if not provided.
<a id="Return_value_comment_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_comment_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_comment_anyOf_i0)

- Type: string
- Must be at most `2147483647` characters long

<a id="tab-pane_Return_value_comment_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_comment_anyOf_i1)

- Type: null

<a id="headingReturn_value_parsed_repo_tags"></a>
<a id="Return_value_parsed_repo_tags"></a>
#### parsed_repo_tags

- Schema name: `Parsed Repo Tags`
- Default: null

Parsed repository tag information or `null` if not available.
<a id="Return_value_parsed_repo_tags_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_parsed_repo_tags_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_parsed_repo_tags_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_parsed_repo_tags_anyOf_i0_items"></a>
###### AppImageParsedRepoTags

- Schema name: `AppImageParsedRepoTags`
- Type: object
- No Additional Properties
<a id="headingReturn_value_parsed_repo_tags_anyOf_i0_items_reference"></a>
<a id="Return_value_parsed_repo_tags_anyOf_i0_items_reference"></a>
###### reference (required)

- Schema name: `Reference`
- Type: string

Full reference to the container image (registry/repository:tag).

<a id="headingReturn_value_parsed_repo_tags_anyOf_i0_items_image"></a>
<a id="Return_value_parsed_repo_tags_anyOf_i0_items_image"></a>
###### image (required)

- Schema name: `Image`
- Type: string

Container image name without registry or tag.

<a id="headingReturn_value_parsed_repo_tags_anyOf_i0_items_tag"></a>
<a id="Return_value_parsed_repo_tags_anyOf_i0_items_tag"></a>
###### tag (required)

- Schema name: `Tag`
- Type: string

Image tag (version) or digest identifier.

<a id="headingReturn_value_parsed_repo_tags_anyOf_i0_items_registry"></a>
<a id="Return_value_parsed_repo_tags_anyOf_i0_items_registry"></a>
###### registry (required)

- Schema name: `Registry`
- Type: string

Container registry hostname (e.g., docker.io, quay.io).

<a id="headingReturn_value_parsed_repo_tags_anyOf_i0_items_complete_tag"></a>
<a id="Return_value_parsed_repo_tags_anyOf_i0_items_complete_tag"></a>
###### complete_tag (required)

- Schema name: `Complete Tag`
- Type: string

Complete image reference including registry, image name, and tag.

<a id="headingReturn_value_parsed_repo_tags_anyOf_i0_items_reference_is_digest"></a>
<a id="Return_value_parsed_repo_tags_anyOf_i0_items_reference_is_digest"></a>
###### reference_is_digest (required)

- Schema name: `Reference Is Digest`
- Type: boolean

Whether the reference uses a digest hash instead of a tag name.

<a id="tab-pane_Return_value_parsed_repo_tags_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_parsed_repo_tags_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
