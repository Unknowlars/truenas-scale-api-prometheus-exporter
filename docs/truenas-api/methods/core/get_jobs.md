---
title: core.get_jobs
kind: method
source_rst: _sources/api_methods_core.get_jobs.rst.txt
source_html: api_methods_core.get_jobs.html
required_roles:
  []
---

# core.get_jobs

## Summary

Get information about long-running jobs. If authenticated session does not have the FULL_ADMIN role, only jobs owned by the current authenticated session will be returned.

`result` key will have sensitive values redacted by default for external clients.

Redaction behavior may be explicitly specfied via the `extra` query-option `raw_result`. If `raw_result` is True then unredacted result is returned.

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

- Type: object

Examples:

```json
[
    [
        "name",
        "=",
        "bob"
    ]
]
```
Examples:

```json
[
    [
        "OR",
        [
            [
                [
                    "name",
                    "=",
                    "bob"
                ]
            ],
            [
                [
                    "name",
                    "=",
                    "larry"
                ]
            ]
        ]
    ]
]
```

#### Parameter 2: options

#### options

- Schema name: `options`
- Type: object
- Default:
```json
{
  "extra": {},
  "order_by": [],
  "select": [],
  "count": false,
  "get": false,
  "offset": 0,
  "limit": 0,
  "force_sql_filters": false
}
```

Query options including pagination, ordering, and additional parameters.
- No Additional Properties
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: array
- No Additional Items

######### Each item of this array must be:

- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

### Return value

- Schema name: `Result`
#### Any of

##### Option 1

- Type: array of object
- No Additional Items

###### Each item of this array must be:

###### CoreGetJobsItemQueryResultItem

- Schema name: `CoreGetJobsItemQueryResultItem`
- Type: object
- No Additional Properties
####### id

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

####### message_ids

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### method

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

####### arguments

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

######## Each item of this array must be:

- Type: object

####### transient

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

####### description

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### abortable

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

####### logs_path

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### logs_excerpt

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### progress

- Schema name: `CoreGetJobsItemProgress`
- Type: object

Current progress information for the job.
- No Additional Properties
######## percent (required)

- Schema name: `Percent`

Completion percentage of the job. `null` if not available.
######### Any of

########## Option 1

- Type: integer

########## Option 2

- Type: null

######## description (required)

- Schema name: `Description`

Human-readable description of the current progress. `null` if not available.
######### Any of

########## Option 1

- Type: string

########## Option 2

- Type: null

######## extra (required)

- Schema name: `Extra`
- Type: object

Additional progress information specific to the job type.

####### result

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

####### result_encoding_error

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

####### error

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### exception

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
######## Any of

######### Option 1

- Type: string

######### Option 2

- Type: null

####### exc_info

Detailed exception information. `null` if no exception occurred.
######## Any of

######### CoreGetJobsItemExcInfo

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
########## repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

########## type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
########### Any of

############ Option 1

- Type: string

############ Option 2

- Type: null

########## errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
########### Any of

############ Option 1

- Type: integer

############ Option 2

- Type: null

########## extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

######### Option 2

- Type: string

######### Option 1

- Type: null

######### Option 2

- Type: string

######### Option 1

- Type: null

######### Option 2

- Type: integer

######### Option 1

- Type: null

######### Option 2

- Type: null

####### state

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

####### time_started

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
######## Any of

######### Option 1

- Type: string
- Type: Format: date-time

######### Option 2

- Type: null

####### time_finished

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
######## Any of

######### Option 1

- Type: string
- Type: Format: date-time

######### Option 2

- Type: null

####### credentials

Authentication credentials used for this job. `null` if no authentication required.
######## Any of

######### CoreGetJobsItemCredentials

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
########## type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

########## data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

######### Option 2

- Type: null

##### CoreGetJobsItemQueryResultItem

- Type: string

##### Option 3

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: integer

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Type: string

##### Option 2

- Type: null

##### Option 1

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
###### repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
####### Any of

######## Option 1

- Type: integer

######## Option 2

- Type: null

###### extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

##### Option 2

- Type: string

##### CoreGetJobsItemExcInfo

- Type: null

##### Option 2

- Type: string

##### Option 1

- Type: null

##### Option 2

- Type: integer

##### Option 1

- Type: null

##### Option 2

- Type: null

##### Option 1

- Type: string
- Type: Format: date-time

##### Option 2

- Type: null

##### Option 1

- Type: string
- Type: Format: date-time

##### Option 2

- Type: null

##### Option 1

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
###### type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

###### data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

##### Option 2

- Type: null

##### CoreGetJobsItemCredentials

- Schema name: `CoreGetJobsItemQueryResultItem`
- Type: object
- No Additional Properties
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

###### message_ids

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### method

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

###### arguments

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

####### Each item of this array must be:

- Type: object

###### transient

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

###### description

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### abortable

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

###### logs_path

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### logs_excerpt

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### progress

- Type: object

Current progress information for the job.

###### result

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

###### result_encoding_error

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

###### error

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### exception

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
####### Any of

######## Option 1

- Type: string

######## Option 2

- Type: null

###### exc_info

Detailed exception information. `null` if no exception occurred.
####### Any of

######## Option 1

- Type: object

######## Option 2

- Type: null

###### state

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

###### time_started

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### time_finished

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
####### Any of

######## Option 1

- Type: string
- Type: Format: date-time

######## Option 2

- Type: null

###### credentials

Authentication credentials used for this job. `null` if no authentication required.
####### Any of

######## Option 1

- Type: object

######## Option 2

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

- Type: string

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

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

- Type: string
- Type: Format: date-time

##### Option 1

- Type: null

##### Option 2

- Type: object

##### Option 1

- Type: null

##### Option 2

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
