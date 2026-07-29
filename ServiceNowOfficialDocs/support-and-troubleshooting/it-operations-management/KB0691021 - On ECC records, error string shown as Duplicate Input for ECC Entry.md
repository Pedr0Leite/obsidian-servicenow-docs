---
title: "On ECC records, error string shown as  \"Duplicate Input for ECC Entry\"
aliases:
  - KB0691021
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0691021
kb_number: KB0691021
last_modified: 2024-04-07
---

## On ECC records, error string shown as "Duplicate Input for ECC Entry"

  

### Issue

# Symptoms

* * *

When you are running a Discovery, we do see the duplicate ECC entries.On ECC records, error string is  "Duplicate Input for ECC Entry".

![](sys_attachment.do?sys_id=74cef8a2db0ab450e515c2230596198e)

# Release

* * *

All version. When you are working with Multiple MID Server there is a chance to encounter this issue.

# Cause

* * *

 If there are two services that are pointed to same MID Server then we can see this behavior.

The configurations for the  MID server looks good from ServiceNow end.

# Resolution

* * *

Login to the MID Server Host machine  
Check for Services   
Check if there are more than one Service that is pointed to the same Config file, please  
If Yes, delete one of them and run the discovery again.  
  
  
  
If you are using Windows os, please see the docs: :[https://www.wikihow.com/Open-Windows-Services  
I](https://www.wikihow.com/Open-Windows-Services)f you are Linux os, please see the docs :[http://www.lostsaloon.com/technology/how-to-list-all-services-in-linux/](http://www.lostsaloon.com/technology/how-to-list-all-services-in-linux/)
