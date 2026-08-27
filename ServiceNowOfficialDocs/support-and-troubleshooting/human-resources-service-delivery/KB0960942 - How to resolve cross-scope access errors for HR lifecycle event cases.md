---
title: "How to resolve cross-scope access errors for HR lifecycle event cases"
aliases:
  - KB0960942
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0960942
kb_number: KB0960942
last_modified: 2026-02-18
---

## How to resolve cross-scope access errors for HR lifecycle event cases

  

### Issue

Resolve the error "Read operation on table was denied" that occurs while completing activities in lifecycle event cases. The full error message is: 

"Read operation on table 'sn\_hr\_le\_case' from scope 'Human Resources: Service Portal' was denied. The application 'Global' must declare a cross scope access privilege. Please contact the application admin to update their access requests."

### Release

All supported releases

### Cause

This error can occur if certain scoped resources (tables, script includes, and others) are set to deny access to other scopes. To resolve this, a scoped administrator must update the Restricted Caller Access record \[sys\_restricted\_caller\_access\] to allow other scopes to access the resource.

### Resolution

1.  Go to the Restricted Caller Access \[sys\_restricted\_caller\_access\] table.
2.  Add the **Updated** column to the list view.
3.  Check the most recently updated Restricted Caller Access records where the Target Scope is **Human Resources: Lifecycle Events.**
4.  Select the link in the **Operation** column or select the information icon to open the record.
5.  In the **Status** field, change the value from **Requested** to **Approved**.
6.  Select **Save**.
7.  Test the activity again.

If the test fails again, repeat the previous steps. In some cases, one script may call another script, which generates an additional Restricted Caller Access record that also requires approval.

### Related Links

[Scoping and HR Roles FAQ](https://support.servicenow.com/kb?id=kb_article_view_popup&sysparm_article=KB0691402 "Scoping and HR Roles FAQ")

[Restricted caller access privilege settings](https://docs.servicenow.com/bundle/paris-application-development/page/build/applications/concept/restricted-caller-access-privilege.html "Restricted caller access privilege settings")

[Define cross-scope access to an application resource](https://docs.servicenow.com/bundle/kingston-application-development/page/build/applications/task/set-RCA-level.html "Define cross-scope access to an application resource")

[Define access to or from an application scope](https://www.servicenow.com/docs/r/application-development/set-RCA-level.html "Define access to or from an application scope")

[How to fix the red popup "... must declare a cross scope access privilege" errors](https://community.servicenow.com/community?id=community_blog&sys_id=ce28d5b8db690c5c5129a851ca961999&view_source=searchResult "How to fix the red popup \"... must declare a cross scope access privilege\" errors")
