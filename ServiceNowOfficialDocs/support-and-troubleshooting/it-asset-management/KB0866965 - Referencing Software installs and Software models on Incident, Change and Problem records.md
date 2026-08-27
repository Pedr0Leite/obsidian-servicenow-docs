---
title: "Referencing Software installs and Software models on Incident, Change and Problem records"
aliases:
  - KB0866965
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0866965
kb_number: KB0866965
last_modified: 2025-01-02
---

## Referencing Software installs and Software models on Incident, Change and Problem records

  

### Summary

-   Software installation record "cmdb\_sam\_sw\_install" cannot be referenced directly on Incident, Change, and Problem records using the out of the box "Configuration Item" field
-   The field "configuration item" that is currently present on the task table, references the "cmdb\_ci" table and since "cmdb\_sam\_sw\_install" is a standalone table, and does not extend cmdb\_ci, these records cannot be referenced on Incident, Problem, and Change tables.

### Instructions

-   According to our current data model, we recommend that the best practice is the Incident/Problem/Change references the hardware/device on which the affected software is installed rather than the software installation record itself
-   For referencing a software install record or a model record from cmdb\_model table, a custom reference field can be created on the task table, that will reference from cmdb\_sam\_sw\_install and cmdb\_model table
