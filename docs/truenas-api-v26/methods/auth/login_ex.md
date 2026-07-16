---
title: auth.login_ex
kind: method
source_rst: _sources/api_methods_auth.login_ex.rst.txt
source_html: api_methods_auth.login_ex.html
required_roles:
  []
---

# auth.login_ex

## Summary

Authenticate using one of a variety of mechanisms.

The mechanism is selected by the `mechanism` field of the request, and the set of supported mechanisms will be expanded in future releases.

.. warning::

Mechanisms with a `_PLAIN` suffix involve passing plain-text passwords or password-equivalent strings and should not be used over untrusted or insecure transport.

The `response_type` of the result indicates the outcome of the current authentication step and whether further action is required to complete authentication:

- `SUCCESS` -- authentication completed and a session was established. - `OTP_REQUIRED` -- the account requires a one-time password; the client must continue authentication by submitting the token via the `OTP_TOKEN` mechanism. - `AUTH_ERR` -- generic authentication failure corresponding to `PAM_AUTH_ERR` and `PAM_USER_UNKNOWN` from libpam. Returned when the account does not exist or the credential is incorrect. - `EXPIRED` -- the supplied credential is expired and not suitable for authentication. - `REDIRECT` -- authentication must be performed on a different server.

A JSON-RPC `error` response (code `-32001`, *Method call error*) is returned instead of a result in the following cases:

- a multistep challenge-response mechanism is in progress and the supplied `mechanism` does not match the expected next step (errno `EBUSY`) - the `OTP_TOKEN` mechanism is used without a preceding step having requested it (errno `EINVAL`) - the current authenticator assurance level prohibits the supplied mechanism (errno `EOPNOTSUPP`)

## Required Roles

- None documented.

## Schema

- Type: object

### Call parameters

- Type: array
- No Additional Items
- Schema name: `Tuple Validation`

#### Parameter 1: login_data

#### login_data

- Schema name: `login_data`

Authentication data specifying mechanism and credentials.

### Return value

- Schema name: `Result`

Authentication response indicating success, failure, or additional steps required.

## Related Docs

- JSON-RPC transport: [JSON-RPC 2.0 over WebSocket API](../../shared/jsonrpc.md)
