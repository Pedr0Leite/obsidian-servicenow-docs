---
title: "A blank screen appears when trying to access certain tables and lists"
aliases:
  - KB0522483
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0522483
kb_number: KB0522483
last_modified: 2025-04-07
---

## A blank screen appears when trying to access certain tables and lists

  

### Issue

A blank screen appears when trying to access certain tables and lists

  
  
Symptom  

* * *

When trying to access certain tables and lists, a blank screen appears. This issue can be experienced when accessing the module from the navigation pane, or typing table or list name directly in the filter text.

The blank page is caused when the audit property is enabled on virtual tables. Virtual tables are those that start with ‘v\_’, for example \[v\_field\_editor\]. Enabling the audit property causes the code to make incremental selections and deletions rather than deleting all, so that it captures the state of the record before and after an update. 

Release

* * *

 Any release

Environment

* * *

 Any O/S or browser

Cause

* * *

When virtual tables are selected, the first action is to delete all records and rebuild them from memory. This causes an infinite loop, resulting in stack overflow and a failure to perform the action. 

Resolution

* * *

To resolve this issue, update the virtual tables to disable the audit property, then revert all other tables to the same auditing scenario as the base system before deciding which additional tables should have the auditing function enabled. Auditing should be enabled for a specific reason and not to audit all tables.

For more information, see [Enable auditing for a table](https://docs.servicenow.com/csh?topicname=t_EnableAuditingForATable.html&version=latest "Turning on Auditing (History) for a Table") in the ServiceNow product documentation.
