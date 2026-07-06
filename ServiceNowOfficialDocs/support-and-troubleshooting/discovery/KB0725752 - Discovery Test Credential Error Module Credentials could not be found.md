---
title: "Discovery Test Credential Error \"Module Credentials could not be found\""
aliases:
  - KB0725752
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725752
kb_number: KB0725752
last_modified: 2024-04-07
---

## Discovery Test Credential Error "Module Credentials could not be found"

  

### Issue

When testing windows credentials, following error is thrown -> "Module Credentials could not be found"

### Release

All Versions.

### Cause

In the mid server script files, the Credentials module file was marked 'inactive'. 

### Resolution

1.  When we test the credentials, we leverage the functions defined in the Credentials module.   
    2\. After importing the OOB script with the correct name 'Credentials.psm1' under parent 'Credentials', the end-user was able to test the credentials.
