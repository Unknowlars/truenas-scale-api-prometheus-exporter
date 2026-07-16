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

Authenticate using one of a variety of mechanisms

NOTE: mechanisms with a _PLAIN suffix indicate that they involve passing plain-text passwords or password-equivalent strings and should not be used on untrusted / insecure transport. Available mechanisms will be expanded in future releases.

params: This takes a single argument consistning of a JSON object with the following keys:

mechanism: the mechanism by which to authenticate to the backend the exact parameters to use vary by mechanism and are described below

PASSWORD_PLAIN username: username with which to authenticate password: password with which to authenticate login_options: dictionary with additional authentication options

API_KEY_PLAIN username: username with which to authenticate api_key: API key string login_options: dictionary with additional authentication options

AUTH_TOKEN_PLAIN token: authentication token string login_options: dictionary with additional authentication options

OTP_TOKEN otp_token: one-time password token. This is only permitted if a previous auth.login_ex call responded with "OTP_REQUIRED".

login_options user_info: boolean - include auth.me output in successful responses.

raises: CallError: a middleware CallError may be raised in the following circumstances.

* An multistep challenge-response authentication mechanism is being used and the specified `mechanism` does not match the expected next step for authentication. In this case the errno will be set to EBUSY.

* OTP_TOKEN mechanism was passed without an explicit request from a previous authentication step. In this case the errno will be set to EINVAL.

* Current authenticator assurance level prohibits the use of the specified authentication mechanism. In this case the errno will be set to EOPNOTSUPP.

returns: JSON object containing the following keys:

response_type: string indicating the results of the current authentication mechanism. This is used to inform client of nature of authentication error or whether further action will be required in order to complete authentication.

<additional keys per response_type>

Notes about response types:

SUCCESS: additional key: user_info: includes auth.me output for the resulting authenticated credentials.

OTP_REQUIRED additional key: username: normalized username of user who must provide an OTP token.

AUTH_ERR Generic authentication error corresponds to PAM_AUTH_ERR and PAM_USER_UNKOWN from libpam. This may be returned if the account does not exist or if the credential is incorrect.

EXPIRED The specified credential is expired and not suitable for authentication.

REDIRECT Authentication must be performed on different server.

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
