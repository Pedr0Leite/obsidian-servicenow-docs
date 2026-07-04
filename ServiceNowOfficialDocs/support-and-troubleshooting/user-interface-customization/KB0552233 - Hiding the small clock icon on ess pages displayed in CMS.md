---
title: "Hiding the small clock icon on ess pages displayed in CMS"
aliases:
  - KB0552233
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0552233
kb_number: KB0552233
last_modified: 2024-01-28
---

## Hiding the small clock icon on ess pages displayed in CMS

  

### Issue

Hiding the small clock icon displayed on CMS pages

Problem

* * *

At the bottom right of CMS site pages there is a small clock icon displaying response times:  
  
![](/sys_attachment.do?sys_id=c68aec66db42b450e515c2230596191c)  

This article explains how to hide the icon.

Cause

* * *

This icon is called the [Response Time Indicator](https://docs.servicenow.com/csh?topicname=c_ResponseTimeIndicator.html&version=latest "Response Time Indicator"). The icon has a default value of true:  
  
![](/sys_attachment.do?sys_id=568aec66db42b450e515c22305961960)

  
Resolution

* * *

Administrators can disable the **Response Time Indicator** clock icon by setting the glide.ui.response\_time system property to false.

1.  Navigate to **System Properties > All Properties**.
2.  Search for glide.ui.response\_time.
3.  Update the **Value** to **false**.
4.  Save the record.
