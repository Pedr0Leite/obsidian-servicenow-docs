---
title: "HR Case short description and other fields are blank"
aliases:
  - KB0794207
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0794207
kb_number: KB0794207
last_modified: 2025-09-03
---

## HR Case short description and other fields are blank

  

### Issue

HR (Human Resource) Case short description and other fields are blank

HR Case short description and other fields are not populated

Record Producer script for HR is not populating the values

### Release

Any

### Cause

HR script includes are customized

### Resolution

Revert the script include hr\_Utils to the out-of-box (OOB) version

If it is still the same issue, check all the HR script includes and see if anything are customized

Revert the customizations and test again
