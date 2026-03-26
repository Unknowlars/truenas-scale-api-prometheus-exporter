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

`force_remove_ix_volumes` should be set when the ix-volumes were created by the system for apps which were migrated from k8s to docker and the user wants to remove them. This is to prevent accidental deletion of the original ix-volumes which were created in dragonfish and before for kubernetes based apps. When this is set, it will result in the deletion of ix-volumes from both docker based apps and k8s based apps and should be carefully set.

`force_remove_custom_app` should be set when the app being deleted is a custom app and the user wants to forcefully remove the app. A use-case for this attribute is that user had an invalid yaml in his custom app and there are no actual docker resources (network/containers/volumes) in place for the custom app, then docker compose down will fail as the yaml itself is invalid. In this case this flag can be set to proceed with the deletion of the custom app. However if this app had any docker resources in place, then this flag will have no effect.

This method is a job.

## Required Roles

- `APPS_WRITE`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: app_name

#### app_name

- Schema name: `app_name`
- Type: string

Name of the application to delete.
- Must be at least `1` characters long

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "remove_images": true,
  "remove_ix_volumes": false,
  "force_remove_ix_volumes": false,
  "force_remove_custom_app": false
}
```

Options controlling what gets removed along with the application.
- No Additional Properties
##### remove_images

- Schema name: `Remove Images`
- Type: boolean
- Default: true

Whether to remove Docker images associated with the application.

##### remove_ix_volumes

- Schema name: `Remove Ix Volumes`
- Type: boolean
- Default: false

Whether to remove TrueNAS-managed storage volumes.

##### force_remove_ix_volumes

- Schema name: `Force Remove Ix Volumes`
- Type: boolean
- Default: false

Force removal of TrueNAS-managed volumes even if they contain data.

##### force_remove_custom_app

- Schema name: `Force Remove Custom App`
- Type: boolean
- Default: false

Force removal of custom applications that might have important data or configurations.

### Return value

- Schema name: `Result`
- Type: const

Returns `true` when the application is successfully deleted.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
