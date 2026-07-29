---
title: "How to remove the interceptor page for interaction records in HR Agent Workspace"
aliases:
  - KB0992743
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0992743
kb_number: KB0992743
last_modified: 2026-04-16
---

## How to remove the interceptor page for interaction records in HR Agent Workspace

  

### Issue

When selecting New in the Interactions list within HR Agent Workspace, an interceptor page appears before the interaction record opens.

 \*You must have the admin role to complete the following steps.

### Release

All versions

### Resolution

1.  1.  In the navigation filter, enter `sys_aw_renderer.list` to open the Workspace Renderer table.
    2.  In the Table Name column, locate the record where the table is set to interaction.
    3.  Open the HR Agent Workspace renderer record.
    4.  Set the renderer field to False.
    5.  Save the record.

![HR Workspace Renderer](/sys_attachment.do?sys_id=2d81a8a583540718cdbbc430feaad3ee "HR Workspace Renderer")

**Verification**

Go to HR Agent Workspace and select **New** in the Interactions list. The interaction record page should now open directly, without the interceptor page.

### Related Links

[Exploring Agent Workspace for HR Case Management](https://www.servicenow.com/docs/r/employee-service-management/agent-workspace-for-hr-case-management/agent-ws-hr-case-mgmt-exploring.html "Exploring Agent Workspace for HR Case Management")

[Setting up Agent Workspace for HR Case Management](https://www.servicenow.com/docs/r/employee-service-management/agent-workspace-for-hr-case-management/setup-configurable-hr-agent-workspace.html "Setting up Agent Workspace for HR Case Management")
