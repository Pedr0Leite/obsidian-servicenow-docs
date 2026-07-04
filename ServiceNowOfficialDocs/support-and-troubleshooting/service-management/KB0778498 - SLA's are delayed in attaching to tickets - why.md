---
title: "SLA's are delayed in attaching to tickets - why?"
aliases:
  - KB0778498
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778498
kb_number: KB0778498
last_modified: 2024-04-08
---

## SLA's are delayed in attaching to tickets - why?

  

### Issue

The user's task\_slas were not attaching to tickets until nearly 4-8 hours after the tickets, which matched the appropriate SLA's Start conditions, were created.

### Resolution

Our customer did not have the "SLA Async Delegator" Scheduled Job within their instance, hence, their sla\_async\_queue was over 300,000 records. This is why they were seeing such high delays in the attachment of task\_sla records to task records. The reason the "SLA Async Delegator" could not be in an instance is one of two things:   
  
\- First, the user activated the "com.snc.sla.async" system property in a lower environment (set it from "false" to "true") and directly imported the preset "true" value record into the affected instance, or   
\- Second, the user moved the already "true" record via an update set into the affected instance (covered in PRB1358945)  
  
Both methods bypass critical logic in the system which would have otherwise generated the necessary Scheduled Job.  
  
After providing the user with the "SLA Async Delegator" Scheduled Job, the sla\_async\_queue started to decrease, but very slowly.

To remedy this, it was recommended that the user change the system property "com.snc.sla.async.job.limit"'s value from the Out of Box (OOB) value of '4' to '8' to help with the load.  
  
It is worth mentioning that increasing the value to '8' from '4' does not mean that there will always be 8 dedicated "workers" for the "SLA Async Delegator" Scheduled Job. Rather, it simply permits, if necessary, the Scheduled Job the leeway and power needed to process down a large, continuous sla\_async\_queue.
