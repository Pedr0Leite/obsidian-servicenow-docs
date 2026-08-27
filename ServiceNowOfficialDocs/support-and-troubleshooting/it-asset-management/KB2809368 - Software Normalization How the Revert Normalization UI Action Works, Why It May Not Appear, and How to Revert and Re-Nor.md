---
title: "Software Normalization: How the \"Revert Normalization\" UI Action Works, Why It May Not Appear, and How to Revert and Re-Normalize via Script"
aliases:
  - KB2809368
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2809368
kb_number: KB2809368
last_modified: 2026-03-01
---

## Issue

In ServiceNow Software Asset Management (SAM) Software Normalization, the Revert Normalization UI action is used to undo a previously applied normalization outcome on a Software Discovery Model record, so the record can be re-evaluated against the latest normalization rules and content.

This article explains:

-   What the Revert Normalization UI action does behind the scenes
-   Common, generic reasons the button does not appear
-   A safe, reusable script to revert and re-normalize a specific discovery model (useful when the UI action is not visible or conditions are not met)

## Resolution

**Option A: Use the UI action (when available):** 

1.  Open the Software Discovery Model record.
2.  Click Revert Normalization.
3.  Re-run normalization (either wait for the scheduled normalization process or run it immediately using the script in Option B).

**Option B: Use a script to revert and re-normalize a specific discovery model:** 

Use this when:

-   The UI action is not visible due to UI compatibility, conditions, or access checks
-   You need to quickly re-evaluate a specific record after a content update
-   You want a consistent revert outcome that matches the platform logic

Run this in Scripts - Background (with appropriate admin roles). Replace the sys\_id with the target discovery model sys\_id.

**// Generic: Revert normalization and normalize again for a single discovery model**  
**// Replace <DISCOVERY\_MODEL\_SYS\_ID> with the sys\_id of the target record**

**var dmSysId = "<DISCOVERY\_MODEL\_SYS\_ID>";**

**var eng = new global.NormalizationEngine();**

**// Step 1: Revert using the engine (preferred over manually clearing fields)**  
**eng.revertNormalization(dmSysId);**

**// Step 2: Normalize again immediately**  
**var dm = new GlideRecord("cmdb\_sam\_sw\_discovery\_model");**  
**if (dm.get(dmSysId)) {**  
    **var ok = eng.normalizeDiscoveryModelRecord(dm);**

**// Re-read to print the final state after normalization**  
    **dm.get(dmSysId);**  
    **gs.info("Normalization result=" + ok +**  
        **", status=" + dm.getValue("status") +**  
        **", norm\_publisher=" + dm.getValue("norm\_publisher") +**  
        **", norm\_product=" + dm.getValue("norm\_product") +**  
        **", norm\_version=" + dm.getValue("norm\_version"));**  
**} else {**  
    **gs.info("Discovery model not found for sys\_id=" + dmSysId);**  
**}**

What this script helps with

-   Performs a true revert using the normalization engine logic (more complete than clearing a few fields manually)
-   Forces an immediate re-normalization without waiting for scheduled jobs
-   Provides a quick status output so you can confirm whether normalization succeeded or still results in “match not found”

Safety notes

-   Run in **sub-production** first if possible.
-   Ensure the user running it has the required permissions and roles.
-   If normalization still results in “match not found”, the issue is typically content/rule coverage, discovered string differences, or missing content updates, not the revert action itself.
