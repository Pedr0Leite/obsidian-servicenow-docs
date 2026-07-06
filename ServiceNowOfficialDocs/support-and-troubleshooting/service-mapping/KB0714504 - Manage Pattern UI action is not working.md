---
title: "Manage Pattern UI action is not working"
aliases:
  - KB0714504
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0714504
kb_number: KB0714504
last_modified: 2024-04-07
---

## Manage Pattern UI action is not working

  

### Issue

# Symptoms

* * *

Clicking on "Manage Pattern" button after opening the pattern will display "URL does not exist" message.

![](sys_attachment.do?sys_id=267c20aedb42b450e515c223059619bb)

![](sys_attachment.do?sys_id=f67c20aedb42b450e515c223059619c0)

# Release

* * *

Kingston and later versions

# Cause

* * *

When you click on "Manage Pattern" the URL that is redirected would look like: http://<Instance-name>.service-now.com/**$sw\_pattern\_debugger.do?........./**

Please observe the **$sw\_pattern\_debugger.do** in the URL. This is older version of the pattern debugger page and it is replaced by new version. This is the reason it fails to open.

# Resolution

* * *

The page **$sw\_pattern\_debugger.do** is replaced by '**$sn\_pattern\_designer.do**'. So the new URL would look like: http://<Instance-name>.service-now.com/**$sn\_pattern\_designer.do****?........./**  
  
The new version of the page can be used by navigating to Pattern Designer -> Discovery patterns. With this, pattern debugger should be opened properly.

# Additional Information

* * *

[Troubleshoot pattern-related mapping errors](https://docs.servicenow.com/csh?topicname=t_TBSMapProcess.html&version=latest "Troubleshoot pattern-related mapping errors")
