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

<a id="headingCall_parameters"></a>
<a id="Call_parameters"></a>
### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: filters

<a id="Call_parameters_items_i0"></a>
#### filters

- Schema name: `filters`
- Type: array
- Default: []

List of filters for query results. See API documentation for "Query Methods" for more guidance.
- No Additional Items

##### Each item of this array must be:

<a id="Call_parameters_items_i0_items"></a>
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
                "name",
                "=",
                "bob"
            ],
            [
                "name",
                "=",
                "larry"
            ]
        ]
    ]
]
```

#### Parameter 2: options

<a id="Call_parameters_items_i1"></a>
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
<a id="headingCall_parameters_items_i1_extra"></a>
<a id="Call_parameters_items_i1_extra"></a>
##### extra

- Schema name: `Extra`
- Type: object
- Default: {}

Extra options are defined on a per-endpoint basis and are described in the documentation for the associated query method.

<a id="headingCall_parameters_items_i1_order_by"></a>
<a id="Call_parameters_items_i1_order_by"></a>
##### order_by

- Schema name: `Order By`
- Type: array of string
- Default: []

An array of field names describing the manner in which query results should be ordered. The field names may also have one of more of the following special prefixes: `-` (reverse sort direction), `nulls_first:` (place any null values at the head of the results list), `nulls_last:` (place any null values at the tail of the results list).
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_order_by_items"></a>
- Type: string

Examples:

```json
[
    "size",
    "-devname",
    "nulls_first:-expiretime"
]
```

<a id="headingCall_parameters_items_i1_select"></a>
<a id="Call_parameters_items_i1_select"></a>
##### select

- Schema name: `Select`
- Type: array
- Default: []

An array of field names specifying the exact fields to include in the query return. The dot character `.` may be used to explicitly select only subkeys of the query result.
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items"></a>
<a id="Call_parameters_items_i1_select_items_anyOf"></a>
###### Any of

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i0"></a>
###### [Option 1](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i0)

- Type: string

<a id="tab-pane_Call_parameters_items_i1_select_items_anyOf_i1"></a>
###### [Option 2](#tab-pane_Call_parameters_items_i1_select_items_anyOf_i1)

- Type: array
- No Additional Items

###### Each item of this array must be:

<a id="Call_parameters_items_i1_select_items_anyOf_i1_items"></a>
- Type: object

Examples:

```json
[
    "username",
    "Authentication.status"
]
```

<a id="headingCall_parameters_items_i1_count"></a>
<a id="Call_parameters_items_i1_count"></a>
##### count

- Schema name: `Count`
- Type: boolean
- Default: false

Return a numeric value representing the number of items that match the specified `query-filters`.

<a id="headingCall_parameters_items_i1_get"></a>
<a id="Call_parameters_items_i1_get"></a>
##### get

- Schema name: `Get`
- Type: boolean
- Default: false

Return the JSON object of the first result matching the specified `query-filters`. The query fails if there specified `query-filters` return no results.

<a id="headingCall_parameters_items_i1_offset"></a>
<a id="Call_parameters_items_i1_offset"></a>
##### offset

- Schema name: `Offset`
- Type: integer
- Default: 0

This specifies the beginning offset of the results array. When combined with the `limit` query-option it may be used to implement pagination of large results arrays. WARNING: some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_limit"></a>
<a id="Call_parameters_items_i1_limit"></a>
##### limit

- Schema name: `Limit`
- Type: integer
- Default: 0

This specifies the maximum number of results matching the specified `query-filters` to return. When combined wtih the `offset` query-option it may be used to implement pagination of large results arrays. WARNING: Some query methods provide volatile results and the onus is on the developer to understand whether pagination is appropriate for a particular query API method.

<a id="headingCall_parameters_items_i1_force_sql_filters"></a>
<a id="Call_parameters_items_i1_force_sql_filters"></a>
##### force_sql_filters

- Schema name: `Force Sql Filters`
- Type: boolean
- Default: false

Force use of SQL for result filtering to reduce response time. May not work for all methods.

<a id="headingReturn_value"></a>
<a id="Return_value"></a>
### Return value

- Schema name: `Result`
<a id="Return_value_anyOf"></a>
#### Any of

<a id="tab-pane_Return_value_anyOf_i0"></a>
##### [Option 1](#tab-pane_Return_value_anyOf_i0)

- Type: array of object
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items"></a>
###### CoreGetJobsItemQueryResultItem

- Schema name: `CoreGetJobsItemQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_id"></a>
<a id="Return_value_anyOf_i0_items_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

<a id="headingReturn_value_anyOf_i0_items_message_ids"></a>
<a id="Return_value_anyOf_i0_items_message_ids"></a>
###### message_ids

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_message_ids_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_method"></a>
<a id="Return_value_anyOf_i0_items_method"></a>
###### method

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

<a id="headingReturn_value_anyOf_i0_items_arguments"></a>
<a id="Return_value_anyOf_i0_items_arguments"></a>
###### arguments

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i0_items_arguments_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i0_items_transient"></a>
<a id="Return_value_anyOf_i0_items_transient"></a>
###### transient

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

<a id="headingReturn_value_anyOf_i0_items_description"></a>
<a id="Return_value_anyOf_i0_items_description"></a>
###### description

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
<a id="Return_value_anyOf_i0_items_description_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_description_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_description_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_abortable"></a>
<a id="Return_value_anyOf_i0_items_abortable"></a>
###### abortable

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

<a id="headingReturn_value_anyOf_i0_items_logs_path"></a>
<a id="Return_value_anyOf_i0_items_logs_path"></a>
###### logs_path

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
<a id="Return_value_anyOf_i0_items_logs_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_logs_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_logs_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_logs_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_logs_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_logs_excerpt"></a>
<a id="Return_value_anyOf_i0_items_logs_excerpt"></a>
###### logs_excerpt

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
<a id="Return_value_anyOf_i0_items_logs_excerpt_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_logs_excerpt_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_logs_excerpt_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_logs_excerpt_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_logs_excerpt_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_progress"></a>
<a id="Return_value_anyOf_i0_items_progress"></a>
###### progress

- Schema name: `CoreGetJobsItemProgress`
- Type: object

Current progress information for the job.
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_progress_percent"></a>
<a id="Return_value_anyOf_i0_items_progress_percent"></a>
###### percent (required)

- Schema name: `Percent`

Completion percentage of the job. `null` if not available.
<a id="Return_value_anyOf_i0_items_progress_percent_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_progress_percent_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_progress_percent_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_progress_percent_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_progress_percent_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_progress_description"></a>
<a id="Return_value_anyOf_i0_items_progress_description"></a>
###### description (required)

- Schema name: `Description`

Human-readable description of the current progress. `null` if not available.
<a id="Return_value_anyOf_i0_items_progress_description_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_progress_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_progress_description_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_progress_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_progress_description_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_progress_extra"></a>
<a id="Return_value_anyOf_i0_items_progress_extra"></a>
###### extra (required)

- Schema name: `Extra`
- Type: object

Additional progress information specific to the job type.

<a id="headingReturn_value_anyOf_i0_items_result"></a>
<a id="Return_value_anyOf_i0_items_result"></a>
###### result

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

<a id="headingReturn_value_anyOf_i0_items_result_encoding_error"></a>
<a id="Return_value_anyOf_i0_items_result_encoding_error"></a>
###### result_encoding_error

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

<a id="headingReturn_value_anyOf_i0_items_error"></a>
<a id="Return_value_anyOf_i0_items_error"></a>
###### error

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
<a id="Return_value_anyOf_i0_items_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_exception"></a>
<a id="Return_value_anyOf_i0_items_exception"></a>
###### exception

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
<a id="Return_value_anyOf_i0_items_exception_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_exception_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_exception_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_exception_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_exception_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_exc_info"></a>
<a id="Return_value_anyOf_i0_items_exc_info"></a>
###### exc_info

Detailed exception information. `null` if no exception occurred.
<a id="Return_value_anyOf_i0_items_exc_info_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0"></a>
###### [CoreGetJobsItemExcInfo](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0)

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_exc_info_anyOf_i0_repr"></a>
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_repr"></a>
###### repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_repr_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_repr_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_repr_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_repr_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_repr_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_exc_info_anyOf_i0_type"></a>
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_type_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_type_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_type_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_exc_info_anyOf_i0_errno"></a>
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_errno"></a>
###### errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_errno_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_errno_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_errno_anyOf_i0)

- Type: integer

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_errno_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i0_errno_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_exc_info_anyOf_i0_extra"></a>
<a id="Return_value_anyOf_i0_items_exc_info_anyOf_i0_extra"></a>
###### extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

<a id="tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_exc_info_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_state"></a>
<a id="Return_value_anyOf_i0_items_state"></a>
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

<a id="headingReturn_value_anyOf_i0_items_time_started"></a>
<a id="Return_value_anyOf_i0_items_time_started"></a>
###### time_started

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
<a id="Return_value_anyOf_i0_items_time_started_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_time_started_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_time_started_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i0_items_time_started_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_time_started_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_time_finished"></a>
<a id="Return_value_anyOf_i0_items_time_finished"></a>
###### time_finished

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
<a id="Return_value_anyOf_i0_items_time_finished_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_time_finished_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i0_items_time_finished_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i0_items_time_finished_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_time_finished_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i0_items_credentials"></a>
<a id="Return_value_anyOf_i0_items_credentials"></a>
###### credentials

Authentication credentials used for this job. `null` if no authentication required.
<a id="Return_value_anyOf_i0_items_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_anyOf_i0"></a>
###### [CoreGetJobsItemCredentials](#tab-pane_Return_value_anyOf_i0_items_credentials_anyOf_i0)

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i0_items_credentials_anyOf_i0_type"></a>
<a id="Return_value_anyOf_i0_items_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

<a id="headingReturn_value_anyOf_i0_items_credentials_anyOf_i0_data"></a>
<a id="Return_value_anyOf_i0_items_credentials_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

<a id="tab-pane_Return_value_anyOf_i0_items_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i0_items_credentials_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i1"></a>
##### [CoreGetJobsItemQueryResultItem](#tab-pane_Return_value_anyOf_i1)

- Schema name: `CoreGetJobsItemQueryResultItem`
- Type: object
- No Additional Properties
<a id="headingReturn_value_anyOf_i1_id"></a>
<a id="Return_value_anyOf_i1_id"></a>
###### id

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

<a id="headingReturn_value_anyOf_i1_message_ids"></a>
<a id="Return_value_anyOf_i1_message_ids"></a>
###### message_ids

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_message_ids_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_method"></a>
<a id="Return_value_anyOf_i1_method"></a>
###### method

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

<a id="headingReturn_value_anyOf_i1_arguments"></a>
<a id="Return_value_anyOf_i1_arguments"></a>
###### arguments

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

###### Each item of this array must be:

<a id="Return_value_anyOf_i1_arguments_items"></a>
- Type: object

<a id="headingReturn_value_anyOf_i1_transient"></a>
<a id="Return_value_anyOf_i1_transient"></a>
###### transient

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

<a id="headingReturn_value_anyOf_i1_description"></a>
<a id="Return_value_anyOf_i1_description"></a>
###### description

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
<a id="Return_value_anyOf_i1_description_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_description_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_description_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_abortable"></a>
<a id="Return_value_anyOf_i1_abortable"></a>
###### abortable

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

<a id="headingReturn_value_anyOf_i1_logs_path"></a>
<a id="Return_value_anyOf_i1_logs_path"></a>
###### logs_path

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
<a id="Return_value_anyOf_i1_logs_path_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_logs_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_logs_path_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_logs_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_logs_path_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_logs_excerpt"></a>
<a id="Return_value_anyOf_i1_logs_excerpt"></a>
###### logs_excerpt

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
<a id="Return_value_anyOf_i1_logs_excerpt_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_logs_excerpt_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_logs_excerpt_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_logs_excerpt_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_logs_excerpt_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_progress"></a>
<a id="Return_value_anyOf_i1_progress"></a>
###### progress

- Type: object

Current progress information for the job.

<a id="headingReturn_value_anyOf_i1_result"></a>
<a id="Return_value_anyOf_i1_result"></a>
###### result

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

<a id="headingReturn_value_anyOf_i1_result_encoding_error"></a>
<a id="Return_value_anyOf_i1_result_encoding_error"></a>
###### result_encoding_error

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

<a id="headingReturn_value_anyOf_i1_error"></a>
<a id="Return_value_anyOf_i1_error"></a>
###### error

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
<a id="Return_value_anyOf_i1_error_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_error_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_error_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_exception"></a>
<a id="Return_value_anyOf_i1_exception"></a>
###### exception

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
<a id="Return_value_anyOf_i1_exception_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_exception_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_exception_anyOf_i0)

- Type: string

<a id="tab-pane_Return_value_anyOf_i1_exception_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_exception_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_exc_info"></a>
<a id="Return_value_anyOf_i1_exc_info"></a>
###### exc_info

Detailed exception information. `null` if no exception occurred.
<a id="Return_value_anyOf_i1_exc_info_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_exc_info_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_exc_info_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_exc_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_exc_info_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_state"></a>
<a id="Return_value_anyOf_i1_state"></a>
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

<a id="headingReturn_value_anyOf_i1_time_started"></a>
<a id="Return_value_anyOf_i1_time_started"></a>
###### time_started

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
<a id="Return_value_anyOf_i1_time_started_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_time_started_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_time_started_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i1_time_started_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_time_started_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_time_finished"></a>
<a id="Return_value_anyOf_i1_time_finished"></a>
###### time_finished

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
<a id="Return_value_anyOf_i1_time_finished_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_time_finished_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_time_finished_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_Return_value_anyOf_i1_time_finished_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_time_finished_anyOf_i1)

- Type: null

<a id="headingReturn_value_anyOf_i1_credentials"></a>
<a id="Return_value_anyOf_i1_credentials"></a>
###### credentials

Authentication credentials used for this job. `null` if no authentication required.
<a id="Return_value_anyOf_i1_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_Return_value_anyOf_i1_credentials_anyOf_i0"></a>
###### [Option 1](#tab-pane_Return_value_anyOf_i1_credentials_anyOf_i0)

- Type: object

<a id="tab-pane_Return_value_anyOf_i1_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_Return_value_anyOf_i1_credentials_anyOf_i1)

- Type: null

<a id="tab-pane_Return_value_anyOf_i2"></a>
##### [Option 3](#tab-pane_Return_value_anyOf_i2)

- Type: integer

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
