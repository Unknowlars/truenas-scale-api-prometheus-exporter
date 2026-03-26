---
title: user.shell_choices
kind: method
source_rst: _sources/api_methods_user.shell_choices.rst.txt
source_html: api_methods_user.shell_choices.html
required_roles:
  - ACCOUNT_READ | READONLY_ADMIN
---

# user.shell_choices

## Summary

Return the available shell choices to be used in `user.create` and `user.update`.

:param group_ids: List of local group IDs for the user.

## Required Roles

- `ACCOUNT_READ | READONLY_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: group_ids

#### group_ids

- Schema name: `group_ids`
- Type: array of integer
- Default: []

Array of group IDs to filter shell choices. Empty array returns all shells.
- No Additional Items

##### Each item of this array must be:

- Type: integer

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
