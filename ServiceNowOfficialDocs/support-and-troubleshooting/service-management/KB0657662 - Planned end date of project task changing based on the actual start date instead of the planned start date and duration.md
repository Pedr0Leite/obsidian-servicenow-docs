---
title: "Planned end date  of project task changing based on the actual start date instead of the planned start date and duration"
aliases:
  - KB0657662
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0657662
kb_number: KB0657662
last_modified: 2025-03-13
---

## Planned end date of project task changing based on the actual start date instead of the planned start date and duration

  

### Issue

Planned end date of the project task changing based on the actual start date instead of the planned start date and duration.

### Cause

This is expected behavior.

### Resolution

The new Planned task Recalculation Exclusions (planned\_task\_recalculation\_exclusions) table enables you to configure the tables on which you would not like the recalculation to occur. 

For example, if you decide that you would not like the recalculation of project tasks to occur, you can add the (pm\_project\_task) table to the (planned\_task\_recalculation\_exclusions) table and the recalculation will not occur. 

The business rule that handles this recalculation is called (Recalulate) "sys\_id = 3a3412b09f230200598a5bb0657fcf69" running on the (planned\_task) table.
