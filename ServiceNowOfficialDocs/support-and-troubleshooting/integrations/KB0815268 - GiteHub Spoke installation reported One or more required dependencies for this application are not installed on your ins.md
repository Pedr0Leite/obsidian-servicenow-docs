---
title: "GiteHub Spoke installation reported  \"One or more required dependencies for this application are not installed on your instance\" error."
aliases:
  - KB0815268
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0815268
kb_number: KB0815268
last_modified: 2024-04-08
---

## GiteHub Spoke installation reported "One or more required dependencies for this application are not installed on your instance" error.

  

### Issue

Unable to install GitHub Spoke Integration.

The following dependency error is reported:

![](/sys_attachment.do?sys_id=4495bc8ddbccb8d066e0a345ca961956)

### Resolution

1) Verify the status of the Application dependencies (these are just right below to the error displayed):

com.glide.hub.dynamic\_inputs  
com.glide.hub.action\_type.datastream  
com.glide.hub.integartion.runtime  
com.glide.hub.action\_step.rest  
Complex Object

  
1.2) On this specific case, the application dependency 'com.glide.hub.dynamic\_inputs' and application dependency 'com.glide.hub.action\_type.datastream' are not installed:

  
![](/sys_attachment.do?sys_id=cc95bc8ddbccb8d066e0a345ca961971)  
  
2) Select application's dependencies:  
com.glide.hub.dynamic\_inputs  
com.glide.hub.action\_type.datastream

  
3) Click the Install button.  
  
  

### Related Links

[GitHub spoke](https://docs.servicenow.com/csh?topicname=github-spoke.html&version=latest "GitHub spoke")
