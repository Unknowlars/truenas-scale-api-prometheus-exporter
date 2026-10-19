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

<a id="headingADDED"></a>
<a id="ADDED"></a>
### ADDED

- Schema name: `CoreGetJobsAddedEvent`
- Type: object
- No Additional Properties
<a id="headingADDED_id"></a>
<a id="ADDED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

ID of the job that was added.

<a id="headingADDED_fields"></a>
<a id="ADDED_fields"></a>
#### fields (required)

- Schema name: `CoreGetJobsItem`
- Type: object

Complete job information for the newly added job.
- No Additional Properties
<a id="headingADDED_fields_id"></a>
<a id="ADDED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

<a id="headingADDED_fields_message_ids"></a>
<a id="ADDED_fields_message_ids"></a>
##### message_ids (required)

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_message_ids_items"></a>
- Type: object

<a id="headingADDED_fields_method"></a>
<a id="ADDED_fields_method"></a>
##### method (required)

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

<a id="headingADDED_fields_arguments"></a>
<a id="ADDED_fields_arguments"></a>
##### arguments (required)

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

###### Each item of this array must be:

<a id="ADDED_fields_arguments_items"></a>
- Type: object

<a id="headingADDED_fields_transient"></a>
<a id="ADDED_fields_transient"></a>
##### transient (required)

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

<a id="headingADDED_fields_description"></a>
<a id="ADDED_fields_description"></a>
##### description (required)

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
<a id="ADDED_fields_description_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_description_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_description_anyOf_i1)

- Type: null

<a id="headingADDED_fields_abortable"></a>
<a id="ADDED_fields_abortable"></a>
##### abortable (required)

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

<a id="headingADDED_fields_logs_path"></a>
<a id="ADDED_fields_logs_path"></a>
##### logs_path (required)

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
<a id="ADDED_fields_logs_path_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_logs_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_logs_path_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_logs_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_logs_path_anyOf_i1)

- Type: null

<a id="headingADDED_fields_logs_excerpt"></a>
<a id="ADDED_fields_logs_excerpt"></a>
##### logs_excerpt (required)

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
<a id="ADDED_fields_logs_excerpt_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_logs_excerpt_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_logs_excerpt_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_logs_excerpt_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_logs_excerpt_anyOf_i1)

- Type: null

<a id="headingADDED_fields_progress"></a>
<a id="ADDED_fields_progress"></a>
##### progress (required)

- Schema name: `CoreGetJobsItemProgress`
- Type: object

Current progress information for the job.
- No Additional Properties
<a id="headingADDED_fields_progress_percent"></a>
<a id="ADDED_fields_progress_percent"></a>
###### percent (required)

- Schema name: `Percent`

Completion percentage of the job. `null` if not available.
<a id="ADDED_fields_progress_percent_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_progress_percent_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_progress_percent_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_progress_percent_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_progress_percent_anyOf_i1)

- Type: null

<a id="headingADDED_fields_progress_description"></a>
<a id="ADDED_fields_progress_description"></a>
###### description (required)

- Schema name: `Description`

Human-readable description of the current progress. `null` if not available.
<a id="ADDED_fields_progress_description_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_progress_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_progress_description_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_progress_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_progress_description_anyOf_i1)

- Type: null

<a id="headingADDED_fields_progress_extra"></a>
<a id="ADDED_fields_progress_extra"></a>
###### extra (required)

- Schema name: `Extra`
- Type: object

Additional progress information specific to the job type.

<a id="headingADDED_fields_result"></a>
<a id="ADDED_fields_result"></a>
##### result (required)

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

<a id="headingADDED_fields_result_encoding_error"></a>
<a id="ADDED_fields_result_encoding_error"></a>
##### result_encoding_error (required)

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

<a id="headingADDED_fields_error"></a>
<a id="ADDED_fields_error"></a>
##### error (required)

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
<a id="ADDED_fields_error_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_error_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_error_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exception"></a>
<a id="ADDED_fields_exception"></a>
##### exception (required)

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
<a id="ADDED_fields_exception_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exception_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exception_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_exception_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exception_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exc_info"></a>
<a id="ADDED_fields_exc_info"></a>
##### exc_info (required)

Detailed exception information. `null` if no exception occurred.
<a id="ADDED_fields_exc_info_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0"></a>
###### [CoreGetJobsItemExcInfo](#tab-pane_ADDED_fields_exc_info_anyOf_i0)

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_exc_info_anyOf_i0_repr"></a>
<a id="ADDED_fields_exc_info_anyOf_i0_repr"></a>
###### repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
<a id="ADDED_fields_exc_info_anyOf_i0_repr_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0_repr_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exc_info_anyOf_i0_repr_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0_repr_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exc_info_anyOf_i0_repr_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exc_info_anyOf_i0_type"></a>
<a id="ADDED_fields_exc_info_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
<a id="ADDED_fields_exc_info_anyOf_i0_type_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exc_info_anyOf_i0_type_anyOf_i0)

- Type: string

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exc_info_anyOf_i0_type_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exc_info_anyOf_i0_errno"></a>
<a id="ADDED_fields_exc_info_anyOf_i0_errno"></a>
###### errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
<a id="ADDED_fields_exc_info_anyOf_i0_errno_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0_errno_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_exc_info_anyOf_i0_errno_anyOf_i0)

- Type: integer

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i0_errno_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exc_info_anyOf_i0_errno_anyOf_i1)

- Type: null

<a id="headingADDED_fields_exc_info_anyOf_i0_extra"></a>
<a id="ADDED_fields_exc_info_anyOf_i0_extra"></a>
###### extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

<a id="tab-pane_ADDED_fields_exc_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_exc_info_anyOf_i1)

- Type: null

<a id="headingADDED_fields_state"></a>
<a id="ADDED_fields_state"></a>
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

<a id="headingADDED_fields_time_started"></a>
<a id="ADDED_fields_time_started"></a>
##### time_started (required)

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
<a id="ADDED_fields_time_started_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_time_started_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_time_started_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_time_started_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_time_started_anyOf_i1)

- Type: null

<a id="headingADDED_fields_time_finished"></a>
<a id="ADDED_fields_time_finished"></a>
##### time_finished (required)

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
<a id="ADDED_fields_time_finished_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_time_finished_anyOf_i0"></a>
###### [Option 1](#tab-pane_ADDED_fields_time_finished_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_ADDED_fields_time_finished_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_time_finished_anyOf_i1)

- Type: null

<a id="headingADDED_fields_credentials"></a>
<a id="ADDED_fields_credentials"></a>
##### credentials (required)

Authentication credentials used for this job. `null` if no authentication required.
<a id="ADDED_fields_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_ADDED_fields_credentials_anyOf_i0"></a>
###### [CoreGetJobsItemCredentials](#tab-pane_ADDED_fields_credentials_anyOf_i0)

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
<a id="headingADDED_fields_credentials_anyOf_i0_type"></a>
<a id="ADDED_fields_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

<a id="headingADDED_fields_credentials_anyOf_i0_data"></a>
<a id="ADDED_fields_credentials_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

<a id="tab-pane_ADDED_fields_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_ADDED_fields_credentials_anyOf_i1)

- Type: null

<a id="headingCHANGED"></a>
<a id="CHANGED"></a>
### CHANGED

- Schema name: `CoreGetJobsChangedEvent`
- Type: object
- No Additional Properties
<a id="headingCHANGED_id"></a>
<a id="CHANGED_id"></a>
#### id (required)

- Schema name: `Id`
- Type: integer

ID of the job that was updated.

<a id="headingCHANGED_fields"></a>
<a id="CHANGED_fields"></a>
#### fields (required)

- Schema name: `CoreGetJobsItem`
- Type: object

Updated job information with changes.
- No Additional Properties
<a id="headingCHANGED_fields_id"></a>
<a id="CHANGED_fields_id"></a>
##### id (required)

- Schema name: `Id`
- Type: integer

Unique identifier for this job.

<a id="headingCHANGED_fields_message_ids"></a>
<a id="CHANGED_fields_message_ids"></a>
##### message_ids (required)

- Schema name: `Message Ids`
- Type: array

Array of message IDs associated with this job.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_message_ids_items"></a>
- Type: object

<a id="headingCHANGED_fields_method"></a>
<a id="CHANGED_fields_method"></a>
##### method (required)

- Schema name: `Method`
- Type: string

Name of the method/service being executed by this job.

<a id="headingCHANGED_fields_arguments"></a>
<a id="CHANGED_fields_arguments"></a>
##### arguments (required)

- Schema name: `Arguments`
- Type: array

Array of arguments passed to the job method.
- No Additional Items

###### Each item of this array must be:

<a id="CHANGED_fields_arguments_items"></a>
- Type: object

<a id="headingCHANGED_fields_transient"></a>
<a id="CHANGED_fields_transient"></a>
##### transient (required)

- Schema name: `Transient`
- Type: boolean

Whether this is a temporary job that will be automatically cleaned up.

<a id="headingCHANGED_fields_description"></a>
<a id="CHANGED_fields_description"></a>
##### description (required)

- Schema name: `Description`

Human-readable description of what this job does. `null` if not provided.
<a id="CHANGED_fields_description_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_description_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_description_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_abortable"></a>
<a id="CHANGED_fields_abortable"></a>
##### abortable (required)

- Schema name: `Abortable`
- Type: boolean

Whether this job can be cancelled/aborted.

<a id="headingCHANGED_fields_logs_path"></a>
<a id="CHANGED_fields_logs_path"></a>
##### logs_path (required)

- Schema name: `Logs Path`

File system path to detailed job logs. `null` if no logs available.
<a id="CHANGED_fields_logs_path_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_logs_path_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_logs_path_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_logs_path_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_logs_path_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_logs_excerpt"></a>
<a id="CHANGED_fields_logs_excerpt"></a>
##### logs_excerpt (required)

- Schema name: `Logs Excerpt`

Brief excerpt from job logs for quick preview. `null` if no logs available.
<a id="CHANGED_fields_logs_excerpt_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_logs_excerpt_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_logs_excerpt_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_logs_excerpt_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_logs_excerpt_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_progress"></a>
<a id="CHANGED_fields_progress"></a>
##### progress (required)

- Schema name: `CoreGetJobsItemProgress`
- Type: object

Current progress information for the job.
- No Additional Properties
<a id="headingCHANGED_fields_progress_percent"></a>
<a id="CHANGED_fields_progress_percent"></a>
###### percent (required)

- Schema name: `Percent`

Completion percentage of the job. `null` if not available.
<a id="CHANGED_fields_progress_percent_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_progress_percent_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_progress_percent_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_progress_percent_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_progress_percent_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_progress_description"></a>
<a id="CHANGED_fields_progress_description"></a>
###### description (required)

- Schema name: `Description`

Human-readable description of the current progress. `null` if not available.
<a id="CHANGED_fields_progress_description_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_progress_description_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_progress_description_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_progress_description_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_progress_description_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_progress_extra"></a>
<a id="CHANGED_fields_progress_extra"></a>
###### extra (required)

- Schema name: `Extra`
- Type: object

Additional progress information specific to the job type.

<a id="headingCHANGED_fields_result"></a>
<a id="CHANGED_fields_result"></a>
##### result (required)

- Schema name: `Result`
- Type: object

The result data returned by the job upon successful completion.

<a id="headingCHANGED_fields_result_encoding_error"></a>
<a id="CHANGED_fields_result_encoding_error"></a>
##### result_encoding_error (required)

- Schema name: `Result Encoding Error`
- Type: object

Encoding error information if result serialization failed.

<a id="headingCHANGED_fields_error"></a>
<a id="CHANGED_fields_error"></a>
##### error (required)

- Schema name: `Error`

Error message if the job failed. `null` if no error occurred.
<a id="CHANGED_fields_error_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_error_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_error_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_error_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_error_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exception"></a>
<a id="CHANGED_fields_exception"></a>
##### exception (required)

- Schema name: `Exception`

Exception details if the job encountered an exception. `null` if no exception occurred.
<a id="CHANGED_fields_exception_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exception_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exception_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_exception_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exception_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exc_info"></a>
<a id="CHANGED_fields_exc_info"></a>
##### exc_info (required)

Detailed exception information. `null` if no exception occurred.
<a id="CHANGED_fields_exc_info_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0"></a>
###### [CoreGetJobsItemExcInfo](#tab-pane_CHANGED_fields_exc_info_anyOf_i0)

- Schema name: `CoreGetJobsItemExcInfo`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_exc_info_anyOf_i0_repr"></a>
<a id="CHANGED_fields_exc_info_anyOf_i0_repr"></a>
###### repr (required)

- Schema name: `Repr`

String representation of the exception. `null` if no exception occurred.
<a id="CHANGED_fields_exc_info_anyOf_i0_repr_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0_repr_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exc_info_anyOf_i0_repr_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0_repr_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exc_info_anyOf_i0_repr_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exc_info_anyOf_i0_type"></a>
<a id="CHANGED_fields_exc_info_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`

Exception type name. `null` if no exception occurred.
<a id="CHANGED_fields_exc_info_anyOf_i0_type_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0_type_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exc_info_anyOf_i0_type_anyOf_i0)

- Type: string

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0_type_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exc_info_anyOf_i0_type_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exc_info_anyOf_i0_errno"></a>
<a id="CHANGED_fields_exc_info_anyOf_i0_errno"></a>
###### errno (required)

- Schema name: `Errno`

System error number if applicable. `null` otherwise.
<a id="CHANGED_fields_exc_info_anyOf_i0_errno_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0_errno_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_exc_info_anyOf_i0_errno_anyOf_i0)

- Type: integer

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i0_errno_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exc_info_anyOf_i0_errno_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_exc_info_anyOf_i0_extra"></a>
<a id="CHANGED_fields_exc_info_anyOf_i0_extra"></a>
###### extra (required)

- Schema name: `Extra`
- Type: object

Additional exception information.

<a id="tab-pane_CHANGED_fields_exc_info_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_exc_info_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_state"></a>
<a id="CHANGED_fields_state"></a>
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

<a id="headingCHANGED_fields_time_started"></a>
<a id="CHANGED_fields_time_started"></a>
##### time_started (required)

- Schema name: `Time Started`

Timestamp when the job started execution. `null` if not yet started.
<a id="CHANGED_fields_time_started_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_time_started_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_time_started_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_time_started_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_time_started_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_time_finished"></a>
<a id="CHANGED_fields_time_finished"></a>
##### time_finished (required)

- Schema name: `Time Finished`

Timestamp when the job completed execution. `null` if still running or not started.
<a id="CHANGED_fields_time_finished_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_time_finished_anyOf_i0"></a>
###### [Option 1](#tab-pane_CHANGED_fields_time_finished_anyOf_i0)

- Type: string
- Type: Format: date-time

<a id="tab-pane_CHANGED_fields_time_finished_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_time_finished_anyOf_i1)

- Type: null

<a id="headingCHANGED_fields_credentials"></a>
<a id="CHANGED_fields_credentials"></a>
##### credentials (required)

Authentication credentials used for this job. `null` if no authentication required.
<a id="CHANGED_fields_credentials_anyOf"></a>
###### Any of

<a id="tab-pane_CHANGED_fields_credentials_anyOf_i0"></a>
###### [CoreGetJobsItemCredentials](#tab-pane_CHANGED_fields_credentials_anyOf_i0)

- Schema name: `CoreGetJobsItemCredentials`
- Type: object
- No Additional Properties
<a id="headingCHANGED_fields_credentials_anyOf_i0_type"></a>
<a id="CHANGED_fields_credentials_anyOf_i0_type"></a>
###### type (required)

- Schema name: `Type`
- Type: string

Authentication type used for the job.

<a id="headingCHANGED_fields_credentials_anyOf_i0_data"></a>
<a id="CHANGED_fields_credentials_anyOf_i0_data"></a>
###### data (required)

- Schema name: `Data`
- Type: object

Authentication data and credentials for the job.

<a id="tab-pane_CHANGED_fields_credentials_anyOf_i1"></a>
###### [Option 2](#tab-pane_CHANGED_fields_credentials_anyOf_i1)

- Type: null

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
