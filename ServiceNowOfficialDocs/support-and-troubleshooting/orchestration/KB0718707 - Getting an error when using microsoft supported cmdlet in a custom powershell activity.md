---
title: "Getting an error when using microsoft supported cmdlet in a custom powershell activity"
aliases:
  - KB0718707
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0718707
kb_number: KB0718707
last_modified: 2024-04-07
---

## Getting an error when using microsoft supported cmdlet in a custom powershell activity

  

### Issue

Orchestration activity may fail with error:

"Parameter cannot be processed because the parameter name <xxxxx> is ambiguous"

### Release

All

### Cause

* * *

1.  Parameter name passed in the command is incorrect.

#   

### Resolution

1.  If you see a similar symptom, it's better to start with the powershell documentation for the cmdlet.
2.  In this case, 'Add-ADGroupMember' cmdlet was leveraged in the activity. In the command, the parameter name passed was '-Member'. According to powershell documentation for the cmdlet, '-Members' is the correct parameter.
3.  After correcting the parameter name, the activity completed successfully.
