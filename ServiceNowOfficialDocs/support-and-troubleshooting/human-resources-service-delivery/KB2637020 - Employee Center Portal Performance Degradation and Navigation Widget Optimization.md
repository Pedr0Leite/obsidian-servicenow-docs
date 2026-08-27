---
title: "Employee Center Portal Performance Degradation and Navigation Widget Optimization"
aliases:
  - KB2637020
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2637020
kb_number: KB2637020
last_modified: 2026-01-01
---

## Employee Center Portal Performance Degradation and Navigation Widget Optimization

  

### Issue

The Employee Center portal experienced significantly increased load times compared to previous performance:

-   Previously: < 5 seconds
-   Currently: 10–20 seconds, especially on first login.

This slowness impacted user experience and business operations.  
Suspected causes included:

-   Custom widgets
-   ACL evaluations
-   Employee Center Navigation widget

### Release

Any Release

### Cause

Performance degradation was linked to navigation rendering logic and lack of asynchronous loading in the custom navigation widget.  
Additional factors included ACL checks and customizations that deviated from out-of-box (OOB) behavior.

### Resolution

-   Updated Employee Center plugin to version 38.0.5.
-   Enabled async mega menu feature, which significantly reduced portal load times when using the OOB Employee Center Navigation widget.
-   Recommended:
    -   Compare custom navigation widget with OOB version.
    -   Implement async load logic to retain customizations while improving performance.
-   Identified a minor cosmetic glitch (flickering/shadow in navigation menu) as a defect:
    -   Logged as PRB1929983.
    -   Provided a CSS workaround, which resolved the issue on the OOB widget.
-   Any further slowness related to VA/AI Search was directed to a separate investigation.
