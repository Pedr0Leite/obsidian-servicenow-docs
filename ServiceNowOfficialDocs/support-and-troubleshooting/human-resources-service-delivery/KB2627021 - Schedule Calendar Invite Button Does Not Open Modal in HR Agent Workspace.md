---
title: "Schedule Calendar Invite Button Does Not Open Modal in HR Agent Workspace"
aliases:
  - KB2627021
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2627021
kb_number: KB2627021
last_modified: 2026-01-03
---

## Schedule Calendar Invite Button Does Not Open Modal in HR Agent Workspace

  

### Issue

Clicking the "Schedule calendar invite" button on the Interview \[sn\_hr\_er\_interview\] form in HR Agent Workspace does not open the expected modal.  
This impacts the declarative action Schedule calendar invite and blocks integration with calendar services (e.g., Outlook, Zoom)

### Release

Xanadu

### Cause

-   The record page variant was missing the Record page modals (HR) page collection for the Modal Container (Viewport) element.
-   This collection is required for the modal to render when the button is clicked.
-   Console errors indicated missing files and data brokers during initial investigation.

### Resolution

-   Confirm that the Schedule calendar invite action and related UX screens are Out-of-Box (OOB).
-   Check the record page variant in UI Builder for missing Record page modals (HR) page collection.
-   Add the required object to the Composition section of the macroponent to restore the modal container.
-   Clear browser cache and UI Builder cache after applying changes.
-   Ensure custom record page variants remain in sync with OOB versions to prevent future issues.
