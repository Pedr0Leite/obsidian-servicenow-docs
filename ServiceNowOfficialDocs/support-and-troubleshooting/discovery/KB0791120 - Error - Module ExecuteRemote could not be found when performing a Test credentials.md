---
title: " Error - Module ExecuteRemote could not be found when performing a Test credentials"
aliases:
  - KB0791120
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0791120
kb_number: KB0791120
last_modified: 2026-05-22
---

## Error - Module ExecuteRemote could not be found when performing a Test credentials

  

### Issue

Testing the credentials in the instance is failing with an error "Module ExecuteRemote could not be found".

**Steps to reproduce**

Navigate to any discovery credentials & click on Test credential. You will see an error message.

### Release

All Releases

### Cause

This is because of missing MID Server script files in the instance.

1\. ExecuteRemote

2\. ExecuteRemote.psm1

These files contains the script that needs to be executed while running credential test.

### Resolution

Import the script files from the OOTB instance or any other instance within same family.

You can find the files in below path:

From Filter navigator > MID Server > Script Files.
