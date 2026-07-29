---
title: "Discovery Tuxedo pattern error : Failed Exploring CI Pattern on Windows Hosts"
aliases:
  - KB0782857
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0782857
kb_number: KB0782857
last_modified: 2024-04-08
---

## Discovery Tuxedo pattern error : Failed Exploring CI Pattern on Windows Hosts

  

### Issue

Trying to discover a tuxedo application running on a Windows host fails executes the Tuxedo pattern and fails with the error 

```
Command result: '.' is not recognized as an internal or external command, operable program or batch file. 
```

### Cause

Tuxedo pattern has steps defined to run commands on a Linux terminal. When the pattern is called for discovering the application on a windows host it fails.

https://<instance-name>.service-now.com/nav\_to.do?uri=sa\_pattern.do?sys\_id=96f0186ea2684e35a14a7ca4aa97f163

### Resolution

```
In order to work around this, we need to add a condition in the Tuxedo Process classifier such that Horizontal probe for the "Tuxedo" pattern is not kicked off on windows machines. Go to "discovery_classy_proc" table and add an "AND" condition as follows.      1. On the drop down for the condition click on the "Show related fields"     2. Then in the drop down you will see the Computer -> Computer Fields. Click on that     3. Then add the condition " Operating System" "Does not contain" "Windows" and save. 
```
