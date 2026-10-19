---
title: jsonrpc
kind: shared
source_html: jsonrpc.html
---

<a id="json-rpc-2-0-over-websocket-api"></a>
# JSON-RPC 2.0 over WebSocket API

<a id="overview"></a>
## Overview

The TrueNAS API implements the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) protocol over WebSocket for communication between clients and the TrueNAS server. This allows real-time interaction, including method calls and event notifications.
<a id="json-rpc-2-0-protocol"></a>
## JSON-RPC 2.0 Protocol

<a id="communication-mechanism"></a>
### Communication Mechanism

- Messages are exchanged using the **WebSocket protocol**.
- The client initiates a WebSocket connection to the TrueNAS API endpoint.
- The API follows the [JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification for request-response messaging.
<a id="request-and-response-format"></a>
## Request and Response Format

<a id="json-rpc-request-structure"></a>
### JSON-RPC Request Structure

A typical **method call** request from the client to TrueNAS follows this structure:

```javascript
{
  "jsonrpc": "2.0",
  "id": number | string,
  "method": string,
  "params": array
}
```

<a id="example-request"></a>
#### Example Request:

Calling the `system.info` method:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "system.info",
  "params": []
}
```
<a id="json-rpc-response-structure"></a>
### JSON-RPC Response Structure

The TrueNAS API will respond with a standard JSON-RPC response:

```javascript
{
  "jsonrpc": "2.0",
  "id": number | string,
  "result": any
}
```

<a id="example-response"></a>
#### Example Response:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "version": "TrueNAS-25.04",
    "uptime": "15 days"
  }
}
```
<a id="error-response"></a>
### Error Response

If an error occurs, the response format is:

```javascript
{
  "jsonrpc": "2.0",
  "id": number | string,
  "error": {
    "code": number,
    "message": string | null,
    "data": {
      "error": number,
      "errname": string,
      "reason": string,
      "trace": {
        "class": string,
        "frames": array,
        "formatted": string,
        "repr": string
      } | null,
      "extra": array,
      "py_exception": string
    }
  }
}
```

<a id="custom-error-codes"></a>
#### Custom Error Codes

The following custom error codes can be returned in addition to the codes defined by the [JSON-RPC 2.0 specification](https://www.jsonrpc.org/specification#:~:text=NOT%20be%20included.-,5.1%20Error%20object,-When%20a%20rpc).

| Error Code | Message | Description |
| --- | --- | --- |
| -32000 | “too many concurrent calls” | The client has exceeded the allowed concurrent requests. |
| -32001 | “method call error” | There was an error executing the requested method. |
<a id="event-notifications"></a>
## Event Notifications

If the server needs to notify a connected client of an event, it sends a **JSON-RPC Notification** message with the `collection_update` method.

<a id="json-rpc-notification-structure"></a>
### JSON-RPC Notification Structure

<a id="id2"></a>
collection_update

```javascript
 {
   "jsonrpc": "2.0",
   "method": "collection_update",
   "params": {
     "msg": string,
     "collection": string,
     "id": any,
     "fields": {
       "id": string,
       "state": string,
       "progress": {
         "percent": number,
         "description": string
       },
       "result": any,
       "exc_info": {
         "type": string,
         "extra": array | null,
         "repr": string
       },
       "error": string,
       "exception": string
     },
     "extra": object
   }
 }
```
<a id="id3"></a>
notify_unsubscribed

```javascript
 {
   "jsonrpc": "2.0",
   "method": "notify_unsubscribed",
   "params": {
     "collection": string,
     "error": {
       "error": number,
       "errname": string,
       "reason": string,
       "trace": {
         "class": string,
         "frames": array,
         "formatted": string,
         "repr": string
       } | null,
       "extra": array,
       "py_exception": string
     }
   }
 }
```
<a id="example-notification"></a>
#### Example Notification:

```json
{
  "jsonrpc": "2.0",
  "method": "collection_update",
  "params": {
    "collection": "disk.query",
    "event": "CHANGED",
    "fields": {
      "name": "sda",
      "status": "HEALTHY"
    }
  }
}
```
<a id="important-notes-on-notifications"></a>
### Important Notes on Notifications

- **No Response Required**: These notifications do not require a response from the client.
- **Event-Driven**: Notifications are used for updates such as status changes, new log entries, or alerts.
<a id="limitations"></a>
## Limitations

- **Batch Requests Are Not Supported**: Each request must be sent individually; batch calls are not allowed.
- **Error Handling**: Custom error codes are provided for handling specific issues.
