---
title: "Playbook Displays Only One Card in HR Agent Workspace on On-Premise Dev Instance"
aliases:
  - KB2656890
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656890
kb_number: KB2656890
last_modified: 2025-12-17
---

## Playbook Displays Only One Card in HR Agent Workspace on On-Premise Dev Instance

  

### Issue

In the on-premise development instance, the Playbook in HR Agent Workspace displays only one random card for all cases, even though multiple active cards are available. The issue is isolated to the development environment; QA and pre-production instances function as expected.

### Release

Any

### Cause

Known defect in Playbook Experience plugin v25.1.2 where the UI renders only one card despite the server returning all expected card objects.

### Resolution

-   Upgrade Playbook Experience plugin to v25.2 or higher.
-   If plugin installation is delayed in UAT or other environments, raise a case with the Plugin Team for assistance.
