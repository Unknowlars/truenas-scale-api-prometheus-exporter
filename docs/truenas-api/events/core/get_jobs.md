---
title: core.get_jobs
kind: event
source_rst: _sources/api_events_core.get_jobs.rst.txt
source_html: api_events_core.get_jobs.html
required_roles:
  []
---

# core.get_jobs

## Summary

Updates on job changes.

## Required Roles

- None documented.

## Schema

- Type: object

### ADDED

- Schema name: `CoreGetJobsAddedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

ID of the job that was added.

#### fields (required)

- Schema name: `CoreGetJobsItem`
- Type: object

Complete job information for the newly added job.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

##### message_ids (required)

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### method (required)

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

##### arguments (required)

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### transient (required)

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

##### description (required)

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### abortable (required)

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

##### logs_path (required)

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### logs_excerpt (required)

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### progress (required)

- Schema name: `CoreGetJobsItemProgress`
- Type: object

Current progress information for the job.
- No Additional Properties
###### percent (required)

- Schema name: `Percent`

Completion percentage of the job. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### description (required)

- Schema name: `Description`

Human-readable description of the current progress. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### extra (required)

- Schema name: `Extra`
- Type: object

Additional progress information specific to the job type.

##### result (required)

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

##### result_encoding_error (required)

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

##### error (required)

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### exception (required)

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### exc_info (required)

Detailed exception information. `null` if no exception occurred.
###### Any of

####### CoreGetJobsItemExcInfo

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
######## repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### state (required)

- Schema name: `State`
- Type: string

Current execution state of the job.
Examples:

```json
"WAITING"
```
Examples:

```json
"RUNNING"
```
Examples:

```json
"SUCCESS"
```
Examples:

```json
"FAILED"
```
Examples:

```json
"ABORTED"
```

##### time_started (required)

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### time_finished (required)

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### credentials (required)

Authentication credentials used for this job. `null` if no authentication required.
###### Any of

####### CoreGetJobsItemCredentials

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
######## type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

######## data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

####### Option 2

- Type: null

### CHANGED

- Schema name: `CoreGetJobsChangedEvent`
- Type: object
- No Additional Properties
#### id (required)

- Schema name: `Id`
- Type: integer

ID of the job that was updated.

#### fields (required)

- Schema name: `CoreGetJobsItem`
- Type: object

Updated job information with changes.
- No Additional Properties
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

##### message_ids (required)

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### method (required)

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

##### arguments (required)

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

###### Each item of this array must be:

- Type: object

##### transient (required)

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

##### description (required)

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### abortable (required)

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

##### logs_path (required)

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### logs_excerpt (required)

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### progress (required)

- Schema name: `CoreGetJobsItemProgress`
- Type: object

Current progress information for the job.
- No Additional Properties
###### percent (required)

- Schema name: `Percent`

Completion percentage of the job. `null` if not available.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### description (required)

- Schema name: `Description`

Human-readable description of the current progress. `null` if not available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### extra (required)

- Schema name: `Extra`
- Type: object

Additional progress information specific to the job type.

##### result (required)

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

##### result_encoding_error (required)

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

##### error (required)

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### exception (required)

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
###### Any of

####### Option 1

- Type: string

####### Option 2

- Type: null

##### exc_info (required)

Detailed exception information. `null` if no exception occurred.
###### Any of

####### CoreGetJobsItemExcInfo

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
######## repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: string

####### Option 1

- Type: null

####### Option 2

- Type: integer

####### Option 1

- Type: null

####### Option 2

- Type: null

##### state (required)

- Schema name: `State`
- Type: string

Current execution state of the job.
Examples:

```json
"WAITING"
```
Examples:

```json
"RUNNING"
```
Examples:

```json
"SUCCESS"
```
Examples:

```json
"FAILED"
```
Examples:

```json
"ABORTED"
```

##### time_started (required)

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### time_finished (required)

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
###### Any of

####### Option 1

- Type: string
- Type: Format: date-time

####### Option 2

- Type: null

##### credentials (required)

Authentication credentials used for this job. `null` if no authentication required.
###### Any of

####### CoreGetJobsItemCredentials

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
######## type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

######## data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

####### Option 2

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
