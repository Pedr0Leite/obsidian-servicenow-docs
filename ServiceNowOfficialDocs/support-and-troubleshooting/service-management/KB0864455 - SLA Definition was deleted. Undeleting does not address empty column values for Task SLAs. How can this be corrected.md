---
title: "SLA Definition was deleted. Undeleting does not address empty column values for Task SLAs. How can this be corrected?"
aliases:
  - KB0864455
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0864455
kb_number: KB0864455
last_modified: 2024-04-08
---

## SLA Definition was deleted. Undeleting does not address empty column values for Task SLAs. How can this be corrected?

  

### Issue

The user had many task SLAs with the "SLA Definition" column empty. They wanted to know why.

### Cause

Another user had deleted the SLA Definition. Hence, the task SLAs that existed for that SLA Definition could not reference the SLA Definition, rendering the "SLA Definition" column value as blank.

### Resolution

Even after the user was able to go to the Deleted Records module and "undelete" the SLA Definition, upon trying to run Repair SLAs against the affected task SLAs, the "SLA Definition" column did not return its original value on any of the task SLAs.

Understandably, the user wanted to know how to correct this. 

It was recommended, as there were 200k+ affected task SLA records, that the user write a custom script to query against the full list of affected task SLAs and script in the correct value for the "SLA Definition" column. They were counseled to place this script inside of a Scheduled Job and run it during off-business hours. 

The user did this, and all of the task SLAs were corrected perfectly.
