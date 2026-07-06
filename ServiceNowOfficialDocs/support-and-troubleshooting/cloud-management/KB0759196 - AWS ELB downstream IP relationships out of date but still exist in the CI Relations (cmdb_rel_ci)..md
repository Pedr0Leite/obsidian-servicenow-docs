---
title: "AWS ELB downstream IP relationships out of date but still exist in the CI Relations (cmdb_rel_ci). "
aliases:
  - KB0759196
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0759196
kb_number: KB0759196
last_modified: 2025-08-25
---

## AWS ELB downstream IP relationships out of date but still exist in the CI Relations (cmdb\_rel\_ci).

  

### Issue

AWS ELB downstream IP relationships out of date but still exist in the CI Relations (cmdb\_rel\_ci).  
Note:  
\- AWS hosted load balancers occasionally have IP address changes.

\- Run daily discovery across AWS accounts, however, the ELB relationships are stale from weeks ago. 

### Release

London

### Cause

By design, ServiceNow does not delete any relationship from the "cmdb\_rel\_ci" even when they are terminated.  
For other CIs when they are no longer in use we update these fields - state/operational status/install status to terminated/retired.  
  
For load balancer IP address table also, ServiceNow can use the operational status field to know if this is an existing IP on the LB or not.  
This is not available in any release at the moment.

### Resolution

Related PRB1345658 has been raised and currently in progress.

Workaround:

-   Manually delete the old IP Address relationship records from the 'cmdb\_rel\_ci' the records.

            OR

-   Create an Auto Flush \[sys\_auto\_flush) entry with the following details:  
    Table: cmdb\_ci\_cloud\_lb\_ipaddress  
    Matchfield: sys\_updated\_on  
    Age in seconds: 259,200 (72 hours)
