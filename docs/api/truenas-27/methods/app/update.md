---
title: app.update
kind: method
source_rst: _sources/api_methods_app.update.rst.txt
source_html: api_methods_app.update.html
required_roles:
  - APPS_WRITE
---

# app.update

## Summary

Update `app_name` app with new configuration.

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

Name of the application to update.
- Must be at least `1` characters long

#### Parameter 2: update

<a id="Call_parameters_items_i1"></a>
#### update

- Schema name: `update`
- Type: object
- Default:
```json
{
  "values": "{}",
  "custom_compose_config": "{}",
  "custom_compose_config_string": ""
}
```

Updated configuration and settings for the application.
- No Additional Properties
<a id="headingCall_parameters_items_i1_values"></a>
<a id="Call_parameters_items_i1_values"></a>
##### values

- Schema name: `Values`
- Type: object

Updated configuration values for the application.

<a id="headingCall_parameters_items_i1_custom_compose_config"></a>
<a id="Call_parameters_items_i1_custom_compose_config"></a>
##### custom_compose_config

- Schema name: `Custom Compose Config`
- Type: object

Updated Docker Compose configuration as a structured object.

<a id="headingCall_parameters_items_i1_custom_compose_config_string"></a>
<a id="Call_parameters_items_i1_custom_compose_config_string"></a>
##### custom_compose_config_string

- Schema name: `Custom Compose Config String`
- Type: string
- Default: ""

Updated Docker Compose configuration as a YAML string.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `AppEntry`
- Type: object

The updated application entry with new configuration details.
- No Additional Properties
<a id="headingReturn_value_name"></a>
<a id="Return_value_name"></a>
#### name (required)

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

<a id="headingReturn_value_state"></a>
<a id="Return_value_state"></a>
#### state (required)

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.
##### Must be one of:

- "CRASHED"
- "DEPLOYING"
- "RUNNING"
- "STOPPED"
- "STOPPING"

<a id="headingReturn_value_upgrade_available"></a>
<a id="Return_value_upgrade_available"></a>
#### upgrade_available (required)

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

<a id="headingReturn_value_latest_version"></a>
<a id="Return_value_latest_version"></a>
#### latest_version (required)

- Schema name: `Latest Version`

The latest available version string, or `null` if unable to determine latest version.
<a id="Return_value_latest_version_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_latest_version_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_latest_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_latest_app_version"></a>
<a id="Return_value_latest_app_version"></a>
#### latest_app_version (required)

- Schema name: `Latest App Version`

The latest application version string, or `null` if unable to determine latest version.
<a id="Return_value_latest_app_version_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_latest_app_version_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_Return_value_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_latest_app_version_anyOf_i1)

- Type: null

<a id="headingReturn_value_image_updates_available"></a>
<a id="Return_value_image_updates_available"></a>
#### image_updates_available (required)

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

<a id="headingReturn_value_custom_app"></a>
<a id="Return_value_custom_app"></a>
#### custom_app (required)

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

<a id="headingReturn_value_migrated"></a>
<a id="Return_value_migrated"></a>
#### migrated (required)

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

<a id="headingReturn_value_human_version"></a>
<a id="Return_value_human_version"></a>
#### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

<a id="headingReturn_value_version"></a>
<a id="Return_value_version"></a>
#### version (required)

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

<a id="headingReturn_value_metadata"></a>
<a id="Return_value_metadata"></a>
#### metadata (required)

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

<a id="headingReturn_value_active_workloads"></a>
<a id="Return_value_active_workloads"></a>
#### active_workloads (required)

- Schema name: `AppActiveWorkloads`
- Type: object

Information about the running containers, ports, and resources used by this application.
- No Additional Properties
<a id="headingReturn_value_active_workloads_containers"></a>
<a id="Return_value_active_workloads_containers"></a>
##### containers (required)

- Schema name: `Containers`
- Type: integer

Total number of containers currently running for this application.

<a id="headingReturn_value_active_workloads_used_ports"></a>
<a id="Return_value_active_workloads_used_ports"></a>
##### used_ports (required)

- Schema name: `Used Ports`
- Type: array of object

Array of all port mappings used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_used_ports_items"></a>
###### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
<a id="headingReturn_value_active_workloads_used_ports_items_container_port"></a>
<a id="Return_value_active_workloads_used_ports_items_container_port"></a>
###### container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

<a id="headingReturn_value_active_workloads_used_ports_items_protocol"></a>
<a id="Return_value_active_workloads_used_ports_items_protocol"></a>
###### protocol (required)

- Schema name: `Protocol`
- Type: string

The network protocol used.
Examples:

```json
"tcp"
```
Examples:

```json
"udp"
```

<a id="headingReturn_value_active_workloads_used_ports_items_host_ports"></a>
<a id="Return_value_active_workloads_used_ports_items_host_ports"></a>
###### host_ports (required)

- Schema name: `Host Ports`
- Type: array of object

Array of host port mappings for this container port.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_used_ports_items_host_ports_items"></a>
###### HostPorts

- Schema name: `HostPorts`
- Type: object
- No Additional Properties
<a id="headingReturn_value_active_workloads_used_ports_items_host_ports_items_host_port"></a>
<a id="Return_value_active_workloads_used_ports_items_host_ports_items_host_port"></a>
###### host_port (required)

- Schema name: `Host Port`
- Type: integer

The port number on the host system.

<a id="headingReturn_value_active_workloads_used_ports_items_host_ports_items_host_ip"></a>
<a id="Return_value_active_workloads_used_ports_items_host_ports_items_host_ip"></a>
###### host_ip (required)

- Schema name: `Host Ip`
- Type: string

The IP address on the host system that the port is bound to.

<a id="headingReturn_value_active_workloads_used_host_ips"></a>
<a id="Return_value_active_workloads_used_host_ips"></a>
##### used_host_ips (required)

- Schema name: `Used Host Ips`
- Type: array of string

Array of host IP addresses in use by the application.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_used_host_ips_items"></a>
- Type: string

<a id="headingReturn_value_active_workloads_container_details"></a>
<a id="Return_value_active_workloads_container_details"></a>
##### container_details (required)

- Schema name: `Container Details`
- Type: array of object

Detailed information about each container in the application.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_container_details_items"></a>
###### AppContainerDetails

- Schema name: `AppContainerDetails`
- Type: object
- No Additional Properties
<a id="headingReturn_value_active_workloads_container_details_items_id"></a>
<a id="Return_value_active_workloads_container_details_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.

<a id="headingReturn_value_active_workloads_container_details_items_service_name"></a>
<a id="Return_value_active_workloads_container_details_items_service_name"></a>
###### service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.

<a id="headingReturn_value_active_workloads_container_details_items_image"></a>
<a id="Return_value_active_workloads_container_details_items_image"></a>
###### image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.

<a id="headingReturn_value_active_workloads_container_details_items_port_config"></a>
<a id="Return_value_active_workloads_container_details_items_port_config"></a>
###### port_config (required)

- Schema name: `Port Config`
- Type: array of object

Array of port mappings for this container.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_container_details_items_port_config_items"></a>
###### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
<a id="headingReturn_value_active_workloads_container_details_items_port_config_items_container_port"></a>
<a id="Return_value_active_workloads_container_details_items_port_config_items_container_port"></a>
###### container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

<a id="headingReturn_value_active_workloads_container_details_items_port_config_items_protocol"></a>
<a id="Return_value_active_workloads_container_details_items_port_config_items_protocol"></a>
###### protocol (required)

- Schema name: `Protocol`
- Type: string

The network protocol used.
Examples:

```json
"tcp"
```
Examples:

```json
"udp"
```

<a id="headingReturn_value_active_workloads_container_details_items_port_config_items_host_ports"></a>
<a id="Return_value_active_workloads_container_details_items_port_config_items_host_ports"></a>
###### host_ports (required)

- Schema name: `Host Ports`
- Type: array

Array of host port mappings for this container port.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_container_details_items_port_config_items_host_ports_items"></a>
- Type: object

<a id="headingReturn_value_active_workloads_container_details_items_state"></a>
<a id="Return_value_active_workloads_container_details_items_state"></a>
###### state (required)

- Schema name: `State`
- Type: enum (of string)

Current state of the container.
###### Must be one of:

- "crashed"
- "created"
- "exited"
- "running"
- "starting"

<a id="headingReturn_value_active_workloads_container_details_items_volume_mounts"></a>
<a id="Return_value_active_workloads_container_details_items_volume_mounts"></a>
###### volume_mounts (required)

- Schema name: `Volume Mounts`
- Type: array of object

Array of volume mounts configured for this container.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_container_details_items_volume_mounts_items"></a>
###### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_active_workloads_container_details_items_volume_mounts_items_source"></a>
<a id="Return_value_active_workloads_container_details_items_volume_mounts_items_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

<a id="headingReturn_value_active_workloads_container_details_items_volume_mounts_items_destination"></a>
<a id="Return_value_active_workloads_container_details_items_volume_mounts_items_destination"></a>
###### destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

<a id="headingReturn_value_active_workloads_container_details_items_volume_mounts_items_mode"></a>
<a id="Return_value_active_workloads_container_details_items_volume_mounts_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

<a id="headingReturn_value_active_workloads_container_details_items_volume_mounts_items_type"></a>
<a id="Return_value_active_workloads_container_details_items_volume_mounts_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The volume type.
Examples:

```json
"bind"
```
Examples:

```json
"volume"
```

<a id="headingReturn_value_active_workloads_volumes"></a>
<a id="Return_value_active_workloads_volumes"></a>
##### volumes (required)

- Schema name: `Volumes`
- Type: array of object

Array of all volume mounts used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_volumes_items"></a>
###### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
<a id="headingReturn_value_active_workloads_volumes_items_source"></a>
<a id="Return_value_active_workloads_volumes_items_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

<a id="headingReturn_value_active_workloads_volumes_items_destination"></a>
<a id="Return_value_active_workloads_volumes_items_destination"></a>
###### destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

<a id="headingReturn_value_active_workloads_volumes_items_mode"></a>
<a id="Return_value_active_workloads_volumes_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

<a id="headingReturn_value_active_workloads_volumes_items_type"></a>
<a id="Return_value_active_workloads_volumes_items_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

The volume type.
Examples:

```json
"bind"
```
Examples:

```json
"volume"
```

<a id="headingReturn_value_active_workloads_images"></a>
<a id="Return_value_active_workloads_images"></a>
##### images (required)

- Schema name: `Images`
- Type: array of string

Array of Docker image names used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_images_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingReturn_value_active_workloads_networks"></a>
<a id="Return_value_active_workloads_networks"></a>
##### networks (required)

- Schema name: `Networks`
- Type: array of object

Array of Docker networks associated with the application.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_active_workloads_networks_items"></a>
###### AppNetworks

- Schema name: `AppNetworks`
- Type: object
<a id="headingReturn_value_active_workloads_networks_items_Name"></a>
<a id="Return_value_active_workloads_networks_items_Name"></a>
###### Name (required)

- Schema name: `Name`
- Type: string

The name of the Docker network.

<a id="headingReturn_value_active_workloads_networks_items_Id"></a>
<a id="Return_value_active_workloads_networks_items_Id"></a>
###### Id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the Docker network.

<a id="headingReturn_value_active_workloads_networks_items_Labels"></a>
<a id="Return_value_active_workloads_networks_items_Labels"></a>
###### Labels (required)

- Schema name: `Labels`
- Type: object

Key-value pairs of labels associated with the network.

<a id="headingReturn_value_active_workloads_networks_items_additionalProperties"></a>
<a id="Return_value_active_workloads_networks_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingReturn_value_notes"></a>
<a id="Return_value_notes"></a>
#### notes (required)

- Schema name: `Notes`

User-provided notes or comments about this application instance.
<a id="Return_value_notes_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_notes_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_notes_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_notes_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_notes_anyOf_i1)

- Type: null

<a id="headingReturn_value_action_required"></a>
<a id="Return_value_action_required"></a>
#### action_required (required)

- Schema name: `Action Required`
- Type: boolean

Whether this application requires user action (e.g., configuration migration or deprecation handling).

<a id="headingReturn_value_portals"></a>
<a id="Return_value_portals"></a>
#### portals (required)

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

<a id="headingReturn_value_version_details"></a>
<a id="Return_value_version_details"></a>
#### version_details

- Schema name: `Version Details`
- Default: null

Detailed version information including changelog and upgrade notes. `null` if not available.
<a id="Return_value_version_details_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_version_details_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_version_details_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_version_details_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_version_details_anyOf_i1)

- Type: null

<a id="headingReturn_value_config"></a>
<a id="Return_value_config"></a>
#### config

- Schema name: `Config`
- Default: null

Current configuration values for the application. `null` if configuration is not requested.
<a id="Return_value_config_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_config_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_config_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
