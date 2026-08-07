---
title: "Guided Decision Tree Not Visible in HR Agent Workspace Playbook"
aliases:
  - KB2630933
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630933
kb_number: KB2630933
last_modified: 2026-01-03
---

## Guided Decision Tree Not Visible in HR Agent Workspace Playbook

  

### Issue

Agents and admin users cannot access the Guided Decision Tree within the playbook activity in HR Agent Workspace. Relevant roles are assigned, but the playbook tab and decision tree remain hidden, impacting HR case handling.

### Release

Any Release

### Cause

Guided Decision Trees are not supported in playbook activities within HR Agent Workspace. They are only available in Recommended Actions in the Contextual Sidebar. The functionality to add Guided Decision Trees to playbooks exists in Customer Service Management (CSM) workspace, not HR Agent Workspace.

### Resolution

-   Verify that Guided Decision Tree functionality is limited to Recommended Actions in HR Agent Workspace.
-   Use Guided Decision Trees in the Contextual Sidebar instead of playbooks.
-   For playbook integration, use CSM workspace, where this feature is supported.
