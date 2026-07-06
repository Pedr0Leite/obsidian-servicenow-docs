---
title: "VCenter Event Collector context gets an \"Exception Null\" when you run test parameter upon configuration of event collector"
aliases:
  - KB0722443
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0722443
kb_number: KB0722443
last_modified: 2024-04-07
---

## Issue

# Symptoms

* * *

When you click on test parameters UI action on the vCenter event collector context, you will see an alert pop up saying Exception Null as shown in the attached screenshot.

#   
![](sys_attachment.do?sys_id=264c646edb42b450e515c2230596191e)  
  
  
  
  
  
  
  
  
  
  
  
  
  
Release

* * *

Any

# Cause

* * *

1)If you look at the exception stack trace in the mid server logs, you can observe that it is throwing exceptions when trying to access the vCenter. 

2) If an instance has multiple VMware type credentials, the credential specific to this vCenter might have a higher order .i.e lower priority than other VMware credentials. Hence the collector context will use the wrong credentials and fails

# Resolution

* * *

 1) Make sure the VMware credential is tested and validated.

2) Make sure the related VMware credential has lower order than other VMware type credentials which means higher priority.
