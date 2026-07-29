---
title: "Flow Stages are not showing in Request Item List View"
aliases:
  - KB0953546
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0953546
kb_number: KB0953546
last_modified: 2026-06-24
---

## Flow Stages are not showing in Request Item List View

  

### Issue

On the **Requested Item List View** I am not seeing any **'Stages'** being rendered.

Instead all of the **Stage Icons** are **empty** and it looks like the **Flow** did not **start**.

### Release

N/A

### Cause

This is happening because the **Flow** is missing the **Stage Records**.

-   Often this can happen if the **Flow** is **transferred** between instances since the **Stages** are not tracked in the update which gets moved.

### Resolution

Ensure that the **Stages** from **\[sys\_hub\_flow\_stage\]** are existing in the affected **instance**. (These can be **transferred** from another **instance** if the issue happened after **Flow Transfers**).

If the issue did **not happen after transfer** then it is likely because the **Stages** were not **created** in the first place.

To resolve this, the following needs to be performed:

1.  Open the **Flow** in the **Flow Designer**
2.  Click the **Three Dots (More Actions Menu) > Stages**
3.  Add **New** Stages

Lastly, the ["](https://docs.servicenow.com/bundle/paris-servicenow-platform/page/administer/flow-designer/task/add-stages.html "\"Configure stages and add them to a flow\" Documentation")**[Configure stages and add them to a flow" Documentation](#mce_temp_url#4531)** can be followed as a reference for creating and using the **Stages** properly.
