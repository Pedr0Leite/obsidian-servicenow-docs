---
title: "JavaScript Error When Submitting Surveys in Mobile View of Employee Center Portal"
aliases:
  - KB2630682
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2630682
kb_number: KB2630682
last_modified: 2026-01-01
---

## JavaScript Error When Submitting Surveys in Mobile View of Employee Center Portal

  

### Issue

Submitting a survey in mobile view of the Employee Center portal triggered a JavaScript error: _“Cannot read property 'rating\_threshold' from undefined”_ in the Experience Feedback Header Wrapper widget. The issue occurred only in mobile or responsive views, while desktop view worked as expected. No customizations were made to the widget or script include, both of which were read-only.

### Release

Any Release

### Cause

The error occurred because the widget attempted to access a property that was not available in mobile view, which is a known product defect.

### Resolution

-   Confirm the issue occurs only in mobile or responsive views when submitting surveys.
-   Replicate the behavior and review related widgets and script includes to ensure they are out-of-box and not customized.
-   Check the associated problem record (PRB1903917) for details on the fix.
-   Upgrade Employee Center Pro to version 36.0.1 (July 2025 release) or later, where the fix for this issue is included.
-   After upgrading, clear cache and validate survey submission in mobile view to confirm the error no longer appears.
-   If immediate upgrade is not possible, plan the upgrade as part of the next scheduled maintenance cycle to prevent recurrence.
