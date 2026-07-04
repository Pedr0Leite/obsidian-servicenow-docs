---
title: "Journeys in DRAFT State Displayed as Completed in ECP Portal"
aliases:
  - KB2642168
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2642168
kb_number: KB2642168
last_modified: 2026-01-02
---

## Journeys in DRAFT State Displayed as Completed in ECP Portal

  

### Issue

Journeys in DRAFT state are incorrectly displayed as Completed with Not started yet progress in the ECP portal. This causes confusion for end users because these journeys are not ready and should not be visible. Customers have requested to exclude DRAFT journeys from appearing in the My Journeys tab and Journeys list.

### Release

Any

### Cause

The issue is related to PRB1864054, which affects the current Journey Designer plugin version. The logic in the portal incorrectly interprets DRAFT journeys as completed.

### Resolution

-   Implemented a workaround in the `jny_JourneyProgressUtilsSNC` script include to correctly display DRAFT journeys, based on internal development guidance.
-   A permanent fix will be available in the upcoming Journey Designer plugin release (expected May 2025). Upgrade to the latest version when available.
-   There is no out-of-the-box (OOB) option to filter out DRAFT journeys by default. Filtering would require customization of widgets or script includes.
-   Use the State dropdown in the portal to filter journey states as an interim solution.
