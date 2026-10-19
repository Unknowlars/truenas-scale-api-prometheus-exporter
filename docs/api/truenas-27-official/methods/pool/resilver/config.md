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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `PoolResilverEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the resilver schedule entry.

<a id="headingReturn_value_begin"></a>
<a id="Return_value_begin"></a>
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

<a id="headingReturn_value_end"></a>
<a id="Return_value_end"></a>
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

<a id="headingReturn_value_enabled"></a>
<a id="Return_value_enabled"></a>
#### enabled

- Schema name: `Enabled`
- Type: boolean
- Default: true

Whether the resilver schedule is enabled.

<a id="headingReturn_value_weekday"></a>
<a id="Return_value_weekday"></a>
#### weekday

- Schema name: `Weekday`
- Type: array of integer
- Default: [1, 2, 3, 4, 5, 6, 7]

Array of weekdays when resilver operations are allowed (1=Monday through 7=Sunday).
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_weekday_items"></a>
- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `7`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
