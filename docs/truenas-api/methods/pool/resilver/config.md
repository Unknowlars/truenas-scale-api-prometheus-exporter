---
title: pool.resilver.config
kind: method
source_rst: _sources/api_methods_pool.resilver.config.rst.txt
source_html: api_methods_pool.resilver.config.html
required_roles:
  - POOL_READ
---

# pool.resilver.config

## Required Roles

- `POOL_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `PoolResilverEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the resilver schedule entry.

#### begin

- Schema name: `Begin`
- Type: string
- Default: "18:00"

Time when the resilver operations window begins (24-hour format).
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

#### end

- Schema name: `End`
- Type: string
- Default: "9:00"

Time when the resilver operations window ends (24-hour format).
Examples:

```json
"00:00"
```
Examples:

```json
"06:30"
```
Examples:

```json
"18:00"
```
Examples:

```json
"23:00"
```

#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the resilver schedule is enabled.

#### weekday

- Schema name: `Weekday`
- Type: array of integer
- Default: [1, 2, 3, 4, 5, 6, 7]

Array of weekdays when resilver operations are allowed (1=Monday through 7=Sunday).
- No Additional Items

##### Each item of this array must be:

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `7`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
