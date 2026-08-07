---
title: "All SLA Definition conditions are missing"
aliases:
  - KB0726450
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0726450
kb_number: KB0726450
last_modified: 2024-04-07
---

## All SLA Definition conditions are missing

  

### Issue

When opening a SLA Definition, all conditions are absent - it appears as if the form is broken somehow.

### Release

ALL

### Cause

A user, when on the contract\_sla table, right-clicked the header and did a Configure > Form Layout and cleared the values for sections "Start condition", "Pause condition", "Stop condition", and "Reset condition".

### Resolution

An attempt was made to track the changes made to these form sections by navigating to the sys\_ui\_section table and locating the appropriate form section (e.g. "Start condition"). Within each form section should be "Section Elements". Unfortunately, as these were deleted and not simply updated, the user who deleted them remains unknown. The table is not audited to reveal such details.  
  
Thankfully, there is a way to resolve this issue of displaying the Start, Pause, Stop, and Reset conditions correctly again. Attached to this article are four screenshots showing how to set up the specific form sections identical to how they appear in an Out of Box (OOB) instance. They are aptly labeled for convenience.  
  
To reach these sections simply navigate to any record on the contract\_sla (SLA Definitions) table, right-click the header of the record, and do Configure > Form Layout.  
  
Under "Form view and section", click each respective section ("Start condition", "Pause condition", "Stop condition", and "Reset condition") and move the correct selections per the screenshots from the "Available" side of the slush bucket to the "Selected" side of the slush bucket. Then, click the blue "Save" UI Action and move on to the next section until all are corrected.
