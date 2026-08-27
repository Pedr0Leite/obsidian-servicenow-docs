---
title: "Collaboration Button for MS Teams not being showed in HR Agent Workspace"
aliases:
  - KB2623492
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2623492
kb_number: KB2623492
last_modified: 2025-12-16
---

## Collaboration Button for MS Teams not being showed in HR Agent Workspace

  

### Issue

The Collaboration (MS Teams chat) button was not available in HR Agent Workspace, even though similar functionality exists in other workspaces. 

### Release

Any Release

### Cause

The Collaborate button is not supported by default in HR Agent Configurable Workspace; only the Discuss UI action is available.

The required UI action was not configured for Workspace format.

### Resolution

-   Enable the Start Microsoft Teams chat UI action for HR cases by setting the Format for Configurable Workspace option in the UI action settings.
-   Verify that the Collaboration button appears and works as expected.
