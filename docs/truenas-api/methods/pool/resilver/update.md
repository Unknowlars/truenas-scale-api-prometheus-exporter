---
title: pool.resilver.update
kind: method
source_rst: _sources/api_methods_pool.resilver.update.rst.txt
source_html: api_methods_pool.resilver.update.html
required_roles:
  - POOL_WRITE
---

# pool.resilver.update

## Summary

Configure Pool Resilver Priority.

If `begin` time is greater than `end` time it means it will rollover the day, e.g. begin = "19:00", end = "05:00" will increase pool resilver priority from 19:00 of one day until 05:00 of the next day.

`weekday` follows crontab(5) values 0-7 (0 or 7 is Sun).

.. examples(websocket)::

Enable pool resilver priority all business days from 7PM to 5AM.

:::javascript { "id": "6841f242-840a-11e6-a437-00e04d680384", "msg": "method", "method": "pool.resilver.update", "params": [{ "enabled": true, "begin": "19:00", "end": "05:00", "weekday": [1, 2, 3, 4, 5] }] }

## Required Roles

- `POOL_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: data

#### data

- Schema name: `data`
- Type: object

The resilver schedule configuration to update.
- No Additional Properties
##### begin

- Schema name: `Begin`
- Type: string

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

##### end

- Schema name: `End`
- Type: string

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

##### enabled

- Schema name: `Enabled`
- Type: boolean

Whether the resilver schedule is enabled.

##### weekday

- Schema name: `Weekday`
- Type: array of integer

Array of weekdays when resilver operations are allowed (1=Monday through 7=Sunday).
- No Additional Items

###### Each item of this array must be:

- Type: integer
- Value must be greater or equal to `1` and lesser or equal to `7`

### Return value

- Schema name: `PoolResilverEntry`
- Type: object

The updated resilver schedule configuration.
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
