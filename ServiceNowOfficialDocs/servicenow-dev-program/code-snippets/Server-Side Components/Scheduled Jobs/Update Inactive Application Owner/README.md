---
title: "Update Inactive Application Owner"
aliases:
  - Update Inactive Application Owner
tags:
  - servicenow-dev-program
  - code-snippet
  - update-inactive-application-owner
  - scheduled-jobs
---

This code snippet will update the owner of application records in the cmdb_ci_appl table where the current owner is inactive. It specifically sets the owner to the manager of that inactive owner, ensuring that each application has an active owner assigned.

**GlideRecord Initialization:**
var grApp = new GlideRecord("cmdb_ci_appl");

**Query for Inactive Owners:**
grApp.addEncodedQuery("owned_by.active=false");

**Executing the Query:**
grApp.query();

**Iterating Through Records:**
while(grApp.next()){

**Getting the Manager’s Sys ID:**
var managerSysId = grApp.owned_by.manager.toString();

**Updating the Owner:**
if (managerSysId) {
    grApp.owned_by = managerSysId;
    grApp.update();
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
