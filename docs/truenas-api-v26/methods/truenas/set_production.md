---
title: truenas.set_production
kind: method
source_rst: _sources/api_methods_truenas.set_production.rst.txt
source_html: api_methods_truenas.set_production.html
required_roles:
  - FULL_ADMIN
---

# truenas.set_production

## Summary

Sets system production state and optionally sends initial debug.

This method is a job.

## Required Roles

- `FULL_ADMIN`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: production

#### production

- Schema name: `production`
- Type: boolean

Whether to configure the system for production use.

#### Parameter 2: attach_debug

#### attach_debug

- Schema name: `attach_debug`
- Type: boolean
- Default: false

Whether to attach debug information when transitioning to production mode.

### Return value

Support ticket details if system was newly marked as production. `null` otherwise.
#### Any of

##### SupportNewTicket

- Schema name: `SupportNewTicket`
- Type: object
- No Additional Properties
###### ticket (required)

- Schema name: `Ticket`

Ticket number if successfully created. `null` if creation failed.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### url (required)

- Schema name: `Url`

URL to view the created ticket. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### has_debug (required)

- Schema name: `Has Debug`
- Type: boolean

Whether debug information was attached to the ticket.

###### debug_attach_error (required)

- Schema name: `Debug Attach Error`

If attaching debug information failed, the error message will appear here.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
