---
title: app.query
kind: event
source_rst: _sources/api_events_app.query.rst.txt
source_html: api_events_app.query.html
required_roles:
  - APPS_READ
---

# app.query

## Summary

Sent on app changes.

## Required Roles

- `APPS_READ`

## Schema

- Type: object

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `AppAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `AppEntry`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_name"></a>
<a id="ADDED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.
###### Must be one of:

- "CRASHED"
- "DEPLOYING"
- "RUNNING"
- "STOPPED"
- "STOPPING"

<a id="headingADDED_fields_upgrade_available"></a>
<a id="ADDED_fields_upgrade_available"></a>
##### upgrade_available (required)

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

<a id="headingADDED_fields_latest_version"></a>
<a id="ADDED_fields_latest_version"></a>
##### latest_version (required)

- Schema name: `Latest Version`

The latest available version string, or `null` if unable to determine latest version.
<a id="ADDED_fields_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_latest_version_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_latest_version_anyOf_i1)

- Type: null

<a id="headingADDED_fields_latest_app_version"></a>
<a id="ADDED_fields_latest_app_version"></a>
##### latest_app_version (required)

- Schema name: `Latest App Version`

The latest application version string, or `null` if unable to determine latest version.
<a id="ADDED_fields_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_latest_app_version_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_ADDED_fields_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_latest_app_version_anyOf_i1)

- Type: null

<a id="headingADDED_fields_image_updates_available"></a>
<a id="ADDED_fields_image_updates_available"></a>
##### image_updates_available (required)

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

<a id="headingADDED_fields_custom_app"></a>
<a id="ADDED_fields_custom_app"></a>
##### custom_app (required)

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

<a id="headingADDED_fields_migrated"></a>
<a id="ADDED_fields_migrated"></a>
##### migrated (required)

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

<a id="headingADDED_fields_human_version"></a>
<a id="ADDED_fields_human_version"></a>
##### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

<a id="headingADDED_fields_version"></a>
<a id="ADDED_fields_version"></a>
##### version (required)

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

<a id="headingADDED_fields_metadata"></a>
<a id="ADDED_fields_metadata"></a>
##### metadata (required)

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

<a id="headingADDED_fields_active_workloads"></a>
<a id="ADDED_fields_active_workloads"></a>
##### active_workloads (required)

- Schema name: `AppActiveWorkloads`
- Type: object

Information about the running containers, ports, and resources used by this application.
- No Additional Properties
<a id="headingADDED_fields_active_workloads_containers"></a>
<a id="ADDED_fields_active_workloads_containers"></a>
###### containers (required)

- Schema name: `Containers`
- Type: integer

Total number of containers currently running for this application.

<a id="headingADDED_fields_active_workloads_used_ports"></a>
<a id="ADDED_fields_active_workloads_used_ports"></a>
###### used_ports (required)

- Schema name: `Used Ports`
- Type: array of object

Array of all port mappings used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_used_ports_items"></a>
###### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_active_workloads_used_ports_items_container_port"></a>
<a id="ADDED_fields_active_workloads_used_ports_items_container_port"></a>
###### container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

<a id="headingADDED_fields_active_workloads_used_ports_items_protocol"></a>
<a id="ADDED_fields_active_workloads_used_ports_items_protocol"></a>
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

<a id="headingADDED_fields_active_workloads_used_ports_items_host_ports"></a>
<a id="ADDED_fields_active_workloads_used_ports_items_host_ports"></a>
###### host_ports (required)

- Schema name: `Host Ports`
- Type: array of object

Array of host port mappings for this container port.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_used_ports_items_host_ports_items"></a>
###### HostPorts

- Schema name: `HostPorts`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_active_workloads_used_ports_items_host_ports_items_host_port"></a>
<a id="ADDED_fields_active_workloads_used_ports_items_host_ports_items_host_port"></a>
###### host_port (required)

- Schema name: `Host Port`
- Type: integer

The port number on the host system.

<a id="headingADDED_fields_active_workloads_used_ports_items_host_ports_items_host_ip"></a>
<a id="ADDED_fields_active_workloads_used_ports_items_host_ports_items_host_ip"></a>
###### host_ip (required)

- Schema name: `Host Ip`
- Type: string

The IP address on the host system that the port is bound to.

<a id="headingADDED_fields_active_workloads_used_host_ips"></a>
<a id="ADDED_fields_active_workloads_used_host_ips"></a>
###### used_host_ips (required)

- Schema name: `Used Host Ips`
- Type: array of string

Array of host IP addresses in use by the application.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_used_host_ips_items"></a>
- Type: string

<a id="headingADDED_fields_active_workloads_container_details"></a>
<a id="ADDED_fields_active_workloads_container_details"></a>
###### container_details (required)

- Schema name: `Container Details`
- Type: array of object

Detailed information about each container in the application.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_container_details_items"></a>
###### AppContainerDetails

- Schema name: `AppContainerDetails`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_active_workloads_container_details_items_id"></a>
<a id="ADDED_fields_active_workloads_container_details_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.

<a id="headingADDED_fields_active_workloads_container_details_items_service_name"></a>
<a id="ADDED_fields_active_workloads_container_details_items_service_name"></a>
###### service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.

<a id="headingADDED_fields_active_workloads_container_details_items_image"></a>
<a id="ADDED_fields_active_workloads_container_details_items_image"></a>
###### image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.

<a id="headingADDED_fields_active_workloads_container_details_items_port_config"></a>
<a id="ADDED_fields_active_workloads_container_details_items_port_config"></a>
###### port_config (required)

- Schema name: `Port Config`
- Type: array of object

Array of port mappings for this container.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_container_details_items_port_config_items"></a>
###### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_active_workloads_container_details_items_port_config_items_container_port"></a>
<a id="ADDED_fields_active_workloads_container_details_items_port_config_items_container_port"></a>
###### container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

<a id="headingADDED_fields_active_workloads_container_details_items_port_config_items_protocol"></a>
<a id="ADDED_fields_active_workloads_container_details_items_port_config_items_protocol"></a>
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

<a id="headingADDED_fields_active_workloads_container_details_items_port_config_items_host_ports"></a>
<a id="ADDED_fields_active_workloads_container_details_items_port_config_items_host_ports"></a>
###### host_ports (required)

- Schema name: `Host Ports`
- Type: array

Array of host port mappings for this container port.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_container_details_items_port_config_items_host_ports_items"></a>
- Type: object

<a id="headingADDED_fields_active_workloads_container_details_items_state"></a>
<a id="ADDED_fields_active_workloads_container_details_items_state"></a>
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

<a id="headingADDED_fields_active_workloads_container_details_items_volume_mounts"></a>
<a id="ADDED_fields_active_workloads_container_details_items_volume_mounts"></a>
###### volume_mounts (required)

- Schema name: `Volume Mounts`
- Type: array of object

Array of volume mounts configured for this container.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_container_details_items_volume_mounts_items"></a>
###### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_active_workloads_container_details_items_volume_mounts_items_source"></a>
<a id="ADDED_fields_active_workloads_container_details_items_volume_mounts_items_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

<a id="headingADDED_fields_active_workloads_container_details_items_volume_mounts_items_destination"></a>
<a id="ADDED_fields_active_workloads_container_details_items_volume_mounts_items_destination"></a>
###### destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

<a id="headingADDED_fields_active_workloads_container_details_items_volume_mounts_items_mode"></a>
<a id="ADDED_fields_active_workloads_container_details_items_volume_mounts_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

<a id="headingADDED_fields_active_workloads_container_details_items_volume_mounts_items_type"></a>
<a id="ADDED_fields_active_workloads_container_details_items_volume_mounts_items_type"></a>
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

<a id="headingADDED_fields_active_workloads_volumes"></a>
<a id="ADDED_fields_active_workloads_volumes"></a>
###### volumes (required)

- Schema name: `Volumes`
- Type: array of object

Array of all volume mounts used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_volumes_items"></a>
###### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_active_workloads_volumes_items_source"></a>
<a id="ADDED_fields_active_workloads_volumes_items_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

<a id="headingADDED_fields_active_workloads_volumes_items_destination"></a>
<a id="ADDED_fields_active_workloads_volumes_items_destination"></a>
###### destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

<a id="headingADDED_fields_active_workloads_volumes_items_mode"></a>
<a id="ADDED_fields_active_workloads_volumes_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

<a id="headingADDED_fields_active_workloads_volumes_items_type"></a>
<a id="ADDED_fields_active_workloads_volumes_items_type"></a>
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

<a id="headingADDED_fields_active_workloads_images"></a>
<a id="ADDED_fields_active_workloads_images"></a>
###### images (required)

- Schema name: `Images`
- Type: array of string

Array of Docker image names used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_images_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingADDED_fields_active_workloads_networks"></a>
<a id="ADDED_fields_active_workloads_networks"></a>
###### networks (required)

- Schema name: `Networks`
- Type: array of object

Array of Docker networks associated with the application.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_active_workloads_networks_items"></a>
###### AppNetworks

- Schema name: `AppNetworks`
- Type: object
<a id="headingADDED_fields_active_workloads_networks_items_Name"></a>
<a id="ADDED_fields_active_workloads_networks_items_Name"></a>
###### Name (required)

- Schema name: `Name`
- Type: string

The name of the Docker network.

<a id="headingADDED_fields_active_workloads_networks_items_Id"></a>
<a id="ADDED_fields_active_workloads_networks_items_Id"></a>
###### Id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the Docker network.

<a id="headingADDED_fields_active_workloads_networks_items_Labels"></a>
<a id="ADDED_fields_active_workloads_networks_items_Labels"></a>
###### Labels (required)

- Schema name: `Labels`
- Type: object

Key-value pairs of labels associated with the network.

<a id="headingADDED_fields_active_workloads_networks_items_additionalProperties"></a>
<a id="ADDED_fields_active_workloads_networks_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingADDED_fields_notes"></a>
<a id="ADDED_fields_notes"></a>
##### notes (required)

- Schema name: `Notes`

User-provided notes or comments about this application instance.
<a id="ADDED_fields_notes_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_notes_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_notes_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_notes_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_notes_anyOf_i1)

- Type: null

<a id="headingADDED_fields_action_required"></a>
<a id="ADDED_fields_action_required"></a>
##### action_required (required)

- Schema name: `Action Required`
- Type: boolean

Whether this application requires user action (e.g., configuration migration or deprecation handling).

<a id="headingADDED_fields_portals"></a>
<a id="ADDED_fields_portals"></a>
##### portals (required)

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

<a id="headingADDED_fields_version_details"></a>
<a id="ADDED_fields_version_details"></a>
##### version_details

- Schema name: `Version Details`
- Default: null

Detailed version information including changelog and upgrade notes. `null` if not available.
<a id="ADDED_fields_version_details_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_version_details_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_version_details_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_version_details_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_version_details_anyOf_i1)

- Type: null

<a id="headingADDED_fields_config"></a>
<a id="ADDED_fields_config"></a>
##### config

- Schema name: `Config`
- Default: null

Current configuration values for the application. `null` if configuration is not requested.
<a id="ADDED_fields_config_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_config_anyOf_i0)

- Type: object

<a id="tab-pane_ADDED_fields_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_config_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `AppChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `AppEntry`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_name"></a>
<a id="CHANGED_fields_name"></a>
##### name (required)

- Schema name: `Name`
- Type: string

The display name of the application.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the application instance.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
##### state (required)

- Schema name: `State`
- Type: enum (of string)

Current operational state of the application.
###### Must be one of:

- "CRASHED"
- "DEPLOYING"
- "RUNNING"
- "STOPPED"
- "STOPPING"

<a id="headingCHANGED_fields_upgrade_available"></a>
<a id="CHANGED_fields_upgrade_available"></a>
##### upgrade_available (required)

- Schema name: `Upgrade Available`
- Type: boolean

Whether a newer version of the application is available for upgrade.

<a id="headingCHANGED_fields_latest_version"></a>
<a id="CHANGED_fields_latest_version"></a>
##### latest_version (required)

- Schema name: `Latest Version`

The latest available version string, or `null` if unable to determine latest version.
<a id="CHANGED_fields_latest_version_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_latest_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_latest_version_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_latest_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_latest_version_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_latest_app_version"></a>
<a id="CHANGED_fields_latest_app_version"></a>
##### latest_app_version (required)

- Schema name: `Latest App Version`

The latest application version string, or `null` if unable to determine latest version.
<a id="CHANGED_fields_latest_app_version_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_latest_app_version_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_latest_app_version_anyOf_i0)

- Type: string
- Must be at least `1` characters long

<a id="tab-pane_CHANGED_fields_latest_app_version_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_latest_app_version_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_image_updates_available"></a>
<a id="CHANGED_fields_image_updates_available"></a>
##### image_updates_available (required)

- Schema name: `Image Updates Available`
- Type: boolean

Whether newer Docker images are available for the containers in this application.

<a id="headingCHANGED_fields_custom_app"></a>
<a id="CHANGED_fields_custom_app"></a>
##### custom_app (required)

- Schema name: `Custom App`
- Type: boolean

Whether this is a custom application (`true`) or from a catalog (`false`).

<a id="headingCHANGED_fields_migrated"></a>
<a id="CHANGED_fields_migrated"></a>
##### migrated (required)

- Schema name: `Migrated`
- Type: boolean

Whether this application has been migrated from kubernetes.

<a id="headingCHANGED_fields_human_version"></a>
<a id="CHANGED_fields_human_version"></a>
##### human_version (required)

- Schema name: `Human Version`
- Type: string

Human-readable version string for display purposes.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_version"></a>
<a id="CHANGED_fields_version"></a>
##### version (required)

- Schema name: `Version`
- Type: string

Technical version identifier of the currently installed application.
- Must be at least `1` characters long

<a id="headingCHANGED_fields_metadata"></a>
<a id="CHANGED_fields_metadata"></a>
##### metadata (required)

- Schema name: `Metadata`
- Type: object

Application metadata including description, category, and other catalog information.

<a id="headingCHANGED_fields_active_workloads"></a>
<a id="CHANGED_fields_active_workloads"></a>
##### active_workloads (required)

- Schema name: `AppActiveWorkloads`
- Type: object

Information about the running containers, ports, and resources used by this application.
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_containers"></a>
<a id="CHANGED_fields_active_workloads_containers"></a>
###### containers (required)

- Schema name: `Containers`
- Type: integer

Total number of containers currently running for this application.

<a id="headingCHANGED_fields_active_workloads_used_ports"></a>
<a id="CHANGED_fields_active_workloads_used_ports"></a>
###### used_ports (required)

- Schema name: `Used Ports`
- Type: array of object

Array of all port mappings used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_used_ports_items"></a>
###### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_used_ports_items_container_port"></a>
<a id="CHANGED_fields_active_workloads_used_ports_items_container_port"></a>
###### container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

<a id="headingCHANGED_fields_active_workloads_used_ports_items_protocol"></a>
<a id="CHANGED_fields_active_workloads_used_ports_items_protocol"></a>
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

<a id="headingCHANGED_fields_active_workloads_used_ports_items_host_ports"></a>
<a id="CHANGED_fields_active_workloads_used_ports_items_host_ports"></a>
###### host_ports (required)

- Schema name: `Host Ports`
- Type: array of object

Array of host port mappings for this container port.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_used_ports_items_host_ports_items"></a>
###### HostPorts

- Schema name: `HostPorts`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_used_ports_items_host_ports_items_host_port"></a>
<a id="CHANGED_fields_active_workloads_used_ports_items_host_ports_items_host_port"></a>
###### host_port (required)

- Schema name: `Host Port`
- Type: integer

The port number on the host system.

<a id="headingCHANGED_fields_active_workloads_used_ports_items_host_ports_items_host_ip"></a>
<a id="CHANGED_fields_active_workloads_used_ports_items_host_ports_items_host_ip"></a>
###### host_ip (required)

- Schema name: `Host Ip`
- Type: string

The IP address on the host system that the port is bound to.

<a id="headingCHANGED_fields_active_workloads_used_host_ips"></a>
<a id="CHANGED_fields_active_workloads_used_host_ips"></a>
###### used_host_ips (required)

- Schema name: `Used Host Ips`
- Type: array of string

Array of host IP addresses in use by the application.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_used_host_ips_items"></a>
- Type: string

<a id="headingCHANGED_fields_active_workloads_container_details"></a>
<a id="CHANGED_fields_active_workloads_container_details"></a>
###### container_details (required)

- Schema name: `Container Details`
- Type: array of object

Detailed information about each container in the application.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_container_details_items"></a>
###### AppContainerDetails

- Schema name: `AppContainerDetails`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_container_details_items_id"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_id"></a>
###### id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the container.

<a id="headingCHANGED_fields_active_workloads_container_details_items_service_name"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_service_name"></a>
###### service_name (required)

- Schema name: `Service Name`
- Type: string

Name of the service this container provides.

<a id="headingCHANGED_fields_active_workloads_container_details_items_image"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_image"></a>
###### image (required)

- Schema name: `Image`
- Type: string

Docker image name and tag used by this container.

<a id="headingCHANGED_fields_active_workloads_container_details_items_port_config"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_port_config"></a>
###### port_config (required)

- Schema name: `Port Config`
- Type: array of object

Array of port mappings for this container.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_container_details_items_port_config_items"></a>
###### UsedPorts

- Schema name: `UsedPorts`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_container_details_items_port_config_items_container_port"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_port_config_items_container_port"></a>
###### container_port (required)

- Schema name: `Container Port`
- Type: integer

The port number inside the container.

<a id="headingCHANGED_fields_active_workloads_container_details_items_port_config_items_protocol"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_port_config_items_protocol"></a>
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

<a id="headingCHANGED_fields_active_workloads_container_details_items_port_config_items_host_ports"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_port_config_items_host_ports"></a>
###### host_ports (required)

- Schema name: `Host Ports`
- Type: array

Array of host port mappings for this container port.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_container_details_items_port_config_items_host_ports_items"></a>
- Type: object

<a id="headingCHANGED_fields_active_workloads_container_details_items_state"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_state"></a>
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

<a id="headingCHANGED_fields_active_workloads_container_details_items_volume_mounts"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_volume_mounts"></a>
###### volume_mounts (required)

- Schema name: `Volume Mounts`
- Type: array of object

Array of volume mounts configured for this container.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_container_details_items_volume_mounts_items"></a>
###### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_container_details_items_volume_mounts_items_source"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_volume_mounts_items_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

<a id="headingCHANGED_fields_active_workloads_container_details_items_volume_mounts_items_destination"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_volume_mounts_items_destination"></a>
###### destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

<a id="headingCHANGED_fields_active_workloads_container_details_items_volume_mounts_items_mode"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_volume_mounts_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

<a id="headingCHANGED_fields_active_workloads_container_details_items_volume_mounts_items_type"></a>
<a id="CHANGED_fields_active_workloads_container_details_items_volume_mounts_items_type"></a>
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

<a id="headingCHANGED_fields_active_workloads_volumes"></a>
<a id="CHANGED_fields_active_workloads_volumes"></a>
###### volumes (required)

- Schema name: `Volumes`
- Type: array of object

Array of all volume mounts used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_volumes_items"></a>
###### AppVolumes

- Schema name: `AppVolumes`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_active_workloads_volumes_items_source"></a>
<a id="CHANGED_fields_active_workloads_volumes_items_source"></a>
###### source (required)

- Schema name: `Source`
- Type: string

The source path or volume name on the host system.

<a id="headingCHANGED_fields_active_workloads_volumes_items_destination"></a>
<a id="CHANGED_fields_active_workloads_volumes_items_destination"></a>
###### destination (required)

- Schema name: `Destination`
- Type: string

The mount path inside the container.

<a id="headingCHANGED_fields_active_workloads_volumes_items_mode"></a>
<a id="CHANGED_fields_active_workloads_volumes_items_mode"></a>
###### mode (required)

- Schema name: `Mode`
- Type: string

The mount mode (e.g., 'rw' for read-write, 'ro' for read-only).

<a id="headingCHANGED_fields_active_workloads_volumes_items_type"></a>
<a id="CHANGED_fields_active_workloads_volumes_items_type"></a>
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

<a id="headingCHANGED_fields_active_workloads_images"></a>
<a id="CHANGED_fields_active_workloads_images"></a>
###### images (required)

- Schema name: `Images`
- Type: array of string

Array of Docker image names used by the application.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_images_items"></a>
- Type: string
- Must be at least `1` characters long

<a id="headingCHANGED_fields_active_workloads_networks"></a>
<a id="CHANGED_fields_active_workloads_networks"></a>
###### networks (required)

- Schema name: `Networks`
- Type: array of object

Array of Docker networks associated with the application.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_active_workloads_networks_items"></a>
###### AppNetworks

- Schema name: `AppNetworks`
- Type: object
<a id="headingCHANGED_fields_active_workloads_networks_items_Name"></a>
<a id="CHANGED_fields_active_workloads_networks_items_Name"></a>
###### Name (required)

- Schema name: `Name`
- Type: string

The name of the Docker network.

<a id="headingCHANGED_fields_active_workloads_networks_items_Id"></a>
<a id="CHANGED_fields_active_workloads_networks_items_Id"></a>
###### Id (required)

- Schema name: `Id`
- Type: string

Unique identifier for the Docker network.

<a id="headingCHANGED_fields_active_workloads_networks_items_Labels"></a>
<a id="CHANGED_fields_active_workloads_networks_items_Labels"></a>
###### Labels (required)

- Schema name: `Labels`
- Type: object

Key-value pairs of labels associated with the network.

<a id="headingCHANGED_fields_active_workloads_networks_items_additionalProperties"></a>
<a id="CHANGED_fields_active_workloads_networks_items_additionalProperties"></a>
###### Additional Properties

Additional Properties of any type are allowed.
- Type: object

<a id="headingCHANGED_fields_notes"></a>
<a id="CHANGED_fields_notes"></a>
##### notes (required)

- Schema name: `Notes`

User-provided notes or comments about this application instance.
<a id="CHANGED_fields_notes_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_notes_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_notes_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_notes_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_notes_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_action_required"></a>
<a id="CHANGED_fields_action_required"></a>
##### action_required (required)

- Schema name: `Action Required`
- Type: boolean

Whether this application requires user action (e.g., configuration migration or deprecation handling).

<a id="headingCHANGED_fields_portals"></a>
<a id="CHANGED_fields_portals"></a>
##### portals (required)

- Schema name: `Portals`
- Type: object

Web portals and access points provided by the application (URLs, ports, etc.).

<a id="headingCHANGED_fields_version_details"></a>
<a id="CHANGED_fields_version_details"></a>
##### version_details

- Schema name: `Version Details`
- Default: null

Detailed version information including changelog and upgrade notes. `null` if not available.
<a id="CHANGED_fields_version_details_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_version_details_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_version_details_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_version_details_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_version_details_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_config"></a>
<a id="CHANGED_fields_config"></a>
##### config

- Schema name: `Config`
- Default: null

Current configuration values for the application. `null` if configuration is not requested.
<a id="CHANGED_fields_config_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_config_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_config_anyOf_i0)

- Type: object

<a id="tab-pane_CHANGED_fields_config_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_config_anyOf_i1)

- Type: null

<a id="headingREMOVED"></a>
<a id="REMOVED"></a>
### REMOVED

- Schema name: `AppRemovedEvent`
- Type: object
- No Additional Properties
<a id="headingREMOVED_id"></a>
<a id="REMOVED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
- Query filters and options: [Query Methods](../../shared/query_methods.md)
