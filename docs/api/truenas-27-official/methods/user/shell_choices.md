---
title: user.shell_choices
kind: method
source_rst: _sources/api_methods_user.shell_choices.rst.txt
source_html: api_methods_user.shell_choices.html
required_roles:
  - ACCOUNT_READ
  - READONLY_ADMIN
---

# user.shell_choices

## Summary

Return the available shell choices to be used in [user.create](create.md) and [user.update](update.md).

## Required Roles

- `ACCOUNT_READ`
- `READONLY_ADMIN`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: group_ids

<a id="Call_parameters_items_i0"></a>
#### group_ids

- Schema name: `group_ids`
- Type: array of integer
- Default: []

Array of group IDs to filter shell choices. Empty array returns all shells.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
- Type: integer

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: object

Object of available shell paths and their descriptive names.
Examples:

```json
{
    "/usr/bin/bash": "bash",
    "/usr/bin/dash": "dash",
    "/usr/bin/rbash": "rbash",
    "/usr/bin/sh": "sh",
    "/usr/bin/tmux": "tmux",
    "/usr/bin/zsh": "zsh",
    "/usr/sbin/nologin": "nologin"
}
```

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
