---
title: "Some task SLAs are not attaching although their Start conditions are met"
aliases:
  - KB0829202
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0829202
kb_number: KB0829202
last_modified: 2024-04-08
---

## Some task SLAs are not attaching although their Start conditions are met

  

### Issue

The user has both a Response and Resolution SLA Definition, both of which have their Start conditions meeting upon insert of their parent SCTASK record. However, on the insert of the SCTASK record, only one or the other will attach, and rarely ever both. The user wanted to know why.

### Resolution

The issue, in this case, was caused by a defunct version of the "Default SLA Workflow" having been associated to each of the SLA Definitions (and the issue still presented itself if, say, SLA Definition for "Response"'s workflow was changed to some other workflow, but the other SLA Definition for "Resolution" still referenced the defunct workflow --- the broken workflow has to be removed entirely from all SLA Definitions attaching to a parent record).  
  
What happened is that SLA processing broke silently at the point the workflow was started. The only clue to this was in a log message (not having checked to see the workflow canvas, upon preview, was actually blank - although the canvas says the workflow is _Published_):

log10:57:45.158 Activity ID: not found in workflow version: 8655420040564500ec0c9e9cad47fec7  
  
The above log message is the last message noted before the "Run SLAs" Business Rule is reported as complete. It is was also found that the second running SLA Definition (whether Response is evaluated first or Resolution - or vice versa, it does not matter) does not even get evaluated if debugging ("Enable logging" on the SLA Definition = checked) is turned on.  
  
With SLA processing, if two SLA Definitions have the same start condition, there is no ordering method by which SLA Definition 'A' should run before 'B' (or in this case, Response vs. Resolution), so this accounts for why intermittently the Response task SLA would attach, and then in another case only the Resolution task SLA would attach.  
  
To fix this issue, the defunct "Default SLA workflow" had to be completely removed from the system, and thus completely disassociated from all SLA Definitions which formerly used it. Then, the Out of Box (OOB) "Default SLA workflow" was given to the customer to utilize. Simply setting the defunct workflow version to inactive did not solve the issue.  
  
Once the defunct workflow was removed, the OOB workflow was brought in, and _all_ formerly associated SLA Definitions were reassociated, both task SLAs attached as per the user's expectation, every time.
