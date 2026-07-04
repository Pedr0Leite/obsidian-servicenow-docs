---
title: "Troubleshooting the SAM – Import Adobe User Subscriptions JOB"
aliases:
  - KB2468178
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2468178
kb_number: KB2468178
last_modified: 2026-05-08
---

## Troubleshooting the SAM – Import Adobe User Subscriptions JOB

  

### Summary

When the SAM – Import Adobe User Subscriptions fails, but `samp_job_log` shows little or no error text, go straight to:

1.  `sys_outbound_http_log` filtered on `hostname=usermanagement.adobe.io` (and timestamp range of the run)
2.  Node/Splunk logs for the same time window (transaction ID from the outbound log helps)
3.  Cross-map the HTTP code to the root cause and fix below

Why the job log can be empty: the job wrapper writes `status` and logs errors via `SampLogger` (system logs), but doesn't provide a detailed error message in `samp_job_log.`Inside Adobe import, exceptions are rethrown as a single "Unhandled exception for profile …" message, which also routes to logs.

### Facts

When customer notices that the JOB - **SAM – Import Adobe User Subscriptions,** they can see the samp\_job\_log table status for this job which is resulted in FAILURE. This is a Direct SaaS Integration between ServiceNow and Adobe User Management API (`usermanagement.adobe.io`).Profile type: `adobe_subscription`.  
  

Adobe Integration supports OAuth 2.0 and JWT (Service Account) authentication. Default is OAuth, but most enterprise setups use JWT + certificate (.pfx)  
  

Logs to Check:

1.  samp\_job\_log – High-level job result (often shows only _failed_).
2.  sys\_outbound\_http\_log – Detailed HTTP request/response to Adobe API (status codes 401, 403, 404, 429, 500).
3.  System/Transaction/Splunk logs – Capture full exception stack traces (e.g., _Unhandled exception for profile …_).  
      
    

**Why job log sometimes show no error message (and how to get more)**

The Wrapper job Creates a record in `samp_job_log`, runs `SamImportUserSubscriptionsAdobe().process()`, sets `status` to _completed_ or _failed_. On exceptions, it logs via `SampLogger.error(jobName, e)` and sets `status='failed'`—but does not save the exception text into the job log record.

Adobe import: Catches any exception, re-activates subscriptions to leave data consistent, then re-throws a single "Unhandled exception for profile … : <ex>" error.

Actionable: Turn on debug logging for SAM (`com.snc.samp.debug=true`): `SampLogger` honors this flag for info/debug messages. Always pair the job log with `sys_outbound_http_log` and Node/Splunk.

* * *

### Release

ALL

### Instructions

When the job `SAM - Import Adobe User Subscriptions` fails, follow this structured troubleshooting approach:

### Step 1 – Check the Job Log (`samp_job_log`)

-   Navigate to SAM → SaaS License Management → Job Logs.
-   Locate the failing job entry.
-   Review the Status and Message fields for high-level error context.

Examples:

-   _Plugin not activated_
-   _Unhandled exception for profile_
-   _Please activate SaaS License Management Integration_

### Step 2 – Check Outbound REST Logs (`sys_outbound_http_log`)

-   Navigate to System Logs → Outbound HTTP Requests.
-   Filter by Adobe Integration Profile or by job timestamp.
-   Look for HTTP response codes:
-   401 Unauthorised → Invalid credentials, expired token, wrong auth type.
-   403 Forbidden → API permission issue in Adobe Console.
-   404 Not Found → Incorrect Adobe API endpoint.
-   429 Too Many Requests → Adobe API throttling.
-   500 Internal Server Error → Adobe-side outage or transient failure.

These errors directly map to issues in Adobe API calls made via `SampAdobeAdmin` script include.

### Step 3 – Analyse Error Response

-   Open the Response Body in the outbound log.
-   Adobe errors usually include a JSON response with an error code and description.
-   Use the error to map the root cause:
    -   Example:{  
          "error": "invalid\_client",  
          "error\_description": "Invalid client\_id or client\_secret"  
        }
        

**Fix: Re-check Adobe Integration Profile credentials.  
**

### Step 4 – Review Backend Logs (If Needed)

-   System Logs → Application Logs
-   Node Transaction Logs
-   MID Server Logs (if Adobe API call routed via MID).
-   These are useful for JavaScript exceptions thrown by script includes (`SampAdobeAdmin`, `SAMSaasIntegrationUtils`).
-   Example messages:
-   `Unhandled exception for profile: <sys_id>`
-   `Cannot find the profile type configuration in the script routing table`

**Troubleshooting Adobe SAM Job Errors:**

### Common Errors & Fixes

**ISSUE 1: Plugin Not Activated:** 

Error: `Please activate the Software Asset Management - SaaS License Management from the store for Adobe integration to work`

Resolution: Activate `sn_sam_saas_int` plugin.

NOTE: After upgrading from pre-Yokohama to Yokohama or Zurich, the following Scheduled jobs fail due to an invalid plugin validation error.

_Error: Please activate the Software Asset Management - SaaS License Management from the store for Office 365 and Adobe integration to work.  
_  
We have a Related Problem: PRB1864635 - KB2037538, which has the updateset fix for this issue.   
  

**ISSUE 2: 401 Unauthorised:** 

**Cause**: Invalid Client ID/Secret, Expired or revoked token and Wrong authentication type selected (OAuth vs JWT). 

**Resolution**:

Verify Adobe Developer Console credentials.

Re-generate token/certificate.

Run the Validate Adobe Credential action.  
  
We have an internal KB1832121 - Adobe Integration Error – "401 - Invalid username/password combo".   
  
**ISSUE 3: 403 Forbidden**

**Cause**: Adobe account does not have required permissions—incorrect API scopes.

**Resolution**: Check Adobe Console → API permissions.

Ensure the Service Account (JWT) has the User Management API enabled.  
  
Please check the official DOC below for more details: 

https://www.servicenow.com/docs/bundle/zurich-it-asset-management/page/product/software-asset-management2/concept/adobe-cloud-integration.html

| Process | Required user role in the Adobe Cloud application | Authentication scopes |
| --- | --- | --- |
| Download subscriptions | Administrator | None |

**ISSUE 4: 404 [HTTP status code](https://www.google.com/search?sca_esv=b4e332f294b324c3&rlz=1C5GCEM_enIN1088IN1089&sxsrf=AE3TifP7aw79OVGc0uJJYcGSxQ4KJaQZ4w%3A1756297150200&q=HTTP+status+code&sa=X&sqi=2&ved=2ahUKEwiwzofe_KqPAxXP1TgGHQKmML4QxccNegUIigEQAQ&mstk=AUtExfBbeQHP3SL1HHHMBTsb7oZOhLcqQd0KJ_BCHQBMN8ra19RCmDeEGhcxRojyvhOnTeVqmO60XmZsu_V-tinVkdsMxIfVIIW_Bi7ZJDVNYAv_l_xw8TpLlHLppffaehdNBIxTIbhnQvyCKIdLVqQFLKnkaAd0E-_NAeSgdPIj5xuT2Hs&csui=3) meaning "Not Found"**  
  

### Observation

-   samp\_job\_log: Job shows "failed" but no error message.
-   sys\_outbound\_http\_log:

response\_status=404  
hostname=usermanagement.adobe.io  
path=/v2/usermanagement//products  
method=GET

There might be two reasons for this issue: 

**Reason 1:** 

-   The Adobe job entry point runs `SamImportUserSubscriptionsAdobe().process()`, which calls `SampAdobeAdmin.importSubscriptionForProfile(profile)`.
-   `SampAdobeAdmin` constructs a REST client using the profile's `sys_rest_message` ("Adobe" REST message) and then performs the API calls. If the endpoint path is malformed (e.g., trailing slash on base + leading slash on resource ⇒ `//products`), Adobe returns 404. The catch re-throws as "Unhandled exception for profile …" and the wrapper only logs it (no detailed message in `samp_job_log`)  
      
    

1\. Open the REST Message referenced by the Adobe integration profile (the profile `rest_message` is read to build the client)2\. Normalise the URL:

Ensure no trailing slash on the base URL and a single leading slash on the resource path, so the final path is like: `/v2/usermanagement/products` (not `//products`).

3\. Use the REST Message "Preview/Test" to confirm you get a 200 (with valid auth).

4\. Re-run the job.

  
**Reason 2:** Missing Org\_Id in the Attributes section of HTTP(s) Connection Adobe Credentials for the below connection URL  
  
Connection URL: https://ims-na1.adobelogin.com

The fact that the Direct Integration profile has the Org\_Id will not satisfy the GET request URL construction, as it will be dependent on HTTP(s) Connection Adobe Credentials.   
  
Please follow the KB2428864 to fix this issue.   
  
**ISSUE 5: 429 Too Many Requests**

Where: `sys_outbound_http_log` `response_status=429` (often with `Retry-After` header).

Why: Adobe rate limiting. The job itself doesn't implement exponential backoff; if you schedule it tightly or run multiple times concurrently, you will hit throttles.

Fix: 

1.  Stagger Adobe import schedules.
2.  Ensure only one instance runs: `SAMSaasIntegrationUtils.processScheduledJob()` explicitly prevents concurrency and logs "An instance of '{job}' is already running…" when it sees multiple triggers
3.  If you must retry, add a delay between attempts; avoid back-to-back manual runs.

Adobe DOC: https://experienceleague.adobe.com/en/docs/experience-cloud-kcs/kbarticles/ka-25100  
  

**ISSUE 6: 5xx (Adobe-side)**

Where: `sys_outbound_http_log` `response_status=5xx`; node/Splunk shows exception wrapped as Unhandled exception for profile …, job ends failed.

Why: Transient Adobe service issue.

**Fix**: Retry after a short delay. If persistent, validate Adobe service health. 

* * *

**OTHER POSSIBLE ISSUE DUE TO TLS / OCSP / Revocation checks**

Where: Node/Splunk shows messages like:

`GlideSSLProtocolSocketFactory.walkCertChainToCheckIfRevoked of: CN=adobe.io …`

`WARNING No URIs provided, removing all URI matcher rules`

Why: Standard certificate chain/revocation checking during HTTPS handshakes. Not an error by itself. If paired with handshake failures, review outbound trust/egress.

**Fix**: Ensure the instance (or MID, if used) can reach Adobe endpoints and any required revocation/OCSP endpoints.

If you actually see SSL handshake failures, capture request\_error in the outbound log and work with your network/security team to allow destinations.   
  
**Records in the samp\_sw\_subscription profile are not getting created even though the job `SAM - Import Adobe User Subscriptions`runs successfully. SEVERE \*\*\* ERROR \*\*\* sn\_sam\_saas\_int (SampAdobeAdmin): Failed to retrieve members (directOnly = false) for group**

When you verify the APP NODE logs using the job transaction ID in the NODE LOGS, you can see an error like below:

SEVERE \*\*\* ERROR \*\*\* sn\_sam\_saas\_int (SampAdobeAdmin): Failed to retrieve members (directOnly = false) for group "683622997": Method "toString" called on incompatible object (org.mozilla.javascript.NativeObject is not an instance of org.mozilla.javascript.BaseFunction).

More details on the SampAdobeAdmin script include: JavaScript code in SampAdobeAdmin is trying to call .toString() (or something like it) on a JSON object returned by Adobe. In Rhino (the JS engine in ServiceNow), if a JSON object contains its own toString property that isn't a function, or if you try to treat a plain object like a function, you get exactly this error.

Once that exception is thrown, the loop that creates subscription records never completes, so samp\_sw\_subscription stays empty.

REASON: If the current 'software asset management(sn\_itam\_samp)' version 3.0.0 installed on the customer instance is not compatible with Yokohoma Patch4b.

Ideally, this version, sn\_itam\_samp 3.0.0, should not be visible to the customer as it's not compatible. Please refer to the store link shared earlier tu. For this, we need to log a task with the platform team on how incompatible version \[sn\_itam\_samp 3.0.0\]was shown when the instance is on Yokohoma Patch4\*.  
  
FIX: To resolve the issue, the customer needs to upgrade the instance to Zurich based on compatibility versions for the sn\_itam\_samp Store app 3.0.0.  
  
We have a task **CSTASK1183227** and **KB2397104**: Applications on Incompatible family versions causing Incorrect Installations

https://support.servicenow.com/kb?id=kb\_article\_view&sysparm\_article=KB2397104

### Related Links

# **Adobe Integration Profile Configuration Step-By-Step | Software Asset Management: KB1001915**
