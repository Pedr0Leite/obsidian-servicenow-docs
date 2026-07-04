---
title: "HR Criteria Not Fully Visible in Agent Workspace When Creating Segment Groups"
aliases:
  - KB2648385
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2648385
kb_number: KB2648385
last_modified: 2026-01-03
---

## HR Criteria Not Fully Visible in Agent Workspace When Creating Segment Groups

  

### Issue

Agents are unable to view all HR criteria in the Agent Workspace when creating a segment group for bulk HR cases. The issue occurs specifically in the Agent Workspace UI, while the Native UI behaves differently depending on user roles. This problem is reproducible in environments where multiple HR criteria exist and affects users with appropriate HR roles.

### Release

Any

### Cause

The HR criteria dropdown in HR Agent Workspace is limited to displaying only 20 criteria due to a system-imposed restriction. When more than 20 criteria exist, some options are not shown. This behavior is part of the default configuration.

### Resolution

-   The limitation is caused by the default configuration of the HR bulk case segment UX macroponent.
-   To display all criteria, update the Data field in the macroponent to increase the limit (e.g., set to 1000).
-   This component is protected and read-only; the change requires appropriate elevated access.
-   If direct editing is not possible, duplicating the macroponent was considered but found complex and not recommended.
-   Preferred workaround: apply the change with elevated access until a permanent fix is available.
-   Problem Record: PRB1847233 has been logged for this issue and can be tracked for future updates.
