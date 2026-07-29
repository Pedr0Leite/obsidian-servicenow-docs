---
title: "SLA Async Jobs are running in a scope where all related SLA Definitions are active = false"
aliases:
  - KB0996941
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0996941
kb_number: KB0996941
last_modified: 2024-08-28
---

## SLA Async Jobs are running in a scope where all related SLA Definitions are active = false

  

### Issue

The user had SLA Definitions in the Human Resources (HR) scope. Even after having set the SLA Definitions to active = false some time ago, and even though there were Stage = Completed task SLAs in the task\_sla table for those SLA Definitions (even deleting these did not resolve the issue), SLA Async Jobs were noted running in the HR scope in the user's system. They wanted to know why.

**Note**: Asynchronous SLA processing is _true_. This will not occur if Asynchronous SLA processing is _false_.

### Cause

The SLA Async Delegator will always run on all task tables even if there are no task\_sla records or active = true SLA Definitions in X or Y scope. The scope does not matter, so long as the table on which records are being created is task or extends task.

### Resolution

Just as shared above, irrespective of if there are or are not task\_slas for A or B table (in this case, HR-related tables) or SLA Definitions in X or Y scope which are active = true or active = false, the SLA Async Delegator will always create SLA Async Jobs every 5 seconds to wake up, check to see if anything needs to be done (even if nothing needs to be done -- no task\_sla records need to be updated, etc). 

There does not need to be a SLA Definition active in X or Y scope for the system to do this.

There does not need to be a task\_sla active for SLA Definitions in X or Y scope for the system to do this. 

The system simply always checks, every 5 seconds, if it has any work it needs to do _when asynchronous SLA processing is true_.
