---
title: "Task SLA Section Not Visible in HR Agent Workspace – Security Constraints Message"
aliases:
  - KB2657270
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657270
kb_number: KB2657270
last_modified: 2026-01-01
---

## Task SLA Section Not Visible in HR Agent Workspace – Security Constraints Message

  

### Issue

HR Agents are unable to view the Task SLA section for HR Employee Relations (ER) cases in Agent Workspace. The message displayed is:  
"1 row removed from this list by security constraints."  
The issue occurs in environments running the Yokohama release and affects multiple instances.

### Release

Any

### Cause

Recent changes to ACL scripts in the Yokohama release restricted access to Task SLA records for HR cases in certain scopes. The task\_sla ACL included an additional script condition, causing visibility issues.

### Resolution

-   Create new ACLs for task\_sla and contract\_sla tables to restore visibility of SLA details for impacted users.
-   Ensure ACLs provide appropriate read access for HR Agent roles.
-   Verify SLA section is visible in Agent Workspace after applying ACL changes.
-   Subscribe to PRB1946815 for updates on the underlying product issue.
