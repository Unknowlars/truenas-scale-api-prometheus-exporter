---
title: audit.config
kind: method
source_rst: _sources/api_methods_audit.config.rst.txt
source_html: api_methods_audit.config.html
required_roles:
  - SYSTEM_AUDIT_READ
---

# audit.config

## Required Roles

- `SYSTEM_AUDIT_READ`

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items

### Return value

- Schema name: `AuditEntry`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for the audit configuration.

#### retention (required)

- Schema name: `Retention`
- Type: integer

Number of days to retain local audit messages.
- Value must be greater or equal to `1` and lesser or equal to `30`

#### reservation (required)

- Schema name: `Reservation`
- Type: integer

Size in GiB of refreservation to set on ZFS dataset where the audit databases are stored. The refreservation specifies the minimum amount of space guaranteed to the dataset, and counts against the space available for other datasets in the zpool where the audit dataset is located.
- Value must be greater or equal to `0` and lesser or equal to `100`

#### quota (required)

- Schema name: `Quota`
- Type: integer

Size in GiB of the maximum amount of space that may be consumed by the dataset where the audit dabases are stored.
- Value must be greater or equal to `0` and lesser or equal to `100`

#### quota_fill_warning (required)

- Schema name: `Quota Fill Warning`
- Type: integer

Percentage used of dataset quota at which to generate a warning alert.
- Value must be greater or equal to `5` and lesser or equal to `80`

#### quota_fill_critical (required)

- Schema name: `Quota Fill Critical`
- Type: integer

Percentage used of dataset quota at which to generate a critical alert.
- Value must be greater or equal to `50` and lesser or equal to `95`

#### remote_logging_enabled (required)

- Schema name: `Remote Logging Enabled`
- Type: boolean

Logging to a remote syslog server is enabled on TrueNAS, and audit logs are included in what is sent remotely.

#### space (required)

- Schema name: `AuditEntrySpace`
- Type: object

ZFS dataset properties relating space used and available for the dataset where the audit databases are written.
- No Additional Properties
##### used (required)

- Schema name: `Used`
- Type: integer

Total space used by the audit dataset in bytes.

##### used_by_dataset (required)

- Schema name: `Used By Dataset`
- Type: integer

Space used by the dataset itself (not including snapshots or reservations) in bytes.

##### used_by_reservation (required)

- Schema name: `Used By Reservation`
- Type: integer

Space reserved for the dataset in bytes.

##### used_by_snapshots (required)

- Schema name: `Used By Snapshots`
- Type: integer

Space used by snapshots of the audit dataset in bytes.

##### available (required)

- Schema name: `Available`
- Type: integer

Available space remaining for the audit dataset in bytes.

#### enabled_services (required)

- Schema name: `AuditEntryEnabledServices`
- Type: object

JSON object with key denoting service, and value containing a JSON array of what aspects of this service are being audited. In the case of the SMB audit, the list contains share names of shares for which auditing is enabled.
- No Additional Properties
##### MIDDLEWARE (required)

- Schema name: `Middleware`
- Type: array

Array of middleware audit event types that are enabled.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### SMB (required)

- Schema name: `Smb`
- Type: array

Array of SMB share names or audit event types that are enabled.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### SUDO (required)

- Schema name: `Sudo`
- Type: array of string

Array of sudo commands or users that are being audited.
- No Additional Items

###### Each item of this array must be:

- Type: string

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
