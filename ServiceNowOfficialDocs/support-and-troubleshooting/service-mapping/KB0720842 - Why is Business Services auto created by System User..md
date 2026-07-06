---
title: "Why is Business Services auto created by System User."
aliases:
  - KB0720842
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0720842
kb_number: KB0720842
last_modified: 2024-04-07
---

## Why is Business Services auto created by System User.

  

### Issue

Why is Business Services auto created by System User.

### Release

Kingston and London

### Cause

Service Mapping uses load balancers on a network to identify possible Business Services (candidates), the business services created by 'system' user would be a result of approving the candidates by choosing map your services option from the service mapping home page.

  

![](/sys_attachment.do?sys_id=c35b2c6adb42b450e515c22305961930)

### Resolution

It is recommend to review while approving the candidates by choosing map your services option from the service mapping home page to avoid creation of undesired business services by 'system' users. 

For more information refer to product document:

[https://docs.servicenow.com/csh?topicname=map-business-services-in-bulk.html&version=latest](https://docs.servicenow.com/csh?topicname=map-business-services-in-bulk.html&version=latest)
