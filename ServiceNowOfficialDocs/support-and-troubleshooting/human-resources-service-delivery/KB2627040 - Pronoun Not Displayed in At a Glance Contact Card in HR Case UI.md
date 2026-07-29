---
title: "Pronoun Not Displayed in \"At a Glance\" Contact Card in HR Case UI"
aliases:
  - KB2627040
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2627040
kb_number: KB2627040
last_modified: 2026-01-03
---

## Pronoun Not Displayed in "At a Glance" Contact Card in HR Case UI

  

### Issue

Employee pronoun does not appear next to their name in the "At a glance" contact card within the HR case UI.

Data resources were configured in UI Builder to fetch pronoun information from the employee profile table, but the pronoun did not display as expected.

### Release

Xanadu

### Cause

The data broker in UI Builder was set to EAGER evaluation, causing it to run without the correct subject person `sys_id`.

This resulted in incorrect or random employee data being returned.

### Resolution

1.  Change the data broker evaluation mode from EAGER to EXPLICIT in UI Builder.
2.  Add an event handler to refresh the data broker after the record data is successfully fetched, ensuring the correct `sys_id` is used.
3.  Validate that the pronoun field is correctly mapped in the data resource and bound to the UI component.
4.  Clear UI Builder cache and refresh the page to apply changes.
