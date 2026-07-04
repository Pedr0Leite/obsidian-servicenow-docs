---
title: "Process Flow Formatter does not show after upgrade"
aliases:
  - KB0778518
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0778518
kb_number: KB0778518
last_modified: 2024-04-08
---

## Process Flow Formatter does not show after upgrade

  

### Issue

The user upgraded their instance from Kingston to Madrid, enabled all of the Problem plugins and Process Flow plugin but when they go into form design they still cannot add the Process Flow formatter to the form. The user also tried importing the Process Flow formatters manually, but the Process Flow formatter itself can still not be added to the form.

### Resolution

The user had already created all the process flow Flow Formatters needed on the problem table (ref: /sys\_process\_flow\_list.do?sysparm\_query=table%3Dproblem&sysparm\_view=).

Now, they simply needed to go to a new Problem record, right-click the header and navigate to Configure > Form Layout.  
  
Once this window opened, the user needed to add "Process Flow" from the left side of the slush-bucket ("Available") to the right side, top of the slush-bucket ("Selected").  
  
Once the user did this, the Flow Formatter displayed as expected, and per their design.
