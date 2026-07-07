---
title: "Show the Ribbon' Preference Not Working in HR Agent Workspace After Xanadu Upgrade"
aliases:
  - KB2656763
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2656763
kb_number: KB2656763
last_modified: 2025-12-17
---

## 'Show the Ribbon' Preference Not Working in HR Agent Workspace After Xanadu Upgrade

  

### Issue

After the Xanadu upgrade, enabling or disabling the Show the ribbon preference in HR Agent Workspace does not affect the display of the case timeline as expected. The issue is reproducible in upgraded instances but not in pre-upgrade environments.

### Release

Any

### Cause

The system does not honor user preferences to hide the ER Timeline when the ribbon is hidden due to a missing condition in the product logic.

### Resolution

-   A Problem Record (PRB1855716) has been raised to address this defect in future releases.
-   Workaround:
    -   Hide the timeline for ER Cases at the workspace level, which applies to all HR Agents.
    -   User-specific preferences for ribbon visibility are not currently supported.
