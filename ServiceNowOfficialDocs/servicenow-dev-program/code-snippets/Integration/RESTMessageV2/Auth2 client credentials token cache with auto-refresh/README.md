---
title: "Auth2 client credentials token cache with auto-refresh"
aliases:
  - Auth2 client credentials token cache with auto-refresh
tags:
  - servicenow-dev-program
  - code-snippet
  - auth2-client-credentials-token-cache-with-auto-refresh
  - restmessagev2
---

# OAuth 2.0 client-credentials token cache with auto-refresh

## What this solves
When integrating with external APIs, teams often re-implement the OAuth 2.0 client-credentials flow and forget to cache tokens or handle 401 refreshes. This helper:
- Requests an access token from your token endpoint
- Caches the token in a system property with an expiry timestamp
- Adds the Bearer token to RESTMessageV2 requests
- If the call returns 401 (expired token), refreshes once and retries

## Where to use
Script Include in global or scoped apps. Call from Business Rules, Scheduled Jobs, Flow Actions, or Background Scripts.

## How it works
- `getToken(options)` fetches or retrieves a cached token; stores `access_token` and `expires_at` (epoch ms) in system properties.
- `request(options)` executes a resource call with Authorization header; on HTTP 401 it refreshes the token and retries once.
- Token expiry has a 60-second buffer to avoid race on near-expiry tokens.

## Security notes
- For production, store `client_secret` in a secure location (Credentials table or encrypted system property) and **do not** hardcode secrets in scripts.
- This snippet reads/writes system properties under a chosen prefix. Ensure only admins can read/write them.

## Options
For `getToken` and `request`:
- `tokenUrl`: OAuth token endpoint URL
- `clientId`: OAuth client id
- `clientSecret`: OAuth client secret
- `scope`: optional scope string
- `audience`: optional audience parameter (some providers require it)
- `propPrefix`: system property prefix for cache (e.g. `x_acme.oauth.sample`)
- `resource` (request only): target API URL
- `method` (request only): GET/POST/etc (default GET)
- `headers` (request only): object of extra headers
- `body` (request only): request body for POST/PUT/PATCH

## References
- RESTMessageV2 API  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/RESTMessageV2/concept/c_RESTMessageV2API.html
- Direct RESTMessageV2 example  
  https://www.servicenow.com/docs/bundle/zurich-api-reference/page/app-store/dev_portal/API_reference/RESTMessageV2/reference/r_DirectRESTMessageV2Example.html
- OAuth 2.0 profiles in ServiceNow (concept)  
  https://www.servicenow.com/docs/bundle/zurich-integrate-applications/page/integrate/outbound-rest/concept/c_oauth2-authentication.html

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_config|sys_rest_message_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Client-Side Components/UI Actions/Open Record in Alternate Instance/RESTMessageV2/sys_rest_message_fn_config|sys_rest_message_fn_config]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/API for Automatic Group creation/README|API for Automatic Group creation]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Aadhaar Verification/Readme|Aadhaar Verification]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/AzureDevOps/README|AzureDevOps]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Integration/RESTMessageV2/Currency Conversion - Using CurrencyFreaks API/README|Currency Conversion - Using CurrencyFreaks API]]
