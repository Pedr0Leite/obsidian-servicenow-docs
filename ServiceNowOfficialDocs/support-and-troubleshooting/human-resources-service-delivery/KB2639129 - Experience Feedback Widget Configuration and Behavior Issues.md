---
title: "Experience Feedback Widget Configuration and Behavior Issues"
aliases:
  - KB2639129
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639129
kb_number: KB2639129
last_modified: 2026-01-01
---

## Experience Feedback Widget Configuration and Behavior Issues

  

### Issue

Several issues were reported with the Experience Feedback Widget:

-   No option to make the “Tell us more” field mandatory in the widget configuration.
-   The “Do not share my personal info” checkbox does not anonymize usernames in survey responses.
-   The “Remind Me Later” button only closes the widget and does not trigger a reminder or reopen the widget.
-   Selecting “All Pages” in Feedback definition does not display the widget on all pages as expected.

### Release

Any Release

### Cause

Current product limitations and configuration dependencies in the Experience Feedback Widget and portal header setup.

### Resolution

To address these issues:

-   Mandatory “Tell us more” field:
    -   This feature is not currently available. It is planned for the next release (May). No workaround exists at this time.
-   Anonymizing user identity:
    -   Enable the “Anonymize responses” option at the survey level to hide user identity instead of relying on the checkbox.
-   “Remind Me Later” button behavior:
    -   The button sets the overlay session limit to zero, preventing the widget from reopening in the same session. Users must start a new session to see the widget again. This behavior cannot be changed through configuration.
-   Widget display on all pages:
    -   Ensure the portal uses the Employee Center Header for proper widget initialization.
    -   Update any custom headers (e.g., in MyHr portal) to the Employee Center Header to enable widget display across all pages.
