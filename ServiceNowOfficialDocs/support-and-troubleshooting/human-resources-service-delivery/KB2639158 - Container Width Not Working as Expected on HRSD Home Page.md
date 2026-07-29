---
title: "Container Width Not Working as Expected on HRSD Home Page"
aliases:
  - KB2639158
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2639158
kb_number: KB2639158
last_modified: 2026-01-01
---

## Container Width Not Working as Expected on HRSD Home Page

  

### Issue

Out-of-the-box (OOTB) functionality for container width is not working as expected on the HRSD Home page. When set to Fluid, Container 1 expands to maximum width, but Container 2 does not. The same Fluid width setting works correctly for both containers in the Service Portal, but not in the HR Portal. This issue affects multiple ServiceNow instances and is critical for the HRSD team.

### Release

Any Release

### Cause

A product defect in Employee Center Pro caused inconsistent behavior for Fluid container width settings on the HR Portal.

### Resolution

To address this issue:

-   Apply a CSS-based workaround to adjust container width until the permanent fix is available.
-   Track the defect under PRB1822532, which is scheduled for resolution in employee-center-pro-content version 34.0.1 (January 2025 release).
-   Before upgrading, mark the sp\_page record as Replace on update to ensure the fix is applied during the update.
