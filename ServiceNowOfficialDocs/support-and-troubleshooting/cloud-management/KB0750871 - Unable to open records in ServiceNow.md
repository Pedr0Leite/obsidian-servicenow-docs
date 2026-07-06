---
title: "Unable to open records in ServiceNow"
aliases:
  - KB0750871
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0750871
kb_number: KB0750871
last_modified: 2025-12-31
---

## Unable to open records in ServiceNow

  

### Issue

Users are unable to open records in ServiceNow. Records appear in list views but fail to open when selected.

### Symptoms

-   Global search returns no results and continues loading indefinitely.
-   Records (for example, incidents or changes) appear correctly in list views.
-   Clicking the record number results in a blank page.
-   Issue may occur across multiple tables (Incident, Change, Problem, and others).

### Facts

-   Audit history growth can impact form performance and stability.
-   This issue can affect any table that generates frequent field updates.
-   Regular audit data maintenance helps prevent record access issues.

### Release

All ServiceNow releases

### Cause

The affected record contains an excessive number of audit history entries (`sys_audit`).  
A large volume of audit records can cause the form rendering process to fail, resulting in a blank page when opening the record.

### Resolution

Remove excessive audit history for the affected record(s).

Steps:

1.  Identify the affected record(s) that cannot be opened.
2.  Navigate to the Audit (sys\_audit) table.
3.  Filter audit records associated with the impacted record (by document key or record sys\_id).
4.  Delete the excessive audit entries.
5.  Refresh the browser and attempt to open the record again.

> Important:  
> Audit records may be required for compliance or auditing purposes. Always review retention policies and confirm approval before deleting audit data—especially in production environments.

### Related Links

[Differences Between Audit and History Sets](https://www.servicenow.com/docs/csh?topicname=c_DiffBtwnAuditHistSets.html&version=latest "Differences Between Audit and History Sets")
