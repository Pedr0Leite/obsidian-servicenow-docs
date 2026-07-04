---
title: "Adhoc Approval Requests Not Triggering in HR Service Delivery After Upgrade"
aliases:
  - KB2657077
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2657077
kb_number: KB2657077
last_modified: 2025-12-17
---

## Adhoc Approval Requests Not Triggering in HR Service Delivery After Upgrade

  

### Issue

Adhoc Approval Requests were not created when using the Add Adhoc Approval option in HR Service Delivery. No approval records appeared in the sysapproval\_approver table. The issue occurred after enabling the Agent Can Add An Approval case option and attempting to add approvals via Native UI or Agent Workspace.

### Release

Xanadu

### Cause

-   The property sn\_hr\_core.deprecated\_workflows determines whether legacy workflows or new flows are used for approvals.
-   In upgraded instances, this property may exist and affect approval behavior.
-   Missing Agent Workspace - Declarative Actions plugin can lead to missing form action mappings.

### Resolution

To resolve the issue:

-   Check if the property sn\_hr\_core.deprecated\_workflows exists in the instance.
    -   Navigate to System Properties > All Properties and search for `sn_hr_core.deprecated_workflows`.
    -   Adjust its value based on whether workflows or flows should be used for approvals.
-   Ensure the Agent Workspace - Declarative Actions plugin (`com.snc.agent_workspace.declarative_action`) is installed for full workspace functionality.
-   Validate Adhoc Approval creation in both Native UI and Agent Workspace after changes.
