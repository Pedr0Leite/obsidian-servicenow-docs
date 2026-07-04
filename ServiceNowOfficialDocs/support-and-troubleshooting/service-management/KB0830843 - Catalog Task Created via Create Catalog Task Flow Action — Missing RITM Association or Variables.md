---
title: "Catalog Task Created via \"Create Catalog Task\" Flow Action — Missing RITM Association or Variables"
aliases:
  - KB0830843
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0830843
kb_number: KB0830843
last_modified: 2026-06-09
---

## Catalog Task Created via "Create Catalog Task" Flow Action — Missing RITM Association or Variables

  

### Issue

Catalog Task Created via "Create Catalog Task" Flow Action — Missing RITM Association or Variables

### Symptoms

-   Catalog Task (SCTASK) created from the Create Catalog Task flow action is not associated with the RITM.
-   Catalog Task does not carry over the expected variables from the catalog item.

### Release

Madrid, New York (RITM association issue) | Washington DC (Variables issue)

### Cause

There are two distinct root causes:

1.  SLA Definition Interfering with Task Creation (Madrid, New York) – The Create Catalog Task action is a two-step process: the `sc_task` record is first inserted, then updated with the provided inputs. If the Catalog Task SLA Definition has a start condition of only _"Active is true"_, the SLA triggers immediately on insert — before the second step completes — preventing the RITM association and input updates from being applied.
2.  Mismatched Template Catalog Item (Washington DC) – The Create Catalog Task action generates the task based on the Template Catalog Item configured in the flow action. If this is set to a different catalog item than the one being requested, the variables from the submitted item will not be present on the created task. This is intended platform behavior.

### Resolution

Apply the fix relevant to the release and symptom observed:

1.  For Missing RITM Association – Update the Catalog Task SLA Definition to include an additional start condition alongside _"Active is true"_, such as _"Short description is not empty"_. This prevents the SLA from firing before the task record is fully populated.
2.  For Missing Variables – Ensure the Template Catalog Item field in the Create Catalog Task flow action is set to the same catalog item that the flow is associated with. Mismatching this field is the root cause and correcting it resolves the issue.
