---
title: support.similar_issues
kind: method
source_rst: _sources/api_methods_support.similar_issues.rst.txt
source_html: api_methods_support.similar_issues.html
required_roles:
  - SUPPORT_READ
---

# support.similar_issues

## Required Roles

- `SUPPORT_READ`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: query

<a id="Call_parameters_items_i0"></a>
#### query

- Schema name: `query`
- Type: string

Search query to find similar issues or knowledge base articles.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: array of object

Array of similar issues found based on the search query.
- No Additional Items

#### Each item of this array must be:

<a id="Return_value_items"></a>
#### SupportSimilarIssue

- Schema name: `SupportSimilarIssue`
- Type: object
<a id="headingReturn_value_items_url"></a>
<a id="Return_value_items_url"></a>
##### url

- Schema name: `Url`
- Type: string

URL link to the similar issue or knowledge base article.

<a id="headingReturn_value_items_summary"></a>
<a id="Return_value_items_summary"></a>
##### summary

- Schema name: `Summary`
- Type: string

Brief summary of the similar issue.

<a id="headingReturn_value_items_additionalProperties"></a>
<a id="Return_value_items_additionalProperties"></a>
##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
