---
title: "Flow Designer Fails to Create Journey Plans During Onboarding"
aliases:
  - KB2630998
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630998
kb_number: KB2630998
last_modified: 2026-01-03
---

## Flow Designer Fails to Create Journey Plans During Onboarding

  

### Issue

Flow Designer fails to create Journey plans when onboarding new users via HR service flows, while Workflow triggers work as expected. Attempts to add roles or embed scripts did not resolve the issue. Error messages indicate authorization failures for both system and integration users.

### Release

Any Release

### Cause

Journey plan creation via Flow Designer requires specific roles and correct application scope. Missing roles or incorrect scope causes security errors. By design, sn\_jny.writer does not include sn\_hr\_le.case\_writer, which can lead to incomplete permissions.

### Resolution

**Verify Application Scope**

-   Open the Flow Designer.
-   Check the application scope of the flow.
-   Ensure the flow runs in Human Resources: Lifecycle Events scope.
-   If not, switch the scope to Lifecycle Events using the scope selector.

**Assign Required Roles to the Flow**

-   Navigate to Flow Properties.
-   Add the following roles under Run As User / Flow Roles:
    -   sn\_hr\_le.case\_writer – Required for Lifecycle Events case operations.
    -   sn\_hr\_core.case\_writer – Required for HR Core case operations.
    -   sn\_jny.writer – Required for Journey plan creation.
-   Save the changes.

 **Validate Role Permissions**

-   Confirm that the integration/system user executing the flow has the above roles.
-   If using a Service Account, verify its role assignments in User Administration.

**Test Journey Plan Creation**

-   -   Trigger the onboarding flow.
    -   Confirm that the Journey plan is created successfully without authorization errors.
