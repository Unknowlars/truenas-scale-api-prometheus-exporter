---
title: system.advanced.config
kind: method
source_rst: _sources/api_methods_system.advanced.config.rst.txt
source_html: api_methods_system.advanced.config.html
required_roles:
  - SYSTEM_ADVANCED_READ
---

# system.advanced.config

## Required Roles

- `SYSTEM_ADVANCED_READ`

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

- Schema name: `SystemAdvancedEntry`
- Type: object
- No Additional Properties
<a id="headingReturn_value_id"></a>
<a id="Return_value_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

<a id="headingReturn_value_advancedmode"></a>
<a id="Return_value_advancedmode"></a>
#### advancedmode (required)

- Schema name: `Advancedmode`
- Type: boolean

Enable advanced mode to show additional configuration options in the web interface.

<a id="headingReturn_value_autotune"></a>
<a id="Return_value_autotune"></a>
#### autotune (required)

- Schema name: `Autotune`
- Type: boolean

Execute autotune script which attempts to optimize the system based on the installed hardware.

<a id="headingReturn_value_kdump_enabled"></a>
<a id="Return_value_kdump_enabled"></a>
#### kdump_enabled (required)

- Schema name: `Kdump Enabled`
- Type: boolean

Enable kernel crash dumps for debugging system crashes.

<a id="headingReturn_value_boot_scrub"></a>
<a id="Return_value_boot_scrub"></a>
#### boot_scrub (required)

- Schema name: `Boot Scrub`
- Type: integer

Number of days between automatic boot pool scrubs.
- Value must be strictly greater than `0`

<a id="headingReturn_value_consolemenu"></a>
<a id="Return_value_consolemenu"></a>
#### consolemenu (required)

- Schema name: `Consolemenu`
- Type: boolean

Enable console menu. Default to standard login in the console if disabled.

<a id="headingReturn_value_consolemsg"></a>
<a id="Return_value_consolemsg"></a>
#### consolemsg (required)

- Schema name: `Consolemsg`
- Type: boolean

Deprecated: Please use `consolemsg` attribute in the `system.general` plugin instead.

<a id="headingReturn_value_debugkernel"></a>
<a id="Return_value_debugkernel"></a>
#### debugkernel (required)

- Schema name: `Debugkernel`
- Type: boolean

Enable debug kernel for additional logging and debugging capabilities.

<a id="headingReturn_value_fqdn_syslog"></a>
<a id="Return_value_fqdn_syslog"></a>
#### fqdn_syslog (required)

- Schema name: `Fqdn Syslog`
- Type: boolean

Include the full domain name in syslog messages.

<a id="headingReturn_value_motd"></a>
<a id="Return_value_motd"></a>
#### motd (required)

- Schema name: `Motd`
- Type: string

Message of the day displayed after login.

<a id="headingReturn_value_login_banner"></a>
<a id="Return_value_login_banner"></a>
#### login_banner (required)

- Schema name: `Login Banner`
- Type: string

Banner message displayed before login prompt.
- Must be at most `4096` characters long

<a id="headingReturn_value_powerdaemon"></a>
<a id="Return_value_powerdaemon"></a>
#### powerdaemon (required)

- Schema name: `Powerdaemon`
- Type: boolean

Enable the power management daemon for automatic power management.

<a id="headingReturn_value_serialconsole"></a>
<a id="Return_value_serialconsole"></a>
#### serialconsole (required)

- Schema name: `Serialconsole`
- Type: boolean

Enable serial console access.

<a id="headingReturn_value_serialport"></a>
<a id="Return_value_serialport"></a>
#### serialport (required)

- Schema name: `Serialport`
- Type: string

Serial port device for console access.

<a id="headingReturn_value_anonstats_token"></a>
<a id="Return_value_anonstats_token"></a>
#### anonstats_token (required)

- Schema name: `Anonstats Token`
- Type: string

Token used for anonymous statistics reporting.

<a id="headingReturn_value_serialspeed"></a>
<a id="Return_value_serialspeed"></a>
#### serialspeed (required)

- Schema name: `Serialspeed`
- Type: enum (of string)

Baud rate for serial console communication.
##### Must be one of:

- "9600"
- "19200"
- "38400"
- "57600"
- "115200"

<a id="headingReturn_value_overprovision"></a>
<a id="Return_value_overprovision"></a>
#### overprovision (required)

- Schema name: `Overprovision`

Percentage of SSD overprovisioning to reserve for wear leveling.
<a id="Return_value_overprovision_anyOf"></a>
##### Any of

<a id="tab-pane_Return_value_overprovision_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_overprovision_anyOf_i0)

- Type: integer
- Value must be greater or equal to `0`

<a id="tab-pane_Return_value_overprovision_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_overprovision_anyOf_i1)

- Type: null

<a id="headingReturn_value_traceback"></a>
<a id="Return_value_traceback"></a>
#### traceback (required)

- Schema name: `Traceback`
- Type: boolean

Enable generation and saving of tracebacks for debugging.

<a id="headingReturn_value_uploadcrash"></a>
<a id="Return_value_uploadcrash"></a>
#### uploadcrash (required)

- Schema name: `Uploadcrash`
- Type: boolean

Automatically upload crash reports to iXsystems for analysis.

<a id="headingReturn_value_anonstats"></a>
<a id="Return_value_anonstats"></a>
#### anonstats (required)

- Schema name: `Anonstats`
- Type: boolean

Enable anonymous usage statistics reporting to help improve TrueNAS.

<a id="headingReturn_value_sed_user"></a>
<a id="Return_value_sed_user"></a>
#### sed_user (required)

- Schema name: `Sed User`
- Type: enum (of string)

SED (Self-Encrypting Drive) user type for drive encryption.
##### Must be one of:

- "USER"
- "MASTER"

<a id="headingReturn_value_sysloglevel"></a>
<a id="Return_value_sysloglevel"></a>
#### sysloglevel (required)

- Schema name: `Sysloglevel`
- Type: enum (of string)

Minimum log level for syslog messages. F*EMERG is most critical, F*DEBUG is least critical.
##### Must be one of:

- "F_EMERG"
- "F_ALERT"
- "F_CRIT"
- "F_ERR"
- "F_WARNING"
- "F_NOTICE"
- "F_INFO"
- "F_DEBUG"

<a id="headingReturn_value_syslogservers"></a>
<a id="Return_value_syslogservers"></a>
#### syslogservers

- Schema name: `Syslogservers`
- Type: array of object
- Default: []

Configurations for up to two remote syslog servers.
- Must contain a maximum of `2` items
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_syslogservers_items"></a>
##### SyslogServer

- Schema name: `SyslogServer`
- Type: object
- No Additional Properties
<a id="headingReturn_value_syslogservers_items_host"></a>
<a id="Return_value_syslogservers_items_host"></a>
###### host (required)

- Schema name: `Host`
- Type: string

Remote syslog server DNS hostname or IP address. Nonstandard port numbers can be used by appending a colon and port number to the hostname, like mysyslogserver:1928. Port 514 is used by default for TCP and UDP transports as per RFC3164; port 6514 is used by default for TLS transport as per RFC5425.

<a id="headingReturn_value_syslogservers_items_transport"></a>
<a id="Return_value_syslogservers_items_transport"></a>
###### transport

- Schema name: `Transport`
- Type: enum (of string)
- Default: "UDP"

Transport Protocol for the remote system log server connection.
###### Must be one of:

- "UDP"
- "TCP"
- "TLS"

<a id="headingReturn_value_syslogservers_items_tls_certificate"></a>
<a id="Return_value_syslogservers_items_tls_certificate"></a>
###### tls_certificate

- Schema name: `Tls Certificate`
- Default: null

Applies only if `transport` is "TLS". ID of the local certificate to send for mutual TLS (mTLS) connections. `null` indicates one-way TLS in which only the server identified by `host` will need to provide a certificate.
<a id="Return_value_syslogservers_items_tls_certificate_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_syslogservers_items_tls_certificate_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_syslogservers_items_tls_certificate_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_syslogservers_items_tls_certificate_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_syslogservers_items_tls_certificate_anyOf_i1)

- Type: null

<a id="headingReturn_value_syslog_audit"></a>
<a id="Return_value_syslog_audit"></a>
#### syslog_audit

- Schema name: `Syslog Audit`
- Type: boolean

The remote syslog server(s) will also receive audit messages.

<a id="headingReturn_value_isolated_gpu_pci_ids"></a>
<a id="Return_value_isolated_gpu_pci_ids"></a>
#### isolated_gpu_pci_ids (required)

- Schema name: `Isolated Gpu Pci Ids`
- Type: array of string

List of GPU PCI IDs to isolate from the host system for VM passthrough.
- No Additional Items

##### Each item of this array must be:

<a id="Return_value_isolated_gpu_pci_ids_items"></a>
- Type: string

<a id="headingReturn_value_kernel_extra_options"></a>
<a id="Return_value_kernel_extra_options"></a>
#### kernel_extra_options (required)

- Schema name: `Kernel Extra Options`
- Type: string

Additional kernel boot parameters to pass to the Linux kernel.

<a id="headingReturn_value_nvidia"></a>
<a id="Return_value_nvidia"></a>
#### nvidia (required)

- Schema name: `Nvidia`
- Type: boolean

Whether NVIDIA GPU support is enabled.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
