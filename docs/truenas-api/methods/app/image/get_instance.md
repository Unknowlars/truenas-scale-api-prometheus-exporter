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

Returns instance matching `id`. If `id` is not found, Validation error is raised.

Please see `query` method documentation for `options`.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: id

#### id

- Schema name: `id`
- Type: string

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

- Schema name: `AppImageEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container image (usually SHA256 hash).
- Must be at least `1` characters long

#### repo_tags (required)

- Schema name: `Repo Tags`
- Type: array of string

Array of repository tags associated with this image.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### repo_digests (required)

- Schema name: `Repo Digests`
- Type: array of string

Array of repository digests (content-addressable identifiers) for this image.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### size (required)

- Schema name: `Size`
- Type: integer

Size of the container image in bytes.

#### dangling (required)

- Schema name: `Dangling`
- Type: boolean

Whether this is a dangling image (no tags or references).

#### update_available (required)

- Schema name: `Update Available`
- Type: boolean

Whether a newer version of this image is available for download.

#### created (required)

- Schema name: `Created`
- Type: string

Timestamp when the container image was created (ISO format).

#### author (required)

- Schema name: `Author`
- Type: string

Author or maintainer of the container image.

#### comment (required)

- Schema name: `Comment`
- Type: string

Comment or description provided by the image author.

#### parsed_repo_tags

- Schema name: `Parsed Repo Tags`
- Default: null

Parsed repository tag information or `null` if not available.
##### Any of

###### Option 1

- Type: array of object
- No Additional Items

####### Each item of this array must be:

####### AppImageParsedRepoTags

- Schema name: `AppImageParsedRepoTags`
- Type: object
- No Additional Properties
######## reference (required)

- Schema name: `Reference`
- Type: string

Full reference to the container image (registry/repository:tag).

######## image (required)

- Schema name: `Image`
- Type: string

Container image name without registry or tag.

######## tag (required)

- Schema name: `Tag`
- Type: string

Image tag (version) or digest identifier.

######## registry (required)

- Schema name: `Registry`
- Type: string

Container registry hostname (e.g., docker.io, quay.io).

######## complete_tag (required)

- Schema name: `Complete Tag`
- Type: string

Complete image reference including registry, image name, and tag.

######## reference_is_digest (required)

- Schema name: `Reference Is Digest`
- Type: boolean

Whether the reference uses a digest hash instead of a tag name.

###### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
