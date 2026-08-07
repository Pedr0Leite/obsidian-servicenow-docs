---
title: "SAM SaaS subscription refresh fails with HTTP 403"
aliases:
  - KB3102316
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3102316
kb_number: KB3102316
last_modified: 2026-06-19
---

## Text

# Issue

The scheduled job "SAM - Refresh <Publisher> Subscriptions" fails repeatedly with message: Failed to download subscriptions. Subscription data stops refreshing on a specific date with no ServiceNow-side changes.

# Root cause

The Outbound HTTP Log shows a 200 OK token response followed by a 403 Forbidden data response. This is NOT a credential/token issue—it's a vendor-side authorization condition.

-   The vendor API is rejecting the request because:
-   Authorizing user lacks vendor administrator role (e.g., Company Admin)
-   OAuth app missing required read scope (e.g., organizations:read)
-   Plan tier does not support org-level API access (Enterprise-only endpoints)
-   OAuth app not installed at organization level (reinstall required, not just token refresh)
-   Vendor admin control is blocking the app (app-access policy, IP allowlist, API access disabled)

**Critical:** Token refresh does NOT re-establish organization-level app installation. If that context is broken, a fresh token will still get 403.

# Resolution  
  

**Vendor support required.** The customer must contact their SaaS vendor support to:

-   Review vendor admin audit log around the failure date to identify what changed
-   Confirm the OAuth app has required scopes and roles (organizations:read, admin access)
-   Reinstall/re-authorize the app at the organization level (not just refresh the token)
-   Verify vendor admin controls are not blocking the app (app-access policy, IP allowlist)

Restore access and confirm organization-level API permissions are active

# Diagnostic checks (optional)

-   Run these read-only checks to confirm vendor-side causation:

## Check 1: Confirm HTTP log pattern

Navigate to System Logs > Outbound HTTP Requests (sys\_outbound\_http\_log). Filter by the job's transaction. Confirm: token call = 200 OK, data call = 403 Forbidden. If the 403 response body is empty, raise the HTTP log level and re-run the job to capture the vendor's detailed 403 reason.

## Check 2: Postman validation (customer-side)

Have the customer reproduce the call in Postman using a freshly authorized token as a vendor administrator:

-   Obtain a fresh access token by re-authorizing the OAuth app at the organization level
-   Call the vendor's token inspection endpoint to verify scopes include organizations:read and org\_id is correct
-   Reproduce the failing data call (e.g., GET https://api.vendor.com/v2/orgs/{org\_id}/members)

**If Postman succeeds (200):** ServiceNow's stored token context is stale → proceed to Check 3.

If Postman fails (403): Vendor support must fix org-level authorization.

## Check 3: Re-authorize in ServiceNow

Once vendor confirms org-level access is restored:

-   Open the integration profile > Download Subscription Subflow tab
-   Open Connection & Credential alias > OAuth 2.0 Credentials record
-   Select Get OAuth Token (Related Links) and re-authorize as a vendor administrator
-   Re-run the SAM refresh job—confirm Status = Completed and data is refreshing
