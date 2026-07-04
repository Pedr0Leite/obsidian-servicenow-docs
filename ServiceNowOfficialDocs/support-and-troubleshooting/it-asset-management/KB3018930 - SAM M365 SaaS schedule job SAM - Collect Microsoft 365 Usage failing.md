---
title: "SAM M365 SaaS schedule job \"SAM - Collect Microsoft 365 Usage\" failing"
aliases:
  - KB3018930
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3018930
kb_number: KB3018930
last_modified: 2026-05-14
---

## Issue

Upon checking log, this is what I see below:  
\-----------------------------------------------------------------------------------------------  
SamCollectUsageO365: Error: CaptureM365AppsUsageReport: Error: com.glide.rest.util.RESTRuntimeException: Response body was requested to be saved as attachment. It's not available through getBody() anymore.  
  
\*\*\* Script: SamCollectUsageO365: Error: CaptureM365AppsUsageReport: Error: com.glide.rest.util.RESTRuntimeException: Response body was requested to be saved as attachment. It's not available through getBody() anymore.: no thrown error  
  
Error: SamCollectUsageO365: Failed to run job. Please look into logs for more details.  
  
SAM:SAM - Collect Microsoft 365 Usage: Error: SamCollectUsageO365: Failed to run job. Please look into logs for more details.: no thrown error  
  
SAM:SampO365RestClient: Following error occurred: com.glide.rest.util.RESTRuntimeException: Response body was requested to be saved as attachment. It's not available through getBody() anymore.: no thrown error  
  
\------------------------------------------------------------------------------------------------

## Resolution

**Resolution:**  
  
Please check the reclamation rule: if it was set to any other number of days than 30,90,180 and change it to the applicable number of days  
  
[https://instance\_name.service-now.com/nav\_to.do?uri=samp\_sw\_reclamation\_rule.do](https://uniteddev.service-now.com/nav_to.do?uri=samp_sw_reclamation_rule.do?sys_id=f5470b471b6e025434b1326ecc4bcb16)

Solution:  
  
After changing the values and saving the last\_activity\_threshold, we can now find the JOB getting completed successfully.
