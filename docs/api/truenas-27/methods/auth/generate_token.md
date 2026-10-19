---
title: auth.generate_token
kind: method
source_rst: _sources/api_methods_auth.generate_token.rst.txt
source_html: api_methods_auth.generate_token.html
required_roles:
  []
---

# auth.generate_token

## Summary

Generate a token to be used for authentication.

`ttl` stands for Time To Live, in seconds. The token will be invalidated if the connection has been inactive for a time greater than this.

`attrs` is a general purpose object/dictionary to hold information about the token.

`match_origin` will only allow using this token from the same IP address or with the same user UID.

NOTE: this endpoint is not supported when server security requires replay-resistant authentication as part of GPOS STIG requirements.

## Required Roles

- None documented.

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: ttl

<a id="Call_parameters_items_i0"></a>
#### ttl

- Schema name: `ttl`
- Default: 600

Time-to-live for the token in seconds or `null` for no expiration (default 600).
<a id="Call_parameters_items_i0_anyOf"></a>
##### Any of

<a id="tab-pane_Call_parameters_items_i0_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i0_anyOf_i0)

- Type: integer

<a id="tab-pane_Call_parameters_items_i0_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i0_anyOf_i1)

- Type: null

#### Parameter 2: attrs

<a id="Call_parameters_items_i1"></a>
#### attrs

- Schema name: `attrs`
- Type: object
- Default: {}

Additional attributes to embed in the token.

#### Parameter 3: match_origin

<a id="Call_parameters_items_i2"></a>
#### match_origin

- Schema name: `match_origin`
- Type: boolean
- Default: true

Whether the token must be used from the same origin that created it.

#### Parameter 4: single_use

<a id="Call_parameters_items_i3"></a>
#### single_use

- Schema name: `single_use`
- Type: boolean
- Default: false

Whether the token can only be used once.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: string

Generated authentication token.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
