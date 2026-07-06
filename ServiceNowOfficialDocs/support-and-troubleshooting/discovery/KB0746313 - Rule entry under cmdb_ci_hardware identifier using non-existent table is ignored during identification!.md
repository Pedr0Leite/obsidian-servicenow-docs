---
title: "Rule entry under cmdb_ci_hardware identifier using non-existent table is ignored during identification!"
aliases:
  - KB0746313
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0746313
kb_number: KB0746313
last_modified: 2024-04-07
---

## Issue

# Symptoms

Error Message: Rule entry under cmdb\_ci\_hardware identifier using non-existent table is ignored during identification!

Error Message: Rule entry under cmdb\_ci\_storage\_server identifier using non-existent table is ignored during identification!   
Error Message: Rule entry under cmdb\_ci\_virtualization\_server identifier using non-existent table is ignored during identification! 

# Release

All releases

# Cause

OOTB the lookup based identification rule requires the reference field to point to cmdb\_ci for correct identification of the CI but in the cmdb\_ci\_network\_adapter table, we do not have any field referencing to the CMDB and so we are seeing this error. 

# Resolution

This because of no reference field between the table \[cmdb\_ci\_network\_adapter\] to the parent table \[cmdb\_ci\] Configuration Item.

Check for the sys dictionary and see if they have removed "Configuration Item" in the reference field for Network Adapter
