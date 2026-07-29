---
title: "HR Tasks from Subflows Not Displayed in Playbook in HR Agent Workspace"
aliases:
  - KB2648392
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2648392
kb_number: KB2648392
last_modified: 2026-01-03
---

## HR Tasks from Subflows Not Displayed in Playbook in HR Agent Workspace

  

### Issue

HR Agent Workspace does not display all HR tasks associated with lifecycle events in the Playbook. Specifically, tasks created via subflows (Activity Type: Flow) using the Create task action do not appear in the Playbook, while tasks created directly from the Activity Set do. The issue persists even after updating related plugins to the latest versions.

### Release

Any

### Cause

HR Agent Workspace currently does not support displaying activities of type Flow in the Playbook. This is a product limitation in the default configuration.

### Resolution

Perform the following steps to verify and address the issue:

1.  Verify Plugin Versions

1.  -   Navigate to System Definition > Plugins.
    -   Confirm that all HR-related plugins are updated to the latest versions.

2.  Check Activity Types

2.  -   Open the lifecycle event configuration.
    -   Identify tasks created via subflows (Activity Type: Flow) and tasks created directly from Activity Sets.
    -   Confirm that only Activity Set tasks appear in the Playbook.

3.  Review Known Limitation

3.  -   Understand that HR Agent Workspace does not currently support displaying activities of type Flow in the Playbook.

4.  Track Problem Record

4.  -   Refer to PRB1831420 for updates on this limitation.
    -   The fix is planned for a future release of HR Agent Workspace.
