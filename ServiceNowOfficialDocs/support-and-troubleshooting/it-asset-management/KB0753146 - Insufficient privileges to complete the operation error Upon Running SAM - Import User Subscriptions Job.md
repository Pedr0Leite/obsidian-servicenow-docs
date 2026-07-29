---
title: "\"Insufficient privileges to complete the operation\" error Upon Running \"SAM - Import User Subscriptions\" Job"
aliases:
  - KB0753146
tags:
  - servicenow
  - support-kb
source_url: https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0753146
kb_number: KB0753146
last_modified: 2026-04-13
---

## "Insufficient privileges to complete the operation" error Upon Running "SAM - Import User Subscriptions" Job

  

### Issue

Running the "**SAM - Import User Subscriptions**" job results in the following error in the syslog:

Unhandled exception for profile : 682ce3251b1ab740ee510d43cd4bcb64 : Error: {   
  "error": {   
    "code": "Authorization\_RequestDenied",   
    "message": "Insufficient privileges to complete the operation.",   
    "innerError": {   
      "request-id": "d5471515-74a7-4028-a8bc-74abd13c7dee",   
      "date": "2019-06-27T20:23:05"   
    }   
  }   
}

### Release

Madrid

### Cause

The **user.read.all**, **reports.read.all** permissions were given as delegated permissions, the API call won't work. You need to explicitly give app permissions, which are not selected by default in the Azure portal.

### Resolution

For the latest information on this topic, see [Integrating with Microsoft Dynamics 365 and Power Apps](https://docs.servicenow.com/csh?version=latest&topicname=integrating-with-microsoft365.html&pubname=tokyo-it-asset-management).

These screenshots show the permission needed on the Azure portal:

![](/sys_attachment.do?sys_id=853c8ae01ba1e1d0c16b43f6fe4bcb14)

![](sys_attachment.do?sys_id=893c8ae01ba1e1d0c16b43f6fe4bcb10)
