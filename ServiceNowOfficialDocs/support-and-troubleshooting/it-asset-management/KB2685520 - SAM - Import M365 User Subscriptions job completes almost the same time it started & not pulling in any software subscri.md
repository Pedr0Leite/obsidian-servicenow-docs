---
title: "\"SAM - Import M365 User Subscriptions\" job completes almost the same time it started & not pulling in any software subscriptions"
aliases:
  - KB2685520
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2685520
kb_number: KB2685520
last_modified: 2026-03-27
---

## "SAM - Import M365 User Subscriptions" job completes almost the same time it started & not pulling in any software subscriptions

  

### Issue

"SAM - Import M365 User Subscriptions" job not pulling in any software subscriptions, and also this job completes almost the same time it started  
  
  

### Symptoms

1\. Observe that this job 'SAM - Import M365 User Subscriptions' completes but it completes almost the same time it started.  
https://<instance\_name>.service-now.com/samp\_job\_log\_list.do?sysparm\_query=nameSTARTSWITHSAM%20-%20Import%20M365%20User%20Subscriptions  
  
2\. No outbound http requests and no system logs been captured at the time the job was completed.  
  
3\. Plugin: Software Asset Management - SaaS License Management is installed and on latest version "16.0.8"

### Release

Zurich

### Cause

Missing rest message which enables to send requests to a REST web service endpoint. This field should be auto populated when you create integration profile.

Business Rule responsible for the same:  
https://<instance\_name>.service-now.com/sys\_script.do?sys\_id=2f0e872a8730030067b5ed4d87cb0bab

![](/sys_attachment.do?sys_id=c0ced9c3477b761cb8a4aa25126d43c4 "Screenshot 1.png")

### Resolution

Delete and create the new M365 integration profile that populates the rest message field which enables to send requests to a REST web service endpoint.

Please refer to the product documentation below.  
[https://www.servicenow.com/docs/csh?topicname=set-up-microsoft-office-365.html&version=latest](https://www.servicenow.com/docs/csh?topicname=set-up-microsoft-office-365.html&version=latest)
