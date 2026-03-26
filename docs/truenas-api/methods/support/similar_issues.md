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

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: query

#### query

- Schema name: `query`
- Type: string

Search query to find similar issues or knowledge base articles.

### Return value

- Schema name: `Result`
- Type: array of object

Array of similar issues found based on the search query.
- No Additional Items

#### Each item of this array must be:

#### SupportSimilarIssue

- Schema name: `SupportSimilarIssue`
- Type: object
##### url

- Schema name: `Url`
- Type: string

URL link to the similar issue or knowledge base article.

##### summary

- Schema name: `Summary`
- Type: string

Brief summary of the similar issue.

##### Additional Properties

Additional Properties of any type are allowed.
- Type: object

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
