---
title: app.delete
kind: method
source_rst: _sources/api_methods_app.delete.rst.txt
source_html: api_methods_app.delete.html
required_roles:
  - APPS_WRITE
---

# app.delete

## Summary

Delete `app_name` app.

`force_remove_custom_app` should be set when the app being deleted is a custom app and the user wants to forcefully remove the app. A use-case for this attribute is that the user had an invalid yaml in their custom app and there are no actual docker resources (network/containers/volumes) in place for the custom app, then docker compose down will fail as the yaml itself is invalid. In this case this flag can be set to proceed with the deletion of the custom app. However if this app had any docker resources in place, then this flag will have no effect.

This method is a job.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

<a id="Call_parameters_items_i0"></a>
#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to delete.
- Must be at least `1` characters long

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "remove_images": true,
  "remove_ix_volumes": false,
  "force_remove_custom_app": false
}
```

Options controlling what gets removed along with the application.
- No Additional Properties
<a id="headingCall_parameters_items_i1_remove_images"></a>
<a id="Call_parameters_items_i1_remove_images"></a>
##### remove_images

- Schema name: `Remove Images`
- Type: boolean
- Default: true

Whether to remove Docker images associated with the application.

<a id="headingCall_parameters_items_i1_remove_ix_volumes"></a>
<a id="Call_parameters_items_i1_remove_ix_volumes"></a>
##### remove_ix_volumes

- Schema name: `Remove Ix Volumes`
- Type: boolean
- Default: false

Whether to remove TrueNAS-managed storage volumes.

<a id="headingCall_parameters_items_i1_force_remove_custom_app"></a>
<a id="Call_parameters_items_i1_force_remove_custom_app"></a>
##### force_remove_custom_app

- Schema name: `Force Remove Custom App`
- Type: boolean
- Default: false

Force removal of custom applications that might have important data or configurations.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the application is successfully deleted.
- Specific value: `true`

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
