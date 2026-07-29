---
title: "Linux Server pattern discovery is failing with an error as \"java.lang.ClassCastException: java.lang.String cannot be cast to java.util.Map\"
aliases:
  - KB0725051
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0725051
kb_number: KB0725051
last_modified: 2024-04-07
---

## Linux Server pattern discovery is failing with an error as "java.lang.ClassCastException: java.lang.String cannot be cast to java.util.Map"

  

### Issue

# Symptoms

* * *

Linux Server pattern discovery is failing with an error as "java.lang.ClassCastException: java.lang.String cannot be cast to java.util.Map"

# Release

* * *

Before London.

# Cause

* * *

"Linux Server" Pattern, Step 13.82: "Merge proc\_mount and file systems" would fail with below exception if the $prodMounts variable is empty.

java.lang.String cannot be cast to java.util.Map   
java.lang.ClassCastException: java.lang.String cannot be cast to java.util.Map

# Resolution

* * *

Update "Linux Server" pattern step 13.82 by adding a precondition as shown below. This precondition would skip this step if the **$procMounts** is empty.  
This has been already been fixed in London release.

![](sys_attachment.do?sys_id=701ffce2db0ab450e515c223059619e5)
