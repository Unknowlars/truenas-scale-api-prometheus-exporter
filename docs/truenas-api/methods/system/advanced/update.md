---
title: system.advanced.update
kind: method
source_rst: _sources/api_methods_system.advanced.update.rst.txt
source_html: api_methods_system.advanced.update.html
required_roles:
  - SYSTEM_ADVANCED_WRITE
---

# system.advanced.update

## Summary

Update System Advanced Service Configuration.

## Required Roles

- `SYSTEM_ADVANCED_WRITE`

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

Updated system advanced configuration data.
- No Additional Properties
##### advancedmode

- Schema name: `Advancedmode`
- Type: boolean

Enable advanced mode to show additional configuration options in the web interface.

##### autotune

- Schema name: `Autotune`
- Type: boolean

Execute autotune script which attempts to optimize the system based on the installed hardware.

##### kdump_enabled

- Schema name: `Kdump Enabled`
- Type: boolean

Enable kernel crash dumps for debugging system crashes.

##### boot_scrub

- Schema name: `Boot Scrub`
- Type: integer

Number of days between automatic boot pool scrubs.
- Value must be strictly greater than `0`

##### consolemenu

- Schema name: `Consolemenu`
- Type: boolean

Enable console menu. Default to standard login in the console if disabled.

##### consolemsg

- Schema name: `Consolemsg`
- Type: boolean

Deprecated: Please use `consolemsg` attribute in the `system.general` plugin instead.

##### debugkernel

- Schema name: `Debugkernel`
- Type: boolean

Enable debug kernel for additional logging and debugging capabilities.

##### fqdn_syslog

- Schema name: `Fqdn Syslog`
- Type: boolean

Include the full domain name in syslog messages.

##### motd

- Schema name: `Motd`
- Type: string

Message of the day displayed after login.

##### login_banner

- Schema name: `Login Banner`
- Type: string

Banner message displayed before login prompt.
- Must be at most `4096` characters long

##### powerdaemon

- Schema name: `Powerdaemon`
- Type: boolean

Enable the power management daemon for automatic power management.

##### serialconsole

- Schema name: `Serialconsole`
- Type: boolean

Enable serial console access.

##### serialport

- Schema name: `Serialport`
- Type: string

Serial port device for console access.

##### serialspeed

- Schema name: `Serialspeed`
- Type: enum (of string)

Baud rate for serial console communication.

##### overprovision

- Schema name: `Overprovision`

Percentage of SSD overprovisioning to reserve for wear leveling.
###### Any of

####### Option 1

- Type: integer
- Value must be greater or equal to `0`

####### Option 2

- Type: null

##### traceback

- Schema name: `Traceback`
- Type: boolean

Enable generation and saving of tracebacks for debugging.

##### uploadcrash

- Schema name: `Uploadcrash`
- Type: boolean

Automatically upload crash reports to iXsystems for analysis.

##### anonstats

- Schema name: `Anonstats`
- Type: boolean

Enable anonymous usage statistics reporting to help improve TrueNAS.

##### sed_user

- Schema name: `Sed User`
- Type: enum (of string)

SED (Self-Encrypting Drive) user type for drive encryption.

##### sysloglevel

- Schema name: `Sysloglevel`
- Type: enum (of string)

Minimum log level for syslog messages. F*EMERG is most critical, F*DEBUG is least critical.

##### syslogservers

- Schema name: `Syslogservers`
- Type: array of object

Configurations for up to two remote syslog servers. **If provided, will overwrite the entire array in the existing entry.**
- Must contain a maximum of `2` items
- No Additional Items

###### Each item of this array must be:

###### SyslogServer

- Schema name: `SyslogServer`
- Type: object
- No Additional Properties
####### host (required)

- Schema name: `Host`
- Type: string

Remote syslog server DNS hostname or IP address. Nonstandard port numbers can be used by appending a colon and port number to the hostname, like mysyslogserver:1928. Port 514 is used by default for TCP and UDP transports as per RFC3164; port 6514 is used by default for TLS transport as per RFC5425.

####### transport

- Schema name: `Transport`
- Type: enum (of string)
- Default: "UDP"

Transport Protocol for the remote system log server connection.

####### tls_certificate

- Schema name: `Tls Certificate`
- Default: null

Applies only if `transport` is "TLS". ID of the local certificate to send for mutual TLS (mTLS) connections. `null` indicates one-way TLS in which only the server identified by `host` will need to provide a certificate.
######## Any of

######### Option 1

- Type: integer

######### Option 2

- Type: null

##### syslog_audit

- Schema name: `Syslog Audit`
- Type: boolean

The remote syslog server(s) will also receive audit messages.

##### kernel_extra_options

- Schema name: `Kernel Extra Options`
- Type: string

Additional kernel boot parameters to pass to the Linux kernel.

##### sed_passwd

- Schema name: `Sed Passwd`
- Type: string

Password for SED (Self-Encrypting Drive) global unlock.

### Return value

- Schema name: `SystemAdvancedEntry`
- Type: object

The updated system advanced configuration.
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Placeholder identifier. Not used as there is only one.

#### advancedmode (required)

- Schema name: `Advancedmode`
- Type: boolean

Enable advanced mode to show additional configuration options in the web interface.

#### autotune (required)

- Schema name: `Autotune`
- Type: boolean

Execute autotune script which attempts to optimize the system based on the installed hardware.

#### kdump_enabled (required)

- Schema name: `Kdump Enabled`
- Type: boolean

Enable kernel crash dumps for debugging system crashes.

#### boot_scrub (required)

- Schema name: `Boot Scrub`
- Type: integer

Number of days between automatic boot pool scrubs.
- Value must be strictly greater than `0`

#### consolemenu (required)

- Schema name: `Consolemenu`
- Type: boolean

Enable console menu. Default to standard login in the console if disabled.

#### consolemsg (required)

- Schema name: `Consolemsg`
- Type: boolean

Deprecated: Please use `consolemsg` attribute in the `system.general` plugin instead.

#### debugkernel (required)

- Schema name: `Debugkernel`
- Type: boolean

Enable debug kernel for additional logging and debugging capabilities.

#### fqdn_syslog (required)

- Schema name: `Fqdn Syslog`
- Type: boolean

Include the full domain name in syslog messages.

#### motd (required)

- Schema name: `Motd`
- Type: string

Message of the day displayed after login.

#### login_banner (required)

- Schema name: `Login Banner`
- Type: string

Banner message displayed before login prompt.
- Must be at most `4096` characters long

#### powerdaemon (required)

- Schema name: `Powerdaemon`
- Type: boolean

Enable the power management daemon for automatic power management.

#### serialconsole (required)

- Schema name: `Serialconsole`
- Type: boolean

Enable serial console access.

#### serialport (required)

- Schema name: `Serialport`
- Type: string

Serial port device for console access.

#### anonstats_token (required)

- Schema name: `Anonstats Token`
- Type: string

Token used for anonymous statistics reporting.

#### serialspeed (required)

- Schema name: `Serialspeed`
- Type: enum (of string)

Baud rate for serial console communication.

#### overprovision (required)

- Schema name: `Overprovision`

Percentage of SSD overprovisioning to reserve for wear leveling.
##### Any of

###### Option 1

- Type: integer
- Value must be greater or equal to `0`

###### Option 2

- Type: null

#### traceback (required)

- Schema name: `Traceback`
- Type: boolean

Enable generation and saving of tracebacks for debugging.

#### uploadcrash (required)

- Schema name: `Uploadcrash`
- Type: boolean

Automatically upload crash reports to iXsystems for analysis.

#### anonstats (required)

- Schema name: `Anonstats`
- Type: boolean

Enable anonymous usage statistics reporting to help improve TrueNAS.

#### sed_user (required)

- Schema name: `Sed User`
- Type: enum (of string)

SED (Self-Encrypting Drive) user type for drive encryption.

#### sysloglevel (required)

- Schema name: `Sysloglevel`
- Type: enum (of string)

Minimum log level for syslog messages. F*EMERG is most critical, F*DEBUG is least critical.

#### syslogservers

- Schema name: `Syslogservers`
- Type: array of object
- Default: []

Configurations for up to two remote syslog servers.
- Must contain a maximum of `2` items
- No Additional Items

##### Each item of this array must be:

##### SyslogServer

- Schema name: `SyslogServer`
- Type: object
- No Additional Properties
###### host (required)

- Schema name: `Host`
- Type: string

Remote syslog server DNS hostname or IP address. Nonstandard port numbers can be used by appending a colon and port number to the hostname, like mysyslogserver:1928. Port 514 is used by default for TCP and UDP transports as per RFC3164; port 6514 is used by default for TLS transport as per RFC5425.

###### transport

- Schema name: `Transport`
- Type: enum (of string)
- Default: "UDP"

Transport Protocol for the remote system log server connection.

###### tls_certificate

- Schema name: `Tls Certificate`
- Default: null

Applies only if `transport` is "TLS". ID of the local certificate to send for mutual TLS (mTLS) connections. `null` indicates one-way TLS in which only the server identified by `host` will need to provide a certificate.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

#### syslog_audit

- Schema name: `Syslog Audit`
- Type: boolean

The remote syslog server(s) will also receive audit messages.

#### isolated_gpu_pci_ids (required)

- Schema name: `Isolated Gpu Pci Ids`
- Type: array of string

List of GPU PCI IDs to isolate from the host system for VM passthrough.
- No Additional Items

##### Each item of this array must be:

- Type: string

#### kernel_extra_options (required)

- Schema name: `Kernel Extra Options`
- Type: string

Additional kernel boot parameters to pass to the Linux kernel.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../../shared/jsonrpc.md)
