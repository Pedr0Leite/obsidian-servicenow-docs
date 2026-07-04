---
title: "Job SAM - Import Adobe User Subscriptions Failed with 404 Not Found"
aliases:
  - KB2939166
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2939166
kb_number: KB2939166
last_modified: 2026-05-21
---

## Job SAM - Import Adobe User Subscriptions Failed with 404 Not Found

  

### Issue

The scheduled job "SAM - Import Adobe User Subscriptions" fails during execution with a 404 Not Found error when attempting to retrieve product subscription data from Adobe.

### Symptoms

-   The job log (samp\_job\_log) shows failure for the Adobe subscription import job.
-   System logs (syslog) display errors similar to:
    -   _"SampAdobeAdminUnhandled exception…"_
    -   _"404 Not Found" response from Adobe endpoint_
-   Outbound HTTP logs (sys\_outbound\_http\_log) confirm failed API calls to:
    
    \[code\]<pre><code>[https://usermanagement.adobe.io/v2/usermanagement//products](https://usermanagement.adobe.io/v2/usermanagement//products)<br/></code></pre>\[/code\]
    
-   Response received:
    -   HTTP Status: 404 Not Found
    -   Server: abc
-   OAuth token generation succeeds, indicating authentication is working correctly.
-   No recent credential changes reported by the Adobe Admin team.

### Release

No specific release 

### Cause

The issue occurs due to a missing Org ID in the Adobe Integration (Subscription Profile) configuration.

Because the Org ID is required to construct the correct Adobe User Management API (UMAPI) endpoint, its absence results in an invalid API URL (note the double slash `//`), leading to a 404 Not Found response from Adobe.

### Resolution

-   Navigate to the Adobe Subscription Profile in ServiceNow:
    -   Table: `samp_sw_subscription_profile`
-   Verify the following configuration:
    -   Ensure the Org ID is populated correctly.
-   If missing:
    -   Obtain the correct Org ID from the Adobe Developer Console.
    -   Update the Integration Profile with the valid Org ID.
-   Save the record and re-run the job:
    -   SAM - Import Adobe User Subscriptions
-   Validate:
    -   Confirm the job completes successfully.
    -   Verify API calls no longer return 404 errors.

### Related Links

-   ServiceNow Documentation:  
    [https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/create-adobe-cloud-oauth.html](https://www.servicenow.com/docs/r/zurich/it-asset-management/software-asset-management/create-adobe-cloud-oauth.html)

-   Adobe Developer Console:  
    [https://developer.adobe.com/console](https://developer.adobe.com/console)

-   Adobe User Management API (UMAPI):  
    https://developer.adobe.com/user-management-api/
