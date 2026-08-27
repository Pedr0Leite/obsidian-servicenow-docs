---
title: "Troubleshooting SAM - Import M365 User Subscriptions job"
aliases:
  - KB2491069
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2491069
kb_number: KB2491069
last_modified: 2026-05-08
---

## Troubleshooting SAM - Import M365 User Subscriptions job

  

### Summary

# Troubleshooting flow:

**Job status first:**

Open the samp\_job\_log for "SAM - Import M365 User Subscriptions" status (completed/failed). This job explicitly states that. 

-   If you're running related SaaS framework jobs, also check sam\_saas\_job\_log (framework's own logs).

**Errors next:**

-   Check syslog for stack traces / SampO365Admin / SampO365RestClient / SAMSaasIntegrationUtils error lines thrown by the client's non-200 responses or script exceptions.  
    Outbound HTTP evidence:
-   Review sys\_outbound\_http\_log for the specific call, URL, status (401/403/404/429/5xx), headers like X-PowerBI-Error-Info, and RequestId. Non-200s will map to the thrown errors above.

**Correlate with backend logs (Splunk/Node)**:

-   Use RequestId / timestamp from the outbound log to pull Node logs around the failing script include (e.g., SampO365Admin, SampO365RestClient); exceptions bubble from \_httpReqExecuteRetry and caller methods.

### Release

ALL

### Instructions

**Common failure categories:**

**A) Prereq/configuration:**

-   SaaS plugin not active: Job aborts with error message and samp\_job\_log.status = failed.  
    Signal: Log text says activate Software Asset Management – SaaS License Management.  
      
    **Fix: Activate plugin sn\_sam\_saas\_int.** 

**NOTE:** After upgrading from pre-Yokohama to Yokohama or Zurich, the following Scheduled jobs fail due to an invalid plugin validation error.

_**Error**:_ Please activate the Software Asset Management - SaaS License Management from the store for Office 365 and Adobe integration to work.

We have an existing internal KB2037538 - PRB1864635. This problem has been fixed and will be available in the next release of the store application, "Software Asset Management - SaaS License Management" (com.sn\_sam\_saas\_int), Version 15.0.17.

https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2037538

**Profile not eligible (Validate Connection not successful)**: Job only processes O365 profiles where custom\_properties contains "validate\_connection": "success".  
  
Signal: Nothing processed; no REST calls.

**NOTE: If we go to the Direct Integration profile for the Microsoft that was created for this job and click on Test connection, we can see the "Connection validation failed for MO365 integration".** 

If we can observe the outbound HTTPS logs and can see that there is a 401 error right after the Test connection action. 

Please refer to the DOC: https://www.servicenow.com/docs/bundle/yokohama-it-asset-management/page/product/software-asset-management2/task/enable-service-principal-authentication-microsoft.html  
  
NOTE: We have a recent PRB1911342 - KB2270532, which says that "Power BI user activity is optional, but it becomes mandatory". With the Y release, a new "Validate the Connection" option was introduced when integrating with Microsoft 365. When a user selects the "Download Activity" option, the system now attempts to validate the connection to Power BI using the endpoint: https://api.powerbi.com/v1.0/myorg/admin/activityevents.

Before the Y release, configuring Power BI was optional; however, with the latest release, Power BI validation appears to have become mandatory, which is not the intended behaviour. 

Currently, if the Power BI API call fails during connection validation, it prevents the execution of any activity-related jobs. This is because the system treats a failure in any of the activity APIs—such as the Reports API or the Power BI API—as a complete validation failure, thereby blocking all related jobs.   
  
To **fix this issue: Run Validate connection until the status is success on the M365 profile.**

**The customer can follow the KB2343420 or KB2270532 to fix this issue.** 

https://support.servicenow.com/kb?id=kb\_article\_view&sys\_kb\_id=4afe1bf5933f2690101833527cba1084

https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2270532

**Wrong/missing REST Message on profile**: importSubscriptionForProfile reads the profile's rest\_message; missing/invalid prevents client creation.

Signal: Early exception before HTTP calls.

**Fix: Ensure the profile references a valid sys\_rest\_message configured for Graph/Power BI.**

**Bad connection alias / credential / base URL**: Publishing/validation checks ensure http\_connection exists, has a credential, and base URL matches product defaults (for microsoft\_365\_subscription it expects graph.microsoft).

Signal: Validation returns explicit messages like "Connection URL is incorrect…" or missing credential errors.

**Fix: Correct the Connection & credential record and base URL, then re-validate.**

**Concurrent run blocked**: Framework blocks when sys\_trigger shows ≥2 active triggers; logs "An instance is already running…".

**Fix: Wait for completion or clear the stuck trigger; the framework also flips previous in-progress job logs to failed.**

**What does the job expect from HTTPS calls (by code path)?**

1) **User & license pull (Graph)**

-   Caller: SampO365Admin.importSubscriptionForProfile() → this.restClient = new sn\_sam\_saas\_int.SampO365RestClient(restMessage.name) → uses client methods below
-   Endpoints/methods configured by REST Message names:
    -   GET Users base endpoint & method (used to paginate users)
    -   POST Users By Batch for license lookups
    -   GET Reports (for other Graph reports if configured)
-   Requests actually sent:
    -   Users page: GET {usersBaseEndPoint}/?$top={N}&$select=userPrincipalName,id,assignedPlans,accountEnabled with pagination via @odata.nextLink (client stores nextLinkUsersPrincipalName)
    -   License details: batched GET /users/{UPN}/licenseDetails?$select=skuPartNumber,skuId,servicePlans (the client constructs per-user requests and executes a batch call)  
        .
-   Expected 200 OK: JSON body with .value array; code parses JSON, advances pagination, and creates/updates samp\_sw\_subscription records per SKU (stamps software\_model when resolvable, sets subscription\_identifier, external\_user\_id, etc.)
-   Unexpected (non-200): the client throws on any status ≠ 200 (including 202/204), so the admin/import flow catches and logs an error; subscriptions previously deactivated are marked active again in the catch path

**2) Power BI Admin usage (optional, when configured)**

-   Caller: same client, via GET Power BI Usage method/endpoint (initialised as powerBIreq, with base endpoint/method resolved from the REST Message)  
    Request style: GET to Admin API (e.g., .../admin/activityevents?...) with Bearer token set by the connection/credential; request and response headers visible in Outbound HTTP logs.
-   Expected 200 OK: JSON (or attachment if saved) → when saveResponseBodyAsAttachment is used, returns sys\_attachment id
-   Unexpected (non-200): client throws; higher layer logs like "Error in validateActivityConnection" (your 401 example)

**3) CSV/attachments for activity/usage**

-   Caller: SampO365Admin.captureUserActivity, captureM365AppsUsageReport, captureManualReportUsageActivity → may save response as attachment and then parse CSV (e.g., csvToArray)  
    Expected 200 OK: attachment saved; downstream parsing updates usage tables.
-   Unexpected: non-200 throws; no attachment; usage not updated

**4) Purchased subscription details**

-   Caller: SampO365Admin.processPurchasedSubsDetails() after REST client is set; maps SKU → purchased/consumed → upserts license detail rows and available rights  
    Expected 200 OK: JSON with skuPartNumber, consumedUnits, prepaidUnits, enabled; tables updated.
-   Unexpected: throw; purchased details remain stale/incomplete

**B) HTTPS status codes: expected vs. unexpected, what they mean here, and exact next steps to TROUBLESHOOT:**

**Tip: Always correlate sys\_outbound\_http\_log status + headers with syslog stack line from SampO365RestClient.\_httpReq/\_httpReqExecuteRetry, then with samp\_job\_log outcome for the scheduled job run**

_**200 OK (Expected)**_

-   Meaning: Graph/Power BI accepted the call; body present (or attachment saved).
-   Outcome: Insert/update pipeline proceeds; subs created/updated; purchased/usage data processed; job likely ends completed in samp\_job\_log
-   If data gaps remain: check SKU→Software Model mapping; unrecognised SKU logic may leave software\_model null (affects install counting)

**202 Accepted / 204 No Content  (Unexpected here)**

-   Meaning: Service accepted without body, but the client treats non-200 as an error and throws.
-   Outcome: Error in logs; job may mark failed.
-   Fix: Use endpoints that return 200 with body/attachment as configured by REST Message methods; avoid "no-content" variants with this client

**400 Bad Request**

-   Meaning: Query invalid (bad $select, dates, or batch body malformed).
-   Signals: Error body in Outbound HTTP; \_httpReq throws; trace in syslog.
-   Fix: Verify REST Message endpoint templates (GET Users/Reports/PowerBI Usage) and any query parameters produced by admin code (date/time, select fields)

**401 Unauthorised:**

-   Common root causes in this job:
    -   Power BI Admin: ServicePrincipalIsNotAllowedByTenantAdminSwitch (tenant disallows SPs) → exactly your case; token is valid but policy blocks it  
        Graph: expired/invalid token or wrong resource/audience.
-   Signals: sys\_outbound\_http\_log 401; headers like X-PowerBI-Error-Info; client throws; admin logs show validation/connection error location
-   Fix:
    -   For Power BI: enable "Allow service principals to use Power BI APIs" or place SP in allowed group; retry.
    -   For Graph: validate connection alias/credential and base URL policy; re-validate profile until custom\_properties.validate\_connection="success"

**The customer can follow the KB2343420 or KB2270532 to fix this issue.** 

https://support.servicenow.com/kb?id=kb\_article\_view&sys\_kb\_id=4afe1bf5933f2690101833527cba1084

https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2270532

**403 Forbidden:**

-   Meaning: Token lacks required app roles/scopes, or the tenant policy denies access.
-   Signals: 403 in Outbound HTTP; body details; throw from client.
-   Fix: Grant required API permissions to the App Registration; ensure tenant switches allow the scenario; re-validate connection on the profile (ValidateConnectionUtils/SAMSaasCommonUtils gating)  
    

See the DOC for more details: [https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/integrate-with-microsoft.html](https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/integrate-with-microsoft.html)

 Important: Minimise security risks and protect information by granting access only to the necessary user or API permissions.

Minimal user permissions
| Process | Required user role in the Microsoft 365 application | Authentication scopes |
| --- | --- | --- |
| Download subscriptions | Application developer | 
-   User.Read.All
-   Organization.Read.All

 |
| Pull user activity | 

-   Power Platform Administrator
-   Application developer

 | Reports.Read.All |
| Reclaim subscriptions | Application developer | 

-   GroupMember.ReadWrite.All
-   LicenseAssignment.ReadWrite.All

 |

**404 Not Found:**

-   Meaning: Wrong endpoint path/method binding from REST Message (e.g., mis-mapped GET Reports, GET Users, GET Power BI Usage), or resource path not valid for the tenant.
-   Signals: 404; throw; early failure before insert/update.
-   Fix: Check the sys\_rest\_message and its method names & endpoints used by the client initialisers (getHttpMethod/getEndPoint for each named method)  
      
    

**A 404 in this M365 job is almost always due to a wrong endpoint path or the service not being enabled. The code is strict: only a 200 OK is considered success.  
**

-   A 404 from Graph or Power BI does not mean the user doesn't exist in ServiceNow.
-   It means the HTTP request endpoint is invalid for that tenant / API version/resource.
-   Since `SampO365RestClient._httpReq` throws on any non-200, the error bubbles up, and the job fails in `samp_job_log`

**Where 404s can originate in this job?**

**A) If the REST Message in your instance has misconfigured** endpoint paths (e.g., missing `/v1.0/` prefix, typo in `users/{id}/licenseDetails`), the HTTP call returns 404.

**Expected vs. Unexpected:**

-   Expected: `[https://graph.microsoft.com/v1.0/users/](https://graph.microsoft.com/v1.0/users/){id}/licenseDetails?...`
-   Unexpected: `[https://graph.microsoft.com/v1.0/user/](https://graph.microsoft.com/v1.0/user/){id}/licenseDetails` (typo → 404).

**B) Incorrect API resource**

-   For user/license calls, the scripts expect:

1.  GET `/users?$select=userPrincipalName,id,...`
2.  GET `/users/{UPN}/licenseDetails?...`

-   For Power BI, it expects:
-   GET `/v1.0/myorg/admin/activityevents?...`
-   If your profile is mis-scoped (using the wrong tenant ID, wrong path, like `/me/` instead of `/users/`), the endpoint may not exist → 404.

### C) Tenant/service mismatch

-   Example: Power BI Admin APIs are only valid for tenant-level admin accounts.
-   If your tenant hasn't enabled the Power BI service or the admin API, calls to `/admin/activityevents` may return 404.
-   You'll see headers like `X-PowerBI-Error-Info: ResourceNotFound`.

**D) Profile connection mispointing**

-   If the connection alias (in `http_connection`) points to the wrong base URL, e.g.,

1.  `https://graph.microsoftonline.com/...` (legacy, invalid) instead of `https://graph.microsoft.com/...`
2.  or missing `.com` in the URL

-   → 404 at the HTTP layer, even though the token is valid.

## How to detect a 404 issue systematically

1\. Check `sys_outbound_http_log`: Status: 404; Endpoint: look carefully at the URL being called. 

-   Example bad endpoint: https://graph.microsoft.com/v1.0/user/licenseDetails
-   Should be: https://graph.microsoft.com/v1.0/users/{id}/licenseDetails

 2. Check the syslog for the stack trace from `SampO365RestClient._httpReq`. And the Logs will show the endpoint string (`name + ' endpoint : ' + endpoint`) just before execution

3\. Validate the REST Message config: Go to the profile's REST Message → check method names and endpoints.

Ensure method labels match what the script expects: "Default GET", "GET Users", "GET Reports", "GET PowerBI Usage".

4\. Check tenant/service availability: Verify your Azure AD tenant actually supports the API you're hitting. For the Power BI Admin API, ensure Power BI is enabled in the tenant.

**Fixing a 404:** 

-   REST Message correction:
    -   Ensure endpoints match Microsoft docs (Graph v1.0).
    -   Typical ones for this job:
        -   GET https://graph.microsoft.com/v1.0/users
        -   GET https://graph.microsoft.com/v1.0/users/{id}/licenseDetails
        -   POST https://graph.microsoft.com/v1.0/$batch (for batched license lookups)
        -   GET https://api.powerbi.com/v1.0/myorg/admin/activityevents?...
-   Connection alias correction:
    -   In http\_connection, confirm the Connection URL contains graph.microsoft.com (as defined in SAMSaasCommonUtils.defaultBaseURL)  
        Any deviation → job validation fails or runtime 404.
-   Profile validation:
    -   Run Validate Connection on the profile.
    -   Only when custom\_properties.validate\_connection = success will the job process it
-   Service enablement:
    -   If Power BI APIs return 404, enable the Power BI Admin API in your tenant.
    -   Verify account/service principal has Admin API access.

**409 Conflict:**

-   Meaning: Rare at Graph/Power BI read endpoints; if seen, treat as unexpected non-200.
-   Fix: Inspect body; usually indicates request semantics conflict—correct and retry. (Client will throw on first sighting)  
      
    

**429 Too Many Requests**

-   Meaning: Throttled by Graph/Power BI.
-   Client behaviour: automatic retry with exponential backoff (1 min → 2 → 4); still throws if it never sees a 200  
    Fix: Reduce concurrency/scope; run outside peak; split profiles; widen job window. You'll see multiple attempts in logs.

**5xx Server Errors**

-   Meaning: Transient service faults.
-   Signals: 5xx in Outbound; throw.
-   Fix: Re-run later; consider scheduling away from maintenance windows. No auto-retry unless surfaced as 429  
    

Note: Any status ≠ 200 triggers `_httpReq` to throw:

if (status !== 200) {  
   throw new Error(res.getBody());  
}

  
**Script: SamImportUserSubscriptionsO365: Error: SampO365AdminUnhandled exception for profile : xxxxxxxxxxxxxxxxxxxxxxx**

 The Microsoft 365 subscription import job (`SamImportUserSubscriptionsO365`) fails because the Azure app registration client secret used for authentication has expired.

 Symptoms

-   Go to syslog.FILTER and filter the exact timeframe with Keyword SAMP. 
-   Errors are logged in the system log during the O365 subscription import run.
-   The following error message appears:

SamImportUserSubscriptionsO365: Error: SampO365AdminUnhandled exception for profile : <profile\_sys\_id> :   
com.glide.communications.ProcessingException: User Not Authenticated.   
Could not retrieve a new access token with the refresh token.   
invalid\_client, AADSTS7000222: The provided client secret keys for app '<app\_id>' are expired.   
Visit the Azure portal to create new keys for your app: https://aka.ms/NewClientSecret,   
or consider using certificate credentials for added security: https://aka.ms/certCreds.   
Trace ID: <trace\_id> Correlation ID: <correlation\_id> Timestamp: <timestamp>

-   The import profile fails to connect to the Microsoft Graph API.
-   No new subscription records are updated in the samp\_sw\_subscription table.

Please follow the **[KB2536403](https://support.servicenow.com/kb?sys_kb_id=8f5abe9947d8f6dcf64de825126d4339&id=kb_article_view)** to resolve this issue. 

**c) Data/Mapping Issues:** 

-   Unrecognised SKUs: Stored without software\_model, install counting fails.
-   User linkage issues: Disabled or missing UPNs leave subscriptions without a user.
-   Suite vs standalone mismatch: Install counting differs if suite logic vs norm\_product.
-   Purchased details missing: Failure in purchased subscription API call → rights not updated.
-   Reclamation misflags: Subscriptions may be stamped as stale\_license based on thresholds.

**Validation After Fix**

1.  Rerun Validate connection on profile → must show success.
2.  Trigger job → confirm samp\_job\_log ends as completed.
3.  Verify new samp\_sw\_subscription rows populated with software\_model and user.
4.  Check install counts updated in number\_of\_installs.
5.  Review sam\_saas\_job\_log for downstream activity/consumption job status.

Appendix:

**Key Tables:**

-   samp\_job\_log → Job status.
-   syslog → Error traces.
-   sys\_outbound\_http\_log → REST call details.
-   samp\_sw\_subscription → Imported subs.
-   cmdb\_sam\_sw\_install → Install counts.

**Key Script Includes:**

-   SamImportUserSubscriptionsO365 → Job driver.
-   SampO365Admin → Import orchestrator.
-   SampO365RestClient → HTTP executor with retry.
-   SampSubscriptionUtil → Install count updater.
-   SAMSaasIntegrationUtils, SAMSaasCommonUtils → Framework utilities.

### Related Links

# Integrating with Microsoft 365: https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/integrate-with-microsoft.html
