---
title: "Catalog tasks are not being created. Why?"
aliases:
  - KB0778521
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778521
kb_number: KB0778521
last_modified: 2026-02-20
---

## Catalog tasks are not being created. Why?

  

### Issue

After the user installed the Explicit Roles Plugin, whenever something is requested via Service Portal or Service Catalog, the associated task that should be created does not get created.  
  
The RITM shows a state of Waiting on Approval even if there is no approval necessary. Also, from the RITM, as an administrator, the user should be able to see/click on the "Show Workflow" Related link but it isn't there. The user tried setting the property glide.security.use\_explicit\_role to "false", but they are still facing the issue.

### Cause

The reported behavior does not have anything to do with the Explicit Roles plugin. Rather, it is because the user does not have a workflow to process Requests (and their approvals).

### Resolution

As mentioned above, in order for the workflow on a RITM to fire, the user needs to have approval passed down from the parent Request record's workflow. This triggers an Out of Box (OOB) Business Rule called "Cascade Request Approval to Request Item" which passes the Request's approval down to the RITM and starts the workflow there.  
  
In an OOB instance, the "Service Catalog Request" workflow handles the automatic approval process needed to properly kick off a RITM's workflow (and thus create the child task which is generated within the RITM's associated workflow).  
  
The issue, in this case, is that the user, through a series of Changes, had the demo data removed from their instance (search in HI for Changes titled "Remove demo data from \[instance\_name\]"). The "Service Catalog Request" workflow is considered demo data and is meant to be a template or a starting point so that the user can create one that matches their specific business needs and process. It is only an example.

Therefore, to remedy the behavior, if the user still has the demo data in a sub-Production environment, simply have them move the "Service Catalog Request" workflow to the affected environment. Or, if needed, they can utilize the attached XML record which contains the workflow from an OOB New York EA instance.
