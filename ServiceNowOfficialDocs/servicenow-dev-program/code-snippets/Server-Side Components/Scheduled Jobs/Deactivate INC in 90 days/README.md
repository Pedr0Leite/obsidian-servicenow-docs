---
title: "Deactivate INC in 90 days"
aliases:
  - Deactivate INC in 90 days
tags:
  - servicenow-dev-program
  - code-snippet
  - deactivate-inc-in-90-days
  - scheduled-jobs
---

This code snippet will help to inactivate the table records after 90 days of creation through schedule insert on sys trigger table  .
Can be used in BR/Script Inculde/Background script.
### Formatted for background script, please check the result in sys_ trigger Table or else click on document id it will redirect to  inserted JOb 


### Sample Output :
==============

Operation	Table	Row Count
insert	sys_trigger	1  

*** Script: Below runscript scheduled on sys trigger at 2023-01-23 13:29:48

var gr = new GlideAggregate('incident');
gr.addQuery('sys_id', '91cce5c52fb6111015d2e33df699b6f9');
gr.query();
if (gr.next()) {
gr.active = false;
gr.update();
}

## Related Notes

- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/API Token Expiry Warning/Readme|API Token Expiry Warning]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Approval Reminder/README|Approval Reminder]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto Disable account/Readme|Auto Disable account]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto close changes requests updated 30 days prior/README|Auto close changes requests updated 30 days prior]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto upgrade store applications/Readme|Auto upgrade store applications]]
- [[ServiceNowOfficialDocs/servicenow-dev-program/code-snippets/Server-Side Components/Scheduled Jobs/Auto-Assign Unassigned Incidents Older Than 30 Minutes/Readme|Auto-Assign Unassigned Incidents Older Than 30 Minutes]]
