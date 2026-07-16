---
title: auth.set_attribute
kind: method
source_rst: _sources/api_methods_auth.set_attribute.rst.txt
source_html: api_methods_auth.set_attribute.html
required_roles:
  []
---

# auth.set_attribute

## Summary

Set current user's `attributes` dictionary `key` to `value`.

e.g. Setting `key="foo"` `value="var"` will result in `{"attributes": {"foo": "bar"}}`.

Attributes set here will appear in the :doc:`auth.me <api_methods_auth.me>` response under the `attributes` field.

.. important::

This endpoint exists solely for the use of the TrueNAS UX team. The data stored in these attributes *must* be considered opaque from the perspective of the middleware backend, with specific documented exceptions. This endpoint should not be used or relied on by any third-party scripts or workflows.

.. warning::

This endpoint is not intended for storing security-sensitive information. The backend storage for this data is not encrypted, and it is indexed by unix user id rather than database ID which exposes a risk of stale settings being reused if a new user gets assigned the same unix user id as a previously-existing one. This is of particular concern when users are provided by directory services.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: key

#### key

- Schema name: `key`
- Type: string

Attribute key name.

#### Parameter 2: value

#### value

- Schema name: `value`
- Type: object

Attribute value to set.

### Return value

- Schema name: `Result`
- Type: null

Returns `null` when the attribute is successfully set.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
