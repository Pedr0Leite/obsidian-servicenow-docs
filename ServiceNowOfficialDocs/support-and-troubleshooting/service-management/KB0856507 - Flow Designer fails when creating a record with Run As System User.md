---
title: "Flow Designer fails when creating a record with Run As: System User"
aliases:
  - KB0856507
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0856507
kb_number: KB0856507
last_modified: 2025-08-01
---

## Flow Designer fails when creating a record with Run As: System User

  

### Issue

When a flow with **Run As: System User** creates a record in the sys\_group\_has\_role table, it results in the error: "Error occurred while inserting record: null". However, when executed with **Run As: User who Initiates session**, the flow runs without errors.

The flow is configured to trigger when a record is created on the sys\_user\_group table. Also, **Create Action** is used to insert a record in the sys\_group\_has\_role table with values as follows:

-   **Action:** Create Record
-   **Table:** Group Role \[ sys\_group\_has\_role\]
-   **Role**: itil
-   **Group**: Trigger > Group Record > Sys ID
-   **Inherits**: Checked

The following image illustrates these settings.

![](sys_attachment.do?sys_id=6d58e4aa93cbaa148960fb2d6cba1007)

### Release

Any supported release

### Cause

The problem is with the itil role (Information Technology Infrastructure Library) being inserted into the sys\_group\_has\_role table. In this instance, the itil role indirectly includes a scope-protected role (itil sn\_templated\_snip.template\_snippet\_reader and sn\_templated\_snip.template\_snippet\_writer), which is part of the "Templated Snippets" scope with application administration enabled.

These roles are not part of the default itil role.

An access handler blocks the addition of these roles when the user performing the insert lacks the same roles. The flow runs as System, which does not have the scope-protected roles, causing the error only for System User and not when executed with User who Initiates session.

### Resolution

This behavior is expected for the System User, as it checks application scope roles. To resolve this, either remove the application-scoped roles from the itil role or avoid executing the flow as System User.
